# Practice Environment: Production Implementation Plan

**Issue**: #717 | **PR**: #725 (draft) | **Issue**: #726
**Status**: Plan review complete (2 rounds, 30 decisions), ready for implementation
**Date**: 2026-02-13

## Overview

This plan refactors the v0.1 prototype into a production-quality practice environment for 50k+ active users. It is the result of two rounds of interactive review:

- **Round 1** (15 issues): Architecture, Code Quality, Tests, Performance review of v0.1 prototype
- **Round 2** (15 issues): Architecture, Code Quality, Tests, Performance review of the plan itself

All 30 decisions were made interactively with the project lead.

---

## Decision Record

### Round 1: v0.1 Prototype Review

| # | Issue | Decision | Rationale |
|---|-------|----------|-----------|
| 1+2 | Command injection + cross-platform shell deps | Replace all shell commands with Node.js native APIs (`fs.cp`, `fs.rm`, `readdir` + `extract-zip`) | Eliminates injection vector AND Windows incompatibility in one refactor |
| 3 | Origin validation dead code + DRY violation | Keep `origin.ts` as single source of truth, import in `terminal.ts`, delete inline duplicate | Security policy should be auditable in one file |
| 4 | Blocking `execFileSync` on every health poll | Cache `claude` path at startup, serve from cache forever | Binary doesn't appear/disappear mid-session |
| 5 | Hand-rolled HTTP client (70 lines) | Replace `httpsGet`/`httpsGetJson` with native `fetch()` | Node 18+ built-in, delete 70 lines |
| 6 | No input validation on routes | Zod schema validation | Scales better than manual checks, type-safe request parsing |
| 7 | Session cleanup race conditions | Fix ordering: detach WS -> kill PTY -> delete from Map -> spawn | StrictMode dedup already handles concurrent requests |
| 8 | Errors not surfaced to frontend | Typed error responses `{ code, message, action }` | 50k non-tech users need self-service error recovery |
| 9 | No server tests | Full suite: unit + integration + E2E (after refactor) | Production release to 50k users requires comprehensive coverage |
| 10 | No frontend tests | Full suite: hook + component + context flow | Same reasoning as #9 |
| 11 | No cross-platform CI | GitHub Actions matrix (macOS, Ubuntu, Windows) | Catches node-pty compilation and fs behavior differences |
| 12 | ZIP loaded into memory | Stream to disk via fetch response stream | Constant memory regardless of ZIP size |
| 13 | No download timeout | `AbortSignal.timeout(30_000)` on fetch | Prevents infinite hangs, returns `DOWNLOAD_TIMEOUT` typed error |
| 14 | No WebSocket heartbeat | Server-side ping/pong (configurable interval, default 30s/10s) | Detects dead connections from laptop sleep / WiFi switch |
| 15 | Claude path resolved on every session start | Reuse startup cache from Decision #4 | One-line change, zero latency on session start |

### Round 2: Plan Review

| # | Issue | Decision | Rationale |
|---|-------|----------|-----------|
| 16 | yauzl is callback-based, complex to use | Use `extract-zip` (Mozilla, wraps yauzl with promise API) | `await extract(src, {dir})` — one line vs 30 lines of callback wrangling |
| 17 | Typed errors don't cover async WebSocket events | Send `{ type: "error", error: AppError }` as WS text frame before closing | PTY_EXITED happens after HTTP 200 — need structured error on WS channel |
| 18 | Phase 1 fully sequential — 2/3 agents idle | Parallelize: frontend-engineer handles Tasks 1.4+1.7 after Task 1.1 | Zero file overlap between tracks, maximizes team capacity |
| 19 | No graceful degradation if node-pty prebuild unavailable | CLI catches node-pty import failure, prints human-readable platform-specific message | Transforms cryptic npm ERR! into actionable guidance for 50k non-tech users |
| 20 | CORS origin regex in 3 locations, Task 1.4 only fixes 2 | Export `ALLOWED_ORIGIN` regex from `origin.ts`, use in main.ts CORS + terminal.ts | Single source of truth for origin policy |
| 21 | Tasks 1.1 and 1.5 overlap on claude path resolution | Move ALL claude path work to Task 1.5 only — Task 1.1 focuses on workspace.ts | Clean boundary, no overlapping scope between tasks |
| 22 | Error recovery UX undefined | Create `PracticeErrorCard` component + error→UX mapping table | Frontend engineer needs explicit spec for what each error renders |
| 23 | No workspace version/freshness mechanism | Add `--refresh` CLI flag to clear cached workspaces | Simple, user-controlled, low effort. Version tracking deferred to v0.2 |
| 24 | bin/cli.ts has no test coverage | Add CLI E2E tests to Task 4.3 (--version, --port, --refresh, startup) | CLI is first user touchpoint — must be tested |
| 25 | WebSocket heartbeat tests timing-sensitive | Make heartbeat intervals configurable (constructor params, short values in tests) | Tests use 100ms/50ms — deterministic, runs in <1s |
| 26 | Learn-app has zero test infrastructure | Split Task 4.4 into 4.4a (Vitest setup) + 4.4b (write tests) | Acknowledge infra gap explicitly so engineer plans for it |
| 27 | Test fixture ZIP contents undefined | Specify fixture structure in plan (GitHub zipball pattern, nested modules, sub-exercises) | Integration tests need known structure to assert against |
| 28 | Terminal resize events not debounced | Debounce FitAddon.fit() with 150ms delay | Prevents TUI flicker during overlay drag |
| 29 | Health poll continues after session established | Stop poll on WS connect, resume on disconnect | Clean lifecycle management, reduces noise |
| 30 | Concurrent downloads for same exercise (TOCTOU) | Promise-based download lock per exerciseId | 10 lines, eliminates race from StrictMode double-mount |

### New Dependencies

| Package | Purpose | Where |
|---------|---------|-------|
| `zod` | Request schema validation (Decision #6) | practice-server |
| `extract-zip` | Cross-platform ZIP extraction with promise API (Decision #16) | practice-server |

### Removed Code

| What | Why |
|------|-----|
| `httpsGet()` / `httpsGetJson()` in workspace.ts | Replaced by native `fetch()` (Decision #5) |
| Inline origin regex in terminal.ts | Replaced by import from `origin.ts` (Decision #3) |
| Inline origin regex in main.ts CORS | Replaced by import from `origin.ts` (Decision #20) |
| Shell commands: `unzip`, `cp -a`, `rm -rf`, `find`, `ls -d` | Replaced by Node fs APIs + extract-zip (Decision #1+2) |
| `execFileSync` in health.ts | Replaced by startup cache (Decision #4) |
| `resolveClaudePath()` per-call shell spawn | Replaced by startup cache (Decision #15, scoped to Task 1.5 per Decision #21) |

---

## Error→UX Mapping (Decision #22)

When the frontend receives a typed error (HTTP or WebSocket), display as follows:

| Error Code | UI Component | Message | Retry Strategy |
|------------|-------------|---------|----------------|
| `CLAUDE_NOT_FOUND` | PracticeSetupCard | "Claude Code not found" + install link | Manual (after installing) |
| `EXERCISE_NOT_FOUND` | PracticeErrorCard | "This exercise isn't available yet" | No retry |
| `DOWNLOAD_FAILED` | PracticeErrorCard | "Couldn't download exercise files" + Try Again | Auto-retry once, then manual |
| `DOWNLOAD_TIMEOUT` | PracticeErrorCard | "Download timed out — check your internet" + Try Again | Manual |
| `EXTRACTION_FAILED` | PracticeErrorCard | "Corrupted download — try `--refresh`" | Manual |
| `PTY_SPAWN_FAILED` | PracticeErrorCard | "Couldn't start Claude Code — check installation" | Manual |
| `PTY_EXITED` | PracticeErrorCard (in terminal) | "Claude Code exited" + Restart button | Manual |
| `SESSION_NOT_FOUND` | (silent) | Auto-create new session | Automatic |
| `INVALID_REQUEST` | (should never reach user) | Developer bug | No retry |

---

## Implementation Phases

### Phase 1: Server Hardening (Refactor)

Refactor practice-server to be production-quality, cross-platform, and secure.

**Goal**: All round-1 review decisions implemented. Server works on macOS, Linux, Windows.

**Execution**: Two parallel tracks after Task 1.1 completes.

```
Track A (server-engineer):    1.1 → 1.2 → 1.3 → 1.5 → 1.6
Track B (frontend-engineer):  (wait for 1.1) → 1.4 + 1.7
```

Track B touches only `terminal.ts` and `origin.ts` — zero file overlap with Track A.

#### Task 1.1: Replace shell commands with Node APIs

**Agent**: server-engineer
**Files**: `apps/practice-server/src/exercises/workspace.ts`, `apps/practice-server/package.json`

- Replace `unzip` with `extract-zip` (`await extract(zipPath, { dir: targetDir })`) — Decision #16
- Replace `cp -a` with `fs.cp()` (Node 16.7+ recursive copy)
- Replace `rm -rf` with `fs.rm()` (Node 14.14+ recursive remove)
- Replace `find -type d` and `ls -d` with `fs.readdir()` recursive search
- Replace `httpsGet`/`httpsGetJson` with native `fetch()`
- Add `AbortSignal.timeout(30_000)` to all fetch calls
- Stream ZIP to disk: pipe `response.body` through `fs.createWriteStream`
- Add promise-based download lock (Decision #30):

```typescript
const inFlightDownloads = new Map<string, Promise<string>>();

export async function downloadAndExtract(exerciseId: string): Promise<string> {
  const existing = inFlightDownloads.get(exerciseId);
  if (existing) return existing;

  const promise = doDownloadAndExtract(exerciseId);
  inFlightDownloads.set(exerciseId, promise);
  try { return await promise; }
  finally { inFlightDownloads.delete(exerciseId); }
}
```

- Add `extract-zip` to package.json
- **Do NOT touch claude path resolution** — that's Task 1.5 (Decision #21)

**Acceptance criteria**:
- Zero shell commands remain in workspace.ts
- `pnpm nx serve practice-server` starts on macOS
- Exercise download + extraction works end-to-end
- Concurrent downloads for same exercise are deduplicated
- TypeScript compiles clean

#### Task 1.2: Typed error system

**Agent**: server-engineer (after 1.1)
**Files**:
- Create `apps/practice-server/src/errors.ts`
- Modify `apps/practice-server/src/routes/sessions.ts`
- Modify `apps/practice-server/src/exercises/workspace.ts`
- Modify `apps/practice-server/src/pty/manager.ts`
- Modify `apps/practice-server/src/ws/terminal.ts` (WebSocket error frames — Decision #17)

Error codes:

```typescript
type ErrorCode =
  | 'CLAUDE_NOT_FOUND'
  | 'EXERCISE_NOT_FOUND'
  | 'DOWNLOAD_FAILED'
  | 'DOWNLOAD_TIMEOUT'
  | 'EXTRACTION_FAILED'
  | 'PTY_SPAWN_FAILED'
  | 'PTY_EXITED'
  | 'SESSION_NOT_FOUND'
  | 'INVALID_REQUEST';

interface AppError {
  code: ErrorCode;
  message: string;
  action?: string;
}
```

WebSocket error delivery (Decision #17):
```typescript
// In manager.ts onExit handler or terminal.ts:
// Send typed error as text frame before closing WebSocket
if (session.ws?.readyState === WebSocket.OPEN) {
  session.ws.send(JSON.stringify({
    type: 'error',
    error: { code: 'PTY_EXITED', message: 'Claude Code exited', action: 'Click Restart to begin a new session' }
  }));
  session.ws.close(1000, 'process_exited');
}
```

**Acceptance criteria**:
- All HTTP error paths return structured `{ error: AppError }` responses
- All async PTY events send typed errors via WebSocket text frames
- No generic 500s remain
- Frontend can switch on `error.code` for both HTTP and WebSocket errors

#### Task 1.3: Zod input validation

**Agent**: server-engineer (after 1.2)
**Files**:
- Modify `apps/practice-server/src/routes/sessions.ts`
- Add `zod` to package.json

```typescript
const StartSessionSchema = z.object({
  exerciseId: z.string().min(1).regex(/^[\w-]+$/),
  subExercise: z.string().regex(/^[\w.-]+$/).optional(),
});
```

**Acceptance criteria**:
- Invalid requests return 400 with `INVALID_REQUEST` typed error
- `subExercise` with special characters is rejected before reaching any file operation
- TypeScript types inferred from Zod schemas

#### Task 1.4: Origin validation consolidation

**Agent**: frontend-engineer (after 1.1, parallel with Track A)
**Files**:
- Modify `apps/practice-server/src/middleware/origin.ts`
- Modify `apps/practice-server/src/ws/terminal.ts`
- Modify `apps/practice-server/src/main.ts` (Decision #20)

- Export `ALLOWED_ORIGIN` regex constant from `origin.ts`
- Import in `terminal.ts` (replace inline regex)
- Import in `main.ts` for CORS config: `cors({ origin: ALLOWED_ORIGIN })`
- Keep `isValidOrigin()` function for WebSocket validation

**Acceptance criteria**:
- `origin.ts` exports both `ALLOWED_ORIGIN` regex and `isValidOrigin()` function
- `terminal.ts` imports and uses `isValidOrigin()`
- `main.ts` imports and uses `ALLOWED_ORIGIN` for CORS
- Zero duplicate regex anywhere in codebase (verified by grep)

#### Task 1.5: Startup cache + health refactor

**Agent**: server-engineer (after 1.3)
**Files**:
- Modify `apps/practice-server/src/main.ts`
- Modify `apps/practice-server/src/routes/health.ts`
- Modify `apps/practice-server/src/pty/manager.ts`

This task owns ALL claude path resolution (Decision #21):
- At server startup: resolve claude path once using `resolveClaudePath()`, store result
- Export `getCachedClaudePath(): string | null`
- Health endpoint reads from cache (no `execFileSync`)
- `spawnSession()` uses cached path instead of calling `resolveClaudePath()`
- If claude not found at startup, server still starts but health returns `{ claudeInPath: false }`
- Remove per-call `resolveClaudePath()` from manager.ts (move resolution logic to main.ts startup)

**Acceptance criteria**:
- Zero `execFileSync` calls after startup
- Health endpoint is non-blocking
- `spawnSession` uses cached path
- `resolveClaudePath()` called exactly once (at startup)

#### Task 1.6: Session cleanup ordering

**Agent**: server-engineer (after 1.5)
**Files**: `apps/practice-server/src/pty/manager.ts`

- When killing existing session: detach WS first, then kill PTY, then delete from Map
- Ensure `onExit` handler doesn't double-delete

**Acceptance criteria**:
- No dangling WS event listeners after session kill
- Clean PTY shutdown (no zombie processes)

#### Task 1.7: WebSocket heartbeat

**Agent**: frontend-engineer (after 1.1, parallel with Track A)
**Files**: `apps/practice-server/src/ws/terminal.ts`

- Add configurable ping interval (default 30s) after WebSocket connection (Decision #25)
- Terminate connection if no pong within configurable timeout (default 10s)
- Clear interval on connection close
- Accept `{ pingInterval, pongTimeout }` as parameters (short values for tests)

```typescript
// Constructor/function accepts options for testability
interface HeartbeatOptions {
  pingInterval?: number;  // ms, default 30000
  pongTimeout?: number;   // ms, default 10000
}
```

**Acceptance criteria**:
- Dead connections detected within `pingInterval + pongTimeout` (40s default)
- Terminal reconnects automatically after network interruption
- Heartbeat intervals configurable for testing

---

### Phase 2: npm Package Distribution

Package practice-server as `npx @agentfactory/practice-server` for end users.

**Goal**: Users run one command to start the practice server. No git clone, no dev setup.

#### Task 2.1: Package structure + CLI

**Agent**: server-engineer
**Files**:
- Create `apps/practice-server/bin/cli.ts` (CLI entry point)
- Modify `apps/practice-server/package.json` (add `bin` field, `@agentfactory/practice-server` name)
- Modify `apps/practice-server/tsconfig.json` (output to `dist/`)

CLI behavior:
```
npx @agentfactory/practice-server
  → starts server on :3100
  → prints banner with URL + health check status
  → checks for claude in PATH, warns if not found

npx @agentfactory/practice-server --port 3200
  → custom port

npx @agentfactory/practice-server --version
  → prints version

npx @agentfactory/practice-server --refresh
  → clears ~/af-practice/ cache, then starts server (Decision #23)
```

node-pty import failure detection (Decision #19):
```typescript
try {
  require('node-pty');
} catch (e) {
  console.error('Could not load terminal support (node-pty).');
  console.error('');
  if (process.platform === 'darwin') {
    console.error('  Fix: xcode-select --install');
  } else if (process.platform === 'linux') {
    console.error('  Fix: sudo apt-get install -y build-essential');
  } else {
    console.error('  Your platform may need a C++ compiler.');
  }
  console.error('');
  console.error('Or use the manual exercise download workflow instead.');
  process.exit(1);
}
```

**Acceptance criteria**:
- `npx @agentfactory/practice-server` starts server from published package
- Banner shows version, port, claude status
- `--port`, `--version`, and `--refresh` flags work
- node-pty import failure shows human-readable platform-specific message

#### Task 2.2: node-pty prebuilds

**Agent**: server-engineer
**Files**:
- Modify `apps/practice-server/package.json` (configure node-pty prebuild)
- Create `.github/workflows/practice-server-release.yml`

Supported platforms:
- macOS arm64 (Apple Silicon)
- macOS x64 (Intel)
- Linux x64
- Windows x64

**Acceptance criteria**:
- `npm install @agentfactory/practice-server` does NOT require C++ toolchain
- Prebuilt binary downloads automatically for target platform
- CI workflow publishes to npm on GitHub release

#### Task 2.3: Setup card + error card + frontend refinements

**Agent**: frontend-engineer
**Files**:
- Create `apps/learn-app/src/components/PracticeSetupCard/index.tsx`
- Create `apps/learn-app/src/components/PracticeErrorCard/index.tsx` (Decision #22)
- Modify `apps/learn-app/src/components/TerminalPanel/index.tsx`
- Modify `apps/learn-app/src/components/TerminalPanel/usePracticeServer.ts`

**PracticeSetupCard** (server not running):
- "Run this command to start the practice server:"
- Copyable command: `npx @agentfactory/practice-server`
- "Don't have Claude Code?" expandable with install link
- Auto-retry health check every 5s, auto-hide when server detected

**PracticeErrorCard** (typed errors — Decision #22):
- Renders error.message + error.action text
- Contextual UI per error code (see Error→UX Mapping table above)
- "Try Again" button for retryable errors
- "Restart" button for PTY_EXITED

**TerminalPanel refinements**:
- Debounce FitAddon.fit() with 150ms delay (Decision #28)
- Handle `{ type: "error" }` WebSocket text frames — show PracticeErrorCard in terminal area

**usePracticeServer refinements**:
- Stop health polling when WebSocket connects, resume on disconnect (Decision #29)

**Acceptance criteria**:
- Setup card appears when server is not running, disappears when detected
- Error card renders for each error code per the mapping table
- Copy button works on setup card
- No TUI flicker during overlay resize drag
- Health poll stops during active session

---

### Phase 3: Exercise Content

Add ExerciseCard markers to remaining exercise lessons and verify all exercise packs work.

**Goal**: All 4 exercise packs (basics, skills, plugins, agent-teams) have working ExerciseCard components.

#### Task 3.1: Add ExerciseCard markers to remaining lessons

**Agent**: frontend-engineer
**Files**: Exercise lesson MDX files in `apps/learn-app/docs/01-General-Agents-Foundations/03-seven-principles/`

- Audit which lessons have exercise packs but no ExerciseCard components
- Add ExerciseCard MDX component for each exercise in each lesson
- Verify exercise IDs match registry entries

**Acceptance criteria**:
- All 4 exercise lessons have ExerciseCard components
- Each card's exerciseId matches an entry in `registry.ts`
- Cards render correctly in Docusaurus

#### Task 3.2: Verify all exercise packs download and extract

**Agent**: test-engineer
**Files**: None (manual + automated verification)

- Test each registry entry: start session, verify ZIP downloads, extracts, Claude Code starts
- Verify sub-exercise resolution works for nested exercises
- Document any broken GitHub release URLs

**Acceptance criteria**:
- All 4 exercise packs download successfully
- Sub-exercise directory resolution works for each pack
- INSTRUCTIONS.md auto-read works in each workspace

---

### Phase 4: Testing & CI

Comprehensive test suite + cross-platform CI.

**Goal**: Full confidence that the practice environment works on all Tier 1 platforms.

#### Task 4.1: Server unit tests

**Agent**: test-engineer
**Files**: `apps/practice-server/src/__tests__/unit/`

Test pure functions:
- `origin.ts`: valid/invalid origins, edge cases (empty, IPv6, port ranges, `ALLOWED_ORIGIN` regex)
- `errors.ts`: error code to message mapping, AppError creation helpers
- `registry.ts`: known exercise lookup, unknown exercise returns undefined
- Zod schemas: valid/invalid inputs, edge cases (special chars, empty strings, missing fields)

Test setup: Vitest (add to practice-server if not already in monorepo)

**Acceptance criteria**:
- All pure functions have >95% branch coverage
- Tests pass on macOS, Linux, Windows (CI matrix)

#### Task 4.2: Server integration tests

**Agent**: test-engineer
**Files**: `apps/practice-server/src/__tests__/integration/`, `apps/practice-server/src/__tests__/fixtures/`

Test I/O operations:
- `workspace.ts`: create workspace dir, download fixture ZIP, extract, verify file structure
- `workspace.ts`: stream large ZIP without memory spike
- `workspace.ts`: handle download timeout gracefully
- `workspace.ts`: handle missing/corrupt ZIP
- `workspace.ts`: concurrent download deduplication (promise lock)
- `manager.ts`: spawn PTY (using `node -e "process.stdout.write('hello')"` for cross-platform CI), verify I/O

**Test fixture ZIP structure** (Decision #27):

Create `apps/practice-server/src/__tests__/fixtures/test-exercise.zip` with this structure:

```
test-exercise/                          ← top-level dir (GitHub zipball pattern)
├── CLAUDE.md
├── INSTRUCTIONS.md
├── module-1/
│   ├── exercise-1.1-first-task/
│   │   └── INSTRUCTIONS.md
│   └── exercise-1.2-second-task/
│       └── INSTRUCTIONS.md
└── module-2/
    └── exercise-2.1-third-task/
        └── INSTRUCTIONS.md
```

This exercises: top-level unwrapping (GitHub zipball pattern), nested module structure, sub-exercise directory resolution at depth 2 and 3, INSTRUCTIONS.md presence.

**Acceptance criteria**:
- Workspace creation/extraction tested with real filesystem
- Error paths tested (timeout, corrupt ZIP, missing exercise, concurrent downloads)
- No `claude` binary required (mock with `node -e` command)
- Fixture ZIP committed to repo

#### Task 4.3: Server E2E tests + CLI tests

**Agent**: test-engineer
**Files**: `apps/practice-server/src/__tests__/e2e/`

Test full server:
- Start server, hit health endpoint, verify response shape
- Start session with valid exercise, verify response
- Start session with invalid exercise, verify typed error
- WebSocket connection, send keystrokes, receive output
- WebSocket heartbeat ping/pong (using short configurable intervals — Decision #25)
- WebSocket error frame delivery (Decision #17)
- Session reconnection after WebSocket disconnect

CLI tests (Decision #24):
- `--version` prints version and exits with code 0
- `--port 3200` starts server on specified port
- `--refresh` clears workspace cache
- Default invocation starts on port 3100
- node-pty import failure shows human-readable message (mock the import)

**Acceptance criteria**:
- Full request lifecycle tested
- WebSocket protocol tested (binary + text frames + error frames)
- Heartbeat tests run in <1s (configurable intervals)
- Graceful error responses for all failure modes
- CLI flags tested
- Tests use a mock PTY command (not `claude`)

#### Task 4.4a: Frontend test infrastructure setup

**Agent**: frontend-engineer
**Files**:
- Create `apps/learn-app/vitest.config.ts`
- Modify `apps/learn-app/package.json` (add vitest, @testing-library/react, jsdom)
- Create `apps/learn-app/src/__tests__/setup.ts` (jsdom environment, mocks for xterm.js and WebSocket)

Setup Vitest with:
- jsdom environment for DOM rendering
- @testing-library/react for component testing
- Mock for `@xterm/xterm` Terminal class (canvas-dependent, can't run in jsdom)
- Mock for WebSocket (node environment)
- Mock for `navigator.clipboard` (copy button tests)

**Acceptance criteria**:
- `pnpm nx test learn-app` runs and discovers tests
- Vitest config resolves Docusaurus/MDX imports without error
- Mocks for xterm.js and WebSocket work correctly

#### Task 4.4b: Frontend tests

**Agent**: frontend-engineer (after 4.4a)
**Files**: `apps/learn-app/src/__tests__/`

Test components:
- `usePracticeServer`: health polling start/stop lifecycle (Decision #29), session start, error handling (mock fetch)
- `TerminalPanel`: mount/unmount, connection states, resize debouncing (Decision #28), error frame handling
- `PracticeSetupCard`: render, copy button, auto-transition on server detection
- `PracticeErrorCard`: renders correct message/action for each error code
- `ExerciseCard` + `PracticeContext`: click Start → context update → overlay opens

**Acceptance criteria**:
- Hook lifecycle fully tested (polling start/stop/resume)
- Component lifecycle tested (mount, unmount, state transitions)
- Error card renders correctly for all error codes
- Context flow tested end-to-end

#### Task 4.5: GitHub Actions CI workflow

**Agent**: test-engineer
**Files**: `.github/workflows/practice-server-ci.yml`

Matrix:
```yaml
strategy:
  matrix:
    os: [macos-latest, ubuntu-latest, windows-latest]
    node: [18, 20]
```

Steps:
1. Checkout
2. Install pnpm
3. Install dependencies (triggers node-pty prebuild download)
4. Run unit tests
5. Run integration tests
6. Run E2E tests
7. TypeScript type check

**Acceptance criteria**:
- All tests pass on all 3 OSes
- node-pty installs without C++ toolchain on all platforms
- CI runs on PR and push to main

---

## Team Structure

| Role | Agent Type | Scope | Phases |
|------|-----------|-------|--------|
| **Lead** (this session) | Orchestrator | Architecture decisions, task assignment, quality review | All |
| **server-engineer** | general-purpose | Server refactoring (Tasks 1.1-1.3, 1.5-1.6), npm packaging (Tasks 2.1-2.2) | 1, 2 |
| **frontend-engineer** | general-purpose | Origin+heartbeat (Tasks 1.4, 1.7), setup/error cards (Task 2.3), ExerciseCard markers (Task 3.1), frontend tests (Tasks 4.4a, 4.4b) | 1, 2, 3, 4 |
| **test-engineer** | general-purpose | Server tests (Tasks 4.1-4.3), CI workflow (Task 4.5), exercise verification (Task 3.2) | 3, 4 |

### Execution Order

```
Phase 1 Track A (server-engineer):    1.1 → 1.2 → 1.3 → 1.5 → 1.6
Phase 1 Track B (frontend-engineer):  (wait for 1.1) → 1.4 + 1.7
         [Track B: terminal.ts + origin.ts only — zero overlap with Track A]

Phase 2 (parallel):                   server-engineer: 2.1, 2.2
                                      frontend-engineer: 2.3

Phase 3 (parallel):                   frontend-engineer: 3.1
                                      test-engineer: 3.2

Phase 4 (parallel):                   test-engineer: 4.1, 4.2, 4.3, 4.5
                                      frontend-engineer: 4.4a → 4.4b
```

### Dependencies

```
Task 1.1 (Node APIs)    ← blocks all other Phase 1 tasks (foundation refactor)
Task 1.2 (typed errors) ← blocks Task 2.3 (error card needs error codes)
Task 1.2 (typed errors) ← blocks Task 4.3 (E2E tests assert on error shapes)
Task 1.3 (Zod)          ← blocks Task 4.1 (unit tests test schemas)
Task 2.1 (package)      ← blocks Task 2.2 (prebuilds)
Task 4.4a (test setup)  ← blocks Task 4.4b (write tests)
Phase 1 complete        ← blocks Phase 4 (tests written for final code)
```

---

## File Inventory

### New Files (18)

| File | Purpose | Task |
|------|---------|------|
| `apps/practice-server/src/errors.ts` | Typed error definitions and helpers | 1.2 |
| `apps/practice-server/bin/cli.ts` | CLI entry point for npx | 2.1 |
| `apps/learn-app/src/components/PracticeSetupCard/index.tsx` | "Start server" UI card | 2.3 |
| `apps/learn-app/src/components/PracticeErrorCard/index.tsx` | Typed error display card | 2.3 |
| `apps/practice-server/src/__tests__/unit/origin.test.ts` | Origin validation tests | 4.1 |
| `apps/practice-server/src/__tests__/unit/errors.test.ts` | Error system tests | 4.1 |
| `apps/practice-server/src/__tests__/unit/registry.test.ts` | Registry lookup tests | 4.1 |
| `apps/practice-server/src/__tests__/unit/schemas.test.ts` | Zod schema tests | 4.1 |
| `apps/practice-server/src/__tests__/integration/workspace.test.ts` | Workspace I/O tests | 4.2 |
| `apps/practice-server/src/__tests__/integration/manager.test.ts` | PTY lifecycle tests | 4.2 |
| `apps/practice-server/src/__tests__/fixtures/test-exercise.zip` | Test fixture ZIP | 4.2 |
| `apps/practice-server/src/__tests__/e2e/server.test.ts` | Full server E2E tests | 4.3 |
| `apps/practice-server/src/__tests__/e2e/cli.test.ts` | CLI E2E tests | 4.3 |
| `apps/learn-app/vitest.config.ts` | Frontend test config | 4.4a |
| `apps/learn-app/src/__tests__/setup.ts` | Test setup (mocks) | 4.4a |
| `apps/learn-app/src/__tests__/usePracticeServer.test.ts` | Hook tests | 4.4b |
| `apps/learn-app/src/__tests__/TerminalPanel.test.tsx` | Component tests | 4.4b |
| `apps/learn-app/src/__tests__/PracticeFlow.test.tsx` | Context flow tests | 4.4b |

### Modified Files (10)

| File | Changes | Task |
|------|---------|------|
| `apps/practice-server/src/exercises/workspace.ts` | Replace shell commands with Node APIs, fetch, streaming, timeouts, download lock | 1.1 |
| `apps/practice-server/src/routes/sessions.ts` | Zod validation, typed errors | 1.2, 1.3 |
| `apps/practice-server/src/pty/manager.ts` | Cached claude path, cleanup ordering, WS error frames | 1.2, 1.5, 1.6 |
| `apps/practice-server/src/routes/health.ts` | Read from startup cache | 1.5 |
| `apps/practice-server/src/ws/terminal.ts` | Import origin.ts, heartbeat, error frame handling | 1.4, 1.7, 1.2 |
| `apps/practice-server/src/middleware/origin.ts` | Export ALLOWED_ORIGIN regex | 1.4 |
| `apps/practice-server/src/main.ts` | Startup cache, import ALLOWED_ORIGIN for CORS | 1.4, 1.5 |
| `apps/practice-server/package.json` | Add zod, extract-zip, bin field, @agentfactory scope | 1.1, 1.3, 2.1 |
| `apps/practice-server/tsconfig.json` | Adjust for bin/ entry point | 2.1 |
| `apps/learn-app/src/components/TerminalPanel/usePracticeServer.ts` | Health poll lifecycle (stop/resume) | 2.3 |

### GitHub Actions (2)

| File | Purpose | Task |
|------|---------|------|
| `.github/workflows/practice-server-ci.yml` | CI test matrix | 4.5 |
| `.github/workflows/practice-server-release.yml` | npm publish on release | 2.2 |

### Deleted Code (within files)

| Location | What | Why |
|----------|------|-----|
| `workspace.ts` | `httpsGet()`, `httpsGetJson()` functions | Replaced by native `fetch()` |
| `workspace.ts` | All `execSync()` / `execAsync()` calls | Replaced by Node fs APIs |
| `terminal.ts` | Inline origin regex | Replaced by import from `origin.ts` |
| `main.ts` | Inline CORS origin regex | Replaced by import from `origin.ts` |
| `health.ts` | `execFileSync()` call | Replaced by startup cache |
| `manager.ts` | `resolveClaudePath()` + `getClaudePath()` + `cachedClaudePath` | Moved to main.ts startup (Task 1.5) |

---

## Success Criteria

### Minimum Viable Release

- [ ] All 30 review decisions implemented
- [ ] Zero shell command dependencies (cross-platform ready)
- [ ] `npx @agentfactory/practice-server` works on macOS + Linux
- [ ] All 4 exercise packs download and work
- [ ] Typed errors surface in frontend with actionable messages (HTTP + WebSocket)
- [ ] CI green on macOS, Ubuntu, Windows

### Production Quality Bar

- [ ] Server test coverage >80%
- [ ] Frontend test coverage >70%
- [ ] WebSocket heartbeat prevents stale connections
- [ ] Setup card + error card guide non-tech users from zero to working
- [ ] No `execFileSync` in hot paths
- [ ] Download timeout prevents infinite hangs
- [ ] Resize debouncing prevents TUI flicker
- [ ] Health poll lifecycle managed (stop on connect, resume on disconnect)
- [ ] Download lock prevents TOCTOU race
- [ ] CLI detects and reports node-pty install failures

---

## Out of Scope (unchanged from spec)

- Go binary distribution / standalone installer
- Multiple concurrent exercises
- Exercise completion verification scripts
- tmux session persistence
- Gamification integration
- Monaco editor / file browser tab
- Code signing / notarization
- Windows native support (WSL is Tier 2)
- Automatic workspace version detection (v0.2 — Decision #23 note)
