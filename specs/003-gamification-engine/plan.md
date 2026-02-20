# Execution Plan: Progress API Implementation (v4 — Final)

## Context

Gamification engine spec (`specs/003-gamification-engine/requirements.md`) and plan (`specs/003-gamification-engine/plan.md`) are complete. This plan covers **execution**: team structure, task sequencing, verification loops.

**v4 changes**: Fixed 5 issues from external review (F1-F5, D2-D3). No Alembic — tables via `create_all()`. Added preferences endpoint. Fixed GatedQuiz integration point.

---

## Review Decisions (Integrated Below)

| ID  | Decision                                                      | Impact                              |
| --- | ------------------------------------------------------------- | ----------------------------------- |
| A1  | **All tests use PostgreSQL** via Docker container (no SQLite) | conftest.py, test infrastructure    |
| A2  | Docusaurus `customFields` for progress-api URL                | Frontend API client config          |
| A3  | Fail-open: Redis miss → fall through to DB                    | core/cache.py pattern               |
| A4  | `ON CONFLICT DO NOTHING` for chapter auto-creation            | services/shared.py                  |
| C1  | `services/shared.py` with standalone async utilities          | DRY across quiz/lesson services     |
| C2  | `ProgressAPIException` with structured error codes            | core/exceptions.py                  |
| C3  | Badge definitions as Python dict constant                     | services/engine/badges.py           |
| C4  | Keep `services/engine/` subpackage                            | Module structure                    |
| T1  | PostgreSQL for ALL tests (Docker container)                   | Replaces SQLite entirely            |
| T2  | Exhaustive failure tests (~15 additional cases)               | Unit + integration tests            |
| T3  | Pydantic `Field()` validators on all inputs                   | schemas/\*.py                       |
| T4  | Dev mode + 3-4 mocked JWKS auth tests                         | tests/test_auth.py                  |
| P1  | SQLAlchemy `selectinload` for dashboard query                 | Models need `Relationship()` fields |
| P2  | `SELECT ... FOR UPDATE` on user_progress                      | Works natively with PG tests        |
| P3  | Denormalize `badge_count` in `user_progress`                  | Simpler leaderboard view            |
| P4  | No cache stampede mitigation (premature at 50k)               | Do nothing                          |

---

## Execution Model: Persistent Team

Use `TeamCreate` to create a `progress-api` team with shared task list. Two persistent teammates work in parallel, coordinated by task dependencies.

```
Team Lead (me)
  ├── backend-dev  (general-purpose, bypassPermissions)
  │     Scope: Python/FastAPI — scaffold, models, services, routes, tests
  │
  └── frontend-dev (general-purpose, bypassPermissions)
        Scope: TypeScript/React — types, API client, components, pages
```

### Parallelism Strategy

Backend-dev and frontend-dev overlap — while frontend finishes slice N, backend starts slice N+1:

```
Time →
backend-dev:  [Scaffold] → [Quiz BE] → [Lesson BE] → [Dashboard BE] → [Leaderboard BE]
                              ↓             ↓              ↓                ↓
me (verify):       V₀    →   V₁a   →     V₂a    →      V₃a     →       V₄a
                              ↓             ↓              ↓                ↓
frontend-dev:            [Quiz FE]  → [Lesson FE] → [Dashboard FE] → [Leaderboard FE]
                              ↓             ↓              ↓                ↓
me (verify):              V₁b    →      V₂b    →       V₃b      →       V₄b
```

Each V = verification gate. Nothing proceeds until the gate passes.

### Task Dependency Graph

```
Task 0:  Scaffold          (backend-dev)     → blocks everything
Task 1a: Quiz Backend      (backend-dev)     → blocked by 0
Task 1b: Quiz Frontend     (frontend-dev)    → blocked by 1a
Task 2a: Lesson Backend    (backend-dev)     → blocked by 1a (can overlap with 1b)
Task 2b: Lesson Frontend   (frontend-dev)    → blocked by 2a
Task 3a: Dashboard Backend (backend-dev)     → blocked by 2a (can overlap with 2b)
Task 3b: Dashboard Frontend(frontend-dev)    → blocked by 3a
Task 4a: Leaderboard BE    (backend-dev)     → blocked by 3a (can overlap with 3b)
Task 4b: Leaderboard FE    (frontend-dev)    → blocked by 4a
Task 5:  Preferences       (both)            → blocked by 4a (backend) + 3b (frontend)
```

---

## Verification Protocol (MANDATORY after every task)

**This is not optional. Every task passes through this gate before the next starts.**

### Backend Verification Gate

```bash
# 1. Tests pass (against real PostgreSQL via Docker)
pnpm nx test progress-api
# Expected: all green, 0 failures

# 2. Lint clean
pnpm nx lint progress-api
# Expected: no errors

# 3. Service starts
pnpm nx serve progress-api &
sleep 3

# 4. Health check
curl -s http://localhost:8002/health | python3 -m json.tool
# Expected: {"status": "healthy"} or similar 200 response

# 5. Endpoint smoke test (for slices with new endpoints)
# Quiz: curl -X POST http://localhost:8002/api/v1/quiz/submit -H "Content-Type: application/json" -d '{...}'
# Lesson: curl -X POST http://localhost:8002/api/v1/lesson/complete ...
# Progress: curl http://localhost:8002/api/v1/progress/me ...
# Leaderboard: curl http://localhost:8002/api/v1/leaderboard

# 6. Kill server
kill %1
```

### Frontend Verification Gate

```bash
# 1. TypeScript compiles
cd apps/learn-app && npx tsc --noEmit
# Expected: no errors

# 2. Build succeeds (catches runtime import errors)
pnpm nx build learn-app
# Expected: build completes

# 3. Spot-check: key files exist and are non-empty
ls -la apps/learn-app/src/lib/progress-types.ts
ls -la apps/learn-app/src/lib/progress-api.ts
ls -la apps/learn-app/src/components/progress/
```

### Failure Protocol

If ANY verification step fails:

1. Send specific error message to the teammate via `SendMessage`
2. Teammate fixes the issue
3. Re-run full verification gate
4. Only proceed after clean pass
5. If 3 fix attempts fail → escalate to user

---

## Branch Strategy

```
main → feat/progress-api
```

Single feature branch. Atomic commits after each verified task. One PR at the end.

---

## Task Definitions

### Task 0: Service Scaffold (backend-dev)

**Goal**: Empty FastAPI app that starts, connects to DB, passes health check. All models defined. Test infrastructure with real PostgreSQL.

**Instructions for teammate**:

- Copy+adapt pattern from `apps/token-metering-api/`
- Target directory: `apps/progress-api/`
- Source module: `src/progress_api/`
- Port: 8002

**Files to create**:

- `project.json` — Nx targets (serve, test, lint, typecheck, build). Port 8002.
- `pyproject.toml` — deps: fastapi, sqlmodel, asyncpg, redis, python-jose, pydantic-settings, testcontainers[postgres]. Dev: pytest, pytest-asyncio, ruff, mypy.
- `Dockerfile`, `docker-compose.yaml`, `.env.example`
- `src/progress_api/main.py` — FastAPI app with CORS, exception handler, router mounting
- `src/progress_api/config.py` — Settings (database, redis, sso, dev_mode, cache TTLs)
- `src/progress_api/core/database.py` — Async engine + session (PostgreSQL via asyncpg)
- `src/progress_api/core/auth.py` — JWKS + CurrentUser + `upsert_user_from_jwt()`
- `src/progress_api/core/cache.py` — Redis get/set/invalidate, fail-open (A3: if redis is None, skip cache)
- `src/progress_api/core/redis.py` — Redis connection (no Lua scripts needed)
- `src/progress_api/core/lifespan.py` — Startup/shutdown for DB + Redis
- `src/progress_api/core/exceptions.py` — `ProgressAPIException(status_code, error_code, message)` (C2)
- `src/progress_api/models/` — All 8 model files with SQLModel definitions:
  - `user.py` — User (with `Relationship()` fields for P1/selectinload)
  - `chapter.py` — Chapter + ChapterAlias
  - `quiz.py` — QuizAttempt
  - `lesson.py` — LessonCompletion
  - `progress.py` — UserProgress (include `badge_count: int = 0` per P3, and `lessons_completed: int = 0`)
  - `badge.py` — UserBadge
  - `activity.py` — ActivityDay
  - `__init__.py` — re-export all
- `src/progress_api/routes/health.py` — GET /health
- `tests/conftest.py` — **PostgreSQL via testcontainers** (T1):
  - Spin up PostgreSQL container at session scope
  - Create tables per test function (fresh schema)
  - `expire_on_commit=False`
  - `app.dependency_overrides[get_session]` pattern
  - `settings.dev_mode = True` for auth bypass
- `tests/test_health.py` — Health check test
- `tests/test_auth.py` — 3-4 auth tests with mocked JWKS (T4): valid JWT, expired, wrong audience, missing token

**Materialized view** (F1): SQLModel's `create_all()` only creates tables, NOT materialized views. The leaderboard materialized view MUST be created via raw SQL. Add a `create_materialized_views()` function called in lifespan AND a pytest fixture that creates it after `create_all()`. Without this, Task 4a tests will crash with `relation "leaderboard" does not exist`.

**Docker pre-flight** (F3): ALL tests require Docker (PostgreSQL via testcontainers). Add to Task 0 verification: `docker ps` must succeed. If Docker isn't running, every test fails — there is no SQLite fallback.

**No Alembic**: Tables created via `SQLModel.metadata.create_all()` in lifespan + raw SQL for materialized view. Alembic migrations are a Phase 2 concern for production deploys.

**project.json must use `uv run`** for all commands (matching token-metering-api pattern): `uv run pytest`, `uv run ruff`, `uv run uvicorn`.

**Do NOT copy from token-metering-api**: Lua scripts, Prometheus metrics, slowapi rate limiting, credit calculation logic.

**Key reference files to read**:

- `apps/token-metering-api/project.json` → adapt targets
- `apps/token-metering-api/pyproject.toml` → adapt deps
- `apps/token-metering-api/src/token_metering_api/main.py` → app structure
- `apps/token-metering-api/src/token_metering_api/core/` → all core modules
- `apps/token-metering-api/tests/conftest.py` → test infrastructure pattern (adapt from SQLite to PG)
- `specs/003-gamification-engine/plan.md` Section 4 → model definitions
- `specs/003-gamification-engine/plan.md` Section 8 → target file structure

**Verification gate**:

- `docker ps` → Docker daemon is running (pre-flight, F3)
- `pnpm nx test progress-api` → health test + auth tests pass (against real PG via testcontainers)
- `pnpm nx lint progress-api` → clean
- `pnpm nx serve progress-api` → starts on 8002
- `curl localhost:8002/health` → 200
- All 8 model files exist under `src/progress_api/models/`
- Materialized view creation function exists in code (grep for `CREATE MATERIALIZED VIEW`)

---

### Task 1a: Quiz Submit Backend (backend-dev, TDD)

**Goal**: `POST /api/v1/quiz/submit` works with full XP + badges + streaks transaction.

**Instructions**:

- Read spec: `specs/003-gamification-engine/requirements.md` sections BR-1, BR-2, BR-3, BR-4
- Read spec: Section 6 "Quiz Submit — Request/Response Contract" (the 12-step transaction)

**Shared utilities first** (C1: `services/shared.py`):

```python
async def upsert_user_from_jwt(session, user) -> User
async def resolve_or_create_chapter(session, slug) -> Chapter  # A4: ON CONFLICT DO NOTHING + SELECT
async def record_activity_day(session, user_id, date, type, ref) -> None
async def update_user_progress(session, user_id, **deltas) -> UserProgress  # P2: SELECT FOR UPDATE, then atomic update
async def invalidate_user_cache(redis, user_id) -> None  # A3: skip if redis is None
```

**TDD sequence**:

1. `tests/unit/test_xp.py` → `services/engine/xp.py` (pure function: `calculate_xp`)
   - Tests (T2 exhaustive): score=0, 50, 85, 100; attempt=1,2,3,4,100; best_score=None,0,50,100; improvement=0, negative, positive
2. `tests/unit/test_badges.py` → `services/engine/badges.py` (pure function: `evaluate_badges` + `BADGE_DEFINITIONS` dict)
   - Badge definitions dict with 14 Phase 1 badges (C3)
   - Tests: first quiz → first-steps; 100% → perfect-score; 100% attempt 1 → ace; all badges already earned → empty list
3. `tests/unit/test_streaks.py` → `services/engine/streaks.py` (pure function: `calculate_streak`)
   - Tests: empty dates, single day, consecutive, gap in middle, today not in list, month boundary crossing
4. `tests/integration/test_quiz_submit.py` → `services/quiz.py` + `routes/quiz.py` + `schemas/quiz.py`
   - Happy path: submit → XP + badges + streak in response
   - Validation errors (T3): score_pct=101 → 422, score_pct=-1 → 422, empty chapter_slug → 422
   - Reattempt: second quiz for same chapter → diminished XP, higher attempt_number
   - Badge idempotency: same badge not awarded twice
   - Cache invalidation test (verify cache key deleted after submit)

**Schema validation** (T3: Pydantic `Field()`):

```python
class QuizSubmitRequest(BaseModel):
    chapter_slug: str = Field(min_length=1)
    score_pct: int = Field(ge=0, le=100)
    questions_correct: int = Field(ge=0)
    questions_total: int = Field(ge=1)
    duration_secs: int | None = Field(default=None, ge=0)
```

**Key reference**:

- `apps/token-metering-api/src/token_metering_api/services/metering.py` → service pattern
- XP formula from spec BR-2: attempt 1 = score_pct, attempt 2 = improvement × 0.5, etc.
- 14 base badges from spec BR-4

**Verification gate**:

- `pnpm nx test progress-api` → all unit + integration tests pass (against real PG)
- New endpoint reachable: `curl -X POST localhost:8002/api/v1/quiz/submit` → 401 (auth required)

---

### Task 1b: Quiz Submit Frontend (frontend-dev)

**Goal**: Quiz.tsx fires API call on complete, shows XP notification.

**Instructions**:

- Read current Quiz.tsx: `apps/learn-app/src/components/quiz/Quiz.tsx`
- Read auth pattern: `apps/learn-app/src/contexts/AuthContext.tsx` (token storage)
- Read Root.tsx: `apps/learn-app/src/theme/Root.tsx` (provider stack)
- Read MDXComponents: `apps/learn-app/src/theme/MDXComponents.tsx` (Quiz registration)
- Read `docusaurus.config.ts` for `customFields` pattern

**Tasks**:

1. Add `progressApiUrl` to `docusaurus.config.ts` `customFields` (A2):
   ```typescript
   customFields: {
     progressApiUrl: process.env.PROGRESS_API_URL || 'http://localhost:8002',
   }
   ```
2. Create `src/lib/progress-types.ts` — TypeScript types matching API contracts from spec
3. Create `src/lib/progress-api.ts` — API client:
   - Reads URL from `useDocusaurusContext().siteConfig.customFields.progressApiUrl`
   - Uses `localStorage.getItem("ainative_id_token")` for auth (NOT access_token)
   - `submitQuizScore(data)`, `completeLesson(data)`, `getProgress()`, `getLeaderboard()`
4. Add `onComplete?: (result: QuizResult) => void` prop to `Quiz.tsx`
5. Create `src/components/progress/QuizXPNotification.tsx` — toast showing XP earned + new badges
6. **Modify `GatedQuiz/index.tsx`** (F2 — this is the actual integration point):
   - MDX pages use `<Quiz>` which maps to `GatedQuiz` via MDXComponents.tsx
   - GatedQuiz wraps Quiz in ContentGate (auth) and passes `...quizProps`
   - **GatedQuiz must**: (a) create an `onComplete` handler that calls `submitQuizScore()`, (b) extract `chapter_slug` from `window.location.pathname`, (c) manage XP notification state, (d) pass the handler down to `<Quiz onComplete={handleComplete}>`
   - This is the natural integration point because the user is already auth-gated here
   - Do NOT try to wire this at MDX page level — GatedQuiz is where auth context exists

**Chapter slug extraction**:

```typescript
const pathSegments = window.location.pathname.split("/");
const docsIndex = pathSegments.indexOf("docs");
const chapterSlug = pathSegments.slice(docsIndex + 1, -1).join("/");
```

**Verification gate**:

- `cd apps/learn-app && npx tsc --noEmit` → no errors
- Quiz.tsx has onComplete prop (grep verify)
- progress-api.ts uses `ainative_id_token` (grep verify)
- progress-api.ts reads URL from customFields (grep verify)
- New files exist: progress-types.ts, progress-api.ts, QuizXPNotification.tsx

---

### Task 2a: Lesson Complete Backend (backend-dev, TDD)

**Goal**: `POST /api/v1/lesson/complete` works. Idempotent.

**Instructions**:

- Read spec: BR-8 (Lesson Completion Tracking)
- Read spec: Section 6 "Lesson Complete — Request/Response Contract"
- Reuse shared utilities from Task 1a (C1: `services/shared.py`)

**Schema validation** (T3):

```python
class LessonCompleteRequest(BaseModel):
    chapter_slug: str = Field(min_length=1)
    lesson_slug: str = Field(min_length=1)
    active_duration_secs: int | None = Field(default=None, ge=0)
```

**TDD**:

1. `tests/integration/test_lesson_complete.py` → `services/lesson.py` + `routes/lesson.py` + `schemas/lesson.py`
2. Test: first completion returns `already_completed: false`
3. Test: second call same (user, chapter, lesson) returns `already_completed: true`, no duplicate row
4. Test: streak updated (activity_day inserted)
5. Test: user_progress.lessons_completed incremented (P2: via SELECT FOR UPDATE)
6. Test: cache invalidated
7. Test: validation — empty slugs → 422, negative duration → 422

**Verification gate**:

- `pnpm nx test progress-api` → all tests pass (including previous quiz tests)
- New endpoint: `curl -X POST localhost:8002/api/v1/lesson/complete` → 401

---

### Task 2b: Lesson Complete Frontend (frontend-dev)

**Goal**: "Mark as Complete" button on lesson pages with active time tracking.

**Instructions**:

- Read spec: BR-8 (active time tracking, visibilitychange API)
- Read Docusaurus swizzle: `apps/learn-app/src/theme/DocItem/Content/` (existing swizzle point)

**Tasks**:

1. Create `src/hooks/useLessonTimer.ts` — tracks active time via `visibilitychange` API
   - Start 1s interval on mount
   - Pause when `document.visibilityState === 'hidden'`
   - Resume when visible
   - Returns `activeSeconds: number`
2. Create `src/components/progress/LessonCompleteButton.tsx` — button + timer display
   - Calls `completeLesson()` from progress-api.ts on click
   - Shows "Completed" state if already done (local state for now — ProgressContext comes in 3b)
   - Extracts chapter_slug + lesson_slug from URL
3. Add `completeLesson()` to `progress-api.ts`
4. Wire button into lesson layout (via DocItem swizzle or MDX wrapper)

**Verification gate**:

- `cd apps/learn-app && npx tsc --noEmit` → no errors
- New files exist: useLessonTimer.ts, LessonCompleteButton.tsx
- progress-api.ts has `completeLesson` function (grep verify)

---

### Task 3a: Dashboard Backend (backend-dev, TDD)

**Goal**: `GET /api/v1/progress/me` returns full user journey data.

**Instructions**:

- Read spec: BR-5 (Progress Dashboard), Section 6 "Progress Dashboard — Response Contract"
- **Use SQLAlchemy `selectinload` for eager loading** (P1): Define `Relationship()` fields on User/UserProgress models, load badges + quiz_attempts + lesson_completions in a single query call with `selectinload`.
- Dashboard reads from `user_progress` (summary row), `user_badges`, aggregated `quiz_attempts` by chapter, `lesson_completions`

**TDD**:

1. `tests/integration/test_progress.py` → `services/progress.py` + `routes/progress.py` + `schemas/progress.py`
2. Test: response shape matches spec (user, stats, badges, chapters with lessons_completed)
3. Test: Redis cache hit (second call returns same data, A3: skip if redis is None)
4. Test: cache busted after quiz submit
5. Test: empty user (no activity) returns zeroed stats, empty arrays

**Verification gate**:

- `pnpm nx test progress-api` → all tests pass
- `curl localhost:8002/api/v1/progress/me` → 401 (confirming route)

---

### Task 3b: Dashboard Frontend (frontend-dev)

**Goal**: `/progress` page with full stats, chapter scores, lesson counts, badges.

**Instructions**:

- Read spec: Section 10 "ProgressContext" code

**Tasks**:

1. Create `src/contexts/ProgressContext.tsx`:
   - Loads `GET /progress/me` on auth (gated — don't fetch if not logged in)
   - Provides `useProgress()` hook with: `progress`, `refreshProgress()`, `isLoading`
   - Re-fetches after quiz submit or lesson complete
2. Create `src/components/progress/ProgressDashboard.tsx`:
   - Stat cards: Total XP, Rank, Current Streak, Perfect Scores
   - Chapter progress: per-chapter best score, XP earned, attempt count, progress bar
   - Lesson completion: per-chapter lesson count
   - Badge gallery: earned badges with dates, locked badges shown as targets (C3: uses BADGE_DEFINITIONS for full list)
3. Create `src/pages/progress.tsx` — page wrapper with Layout
4. Add `<ProgressProvider>` to Root.tsx provider stack (after AuthProvider)
5. Create `src/components/progress/gamification.css` — design tokens (oklch palette matching Polar Night theme)
6. Update LessonCompleteButton (task 2b) to use ProgressContext for "already completed" state

**Verification gate**:

- `cd apps/learn-app && npx tsc --noEmit` → no errors
- ProgressContext exists and is wired into Root.tsx (grep verify)
- /progress page file exists

---

### Task 4a: Leaderboard Backend (backend-dev, TDD)

**Goal**: `GET /api/v1/leaderboard` returns ranked users.

**Instructions**:

- Read spec: BR-6 (Leaderboard), materialized view SQL from Section 7
- **Materialized view uses denormalized `badge_count`** (P3):
  ```sql
  CREATE MATERIALIZED VIEW leaderboard AS
  SELECT u.id, u.display_name, u.avatar_url, p.total_xp,
         RANK() OVER (ORDER BY p.total_xp DESC) AS rank,
         p.badge_count
  FROM users u JOIN user_progress p ON u.id = p.user_id
  WHERE u.show_on_leaderboard = TRUE AND p.total_xp > 0
  ORDER BY p.total_xp DESC;
  CREATE UNIQUE INDEX idx_leaderboard_id ON leaderboard(id);
  ```
- Tests run against real PostgreSQL (T1) — materialized view created and refreshed in tests
- **Use `p.badge_count` from `user_progress`, NOT the subquery in the spec's Section 7 SQL** (D2: decision P3 supersedes spec). The spec's SQL has a correlated subquery — ignore it.
- Scheduler: simple background task to refresh view every 5-15 min (APScheduler or asyncio.create_task)

**TDD**:

1. `tests/integration/test_leaderboard.py` → `services/leaderboard.py` + `routes/leaderboard.py` + `schemas/leaderboard.py`
2. Test: returns top 100 ranked by XP
3. Test: current user's rank included even if not in top 100
4. Test: Redis cache (global key `progress:leaderboard`, A3: skip if redis is None)
5. Test: empty leaderboard (no users with XP) → empty list
6. Test: user with `show_on_leaderboard = False` excluded

**Verification gate**:

- `pnpm nx test progress-api` → all tests pass
- `curl localhost:8002/api/v1/leaderboard` → 401

---

### Task 4b: Leaderboard Frontend (frontend-dev)

**Goal**: `/leaderboard` page with ranked users table.

**Instructions**:

**Tasks**:

1. Create `src/components/progress/BadgeCard.tsx` — badge display component
2. Create `src/components/progress/Leaderboard.tsx` — simple ranked table:
   - Top 100 users with rank, name, avatar, XP, badge count
   - Current user highlighted (different background)
   - Top 3 get special styling (gold/silver/bronze)
3. Create `src/pages/leaderboard.tsx` — page wrapper with Layout
4. Add nav links to progress dashboard and leaderboard (in appropriate navigation component)
5. Add `getLeaderboard()` to `progress-api.ts`

**Verification gate**:

- `cd apps/learn-app && npx tsc --noEmit` → no errors
- Leaderboard page file exists
- progress-api.ts has `getLeaderboard` function

---

### Task 5: Preferences Endpoint + Privacy Toggle (backend-dev + frontend-dev)

**Goal**: `PATCH /api/v1/progress/me/preferences` — users can opt out of leaderboard (D3: GDPR requirement from spec Section 6 line 431).

**Backend** (backend-dev):

1. `schemas/preferences.py` — `PreferencesUpdateRequest(BaseModel): show_on_leaderboard: bool`
2. `routes/preferences.py` — `PATCH /api/v1/progress/me/preferences`
3. `services/preferences.py` — update user's `show_on_leaderboard` field
4. `tests/integration/test_preferences.py`:
   - Toggle on → off → verify user excluded from leaderboard
   - Toggle off → on → verify user reappears
   - Verify cache invalidated after toggle

**Frontend** (frontend-dev):

5. Add toggle switch to ProgressDashboard (task 3b component) — "Show me on leaderboard"
6. Add `updatePreferences()` to `progress-api.ts`

**Verification gate**:

- `pnpm nx test progress-api` → all tests pass
- `curl -X PATCH localhost:8002/api/v1/progress/me/preferences` → 401

---

## Final Verification (after all tasks complete)

**Full integration test — I run ALL of these:**

```bash
# 1. All backend tests (against real PostgreSQL)
pnpm nx test progress-api

# 2. Backend lint
pnpm nx lint progress-api

# 3. Frontend compiles
cd apps/learn-app && npx tsc --noEmit

# 4. Start progress-api + its Docker PostgreSQL
cd apps/progress-api && docker compose up -d
pnpm nx serve progress-api &
sleep 3

# 5. Health check
curl -s http://localhost:8002/health

# 6. Endpoint smoke tests (all should return 401 — auth required)
curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost:8002/api/v1/quiz/submit -H "Content-Type: application/json" -d '{}'
curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost:8002/api/v1/lesson/complete -H "Content-Type: application/json" -d '{}'
curl -s -o /dev/null -w "%{http_code}" http://localhost:8002/api/v1/progress/me
curl -s -o /dev/null -w "%{http_code}" http://localhost:8002/api/v1/leaderboard

# 7. Cleanup
kill %1
cd apps/progress-api && docker compose down

# 8. Frontend build
pnpm nx build learn-app
```

**Expected outcomes**:

- All tests green (against real PostgreSQL)
- All lint clean
- All 4 API endpoints return 401 (auth required) — confirming routes registered
- Health returns 200
- Frontend builds without errors

---

## Estimated Scope

| Metric               | Estimate                       |
| -------------------- | ------------------------------ |
| Team members         | 2 (backend-dev + frontend-dev) |
| Tasks                | 10 (+ 10 verification gates)   |
| Backend files        | ~25                            |
| Frontend files       | ~12                            |
| Test files           | ~8                             |
| Total lines (approx) | ~5,000                         |
| Backend tests        | ~50-60 (exhaustive per T2)     |

## Team Lifecycle

1. `TeamCreate` → `progress-api` team
2. `TaskCreate` × 9 → all tasks with dependencies
3. `Task` tool → spawn `backend-dev` and `frontend-dev` teammates
4. Assign Task 0 to backend-dev → work → **verify** → commit
5. Assign Task 1a to backend-dev → work → **verify** → commit
6. Assign Task 1b to frontend-dev (parallel with 2a) → ...
7. Continue until all tasks verified and committed
8. Final verification → create PR → shutdown teammates → `TeamDelete`
