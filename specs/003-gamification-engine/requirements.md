# 003 — Gamification Engine: Business Requirements

> **Status**: Spec Complete — OQs resolved, lesson completion added, ready for implementation planning
> **Origin**: Strategic prioritization session (Feb 2026)
> **Key Insight**: The 6 interactive teaching modes are the _data generators_. Gamification is the _data surfacer_. They are one system.
> **Design Session**: Issue #708 discussion — schema, API design, chapter identification, scalability decisions

---

## 1. Problem Statement

Agent Factory has a **complete teaching platform** — SSO, content, AI tutoring (Teach/Ask), quizzes, personalization — but **no feedback loop** telling learners how they're progressing. Quiz scores vanish on page refresh. Study sessions leave no trace. There's no reason to come back tomorrow.

**The gap**: Rich interaction data is generated every session but never surfaces back to the learner.

## 2. The Unified Engine Model

```
┌─────────────────────────────────────────────────────────┐
│                    LEARNER SURFACE                       │
│   XP Counter │ Badges │ Streaks │ Progress │ Leaderboard │
└──────────────────────────┬──────────────────────────────┘
                           │ surfaces
┌──────────────────────────▼──────────────────────────────┐
│                  PROGRESS STORE                          │
│   quiz_attempts │ lesson_completions │ user_progress     │
│   user_badges │ activity_days │ streaks                  │
└──────────────────────────┬──────────────────────────────┘
                           │ aggregates
┌──────────────────────────▼──────────────────────────────┐
│               INTERACTIVE MODE ENGINE                    │
│                                                          │
│  LIVE TODAY:          FUTURE MODES:                       │
│  ├── Teach Mode       ├── Socratic Mode (pilot 3-6mo)   │
│  ├── Ask Mode         ├── Coach Mode                     │
│  ├── Quiz Mode        ├── Mentor Mode                    │
│  │   (static MCQ)     ├── Simulator Mode                 │
│  │                    └── Manager Mode                   │
│  │                                                       │
│  Each mode produces mastery signals:                     │
│  conversations, scores, highlights, completions          │
└─────────────────────────────────────────────────────────┘
```

**This is NOT "build gamification, then build interactive modes."**
It's: **every mode that comes online automatically feeds the engagement surface.**

---

## 3. Current State Inventory

### What's Live and Producing Data

| Component                   | Status      | Data Produced                                                | Persisted?                   |
| --------------------------- | ----------- | ------------------------------------------------------------ | ---------------------------- |
| **Quiz UI** (static MCQ)    | Live        | Score %, per-question results, explanations                  | **No** (React state only)    |
| **Teach Mode** (GPT-5-nano) | Live        | Conversation threads, message count, timestamps, lesson path | Yes (PostgreSQL via ChatKit) |
| **Ask Mode** (DeepSeek)     | Live        | Highlighted text, question type, lesson context              | Yes (PostgreSQL via ChatKit) |
| **Personalization**         | Live (3/mo) | Generated content, interest tag, grade level                 | Yes (R2 + DB)                |
| **Token Metering**          | Live        | Token usage per request, model, cost                         | Yes (token-metering-api)     |
| **GA4 Analytics**           | Live        | Scroll depth, time on page, quiz events                      | Yes (Google Analytics)       |
| **Reading Progress**        | Live        | Scroll % indicator                                           | **No** (visual only)         |

### Assessment Inventory

| Assessment Type                          | Count                            | Format                            | Interactive?       | Trackable?                |
| ---------------------------------------- | -------------------------------- | --------------------------------- | ------------------ | ------------------------- |
| Chapter-end quizzes (`<Quiz>` component) | ~40 quizzes, **1,513 questions** | Static MCQ in MDX, 4 options each | Yes                | **No** (React state only) |
| `assessment_quick_check` in frontmatter  | Throughout lessons               | Teacher-facing prompts            | No — teacher notes | N/A                       |

**Key finding**: The `<Quiz>` component (`Quiz.tsx`) is entirely client-side. Zero API calls. Score calculated via `calculateScore()`, stored in `useState`, lost on page refresh. The component supports `questionsPerBatch` (default 15) — chapters with 50 questions show a random 15 per attempt.

### What Was Built Then Removed (PR #680 history)

PR #680 (`feat/user-progress`) contained frontend gamification UI with mock data. **All removed from current branch.** TypeScript types and design documents remain in PR #680 for reference. See Appendix A for full assessment.

---

## 4. Business Requirements

### BR-1: Quiz Score Persistence

**Requirement**: When a learner completes a quiz, the score MUST be persisted to a backend store and associated with their user account.

**Rationale**: This is the prerequisite for everything else. Without persisted scores, XP, badges, progress, and leaderboards are impossible.

**Acceptance Criteria**:

- Quiz score survives page refresh
- Score includes: user_id, chapter_slug, score_percentage, questions_correct, questions_total, attempt_number, duration_seconds, timestamp
- Multiple attempts tracked with diminishing XP returns
- Best score per chapter is queryable

**Data Source**: `Quiz.tsx` already calculates scores — needs a single `onComplete` callback prop that fires `POST /api/v1/quiz/submit`.

---

### BR-2: XP System with Diminishing Returns

**Requirement**: Each quiz submission earns XP using a fair formula that rewards first attempts and diminishing returns on reattempts.

**Rationale**: Prevents XP farming while still rewarding improvement. Creates meaningful differentiation on leaderboard.

**Formula** (from PR #680, validated):

```
Attempt 1: XP = score_percentage (e.g., 85% → 85 XP)
Attempt 2: XP = improvement × 0.5
Attempt 3: XP = improvement × 0.25
Attempt 4+: XP = improvement × 0.10
No improvement = 0 XP
```

**Note**: Quiz.tsx shows a random subset of questions per attempt (`questionsPerBatch`). Two attempts may test different questions. This is acceptable — score percentage is the mastery signal, not which specific questions were answered.

**Acceptance Criteria**:

- 100 XP base per quiz, scaled by percentage
- Improvement-only XP on reattempts (never exceeds first-attempt potential)
- XP is immutable once earned (never removed, even if curriculum changes)

---

### BR-3: Streak Tracking

**Requirement**: Track consecutive days of learning activity to encourage daily engagement.

**Rationale**: Streaks are the highest-ROI gamification mechanic. Duolingo's entire retention model is built on streaks.

**RESOLVED — Active Day Definition (graduated by phase)**:

| Phase         | What Counts as "Active Day"                                             |
| ------------- | ----------------------------------------------------------------------- |
| Phase 1 (MVP) | Quiz completion **OR** lesson marked as complete                        |
| Phase 2       | Above **OR** Teach session >= 5 turns **OR** Ask mode usage on a lesson |

**Design**: The `activity_days` table stores the _reason_ for each activity from day one. When Phase 2 adds Teach/Ask, the streak logic doesn't change — only the event producers expand.

**RESOLVED — Personalization does NOT count** (OQ-6): Rate-limited to 3/month, not a learning activity, creates perverse incentives. Excluded from streaks and XP entirely.

**Acceptance Criteria**:

- Current streak (consecutive days) tracked
- Longest streak (all-time) tracked
- Streak badges at 3, 7, 30 days
- Grace period: 1 streak freeze per week (Duolingo pattern, Phase 2)

---

### BR-4: Badge System

**Requirement**: Award achievement badges for meaningful learning milestones.

**Rationale**: Badges mark mastery moments. They're the "yearbook" of a learner's journey. They provide collection motivation beyond XP.

**RESOLVED — 3 Tiers** (OQ-9): Bronze/Silver/Gold. Proven by GitHub and Google. Clean, doesn't overwhelm. 4th tier can be added later if engagement data warrants it.

**14 Base Badges (Phase 1)**:

| Category        | Badges                           | Trigger                    |
| --------------- | -------------------------------- | -------------------------- |
| Milestone       | First Steps                      | First quiz completed       |
| Achievement     | Perfect Score                    | 100% on any quiz           |
| Achievement     | Ace                              | 100% on first attempt      |
| Streak          | On Fire, Week Warrior, Dedicated | 3, 7, 30-day streaks       |
| Part Completion | Foundations through Cloud Native | All quizzes in Part 1-6    |
| Capstone        | Agent Factory Graduate           | All quizzes in entire book |
| Ranking         | Elite                            | Top 100 on leaderboard     |

**Tiered Expansions (Phase 2+)**:

| Badge                  | Bronze         | Silver            | Gold                |
| ---------------------- | -------------- | ----------------- | ------------------- |
| On Fire (streak)       | 3 days         | 7 days            | 30 days             |
| Perfect Score          | 1 perfect quiz | 5 perfect quizzes | All quizzes perfect |
| Deep Diver (Ask mode)  | 10 lessons     | 50 lessons        | All lessons         |
| Study Bug (Teach mode) | 10 sessions    | 50 sessions       | 100 sessions        |

**Acceptance Criteria**:

- Badges evaluated synchronously in the quiz submit transaction (Phase 1 has ~8 applicable badges — simple condition checks, no performance concern)
- Badge unlock notification returned in submit response
- Badge gallery viewable on dashboard
- Badges never revoked
- `user_badges` composite PK prevents double-awarding (UPSERT idempotent)

---

### BR-5: Progress Dashboard

**Requirement**: A dedicated page showing the learner's journey across the entire book.

**Rationale**: Progress visibility is the core motivation loop. Learners need to see how far they've come and what's ahead.

**Dashboard Sections**:

1. **Stat Cards**: Total XP, Global Rank, Current Streak, Perfect Scores
2. **Chapter Progress**: Per-chapter best score, XP earned, attempt count, visual progress bar
3. **Badge Gallery**: Earned badges with dates, locked badges shown as targets
4. **Activity History**: Recent quiz completions (Phase 2: study sessions)

**Acceptance Criteria**:

- Page loads in <2s — reads from pre-computed `user_progress` summary table (single row lookup)
- Shows progress against ACTIVE curriculum (archived chapters excluded from %)
- Mobile responsive

---

### BR-6: Leaderboard

**Requirement**: Global leaderboard ranking learners by total XP.

**RESOLVED — Scope** (OQ-4): Global for now. At 50k users, still a single materialized view. Schema supports future scope column (cohort, org) but Phase 1 only implements global.

**Design**:

- Top 100 displayed
- Current user's rank always shown (even if not in top 100)
- Display: rank, display_name, avatar, XP, badge count
- Top 3 get special styling

**RESOLVED — Privacy** (OQ-5):

- Opt-out flag (`show_on_leaderboard: boolean`, default true)
- Opted-out users show as "Anonymous Learner" or excluded
- Progress data exportable via `GET /api/v1/progress/me/export` (GDPR Article 20)
- Account deletion cascades to all progress data
- No PII in progress-api beyond user_id — display names stored locally from JWT claims

**Acceptance Criteria**:

- Materialized view refreshed every 5-15 minutes (not real-time)
- Cached in Redis/memory — 50k concurrent readers, one payload
- User can opt out of leaderboard display

---

### BR-7: Content-Addressed Progress Architecture

**Requirement**: Progress tracking must survive curriculum changes (lessons added, removed, reordered).

**Rationale**: The book is actively evolving. Chapters get added, restructured, archived. Earned progress must never be lost.

**RESOLVED — Chapter Identification via Docusaurus URL Slugs**:

Docusaurus's `numberPrefixParser` (default, no custom config) strips numeric prefixes from directory/file names:

```
Filesystem:                                    URL slug:
01-General-Agents-Foundations/                 → General-Agents-Foundations/
  01-agent-factory-paradigm/                   →   agent-factory-paradigm/
    11-chapter-quiz.md                         →     chapter-quiz
```

The URL slug is the stable identifier:

- **Reorder chapter** (01 → 03): URL stays `agent-factory-paradigm`. Nothing breaks.
- **Move to different part**: URL changes — but this also breaks all bookmarks, SEO, external links. It's a major content migration that already requires Docusaurus redirects.
- **Rename directory**: Conceptually a different chapter. Also breaks all URLs — requires redirects anyway.

**The URL slug is as stable as the URL itself. URLs are the one thing people are already disciplined about keeping stable.**

**Implementation**:

1. Frontend extracts chapter path from `window.location.pathname`:
   `/docs/General-Agents-Foundations/agent-factory-paradigm/chapter-quiz` → `General-Agents-Foundations/agent-factory-paradigm`
2. Sends to progress-api as the chapter identifier
3. Backend's `chapter_aliases` table maps slug → internal `chapter_id` (database-owned, auto-generated)
4. If a URL ever changes (rare, requires redirects anyway), add a new alias pointing to the same internal ID

**No UUIDs in frontmatter. No MDX file changes. No fragile human-maintained contracts. The database owns identity.**

**Design Principles**:

1. **Separate content identity from progress** — `chapters` + `chapter_aliases` tables vs. `quiz_attempts`/`user_progress`
2. **Soft deletes only** — `is_active = FALSE`, never hard delete
3. **Completion % against active chapters** — Archived chapters don't count toward progress
4. **XP is immutable** — Once earned, XP persists even if source chapter is archived
5. **Database owns identity** — Internal chapter IDs are auto-generated, immutable. Slugs are mutable lookup keys.

**Acceptance Criteria**:

- Adding a chapter: new alias auto-created on first quiz submission, completion % recalculated
- Archiving a chapter: `is_active = FALSE`, earned XP preserved
- Renaming a chapter: add new alias pointing to same internal ID
- Moving a chapter between parts: update alias, progress follows

---

### BR-8: Lesson Completion Tracking

**Requirement**: Students can mark individual lessons as complete. Active reading time is recorded.

**Rationale**: Without lesson-level progress, students only know they "did the quiz" — not which lessons they actually read. This is the missing signal between "opened the book" and "passed the quiz." It also makes the progress dashboard useful for lesson-level navigation ("where did I leave off?").

**Design**: A "Mark as Complete" button at the bottom of each lesson page. When clicked, the frontend sends the lesson slug and the active reading time (tab-focused seconds only).

**Active Time Tracking**:

```
Page loads → start 1-second interval timer
Tab hidden (visibilitychange) → pause timer
Tab visible → resume timer
"Mark as Complete" clicked → POST with accumulated active_duration_secs
```

Only active time (tab focused) is tracked. If a student opens a lesson, checks email for 20 minutes, comes back and finishes, only the actual reading time is recorded.

**What this enables** (without building anything extra now):

- Average reading time per lesson → identify lessons that are too long/dense
- Students who "completed" in 5 seconds → low-quality completion (future: minimum threshold)
- Per-student reading speed → future adaptive difficulty input
- Sidebar progress indicators (Phase 2) — now have data to drive them

**Acceptance Criteria**:

- Lesson marked complete survives page refresh (persisted to backend)
- Active duration recorded in seconds (tab-visible time only)
- Completion is idempotent — marking complete twice doesn't create duplicates
- `GET /progress/me` includes `lessons_completed` array
- Completion counts as an active day for streak tracking

---

### BR-9: Study Session Tracking (Engine Foundation)

**Requirement**: Track learning sessions across ALL interactive modes, not just quizzes.

**Rationale**: This is the **engine requirement** — what makes gamification a unified system rather than just "quiz scores + badges." Every mode produces mastery evidence. The system must capture it.

**MVP Scope**: Quiz persistence + lesson completion are the MVP. Teach/Ask session tracking is Phase 2. But the schema and API must be designed to accommodate all modes from day one.

**Session Signals by Mode**:

| Mode       | Signal                         | Mastery Evidence                              | Phase |
| ---------- | ------------------------------ | --------------------------------------------- | ----- |
| **Quiz**   | Score + attempt count          | Direct mastery measurement                    | 1     |
| **Lesson** | Mark complete + active time    | Engaged with reading material                 | 1     |
| **Teach**  | Thread completion (N turns)    | Engaged with material, correctness trajectory | 2     |
| **Teach**  | Restatement quality            | Deep comprehension (student explains back)    | 3     |
| **Ask**    | Highlight frequency per lesson | Comprehension gaps identified                 | 2     |
| **Ask**    | Question type distribution     | Surface vs. deep understanding                | 2     |

**Acceptance Criteria**:

- `activity_days` table captures activity type and reference from Phase 1
- Phase 2 adds `study_sessions` table: user_id, lesson_path, mode (teach/ask/quiz), started_at, completed_at, metadata (JSONB)
- Quiz submissions and lesson completions link to activity_days immediately
- Teach mode threads can be linked to study sessions (thread_id reference) in Phase 2
- Schema extensible for future modes without migration

---

## 5. Resolved Design Decisions

All original Open Questions (OQ-1 through OQ-9) have been resolved through the design session.

### RD-1: New Service (was OQ-1)

**Decision**: New `progress-api` service (FastAPI).

**Rationale**: Clean ownership, independent scaling. Reuses auth patterns from existing services (JWT/JWKS from SSO, same middleware as study-mode-api and token-metering-api).

### RD-2: Active Day Definition (was OQ-2)

**Decision**: Graduated by phase. See BR-3.

### RD-3: Real-time vs Batch (was OQ-3)

**Decision**: Real-time for quiz XP, eventual consistency for everything else.

| Operation                          | Timing                                      | Rationale                               |
| ---------------------------------- | ------------------------------------------- | --------------------------------------- |
| Quiz submit → XP + badges + streak | Synchronous (in response)                   | Dopamine hit must be instant            |
| Leaderboard rank                   | Materialized view, refreshed every 5-15 min | Nobody notices rank changed 10 min late |
| Phase 2 study session XP           | Batch (hourly)                              | Teach/Ask sessions are long-running     |

### RD-4: Leaderboard Scope (was OQ-4)

**Decision**: Global for now. Schema includes scope column for future extensibility (cohort, org) but Phase 1 only implements global. At 50k users, still trivially a single table scan.

### RD-5: Privacy/GDPR (was OQ-5)

**Decision**: Minimal but GDPR-defensible. See BR-6.

### RD-6: Personalization XP (was OQ-6)

**Decision**: No. Personalization does NOT count for streaks or XP.

**Rationale**: Rate-limited to 3/month (useless for streaks). Content delivery mechanism, not a learning activity. Doesn't demonstrate comprehension. Creates perverse incentive to burn personalizations for XP.

### RD-7: xAPI Timing (was OQ-7)

**Decision**: Phase 3. No xAPI in Phase 1 or 2. No xAPI libraries, no Learning Record Store, no statement emitting.

The only xAPI consideration for Phase 1-2 is mental: our table structure (user → action → object → result) happens to map cleanly to xAPI's actor-verb-object-result model. So when Phase 3 adds xAPI, it's just a formatter on top of existing data — no schema migration.

### RD-8: Lesson Completion Definition (was OQ-8)

**Decision**: Explicit "Mark as Complete" button with active reading time, starting in Phase 1.

| Phase   | Definition                                                                                                  |
| ------- | ----------------------------------------------------------------------------------------------------------- |
| Phase 1 | Student clicks "Mark as Complete" → records completion + active reading time (tab-focused seconds)          |
| Phase 2 | Above + Teach/Ask session = "verified study" (stronger signal). Sidebar shows completion status per lesson. |

**Rationale**: Automatic completion (scroll/time thresholds) is gameable. A manual button puts the student in control and captures intent. Active time tracking (paused when tab hidden) gives honest reading duration without complexity. No AI features required — purely frontend → progress-api.

### RD-9: Badge Tiers (was OQ-9)

**Decision**: 3 tiers (Bronze/Silver/Gold). See BR-4.

---

## 6. API Design (Business Operations, Not CRUD)

### Design Principle

APIs are operation-oriented, not entity-oriented. Each endpoint maps to a business operation — not to a database table.

### Phase 1 MVP Endpoints (4 external + 1 admin)

| Business Operation                  | Endpoint                          | Method | Auth     |
| ----------------------------------- | --------------------------------- | ------ | -------- |
| Student finishes a quiz             | `/api/v1/quiz/submit`             | POST   | Required |
| Student marks lesson complete       | `/api/v1/lesson/complete`         | POST   | Required |
| Student views their progress        | `/api/v1/progress/me`             | GET    | Required |
| Student views leaderboard           | `/api/v1/leaderboard`             | GET    | Required |
| Student updates privacy preferences | `/api/v1/progress/me/preferences` | PATCH  | Required |

### Phase 2 Additions

| Business Operation                      | Endpoint                     | Method |
| --------------------------------------- | ---------------------------- | ------ |
| System records study session completion | `/api/v1/sessions/complete`  | POST   |
| Student exports their data (GDPR)       | `/api/v1/progress/me/export` | GET    |

### Internal Operations (not API endpoints)

| Operation           | Mechanism                                                                          |
| ------------------- | ---------------------------------------------------------------------------------- |
| Leaderboard refresh | Scheduled job: `REFRESH MATERIALIZED VIEW CONCURRENTLY leaderboard` every 5-15 min |
| Streak expiry check | Daily cron: identify users whose streak broke                                      |

### Quiz Submit — Request/Response Contract

**Request**:

```json
POST /api/v1/quiz/submit
Authorization: Bearer <id_token>

{
    "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
    "score_pct": 85,
    "questions_correct": 13,
    "questions_total": 15,
    "duration_secs": 420
}
```

**Server-side (single transaction)**:

```
 1. UPSERT user from JWT claims (sub, name, email) — keeps name fresh, no SSO calls
 2. RESOLVE chapter_slug → internal chapter_id via chapter_aliases (auto-create on first encounter)
 3. COUNT previous attempts for (user, chapter) → attempt_number
 4. GET best previous score for (user, chapter) → best_score
 5. CALCULATE XP:
    - attempt 1: xp = score_pct
    - attempt 2: xp = max(0, score_pct - best_score) × 0.5
    - attempt 3: xp = max(0, score_pct - best_score) × 0.25
    - attempt 4+: xp = max(0, score_pct - best_score) × 0.10
 6. INSERT quiz_attempt
 7. CHECK badge conditions:
    - First quiz ever? → 'first-steps'
    - score_pct == 100? → 'perfect-score'
    - score_pct == 100 AND attempt_number == 1? → 'ace'
    - All chapters in part completed? → part completion badge
 8. INSERT new badges (ON CONFLICT DO NOTHING — idempotent)
 9. UPSERT activity_day for today
10. CALCULATE streak from activity_days
11. UPDATE user_progress summary (total_xp, streak, counts, etc.)
12. COMMIT
```

**Response**:

```json
{
  "xp_earned": 85,
  "total_xp": 1234,
  "attempt_number": 1,
  "best_score": 85,
  "new_badges": [
    {
      "id": "first-steps",
      "name": "First Steps",
      "earned_at": "2026-02-12T10:30:00Z"
    }
  ],
  "streak": { "current": 5, "longest": 12 },
  "rank": 42
}
```

One request. One response. Full dopamine payload.

### Lesson Complete — Request/Response Contract

**Request**:

```json
POST /api/v1/lesson/complete
Authorization: Bearer <id_token>

{
    "chapter_slug": "General-Agents-Foundations/agent-factory-paradigm",
    "lesson_slug": "selling-agentic-ai-services",
    "active_duration_secs": 480
}
```

**Server-side (single transaction)**:

```
1. UPSERT user from JWT claims (same as quiz submit)
2. RESOLVE chapter_slug → chapter_id via chapter_aliases
3. INSERT lesson_completion (ON CONFLICT DO NOTHING — idempotent)
4. UPSERT activity_day for today (type: 'lesson')
5. CALCULATE streak from activity_days
6. UPDATE user_progress summary (streak, last_activity_date)
7. COMMIT
```

**Response**:

```json
{
  "completed": true,
  "active_duration_secs": 480,
  "streak": { "current": 5, "longest": 12 },
  "already_completed": false
}
```

If already completed, returns `already_completed: true` and the original `active_duration_secs`. No duplicate rows, no extra XP.

**Note**: Lesson completion does NOT award XP in Phase 1. It tracks progress and feeds streaks. XP for lesson completion can be added in Phase 2 (e.g., 5 XP per lesson, once) without schema changes.

### Progress Dashboard — Response Contract

**Request**: `GET /api/v1/progress/me`

**Response**:

```json
{
  "user": { "display_name": "Jane", "avatar_url": null },
  "stats": {
    "total_xp": 1234,
    "rank": 42,
    "current_streak": 5,
    "longest_streak": 12,
    "quizzes_completed": 8,
    "perfect_scores": 2
  },
  "badges": [
    {
      "id": "first-steps",
      "name": "First Steps",
      "earned_at": "2026-02-01T..."
    },
    {
      "id": "perfect-score",
      "name": "Perfect Score",
      "earned_at": "2026-02-05T..."
    }
  ],
  "chapters": [
    {
      "slug": "General-Agents-Foundations/agent-factory-paradigm",
      "title": "The AI Agent Factory Paradigm",
      "best_score": 85,
      "attempts": 2,
      "xp_earned": 110,
      "lessons_completed": [
        {
          "lesson_slug": "digital-fte-revolution",
          "active_duration_secs": 420,
          "completed_at": "2026-02-10T14:30:00Z"
        },
        {
          "lesson_slug": "selling-agentic-ai-services",
          "active_duration_secs": 600,
          "completed_at": "2026-02-11T09:15:00Z"
        }
      ]
    }
  ]
}
```

4 queries, all indexed, all on one user's data. Sub-millisecond at 50k users.

---

## 7. Schema Design

### Design Principles

1. **Denormalized summary table** — `user_progress` is pre-computed on every write (quiz submit or lesson complete). Dashboard reads = single row lookup. O(1).
2. **Database owns identity** — Chapters have auto-generated internal IDs. Slugs are mutable lookup keys.
3. **Activity tracking extensible** — `activity_days` stores the _reason_ for each activity. Phase 2 modes plug in without schema changes.
4. **Idempotent completions** — `lesson_completions` uses composite PK (user, chapter, lesson). Marking complete twice = no-op.
5. **Materialized view for leaderboard** — Refreshed every 5-15 min. 50k users reading = 1 cached payload.
6. **User data denormalized from SSO** — Name/email extracted from JWT claims, stored locally. Zero cross-service queries on read path.

### Tables

```sql
-- User identity (denormalized from SSO JWT claims)
-- Created lazily on first quiz submit. Name updated from JWT on every request.
CREATE TABLE users (
    id                  TEXT PRIMARY KEY,  -- JWT 'sub' claim
    display_name        TEXT NOT NULL,
    email               TEXT,
    avatar_url          TEXT,
    show_on_leaderboard BOOLEAN DEFAULT TRUE,
    created_at          TIMESTAMPTZ DEFAULT NOW(),
    updated_at          TIMESTAMPTZ DEFAULT NOW()
);

-- Chapter identity (database-owned)
CREATE TABLE chapters (
    id          SERIAL PRIMARY KEY,
    title       TEXT NOT NULL,
    part_slug   TEXT,          -- e.g. 'General-Agents-Foundations'
    is_active   BOOLEAN DEFAULT TRUE,
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- Multiple slugs can point to the same chapter (survives renames)
CREATE TABLE chapter_aliases (
    slug        TEXT PRIMARY KEY,  -- e.g. 'General-Agents-Foundations/agent-factory-paradigm'
    chapter_id  INT NOT NULL REFERENCES chapters(id)
);

-- Individual quiz submissions
CREATE TABLE quiz_attempts (
    id                BIGSERIAL PRIMARY KEY,
    user_id           TEXT NOT NULL REFERENCES users(id),
    chapter_id        INT NOT NULL REFERENCES chapters(id),
    score_pct         SMALLINT NOT NULL,   -- 0-100
    questions_correct SMALLINT NOT NULL,
    questions_total   SMALLINT NOT NULL,
    attempt_number    SMALLINT NOT NULL,
    xp_earned         INT NOT NULL,
    duration_secs     INT,
    created_at        TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX idx_quiz_user_chapter ON quiz_attempts(user_id, chapter_id);

-- Lesson completion tracking (idempotent — one row per user per lesson)
CREATE TABLE lesson_completions (
    user_id              TEXT NOT NULL REFERENCES users(id),
    chapter_slug         TEXT NOT NULL,    -- e.g. 'General-Agents-Foundations/agent-factory-paradigm'
    lesson_slug          TEXT NOT NULL,    -- e.g. 'selling-agentic-ai-services'
    active_duration_secs INT,             -- tab-focused reading time only
    completed_at         TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (user_id, chapter_slug, lesson_slug)
);
CREATE INDEX idx_lesson_user ON lesson_completions(user_id);

-- Pre-computed summary (updated atomically on every quiz submit or lesson complete)
CREATE TABLE user_progress (
    user_id            TEXT PRIMARY KEY REFERENCES users(id),
    total_xp           INT DEFAULT 0,
    quizzes_completed  INT DEFAULT 0,
    lessons_completed  INT DEFAULT 0,
    perfect_scores     INT DEFAULT 0,
    current_streak     INT DEFAULT 0,
    longest_streak     INT DEFAULT 0,
    last_activity_date DATE,
    updated_at         TIMESTAMPTZ DEFAULT NOW()
);

-- Earned badges
CREATE TABLE user_badges (
    user_id     TEXT NOT NULL REFERENCES users(id),
    badge_id    TEXT NOT NULL,       -- e.g. 'first-steps', 'perfect-score'
    earned_at   TIMESTAMPTZ DEFAULT NOW(),
    trigger_ref TEXT,               -- e.g. 'quiz:agent-factory-paradigm:attempt:1'
    PRIMARY KEY (user_id, badge_id)  -- prevents double-awarding
);

-- Daily activity tracking (for streaks)
CREATE TABLE activity_days (
    user_id       TEXT NOT NULL REFERENCES users(id),
    activity_date DATE NOT NULL,
    activity_type TEXT NOT NULL,       -- 'quiz' (Phase 1), 'teach', 'ask' (Phase 2)
    reference_id  TEXT,               -- chapter slug or thread_id
    created_at    TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (user_id, activity_date, activity_type, reference_id)
);

-- Phase 2: Study sessions (Teach/Ask mode tracking)
-- CREATE TABLE study_sessions (
--     id           BIGSERIAL PRIMARY KEY,
--     user_id      TEXT NOT NULL REFERENCES users(id),
--     lesson_path  TEXT NOT NULL,
--     mode         TEXT NOT NULL,       -- 'teach', 'ask', 'quiz'
--     started_at   TIMESTAMPTZ NOT NULL,
--     completed_at TIMESTAMPTZ,
--     metadata     JSONB,              -- mode-specific data (turns, highlights, etc.)
--     created_at   TIMESTAMPTZ DEFAULT NOW()
-- );

-- Leaderboard (materialized, refreshed every 5-15 min)
CREATE MATERIALIZED VIEW leaderboard AS
SELECT
    u.id, u.display_name, u.avatar_url,
    p.total_xp,
    RANK() OVER (ORDER BY p.total_xp DESC) AS rank,
    (SELECT COUNT(*) FROM user_badges b WHERE b.user_id = u.id) AS badge_count
FROM users u
JOIN user_progress p ON u.id = p.user_id
WHERE u.show_on_leaderboard = TRUE AND p.total_xp > 0
ORDER BY p.total_xp DESC;

CREATE UNIQUE INDEX idx_leaderboard_id ON leaderboard(id);
```

---

## 8. User Identity Architecture

### No SSO Queries on Read Path

The progress-api stores user identity locally, denormalized from JWT claims. Zero cross-service queries.

**JWT claims available** (from SSO id_token):

| Claim   | Field                | Usage                           |
| ------- | -------------------- | ------------------------------- |
| `sub`   | `users.id`           | Primary key, immutable          |
| `name`  | `users.display_name` | Shown on leaderboard, dashboard |
| `email` | `users.email`        | For data export / GDPR          |

**Lifecycle**:

1. **First quiz submit**: JWT claims extracted → `INSERT INTO users (id, display_name, email)` (lazy creation)
2. **Every authenticated request**: `UPDATE users SET display_name = $name, updated_at = NOW() WHERE id = $sub` (keeps name fresh if user changes it in SSO)
3. **Leaderboard / dashboard reads**: Query `users` table directly — never calls SSO

**Auth pattern**: Identical to study-mode-api and token-metering-api — JWKS-based JWT verification, cached 1 hour, local signature check, no SSO call per request. `CurrentUser` class extracted from JWT payload. Dev mode bypass for local development.

---

## 9. Scalability Design (50k Users)

### Read Path (where scale matters)

| Read Operation             | Strategy                                         | Latency            |
| -------------------------- | ------------------------------------------------ | ------------------ |
| Dashboard (`/progress/me`) | Single-row lookup on `user_progress` by PK       | Sub-ms             |
| Leaderboard                | Materialized view → Redis/memory cache           | Sub-ms (cache hit) |
| Badge gallery              | Part of `/progress/me` response                  | Same request       |
| Chapter scores             | `quiz_attempts` indexed by (user_id, chapter_id) | Sub-ms             |

### Write Path (low volume, user-isolated)

| Write Operation     | Frequency                       | Contention                                        |
| ------------------- | ------------------------------- | ------------------------------------------------- |
| Quiz submit         | ~100 concurrent at peak         | Zero — each user writes to their own data         |
| Leaderboard refresh | Every 5-15 min (background job) | None — `REFRESH CONCURRENTLY` doesn't block reads |

### Infrastructure

| Concern              | Solution                                                                    |
| -------------------- | --------------------------------------------------------------------------- |
| Connection pooling   | PgBouncer (transaction mode) — 50k users ≠ 50k connections                  |
| Leaderboard caching  | Redis or application-level cache. Invalidated on materialized view refresh. |
| Hot path computation | Zero on read path. All XP/badge/streak calculated on write (quiz submit).   |
| Name freshness       | Updated from JWT on every request. No SSO calls.                            |
| Database             | PostgreSQL (same as other services). Single instance handles this scale.    |

---

## 10. Frontend Changes (Minimal for Phase 1)

### Quiz.tsx Modifications

**Current state**: `Quiz.tsx` has no API calls. `handleSubmit` sets `showResults = true` in React state. That's it.

**Required change**: Add `onComplete` callback prop.

```typescript
// New prop
interface QuizProps {
  title?: string;
  questions: QuizQuestion[];
  questionsPerBatch?: number;
  onComplete?: (result: QuizResult) => void; // NEW
}

interface QuizResult {
  score_pct: number;
  questions_correct: number;
  questions_total: number;
  duration_secs: number;
}
```

The `onComplete` callback fires inside `handleSubmit`, right after `setShowResults(true)`.

### Page-Level Integration

The MDX quiz pages (or a wrapper component) derive the chapter slug from the URL:

```typescript
// Extract chapter path from URL
// /docs/General-Agents-Foundations/agent-factory-paradigm/chapter-quiz
// → "General-Agents-Foundations/agent-factory-paradigm"
const pathSegments = window.location.pathname.split("/");
const docsIndex = pathSegments.indexOf("docs");
const chapterSlug = pathSegments.slice(docsIndex + 1, -1).join("/");
// Strip quiz page name, keep part/chapter
```

Sends `POST /api/v1/quiz/submit` with the chapter slug and score data. Shows XP/badge notification from response.

**No MDX file changes. No frontmatter changes. No UUID migrations.**

### ProgressContext (How the UI Knows What's Completed)

A React context that loads progress data once on authentication and makes it available to any component.

```typescript
// ProgressContext loads GET /api/v1/progress/me on auth
// Caches result, refreshes after quiz submit or lesson complete
const { progress, refreshProgress } = useProgress();

// Check chapter quiz completion
const chapterScore = progress?.chapters.find(
  (c) => c.slug === currentChapterSlug,
);
const hasCompletedQuiz = !!chapterScore;
const bestScore = chapterScore?.best_score;

// Check lesson completion
const isLessonDone = chapterScore?.lessons_completed.some(
  (l) => l.lesson_slug === currentLessonSlug,
);
```

**Where progress surfaces in the UI**:

| Location                     | What's Shown                                                                               | Phase |
| ---------------------------- | ------------------------------------------------------------------------------------------ | ----- |
| **Quiz page (before start)** | "Your best: 85% / Attempts: 2" if previous attempts exist                                  | 1     |
| **Quiz page (after submit)** | XP earned, new badges, streak update (from submit response)                                | 1     |
| **Lesson page (bottom)**     | "Mark as Complete" button. Shows "Completed" state if already done.                        | 1     |
| **Progress dashboard**       | Full stats, chapter scores, lessons completed per chapter, badge gallery, leaderboard rank | 1     |
| **Sidebar items**            | Checkmark next to completed lessons + score badge next to completed chapters               | 2     |
| **Navbar**                   | XP counter (always visible)                                                                | 2     |
| **Chapter landing page**     | Progress bar showing lessons completed + quiz score                                        | 2     |

**Phase 1 delivers both quiz persistence AND lesson completion tracking**: quiz page shows previous scores, lesson pages have a "Mark as Complete" button, dashboard shows everything including per-chapter lesson completion counts. Phase 2 adds the inline sidebar indicators that make progress visible while browsing.

---

## 11. XP Economics

### Base XP Sources

| Activity                       | XP Earned            | Frequency                     | Phase |
| ------------------------------ | -------------------- | ----------------------------- | ----- |
| Quiz completion (1st attempt)  | 0-100 XP (= score %) | Per chapter quiz              | 1     |
| Quiz improvement (2nd attempt) | improvement × 0.5    | Per reattempt                 | 1     |
| Quiz improvement (3rd attempt) | improvement × 0.25   | Per reattempt                 | 1     |
| Teach mode session (5+ turns)  | 10 XP                | Per session, max 3/day/lesson | 2     |
| Ask mode usage (per lesson)    | 5 XP                 | Per unique lesson, once       | 2     |
| Lesson completion              | 5 XP                 | Per lesson, once              | 2     |

### Bonus XP (Phase 2+)

| Bonus Type              | Multiplier | Trigger                                  |
| ----------------------- | ---------- | ---------------------------------------- |
| **Streak Bonus**        | 1.5x       | Active streak >= 7 days                  |
| **Perfect Score Bonus** | +25 XP     | 100% on first attempt                    |
| **First-of-Day Bonus**  | +10 XP     | First activity of the day                |
| **Chapter Sweep Bonus** | +50 XP     | Complete ALL lessons + quiz in a chapter |
| **Weekend Challenge**   | 2x         | Platform event (bi-weekly)               |

### Anti-Gaming Rules

- Max 3 Teach sessions per lesson per day count toward XP
- Ask mode XP: once per unique lesson
- Quiz reattempt XP: diminishing returns
- No XP for page views alone

---

## 12. Implementation Phases

### Phase 1: Foundation MVP — 3-4 weeks

**Goal**: Quiz scores persist, lesson completion tracked, XP works, basic dashboard exists.

| Task                                | Description                                                                                                    |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Progress API service scaffold       | FastAPI app with JWKS auth (copy pattern from study-mode-api), PostgreSQL, health check                        |
| Database schema                     | users, chapters, chapter_aliases, quiz_attempts, lesson_completions, user_progress, user_badges, activity_days |
| Leaderboard materialized view       | + scheduled refresh job                                                                                        |
| `POST /api/v1/quiz/submit`          | Full atomic transaction: persist + XP + badges + streak + summary update                                       |
| `POST /api/v1/lesson/complete`      | Idempotent completion: persist + active_duration + streak + summary update                                     |
| `GET /api/v1/progress/me`           | Pre-computed dashboard data from user_progress + badges + chapter scores + lessons completed                   |
| `GET /api/v1/leaderboard`           | From materialized view + current user rank                                                                     |
| Frontend: Quiz.tsx `onComplete`     | Add callback prop, wire to API                                                                                 |
| Frontend: "Mark as Complete" button | Lesson page footer button, active time timer (visibilitychange API), POST on click                             |
| Frontend: XP notification           | Toast/modal showing XP earned + new badges from submit response                                                |
| Frontend: Progress dashboard page   | Stats, chapter progress, lesson completion counts, badge gallery                                               |

### Phase 2: Social + Retention — 1-2 weeks

| Task                                    | Description                                |
| --------------------------------------- | ------------------------------------------ |
| Streak grace period                     | 1 free streak freeze per week              |
| `study_sessions` table                  | Track Teach/Ask sessions as activity       |
| Teach/Ask → streak                      | Count completed sessions as active day     |
| `PATCH /api/v1/progress/me/preferences` | Leaderboard opt-out                        |
| Frontend: Leaderboard page              | Rankings table with current user highlight |
| Frontend: XP counter in navbar          | Always-visible motivation                  |
| Badge unlock animations                 | Satisfying unlock moments                  |

### Phase 3: Engine Integration + xAPI — 2-3 weeks

| Task                             | Description                                            |
| -------------------------------- | ------------------------------------------------------ |
| Mode-agnostic mastery endpoint   | `POST /api/v1/sessions/complete` for any mode          |
| Lesson XP rewards                | 5 XP per lesson completion (once per lesson)           |
| xAPI statement emitter           | Emit xAPI statements from progress-api to LRS          |
| LearnMCP-xAPI integration        | MCP server for AI agent access to learning data        |
| Token usage dashboard            | Surface "AI Credits Used" from token-metering-api      |
| Bonus XP engine                  | Streak multiplier, first-of-day, perfect score bonuses |
| Tiered badge system              | Bronze/Silver/Gold versions of activity badges         |
| `GET /api/v1/progress/me/export` | GDPR data export                                       |

### Phase 4: Advanced — Future

| Task                      | Description                                               |
| ------------------------- | --------------------------------------------------------- |
| Socratic mode integration | Mastery scoring via graders                               |
| Concept-level progress    | Track mastery per concept, not just per chapter           |
| Spaced repetition         | Return to weakest concepts after N days                   |
| Achievement sharing       | Share badges to social media                              |
| Weekend Challenge events  | Bi-weekly 2x XP events                                    |
| Streak Freeze mechanic    | Earned through high quiz scores                           |
| Hidden badges             | Surprise badges for unusual behaviors (GitHub YOLO style) |

---

## 13. Success Metrics

| Metric                       | Baseline (now)        | Target (3 months post-launch) |
| ---------------------------- | --------------------- | ----------------------------- |
| Quiz completion rate         | Unknown (no tracking) | Measurable + 20% from Month 1 |
| 7-day return rate            | Unknown               | 30%+                          |
| Quiz retake rate             | Unknown               | 15%+ (users improving scores) |
| Average quizzes per user     | Unknown               | 5+ per month                  |
| Leaderboard page views       | 0                     | 500+ unique/month             |
| Streak maintenance (7+ days) | 0                     | 10% of active users           |

---

## 14. Dependency Map

```
                        ┌──────────────┐
                        │     SSO      │
                        │ (JWT tokens) │
                        └──────┬───────┘
                               │ auth (JWKS, no per-request calls)
    ┌──────────────────────────┼──────────────────────────┐
    │                          │                          │
┌───▼────────────┐   ┌────────▼────────┐   ┌─────────────▼──┐
│ study-mode-api │   │  progress-api   │   │agentfactory-api│
│ (Teach/Ask)    │   │  (NEW)          │   │(Personalize)   │
│                │   │                 │   │                │
│ threads ───────┼──►│ sessions (Ph2)  │   │                │
│ messages       │   │ quiz scores     │   │                │
└────────────────┘   │ lesson complete │   └────────────────┘
                     │ XP/badges       │
                     │ leaderboard     │
┌────────────────┐   │ user identity   │
│token-metering  │   │ (from JWT)      │
│(credits/usage) ├──►│ token dash (Ph3)│
└────────────────┘   └───────┬─────────┘
                             │ emits xAPI statements (Ph3)
                     ┌───────▼─────────┐
                     │  xAPI LRS       │
                     │  (Phase 3)      │
                     │  LearnMCP-xAPI  │
                     └───────┬─────────┘
                             │
                     ┌───────▼─────────┐
                     │   learn-app     │
                     │   (frontend)    │
                     │                 │
                     │ Quiz.tsx        │
                     │ Dashboard       │
                     │ Leaderboard     │
                     │ Badge Gallery   │
                     │ XP Counter      │
                     └─────────────────┘
```

---

## 15. Risk Assessment

| Risk                                   | Impact                | Mitigation                                                           |
| -------------------------------------- | --------------------- | -------------------------------------------------------------------- |
| XP farming (bot accounts)              | Leaderboard integrity | Rate limit quiz attempts, require auth, CAPTCHAs if needed           |
| Curriculum restructure breaks progress | User trust            | Content-addressed architecture (DB-owned IDs, aliases, soft deletes) |
| Backend not ready when frontend ships  | Dead UI               | Ship backend first (Phase 1), then wire frontend                     |
| Over-gamification cheapens learning    | Brand damage          | Keep it scholarly — Polar Night aesthetic, no flashy animations      |
| Streak pressure causes burnout         | User churn            | Grace period (1 day), no public streak display                       |
| Privacy concerns (leaderboard)         | GDPR/trust            | Opt-out mechanism, anonymous display option                          |
| Quiz randomization affects XP fairness | User perception       | Track score %, not absolute — randomization makes gaming harder      |

---

## Appendix A: PR #680 Assessment

PR #680 (`feat/user-progress`, 6 commits, 4656 additions) contains frontend gamification UI with mock data. **Do not merge. Cherry-pick reusable code into the new implementation.**

### Documents (Reference Only)

| File                            | Verdict   | Notes                                                                                                                                                                                                                   |
| ------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `gamified-progress-feat-prd.md` | Reference | Good XP formula and badge definitions. Our spec supersedes all decisions. Schema uses UUIDs (we use slugs), uses `"ch-11"` format (we use URL slugs), no lesson completion.                                             |
| `decision-progress.md`          | Reference | Thoughtful content-addressed architecture discussion. We've already adopted the good ideas (soft deletes, immutable XP, summary tables, materialized views) and improved on the weak ones (URL slugs instead of UUIDs). |

### Code — Reuse (with modifications)

| File                  | Lines | Reuse % | What to change                                                                                                                                                                        |
| --------------------- | ----- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `progress-types.ts`   | 130   | ~80%    | Add `LessonCompletion` type, add `lessons_completed` to `ChapterScore`, change `chapterId` from `"ch-11"` to slug format. `BADGE_DEFINITIONS` constant is directly usable.            |
| `ProgressContext.tsx` | 195   | ~70%    | Good structure: auth-gated loading, optimistic updates, XP animation state, `useXP()`/`useStreak()`/`useBadges()` hooks. Add `completeLesson()` action. **Fix auth bug** (see below). |
| `progress-api.ts`     | 270   | ~50%    | `apiFetch` wrapper is solid. `submitQuizScore` needs slug-based payload. Add `completeLesson()`. **Remove all mock data** (~150 lines). **Fix auth** (see below).                     |
| `gamification.css`    | 403   | ~90%    | Clean oklch color tokens for XP/streak/rank. Review against current Polar Night theme. Mostly usable as-is.                                                                           |
| `BadgeCard.tsx`       | ~80   | ~90%    | Clean component using `BADGE_DEFINITIONS`. Minor Polar Night review.                                                                                                                  |
| `QuizXPModal.tsx`     | ~120  | ~80%    | Animated XP counter, badge unlock display. Update to accept our response shape.                                                                                                       |
| `XPCounter.tsx`       | 226   | ~60%    | `useAnimatedNumber` hook is good. Dropdown stats preview is nice UX. Update data model.                                                                                               |

### Code — Rebuild

| File                    | Lines | Why                                                                                                                                             |
| ----------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `ProgressDashboard.tsx` | 367   | Hardcoded chapter names, `"ch-1"` IDs, no lesson completion section. Data model is wrong throughout. Keep layout structure as visual reference. |
| `Leaderboard.tsx`       | 566   | Overcomplicated (566 lines). Inline badge modal, mock data generation. Our spec calls for simpler component reading from materialized view.     |
| `BadgeUnlockModal.tsx`  | ~100  | CSS confetti animations conflict with "scholarly, Polar Night aesthetic, no flashy animations" from risk assessment.                            |

### Code — Take as-is (with minor edits)

| File                           | Notes                                                                                                   |
| ------------------------------ | ------------------------------------------------------------------------------------------------------- |
| `pages/progress.tsx`           | 15 lines, wraps `<ProgressDashboard />` in Layout.                                                      |
| `pages/leaderboard.tsx`        | 15 lines, wraps `<Leaderboard />` in Layout.                                                            |
| `components/progress/index.ts` | Barrel export file.                                                                                     |
| `theme/Root.tsx`               | Adds `<ProgressProvider>` wrapper. Correct pattern. Remove `useMockData` flag — ship with real backend. |

### Discard

| File/Dir                                    | Why                                 |
| ------------------------------------------- | ----------------------------------- |
| `.claude/handoffs/*` (4 files)              | Session artifacts, no reuse value   |
| `.claude/logs/*` (6 files)                  | Debug logs from development         |
| `.claude/skills/frontend-design/*`          | Skill created during PR, not needed |
| Mock data in `progress-api.ts` (~150 lines) | Ship with real backend, not mocks   |
| `pnpm-lock.yaml` changes                    | Stale, must regenerate              |

### Critical Auth Bug

```typescript
// PR 680 (WRONG — access_token is for SSO userinfo endpoint):
return localStorage.getItem("ainative_access_token");

// Correct (id_token is the JWT with sub/name/email for JWKS verification):
return localStorage.getItem("ainative_id_token");
```

All services (study-mode-api, token-metering-api) verify `id_token` via JWKS. The `access_token` is an opaque token for SSO's own endpoints.

### No New Dependencies Required

Radix UI components (`dialog`, `avatar`, `dropdown-menu`, `tooltip`) and `lucide-react` already exist on main branch. No package.json changes needed from this PR.

### Recommendation

Start fresh from `main`. Cherry-pick reusable files (`progress-types.ts`, `gamification.css`, `BadgeCard.tsx`, page shells). Close PR #680 with comment linking to this spec.

## Appendix B: Industry Badge Research

### Badge Design Principles (Synthesized from Google, GitHub, Duolingo)

| Principle                  | Source            | Our Application                           |
| -------------------------- | ----------------- | ----------------------------------------- |
| **Tiered progression**     | Google, GitHub    | Bronze/Silver/Gold versions of key badges |
| **Activity-based earning** | GitHub            | Badges from doing, not just scoring       |
| **Shareable credentials**  | Google            | Profile page with public badge display    |
| **Surprise/delight**       | GitHub (YOLO)     | Hidden badges for unexpected achievements |
| **Grace period**           | Duolingo (Freeze) | 1 streak freeze per week                  |
| **Time-limited events**    | Duolingo (2x XP)  | Weekend/monthly bonus XP challenges       |

### Duolingo Engagement Data

- Streaks increase commitment by **60%**
- XP leaderboards drive **40% more engagement**
- Users who hit 7-day streak are **3.6x more likely** to stay engaged
- Streak Freeze reduced churn by **21%**
- Limited-time XP boosts → **50% activity surge**

## Appendix C: Study Mode API Signals Available Today

**Already persisted** (can be queried for gamification in Phase 2):

- `threads.lesson_path` — which lesson was studied
- `threads.created_at` — when study started
- `items.created_at` — per-message timestamps
- `threads.data.mode` — "teach" or "ask"
- `items.data.role` — user vs assistant turn count

**Available but not captured**:

- Teach mode correctness (needs post-hoc evaluation)
- Ask mode highlighted text (in metadata, not aggregated)
- Session completion signal (no explicit "done studying" event)
- Concept-level tagging (messages aren't tagged to specific concepts)
