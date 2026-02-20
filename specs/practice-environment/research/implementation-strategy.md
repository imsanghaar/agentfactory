# Implementation Strategy: 1-Click Practice Environment

**Date**: 2026-02-12
**Author**: strategist agent
**Depends on**: All research in `specs/practice-environment/research/`
**Supersedes**: Distribution decisions in `requirements-finalization.md` Section 5.1

---

## Executive Summary

Build a single Go binary (`af-practice`) that embeds xterm.js and bridges WebSocket to a local PTY running Claude Code. Distribute via platform-native one-liner installers (`curl | bash` on macOS/Linux, `irm | iex` on Windows). No npm, no brew, no Node.js required.

The critical insight from cross-platform research: **Claude Code no longer requires Node.js** (ships as a Bun-compiled binary via native installer). We cannot assume students have Node.js. The `npx`-based distribution proposed in earlier requirements is therefore invalid as the primary path.

---

## Table of Contents

1. [Architecture Decision: Go Binary](#1-architecture-decision-go-binary)
2. [Distribution Strategy](#2-distribution-strategy)
3. [The Complete Student Journey](#3-the-complete-student-journey)
4. [Component Architecture](#4-component-architecture)
5. [Phase Plan](#5-phase-plan)
6. [Critical Risk: Claude Code TUI Rendering](#6-critical-risk-claude-code-tui-rendering)
7. [What Changed from Earlier Requirements](#7-what-changed-from-earlier-requirements)
8. [Open Decisions for Review](#8-open-decisions-for-review)

---

## 1. Architecture Decision: Go Binary

### Why Go (Not Node.js, Rust, or ttyd)

| Criterion               | Go                      | Node.js (npx)                 | Rust                       | ttyd (ship as-is)            |
| ----------------------- | ----------------------- | ----------------------------- | -------------------------- | ---------------------------- |
| **Single binary**       | Yes (~10-15 MB)         | No (requires Node.js runtime) | Yes (~8-12 MB)             | Yes (~5 MB)                  |
| **Cross-compile**       | Trivial (`GOOS/GOARCH`) | N/A                           | Complex (`cargo cross`)    | Pre-built binaries partial   |
| **Windows PTY**         | ConPTY via Go libs      | node-pty (requires C++ build) | portable-pty               | 32-bit only, no macOS binary |
| **Embed static assets** | `go:embed` built-in     | Bun compile or pkg            | `include_bytes!`           | Already embedded             |
| **Node.js required?**   | **No**                  | **Yes**                       | **No**                     | **No**                       |
| **Maintenance burden**  | Medium (we own it)      | Low (npm ecosystem)           | High (Rust learning curve) | Low (external project)       |

**Decision: Go binary.** Rationale:

1. **Zero dependencies on student machine.** The binary is self-contained. No Node.js, no npm, no brew, no Python. Just download and run.
2. **Trivial cross-compilation.** `GOOS=windows GOARCH=amd64 go build` produces a Windows binary from macOS. We get all 6 platform targets from one CI job.
3. **Proven architecture.** GoTTY, tty2web, and ttyd all use this exact pattern (WebSocket server + PTY + embedded xterm.js). Go is the natural language for this kind of tool.
4. **Right-sized.** ~10-15 MB binary includes everything: HTTP server, WebSocket handler, PTY management, embedded xterm.js frontend. No bloat.

### Why NOT ttyd directly

ttyd is excellent but has critical gaps for our use case:

- **No macOS binary in releases** -- students would need `brew install ttyd`, violating the "no brew" constraint
- **Only 32-bit Windows binary** -- problematic on modern 64-bit Windows
- **No exercise management** -- ttyd just bridges a command to a browser. We need workspace creation, exercise resolution, health checks, completion verification
- **No REST API** -- we need `/health`, `/exercises/start`, `/exercises/verify` endpoints alongside the WebSocket terminal

Our Go binary is "ttyd + exercise management" in one tool.

---

## 2. Distribution Strategy

### The Claude Code / Tailscale Pattern

Follow the same installation pattern that Claude Code itself uses:

```bash
# macOS / Linux
curl -fsSL https://agentfactory.dev/install.sh | bash

# Windows (PowerShell)
irm https://agentfactory.dev/install.ps1 | iex
```

### What the Install Script Does

**`install.sh` (macOS/Linux):**

```bash
#!/bin/bash
set -euo pipefail

# 1. Detect OS and architecture
OS=$(uname -s | tr '[:upper:]' '[:lower:]')    # darwin, linux
ARCH=$(uname -m)                                 # x86_64, arm64, aarch64
case "$ARCH" in
  x86_64)  ARCH="amd64" ;;
  aarch64) ARCH="arm64" ;;
esac

# 2. Download binary from GitHub releases
RELEASE_URL="https://github.com/panaversity/agentfactory/releases/latest/download/af-practice-${OS}-${ARCH}"
INSTALL_DIR="$HOME/.local/bin"
mkdir -p "$INSTALL_DIR"
curl -fsSL "$RELEASE_URL" -o "$INSTALL_DIR/af-practice"
chmod +x "$INSTALL_DIR/af-practice"

# 3. Ensure PATH includes install dir
if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
  SHELL_RC="$HOME/.$(basename "$SHELL")rc"
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_RC"
  echo "Added $INSTALL_DIR to PATH in $SHELL_RC. Restart your terminal or run: source $SHELL_RC"
fi

# 4. Done
echo ""
echo "af-practice installed successfully!"
echo "Run 'af-practice' to start the practice server."
echo ""
```

**`install.ps1` (Windows):**

```powershell
$ErrorActionPreference = 'Stop'

# 1. Detect architecture
$arch = if ([Environment]::Is64BitOperatingSystem) { "amd64" } else { "386" }
$url = "https://github.com/panaversity/agentfactory/releases/latest/download/af-practice-windows-$arch.exe"

# 2. Download to known location
$installDir = "$env:LOCALAPPDATA\AgentFactory"
New-Item -ItemType Directory -Force -Path $installDir | Out-Null
$binPath = "$installDir\af-practice.exe"
Invoke-WebRequest -Uri $url -OutFile $binPath

# 3. Add to PATH (user-level, persistent)
$currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($currentPath -notlike "*$installDir*") {
    [Environment]::SetEnvironmentVariable("PATH", "$currentPath;$installDir", "User")
}

Write-Host ""
Write-Host "af-practice installed successfully!" -ForegroundColor Green
Write-Host "Restart your terminal, then run 'af-practice' to start."
Write-Host ""
```

### Release Targets

Built via GitHub Actions CI on every tagged release:

| Target         | Binary Name                     | Notes            |
| -------------- | ------------------------------- | ---------------- |
| macOS x86_64   | `af-practice-darwin-amd64`      | Intel Macs       |
| macOS arm64    | `af-practice-darwin-arm64`      | Apple Silicon    |
| Linux x86_64   | `af-practice-linux-amd64`       | Most Linux       |
| Linux arm64    | `af-practice-linux-arm64`       | RPi, ARM servers |
| Windows x86_64 | `af-practice-windows-amd64.exe` | 64-bit Windows   |
| Windows x86    | `af-practice-windows-386.exe`   | 32-bit fallback  |

### Self-Update Mechanism

The binary checks for updates on startup (non-blocking):

```
$ af-practice
Practice server v0.2.1 starting...
  Update available: v0.3.0. Run 'af-practice update' to upgrade.
Listening on http://localhost:3100
```

`af-practice update` downloads the new binary and replaces itself (same pattern as `rustup update`).

---

## 3. The Complete Student Journey

### 3.1 First-Time Setup (All Platforms)

**Prerequisite**: Student has Claude Code installed (taught in Part 3 of the book).

#### macOS

```bash
# Step 1: Install practice server (one-time, ~5 seconds)
curl -fsSL https://agentfactory.dev/install.sh | bash

# Step 2: Start it (each practice session)
af-practice
# Output: "Practice server running on http://localhost:3100"
# Output: "Open your lesson and click Practice!"
```

#### Linux (Ubuntu/Debian)

```bash
# Same as macOS
curl -fsSL https://agentfactory.dev/install.sh | bash
af-practice
```

#### Windows

```powershell
# Step 1: Install (one-time, PowerShell)
irm https://agentfactory.dev/install.ps1 | iex

# Step 2: Start (each practice session -- PowerShell, CMD, or Git Bash)
af-practice
```

### 3.2 Practice Flow (After Setup)

```
Student opens lesson page in browser
         |
         v
Clicks "Practice" button
         |
         v
Browser checks localhost:3100/health
         |
    +-----------+
    |  Running?  |
    +-----+-----+
     No   |   Yes
     |    |    |
     v    |    v
  Show    |  POST /exercises/start
  setup   |    |
  card    |    v
          |  Server creates workspace,
          |  starts Claude Code in PTY
          |    |
          |    v
          |  Returns WebSocket URL
          |    |
          |    v
          |  xterm.js connects via WebSocket
          |    |
          |    v
          +-> Terminal appears in browser panel
              Claude Code greets student with
              exercise instructions
```

### 3.3 The "Setup Card" UX (When Server Not Running)

```
+----------------------------------------------+
|  Start the Practice Server                    |
|                                               |
|  To practice exercises, run this in your      |
|  terminal:                                    |
|                                               |
|  $ af-practice                    [Copy]      |
|                                               |
|  Don't have it yet?                           |
|  $ curl -fsSL https://agent       [Copy]      |
|    factory.dev/install.sh | bash              |
|                                               |
|  [Retry]  [Setup Guide]                       |
+----------------------------------------------+
```

**Key UX decisions:**

1. Only show ONE command initially (`af-practice`). Most returning students just need to start it.
2. "Don't have it yet?" is a progressive disclosure -- only show install command if they don't have it.
3. The setup card auto-retries every 5 seconds (polling `/health`) so it disappears the moment the server starts.

---

## 4. Component Architecture

### 4.1 The Go Binary (`af-practice`)

```
af-practice binary (~10-15 MB)
├── Embedded assets (go:embed)
│   ├── xterm.js + addons (FitAddon, WebGL)
│   ├── terminal.html (minimal HTML page)
│   └── terminal.css
│
├── HTTP Server (net/http)
│   ├── GET  /health              → Dependency check, version info
│   ├── GET  /terminal/:id        → Serve embedded xterm.js HTML
│   ├── POST /exercises/start     → Create workspace, start exercise
│   ├── POST /exercises/verify    → Run verification script
│   ├── POST /exercises/reset     → Kill session, clean workspace
│   └── GET  /exercises/sessions  → List active sessions
│
├── WebSocket Handler (gorilla/websocket or nhooyr/websocket)
│   └── /ws/:session-id           → Bidirectional PTY stream
│       ├── Binary frames: raw terminal I/O
│       └── Text frames: JSON control messages (resize, ping)
│
├── PTY Manager
│   ├── Unix: github.com/creack/pty (forkpty)
│   └── Windows: ConPTY via syscall or go-winpty
│
├── Session Manager
│   ├── Map[sessionID] → PTY process
│   ├── Create: spawn shell in workspace dir, run Claude Code
│   ├── Attach: return existing PTY (reconnect)
│   └── Destroy: kill PTY, optionally clean workspace
│
└── Exercise Resolver
    ├── Fetch from learn-app: GET http://localhost:3000/exercises/<id>/
    ├── Cache locally in workspace
    └── Registry lookup for exercise metadata
```

### 4.2 tmux Decision: Defer to Phase 2

**The requirements-finalization.md heavily relies on tmux for session persistence.** However, tmux introduces significant complexity:

- **Not available on Windows** without WSL
- **Extra install step** on macOS (`brew install tmux`)
- **Adds indirection** in the PTY pipeline (WebSocket -> PTY -> tmux -> shell -> Claude Code)

**Phase 1 strategy: Use direct PTY, no tmux.**

The Go binary spawns Claude Code directly via PTY. Session state:

| Scenario                  | Without tmux (Phase 1)                                     | With tmux (Phase 2)           |
| ------------------------- | ---------------------------------------------------------- | ----------------------------- |
| Browser tab closed        | PTY stays alive. Reconnect shows current state.            | Same                          |
| Browser refreshed         | WebSocket reconnects to same PTY.                          | Same                          |
| Practice server restarted | **PTY lost.** Claude Code `--resume` reloads conversation. | tmux session survives         |
| Machine reboot            | PTY lost. `--resume` reloads.                              | tmux also lost. Same outcome. |

**Key insight**: For the most common scenarios (tab close, refresh, navigate away), direct PTY handles reconnection just fine. The practice server keeps the PTY alive as long as it's running. The ONLY case where tmux helps is "practice server crashes/restarts" -- and even then, Claude Code's `--resume` flag recovers the conversation.

tmux is a nice-to-have for Phase 2. It should NOT block Phase 1 or add to the install requirements.

### 4.3 Browser Component (Docusaurus Integration)

This part is NOT in the Go binary. It lives in the learn-app codebase.

```
apps/learn-app/src/components/
├── TerminalPanel/
│   ├── index.tsx          # xterm.js React component
│   ├── styles.module.css  # Terminal styling
│   └── usePracticeServer.ts  # Hook: health check, exercise start, WebSocket
├── PanelTabBar/
│   ├── index.tsx          # [Chat] [Practice] tabs
│   └── styles.module.css
└── PracticeSetupCard/
    └── index.tsx          # "Start the practice server" card
```

**Modified files:**

- `TeachMePanel/index.tsx` -- Add tab bar, conditionally show TerminalPanel
- `DocPageActions/index.tsx` -- Add "Practice" button (visible when exercise exists for lesson)
- `package.json` -- Add `@xterm/xterm`, `@xterm/addon-attach`, `@xterm/addon-fit`

### 4.4 Exercise Content (Static Files in learn-app)

```
apps/learn-app/static/exercises/
├── registry.json
└── ch3-basics-module1/
    ├── config.json
    ├── CLAUDE.md
    ├── starter/
    │   └── (starter files if any)
    └── verify.sh
```

Exercises are served as static files by Docusaurus. The Go binary fetches them from `http://localhost:3000/exercises/<id>/` on exercise start.

**Chapter 3 already has ~100 exercises with INSTRUCTIONS.md files.** The strategy for these existing exercises:

1. Each existing INSTRUCTIONS.md maps to an exercise config
2. A conversion script transforms INSTRUCTIONS.md -> CLAUDE.md format (adding Rules, Success Criteria, Progressive Hints sections)
3. The registry.json references all of them
4. verify.sh scripts are authored per-exercise (or a generic "files exist" check as default)

---

## 5. Phase Plan

### Phase 0: Proof of Concept (Days 1-2)

**Goal**: Validate the kill-shot risk -- does Claude Code TUI render correctly when accessed via WebSocket + xterm.js?

**Method**:

1. Install ttyd (`brew install ttyd`)
2. Run: `ttyd -W bash` (writable terminal)
3. Open `http://localhost:7681` in browser
4. In the browser terminal, run: `claude`
5. Verify: Does Claude Code's TUI render correctly? Status bars, colors, input, cursor?

**If rendering works**: Proceed to Phase 1.
**If rendering is broken**: Investigate. Test direct PTY (skip tmux). If still broken, pivot to Claude Code headless mode (`-p` flag) with a chat-like UI.

**Deliverable**: Go/no-go decision with evidence (screenshots).

### Phase 1: Working Go Binary (Days 3-7)

**Goal**: `af-practice` binary that serves a terminal in the browser connected to Claude Code via PTY.

**Scope**:

- Go binary with embedded xterm.js
- WebSocket-to-PTY bridge (creack/pty on Unix, ConPTY on Windows)
- Single endpoint: `GET /` serves terminal HTML, `GET /ws` connects WebSocket to PTY
- PTY spawns `claude` in a specified working directory
- Health check: `GET /health` reports version, checks for `claude` in PATH
- Resize support: browser sends resize JSON, server resizes PTY
- Build for macOS (arm64 + amd64) and Linux (amd64) initially

**NOT in scope for Phase 1**:

- Exercise management (just spawns Claude Code in current dir)
- Completion verification
- Registry, config files
- Windows build (add in Phase 2)
- Install scripts (manual download from GitHub releases)

**Deliverable**: Binary that works. Download, run `af-practice`, open browser, see Claude Code.

### Phase 2: Exercise Management + Browser Integration (Days 8-14)

**Goal**: Full exercise lifecycle and learn-app integration.

**Scope**:

- REST API: `/exercises/start`, `/exercises/verify`, `/exercises/reset`, `/exercises/sessions`
- Exercise resolver: fetch from learn-app static files
- Workspace management: create `~/af-practice/<exercise-id>/`, copy starter files
- Session tracking: multiple concurrent exercises
- Learn-app components: TerminalPanel, PanelTabBar, PracticeSetupCard
- Docusaurus integration: Practice button on lessons with exercises
- WebSocket reconnection with exponential backoff
- Connection status UI (connecting, connected, reconnecting, failed)
- Convert 5-10 Chapter 3 exercises from INSTRUCTIONS.md to CLAUDE.md format

**Deliverable**: Click "Practice" in lesson page -> terminal appears with exercise-specific Claude Code session.

### Phase 3: Cross-Platform + Distribution (Days 15-21)

**Goal**: Works on all platforms with one-command install.

**Scope**:

- Windows build (ConPTY integration)
- GitHub Actions CI: build all 6 targets on every tag
- Install scripts: `install.sh` (macOS/Linux), `install.ps1` (Windows)
- Host install scripts at agentfactory.dev (or GitHub Pages)
- Self-update mechanism (`af-practice update`)
- Completion verification: run verify.sh scripts
- Port fallback (3100-3110)
- Error messages for all failure modes

**Deliverable**: Student on any platform can install and use practice environment.

### Phase 4: Polish + tmux (Days 22-28)

**Goal**: Session persistence and production polish.

**Scope**:

- Optional tmux integration (if tmux detected, use it; otherwise direct PTY)
- Session recovery on server restart (rediscover tmux sessions)
- Exercise completion -> gamification event bridge (when gamification engine exists)
- Convert remaining Chapter 3 exercises (~100 total)
- Documentation: setup guide, troubleshooting, exercise authoring guide
- Testing: integration tests, cross-platform verification

**Deliverable**: Production-quality practice environment.

---

## 6. Critical Risk: Claude Code TUI Rendering

### The Kill Shot

From requirements-finalization.md Section 6.3:

> **"Claude Code's interactive TUI must render correctly in xterm.js via a WebSocket-connected PTY session."**

If this doesn't work, nothing else matters.

### Evidence It WILL Work

1. **claude-code-gui** (Tauri + xterm.js + portable-pty): An existing open-source project that renders Claude Code TUI in xterm.js. It works. This is the strongest evidence.

2. **Claude Code's renderer produces standard ANSI**: Claude Code uses a React-to-terminal renderer that outputs standard VT100/ANSI escape sequences. xterm.js handles these correctly (it's used by VS Code).

3. **Known minor issues only**: The research found only cosmetic issues (Unicode box-drawing fallback to ASCII, scroll event rates in tmux). Nothing that would make the TUI unusable.

### Why Phase 0 Exists

Despite the evidence above, we have not found anyone specifically running Claude Code inside a WebSocket-bridged terminal (the exact pipeline: xterm.js -> WebSocket -> Go binary -> PTY -> Claude Code). Phase 0 validates this specific pipeline.

### Fallback Plan

If the TUI is broken:

1. **Try without tmux** -- Direct PTY eliminates one variable
2. **Try `TERM=xterm-256color`** -- Ensure proper terminal type
3. **Try Claude Code `--no-animation`** or `--plain` flags if they exist
4. **Pivot to headless mode**: Use Claude Code's `-p` (print) flag. Build a chat-like UI that sends exercise prompts via stdin and displays responses. Loses the "real terminal" feel but preserves the guided exercise concept.

---

## 7. What Changed from Earlier Requirements

The cross-platform research (Task #1) surfaced critical findings that change several decisions from `requirements-finalization.md`:

| Decision               | Previous (requirements-finalization.md)           | Updated (this strategy)                | Reason                                                                              |
| ---------------------- | ------------------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------- |
| **Distribution**       | `npx @agent-factory/practice-server`              | Go binary + `curl \| bash` installer   | Claude Code no longer requires Node.js. Students may not have npm.                  |
| **Language**           | Node.js (TypeScript)                              | Go                                     | Need single binary, zero-dependency. Go cross-compiles trivially.                   |
| **PTY library**        | node-pty (native addon, requires C++ compilation) | creack/pty (Go, pure syscall) + ConPTY | No compilation needed on student machine.                                           |
| **tmux**               | Required (Phase 1)                                | Optional (Phase 2, nice-to-have)       | Adds install friction, not available on Windows, direct PTY handles most scenarios. |
| **Windows**            | "Tier 2 (WSL2 only)"                              | Tier 1 (native via ConPTY)             | Claude Code runs natively on Windows. Practice env should too.                      |
| **Port**               | 3100 (unchanged)                                  | 3100 (unchanged)                       | No change needed.                                                                   |
| **Exercise storage**   | Static files in learn-app (unchanged)             | Same (unchanged)                       | Still the right call.                                                               |
| **Terminal placement** | Tab in Sheet panel (unchanged)                    | Same (unchanged)                       | Still the right call.                                                               |

### What DIDN'T Change

- Exercise CLAUDE.md format: same
- Exercise registry structure: same
- REST API design: same (endpoints, request/response format)
- WebSocket protocol: same (binary frames for I/O, text frames for control)
- Security model: same (localhost only, origin validation)
- Completion verification: same (script-based)
- ChatKit integration strategy: same (tab, not widget)

---

## 8. Open Decisions for Review

### 8.1 Naming

**Binary name options:**

- `af-practice` (short, matches `af-` namespace) -- **RECOMMENDED**
- `agentfactory-practice` (explicit but long)
- `practice-env` (generic)

**Install domain options:**

- `agentfactory.dev/install.sh` (branded) -- **RECOMMENDED**
- GitHub raw URL (no custom domain needed, but ugly)

### 8.2 Exercise Content Sync

How does the Go binary get exercise content?

| Option                      | Mechanism                                     | Pros                                      | Cons                           |
| --------------------------- | --------------------------------------------- | ----------------------------------------- | ------------------------------ |
| **A: Fetch from learn-app** | `GET http://localhost:3000/exercises/<id>/`   | Always current, single source of truth    | Learn-app must be running      |
| **B: Bundled in binary**    | Exercises compiled into Go binary             | Works offline, no dependency on learn-app | Stale exercises, larger binary |
| **C: Separate download**    | `af-practice sync-exercises` fetches from CDN | Works without learn-app running           | Extra step, version management |

**Recommendation: Option A** for development (learn-app always running during practice). Option C as future enhancement for production/offline use.

### 8.3 Existing Chapter 3 Exercises

Chapter 3 has ~100 exercises with `INSTRUCTIONS.md` files. Strategy:

1. **Batch conversion**: Write a script that reads INSTRUCTIONS.md and generates CLAUDE.md + config.json + verify.sh
2. **Manual polish**: Review and improve the top 10-20 exercises manually
3. **Registry**: Auto-generate registry.json from exercise directories
4. **Incremental**: Ship with 5-10 polished exercises in Phase 2, expand in Phase 4

### 8.4 Session Management Without tmux

In Phase 1 (no tmux), how do we handle multiple exercises?

**Approach**: The Go binary maintains an in-memory map of `sessionID -> PTY process`. Each exercise gets its own PTY. When the server shuts down, all PTYs are cleaned up gracefully (SIGTERM -> SIGKILL after 5s).

**Reconnection**: When a browser reconnects to `/ws/<session-id>`, the server finds the existing PTY and pipes it to the new WebSocket. The terminal shows the current state (whatever Claude Code is displaying). There is no "replay" of history -- the student sees the current screen, not scrollback.

**Scrollback**: xterm.js has a configurable scrollback buffer (default 1000 lines). This is client-side only. A new WebSocket connection starts with a fresh buffer. If scrollback history is important, tmux (Phase 2) provides server-side scrollback.

---

## Appendix A: Go Dependencies

```go
// go.mod
module github.com/panaversity/agentfactory/practice-server

go 1.22

require (
    github.com/creack/pty v1.1.21           // PTY on Unix
    github.com/gorilla/websocket v1.5.3     // WebSocket server
    // Or: nhooyr.io/websocket v1.8.11      // Alternative, more Go-idiomatic
)

// ConPTY on Windows: direct syscall or github.com/iamacarpet/go-winpty
```

## Appendix B: GitHub Actions Build Matrix

```yaml
strategy:
  matrix:
    include:
      - os: macos-latest
        goos: darwin
        goarch: amd64
      - os: macos-latest
        goos: darwin
        goarch: arm64
      - os: ubuntu-latest
        goos: linux
        goarch: amd64
      - os: ubuntu-latest
        goos: linux
        goarch: arm64
      - os: windows-latest
        goos: windows
        goarch: amd64
      - os: windows-latest
        goos: windows
        goarch: 386
```

## Appendix C: Comparison to Requirements Doc Decisions

For reviewers: here is a section-by-section comparison showing what this strategy changes vs. keeps from `requirements-finalization.md`:

| Section                  | Kept                                 | Changed                                                    |
| ------------------------ | ------------------------------------ | ---------------------------------------------------------- |
| 1.1 Practice button flow | REST API design, exercise resolution | Server URL discovery (port scanning unchanged)             |
| 1.2 Terminal lifecycle   | All states and behaviors             | PTY-based instead of tmux-based (Phase 1)                  |
| 1.3 Exercise lifecycle   | Setup, hints, completion             | No change                                                  |
| 1.4 Session persistence  | Browser refresh, tab close           | Server restart now loses sessions (acceptable for Phase 1) |
| 1.5 Failure modes        | All error handling                   | Added "af-practice not installed" as new state             |
| 2.1 Latency              | All targets                          | No change                                                  |
| 2.2 Reliability          | Auto-reconnect                       | tmux resilience deferred to Phase 2                        |
| 2.4 Compatibility        | macOS Tier 1, Linux Tier 1           | Windows upgraded from Tier 2 (WSL) to Tier 1 (native)      |
| 2.5 Dependencies         | Claude Code, API key                 | Removed Node.js/npm/tmux from required                     |
| 3.1-3.3 APIs             | All API contracts                    | Server is Go, not Node.js (same HTTP interface)            |
| 5.1 Distribution         | --                                   | Completely replaced: Go binary + installer scripts         |
| 5.2 Port                 | 3100 with fallback                   | No change                                                  |
| 5.3 Exercise storage     | Static files in learn-app            | No change                                                  |
| 5.4 Terminal placement   | Tab in Sheet panel                   | No change                                                  |
| 5.6 Completion detection | Script-based verification            | No change                                                  |
