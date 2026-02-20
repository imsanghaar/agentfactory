# Cross-Platform Terminal-in-Browser & Zero-Friction Install Research

## 1. Cross-Platform Terminal Bridging (Windows Focus)

### Claude Code on Windows: Current State (Feb 2026)

Claude Code now runs **natively on Windows** — WSL is no longer required.

| Method                         | Command                                    | Requirements            |
| ------------------------------ | ------------------------------------------ | ----------------------- |
| Native installer (recommended) | `irm https://claude.ai/install.ps1 \| iex` | PowerShell, Windows 10+ |
| npm (legacy)                   | `npm install -g @anthropic-ai/claude-code` | Node.js 18+             |
| WSL2 (optional)                | Same as Linux install                      | WSL2 enabled            |

**Key fact**: The native installer bundles a Bun-compiled binary. No Node.js or npm required. This means we CANNOT assume students have Node.js installed.

**Git Bash is required** for native Windows Claude Code. This means students have a bash-like shell available.

Sources:

- [Claude Code Setup Docs](https://code.claude.com/docs/en/setup)
- [Claude Code Native Installer](https://claudefa.st/blog/guide/native-installer)
- [Claude Code Windows Installation](https://interworks.com/blog/2026/01/27/how-to-install-claude-code-on-windows-11/)

### ConPTY (Windows Pseudo Console API)

Windows 10 (1809+) provides ConPTY — a proper pseudo-terminal API. This is what enables tools like `ttyd` and `node-pty` to work on Windows. Prior to ConPTY, Windows had no native PTY, making terminal-sharing tools impractical.

**Implication**: Any solution using ConPTY requires Windows 10 1809+ (October 2018 update). This is a safe requirement — older versions are EOL.

---

## 2. Zero-Friction Install Patterns

### Pattern Comparison

| Product            | Install Method                                                    | Dependencies                     | Cross-Platform    |
| ------------------ | ----------------------------------------------------------------- | -------------------------------- | ----------------- |
| **Claude Code**    | `curl \| bash` (macOS/Linux), `irm \| iex` (Windows)              | None (standalone binary via Bun) | Yes               |
| **Tailscale**      | `curl https://tailscale.com/install.sh \| sh`                     | None (static Go binary)          | Yes               |
| **Docker Desktop** | GUI installer download                                            | None                             | Yes               |
| **Rust/rustup**    | `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh` | None                             | Yes (not Windows) |
| **ttyd**           | Download binary from GitHub releases                              | None (static C binary)           | Yes (see caveats) |

### Key Insight: The "Already Has" Question

**Critical finding**: Claude Code's native installer does NOT require Node.js. Students may or may not have Node.js installed. We CANNOT rely on `npx` as a distribution mechanism.

**Best zero-friction patterns** (in order of simplicity):

1. **Platform-specific one-liner** (Claude Code / Tailscale pattern): Detects OS, downloads correct binary, adds to PATH. Users run one command.
2. **Single binary download** (ttyd / Go binary pattern): User downloads one file, runs it. No installer needed.
3. **npx** (only if Node.js guaranteed): `npx @our-package/practice-env` — zero-install, but requires Node.js.

### npx Analysis

npx downloads the package to a temp folder, executes it, then cleans up. Advantages:

- Truly zero-install if Node.js is present
- Always gets latest version
- No PATH management needed

**Verdict**: npx is viable ONLY as a secondary install path for users who happen to have Node.js. Cannot be the primary method.

Sources:

- [Building Great CLIs in 2025: Node.js vs Go vs Rust](https://medium.com/@no-non-sense-guy/building-great-clis-in-2025-node-js-vs-go-vs-rust-e8e4bf7ee10e)
- [Tailscale installer.sh](https://github.com/tailscale/tailscale/blob/main/scripts/installer.sh)

---

## 3. Terminal-in-Browser Solutions: Comprehensive Comparison

### ttyd (RECOMMENDED — with caveats)

**What**: C-based tool that shares a terminal over HTTP/WebSocket using xterm.js.

| Feature             | Status                                                            |
| ------------------- | ----------------------------------------------------------------- |
| Linux/macOS support | Pre-built static binaries (aarch64, x86_64, arm, etc.)            |
| Windows support     | `ttyd.win32.exe` available in releases (32-bit only, uses ConPTY) |
| xterm.js version    | Embedded, fully featured with CJK/IME                             |
| Binary size         | ~3-5 MB                                                           |
| Protocol            | WebSocket over HTTP, optional SSL                                 |
| Write mode          | `-W` flag enables input from browser                              |
| Reconnect           | Built-in support                                                  |
| Auth                | Optional basic auth                                               |

**Windows caveat**: Only a 32-bit `.exe` is provided. Native Windows console programs may need `winpty` wrapper. The maintainer closed "Windows binaries?" issue as wontfix in 2018, but subsequently added ConPTY support and ships a win32 binary.

**Verified asset list (v1.7.7)**:

```
ttyd.aarch64, ttyd.arm, ttyd.armhf, ttyd.i686,
ttyd.mips, ttyd.mips64, ttyd.mips64el, ttyd.mipsel,
ttyd.s390x, ttyd.win32.exe, ttyd.x86_64
```

No 64-bit Windows binary. No macOS binary (macOS users typically use Homebrew: `brew install ttyd`).

Sources:

- [ttyd GitHub](https://github.com/tsl0922/ttyd)
- [ttyd releases](https://github.com/tsl0922/ttyd/releases/tag/1.7.7)
- [Windows binaries issue #101](https://github.com/tsl0922/ttyd/issues/101)

### GoTTY

**What**: Go-based tool that turns CLI tools into web applications via xterm.js/hterm.

| Feature             | Status                                         |
| ------------------- | ---------------------------------------------- |
| Linux/macOS support | Pre-built binaries                             |
| Windows support     | **NOT SUPPORTED**                              |
| Last update         | Archived/unmaintained (original repo by yudai) |

**Verdict**: Dead project, no Windows support. Not viable.

Source: [GoTTY GitHub](https://github.com/yudai/gotty)

### tty2web

**What**: Go-based fork of GoTTY with improvements including Windows ConPTY support.

| Feature             | Status                                                      |
| ------------------- | ----------------------------------------------------------- |
| Linux/macOS/FreeBSD | Pre-built binaries                                          |
| Windows support     | Code supports ConPTY, but **NO Windows binary in releases** |
| Features            | Bind/reverse mode, bidirectional file transfer              |

**Verdict**: Has Windows support in code but doesn't ship Windows binaries. Would need to cross-compile ourselves.

Source: [tty2web GitHub](https://github.com/kost/tty2web)

### Shellinabox

**What**: Web-based terminal emulator using Ajax (not WebSocket).

| Feature         | Status                               |
| --------------- | ------------------------------------ |
| Technology      | Ajax-based (outdated, not WebSocket) |
| Windows support | No                                   |
| Maintenance     | Abandoned                            |

**Verdict**: Outdated technology, no Windows, dead project. Not viable.

### code-server

**What**: VS Code in the browser, which includes terminal access.

| Feature         | Status                                               |
| --------------- | ---------------------------------------------------- |
| Platforms       | Linux amd64/arm64, macOS amd64 only                  |
| Windows support | No native server binary                              |
| Size            | ~200+ MB                                             |
| Complexity      | Full VS Code — massive overkill for terminal sharing |

**Verdict**: Way too heavy. We need a terminal, not a full IDE.

Source: [code-server GitHub](https://github.com/coder/code-server)

### VibeTunnel

**What**: Browser-based terminal built with Bun/Node.js, xterm.js, and named pipes. Originally a macOS menu-bar app.

| Feature      | Status                                                         |
| ------------ | -------------------------------------------------------------- |
| Architecture | Swift menubar app + Bun/Node.js server + Lit/xterm.js frontend |
| Platforms    | macOS only                                                     |
| Protocol     | Server-Sent Events (SSE), not WebSocket                        |
| Notable      | Uses same xterm.js as VS Code                                  |

**Verdict**: macOS-only, tied to Swift/SwiftUI. Not cross-platform. But validates the architecture: local server + xterm.js frontend works well.

Source: [VibeTunnel](https://steipete.me/posts/2025/vibetunnel-turn-any-browser-into-your-mac-terminal)

### imprint

**What**: Go-based tool that lets AI agents control a terminal via MCP, using ttyd + tmux + go-rod + xterm.js.

| Feature         | Status                                     |
| --------------- | ------------------------------------------ |
| Platforms       | macOS, Linux (Ubuntu/Debian, Arch)         |
| Windows support | Not mentioned                              |
| Architecture    | ttyd + tmux + headless Chrome + MCP        |
| Use case        | AI agent terminal testing, not user-facing |

**Verdict**: Overly complex for our use case (requires Chrome, tmux). But validates ttyd as the PTY layer.

Source: [imprint GitHub](https://github.com/kessler-frost/imprint)

### claude-code-gui (Tauri)

**What**: Desktop GUI for Claude Code built with Tauri, React, xterm.js, and portable-pty.

| Feature       | Status                                           |
| ------------- | ------------------------------------------------ |
| Architecture  | Tauri (Rust backend) + React + xterm.js          |
| PTY           | portable-pty (Rust crate) for pseudo-terminal    |
| Platforms     | Cross-platform via Tauri (Windows, macOS, Linux) |
| Communication | Tauri event system for PTY streams               |

**Verdict**: Proves xterm.js + PTY works for Claude Code rendering. But Tauri requires a desktop app install — too heavy for our "embed in browser" requirement. However, the PTY approach (portable-pty) is worth noting for a custom Go/Rust solution.

Source: [claude-code-gui GitHub](https://github.com/5Gears0Chill/claude-code-gui)

---

## 4. The ttyd + Claude Code Rendering Test

### Claude Code's Terminal Architecture

Claude Code uses a **custom React-to-terminal renderer** (evolved from Ink):

1. Constructs a React scene graph
2. Layouts elements
3. Rasterizes to a 2D screen buffer
4. Diffs against previous frame
5. Generates ANSI escape sequences from the diff

This is standard terminal output — any terminal emulator that handles ANSI escape codes should render it.

### Known xterm.js Rendering Issues with Claude Code

| Issue                                  | Severity | Workaround                                            |
| -------------------------------------- | -------- | ----------------------------------------------------- |
| Unicode box-drawing characters         | Low      | Falls back to ASCII (`+`, `-`) — cosmetic only        |
| Terminal flickering in multiplexers    | Medium   | Resolved by DEC mode 2026 synchronized output         |
| Progress bar rendering (`\r` handling) | Low      | Only affects command output, not Claude Code's own UI |
| High scroll event rate (4000-6700/sec) | Medium   | Only in tmux; direct terminal works fine              |

### Will Claude Code TUI render correctly in ttyd?

**Assessment: YES, with minor cosmetic issues.**

ttyd uses xterm.js, which is the same terminal emulator library used by:

- VS Code's integrated terminal
- Hyper terminal
- Various web-based terminals

Claude Code's ANSI output is standard. The only known issue is Unicode box-drawing characters may render as ASCII fallbacks in some xterm.js configurations. The Claude Code team has already addressed flickering with synchronized output support.

**No reports found** of people specifically running Claude Code inside ttyd. This is an untested combination that needs verification.

Sources:

- [Claude Code Terminal UI Internals](https://kotrotsos.medium.com/claude-code-internals-part-11-terminal-ui-542fe17db016)
- [Interactive TUI frozen issue #23326](https://github.com/anthropics/claude-code/issues/23326)
- [Flickering issue #1913](https://github.com/anthropics/claude-code/issues/1913)
- [Scroll events issue #9935](https://github.com/anthropics/claude-code/issues/9935)
- [xterm.js headless emulator issue #13637](https://github.com/anthropics/claude-code/issues/13637)

---

## 5. Single Binary Distribution Approaches

### Option A: Ship ttyd directly

Download ttyd binary per-platform, wrap in our install script.

**Pros**: Battle-tested C code, small binary, proven WebSocket + xterm.js
**Cons**: No macOS binary in releases (need Homebrew or compile), only 32-bit Windows binary, we don't control the binary

### Option B: Go binary with embedded xterm.js

Write a custom Go binary that:

- Embeds xterm.js HTML/JS via `go:embed` (Go 1.16+)
- Creates a PTY (`creack/pty` on Unix, ConPTY on Windows)
- Serves WebSocket bridge between browser and PTY
- Cross-compiles to all platforms via `GOOS`/`GOARCH`

**Existing examples**:

- [simple-golang-react-xtermjs-websocket](https://github.com/sagoresarker/simple-golang-react-xtermjs-websocket) — working demo
- [web-terminal](https://github.com/soolaugust/web-terminal) — Go + xterm.js + WebSocket demo
- tty2web itself (Go-based, similar architecture)

**Pros**: Full control, true single binary, cross-compile all platforms, embed everything
**Cons**: Must build and maintain PTY handling ourselves (or use creack/pty + ConPTY)

### Option C: Rust binary with portable-pty

Similar to Option B but in Rust using `portable-pty` crate.

**Pros**: portable-pty is battle-tested (used by wezterm, claude-code-gui), great cross-compilation via cargo-dist
**Cons**: Rust cross-compilation is more complex than Go, larger binary size

### Option D: Node.js/Bun server (like VibeTunnel)

Use Bun to compile a self-contained binary with xterm.js frontend.

**Pros**: Bun can compile to standalone binary, JavaScript ecosystem familiarity
**Cons**: Bun standalone binaries are larger (~50-80MB), newer/less proven, Bun cross-compilation is limited

### Comparison Matrix

| Approach                | Binary Size | Cross-Platform                         | Build Complexity | Windows PTY        | Maintenance         |
| ----------------------- | ----------- | -------------------------------------- | ---------------- | ------------------ | ------------------- |
| **Ship ttyd**           | ~5 MB       | Partial (no macOS release, 32-bit Win) | None (pre-built) | ConPTY (win32)     | External dependency |
| **Go + embed**          | ~10-15 MB   | Excellent (GOOS/GOARCH)                | Medium           | ConPTY via Go libs | We own it           |
| **Rust + portable-pty** | ~8-12 MB    | Good (cargo cross)                     | High             | portable-pty       | We own it           |
| **Bun standalone**      | ~50-80 MB   | Limited                                | Low              | node-pty           | Bun ecosystem risk  |

---

## 6. Summary & Recommendations

### Recommended Architecture: Custom Go Binary

A Go binary that embeds xterm.js HTML and bridges WebSocket to a local PTY is the strongest option:

1. **True single binary** — no dependencies, no installers
2. **Cross-platform** — Go cross-compilation is trivial (`GOOS=windows GOARCH=amd64`)
3. **Small** — ~10-15 MB including embedded frontend
4. **Battle-tested pattern** — GoTTY, tty2web, and ttyd all use this exact architecture
5. **Windows ConPTY** — Go libraries exist for this (e.g., `iamacarpet/go-winpty`, ConPTY via Windows API)

### Distribution Pattern

Follow the Claude Code / Tailscale pattern:

```bash
# macOS/Linux
curl -fsSL https://[our-domain]/install.sh | bash

# Windows
irm https://[our-domain]/install.ps1 | iex
```

The install script:

1. Detects OS + architecture
2. Downloads the correct binary from GitHub releases
3. Places it in a standard location
4. Prints "Run `practice-env` to start"

### Fallback: ttyd as MVP

For a quick MVP, shipping ttyd directly works on Linux and Windows (32-bit). macOS users would need `brew install ttyd`. This gets us to market faster but has gaps (no macOS binary, 32-bit only on Windows).

### Open Questions Requiring Validation

1. **Does Claude Code TUI actually render correctly in ttyd?** — Needs hands-on test
2. **Windows ConPTY + Claude Code interaction** — Does `ttyd claude` work on Windows?
3. **Performance at high scroll rates** — xterm.js can handle 4000+ events/sec, but browser tab may lag
4. **Keyboard input passthrough** — All Claude Code keybindings (Ctrl-C, etc.) must work through WebSocket
5. **Terminal resize** — Does xterm.js resize propagate correctly through to Claude Code?
