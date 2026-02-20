# Translation Service — Requirements Exploration

## Status: DRAFT — Partial Requirements Locked

---

## 1. Feature Summary

Add a "Translate" tab to all lesson pages in learn-app (alongside Full Lesson and Summary) that translates lesson content into 7 languages using DeepSeek, with caching and quality controls.

**Target languages**: Urdu, Hindi, French, German, Spanish, Chinese (Simplified), Arabic

---

## 2. Existing Architecture Context

### What Exists Today

| Component              | Technology                              | Key Pattern                                                                                                                                                   |
| ---------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **learn-app**          | Docusaurus + React                      | 2 tabs (Full Lesson, Summary). Summary is static build-time from `.summary.md` files. Auth via `useAuth()` hook.                                              |
| **study-mode-api**     | FastAPI + DeepSeek + Redis + PostgreSQL | ChatKit-based tutoring. DeepSeek called via OpenAI-compatible client. Redis for content caching (30-day TTL). GitHub raw content fetching. JWT auth via JWKS. |
| **token-metering-api** | FastAPI + Redis + PostgreSQL            | Balance checking, reservation via Lua scripts, audit trail. Prometheus metrics. Rate limiting.                                                                |

### Key Observations

1. **Summary tab is static** — built at build time from `.summary.md` files, NOT generated via API. This is different from what the other session assumed.
2. **Study-mode-api already has**: DeepSeek client, Redis caching, content loading from GitHub, JWT auth, rate limiting
3. **Token-metering-api already has**: PostgreSQL with SQLModel, Redis Lua scripts, Prometheus metrics, structured error handling, admin endpoints
4. **No R2 storage exists** in either service currently
5. **learn-app has minimal i18n** — only `["en"]` locale configured, used only for date formatting

---

## 3. Architecture Decision: Extend vs. New Service

### Option A: Extend study-mode-api

**Pros:**

- Reuses DeepSeek client, Redis, auth, content loader
- Fewer moving parts to deploy
- Single service to maintain

**Cons:**

- study-mode-api is already complex (ChatKit, agents, metering hooks, rate limiting)
- Translation is a distinct domain (caching strategy, content hashing, language management)
- Coupling translation lifecycle to study-mode releases
- study-mode-api has 20 msg/24hr rate limit — translation needs different limits
- If translation has issues, it affects tutoring availability

### Option B: New translation-api service (User's preference)

**Pros:**

- Clean separation of concerns
- Independent scaling (translation can be CPU/memory heavy with long content)
- Independent release cycle
- Can optimize caching strategy specifically for translations (longer TTLs, R2 cold storage)
- Can have its own rate limits, metrics, health checks
- Failure isolation — translation down doesn't affect tutoring
- Can copy proven patterns from both services (best of both worlds)

**Cons:**

- More infrastructure to maintain (another Dockerfile, deployment, monitoring)
- Code duplication for auth, Redis setup, config management
- Additional service in the Nx monorepo

### Option C: Shared library + new service (Hybrid)

**Pros:**

- Extract common code (auth, Redis, config) into a shared lib
- New service stays lean, only translation logic
- Reduces duplication across all three services

**Cons:**

- Larger refactor scope
- Shared lib versioning complexity
- Not necessary for MVP

**Recommendation**: Option B for now, with shared lib extraction as future optimization.

---

## 4. OPEN QUESTIONS — Business Requirements

These need answers before we can write a proper spec:

### Q1: Translation Scope

- **Full lesson content only?** Or also: page titles, navigation, sidebar, UI strings?
- **Code blocks**: Keep code in English (standard practice) or translate comments within code?
- **MDX components**: What happens with interactive components (Try With AI, quizzes, OSTabs)?
- **Images/diagrams**: Translate alt text? Recreate diagrams?

### Q2: Translation Trigger — DECIDED

**Answer: On-demand with R2 cache-aside pattern.**

```
User clicks Translate tab → API call
  → Check Redis hot cache
    → HIT:  Return cached (fastest, ~50ms, no hash verification)
  → Check R2 persistent store + verify source hash via GitHub
    → HIT + fresh: Promote to Redis, return (~150ms)
    → HIT + stale: Regenerate via DeepSeek → Store in R2 → Return
  → MISS: Generate via DeepSeek → Store in R2 + Redis → Return (slow first time, ~5-15s)
```

- First user for a lesson+language pays the latency cost
- All subsequent users get R2-cached response
- No batch pre-generation needed
- R2 is persistent (survives Redis evictions, cheap at $0.015/GB/month)

### Q3: Quality & Review

- **Machine-only**: DeepSeek translates, no human review?
- **Community review**: Allow users to report/suggest fixes?
- **Professional review**: Queue for human translators?
- **Quality metrics**: How do we measure translation quality?

### Q4: Access Control — DECIDED

**Answer: Free for authenticated users, rate-limited to prevent abuse.**

- No token metering integration (translations don't cost user credits)
- Rate limit: ~20 translations/day per user (configurable)
- Authentication required (same JWT/JWKS as other services)
- Unauthenticated users see locked Translate tab (same pattern as Summary tab)

### Q5: Content Freshness — DECIDED

**Answer: Hash-based automatic invalidation.**

- Store SHA256 of source content alongside translation in R2
- **Cache-first flow**: Redis hits return immediately (no hash check, up to 24hr stale)
- R2 hits verify hash: fetch source → compute hash → compare with stored hash
- If hash matches → promote to Redis, return cached translation (fast)
- If hash differs → regenerate via DeepSeek → overwrite in R2 → return
- If GitHub unreachable → serve stale R2 translation with `source_unavailable` flag
- No webhooks needed, no manual intervention
- Trade-off: Redis allows up to 24hr staleness for speed; R2 layer guarantees freshness

### Q6: Caching & Storage — DECIDED

**Answer: R2 as primary persistent store, Redis as optional hot cache.**

```
Storage tiers:
  L1: Redis (optional hot cache, 24hr TTL) — fast repeated access
  L2: R2 (primary store, persistent) — cheap, durable, ~100ms access
  L3: DeepSeek generation (on cache miss) — 5-15s, costs ~$0.002/lesson
```

- R2 key structure: `translations/{lesson_path}/{lang}.json`
- JSON payload: `{ content_hash, translated_content, model, created_at }`
- Content hash enables invalidation when source lesson changes
- PostgreSQL for metadata/tracking only — NOT for storing translated content
- DB tracks: who requested what (user_id, lesson_path, target_lang, content_hash, timestamp)
- Enables analytics: which lessons/languages are most requested, who's using it

### Q7: RTL Support

- **Urdu and Arabic need RTL layout**
- **Code blocks stay LTR within RTL context**
- **Mixed content**: How to handle inline code in RTL paragraphs?

### Q8: Cost & Scale

- **~400 lessons × 7 languages = 2,800 translations**
- **DeepSeek cost**: ~$0.002 per lesson = ~$5.60 total for full book
- **Acceptable latency**: How long can user wait for first translation?
- **Concurrent translations**: Expected peak load?

### Q9: Technical Glossary — DECIDED

**Answer: Let DeepSeek decide per language context.**

- No maintained glossary for MVP
- DeepSeek naturally keeps English tech terms in languages where that's convention
- Prompt will instruct: "Keep code, variable names, and file paths in English. For technical terms, use the convention natural to {target_language}."
- Brand terms ("Agent Factory", "Panaversity") — instruct to keep in English
- Can add glossary support later if quality issues arise

### Q10: Integration with Token Metering

- **Should translation requests go through metering** (reserve → deduct)?
- **Different pricing per language** (some languages harder to translate)?
- **Or flat-rate / free** since it's educational content?

---

## 5. Proposed Architecture (Pending Requirements)

```
┌─────────────────────────────────────────────────────────────────┐
│                    FRONTEND (learn-app)                          │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ LessonContent Tabs:                                       │  │
│  │   [Full Lesson] [Summary] [Translate]                     │  │
│  │                                                           │  │
│  │ TranslateTab:                                             │  │
│  │  - LanguageSelector (7 languages, with native names)      │  │
│  │  - TranslatedContent (ReactMarkdown, RTL-aware)           │  │
│  │  - LoadingState / CacheIndicator                          │  │
│  │  - Error state handling                                    │  │
│  └───────────────────────────────────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────────┘
                           │ POST /api/v1/translate
┌──────────────────────────▼──────────────────────────────────────┐
│               TRANSLATION-API (New Service)                      │
│  Port: 8002                                                      │
│                                                                  │
│  Routes:                                                         │
│    POST /api/v1/translate          ← Translate lesson content    │
│    GET  /api/v1/languages          ← List supported languages    │
│    POST /admin/invalidate-cache    ← Clear cached translations   │
│    GET  /health                    ← Health check                │
│    GET  /metrics                   ← Prometheus metrics           │
│                                                                  │
│  Copied from study-mode-api:                                     │
│    - DeepSeek client setup (OpenAI-compatible)                   │
│    - Redis caching layer                                         │
│    - JWT auth (JWKS verification)                                │
│    - Content loader (GitHub raw fetch)                            │
│    - Config management (pydantic-settings)                       │
│                                                                  │
│  Copied from token-metering-api:                                 │
│    - PostgreSQL + SQLModel setup                                 │
│    - Structured error handling                                   │
│    - Prometheus metrics                                          │
│    - Rate limiting (slowapi)                                     │
│    - Docker multi-stage build                                    │
│    - Test infrastructure (in-memory SQLite)                      │
│                                                                  │
│  New/Unique:                                                     │
│    - Translation prompt engineering                              │
│    - Content chunking (split long lessons)                       │
│    - Content hash-based cache invalidation                       │
│    - RTL content handling                                        │
│    - R2 persistent blob storage (aioboto3)                        │
│                                                                  │
│  Core Flow:                                                      │
│    Request → Redis(hot) → R2(persistent) → DeepSeek(generate)   │
│                                                                  │
│  Infrastructure:                                                 │
│    ┌──────────┐  ┌───────┐  ┌────┐  ┌────────────┐             │
│    │ DeepSeek │  │ Redis │  │ R2 │  │ PostgreSQL │              │
│    │ (LLM)   │  │(hot$) │  │($$)│  │ (metadata) │              │
│    └──────────┘  └───────┘  └────┘  └────────────┘             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. Data Model (Draft)

### R2 Storage (translated content blobs)

```
Key:    translations/{lesson_path}/{lang_code}.json
Value:  {
  "content_hash": "sha256_of_source",    # For invalidation
  "translated_content": "# Markdown...",   # The actual translation
  "model": "deepseek-chat",
  "tokens_used": 1234,
  "created_at": "2026-02-05T..."
}
```

### PostgreSQL (metadata/tracking only)

```python
# Request log — who requested what, enables analytics
class TranslationRequest(SQLModel, table=True):
    id: int | None
    user_id: str              # Who requested
    lesson_path: str          # What lesson
    target_lang: str          # "ur", "hi", "fr", "de", "es", "zh", "ar"
    content_hash: str         # Source content hash at time of request
    cache_source: str         # "redis", "r2", or "generated"
    generation_time_ms: int | None  # How long DeepSeek took (null if cache hit)
    created_at: datetime

# Supported languages: hardcoded list in config (not DB-managed for MVP)
# See spec §5 GET /api/v1/languages for the static list
```

---

## 7. Files to Copy/Adapt

### From study-mode-api → translation-api

| Source File                  | Adapt For                                                                 |
| ---------------------------- | ------------------------------------------------------------------------- |
| `config.py`                  | Add translation-specific settings (supported languages, chunk size, etc.) |
| `auth.py`                    | Copy as-is (same JWT/JWKS pattern)                                        |
| `core/redis_cache.py`        | Adapt TTLs for translation caching (longer: days not hours)               |
| `services/content_loader.py` | Reuse GitHub content fetching                                             |
| `fte/ask_agent.py`           | Copy DeepSeek client setup only (not the agent framework)                 |

### From token-metering-api → translation-api

| Source File           | Adapt For                                       |
| --------------------- | ----------------------------------------------- |
| `core/database.py`    | Copy PostgreSQL async setup with SSL handling   |
| `core/exceptions.py`  | Copy structured error handling pattern          |
| `core/metrics.py`     | Adapt Prometheus metrics for translation domain |
| `core/rate_limit.py`  | Copy rate limiting setup                        |
| `core/lifespan.py`    | Copy startup/shutdown pattern                   |
| `Dockerfile`          | Copy multi-stage build pattern                  |
| `docker-compose.yaml` | Adapt for translation service (port 8002)       |
| `tests/conftest.py`   | Copy test infrastructure                        |

---

## 8. Implementation Phases (Tentative)

### Phase 1: Scaffold & Core (Day 1-2)

- Create `apps/translation-api/` with copied infrastructure
- Set up FastAPI app, Redis, PostgreSQL, auth
- Nx project configuration
- Basic health endpoint working

### Phase 2: Translation Engine (Day 2-3)

- DeepSeek translation prompt engineering
- Content chunking for long lessons
- Translation caching (Redis hot + R2 persistent)
- Content hash-based invalidation

### Phase 3: API Endpoints (Day 3-4)

- POST /api/v1/translate
- GET /api/v1/languages
- POST /admin/invalidate-cache
- Rate limiting, error handling

### Phase 4: Frontend (Day 4-5)

- TranslateTab component
- LanguageSelector
- RTL support (Urdu, Arabic)
- Loading states, error handling

### Phase 5: Quality & Polish (Day 5-6)

- Glossary management
- Feedback mechanism
- Metrics & monitoring
- E2E testing

---

## 9. Next Steps

1. **Answer the 10 open questions** above to lock down requirements
2. **Write formal spec** at `specs/002-translation-service/spec.md`
3. **Create implementation plan** with task breakdown
4. **Start Phase 1**: Scaffold the service
