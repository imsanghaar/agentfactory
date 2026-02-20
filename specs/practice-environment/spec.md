# Practice Environment: Embedded Terminal with Claude Code

**Issue**: #717
**Status**: v0.2 — Hono migration + UX hardening before npm publish
**Plan**: `specs/practice-environment/plan.md` (15-issue review, all decisions locked)
**Created**: 2026-02-12
**Updated**: 2026-02-16

## Problem Statement

Students learn ABOUT building AI agents but never BUILD AI agents within the platform. The learning loop breaks at the transition from understanding to doing. Chapter 3 has ~100 exercises across 4 exercise packs (GitHub repos with ZIP releases), but the current flow is: download ZIP → unzip → open terminal → run Claude Code. This breaks the learning loop.

## Solution

Embed a terminal (xterm.js) in the learn-app lesson page as a resizable fixed overlay, connected to a local practice server (`@agentfactory/practice`) that spawns Claude Code via node-pty in the correct exercise workspace directory. One click from lesson page to guided practice.

## Architecture

```
Browser (learn-app on Vercel)         Local Machine
┌──────────────────────────┐         ┌──────────────────────────┐
│ Lesson Page               │         │ @agentfactory/practice   │
│ ┌──────────┬────────────┐│         │ (Hono + node-pty)        │
│ │ Lesson   │ Practice   ││         │                          │
│ │ content  │ terminal   ││  HTTP   │ GET  /health             │
│ │ (left)   │ (right)    ││◄───────►│ POST /sessions/start     │
│ │          │            ││         │ POST /sessions/reset     │
│ │          │ ┌────────┐ ││  WS     │ /sessions/:id/ws         │
│ │          │ │xterm.js│ ││◄══════►│ node-pty → Claude Code   │
│ │          │ └────────┘ ││         │                          │
│ └──────────┴────────────┘│         │ ~/af-practice/<id>/      │
│ [Start] buttons per       │         │   ├── CLAUDE.md          │
│ exercise (ExerciseCard)   │         │   └── (exercise files)   │
└──────────────────────────┘         └──────────────────────────┘
```

### How It Works

The system has three pieces:

1. **Claude Code CLI** — The actual AI agent. Spawned as a child process via node-pty. It has no idea it's running in a browser — it thinks it's in a normal terminal.

2. **practice server** (`@agentfactory/practice`) — Node.js/Hono server on localhost:3100 with three jobs:
   - **Exercise workspace management**: Downloads ZIP from GitHub releases, extracts to `~/af-practice/<exerciseId>/`, resolves sub-exercise directories
   - **PTY spawning**: node-pty creates a real pseudo-terminal (same lib VS Code uses). Claude Code requires a PTY for colors, cursor movement, interactive prompts
   - **WebSocket relay**: Every byte Claude Code outputs goes through WebSocket to browser. Every keystroke goes back. Transparent bidirectional pipe

3. **Browser (xterm.js)** — Terminal emulator in a `<canvas>` element. Interprets ANSI escape codes, renders Claude Code's TUI pixel-by-pixel. Same parsing that iTerm2 or Terminal.app does, just in JavaScript.

### Data Flow

```
1. User clicks "Start" on Exercise 1.1 (ExerciseCard component)
2. ExerciseCard → PracticeContext → ContentWrapper opens overlay
3. PracticeOverlay → usePracticeServer hook scans ports 3100-3110 for healthy server
4. Hook calls POST /sessions/start { exerciseId: "ch3-basics", subExercise: "1.1" }
   (or POST /sessions/reset { exerciseId } to reset workspace and re-download)
5. Server downloads exercise ZIP from GitHub releases (first time only)
6. Server resolves: find ~/af-practice/ch3-basics -name "exercise-1.1-*"
   → ~/af-practice/ch3-basics/module-1/exercise-1.1-messy-downloads/
7. Server spawns Claude Code via node-pty in that directory
8. Claude Code auto-prompted: "Read INSTRUCTIONS.md and present overview..."
9. Server returns { sessionId, wsUrl }
10. Browser opens WebSocket → bidirectional PTY I/O via binary frames
11. xterm.js renders Claude Code TUI in browser
```

### WebSocket Protocol

```
Browser → Server:
  Binary frames: raw terminal input (keystrokes)
  Text frames:   JSON control messages { type: "resize", cols: 80, rows: 24 }

Server → Browser:
  Binary frames: raw PTY output (ANSI escape sequences, colors, cursor movement)
```

### Session Management

- **Single exercise at a time**: Starting new exercise kills previous Claude Code process
- **Session deduplication**: Server reuses existing session at same workspace path (handles React StrictMode double-mount)
- **PTY persistence**: PTY stays alive when WebSocket disconnects — reconnect pipes to same process
- **Clean environment**: All `CLAUDE*` env vars stripped to prevent "nested session" detection

### Security

- **Origin validation**: WebSocket upgrades only from `localhost:*` origins
- **CORS**: Only `localhost` and `127.0.0.1` allowed
- **No auth needed**: Local-only server, no sensitive data exposed

## Key Components

| Component         | Location                                                           | Purpose                                     |
| ----------------- | ------------------------------------------------------------------ | ------------------------------------------- |
| practice-server   | `apps/practice-server/`                                            | Hono + WebSocket + node-pty bridge          |
| TerminalPanel     | `apps/learn-app/src/components/TerminalPanel/`                     | xterm.js React wrapper                      |
| ExerciseCard      | `apps/learn-app/src/components/ExerciseCard/`                      | Per-exercise "Start" button (MDX component) |
| PracticeContext   | `apps/learn-app/src/contexts/PracticeContext.tsx`                  | ExerciseCard ↔ ContentWrapper React context |
| PracticeOverlay   | `apps/learn-app/src/theme/DocItem/Content/index.tsx`               | Fixed overlay with resize handle + terminal |
| usePracticeServer | `apps/learn-app/src/components/TerminalPanel/usePracticeServer.ts` | Server health polling + session management  |

## Exercise Registry

```typescript
const EXERCISE_REGISTRY = {
  "ch3-basics": { repo: "panaversity/claude-code-basic-exercises" },
  "ch3-skills": { repo: "panaversity/claude-code-skills-exercises" },
  "ch3-plugins": { repo: "panaversity/claude-code-plugins-exercises" },
  "ch3-agent-teams": { repo: "panaversity/claude-code-agent-teams-exercises" },
};
```

## Distribution Strategy

See `specs/practice-environment/research/distribution-strategy.md` for full analysis.

**Summary**: Two-phase approach:

1. **Phase 1 (Launch)**: `npx @agentfactory/practice` — npm handles platform-specific node-pty binaries
2. **Phase 2 (Scale)**: Rewrite in Go for true standalone binary (zero deps)

## Framework Decision: Hono over Express

**Decision**: Replace Express with Hono before npm publish. Once published, the HTTP framework is locked.

**Why Hono**:
- 19 npm deps vs Express's 81 (node-pty dominates at 62MB/74MB regardless)
- Native TypeScript — no `@types/express`, `@types/cors` dev deps needed
- Built-in CORS, validation middleware — fewer moving parts
- `c.req.json()` returns typed bodies, `c.json()` returns typed responses
- Same `@hono/node-server` produces a Node.js `http.Server` — WS upgrade pattern unchanged
- Performance: Hono benchmarks 2-3x faster than Express on route matching (irrelevant for 5 routes, but free)

**Why NOT Deno/NestJS/Fastify**:
- **Deno**: Cannot use node-pty (requires real PTY, not subprocess pipes)
- **NestJS**: 200+ deps, decorators, DI framework — absurdly over-engineered for 3 HTTP routes
- **Fastify**: Better than Express but worse than Hono — more deps, plugin system overkill for this server

**Migration scope**: Only the HTTP routing layer changes. WebSocket (`ws` library with `noServer: true`) and PTY management are framework-independent.

| File | Change |
|------|--------|
| `main.ts` | `express()` → `new Hono()` + `serve()` from `@hono/node-server` |
| `routes/health.ts` | `Router` → Hono route group |
| `routes/sessions.ts` | `req.body`/`res.json()` → `c.req.json()`/`c.json()` |
| `middleware/origin.ts` | `cors` npm → `cors()` from `hono/cors` |
| `package.json` | Drop `express`, `cors`, `@types/express`, `@types/cors`; add `hono`, `@hono/node-server` |
| `ws/terminal.ts` | **Unchanged** — raw WS on Node.js `http.Server` |

## UX Improvement Plan (v0.2)

### P0 — Must fix before ship

1. **Style the reset button** — `.practice-terminal-reset` CSS missing (button renders unstyled)
2. **Fix misleading terminal hint** — Says "Tell Claude Code which exercise to start" but Claude is auto-prompted. Replace with exercise name + sub-exercise ID
3. **Add loading spinner** — "Starting exercise..." and "Connecting..." are plain text with no animation
4. **Keyboard shortcut: Esc to close** — Users expect Esc to dismiss overlays

### P1 — Ship quality polish

5. **Exercise switching without close** — Dropdown or breadcrumb in terminal header to switch exercise without closing overlay
6. **Session reconnect on overlay re-open** — If PTY is alive but overlay was closed, reconnect instead of spawning new
7. **Animated setup card** — Terminal-like `npx @agentfactory/practice` with blinking cursor feel
8. **Connection status in overlay header** — Show green/yellow/red dot next to exercise name

### P2 — Post-launch UX

9. **Exercise progress indicators** — Show which exercises attempted/completed (localStorage)
10. **Touch-friendly resize** — Current drag handle only works with mouse; add touch events
11. **Mobile layout refinement** — Test the 50vh stack on real phones, adjust for usability

## Current Status (v0.2 — Hono migration + UX hardening)

### Complete (v0.1)

- Practice server with full session lifecycle (Node.js/Express → migrating to Hono)
- Exercise download from GitHub releases (with caching)
- Sub-exercise directory resolution (3 levels deep)
- xterm.js rendering Claude Code TUI in browser
- Resizable split overlay (20-80% range, drag handle)
- Session deduplication (React StrictMode safe)
- Initial prompt (Claude auto-reads INSTRUCTIONS.md)
- ExerciseCard markers for 24 exercises in basics lesson
- Docusaurus chrome hidden in practice mode (sidebar, TOC, footer)
- Content width fills left pane
- Typed error system with `{ code, message, action }` responses
- Zod input validation on all routes
- PTY spawn error handling (try/catch with typed errors)
- Port auto-detection (scans 3100-3110 in parallel, caches discovered port)
- Feature flag (`PRACTICE_ENABLED` env var on Vercel, default on)
- Exercise reset endpoint (`POST /sessions/reset` — kills sessions, deletes workspace)
- Reset button in terminal header (re-downloads fresh workspace)
- Improved error guidance (CLAUDE_NOT_FOUND install link, EXTRACTION_FAILED retryable)
- Cross-platform Windows fixes (`.cmd` file handling, `where.exe` path resolution)
- Clean env stripping (all `CLAUDE*` vars removed to prevent nested session detection)
- Full test suite: 143 tests (88 server + 55 frontend)
- GitHub Actions CI matrix (macOS, Ubuntu, Windows × Node 18, 22)

### In Progress (v0.2)

- [ ] Replace Express with Hono (framework migration)
- [ ] P0 UX fixes (reset button CSS, hint text, loading spinner, Esc key)

### Remaining for Ship

- [ ] P1 UX polish (exercise switching, reconnect, setup card animation, status dot)
- Configure `NPM_TOKEN` secret in GitHub repo settings
- Create GitHub release tag `practice-server-v0.1.0` to trigger npm publish
- Set `PRACTICE_ENABLED=false` on Vercel (default off until beta)
- Manual E2E testing on Windows 10/11

## API Endpoints

| Method | Path                   | Purpose                                         |
| ------ | ---------------------- | ----------------------------------------------- |
| `GET`  | `/health`              | Server health + claude path status              |
| `POST` | `/sessions/start`      | Start exercise session (download + spawn PTY)   |
| `POST` | `/sessions/reset`      | Kill sessions, delete workspace for re-download |
| `GET`  | `/sessions/:id/status` | Session status query                            |
| `WS`   | `/sessions/:id/ws`     | Bidirectional PTY I/O                           |

## Out of Scope (v0.2+)

- Go binary distribution / standalone installer
- Multiple concurrent exercises
- Exercise completion verification scripts
- tmux session persistence
- Gamification integration
- Monaco editor / file browser tab
- VS Code integration (`code .` to open workspace)
- Code signing / notarization
- Windows native support (WSL is Tier 2)
