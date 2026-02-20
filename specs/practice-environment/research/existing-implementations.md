# Existing Implementations: Browser-Embedded Terminals

Research document for the Practice Environment feature.
Date: 2026-02-12

---

## Table of Contents

1. [xterm.js + WebSocket Architectures](#1-xtermjs--websocket-architectures)
2. [Production Implementations](#2-production-implementations)
3. [node-pty and Alternatives](#3-node-pty-and-alternatives)
4. [tmux Integration Patterns](#4-tmux-integration-patterns)
5. [Security Model](#5-security-model)
6. [ChatKit Custom Widgets](#6-chatkit-custom-widgets)
7. [Educational Platform Terminals](#7-educational-platform-terminals)
8. [React Wrappers for xterm.js](#8-react-wrappers-for-xtermjs)
9. [Recommendations](#9-recommendations)

---

## 1. xterm.js + WebSocket Architectures

### Core Pattern

Every production browser-embedded terminal follows the same fundamental architecture:

```
Browser (xterm.js) <--WebSocket--> Server (node-pty / pty) <--pty fd--> Shell Process
```

**xterm.js** (https://github.com/xtermjs/xterm.js) is the dominant terminal emulator library for the web. It handles:

- VT100/VT220/xterm escape code rendering
- Cursor management, colors, scrollback buffer
- User input capture and encoding
- WebGL2-accelerated rendering (via `@xterm/addon-webgl`)
- Addon ecosystem: `addon-attach` (WebSocket), `addon-fit` (resize), `addon-search`, `addon-serialize`

### addon-attach Protocol

The `@xterm/addon-attach` addon connects xterm.js directly to a WebSocket:

```javascript
import { Terminal } from "@xterm/xterm";
import { AttachAddon } from "@xterm/addon-attach";

const terminal = new Terminal();
const ws = new WebSocket("wss://localhost:7681/ws");
const attachAddon = new AttachAddon(ws);
terminal.loadAddon(attachAddon);
terminal.open(document.getElementById("terminal"));
```

**Protocol details:**

- WebSocket binary type is set to `arraybuffer`
- Text input from `term.onData` is sent as text frames
- Binary data from `term.onBinary` is sent as binary frames
- Incoming data is written via `writeUtf8` (ArrayBuffer conversion)
- The protocol does NOT separate message types by default -- for multiplexing, you need a custom protocol layer (single-byte prefix pattern)

**Flow control caveat:** WebSocket has no native backpressure. Buffers on both ends can grow unbounded. Production systems must implement application-level flow control (XON/XOFF or custom pause/resume signaling via `ws.bufferedAmount` monitoring).

Sources:

- https://github.com/xtermjs/xterm.js
- https://xtermjs.org/docs/guides/flowcontrol/
- https://github.com/xtermjs/xterm.js/discussions/4625

---

## 2. Production Implementations

### 2.1 VS Code Terminal

**Architecture: IPC, not WebSocket**

VS Code's terminal does NOT use WebSocket. It uses a three-process IPC architecture:

```
Renderer Process (xterm.js UI)
    |
    | IPC (inter-process communication)
    v
Pty Host Process (PtyService)
    |
    | fork/spawn
    v
Shell Process (bash/zsh/pwsh via node-pty)
```

**Key components:**

- **Renderer Process**: Hosts `TerminalInstance`, renders via xterm.js (`@xterm/xterm 6.1.0-beta`)
- **Pty Host Process**: Isolated process running `PtyService`, manages shell lifecycle
- **Extension Host**: `ExtHostTerminalService` implements the `vscode.window.createTerminal()` API

**Why IPC not WebSocket:** VS Code runs as an Electron app where processes share a machine. IPC is lower-latency and avoids network stack overhead. The Pty Host is isolated so that shell crashes don't bring down the UI.

**For remote scenarios** (VS Code Server, Codespaces), VS Code DOES use WebSocket to bridge the renderer in the browser to the remote Pty Host. This is the architecture we care about.

**Key dependencies:**

- `node-pty 1.2.0-beta.6` -- native PTY bindings
- `@xterm/xterm 6.1.0-beta.102` -- terminal emulator

**Lessons for our design:**

- Separate the PTY host from the UI process for crash isolation
- Use IPC locally, WebSocket only when crossing network boundaries
- Terminal resize events need explicit handling (cols/rows sent as control messages)

Sources:

- https://deepwiki.com/microsoft/vscode/6.6-terminal-ui-and-layout
- https://code.visualstudio.com/docs/terminal/advanced
- https://github.com/microsoft/node-pty

### 2.2 ttyd -- Terminal Sharing Over HTTP

**Repo:** https://github.com/tsl0922/ttyd

**Architecture:**

```
Browser (xterm.js + WebGL2)
    |
    | WebSocket (libwebsockets)
    v
ttyd server (C, libwebsockets + libuv)
    |
    | forkpty()
    v
Shell/Command Process
```

**Tech stack:**

- Written in C (56% of codebase)
- Backend: libwebsockets + libuv for async I/O
- Frontend: xterm.js with WebGL2 renderer
- Default port: 7681

**Key features:**

- SSL/TLS via OpenSSL or Mbed TLS
- Basic auth (`-c user:pass`)
- Reverse proxy auth via HTTP headers (`-H`)
- **Origin checking** (`-O` flag) -- prevents cross-origin WebSocket
- ZMODEM file transfer (lrzsz) and trzsz
- Sixel graphics rendering
- Single-client mode, configurable client limits
- CJK and IME support

**Pros:**

- Extremely lightweight (single binary, ~2MB)
- Production-proven, actively maintained
- Cross-platform (Linux, macOS, Windows via MSYS2)
- Built-in auth and TLS

**Cons:**

- Written in C (harder to extend from Node.js)
- Single-command model (one command per ttyd instance)
- No session multiplexing built in (need tmux externally)

**Lessons for our design:**

- The `-O` origin check flag is a good security pattern
- Single-binary deployment is ideal for local tools
- ttyd is a reference for minimal, correct WebSocket terminal implementation

Sources:

- https://github.com/tsl0922/ttyd
- https://tsl0922.github.io/ttyd/

### 2.3 WeTTY -- Web + TTY

**Repo:** https://github.com/butlerx/wetty

**Architecture:**

```
Browser (xterm.js)
    |
    | WebSocket
    v
WeTTY Node.js Server (Express + ws)
    |
    | SSH or /bin/login
    v
Shell/SSH Target
```

**Tech stack:**

- TypeScript (65%) / JavaScript (28%)
- Node.js 18+ required
- xterm.js frontend
- WebSocket transport (not Socket.IO)
- pnpm package manager

**Connection modes:**

1. **Local mode** (as root): Spawns `/bin/login` for local shell access
2. **SSH mode** (default): Connects to SSH server via `--ssh-host`, `--ssh-port`, `--ssh-user`

**Auth options:**

- Password authentication
- Public key authentication
- Combined methods (`publickey,password`)
- Client private keys for passwordless connections

**Key features:**

- SSL/TLS support (`--ssl-key`, `--ssl-cert`)
- Base path configuration (for reverse proxy setups)
- Multiple concurrent sessions
- Docker deployment available

**Pros:**

- Pure Node.js/TypeScript -- easy to extend
- Active community (522 commits, 68 contributors)
- SSH integration for remote machine access
- WebSocket (not polling) for low latency

**Cons:**

- SSH-centric design (not ideal for local pty spawning)
- No built-in session multiplexing
- Requires Node.js 18+

**Lessons for our design:**

- TypeScript implementation is a good reference for our Node.js server
- SSH mode is irrelevant for us (we want local pty), but the WebSocket plumbing is reusable
- Docker deployment pattern is worth adopting

Sources:

- https://github.com/butlerx/wetty
- https://www.npmjs.com/package/wetty

### 2.4 Gitpod Browser Terminal

**Architecture:**

```
Browser (xterm.js via Theia/VS Code)
    |
    | WebSocket (JSONRPC 2.0)
    v
Gitpod Server (TypeScript)
    |
    | Kubernetes Pod API
    v
Workspace Pod (ephemeral, per-user)
```

**Key details:**

- Uses JSONRPC 2.0 over WebSocket for RPC
- Each workspace is a dedicated Kubernetes pod
- Workspace URLs: `https://[WORKSPACE_NAME].[CLUSTER_NAME].gitpod.io`
- Terminal runs inside the workspace pod

**Gitpod also has `xterm-web-ide`** (https://github.com/gitpod-io/xterm-web-ide):

- A standalone web IDE built entirely on xterm.js
- Supports NeoVim, Emacs, Vim in the browser
- TypeScript (55%), Vite-based build
- Experimental -- "not ready for production use"

**Security vulnerability (documented by Snyk Labs):**

- The WebSocket server did NOT validate the Origin header
- Authentication relied solely on cookies during WS upgrade handshake
- No additional auth within the WebSocket exchange itself
- Subdomain relationship exploitation: workspace URLs share the same registrable domain as `gitpod.io`, allowing cross-site WebSocket hijacking from a malicious workspace
- **Lesson: Cookie-only auth + no origin validation = critical RCE vulnerability**

Sources:

- https://github.com/gitpod-io/xterm-web-ide
- https://labs.snyk.io/resources/gitpod-remote-code-execution-vulnerability-websockets/
- https://www.gitpod.io/docs/references/ides-and-editors/browser-terminal

### 2.5 pyxtermjs -- Python Reference Implementation

**Repo:** https://github.com/cs01/pyxtermjs

**Architecture:**

```
Browser (xterm.js)
    |
    | Socket.IO (WebSocket)
    v
Flask Server (flask-socketio)
    |
    | Python pty module
    v
bash process
```

**Purpose:** Proof-of-concept showing xterm.js + Python + Flask + WebSocket integration.

**Data flow:**

1. Flask server spawns a pty using Python's built-in `pty` module
2. Terminal output flows from bash -> pty -> Flask -> Socket.IO -> xterm.js
3. User input flows from xterm.js -> Socket.IO -> Flask -> pty -> bash

**CLI options:**

```
-p PORT    (default: 5000)
--host     (default: 127.0.0.1)
--command  (default: bash)
--debug    (debug mode)
```

**Pros:**

- Dead simple reference implementation
- Shows the minimal viable architecture
- Python-native (uses stdlib `pty` module)

**Cons:**

- Not production-ready (proof of concept)
- Socket.IO adds overhead vs raw WebSocket
- No auth, no TLS, no session management

Sources:

- https://github.com/cs01/pyxtermjs
- https://pypi.org/project/pyxtermjs/

---

## 3. node-pty and Alternatives

### 3.1 node-pty (Microsoft)

**Repo:** https://github.com/microsoft/node-pty

The dominant library for spawning pseudo-terminals in Node.js. Used by VS Code, Hyper, Theia, and 25+ terminal emulators.

**API surface:**

```javascript
import * as pty from "node-pty";
import * as os from "node:os";

const shell = os.platform() === "win32" ? "powershell.exe" : "bash";

const ptyProcess = pty.spawn(shell, [], {
  name: "xterm-color",
  cols: 80,
  rows: 30,
  cwd: process.env.HOME,
  env: process.env,
});

// Read output
ptyProcess.onData((data) => {
  // data is a string containing terminal output
  process.stdout.write(data);
});

// Write input
ptyProcess.write("ls\r");

// Resize
ptyProcess.resize(100, 40);

// Kill
ptyProcess.kill();
```

**Flow control (optional):**

```javascript
const ptyProcess = pty.spawn(shell, [], { handleFlowControl: true });
ptyProcess.write("\x13"); // XOFF - pause output
ptyProcess.write("\x11"); // XON - resume output
```

**Platform support:**
| Platform | Mechanism |
|----------|-----------|
| Linux | Native `forkpty(3)` |
| macOS | Native `forkpty(3)` |
| Windows 1809+ | ConPTY API |

**Build requirements:**

- Linux: `make`, `python`, `build-essential`
- macOS: Xcode command line tools
- Windows: Visual Studio 2022 with C++ and Spectre-mitigated libs

**Critical limitations:**

1. **NOT thread-safe** -- cannot run across worker threads
2. **Permission inheritance** -- all spawned processes run at parent process permission level
3. **Native addon** -- requires compilation (node-gyp), complicates deployment
4. **Node.js version tracking** -- compatibility follows VS Code's Node version

**Security considerations:**

- Processes inherit parent permissions (if server runs as root, shell runs as root)
- **Recommendation from node-pty docs**: "Care should be taken when using node-pty inside a server accessible on the internet. Launching the pty inside a container is recommended."
- No built-in sandboxing -- must use OS-level isolation (containers, namespaces)

Sources:

- https://github.com/microsoft/node-pty
- https://www.npmjs.com/package/node-pty

### 3.2 Alternatives to node-pty

| Library                  | Language          | Mechanism                              | Notes                                                   |
| ------------------------ | ----------------- | -------------------------------------- | ------------------------------------------------------- |
| **node-pty** (Microsoft) | C++/N-API         | forkpty(3) / ConPTY                    | Industry standard, VS Code uses it                      |
| **pty.node**             | C                 | forkpty(3)                             | Lighter, fewer features                                 |
| **node-partty**          | C                 | forkpty(3)                             | Smart defaults variant                                  |
| **get-pty-output**       | Rust (N-API)      | portable-pty (unix) / conpty (windows) | Better cross-platform, no node-gyp                      |
| **node-rust-pty**        | Rust (N-API)      | portable-pty                           | High-perf, virtual DOM rendering, advanced session mgmt |
| **@zenyr/bun-pty**       | Rust (FFI)        | portable-pty                           | Bun runtime specific                                    |
| **Python `pty` module**  | C (Python stdlib) | forkpty(3)                             | Unix-only, no Windows                                   |

**Recommendation:** Use **node-pty** unless build complexity is a blocker. It is the most battle-tested option with the widest platform support. If native compilation is problematic, **get-pty-output** (Rust-based with N-API bindings) avoids node-gyp entirely and offers equivalent cross-platform support.

Sources:

- https://github.com/LayerDynamics/node-rust-pty
- https://www.npmjs.com/package/get-pty-output
- https://www.npmjs.com/package/pty.node

---

## 4. tmux Integration Patterns

### 4.1 node-tmux

**Repo:** https://github.com/StarlaneStudios/node-tmux

Lightweight Node.js wrapper that shells out to the `tmux` CLI.

**API:**

```javascript
import { tmux } from "node-tmux";

const tm = await tmux(); // Validates tmux is installed

// Session lifecycle
await tm.newSession("practice-env", "bash"); // Create
await tm.hasSession("practice-env"); // Check
await tm.listSessions(); // List all
await tm.renameSession("practice-env", "new"); // Rename
await tm.killSession("practice-env"); // Destroy

// Send input to a session
await tm.writeInput("practice-env", "ls -la", true); // true = append newline
```

**How it works:** Executes `tmux` CLI commands via `child_process.exec`. No direct C bindings -- pure shell orchestration.

**Pros:**

- Simple, small API surface
- No native dependencies
- Manages session lifecycle cleanly

**Cons:**

- Shells out to `tmux` CLI (process spawn per operation)
- No streaming of session output
- No attach/detach in the programmatic sense
- Requires tmux installed on the system

### 4.2 WebMux (Rust + Vue)

**Repo:** https://github.com/nooesc/webmux

Web-based tmux session viewer with WebSocket real-time communication.

**WebSocket message protocol:**

- Session events: `sessions-list`, `session-created`, `session-killed`, `session-renamed`
- Attach/detach: `attached`, `disconnected`
- Window events: `windows-list`, `window-created`, `window-selected`, `window-killed`, `window-renamed`
- Terminal I/O: terminal output messages
- Monitor: `tmux-update` events

**Stack:** Rust backend, Vue 3 + Tailwind frontend, PWA support.

### 4.3 WebTMUX (Express + Socket.IO + xterm.js)

**Repo:** https://github.com/nonoxz/webtmux

Connects xterm.js in the browser to tmux sessions via Express + Socket.IO.

**Stack:** Node.js (Express), Socket.IO, xterm.js.

### 4.4 tmux-mcp (MCP Server)

An MCP server providing programmatic tmux control for AI assistants. Uses `libtmux` (Python) to execute tmux commands.

### 4.5 Recommended tmux Integration Pattern

For our use case (managing practice environment sessions):

```javascript
// Recommended: node-tmux for lifecycle + node-pty for I/O
import { tmux } from "node-tmux";
import * as pty from "node-pty";

// Option A: Use tmux for session persistence, node-pty for WebSocket bridge
const tm = await tmux();
await tm.newSession("student-session-123");

// Attach to tmux session via node-pty
const ptyProcess = pty.spawn(
  "tmux",
  ["attach-session", "-t", "student-session-123"],
  {
    name: "xterm-256color",
    cols: 80,
    rows: 24,
    cwd: "/home/student",
    env: process.env,
  },
);

// Bridge pty to WebSocket
ptyProcess.onData((data) => ws.send(data));
ws.on("message", (data) => ptyProcess.write(data));
```

**Why this pattern:**

- tmux handles session persistence (survives WebSocket disconnect)
- node-pty provides the PTY bridge for xterm.js compatibility
- Clean separation: tmux = session lifecycle, node-pty = I/O transport, xterm.js = rendering

Sources:

- https://github.com/StarlaneStudios/node-tmux
- https://github.com/nooesc/webmux
- https://github.com/nonoxz/webtmux

---

## 5. Security Model

### 5.1 WebSocket Security Fundamentals

**Critical fact: WebSockets bypass CORS entirely.** The Same-Origin Policy and CORS restrictions are ineffective because:

1. No HTTP response data is required to complete the WebSocket handshake
2. Data transfer occurs over the WebSocket protocol (ws/wss), not HTTP

This means **any website can open a WebSocket to localhost** unless the server explicitly validates the Origin header.

### 5.2 Origin Validation (Mandatory)

```javascript
const wss = new WebSocket.Server({
  verifyClient: (info, cb) => {
    const origin = info.origin || info.req.headers.origin;
    const allowedOrigins = [
      "http://localhost:3000", // Docusaurus dev
      "https://your-domain.com", // Production
    ];

    if (allowedOrigins.includes(origin)) {
      cb(true);
    } else {
      cb(false, 403, "Forbidden");
    }
  },
});
```

**Key patterns:**

- Whitelist only trusted origins
- Reject null origins and `file://` protocols
- Validate during the handshake (before connection is established)

### 5.3 Authentication Strategies

**JWT Token Auth (Recommended for our use case):**

```javascript
// During WebSocket upgrade handshake
const wss = new WebSocket.Server({
  verifyClient: (info, cb) => {
    const url = new URL(info.req.url, "http://localhost");
    const token = url.searchParams.get("token");

    try {
      const decoded = jwt.verify(token, process.env.JWT_SECRET);
      info.req.userId = decoded.userId;
      cb(true);
    } catch (err) {
      cb(false, 401, "Unauthorized");
    }
  },
});
```

**Why NOT cookie-based auth:**

- Cookies are sent automatically on WebSocket upgrade (CSRF risk)
- SameSite cookies help but don't prevent subdomain attacks (Gitpod vulnerability)
- Token-in-URL is explicit and controllable

### 5.4 Gitpod Vulnerability Case Study

Gitpod's security failure is directly relevant to our architecture:

1. WebSocket server accepted connections from ANY origin
2. Authentication relied solely on browser cookies during WS upgrade
3. No additional auth within the WebSocket exchange
4. Workspace subdomains shared the same registrable domain as `gitpod.io`
5. Result: **Remote Code Execution** -- attacker could execute arbitrary commands in victim's workspace

**Our mitigation:**

- Always validate Origin header
- Use token-based auth, not cookies
- Short-lived tokens (2-5 minute expiry)
- Scope tokens: `scope: "terminal:attach"`

### 5.5 Process Isolation

**node-pty processes inherit parent permissions.** Mitigations:

| Technique                        | Isolation Level | Overhead |
| -------------------------------- | --------------- | -------- |
| Unprivileged user (UID 1000)     | Basic           | None     |
| Container (Docker)               | Strong          | Moderate |
| gVisor (user-space kernel)       | Very Strong     | Moderate |
| Kata Containers (lightweight VM) | Maximum         | High     |
| Firecracker (microVM)            | Maximum         | High     |

**For localhost educational tool:**

- Run the WebSocket server as a non-root user
- Spawn shells with restricted environment
- Consider Docker container for the practice env (optional, adds complexity)

**Container security hardening (if using Docker):**

```javascript
// Dockerode container creation
{
  HostConfig: {
    Memory: 256 * 1024 * 1024,           // 256 MB limit
    NanoCpus: 500_000_000,               // 0.5 CPU
    PidsLimit: 256,                      // Process limit
    CapDrop: ["ALL"],                    // Drop all capabilities
    SecurityOpt: ["no-new-privileges"],  // Prevent escalation
    Tmpfs: { "/tmp": "rw,size=64m" }    // Volatile /tmp
  }
}
```

### 5.6 Rate Limiting & Resource Protection

```
Per-connection: 10 messages/second
Global: 1000 messages/second
Per-IP: 5 concurrent connections
Max message size: 1 MB
Idle timeout: 10 minutes
Ping/pong keepalive: 30 seconds
```

### 5.7 Security Checklist for Our Implementation

- [ ] WSS (TLS) in production (self-signed OK for localhost dev)
- [ ] Origin validation on every WebSocket upgrade
- [ ] Token-based auth (not cookies) during handshake
- [ ] Short-lived tokens (2-5 minute expiry)
- [ ] Scoped tokens (`terminal:attach` permission)
- [ ] Message size limits (1MB max)
- [ ] Rate limiting on upgrade handler
- [ ] Idle connection timeout (10 min)
- [ ] Non-root process for spawned shells
- [ ] Input sanitization (no shell injection via WebSocket)
- [ ] Structured logging of auth failures

Sources:

- https://websocket.org/guides/security/
- https://labs.snyk.io/resources/gitpod-remote-code-execution-vulnerability-websockets/
- https://blog.securityevaluators.com/websockets-not-bound-by-cors-does-this-mean-2e7819374acc
- https://cwe.mitre.org/data/definitions/1385.html
- https://thinhdanggroup.github.io/realtime-developer-sandbox/

---

## 6. ChatKit Custom Widgets

### 6.1 Widget System Overview

ChatKit widgets are JSON-defined UI components rendered inside the chat surface. They are NOT arbitrary React components -- they follow a strict schema.

**Widget structure:**

- `WidgetRoot` -- top-level container (Card, ListView, or Basic)
- `WidgetNode` -- child components within the root

**Available widget types:**

| Category    | Types                                          |
| ----------- | ---------------------------------------------- |
| Containers  | Card, ListView, Basic                          |
| Interactive | Button, Form, Select, DatePicker               |
| Display     | Image, Badge, Markdown, Text, Headline, Spacer |
| Input       | TextInput, Radio                               |

### 6.2 Can You Embed xterm.js in a ChatKit Widget?

**No. ChatKit widgets do NOT support arbitrary React components.**

Evidence:

1. **GitHub Issue #73** (chatkit-js): OpenAI's Tyler Smith stated "We don't currently have anything to share about rendering Widgets outside the context of our products." Only structured widget schemas (Card, Row, Markdown, etc.) are supported.
2. **OpenAI Community Forum**: When asked "Is it possible to render custom UI in ChatKit?", the answer was to extract JSON from the chat and render custom UI externally -- not within the ChatKit widget system itself.
3. **Widget types are closed**: No custom widget type registration mechanism exists. You can only use the predefined set.

### 6.3 What ChatKit CAN Do

**Widget actions:** Buttons and controls can trigger server-side logic via `ActionConfig`. The server receives a payload and can stream new widgets or update existing ones.

**Effects system:** The advanced samples show an `onEffect` handler that synchronizes server events with client-side state (side panels, status updates). This is the closest to custom rendering.

**Example from advanced samples:**

- **Metro Map**: React Flow visualization rendered in a SIDE PANEL, not inside the chat widget
- **Customer Support**: Itinerary panel updated via server-streamed effects
- **Cat Lounge**: Client effects (`update_cat_status`, `cat_say`) update UI state outside the chat

### 6.4 Workaround: Side Panel Pattern

The advanced samples demonstrate a pattern where ChatKit widgets trigger effects that update a SEPARATE React component rendered alongside (not inside) the chat:

```
+---------------------------+-------------------+
|                           |                   |
|   ChatKit Chat Surface    |   Side Panel      |
|   (standard widgets)      |   (custom React)  |
|                           |                   |
|   [Widget: "Open Term"]   |   <XTerm />       |
|                           |                   |
+---------------------------+-------------------+
```

**This is the viable pattern for embedding a terminal alongside ChatKit.** The terminal lives in a custom React component outside ChatKit, and ChatKit effects/actions control when it appears and what commands to run.

### 6.5 ChatKit Python SDK

**Repo:** https://github.com/openai/chatkit-python

The Python SDK provides:

- `WidgetTemplate.from_file("path/to/my_widget.widget")` -- load widget definitions
- `template.build(data)` -- render with data, returns `DynamicWidgetRoot`
- Widget types: Card, ListView, Basic roots
- Action handling via `ChatKitServer.action()` method

### 6.6 ChatKit Limitations Summary

| Capability                                   | Supported?           |
| -------------------------------------------- | -------------------- |
| Predefined widget types (Card, Button, etc.) | Yes                  |
| Widget actions (button clicks -> server)     | Yes                  |
| Streaming widgets (progressive rendering)    | Yes                  |
| Custom React components inside chat          | **No**               |
| Arbitrary HTML/iframe inside chat            | **No**               |
| Side panel with custom React components      | Yes (via effects)    |
| xterm.js terminal inside chat widget         | **No**               |
| xterm.js terminal in side panel              | **Yes (workaround)** |

Sources:

- https://github.com/openai/chatkit-js/issues/73
- https://community.openai.com/t/is-it-possible-to-render-custom-ui-in-chatkit/1364085
- https://github.com/openai/openai-chatkit-advanced-samples
- https://openai.github.io/chatkit-python/api/chatkit/widgets/
- https://www.eesel.ai/blog/chatkit-widgets
- https://www.eesel.ai/blog/chatkit-python-sdk-widgets

---

## 7. Educational Platform Terminals

### 7.1 KillerCoda (Katacoda successor)

**Architecture:**

- Each session runs in a secure, isolated namespace (Kubernetes-based)
- Uses **Theia** (not raw xterm.js) as the IDE and terminal
- Theia runs as root directly on the main host (not containerized)
- Theia footprint: ~100MB (vs VS Code's ~1GB+)
- Katacoda-compatible scenario format

**Terminal:** Theia provides its own xterm.js-based terminal. The Theia terminal connects to the workspace environment via its internal architecture (IPC to shell process).

**Limitations:** Environments limited to preconfigured VMs and small Kubernetes clusters.

### 7.2 Instruqt

**Architecture:**

- Terminal is a "fully functional terminal emulator in the browser that connects to the target resource"
- Target must be a **container** resource (not Kubernetes cluster directly)
- Configurable: shell, user, group, working directory, command

**Configuration example:**

```yaml
terminal:
  target: my-container
  shell: /bin/bash
  user: root
  group: root
  working_directory: /workspace
```

**For Kubernetes access:** Create a container with kubectl pre-configured, attach terminal to that container.

### 7.3 Docusaurus Terminal Plugins

**`@sp-days-framework/docusaurus-plugin-terminal-codeblock`:**

- Renders realistic terminal OUTPUT (not interactive)
- Command prompts, ANSI colors, interactive highlights
- Theme-aware (light/dark modes)
- Line highlighting with tooltips

**This is display-only, NOT an interactive terminal.** No WebSocket, no pty.

**Other Docusaurus code plugins:**

- `docusaurus-plugin-code-preview` -- live code preview in iframes
- `@docusaurus/theme-live-codeblock` -- interactive code editing (React live)

**None of these provide an interactive terminal with shell access.**

### 7.4 Developer Sandbox Architecture (Best Practices)

From ThinhDA's comprehensive guide on building real-time developer sandboxes:

**Reference architecture:**

```
Browser (xterm.js) <--WSS (TLS)--> Node.js Server <--Unix Socket--> Docker Engine
```

**Performance optimizations:**
| Optimization | Technique |
|---|---|
| Co-location | Server on same host as Docker daemon (Unix socket) |
| Compression | Disabled for interactive traffic (CPU latency) |
| TCP behavior | TCP_NODELAY enabled (default in ws library) |
| NGINX proxy | `proxy_buffering off` on WebSocket path |
| Binary frames | `ws.binaryType = "arraybuffer"` (not base64) |

**Backpressure implementation:**

```
Docker stream -> check ws.bufferedAmount
              -> if > 1MB, pause Docker stream
              -> resume when buffer < 512KB via send callback
```

**Lifecycle management:**

- Idle reap: 10-minute timeout with 5-second granularity
- Immediate kill on client disconnect (unless reconnect semantics)
- Orphan janitor: periodic daemon removes exited containers with sandbox labels
- Docker labels for tracking: `sandbox: true`, `user: <id>`, `created_by: webterm`

**Cold start optimization:**

- Pre-pull images on each host
- Build minimal images with only terminal essentials
- Periodic refresh cycles

Sources:

- https://killercoda.com/
- https://docs.labs.instruqt.com/reference/sandbox/ui/terminal/
- https://www.npmjs.com/package/@sp-days-framework/docusaurus-plugin-terminal-codeblock
- https://thinhdanggroup.github.io/realtime-developer-sandbox/

---

## 8. React Wrappers for xterm.js

For embedding xterm.js in a React application (relevant for our Docusaurus/React frontend):

| Package                   | Maintained   | xterm Version   | API Style                     |
| ------------------------- | ------------ | --------------- | ----------------------------- |
| `xterm-for-react`         | Low activity | Older xterm     | Component-based (`<XTerm />`) |
| `react-xtermjs` (Qovery)  | Active       | Latest @xterm   | Hook (`useXTerm`) + Component |
| `@pablo-lion/xterm-react` | Active       | Latest @xterm   | Component + addons            |
| `xterm-for-react-18`      | Fork         | React 18 compat | Component-based               |

**Recommended: `react-xtermjs` by Qovery** -- provides both hook and component APIs, uses latest `@xterm/xterm`, actively maintained.

```jsx
import { useXTerm } from "react-xtermjs";

function Terminal() {
  const { instance, ref } = useXTerm({
    options: {
      cursorBlink: true,
      fontSize: 14,
      theme: { background: "#1e1e1e" },
    },
  });

  useEffect(() => {
    if (instance) {
      const ws = new WebSocket("ws://localhost:7681");
      const attachAddon = new AttachAddon(ws);
      instance.loadAddon(attachAddon);
    }
  }, [instance]);

  return <div ref={ref} style={{ width: "100%", height: "400px" }} />;
}
```

**Alternative: Direct xterm.js usage** (no wrapper needed for simple cases):

```jsx
import { useRef, useEffect } from "react";
import { Terminal } from "@xterm/xterm";
import { FitAddon } from "@xterm/addon-fit";
import { AttachAddon } from "@xterm/addon-attach";

function TerminalComponent({ wsUrl }) {
  const termRef = useRef(null);

  useEffect(() => {
    const terminal = new Terminal({ cursorBlink: true });
    const fitAddon = new FitAddon();
    terminal.loadAddon(fitAddon);
    terminal.open(termRef.current);
    fitAddon.fit();

    const ws = new WebSocket(wsUrl);
    ws.onopen = () => {
      const attachAddon = new AttachAddon(ws);
      terminal.loadAddon(attachAddon);
      // Send initial resize
      ws.send(
        JSON.stringify({
          type: "resize",
          cols: terminal.cols,
          rows: terminal.rows,
        }),
      );
    };

    const resizeObserver = new ResizeObserver(() => fitAddon.fit());
    resizeObserver.observe(termRef.current);

    return () => {
      resizeObserver.disconnect();
      ws.close();
      terminal.dispose();
    };
  }, [wsUrl]);

  return <div ref={termRef} />;
}
```

Sources:

- https://github.com/Qovery/react-xtermjs
- https://github.com/robert-harbison/xterm-for-react
- https://github.com/PabloLION/xterm-react

---

## 9. Recommendations

### 9.1 Architecture Recommendation

Adopt the **ttyd-inspired lightweight WebSocket server pattern**, adapted for Node.js:

```
+--------------------------------------------------+
|  Browser (Docusaurus / ChatKit Side Panel)        |
|  +--------------------------------------------+  |
|  |  React Component                           |  |
|  |  +--------------------------------------+  |  |
|  |  |  xterm.js + FitAddon + AttachAddon   |  |  |
|  |  +--------------------------------------+  |  |
|  +--------------------------------------------+  |
+--------------------------------------------------+
                        |
                   WSS (TLS)
                   + JWT token auth
                   + Origin validation
                        |
+--------------------------------------------------+
|  Local WebSocket Server (Node.js)                 |
|  +--------------------------------------------+  |
|  |  ws library (lightweight WebSocket)        |  |
|  |  - Origin whitelist                        |  |
|  |  - JWT verify on upgrade                   |  |
|  |  - Rate limiting                           |  |
|  +--------------------------------------------+  |
|  +--------------------------------------------+  |
|  |  Session Manager                           |  |
|  |  - node-tmux (session lifecycle)           |  |
|  |  - node-pty (pty bridge to tmux)           |  |
|  |  - Session map: sessionId -> ptyProcess    |  |
|  +--------------------------------------------+  |
+--------------------------------------------------+
                        |
                   tmux sessions
                        |
+--------------------------------------------------+
|  tmux                                             |
|  - Session: student-{userId}                      |
|  - Survives WebSocket disconnect                  |
|  - Reconnectable                                  |
+--------------------------------------------------+
```

### 9.2 Technology Choices

| Component          | Choice                       | Rationale                                      |
| ------------------ | ---------------------------- | ---------------------------------------------- |
| Terminal emulator  | `@xterm/xterm`               | Industry standard, VS Code uses it             |
| WebSocket addon    | `@xterm/addon-attach`        | Official, maintained by xterm.js team          |
| Resize addon       | `@xterm/addon-fit`           | Responsive terminal sizing                     |
| React wrapper      | Direct xterm.js (no wrapper) | Simpler, fewer dependencies, more control      |
| WebSocket server   | `ws` (npm)                   | Lightweight, no Socket.IO overhead             |
| PTY library        | `node-pty`                   | Battle-tested, cross-platform, VS Code uses it |
| Session management | `node-tmux`                  | Simple API for tmux lifecycle                  |
| Auth               | JWT (short-lived, scoped)    | Prevents CSWSH, no cookie issues               |

### 9.3 ChatKit Integration Strategy

Since ChatKit does NOT support custom React components inside widgets:

**Pattern: Side Panel with Effect-Driven Control**

1. ChatKit widget displays a "Open Terminal" button
2. Button triggers a server action
3. Server responds with a client effect: `{ type: "open_terminal", sessionId: "..." }`
4. React `onEffect` handler opens the terminal side panel
5. Terminal component connects to WebSocket server with the session ID
6. ChatKit can send commands to the terminal via additional effects

This mirrors the Metro Map and Customer Support patterns in the ChatKit advanced samples.

### 9.4 What NOT to Build

- **Do NOT embed xterm.js inside a ChatKit widget** -- it is not supported
- **Do NOT use Socket.IO** -- raw `ws` is sufficient and lower overhead
- **Do NOT use cookie-based auth** for WebSocket -- use JWT tokens
- **Do NOT skip origin validation** -- this is the #1 WebSocket vulnerability
- **Do NOT run node-pty as root** -- use an unprivileged user
- **Do NOT build session persistence from scratch** -- use tmux

### 9.5 Implementation Priority

1. **Phase 1: WebSocket Server + xterm.js** -- Basic terminal in browser connected to local shell via node-pty
2. **Phase 2: tmux Integration** -- Session persistence, reconnection support
3. **Phase 3: Security Hardening** -- JWT auth, origin validation, rate limiting
4. **Phase 4: ChatKit Integration** -- Side panel pattern with effect-driven control
5. **Phase 5: Docker Isolation** (optional) -- Container-based sandboxing for multi-tenant

### 9.6 Key Risks

| Risk                                        | Mitigation                                                   |
| ------------------------------------------- | ------------------------------------------------------------ |
| node-pty build failures on student machines | Provide prebuilt binaries or use get-pty-output (Rust/N-API) |
| WebSocket hijacking from malicious sites    | Strict origin validation + JWT auth                          |
| Shell escape / privilege escalation         | Non-root user, optional container isolation                  |
| ChatKit widget limitations                  | Side panel pattern (proven in advanced samples)              |
| tmux not installed on all platforms         | Detect tmux availability, fall back to raw node-pty sessions |
| xterm.js performance with large output      | WebGL2 renderer addon, flow control                          |

---

## Appendix: Source Repository Links

| Project                  | URL                                                       | Stars | Language          |
| ------------------------ | --------------------------------------------------------- | ----- | ----------------- |
| xterm.js                 | https://github.com/xtermjs/xterm.js                       | 18k+  | TypeScript        |
| node-pty                 | https://github.com/microsoft/node-pty                     | 3k+   | C++/TypeScript    |
| ttyd                     | https://github.com/tsl0922/ttyd                           | 8k+   | C                 |
| WeTTY                    | https://github.com/butlerx/wetty                          | 4k+   | TypeScript        |
| node-tmux                | https://github.com/StarlaneStudios/node-tmux              | <100  | TypeScript        |
| WebMux                   | https://github.com/nooesc/webmux                          | <100  | Rust/Vue          |
| WebTMUX                  | https://github.com/nonoxz/webtmux                         | <100  | JavaScript        |
| pyxtermjs                | https://github.com/cs01/pyxtermjs                         | 2k+   | Python            |
| xterm-web-ide            | https://github.com/gitpod-io/xterm-web-ide                | <100  | TypeScript        |
| react-xtermjs            | https://github.com/Qovery/react-xtermjs                   | <100  | TypeScript        |
| ChatKit JS               | https://github.com/openai/chatkit-js                      | 1k+   | TypeScript        |
| ChatKit Python           | https://github.com/openai/chatkit-python                  | 500+  | Python            |
| ChatKit Advanced Samples | https://github.com/openai/openai-chatkit-advanced-samples | 200+  | TypeScript/Python |
