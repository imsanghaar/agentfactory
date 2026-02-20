# Translation Service — Technical Specification

## Status: READY FOR REVIEW

---

## 1. Overview

A new `translation-api` microservice that translates lesson content from English into 7 languages using DeepSeek, with R2 persistent caching and on-demand generation.

**Languages**: Urdu (ur), Hindi (hi), French (fr), German (de), Spanish (es), Chinese Simplified (zh), Arabic (ar)

**Frontend**: New "Translate" tab in LessonContent alongside Full Lesson and Summary.

---

## 2. Locked Decisions

| #   | Decision     | Answer                                                                       |
| --- | ------------ | ---------------------------------------------------------------------------- |
| D1  | Architecture | New `translation-api` service (separate from study-mode-api)                 |
| D2  | Trigger      | On-demand with R2 cache-aside (lazy generation)                              |
| D3  | Access       | Free for authenticated users, rate-limited (~20/day)                         |
| D4  | Storage      | R2 primary (content blobs), Redis hot cache, PostgreSQL metadata             |
| D5  | Invalidation | SHA256 content hash at R2 layer; Redis hot cache allows up to 24hr staleness |
| D6  | Glossary     | Let DeepSeek decide per language (no maintained glossary for MVP)            |
| D7  | Metering     | NOT integrated — translations are free (no token cost)                       |
| D8  | DB purpose   | Track requests for analytics (user_id, lesson_path, lang, hash)              |

---

## 3. Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                      FRONTEND (learn-app)                           │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ LessonContent Tabs:                                           │  │
│  │   [Full Lesson] [Summary] [Translate]                         │  │
│  │                                                               │  │
│  │ TranslateTab:                                                 │  │
│  │  - LanguageSelector (7 langs, native names, RTL indicators)   │  │
│  │  - TranslatedContent (rendered markdown, RTL-aware)           │  │
│  │  - Loading skeleton / progress indicator                      │  │
│  │  - ContentGate (locked for unauthenticated users)             │  │
│  └───────────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────────┘
                             │ POST /api/v1/translate
┌────────────────────────────▼────────────────────────────────────────┐
│                   TRANSLATION-API (New Service)                      │
│  Port: 8002                                                         │
│                                                                     │
│  Endpoints:                                                         │
│    POST /api/v1/translate        Translate lesson content            │
│    GET  /api/v1/languages        List supported languages            │
│    POST /admin/invalidate-cache  Clear cached translations           │
│    GET  /health                  Health check                        │
│    GET  /metrics                 Prometheus metrics                   │
│                                                                     │
│  Flow (cache-first):                                                │
│    Auth(JWT) → RateLimit → Redis(hot, skip hash)                    │
│      → R2(persistent) → GitHub(hash) → DeepSeek(generate)          │
│      → StoreR2 → CacheRedis → LogDB → Return                       │
│                                                                     │
│  Infrastructure:                                                    │
│    ┌──────────┐  ┌───────┐  ┌────┐  ┌────────────┐                 │
│    │ DeepSeek │  │ Redis │  │ R2 │  │ PostgreSQL │                  │
│    │  (LLM)   │  │ (hot) │  │($$)│  │ (metadata) │                  │
│    └──────────┘  └───────┘  └────┘  └────────────┘                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 4. Request Flow (POST /api/v1/translate)

```
1. JWT Authentication (JWKS verification, same as study-mode-api)
2. Rate limit check (20 requests/day per user_id from JWT `sub` claim, via slowapi with Redis backend)
3. Validate request (lesson_path, target_lang in supported set)
4. Check Redis hot cache (key: translate:{path}:{lang})
   → HIT: log to DB (cache_source="redis"), return cached, done
5. Check R2 persistent store (key: translations/{path}/{lang}.json)
   → HIT: proceed to step 6 for hash verification
   → MISS: proceed to step 6 for generation
6. Fetch source content from GitHub (reuse content_loader pattern, cached in Redis 1hr)
   → GitHub returns 404: return 404 "Lesson not found" (path is invalid)
   → GitHub unreachable/5xx + R2 had translation: return stale translation with source_unavailable=true
   → GitHub unreachable/5xx + no R2 translation: return 503 "Source content unavailable"
7. Compute SHA256 of source content
8. If R2 had translation AND hash matches:
   → Cache in Redis (24hr TTL), log to DB (cache_source="r2"), return
9. Generate translation via DeepSeek
   a. Strip MDX/JSX components, preserve only translatable markdown prose
   b. If content > chunk threshold (see §6): chunk by markdown headings
   c. Translate chunk(s) with structured prompt
   d. Reassemble if chunked
10. Store in R2 (with content_hash, model, timestamp metadata)
11. Cache in Redis (24hr TTL)
12. Log request to PostgreSQL (user_id, path, lang, content_hash, cache_source="generated", generation_time_ms, tokens_used)
13. Return translated content
```

**Key design choice:** GitHub fetch is deferred until after Redis and R2 cache lookups:

- **Redis hits** skip GitHub entirely (fastest path, no hash verification)
- **R2 hits** fetch GitHub to verify the content hash, then return if fresh
- **If GitHub is down** during an R2 hit, serve the stale R2 translation with `source_unavailable: true`
- Source content hash is cached in Redis (1hr TTL) to reduce GitHub calls on repeated R2 verifications

**Latency expectations:**

- Redis hit: ~50ms
- R2 hit: ~150ms
- Fresh generation (short lesson): ~5-8s
- Fresh generation (long lesson, chunked): ~10-20s

---

## 5. API Specification

### POST /api/v1/translate

**Request:**

```json
{
  "lesson_path": "01-General-Agents-Foundations/01-agent-factory-paradigm/01-welcome",
  "target_lang": "ur"
}
```

**Response (200):**

```json
{
  "translated_content": "# ایجنٹ فیکٹری پیراڈائم...",
  "target_lang": "ur",
  "direction": "rtl",
  "content_hash": "a1b2c3d4...",
  "cache_source": "r2",
  "model": "deepseek-chat",
  "generated_at": "2026-02-05T12:00:00Z",
  "source_unavailable": false
}
```

Field notes:

- `cache_source`: `"redis"` | `"r2"` | `"generated"` — where the translation came from
- `source_unavailable`: `true` when GitHub was unreachable and a stale R2 translation was returned. Clients should display a "translation may be outdated" notice. Default `false`.

**Error responses:**

- `401`: Missing/invalid JWT
- `404`: Lesson not found at path
- `422`: Invalid target_lang
- `429`: Rate limit exceeded (include `Retry-After` and `X-RateLimit-Remaining` headers)
- `503`: DeepSeek or GitHub unavailable (after retries), or R2 unavailable with no cached translation

**Rate limiting detail:**

- Key function extracts `sub` claim from verified JWT as the per-user key
- If JWT is valid but `sub` is missing (shouldn't happen, but defensive): fall back to IP-based limiting
- Limit: 20 requests/day per user (slowapi fixed window with Redis storage backend, same lib as token-metering-api)
- If Redis is unavailable: fail-open (allow request, log warning) — same as token-metering-api

### GET /api/v1/languages

**Response (200):**

```json
{
  "languages": [
    { "code": "ur", "name": "Urdu", "native_name": "اردو", "direction": "rtl" },
    {
      "code": "hi",
      "name": "Hindi",
      "native_name": "हिन्दी",
      "direction": "ltr"
    },
    {
      "code": "fr",
      "name": "French",
      "native_name": "Français",
      "direction": "ltr"
    },
    {
      "code": "de",
      "name": "German",
      "native_name": "Deutsch",
      "direction": "ltr"
    },
    {
      "code": "es",
      "name": "Spanish",
      "native_name": "Español",
      "direction": "ltr"
    },
    {
      "code": "zh",
      "name": "Chinese (Simplified)",
      "native_name": "简体中文",
      "direction": "ltr"
    },
    {
      "code": "ar",
      "name": "Arabic",
      "native_name": "العربية",
      "direction": "rtl"
    }
  ]
}
```

### GET /health

Reports service health with per-dependency status. Only R2 is strictly required — without it, no translations can be served or stored. All other dependencies are degraded-tolerant.

```json
{
  "status": "healthy",
  "dependencies": {
    "r2": "ok",
    "deepseek": "ok",
    "redis": "ok",
    "postgresql": "ok"
  }
}
```

- `"healthy"`: R2 up + DeepSeek up (full capability)
- `"degraded"`: R2 up but DeepSeek/Redis/PostgreSQL down (can serve cached translations, cannot generate new ones)
- `"unhealthy"`: R2 down (cannot serve or store anything)
- HTTP 200 for healthy/degraded, 503 for unhealthy only

### GET /metrics

Prometheus text format.

### POST /admin/invalidate-cache

Admin endpoint to clear cached translations. Requires `X-Admin-Secret` header matching the `ADMIN_SECRET` env var (same pattern as study-mode-api).

**Request:**

```json
{
  "lesson_path": "01-General-Agents-Foundations/01-agent-factory-paradigm/01-welcome",
  "target_lang": "ur"
}
```

Both fields optional:

- Both provided: invalidate specific lesson+language from Redis and R2
- Only `lesson_path`: invalidate all languages for that lesson
- Only `target_lang`: invalidate all lessons for that language
- Neither: invalidate entire cache (dangerous, requires confirmation header `X-Confirm-Full-Purge: true`)

**Response (200):**

```json
{
  "invalidated": { "redis_keys": 1, "r2_objects": 1 }
}
```

---

## 6. Translation Engine

### DeepSeek Configuration

```python
client = AsyncOpenAI(
    api_key=settings.deepseek_api_key,
    base_url="https://api.deepseek.com/v1",
)

# Model: deepseek-chat (DeepSeek-V3)
# Temperature: 0.3 (consistency over creativity)
# Timeout: 120s
#
# max_tokens is set dynamically per request:
#   - Estimated as 1.3x input token count (translation ≈ same length, plus overhead)
#   - Capped at 65536 (DeepSeek-V3 output limit)
#   - This avoids truncation for any lesson size
```

### Translation Prompt

```
You are a professional technical translator for educational programming content.

## Task
Translate the following lesson content from English to {language_name} ({language_code}).

## Rules
1. Preserve ALL markdown formatting exactly (headers, code blocks, bold, italic, links, lists, tables)
2. Keep ALL code examples, variable names, function names, file paths, and URLs in English
3. Keep brand terms in English: "Agent Factory", "Panaversity", "TutorsGPT"
4. Translate only human-readable prose, headings, and list descriptions
5. For technical terms (API, Docker, FastAPI, etc.), use the convention natural to {language_name}
6. Maintain the educational tone — clear, accessible, encouraging
7. Translate "Try With AI" section instructions but keep the prompt templates in English
8. Preserve YAML frontmatter keys in English, translate values where appropriate (title, description)
9. Do NOT add explanations, commentary, or translator notes
10. Output ONLY the translated markdown

## Content
{content}
```

### Chunking Strategy

Chunking threshold is driven by max_tokens output cap, not context window. Since translation output ≈ input length, we chunk when input exceeds ~24K tokens (leaving margin for the prompt and output expansion in verbose languages like German/Hindi).

1. **Preferred**: Translate full document in single call (most lessons are 5K-12K tokens — well under threshold)
2. **Split by `##` headings** if document exceeds 24K tokens
3. **Split by `###` headings** if any `##` section exceeds 24K tokens
4. **Paragraph boundary** as final fallback
5. **Atomic units** (never split): code blocks, tables, lists, blockquotes, Docusaurus admonitions
6. Each chunk includes its heading hierarchy for context
7. Reassemble in original order after translation

Token estimation: ~1 token per 4 characters for English, ~1 token per 2 characters for CJK/Arabic/Devanagari.

**Note:** MDX/JSX components (e.g., `<Tabs>`, `<Quiz>`, custom imports) are permanently stripped before translation. The translation operates on pure markdown only. Components are removed (not placeholdered, not restored) because the frontend renders translated content as plain markdown via react-markdown, which cannot handle JSX. If a lesson is heavily MDX-dependent, the translated version will contain only the prose and code portions.

---

## 7. Storage Architecture

### R2 (Primary — translated content blobs)

```
Bucket: tutorsgpt-translations

Key pattern:
  translations/{lesson_path}/{lang_code}.json

Example:
  translations/01-General-Agents-Foundations/01-agent-factory-paradigm/01-welcome/ur.json

Value:
{
  "content_hash": "sha256_of_english_source",
  "translated_content": "# ایجنٹ فیکٹری...",
  "model": "deepseek-chat",
  "tokens_used": 2450,
  "generated_at": "2026-02-05T12:00:00Z"
}
```

**R2 client**: `aioboto3` with S3-compatible API (Cloudflare R2 endpoint).

```python
session = aioboto3.Session()
async with session.client(
    "s3",
    endpoint_url=settings.r2_endpoint_url,      # https://<account_id>.r2.cloudflarestorage.com
    aws_access_key_id=settings.r2_access_key_id,
    aws_secret_access_key=settings.r2_secret_access_key,
    region_name="auto",
) as s3:
    await s3.put_object(Bucket=bucket, Key=key, Body=json.dumps(data))
    response = await s3.get_object(Bucket=bucket, Key=key)
    body = await response["Body"].read()
```

**R2 costs** (free tier): 10GB storage, 10M reads/month, 1M writes/month — more than sufficient for MVP.

### Redis (Hot cache — optional acceleration)

```
Key:    translate:{lesson_path}:{lang}
Value:  Full response JSON: { content_hash, translated_content, model, generated_at, direction }
TTL:    86400 (24 hours)
```

Redis stores the translation data fields. The `cache_source` and `source_unavailable` fields are NOT stored — they are injected at response time by the route handler (`cache_source="redis"`, `source_unavailable=false`).

Note: Redis key does NOT include content_hash (unlike R2) because Redis serves as a fast-path before we know the current source hash. The stored content_hash is checked lazily — if a Redis-cached translation's hash doesn't match the source (detected when source is later fetched for another reason), the Redis entry is invalidated. In practice, Redis TTL (24hr) handles most staleness naturally.

Redis is optional — if unavailable, flow falls through to R2. Same graceful degradation pattern as study-mode-api.

### PostgreSQL (Metadata/analytics only)

```python
class TranslationRequest(SQLModel, table=True):
    __tablename__ = "translation_requests"

    id: int | None = Field(default=None, primary_key=True)
    user_id: str = Field(index=True)
    lesson_path: str = Field(index=True)
    target_lang: str              # "ur", "hi", "fr", "de", "es", "zh", "ar"
    content_hash: str             # SHA256 of source at request time
    cache_source: str             # "redis", "r2", "generated"
    generation_time_ms: int | None  # null if cache hit
    tokens_used: int | None       # null if cache hit
    created_at: datetime = Field(default_factory=datetime.utcnow)
```

Enables analytics: most requested lessons, most popular languages, cache hit rates, generation costs.

---

## 8. Service Structure (Nx monorepo)

```
apps/translation-api/
├── src/translation_api/
│   ├── __init__.py
│   ├── main.py                    # FastAPI app, CORS, routes
│   ├── config.py                  # Pydantic Settings (env-based)
│   ├── core/
│   │   ├── auth.py                # JWT/JWKS (copied from study-mode-api)
│   │   ├── database.py            # SQLModel + AsyncPG (copied from token-metering-api)
│   │   ├── redis_cache.py         # Redis client (copied from study-mode-api)
│   │   ├── r2_client.py           # NEW: Cloudflare R2 via aioboto3
│   │   ├── rate_limit.py          # slowapi (copied from token-metering-api)
│   │   ├── metrics.py             # Prometheus (adapted from token-metering-api)
│   │   ├── lifespan.py            # Startup/shutdown
│   │   └── exceptions.py          # Structured errors
│   ├── models/
│   │   └── translation.py         # TranslationRequest SQLModel
│   ├── routes/
│   │   ├── translate.py           # POST /api/v1/translate
│   │   ├── languages.py           # GET /api/v1/languages
│   │   ├── admin.py               # POST /admin/invalidate-cache
│   │   └── health.py              # GET /health, GET /metrics
│   └── services/
│       ├── content_loader.py      # GitHub fetch (copied from study-mode-api)
│       ├── translation_engine.py  # DeepSeek translation + chunking
│       ├── cache_manager.py       # R2 + Redis cache-aside orchestration
│       └── request_logger.py      # PostgreSQL request logging
├── tests/
│   ├── conftest.py                # Fixtures (in-memory SQLite, mocked R2)
│   ├── test_translate.py          # API endpoint tests
│   ├── test_cache_manager.py      # Cache flow tests
│   ├── test_translation_engine.py # Chunking + prompt tests
│   └── test_content_loader.py     # GitHub fetch tests
├── project.json                   # Nx targets
├── pyproject.toml                 # Dependencies
├── Dockerfile                     # Multi-stage (python:3.12-slim)
├── docker-compose.yaml            # Local dev (postgres + redis)
└── README.md
```

### Nx project.json

```json
{
  "name": "translation-api",
  "targets": {
    "serve": {
      "command": "uv run uvicorn translation_api.main:app --reload --port 8002",
      "options": { "cwd": "apps/translation-api" }
    },
    "test": {
      "command": "uv run pytest tests/ -v --tb=short",
      "options": { "cwd": "apps/translation-api" },
      "cache": true,
      "inputs": [
        "{projectRoot}/src/**/*",
        "{projectRoot}/tests/**/*",
        "pythonInputs"
      ]
    },
    "test-coverage": {
      "command": "uv run pytest tests/ -v --tb=short --cov=src/translation_api --cov-report=term-missing --cov-fail-under=80",
      "options": { "cwd": "apps/translation-api" }
    },
    "lint": {
      "command": "uv run ruff check src/ tests/",
      "options": { "cwd": "apps/translation-api" },
      "cache": true,
      "inputs": [
        "{projectRoot}/src/**/*",
        "{projectRoot}/tests/**/*",
        "pythonInputs"
      ]
    },
    "format": {
      "command": "uv run ruff format src/ tests/",
      "options": { "cwd": "apps/translation-api" }
    },
    "format-check": {
      "command": "uv run ruff format --check src/ tests/",
      "options": { "cwd": "apps/translation-api" },
      "cache": true,
      "inputs": [
        "{projectRoot}/src/**/*",
        "{projectRoot}/tests/**/*",
        "pythonInputs"
      ]
    },
    "typecheck": {
      "command": "uv run mypy src/",
      "options": { "cwd": "apps/translation-api" },
      "cache": true,
      "inputs": ["{projectRoot}/src/**/*", "pythonInputs"]
    },
    "build": {
      "command": "docker build -t translation-api:latest .",
      "options": { "cwd": "apps/translation-api" }
    }
  }
}
```

### pyproject.toml dependencies

```toml
[project]
name = "translation-api"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.115.0",
    "uvicorn[standard]>=0.32.0",
    "pydantic>=2.10.0",
    "pydantic-settings>=2.6.0",
    "sqlmodel>=0.0.22",
    "sqlalchemy[asyncio]>=2.0.0",
    "asyncpg>=0.30.0",
    "redis>=5.0.0",
    "aioboto3>=13.0.0",        # R2 (S3-compatible) async client
    "openai>=1.50.0",           # DeepSeek (OpenAI-compatible)
    "python-jose[cryptography]>=3.3.0",
    "httpx>=0.28.0",
    "python-dotenv>=1.0.0",
    "prometheus-client>=0.21.0",
    "slowapi>=0.1.9",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3.0",
    "pytest-asyncio>=0.24.0",
    "pytest-mock",
    "pytest-cov",
    "aiosqlite>=0.20.0",
    "ruff>=0.8.0",
    "mypy>=1.13.0",
]
```

---

## 9. Frontend: TranslateTab Component

### Tab Integration

Extend existing `LessonContent` component with third tab:

```typescript
type TabType = "lesson" | "summary" | "translate";
const [activeTab, setActiveTab] = useState<TabType>("lesson");
```

Tab renders:

- **Authenticated**: `<TranslateTab lessonPath={path} />`
- **Not authenticated**: `<ContentGate type="translate">` (same lock pattern as Summary)

### TranslateTab Component

```typescript
interface TranslateTabProps {
  lessonPath: string;
}

// State:
// - selectedLang: string | null
// - translatedContent: string | null
// - isLoading: boolean
// - error: string | null
// - cacheSource: 'redis' | 'r2' | 'generated' | null

// Flow:
// 1. User selects language from dropdown
// 2. POST /api/v1/translate { lesson_path, target_lang }
// 3. Show loading skeleton (with "first time may take a moment" message)
// 4. Render translated content as plain markdown (NOT MDX)
//    - Use react-markdown or rehype for rendering (NOT Docusaurus MDX pipeline)
//    - MDX/JSX components are stripped server-side before translation
//    - Translated output is pure markdown: headings, paragraphs, code, lists, tables
//    - Apply RTL dir attribute if language requires it
// 5. Persist selected language in localStorage for return visits
```

### Language Selector

```typescript
const LANGUAGES = [
  { code: "ur", name: "Urdu", nativeName: "اردو", dir: "rtl" },
  { code: "hi", name: "Hindi", nativeName: "हिन्दी", dir: "ltr" },
  { code: "fr", name: "French", nativeName: "Français", dir: "ltr" },
  { code: "de", name: "German", nativeName: "Deutsch", dir: "ltr" },
  { code: "es", name: "Spanish", nativeName: "Español", dir: "ltr" },
  { code: "zh", name: "Chinese (Simplified)", nativeName: "简体中文", dir: "ltr" },
  { code: "ar", name: "Arabic", nativeName: "العربية", dir: "rtl" },
];
```

Dropdown shows: `nativeName (name)` — e.g., "اردو (Urdu)"

### RTL Support

```css
.translateContent[dir="rtl"] {
  direction: rtl;
  text-align: right;
}

/* Code blocks stay LTR in RTL context */
.translateContent[dir="rtl"] pre,
.translateContent[dir="rtl"] code {
  direction: ltr;
  text-align: left;
  unicode-bidi: isolate;
}

/* Tables stay LTR */
.translateContent[dir="rtl"] table {
  direction: ltr;
}

/* Inline code in RTL text needs bidi isolation */
.translateContent[dir="rtl"] p code,
.translateContent[dir="rtl"] li code {
  unicode-bidi: isolate;
  direction: ltr;
}
```

---

## 10. Configuration (Environment Variables)

```bash
# Core
ENVIRONMENT=development
DEV_MODE=false
PORT=8002

# Auth (same as study-mode-api)
SSO_URL=https://sso.example.com
JWKS_CACHE_TTL=3600
DEV_USER_ID=dev-user-001
ADMIN_SECRET=change-me-in-production  # For POST /admin/invalidate-cache

# DeepSeek
DEEPSEEK_API_KEY=sk-...
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
DEEPSEEK_MODEL=deepseek-chat
DEEPSEEK_TEMPERATURE=0.3
DEEPSEEK_MAX_TOKENS_CAP=65536  # Upper bound; actual max_tokens set dynamically as 1.3x input
DEEPSEEK_TIMEOUT=120

# R2
R2_ENDPOINT_URL=https://<account_id>.r2.cloudflarestorage.com
R2_ACCESS_KEY_ID=...
R2_SECRET_ACCESS_KEY=...
R2_BUCKET_NAME=tutorsgpt-translations

# Redis
REDIS_URL=redis://localhost:6379
REDIS_TRANSLATION_TTL=86400  # 24 hours

# PostgreSQL
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/translations

# GitHub (for content fetching)
GITHUB_REPO=panaversity/learn-agentic-ai
GITHUB_TOKEN=ghp_...

# Rate Limiting
RATE_LIMIT_PER_DAY=20

# Content
MAX_CHUNK_TOKENS=24000
CONTENT_CACHE_TTL=3600  # 1 hour for source content hash caching
```

---

## 11. Metrics (Prometheus)

```
# Counters
translation_requests_total{lang, cache_source, status}
translation_errors_total{lang, error_type}
translation_rate_limited_total

# Histograms
translation_generation_duration_seconds{lang}
translation_request_duration_seconds{lang, cache_source}

# Gauges
translation_cache_size_bytes{tier}  # redis, r2
```

---

## 12. Cost Analysis

| Item                                         | Cost                      |
| -------------------------------------------- | ------------------------- |
| Per lesson translation (avg 5K tokens)       | ~$0.002                   |
| Full book first-time (400 lessons x 7 langs) | ~$5.60                    |
| R2 storage (2,800 translations x ~10KB avg)  | ~28MB = free tier         |
| R2 reads (10M/month free)                    | Free for expected traffic |
| Redis (existing infrastructure)              | $0 incremental            |
| PostgreSQL (existing infrastructure)         | $0 incremental            |

After initial generation, ongoing cost is near-zero (only when source content changes).

---

## 13. What to Copy From Each Service

### From study-mode-api

| Source                       | Target                       | Adaptation                                 |
| ---------------------------- | ---------------------------- | ------------------------------------------ |
| `auth.py`                    | `core/auth.py`               | Copy as-is (same JWT/JWKS pattern)         |
| `core/redis_cache.py`        | `core/redis_cache.py`        | Change TTLs, add translation-specific keys |
| `services/content_loader.py` | `services/content_loader.py` | Copy GitHub fetch, adapt path resolution   |
| `config.py`                  | `config.py`                  | New settings (R2, translation-specific)    |
| `core/lifespan.py`           | `core/lifespan.py`           | Add R2 client init, remove ChatKit         |

### From token-metering-api

| Source                | Target                | Adaptation                               |
| --------------------- | --------------------- | ---------------------------------------- |
| `core/database.py`    | `core/database.py`    | Copy async SQLModel setup, SSL handling  |
| `core/exceptions.py`  | `core/exceptions.py`  | Rename to translation error types        |
| `core/rate_limit.py`  | `core/rate_limit.py`  | Change to per-day limit (not per-minute) |
| `core/metrics.py`     | `core/metrics.py`     | Translation-specific metrics             |
| `Dockerfile`          | `Dockerfile`          | Change port to 8002, package name        |
| `docker-compose.yaml` | `docker-compose.yaml` | Add R2 mock (MinIO) for local dev        |
| `tests/conftest.py`   | `tests/conftest.py`   | Copy SQLite fixtures, add R2 mock        |

### New (not copied)

| File                             | Purpose                                  |
| -------------------------------- | ---------------------------------------- |
| `core/r2_client.py`              | Cloudflare R2 async client via aioboto3  |
| `services/translation_engine.py` | DeepSeek translation + markdown chunking |
| `services/cache_manager.py`      | R2 + Redis cache-aside orchestration     |
| `services/request_logger.py`     | Async PostgreSQL request logging         |
| `routes/translate.py`            | Main translation endpoint                |
| `routes/languages.py`            | Language listing endpoint                |

---

## 14. Open Questions (Non-blocking for Phase 1)

| #   | Question                          | Default for MVP                                                           |
| --- | --------------------------------- | ------------------------------------------------------------------------- |
| Q1  | Translate MDX components?         | No — skip interactive components, translate prose only                    |
| Q3  | Quality review process?           | Machine-only for MVP, add feedback button later                           |
| Q7  | RTL edge cases?                   | Standard CSS dir="rtl", code stays LTR                                    |
| Q8  | First-request latency acceptable? | Yes, show clear loading UX with "generating..." message                   |
| Q11 | Request coalescing?               | Not for MVP — rare that two users hit same uncached lesson simultaneously |

---

## 15. Implementation Phases

### Phase 1: Service Scaffold (2 days)

- Create `apps/translation-api/` directory structure
- Copy infrastructure from both services (auth, DB, Redis, rate limit, metrics)
- Add R2 client (`aioboto3`)
- Nx project.json + pyproject.toml
- Dockerfile + docker-compose
- Health endpoint passing
- **Done when**: `pnpm nx serve translation-api` starts, `/health` returns 200

### Phase 2: Translation Engine (2 days)

- DeepSeek client with translation prompt
- Content loader (GitHub fetch with hash computation)
- Markdown chunking for long lessons
- Cache manager (R2 + Redis cache-aside)
- **Done when**: Unit tests pass for: single-chunk translation, multi-chunk translation, cache hit/miss

### Phase 3: API Endpoints + DB (1 day)

- POST /api/v1/translate (full flow)
- GET /api/v1/languages
- PostgreSQL request logging
- Rate limiting (20/day per user)
- Error handling (all error codes)
- **Done when**: Integration tests pass for full request flow

**Required test cases (Phase 3):**
- Health endpoint: healthy (all deps up), degraded (Redis down), unhealthy (R2 down)
- Redis hit returns full response schema (including `model`, `generated_at`, `direction`)
- GitHub 404 returns HTTP 404 (not 503)
- GitHub unreachable + R2 cache exists returns stale translation with `source_unavailable: true`
- GitHub unreachable + no R2 cache returns HTTP 503
- R2 hit with matching hash promotes to Redis and returns
- R2 hit with stale hash triggers regeneration
- Rate limit at 21st request returns 429 with `Retry-After`
- Admin invalidate-cache with valid secret clears Redis + R2
- Admin invalidate-cache with invalid secret returns 401

### Phase 4: Frontend (2 days)

- TranslateTab component
- Language selector with native names
- RTL CSS support
- Loading states and error handling
- ContentGate for unauthenticated users
- **Done when**: Tab renders, language selection works, translation displays correctly

### Phase 5: Quality & Polish (1 day)

- Prometheus metrics
- Docker build verification
- E2E manual testing across all 7 languages
- CI integration (Nx affected detection)
- **Done when**: CI passes, manual translation quality spot-checked for 3+ languages

---

## 16. Success Criteria

1. Authenticated user can click Translate tab, select a language, and see translated lesson content
2. First translation generates in < 20 seconds, subsequent loads in < 500ms (R2 cache)
3. When source content changes, next R2-layer request auto-regenerates translation (Redis may serve stale for up to 24hr)
4. Urdu and Arabic display correctly in RTL layout
5. Code blocks remain in English and LTR
6. Rate limit enforced at 20 translations/day per user
7. Service runs independently — study-mode-api unaffected by translation failures
8. Full book (400 lessons x 7 languages) costs < $10 to generate
