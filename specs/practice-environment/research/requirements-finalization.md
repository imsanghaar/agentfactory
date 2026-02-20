# Practice Environment: Finalized Requirements Document

**Status**: Complete
**Date**: 2026-02-12
**Depends on**: `specs/practice-environment/spec.md`
**Integrates with**: Gamification Engine (`specs/003-gamification-engine/`)

---

## Table of Contents

1. [Functional Requirements](#1-functional-requirements)
2. [Non-Functional Requirements](#2-non-functional-requirements)
3. [Component Interfaces](#3-component-interfaces)
4. [User Journeys](#4-user-journeys)
5. [Technical Decisions](#5-technical-decisions)
6. [Risk Analysis](#6-risk-analysis)
7. [Scope Definition](#7-scope-definition)

---

## 1. Functional Requirements

### 1.1 "Practice" Button Click Flow

When a student clicks "Practice" on a lesson page:

1. **Button appears** as a third action alongside "Teach Me" and "Ask" in `DocPageActions` toolbar (same auth-gate pattern: visible to all, login-gated action).
2. **Practice server health check**: Browser sends `GET http://localhost:3100/health` (the practice server port -- see Section 5.2).
   - **If healthy**: proceed to step 3.
   - **If unreachable**: show inline setup instructions (see Section 1.5 Failure Modes).
3. **Exercise resolution**: Browser sends `POST http://localhost:3100/exercises/start` with `{ exerciseId, lessonPath }`. The practice server:
   a. Resolves the exercise config from the exercise registry.
   b. Creates workspace directory `~/af-practice/<exercise-id>/` if not exists.
   c. Writes exercise CLAUDE.md and starter files into workspace.
   d. Creates or reattaches to tmux session named `af-<exercise-id>`.
   e. Starts Claude Code in the tmux session with `--resume` if a prior session exists.
   f. Returns `{ sessionId, wsUrl }` to the browser.
4. **Terminal connection**: Browser opens WebSocket to `wsUrl`, xterm.js attaches.
5. **Terminal renders** in the ChatKit panel area (see Section 5.4 for widget vs. component decision).

### 1.2 Terminal Lifecycle

| State          | Trigger                                                                                                            | Behavior                                                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| **Create**     | First "Practice" click for an exercise                                                                             | New tmux session + workspace created                                                                                    |
| **Connect**    | WebSocket opened from browser                                                                                      | xterm.js streams I/O to/from tmux session                                                                               |
| **Disconnect** | Browser tab closed, navigated away, or WebSocket drops                                                             | tmux session continues running in background; WebSocket server marks connection as idle                                 |
| **Reconnect**  | Student returns to same exercise                                                                                   | Practice server finds existing tmux session, returns same `wsUrl`; xterm.js reconnects and shows current terminal state |
| **Destroy**    | Explicit "Reset Exercise" action OR exercise completed + confirmed OR idle timeout (configurable, default 4 hours) | tmux session killed, workspace optionally archived                                                                      |

**Key invariant**: The tmux session is the source of truth. The browser is a viewport. Closing the browser never kills the exercise.

### 1.3 Exercise Lifecycle

```
[Not Started] --> (click Practice) --> [Setting Up]
    |                                       |
    |                                       v
    |                              [Workspace Created]
    |                                       |
    |                                       v
    |                              [Claude Code Running]
    |                                       |
    |                              (student works...)
    |                                       |
    |                                       v
    |                              [Completion Detected]
    |                                       |
    |                                       v
    |                              [Verified Complete]
    |                                       |
    +--- (Reset Exercise) <--- [In Progress] --+
```

#### Setup Phase

1. Create `~/af-practice/<exercise-id>/` directory.
2. Copy exercise CLAUDE.md (from bundled exercises in learn-app -- see Section 5.5).
3. Copy any starter files (e.g., skeleton code, test files).
4. Create tmux session: `tmux new-session -d -s af-<exercise-id> -c ~/af-practice/<exercise-id>/`.
5. Launch Claude Code inside tmux: `tmux send-keys -t af-<exercise-id> 'claude' Enter`.

#### Hint Progression

Hints are embedded in the exercise CLAUDE.md under `## Progressive Hints`. Claude Code reads these and reveals them only when the student explicitly asks for help. This is Claude Code behavior, not platform logic -- the CLAUDE.md instructs Claude Code on hint behavior.

The platform does NOT manage hint state. Claude Code's conversation history (persisted via `--resume`) IS the hint state.

#### Completion Verification

See Section 5.6 for decision on mechanism. The recommended approach:

1. Exercise CLAUDE.md defines `## Success Criteria` as a checklist.
2. Practice server runs verification script (per-exercise, defined in exercise config): file existence checks, test execution, or output validation.
3. Verification triggered by: (a) student clicks "Check My Work" button in UI, or (b) Claude Code suggests checking.
4. Result returned to browser as `{ complete: boolean, criteria: [{name, passed}] }`.
5. On full completion: signal sent to gamification engine via `POST /api/gamification/events` (when gamification engine exists).

### 1.4 Session Persistence

| Scenario                     | Behavior                                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Browser refresh (F5)         | WebSocket reconnects to same tmux session. Terminal history visible.                                                            |
| Close tab, reopen later      | Same as refresh. tmux session still running.                                                                                    |
| Close browser entirely       | tmux session persists. On next visit, "Resume" button shows instead of "Practice".                                              |
| Machine reboot               | tmux sessions are lost. Workspace files persist. Student starts new Claude Code session with `--resume` to reload conversation. |
| Navigate to different lesson | Previous exercise's tmux session continues in background. Student can have multiple sessions.                                   |

### 1.5 Failure Modes

| Failure                              | Detection                                                                | User Experience                                                                                                                                                       |
| ------------------------------------ | ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Practice server not running**      | Health check returns connection refused                                  | Inline card: "Practice server not running. Run `npx @agent-factory/practice-server` in your terminal to start it." with copy-to-clipboard button                      |
| **Claude Code not installed**        | Practice server checks `which claude` on startup                         | Health endpoint returns `{ healthy: false, reason: "claude_not_found" }`. UI shows: "Claude Code is required. Install it: `npm install -g @anthropic-ai/claude-code`" |
| **No Anthropic API key**             | Claude Code exits with auth error within first 5 seconds of tmux session | Practice server detects quick exit, returns error. UI shows: "Set your Anthropic API key: `export ANTHROPIC_API_KEY=sk-...`"                                          |
| **Exercise files missing**           | Exercise ID not found in registry                                        | UI shows: "This exercise isn't available yet. Check back after updating."                                                                                             |
| **tmux not installed**               | Practice server checks `which tmux` on startup                           | Health endpoint returns `{ healthy: false, reason: "tmux_not_found" }`. UI shows install instructions per platform.                                                   |
| **WebSocket disconnect (temporary)** | WebSocket `onclose` event with code != 1000                              | Auto-reconnect with exponential backoff (1s, 2s, 4s, 8s, max 30s). Show "Reconnecting..." overlay on terminal.                                                        |
| **WebSocket disconnect (permanent)** | 5 consecutive reconnect failures                                         | Show "Connection lost. Your exercise is still running in the background. Click to reconnect." button.                                                                 |
| **Port conflict**                    | Practice server fails to bind to port                                    | Server tries next port in range (3100-3110). Returns actual port in health response. Learn-app checks range on health check.                                          |

### 1.6 Concurrent Exercises

**Decision: Allow multiple simultaneous exercises.**

Rationale: Students may want to reference a completed exercise while working on a new one. tmux supports unlimited sessions. The cost is minimal (one tmux session + one Claude Code process per exercise).

Constraints:

- Only ONE WebSocket connection per exercise at a time (prevent duplicate terminals).
- Practice server tracks active sessions: `GET /exercises/sessions` returns list.
- UI shows "active exercises" indicator if exercises are running in background.
- Resource warning if > 3 concurrent Claude Code processes (each uses ~200MB RAM + API calls).

---

## 2. Non-Functional Requirements

### 2.1 Latency

| Operation                                    | Target  | Acceptable | Unacceptable |
| -------------------------------------------- | ------- | ---------- | ------------ |
| Health check response                        | < 50ms  | < 200ms    | > 500ms      |
| Exercise start (new)                         | < 3s    | < 5s       | > 10s        |
| Exercise start (resume)                      | < 1s    | < 2s       | > 5s         |
| Terminal first paint after WebSocket connect | < 200ms | < 500ms    | > 1s         |
| Keystroke round-trip (type -> echo)          | < 50ms  | < 100ms    | > 200ms      |
| Completion check                             | < 2s    | < 5s       | > 10s        |

The 3-second target for "click Practice -> terminal visible" from the spec is achievable because:

- Health check: ~50ms (localhost)
- Exercise start API: ~500ms (workspace setup) to ~2s (first-time tmux + Claude Code launch)
- WebSocket connect + first render: ~200ms
- Total: ~750ms (resume) to ~2.75s (first time)

### 2.2 Reliability

- **WebSocket**: Auto-reconnect with exponential backoff. Terminal state is never lost (tmux is the source of truth).
- **Practice server crash**: tmux sessions survive practice server restarts. On restart, server rediscovers existing sessions via `tmux list-sessions`.
- **Data loss prevention**: Exercise workspaces persist on disk at `~/af-practice/`. Even a full system restart only loses tmux session state, not files or Claude Code conversation history (which Claude Code persists separately).

### 2.3 Security

| Concern                   | Mitigation                                                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Localhost only**        | Practice server binds to `127.0.0.1` only (not `0.0.0.0`). Refuses external connections.                                                                                                   |
| **CORS**                  | `Access-Control-Allow-Origin: http://localhost:3000` (learn-app dev server). Configurable for production builds.                                                                           |
| **Origin validation**     | WebSocket upgrade handler checks `Origin` header matches allowed origins list. Rejects non-localhost origins.                                                                              |
| **Command injection**     | Exercise IDs are alphanumeric-plus-hyphens only. Validated with regex `^[a-z0-9-]+$` before use in any shell command. Workspace paths are constructed, never interpolated from user input. |
| **File system access**    | Practice server has no elevated privileges. Runs as the user. Workspaces are in `~/af-practice/` only.                                                                                     |
| **No secrets in transit** | All communication is localhost. No TLS needed for the WebSocket (ws://, not wss://). The student's Anthropic API key is in their shell environment, never transmitted to the browser.      |
| **Session hijacking**     | Since everything is localhost, the threat model is minimal. A session token is still issued per WebSocket connection for clean disconnect/reconnect handling.                              |

### 2.4 Compatibility

| Platform                  | Support Level        | Notes                                                                                                                                        |
| ------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **macOS**                 | Primary (Tier 1)     | tmux available via Homebrew. Claude Code native. Node.js via nvm/brew.                                                                       |
| **Linux (Ubuntu/Debian)** | Tier 1               | tmux via apt. Everything works natively.                                                                                                     |
| **Windows (WSL2)**        | Tier 2               | tmux in WSL. Practice server runs in WSL. Learn-app can run in Windows or WSL. WebSocket crosses WSL/Windows boundary (localhost is shared). |
| **Windows (native)**      | Not supported (v0.1) | No tmux. Would require alternative session management (ConPTY). Out of scope.                                                                |
| **Codespaces / Gitpod**   | Future               | Would work with port forwarding. Not tested for v0.1.                                                                                        |

### 2.5 Dependencies (Student's Machine)

**Required:**

- Node.js >= 20 (already required for learn-app)
- npm (comes with Node.js)
- tmux >= 3.0 (macOS: `brew install tmux`, Linux: `apt install tmux`)
- Claude Code CLI (`npm install -g @anthropic-ai/claude-code`)
- Anthropic API key (set as `ANTHROPIC_API_KEY` environment variable)

**Already present** (from existing learn-app setup):

- Node.js, npm, pnpm
- Git
- A modern browser (Chrome, Firefox, Safari, Edge)

**Minimum viable setup command sequence:**

```bash
# One-time setup (if not already done)
brew install tmux                              # macOS
# OR: sudo apt install tmux                    # Linux

npm install -g @anthropic-ai/claude-code       # if not already installed
export ANTHROPIC_API_KEY=sk-ant-...            # in .bashrc/.zshrc

# Per-session (when they want to practice)
npx @agent-factory/practice-server             # starts practice server
```

---

## 3. Component Interfaces

### 3.1 Browser <-> Practice Server: REST API

#### Health Check

```
GET /health

Response 200:
{
  "healthy": boolean,
  "version": "0.1.0",
  "port": 3100,
  "dependencies": {
    "tmux": { "installed": true, "version": "3.4" },
    "claude": { "installed": true, "version": "1.0.17" }
  },
  "activeSessions": 2
}
```

#### Start Exercise

```
POST /exercises/start
Content-Type: application/json

{
  "exerciseId": "ch34-first-agent",
  "lessonPath": "05-Building-Custom-Agents/34-openai-agents-sdk/08-your-first-agent-concept"
}

Response 200 (new session):
{
  "sessionId": "af-ch34-first-agent",
  "wsUrl": "ws://localhost:3100/terminal/af-ch34-first-agent",
  "status": "created",
  "workspace": "~/af-practice/ch34-first-agent/"
}

Response 200 (existing session):
{
  "sessionId": "af-ch34-first-agent",
  "wsUrl": "ws://localhost:3100/terminal/af-ch34-first-agent",
  "status": "resumed",
  "workspace": "~/af-practice/ch34-first-agent/"
}

Response 404:
{
  "error": "exercise_not_found",
  "message": "Exercise 'ch34-first-agent' is not in the registry"
}

Response 503:
{
  "error": "dependency_missing",
  "missing": "claude",
  "message": "Claude Code CLI not found. Install: npm install -g @anthropic-ai/claude-code"
}
```

#### List Active Sessions

```
GET /exercises/sessions

Response 200:
{
  "sessions": [
    {
      "sessionId": "af-ch34-first-agent",
      "exerciseId": "ch34-first-agent",
      "status": "running",
      "createdAt": "2026-02-12T10:30:00Z",
      "lastActivity": "2026-02-12T11:45:00Z",
      "connected": true
    }
  ]
}
```

#### Check Completion

```
POST /exercises/verify
Content-Type: application/json

{
  "exerciseId": "ch34-first-agent"
}

Response 200:
{
  "complete": false,
  "criteria": [
    { "name": "Agent file exists", "passed": true },
    { "name": "Agent responds to greeting", "passed": false },
    { "name": "Tests pass", "passed": false }
  ]
}
```

#### Reset Exercise

```
POST /exercises/reset
Content-Type: application/json

{
  "exerciseId": "ch34-first-agent"
}

Response 200:
{
  "status": "reset",
  "message": "Workspace cleared and tmux session killed"
}
```

### 3.2 Browser <-> Practice Server: WebSocket Protocol

```
Connection: ws://localhost:3100/terminal/<session-id>

Messages (binary, bidirectional):
  Browser -> Server: raw terminal input bytes (keystrokes)
  Server -> Browser: raw terminal output bytes (from tmux)

Control messages (JSON, text frames):
  Browser -> Server:
    { "type": "resize", "cols": 120, "rows": 40 }
    { "type": "ping" }

  Server -> Browser:
    { "type": "pong" }
    { "type": "session_ended", "reason": "timeout" | "reset" | "completed" }
    { "type": "error", "message": "..." }
```

The WebSocket carries raw PTY data as binary frames and control messages as text (JSON) frames. This is the standard xterm.js attach addon pattern. The binary/text frame distinction is built into the WebSocket protocol -- no custom framing needed.

### 3.3 Practice Server <-> tmux: Process Management

The practice server does NOT use node-pty. Instead, it manages tmux sessions via shell commands and pipes I/O through tmux's native mechanism:

```
# Create session
tmux new-session -d -s <session-id> -c <workspace-path> -x 120 -y 40

# Attach for I/O (server-side, piped to WebSocket)
# Option A: Use tmux's control mode (-CC) -- structured output, parseable
# Option B: Use node-pty to spawn `tmux attach -t <session-id>` -- simpler I/O
# Recommendation: Option B (node-pty wrapping tmux attach)

# Resize
tmux resize-window -t <session-id> -x <cols> -y <rows>

# Send keys (for initial Claude Code launch)
tmux send-keys -t <session-id> 'claude' Enter

# Check if session exists
tmux has-session -t <session-id>

# Kill session
tmux kill-session -t <session-id>

# List sessions
tmux list-sessions -F '#{session_name} #{session_activity}'
```

**Implementation detail**: The practice server uses `node-pty` to spawn `tmux attach-session -t <session-id>`. This gives the server a PTY file descriptor that can be piped to/from the WebSocket. When the WebSocket disconnects, the node-pty process is killed (detaching from tmux), but the tmux session continues.

### 3.4 ChatKit Agent <-> Terminal Widget

**This is the hardest integration point.** See Section 5.4 for the decision.

**Recommended approach (for v0.1): Terminal is NOT a ChatKit widget.** Instead:

The terminal renders as a **separate React component alongside ChatKit**, toggled by a tab system in the Sheet panel. The panel gets two tabs: "Chat" and "Practice". This avoids the complexity of ChatKit's widget system entirely for v0.1.

```
┌─────────────────────────────────┐
│  Sheet Panel                    │
│  [Chat] [Practice]             │  <-- Tab bar (new component)
│  ┌─────────────────────────────┐│
│  │  (Tab: Chat)                ││
│  │  <ChatKit />                ││
│  │                             ││
│  │  -- OR --                   ││
│  │                             ││
│  │  (Tab: Practice)            ││
│  │  <TerminalPanel             ││
│  │    exerciseId={...}         ││
│  │    practiceServerUrl={...}  ││
│  │  />                         ││
│  └─────────────────────────────┘│
└─────────────────────────────────┘
```

**Why not a ChatKit widget?**

1. ChatKit widgets are JSON-defined UI components (cards, lists, forms). They do not support arbitrary React components like xterm.js.
2. The `stream_widget()` helper renders ChatKit's built-in widget node types. A terminal is not one of them.
3. GitHub issue openai/chatkit-js#73 confirms: custom widget rendering outside OpenAI products is not officially supported.
4. Trying to hack xterm.js into a ChatKit widget would be fragile, version-dependent, and unsupported.

**Future path to ChatKit integration (v0.2+):** If/when ChatKit adds custom React component slots or a plugin system, the terminal can be migrated into the chat thread. The Tab approach gives us a clean, working solution now that can be upgraded later.

### 3.5 Exercise Registry

Exercises are defined as JSON config files bundled with the learn-app content:

```
apps/learn-app/static/exercises/
  registry.json                           # Index of all exercises
  ch34-first-agent/
    config.json                           # Exercise metadata
    CLAUDE.md                             # Exercise-specific instructions
    starter/                              # Files copied to workspace
      agent.py
      requirements.txt
    verify.sh                             # Completion verification script
```

#### registry.json

```json
{
  "version": "1.0",
  "exercises": [
    {
      "id": "ch34-first-agent",
      "title": "Build Your First Agent",
      "lessonPath": "05-Building-Custom-Agents/34-openai-agents-sdk/08-your-first-agent-concept",
      "difficulty": "beginner",
      "estimatedMinutes": 30,
      "xpReward": 150
    }
  ]
}
```

#### config.json

```json
{
  "id": "ch34-first-agent",
  "title": "Build Your First Agent",
  "description": "Create a simple AI agent using the OpenAI Agents SDK",
  "prerequisites": ["python3", "pip"],
  "workspace": {
    "starterFiles": ["agent.py", "requirements.txt"],
    "setupCommands": ["pip install -r requirements.txt"]
  },
  "verification": {
    "type": "script",
    "script": "verify.sh",
    "timeout": 30
  },
  "hints": 3,
  "xpReward": 150
}
```

#### Exercise Resolution Flow

1. Learn-app serves `registry.json` as a static file.
2. Browser fetches registry on first "Practice" click (cached afterward).
3. Browser looks up exercise by `lessonPath` match.
4. If found, sends `exerciseId` to practice server.
5. Practice server fetches exercise files from learn-app's static server: `GET http://localhost:3000/exercises/<exercise-id>/CLAUDE.md` (or from a local cache/bundle).

**Alternative considered**: Practice server bundles exercises locally. Rejected because it creates a version sync problem -- exercise content should live with the lesson content.

---

## 4. User Journeys

### 4.1 First-Time Setup

**Persona**: Maya, domain expert learning to build AI agents. Has Node.js installed (required for learn-app). Does NOT have tmux or Claude Code.

1. Maya reads Lesson 34.8 ("Your First Agent Concept").
2. She sees the "Practice" button in the toolbar.
3. She clicks "Practice".
4. Browser runs health check -> connection refused.
5. UI shows a friendly setup card:

   ```
   ┌─────────────────────────────────────────────┐
   │  Set Up Your Practice Environment           │
   │                                              │
   │  To practice building agents, you need:      │
   │                                              │
   │  1. Install tmux (terminal multiplexer):     │
   │     $ brew install tmux          [Copy]      │
   │                                              │
   │  2. Install Claude Code:                     │
   │     $ npm i -g @anthropic-ai/claude-code     │
   │                                       [Copy] │
   │                                              │
   │  3. Set your API key:                        │
   │     $ export ANTHROPIC_API_KEY=sk-ant-...    │
   │                                       [Copy] │
   │                                              │
   │  4. Start the practice server:               │
   │     $ npx @agent-factory/practice-server     │
   │                                       [Copy] │
   │                                              │
   │  Then click Practice again!                  │
   │                                              │
   │  [Detailed Guide] [I need help]              │
   └─────────────────────────────────────────────┘
   ```

6. Maya follows the steps in her terminal.
7. She clicks "Practice" again.
8. Health check succeeds (but reports `claude: not installed`).
9. UI shows targeted message: "Claude Code not found. Run: `npm install -g @anthropic-ai/claude-code`"
10. Maya installs Claude Code, clicks again.
11. This time everything works. Terminal appears.

**Key UX principle**: Progressive disclosure of problems. Never dump ALL requirements at once -- show the NEXT thing they need.

### 4.2 First Exercise (Happy Path)

**Persona**: Maya, setup complete. First time doing an exercise.

1. Maya is on Lesson 34.8. Clicks "Practice".
2. Panel opens to "Practice" tab. Shows "Starting exercise..." spinner.
3. After ~2 seconds:
   - Workspace created at `~/af-practice/ch34-first-agent/`
   - tmux session started.
   - Claude Code launches.
4. Terminal shows Claude Code welcome, then Claude reads the exercise CLAUDE.md and greets:

   ```
   Welcome to "Build Your First Agent"!

   Your task: Create a simple AI agent that can greet users and
   answer questions about itself.

   I'll guide you step by step. Let's start:

   First, let's look at the starter code in agent.py.
   Can you open it and tell me what you see?
   ```

5. Maya interacts with Claude Code in the terminal. Types commands, asks for hints.
6. After building the agent, she clicks "Check My Work" button (above terminal).
7. Verification runs: `verify.sh` checks file exists, runs a test.
8. Results show: 2/3 criteria met. "Agent responds to greeting" failed.
9. Maya asks Claude Code for help. Fixes the issue.
10. Clicks "Check My Work" again. 3/3 passed!
11. UI shows completion celebration: "+150 XP" (when gamification exists).
12. Exercise marked complete. Terminal remains available for experimentation.

### 4.3 Returning to In-Progress Exercise

**Persona**: Maya started an exercise yesterday, closed her laptop.

1. Maya opens learn-app, navigates to the lesson.
2. "Practice" button shows "Resume" indicator (dot or badge).
3. She clicks it.
4. Panel opens. Practice server finds: workspace exists but tmux session is gone (machine rebooted).
5. Practice server creates new tmux session in existing workspace.
6. Claude Code launches with `--resume` flag, loading conversation history.
7. Terminal shows Claude Code picking up where she left off.
8. Maya continues working.

**If tmux session is still alive** (e.g., she just navigated away and came back):

- Step 5 is skipped. Server reattaches to existing session.
- Terminal shows exact current state (whatever Claude Code is displaying).

### 4.4 Exercise Completion and XP Award

1. Student clicks "Check My Work".
2. Practice server runs `verify.sh` in the exercise workspace.
3. All criteria pass.
4. Practice server returns `{ complete: true, criteria: [...] }`.
5. Browser shows completion UI with confetti/celebration.
6. **If gamification engine exists**: Browser sends event to study-mode-api:
   ```
   POST /api/gamification/events
   {
     "type": "exercise_completed",
     "exerciseId": "ch34-first-agent",
     "xp": 150,
     "userId": "<from-auth>"
   }
   ```
7. **If gamification engine does NOT exist yet** (v0.1): Completion is displayed locally only. No XP persisted. This is acceptable for v0.1 -- the value is in the practice itself.

### 4.5 Failure Recovery

#### WebSocket Disconnect (Network Blip)

1. WebSocket closes unexpectedly.
2. Terminal shows translucent "Reconnecting..." overlay.
3. Browser attempts reconnect: 1s, 2s, 4s, 8s delays.
4. On reconnect success: overlay disappears, terminal resumes. No data lost (tmux had all state).
5. On 5 consecutive failures: overlay changes to "Connection lost. [Reconnect] [Close]" buttons.

#### Practice Server Crashes

1. WebSocket disconnects because server process died.
2. Same reconnect flow as above.
3. If student restarts practice server (`npx @agent-factory/practice-server`):
   - Server rediscovers existing tmux sessions on startup.
   - Browser reconnects successfully.
4. tmux sessions and workspaces are fully intact.

#### Claude Code Crashes Inside tmux

1. Claude Code process exits inside the tmux session.
2. Student sees shell prompt in the terminal (tmux session is still alive, just Claude Code exited).
3. Student can type `claude --resume` to restart Claude Code with conversation history.
4. Practice server does NOT auto-restart Claude Code (student might have exited intentionally).

---

## 5. Technical Decisions

### 5.1 Practice Server Distribution

| Option                                             | Pros                                                                            | Cons                                                                                                                                                   | Recommendation  |
| -------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| **A: `npx @agent-factory/practice-server`**        | Zero install (runs from npm cache). Always gets latest version. Single command. | Slower first launch (~10s npm download). Requires npm.                                                                                                 | **RECOMMENDED** |
| B: `npm install -g @agent-factory/practice-server` | Faster after install. Available offline.                                        | Extra install step. Version can go stale. Clutters global npm.                                                                                         | Not recommended |
| C: Bundled with learn-app                          | No separate process.                                                            | learn-app is Docusaurus (static site generator). Embedding a Node.js WebSocket server in Docusaurus's dev server is fragile and architecturally wrong. | Rejected        |
| D: Homebrew / system package                       | Native feel.                                                                    | Massive distribution overhead. Cross-platform complexity. npm is already available.                                                                    | Rejected        |

**Decision: Option A (`npx`).** The student already has Node.js/npm. `npx` is the standard way to run Node.js CLI tools without permanent installation. The first launch downloads the package (~5MB estimated); subsequent launches use the npm cache.

**Package name**: `@agent-factory/practice-server` (npm scoped package under the `@agent-factory` org).

### 5.2 WebSocket Port

| Option                                           | Pros                                                                       | Cons                                                                                      | Recommendation                |
| ------------------------------------------------ | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------- |
| **A: Fixed port 3100, fallback range 3100-3110** | Predictable. Learn-app knows where to find it. Fallback handles conflicts. | Could conflict with other dev tools.                                                      | **RECOMMENDED**               |
| B: Fully dynamic (OS-assigned)                   | Never conflicts.                                                           | Learn-app doesn't know the port. Requires discovery mechanism (file on disk, mDNS, etc.). | Over-engineered for localhost |
| C: Fixed port, no fallback                       | Simplest.                                                                  | Fails if port is taken.                                                                   | Too brittle                   |

**Decision: Option A.** Port 3100 (primary) with fallback to 3101-3110. The practice server writes its actual port to `~/.af-practice-server.json` on startup:

```json
{ "port": 3100, "pid": 12345, "startedAt": "2026-02-12T10:00:00Z" }
```

The learn-app browser code:

1. First tries `localhost:3100/health`.
2. If that fails, reads from a well-known discovery endpoint is not possible from browser... so instead:
3. Tries ports 3100-3110 sequentially (fast localhost checks, ~10ms each).
4. Caches the working port in `sessionStorage`.

**Why 3100?** Port 3000 is learn-app (Docusaurus). Port 3001 is SSO server. Port 8000 is study-mode-api. Port 8001 is token-metering-api. Port 3100 gives headroom.

### 5.3 Exercise Storage

| Option                                        | Pros                                                                              | Cons                                                                                              | Recommendation  |
| --------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | --------------- |
| **A: Bundled with learn-app as static files** | Version-locked with lesson content. No extra fetch. Simple authoring (same repo). | Increases learn-app build size. Exercises shipped even if student never practices.                | **RECOMMENDED** |
| B: Separate npm package                       | Independent versioning. Smaller learn-app.                                        | Version sync hell. Extra dependency. More moving parts.                                           | Not recommended |
| C: CDN / remote fetch                         | Always fresh.                                                                     | Requires internet. Adds latency. Defeats "local-first" principle.                                 | Rejected        |
| D: Bundled with practice server package       | Self-contained practice server.                                                   | Exercises version-locked to server, not to content. When content updates, server must update too. | Rejected        |

**Decision: Option A.** Exercises live at `apps/learn-app/static/exercises/` in the monorepo. They are served by Docusaurus as static files at `/exercises/...`. The practice server fetches them from the learn-app dev server on first use and caches locally.

**Authoring workflow**: Content authors create exercise folders alongside lessons. The exercise's `lessonPath` in `registry.json` links it to the lesson. A CI check validates that every exercise references a real lesson path.

### 5.4 Terminal Widget Placement

| Option                                      | Pros                                                                          | Cons                                                                                                                                                                | Recommendation           |
| ------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| **A: Tab alongside ChatKit in Sheet panel** | Clean separation. No ChatKit hacking. Works today. Full terminal real estate. | Two separate UIs (Chat and Practice) that don't directly interact.                                                                                                  | **RECOMMENDED for v0.1** |
| B: ChatKit widget (stream_widget)           | Terminal embedded IN the chat thread. Feels integrated.                       | ChatKit widgets are JSON-defined, not arbitrary React components. No official support for custom React widgets (confirmed by chatkit-js#73). Would be fragile hack. | Not feasible for v0.1    |
| C: Separate modal/overlay                   | Doesn't take over the ChatKit panel. Can be larger.                           | Modal fatigue. Disconnected from lesson context. Z-index wars.                                                                                                      | Not recommended          |
| D: Split view (chat left, terminal right)   | Both visible simultaneously.                                                  | Requires significant layout redesign. Screen real estate on mobile.                                                                                                 | Future consideration     |

**Decision: Option A.** Add a tab bar to the existing `SheetContent` in `TeachMePanel`. Tabs: "Chat" (existing ChatKit) and "Practice" (new `TerminalPanel` component).

Implementation sketch for `TeachMePanel/index.tsx`:

```tsx
// New state
const [activeTab, setActiveTab] = useState<"chat" | "practice">("chat");

// In SheetContent:
<TabBar
  active={activeTab}
  onChange={setActiveTab}
  showPractice={hasExercise}
/>;
{
  activeTab === "chat" ? (
    <ChatKitWrapper {...chatProps} />
  ) : (
    <TerminalPanel exerciseId={exerciseId} serverUrl={practiceServerUrl} />
  );
}
```

**The "Practice" tab only appears when the current lesson has an associated exercise.** This is determined by checking the exercise registry.

### 5.5 Exercise CLAUDE.md Delivery

| Option                                                  | Pros                                                           | Cons                                                                               | Recommendation  |
| ------------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------- |
| **A: Downloaded at exercise start time from learn-app** | Always matches current lesson content. Single source of truth. | Requires learn-app to be running (it always is for local dev). Extra HTTP request. | **RECOMMENDED** |
| B: Pre-installed with practice server package           | Available offline. No fetch step.                              | Version sync with learn-app content. Stale exercises.                              | Rejected        |
| C: Checked into ~/af-practice/ by student               | Student controls content.                                      | Terrible UX. Students don't want to manage files.                                  | Rejected        |

**Decision: Option A.** The practice server fetches exercise files from `http://localhost:3000/exercises/<id>/CLAUDE.md` (and starter files) when creating a new workspace. Files are cached in the workspace -- subsequent resumes use the local copy.

**Cache invalidation**: The practice server checks the exercise's `config.json` for a `version` field. If the remote version is newer than the local copy, it re-downloads. This handles exercise content updates.

### 5.6 Completion Detection

| Option                                       | Pros                                                                                      | Cons                                                                     | Recommendation             |
| -------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------- |
| **A: Script-based verification (verify.sh)** | Flexible. Per-exercise logic. Can check files, run tests, validate output. Deterministic. | Requires authoring verification scripts. Platform-specific shell issues. | **RECOMMENDED**            |
| B: Claude Code self-report                   | Zero authoring overhead. Claude Code knows if student succeeded.                          | Non-deterministic. Claude could be wrong. Gaming-vulnerable.             | Not recommended as primary |
| C: File system checks only                   | Simple. Check if expected files exist with expected content.                              | Too shallow. File existing != file working.                              | Insufficient alone         |
| D: Student self-report ("I'm done")          | Simplest.                                                                                 | No verification. XP gaming. No pedagogical value.                        | Rejected                   |

**Decision: Option A (script-based) as primary, with Option C (file checks) as the default when no custom script exists.**

Each exercise has a `verify.sh` (or `verify.py` for Python exercises) that:

1. Runs in the exercise workspace directory.
2. Outputs JSON to stdout: `{ "criteria": [{"name": "...", "passed": true/false}] }`.
3. Exit code 0 if all pass, non-zero otherwise.
4. Has a configurable timeout (default 30 seconds).

Example `verify.sh`:

```bash
#!/bin/bash
# Verify ch34-first-agent exercise

results=()

# Check 1: Agent file exists
if [ -f "agent.py" ]; then
  results+=('{"name":"Agent file exists","passed":true}')
else
  results+=('{"name":"Agent file exists","passed":false}')
fi

# Check 2: Agent has required function
if grep -q "def run" agent.py 2>/dev/null; then
  results+=('{"name":"Agent has run function","passed":true}')
else
  results+=('{"name":"Agent has run function","passed":false}')
fi

# Check 3: Tests pass
if python -m pytest test_agent.py -q 2>/dev/null; then
  results+=('{"name":"Tests pass","passed":true}')
else
  results+=('{"name":"Tests pass","passed":false}')
fi

# Output JSON
echo "{\"criteria\":[$(IFS=,; echo "${results[*]}")]}"
```

---

## 6. Risk Analysis

### 6.1 Risk Matrix

| Risk                                                         | Likelihood                      | Impact   | Mitigation                                                                                                                                                                                         |
| ------------------------------------------------------------ | ------------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **xterm.js + WebSocket + tmux I/O has rendering artifacts**  | Medium                          | High     | Piece 1 proof-of-concept tests this exact stack before building anything else. Use node-pty wrapping `tmux attach` (battle-tested pattern).                                                        |
| **Claude Code's interactive UI breaks in xterm.js**          | Medium                          | Critical | Claude Code uses full terminal UI (status bars, progress indicators). Must test that xterm.js renders these correctly. If it doesn't, the entire approach is dead. **This is the kill-shot risk.** |
| **Student's Anthropic API key setup is too much friction**   | High                            | Medium   | Most Agent Factory students will already have Claude Code installed (the book teaches it in Part 3). For those who don't, the setup guide is clear. But this IS a friction point.                  |
| **WebSocket port conflicts in complex dev environments**     | Medium                          | Low      | Port range fallback (3100-3110) handles this. Documented in troubleshooting guide.                                                                                                                 |
| **Exercise authoring is too labor-intensive**                | Medium                          | Medium   | Start with 2-3 exercises for the most hands-on chapters. Create an exercise template and authoring guide. Each exercise is ~4 files (config.json, CLAUDE.md, starter files, verify.sh).            |
| **tmux unavailable on Windows (non-WSL)**                    | Low (most devs use macOS/Linux) | Medium   | Documented as "not supported in v0.1". WSL2 works. Native Windows support requires alternative PTY approach (future).                                                                              |
| **Practice server process management confusion**             | Medium                          | Medium   | Clear error messages. `npx` approach means no persistent daemon. Student runs it when needed, Ctrl+C to stop.                                                                                      |
| **Race condition: multiple browser tabs open same exercise** | Low                             | Low      | Practice server enforces one WebSocket per session. Second tab gets `{ error: "session_in_use" }` and shows "This exercise is open in another tab."                                                |

### 6.2 Hardest Parts (Technical)

**Ranked by difficulty:**

1. **xterm.js rendering fidelity for Claude Code's TUI** -- Claude Code has a rich terminal UI with status bars, progress spinners, syntax highlighting, and interactive prompts. xterm.js must render all of this correctly. Any rendering bug would make the practice experience feel broken. This cannot be solved incrementally; it either works or it doesn't.

2. **WebSocket <-> node-pty <-> tmux I/O plumbing** -- Getting bidirectional binary streaming right with proper encoding, resize handling, and no dropped bytes. This is well-trodden ground (many open-source implementations exist) but still requires careful implementation.

3. **Exercise CLAUDE.md authoring that produces good tutoring** -- The quality of the practice experience depends entirely on how well the CLAUDE.md is written. Too prescriptive = student just follows orders. Too vague = student is lost. This is a content design problem more than a technical one.

4. **Cross-platform tmux/PTY compatibility** -- macOS and Linux tmux behave slightly differently. Shell environments vary. PATH resolution can be tricky when launching from a Node.js process.

### 6.3 What Piece 1 (Standalone Terminal Proof) Might Reveal

Piece 1 tests: "Can I embed xterm.js in a React component, connect it via WebSocket to a local Node.js server, attach to a tmux session, and run Claude Code with full rendering fidelity?"

**Discoveries that would CHANGE the plan:**

| Discovery                                                                    | Plan Change                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Claude Code's TUI renders perfectly in xterm.js                              | Proceed as designed.                                                                                                                                                                                              |
| Claude Code has minor rendering issues (cosmetic)                            | File issues, work around. Proceed.                                                                                                                                                                                |
| Claude Code's TUI is fundamentally broken in xterm.js (unreadable, unusable) | **PIVOT**: Use Claude Code in `--print` / headless mode instead of interactive TUI. Build a simpler chat-like interface that sends prompts and shows responses. Loses the "real terminal" feel but is functional. |
| node-pty + tmux has encoding issues                                          | Switch from tmux to direct node-pty (lose session persistence, gain simpler I/O). Or use tmux's `-CC` control mode.                                                                                               |
| WebSocket latency makes typing feel laggy (>200ms round-trip on localhost)   | Investigate. Localhost should be <10ms. If laggy, likely a buffering issue in the node-pty or WebSocket implementation. Fixable.                                                                                  |
| xterm.js addon-attach has bugs with binary data                              | Use raw WebSocket handling instead of the attach addon. Write ~20 lines of custom code instead.                                                                                                                   |

**The ONE thing that kills the approach**: Claude Code's interactive TUI not rendering correctly in xterm.js. Everything else is solvable. This is why Piece 1 exists.

---

## 7. Scope Definition

### 7.1 v0.1 (Minimum Shippable)

**In scope:**

- Practice server: Node.js, WebSocket, tmux session management
- Terminal component: xterm.js React component with WebSocket attach
- Panel integration: Tab bar in Sheet panel ("Chat" / "Practice")
- Exercise lifecycle: start, resume, reset
- Exercise registry: JSON config files in learn-app static
- Exercise CLAUDE.md: fetched from learn-app, written to workspace
- Health check with dependency validation
- Failure modes: server not running, Claude Code not installed, API key missing
- Auto-reconnect on WebSocket disconnect
- Completion verification: script-based (`verify.sh`)
- Completion UI: criteria checklist, pass/fail display
- 2-3 starter exercises for chapters 33-34 (first agent concepts)
- macOS + Linux support
- Documentation: setup guide, troubleshooting

**NOT in scope for v0.1:**

- Gamification integration (XP awards) -- depends on gamification engine
- ChatKit widget integration (terminal IN the chat thread)
- Windows native support (WSL works)
- Exercise authoring CLI/tools (manual authoring is fine for 2-3 exercises)
- Exercise marketplace or community contributions
- Multi-user support (one student per machine)
- Cloud/remote practice environments
- Automated exercise generation from lesson content
- Progress tracking / analytics dashboard
- Teaching aid integration (ChatKit agent aware of exercise state)
- Codespaces / Gitpod support
- Mobile support (terminal on mobile is impractical)

### 7.2 v0.2 (Planned Follow-ups)

- Gamification integration: exercise completion -> XP events
- More exercises: 10-15 covering chapters 33-42
- Teaching aid awareness: ChatKit agent can see exercise status ("student is stuck on criterion 2")
- Exercise authoring guide + template
- Progress persistence: local storage of completed exercises
- WSL2 testing and documentation
- Split view option (chat + terminal simultaneously)

### 7.3 v0.3+ (Future Vision)

- ChatKit widget integration (when ChatKit supports custom React components)
- Exercise marketplace (community-contributed exercises)
- Automated exercise generation from lesson content using AI
- Cloud practice environments (Codespaces/Gitpod)
- Collaborative exercises (pair programming)
- Teaching dashboard (instructor sees student progress)

### 7.4 Kill Shot

**The one thing that, if it doesn't work, kills the entire approach:**

> **Claude Code's interactive TUI must render correctly in xterm.js via a WebSocket-connected tmux session.**

If the terminal rendering is broken -- garbled output, missing UI elements, broken cursor positioning, unusable status bars -- then embedding a terminal in the browser provides no value. Students would be better off just opening their own terminal.

This is why the implementation plan starts with Piece 1: a standalone proof-of-concept that tests exactly this. No further work should proceed until Piece 1 confirms rendering fidelity.

**Fallback if the kill shot fires**: Use Claude Code's headless mode (`-p` flag) and build a chat-like interface that sends exercise prompts and displays Claude Code's text responses. This loses the "real terminal" experience but preserves the guided exercise concept. The CLAUDE.md and exercise system would work identically; only the presentation layer changes.

---

## Appendix A: File/Component Map

```
New files to create:
  packages/practice-server/           # npm package (@agent-factory/practice-server)
    src/
      index.ts                        # Entry point, CLI argument parsing
      server.ts                       # HTTP + WebSocket server
      tmux-manager.ts                 # tmux session CRUD
      exercise-resolver.ts            # Fetch + cache exercise configs
      completion-verifier.ts          # Run verify.sh scripts
    package.json
    tsconfig.json

  apps/learn-app/
    static/exercises/                  # Exercise content (static files)
      registry.json
      ch34-first-agent/
        config.json
        CLAUDE.md
        starter/
        verify.sh
    src/components/
      TerminalPanel/                   # xterm.js React component
        index.tsx
        styles.module.css
        usePracticeServer.ts           # Hook for practice server communication
      PanelTabBar/                     # Tab bar for Chat/Practice
        index.tsx
        styles.module.css

Modified files:
  apps/learn-app/src/components/TeachMePanel/index.tsx  # Add tab system
  apps/learn-app/src/components/DocPageActions/index.tsx # Add Practice button
  apps/learn-app/src/contexts/StudyModeContext.tsx       # Add practice state
  apps/learn-app/package.json                            # Add xterm.js deps
```

## Appendix B: Dependency Versions

```json
{
  "practice-server": {
    "ws": "^8.18.0",
    "node-pty": "^1.0.0",
    "express": "^5.0.0"
  },
  "learn-app (new deps)": {
    "@xterm/xterm": "^5.5.0",
    "@xterm/addon-attach": "^0.11.0",
    "@xterm/addon-fit": "^0.10.0"
  }
}
```

## Appendix C: Research Sources

- [xterm.js GitHub repository](https://github.com/xtermjs/xterm.js) -- Terminal emulator for the web
- [xterm.js attach addon](https://github.com/xtermjs/xterm.js/tree/master/addons/addon-attach) -- WebSocket attachment
- [ChatKit widgets documentation](https://platform.openai.com/docs/guides/chatkit-widgets) -- OpenAI ChatKit widget system
- [ChatKit advanced integrations](https://platform.openai.com/docs/guides/custom-chatkit) -- Custom ChatKit backends
- [chatkit-js#73 - Custom widget rendering](https://github.com/openai/chatkit-js/issues/73) -- Confirms no custom React widget support
- [openai-chatkit-advanced-samples](https://github.com/openai/openai-chatkit-advanced-samples) -- Reference implementations
- [node-tmux](https://github.com/StarlaneStudios/node-tmux) -- Node.js tmux wrapper
- [Claude Code headless mode](https://code.claude.com/docs/en/headless) -- Non-interactive Claude Code
- [claude-tmux](https://github.com/nielsgroen/claude-tmux) -- Claude Code + tmux session management
- [xterm-react](https://github.com/PabloLION/xterm-react) -- React component for xterm.js
- [Building browser terminal with xterm.js](https://www.presidio.com/technical-blog/building-a-browser-based-terminal-using-docker-and-xtermjs/) -- Reference architecture
- [node-pty with Socket.io for multiple users](https://medium.com/@deysouvik700/efficient-and-scalable-usage-of-node-js-pty-with-socket-io-for-multiple-users-402851075c4a) -- Scalability patterns
- [ChatKit widgets practical guide](https://www.eesel.ai/blog/chatkit-widgets) -- Widget implementation guide
