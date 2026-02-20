# Browser-to-Local Process Bridging: Architecture Research

Research into how Vercel, StackBlitz, Replit, and the broader ecosystem approach the problem of connecting browser UIs to local execution environments.

**Date**: 2026-02-12
**Purpose**: Inform architecture decisions for embedding a terminal in a Docusaurus site that connects to a local tmux session running Claude Code.

---

## Table of Contents

1. [Vercel's v0 and Sandbox Architecture](#1-vercels-v0-and-sandbox-architecture)
2. [Turbopack / HMR WebSocket Patterns](#2-turbopack--hmr-websocket-patterns)
3. [Next.js / Docusaurus WebSocket Server Patterns](#3-nextjs--docusaurus-websocket-server-patterns)
4. [StackBlitz WebContainers](#4-stackblitz-webcontainers)
5. [Replit's Architecture](#5-replits-architecture)
6. [Local-First Development Tool Patterns](#6-local-first-development-tool-patterns)
7. [The Companion App Pattern](#7-the-companion-app-pattern)
8. [Terminal-in-Browser: xterm.js + tmux](#8-terminal-in-browser-xtermjs--tmux)
9. [Chrome Private Network Access (PNA)](#9-chrome-private-network-access-pna)
10. [Vercel-Quality Engineering Approach](#10-vercel-quality-engineering-approach)
11. [Recommended Approach](#11-recommended-approach)

---

## 1. Vercel's v0 and Sandbox Architecture

### How v0.dev Works

v0 is Vercel's AI code generation platform. Its architecture demonstrates how to bridge a browser UI to code execution environments.

**Code Generation Pipeline:**

- User describes UI in natural language via chat
- LLM generates React + Tailwind CSS code (currently using Anthropic Sonnet models)
- A custom `vercel-autofixer-01` model runs mid-stream, catching errors as output is generated
- Post-generation linter pass catches style inconsistencies
- Generated code uses shadcn/ui components

**Execution Environment:**

- v0 uses **Vercel Sandbox** -- lightweight Firecracker microVMs (NOT Docker, NOT WebContainers)
- Each sandbox is an isolated Linux VM with its own filesystem, network, and process space
- Powered by "Hive", Vercel's internal compute platform
- Sandbox spins up, runs code, and disappears -- often in seconds
- Supports Node.js 22 and Python 3.13 by default

**Browser-to-Sandbox Connection:**

- The sandbox-based runtime mirrors how apps actually run on Vercel infrastructure
- Code preview renders directly in the browser within the chat interface
- Git integration: each chat creates a branch, can open PRs, deploy on merge
- Can import any GitHub repo and automatically pull environment variables from Vercel

**Key Insight**: v0 runs code in remote cloud VMs, not locally. The browser connects to Vercel's infrastructure. This is the opposite of our use case (we need local), but the UX patterns (inline preview, seamless connection) are instructive.

### Vercel Hive Infrastructure (Deep Dive)

Hive is Vercel's low-level compute platform:

- **Firecracker microVMs** called "cells" provide isolation
- **Box Daemon**: runs on each physical host, provisions block devices, spawns Firecracker processes, manages communication via dedicated socket connections
- **Cell Daemon**: runs inside each cell, maintains communication with box daemon, controls build containers
- **Control Plane**: orchestrates cell allocation and lifecycle

Communication between box daemon and cell daemon uses a dedicated socket connection -- similar to how we'd need a WebSocket between browser and local process.

**Sources:**

- [Vercel blog: Deep dive into Hive](https://vercel.com/blog/a-deep-dive-into-hive-vercels-builds-infrastructure)
- [Vercel Sandbox docs](https://vercel.com/docs/vercel-sandbox)
- [Vercel Sandbox GA announcement](https://vercel.com/blog/vercel-sandbox-is-now-generally-available)
- [v0 docs](https://v0.app/docs)
- [v0 composite model family](https://vercel.com/blog/v0-composite-model-family)

---

## 2. Turbopack / HMR WebSocket Patterns

### How Turbopack Hot Reload Works

Turbopack is Vercel's Rust-based bundler that powers Next.js development. Its HMR (Hot Module Replacement) system demonstrates mature WebSocket patterns.

**Architecture:**

- Dev server listens on a port (typically 3000)
- Browser tab opens a WebSocket connection to `ws://localhost:3000/_next/webpack-hmr`
- Turbopack's incremental compilation engine (built on Turbo, a memoization framework in Rust) detects file changes
- Only changed modules are recomputed -- results cached per-function
- Updates pushed to browser via WebSocket in milliseconds regardless of codebase size

**WebSocket Connection Management:**

- Browser maintains persistent WebSocket subscription to dev server
- Open tabs with HMR subscriptions can prevent dev server from exiting cleanly (they had to add explicit connection termination in PR #75344)
- Connection is bidirectional but primarily server-to-client (push updates)

**Patterns We Can Adapt:**

1. **WebSocket endpoint on dev server**: Turbopack uses `/_next/webpack-hmr` path. We could use a similar namespaced path like `/_terminal/ws`
2. **Automatic reconnection**: HMR connections handle disconnects and reconnects gracefully
3. **Heartbeat/ping**: Keeps connections alive, detects disconnects early
4. **Namespaced WebSocket paths**: Avoids conflicts with other WebSocket consumers

**Sources:**

- [Turbopack vision blog](https://vercel.com/blog/the-turbopack-vision)
- [Turbopack Dev stable announcement](https://nextjs.org/blog/turbopack-for-development-stable)
- [HMR WebSocket termination PR](https://github.com/vercel/next.js/pull/75344)

---

## 3. Next.js / Docusaurus WebSocket Server Patterns

### Next.js WebSocket Approaches

Next.js does not natively support WebSocket in API routes. Several patterns exist:

**Pattern 1: HTTP Upgrade in API Routes**

```javascript
// pages/api/socket.js
import { WebSocketServer } from "ws";

export default function handler(req, res) {
  if (!res.socket.server.wss) {
    const wss = new WebSocketServer({ noServer: true });
    res.socket.server.wss = wss;

    res.socket.server.on("upgrade", (request, socket, head) => {
      wss.handleUpgrade(request, socket, head, (ws) => {
        wss.emit("connection", ws, request);
      });
    });
  }
  res.end();
}
```

**Pattern 2: Custom Server (Recommended for our use case)**
Run a separate WebSocket server alongside the main dev server. Works with both App Router and Pages Router.

**Pattern 3: next-ws Package**
Adds WebSocket support to App Router routes. Not suitable for serverless (Vercel), but works for local dev servers -- similar to our use case.

### Docusaurus WebSocket Integration

Docusaurus is a static site generator. It does NOT have native WebSocket support. Options:

**Option A: Separate WebSocket Server (Simplest)**

- Run a separate Node.js WebSocket server process alongside Docusaurus
- Client-side React component connects to `ws://localhost:PORT`
- Production: reverse proxy (Nginx/Caddy) handles WebSocket upgrades

**Option B: Docusaurus Plugin with devServer Config**

```javascript
// docusaurus-plugin-terminal/index.js
module.exports = function (context, options) {
  return {
    name: "docusaurus-plugin-terminal",
    configureWebpack(config, isServer, utils) {
      return {
        devServer: {
          proxy: {
            "/_terminal/ws": {
              target: "ws://localhost:7681",
              ws: true,
              changeOrigin: true,
            },
          },
        },
      };
    },
  };
};
```

**Option C: docusaurus-plugin-devserver-proxy**
An existing npm package specifically for adding devServer proxy support in Docusaurus, including WebSocket proxying.

**Key Finding**: Docusaurus's `configureWebpack` hook can return a `devServer` field that includes proxy configuration with `ws: true` for WebSocket support. This means we can proxy WebSocket connections through the Docusaurus dev server to a separate terminal server process.

**Sources:**

- [Docusaurus Lifecycle APIs](https://docusaurus.io/docs/api/plugin-methods/lifecycle-apis)
- [Next.js WebSocket discussion](https://github.com/vercel/next.js/discussions/58698)
- [next-ws package](https://github.com/apteryxxyz/next-ws)
- [docusaurus-plugin-devserver-proxy](https://www.npmjs.com/package/docusaurus-plugin-devserver-proxy)
- [WebSocket in Next.js on Fly.io](https://fly.io/javascript-journal/websockets-with-nextjs/)

---

## 4. StackBlitz WebContainers

### How WebContainers Work

WebContainers run Node.js entirely in the browser using WebAssembly.

**Technical Architecture:**

- WebAssembly-based micro-operating system running in a browser tab
- Boots with an ephemeral virtual file system stored in memory
- Virtualized TCP network stack mapped to the browser's ServiceWorker API
- Runs entirely locally -- works even offline
- Each project gets its own domain and installs a Service Worker
- Can run npm, pnpm, yarn natively in the browser (up to 10x faster than local)
- WASI support enables Python, WordPress tools, jq, and other traditionally native tools

**Terminal Integration (jsh shell):**

```javascript
const shellProcess = await webcontainerInstance.spawn("jsh", {
  terminal: { cols: 80, rows: 24 },
});
// Pipe output to xterm.js terminal
shellProcess.output.pipeTo(
  new WritableStream({
    write(data) {
      terminal.write(data);
    },
  }),
);
// Pipe input from xterm.js to jsh
const input = shellProcess.input.getWriter();
terminal.onData((data) => {
  input.write(data);
});
```

### What Can and Cannot Run in WebContainers

**Can Run:**

- Node.js (JavaScript, TypeScript)
- Package managers (npm, pnpm, yarn)
- Python (via WASI)
- Dev servers (Vite, webpack, Next.js)
- Any pure JS/TS tooling

**Cannot Run:**

- Native addons (C/C++ compiled to native code) unless compiled to WASM
- Custom Service Workers (WebContainers use Service Workers internally)
- Tools requiring raw filesystem access outside the virtual FS
- Docker or other container runtimes
- **Claude Code** -- requires native process spawning, filesystem access, network access to Anthropic API, and runs as a CLI tool with tmux integration. None of these are possible in a WebContainer.

### Relevance to Our Use Case

**WebContainers are NOT suitable for running Claude Code** because:

1. Claude Code is a CLI tool that needs real OS-level process management
2. It needs to spawn tmux sessions, interact with git, read/write real files
3. It needs network access to Anthropic's API
4. It requires native Node.js addons and system-level access

However, WebContainers demonstrate that **xterm.js + process I/O piping** is the proven pattern for browser-based terminals. We just need the process to run locally instead of in WASM.

**Sources:**

- [WebContainers introduction](https://blog.stackblitz.com/posts/introducing-webcontainers/)
- [WebContainers API reference](https://webcontainers.io/api)
- [Connect a terminal tutorial](https://webcontainers.io/tutorial/6-connect-a-terminal)
- [WebContainers troubleshooting](https://webcontainers.io/guides/troubleshooting)
- [WebContainers browser support](https://developer.stackblitz.com/platform/webcontainers/browser-support)

---

## 5. Replit's Architecture

### IDE Architecture

Replit's browser IDE demonstrates a mature approach to browser-to-execution-environment communication.

**Frontend Architecture:**

- ~3000 lines core code that functions as a window manager and event middleman
- Everything is a plugin -- terminal, editor, file tree, console are all plugins
- Plugins expose render targets or internal state management
- No direct dependencies between plugins -- they communicate through the Redux store
- Layout is a Redux state, changeable at runtime
- Server-rendered for fast initial load even on slow connections

**Key Design Decision**: The terminal is "just another plugin" that can be swapped, configured, or replaced. This is the right abstraction for our case too.

### Connection Architecture (Crosis + Eval)

Replit's browser-to-container communication is the most relevant architecture for our use case:

**Components:**

1. **Client (Browser)**: Uses Crosis, a JavaScript client that speaks Replit's container protocol
2. **Eval**: A reverse WebSocket proxy sitting between client and container VMs
3. **Conman**: Container manager that runs all Repls in Linux containers
4. **Lore**: Metadata service that tells clients where to connect

**Connection Flow:**

1. Browser sends request to repl-it-web to ask which cluster to connect to
2. Server consults Lore for metadata, responds with Eval URL + auth token
3. Client opens WebSocket to Eval's WebSocket endpoint
4. Eval upgrades connection, establishes WebSocket to remote Conman VM
5. Eval copies data bidirectionally between client and Repl container
6. Data flows: Browser <-> WebSocket <-> Eval Proxy <-> WebSocket <-> Conman VM

**Crosis Channel Protocol:**

- Central concept is a "channel" -- send commands and receive responses
- Client manages connection lifecycle (disconnects, reconnects)
- Fallback from WebSocket to long polling after 3 failed connection attempts
- Uses `@replit/protocol` package as peer dependency for message serialization

**Reliability Patterns:**

- Eval (proxy) has smaller surface than Conman, so it's more stable
- Conman rollouts only disconnect the target VM, not the proxy
- Eval retries connections to Conman on failure
- Clear observability: logs show exactly which part of the connection setup failed

**What We Can Steal:**

- The channel abstraction (terminal I/O as a channel)
- Separation of proxy from actual process management
- WebSocket with long-polling fallback
- Automatic reconnection with exponential backoff
- Clear error taxonomy (auth failed vs connection failed vs process failed)

**Sources:**

- [Replit: More Reliable Connections (Eval blog)](https://blog.replit.com/eval)
- [Replit: Modular, fast, small IDE](https://blog.replit.com/ide)
- [Crosis GitHub](https://github.com/replit/crosis)
- [Replit Cloud IDE](https://datasciencedojo.com/blog/replit-cloud-ide/)

---

## 6. Local-First Development Tool Patterns

### Docker Desktop: Browser UI to Local Daemon

Docker Desktop runs a local daemon that the Docker Desktop UI (built with Electron, but the pattern applies) communicates with. The daemon exposes a local socket/API that the UI connects to.

**Pattern**: Local daemon process + API/socket communication + UI client

### Tailscale Funnel / Serve

Tailscale demonstrates two relevant patterns:

**Tailscale Serve** (local access):

- Exposes a local service to other devices on your Tailscale network
- Acts as a reverse proxy from your Tailscale hostname to a local port
- Handles TLS termination

**Tailscale Funnel** (internet access):

- Routes traffic from the wider internet to a local service
- Georeplicated ingress servers accept TCP connections
- Looks at TLS ClientHello SNI, proxies encrypted connections to your machine
- Simple command: `tailscale funnel 3000`

**Relevance**: If we ever need remote access to the local terminal (pair programming, instructor viewing student terminal), Tailscale Funnel is the gold standard. For local-only, it's overkill.

### ngrok / localtunnel

**How ngrok works:**

1. Local client opens outbound connection to ngrok cloud
2. ngrok assigns a public URL (e.g., `abc123.ngrok.io`)
3. External requests to that URL are forwarded through the tunnel to local machine
4. Fundamental insight: "if servers can't connect to you, make your machine connect to them first"

**Relevance**: NOT needed for our use case (browser and terminal are on the same machine), but the connection-reversal pattern is useful if we ever need remote access.

**Sources:**

- [Tailscale Funnel introduction](https://tailscale.com/blog/introducing-tailscale-funnel)
- [Tailscale Serve and Funnel](https://tailscale.com/blog/reintroducing-serve-funnel)
- [ngrok guide](https://www.sitepoint.com/use-ngrok-test-local-site/)

---

## 7. The Companion App Pattern

### Pattern Overview

Several products solve the browser-to-local communication problem by installing a small "companion" process on the user's machine that the browser communicates with.

### Figma Local Font Helper

**Architecture:**

- Small daemon process (FigmaAgent) installed on user's machine
- Runs an HTTP + HTTPS server on **localhost**
- Responds with a list of locally installed fonts when queried
- Only accepts connections from figma.com (origin checking)
- NOT exposed to public internet
- Chrome 142+ requires user permission prompt for local network access

**Communication**: Simple HTTP request/response. Browser makes fetch to `http://localhost:PORT/fonts`, gets JSON back.

### 1Password Browser Extension

**Architecture:**

- Browser extension communicates with desktop app via **Chrome Native Messaging API**
- Native messaging uses stdin/stdout pipes (no network)
- App verifies browser's code signature before accepting connection
- Encryption keys and vault data shared over this channel

**Communication**: Chrome Native Messaging (stdio pipes). Most secure option, but requires a browser extension.

### Raycast

**Architecture:**

- Raycast is a native macOS app
- Extensions run in a child Node.js process
- Communication between Raycast and extensions via **stdio + RPC protocol**
- Browser Extension API provides deeper browser integration
- Can check if desktop app is installed, deep-link into it

**Communication**: IPC via file handles + thin RPC protocol.

### ToDesktop Communication Server

**Architecture:**

- npm package: `@todesktop/client-comm-server`
- Desktop app runs a local server on specific ports (20001, 39214)
- Web app checks if comm server is running: `checkIfCommServerRunning()`
- Can broadcast messages: `broadcast(message)`
- Can listen for messages from desktop app

**Communication**: HTTP/WebSocket on localhost ports. This is the closest pattern to what we need.

### Key Patterns Across All Companion Apps

| Product           | Transport                | Auth                 | Install Method        |
| ----------------- | ------------------------ | -------------------- | --------------------- |
| Figma Font Helper | HTTP on localhost        | Origin checking      | Installer download    |
| 1Password         | Native Messaging (stdio) | Code signing         | App Store / installer |
| Raycast           | IPC via file handles     | N/A (same machine)   | Homebrew / download   |
| ToDesktop         | HTTP on localhost ports  | N/A (localhost only) | npm package           |

**Best Pattern for Our Use Case**: **HTTP/WebSocket on localhost** (ToDesktop-style), because:

- No browser extension required
- Works in any browser
- npm-installable
- Can check if server is running from client-side code
- WebSocket enables bidirectional streaming (needed for terminal I/O)

**Sources:**

- [Figma local network access](https://help.figma.com/hc/en-us/articles/34458998159511-Local-network-access-in-Figma)
- [1Password browser connection security](https://support.1password.com/1password-browser-connection-security/)
- [Raycast API docs](https://developers.raycast.com)
- [ToDesktop comm server](https://www.npmjs.com/package/@todesktop/client-comm-server)
- [Figma-Linux font helper](https://github.com/Figma-Linux/figma-linux-font-helper)

---

## 8. Terminal-in-Browser: xterm.js + tmux

### The Proven Stack

The browser terminal ecosystem has converged on a standard architecture:

**Frontend**: xterm.js

- Full terminal emulator in the browser (TypeScript)
- Supports bash, vim, tmux, curses-based apps, mouse events
- WebGL2 renderer for performance
- CJK/IME input support
- @xterm/addon-attach for WebSocket connection
- @xterm/addon-fit for auto-sizing

**Backend Bridge (Option A): node-pty + WebSocket server**

```
Browser (xterm.js) <--WebSocket--> Node.js Server <--node-pty--> Shell/tmux
```

- node-pty spawns a pseudo-terminal (PTY)
- Server relays I/O between WebSocket and PTY
- Can attach to existing tmux sessions: `tmux attach -t session-name`

**Backend Bridge (Option B): ttyd**

- Written in C, uses libwebsockets + libuv
- Single binary, installable via Homebrew
- Runs on port 7681 by default
- Direct tmux integration: `ttyd tmux new -A -s session-name`
- Supports SSL/TLS, basic auth, readonly mode
- Max client limits, origin checking
- Install: `brew install ttyd` or pre-built binaries

**Backend Bridge (Option C): WebTMUX**

- Express + Socket.io + xterm.js
- Specifically designed for tmux session interaction via browser
- Uses tmux for session management
- Full terminal emulation

### ttyd is the Most Relevant Tool

ttyd solves almost exactly our problem:

```bash
# Start a web terminal connected to a tmux session
ttyd tmux new -A -s claude-code
# Now browse to http://localhost:7681 for a terminal
```

**Architecture of ttyd:**

- C binary (~56% C, ~27% TypeScript for frontend)
- libwebsockets for WebSocket server
- libuv for async I/O
- xterm.js frontend with WebGL2 rendering
- Custom WebSocket protocol streams terminal I/O
- Configurable ping interval (default 5s)
- Origin checking for security
- ZMODEM file transfer support

**What We Could Build On Top of ttyd:**

1. Start ttyd pointing at a tmux session running Claude Code
2. Embed an iframe or custom xterm.js client in Docusaurus
3. Docusaurus plugin manages the connection lifecycle
4. Fallback UI when ttyd isn't running

**Sources:**

- [ttyd GitHub](https://github.com/tsl0922/ttyd)
- [xterm.js GitHub](https://github.com/xtermjs/xterm.js)
- [WebTMUX GitHub](https://github.com/nonoxz/webtmux)
- [Browser terminal with xterm.js and node-pty](https://ashishpoudel.substack.com/p/web-terminal-with-xtermjs-node-pty)
- [Creating browser-based terminals](https://www.eddymens.com/blog/creating-a-browser-based-interactive-terminal-using-xtermjs-and-nodejs)
- [Building browser terminal with Docker and xterm.js](https://www.presidio.com/technical-blog/building-a-browser-based-terminal-using-docker-and-xtermjs/)

---

## 9. Chrome Private Network Access (PNA)

### Critical Browser Security Consideration

Chrome 142+ introduces **Local Network Access** (formerly Private Network Access), which restricts browser-to-localhost communication.

**What It Does:**

- Websites must explicitly request permission to access local network resources
- CORS preflight requests carry `Access-Control-Request-Private-Network: true`
- Server must respond with `Access-Control-Allow-Private-Network: true`
- User gets a permission prompt in the browser

**Impact on Our Architecture:**

- A Docusaurus site served from `localhost:3000` connecting to a WebSocket on `localhost:7681` may trigger PNA checks
- If both are on localhost, this is a "private-to-private" request (less restricted)
- If the Docusaurus site is served from a public URL, connecting to localhost WILL require PNA headers

**Mitigation Strategies:**

1. **Same-origin proxy**: Proxy WebSocket through Docusaurus dev server (same origin = no PNA issue)
2. **PNA headers**: Add `Access-Control-Allow-Private-Network: true` to WebSocket server responses
3. **localhost-only**: If both services are on localhost, restrictions are minimal

**Sources:**

- [Chrome local network access prompt](https://developer.chrome.com/blog/local-network-access)
- [PNA preflight blog](https://developer.chrome.com/blog/private-network-access-preflight)
- [PNA permission prompt end](https://developer.chrome.com/blog/pna-permission-prompt-ot-end)

---

## 10. Vercel-Quality Engineering Approach

### How a Vercel-quality team would architect this

Given the problem: "Embed a terminal in a Docusaurus site that connects to a local tmux session running Claude Code", here's what world-class engineering looks like:

### Package Architecture (Turborepo Monorepo)

```
@agentfactory/terminal/
  packages/
    terminal-server/        # Node.js server: WebSocket <-> tmux bridge
      src/
        index.ts           # Entry point, starts server
        tmux.ts            # tmux session management
        ws-server.ts       # WebSocket server with reconnection
        health.ts          # Health check endpoint
      package.json         # bin: { "af-terminal": "./dist/cli.js" }

    terminal-client/        # React component for Docusaurus
      src/
        TerminalEmbed.tsx  # xterm.js + WebSocket client
        StatusBar.tsx      # Connection status, session info
        hooks/
          useTerminal.ts   # WebSocket lifecycle management
          useReconnect.ts  # Exponential backoff reconnection
      package.json

    docusaurus-plugin/      # Docusaurus integration
      src/
        index.ts           # Plugin: devServer proxy + theme
        theme/
          Terminal.tsx      # MDX component
      package.json

    shared/                 # Shared types and protocol
      src/
        protocol.ts        # Message types, version negotiation
        constants.ts       # Ports, paths, timeouts
      package.json

  turbo.json
  package.json
```

### Install Experience

**Tier 1: npx (Zero-install trial)**

```bash
# Student runs this ONCE to start the terminal server
npx @agentfactory/terminal-server start

# Starts WebSocket server on localhost:7681
# Attaches to or creates tmux session 'claude-code'
# Prints: "Terminal server running. Open your lesson to connect."
```

**Tier 2: Global install (Regular users)**

```bash
npm install -g @agentfactory/terminal-server
af-terminal start
```

**Tier 3: Homebrew (Power users, includes ttyd)**

```bash
brew tap agentfactory/tools
brew install af-terminal
af-terminal start
```

### Upgrade and Versioning Strategy

**Protocol Versioning:**

- WebSocket handshake includes protocol version in URL: `ws://localhost:7681/v1/terminal`
- Server and client negotiate compatible version
- Client shows "update available" banner when server is outdated
- Semver for npm packages, protocol version is separate

**Upgrade Flow:**

```
1. Client connects, sends { type: 'hello', protocolVersion: 2 }
2. Server responds { type: 'hello', protocolVersion: 2, serverVersion: '1.3.0' }
3. If protocolVersion mismatch: client shows "Please update: npm update -g @agentfactory/terminal-server"
4. If compatible: proceed with session attachment
```

### Error Handling and Fallback UX

**Connection States:**

```
DISCONNECTED  -> Attempting connection...
CONNECTING    -> Spinner + "Connecting to terminal server..."
CONNECTED     -> Terminal visible, status bar green
RECONNECTING  -> Terminal grayed out, "Reconnecting..." overlay
FAILED        -> Setup instructions shown inline
NO_SERVER     -> "Terminal server not detected. Run: npx @agentfactory/terminal-server start"
NO_TMUX       -> "No tmux session found. Run: claude in your terminal first"
```

**Fallback UX (No server running):**

```
+-----------------------------------------------+
|  Terminal Server Not Detected                  |
|                                                |
|  To use the practice terminal, run:            |
|                                                |
|  $ npx @agentfactory/terminal-server start     |
|                                                |
|  Then refresh this page.                       |
|                                                |
|  [Copy Command]  [Setup Guide]                 |
+-----------------------------------------------+
```

**Key UX Principles:**

- NEVER show a blank terminal or cryptic error
- ALWAYS show the exact command to fix the situation
- Auto-detect and reconnect -- user should never need to manually reconnect
- Show connection status persistently but unobtrusively

### Testing Strategy

**Unit Tests:**

- Protocol message serialization/deserialization
- Reconnection logic with mocked WebSocket
- tmux session detection and creation
- Health check endpoint

**Integration Tests:**

- Start server, connect client, send input, verify output
- Disconnect server, verify client reconnects
- Multiple clients connecting to same session
- Protocol version negotiation

**E2E Tests:**

- Docusaurus dev server with plugin loaded
- Terminal component renders
- Type command, see output
- Browser refresh reconnects automatically

**Chaos Tests:**

- Kill server mid-session, verify graceful degradation
- Kill tmux session, verify error message
- Rapid connect/disconnect cycles
- Simulate slow network (throttled WebSocket)

---

## 11. Recommended Approach

### Architecture Decision

After researching all major approaches, the recommended architecture is:

**A local companion server (npm package) + Docusaurus plugin with xterm.js client, connected via WebSocket on localhost.**

This combines the best patterns from:

- **Replit**: Channel-based WebSocket protocol with proxy separation
- **ttyd**: Proven terminal-to-web bridge via WebSocket + xterm.js
- **Figma/ToDesktop**: Companion process on localhost, detectable from browser
- **Turbopack**: WebSocket connection management, heartbeat, reconnection
- **Vercel Turborepo**: Monorepo package architecture

### Why NOT Other Approaches

| Approach                             | Why Not                                                        |
| ------------------------------------ | -------------------------------------------------------------- |
| **WebContainers**                    | Cannot run Claude Code (needs real OS, network, tmux)          |
| **Cloud VMs (Vercel Sandbox style)** | Overkill for local dev; adds latency and cost                  |
| **Native Messaging**                 | Requires browser extension; too heavy                          |
| **Electron wrapper**                 | Adds 200MB+ dependency; students already have a browser        |
| **iframe to ttyd**                   | No control over UX; can't integrate with lesson content        |
| **ngrok/tunnel**                     | Both services are local; tunneling adds unnecessary complexity |

### Recommended Stack

```
+------------------+     WebSocket      +------------------+     PTY/pipe      +------------------+
|                  |  ws://localhost:    |                  |                   |                  |
|  Docusaurus      |  7681/v1/terminal  |  Terminal Server  |  tmux attach -t  |  tmux session    |
|  + xterm.js      | <===============> |  (Node.js)       | <===============> |  running Claude  |
|  + plugin        |                   |  + node-pty      |                   |  Code            |
|                  |                   |  + ws             |                   |                  |
+------------------+                   +------------------+                   +------------------+
     Browser                              npm package                           User's terminal
     (port 3000)                          (port 7681)                           (tmux session)
```

### Implementation Phases

**Phase 1: Proof of Concept (1-2 days)**

- Use ttyd directly: `ttyd tmux new -A -s claude-code`
- Embed iframe in Docusaurus MDX page pointing to ttyd
- Validate the concept works end-to-end

**Phase 2: Custom Terminal Server (1 week)**

- Node.js server with node-pty + ws
- Attaches to existing tmux session (or creates one)
- Health check endpoint at `http://localhost:7681/health`
- Basic protocol versioning
- npm package with CLI entry point

**Phase 3: Docusaurus Plugin + xterm.js Client (1 week)**

- Custom React component using xterm.js
- Docusaurus plugin for devServer proxy configuration
- Connection status UI and fallback messages
- Auto-reconnection with exponential backoff

**Phase 4: Polish (1 week)**

- npx zero-install experience
- Protocol version negotiation
- Error taxonomy and helpful messages
- Testing suite
- Documentation

### Critical Design Decisions

1. **WebSocket over HTTP polling**: Terminal I/O is high-frequency, low-latency. WebSocket is the only viable transport.

2. **Separate server process over Docusaurus middleware**: Docusaurus is a static site generator. Trying to wedge a terminal server into it would be fragile. A separate process is clean, testable, and works in production too.

3. **devServer proxy for development**: During `docusaurus start`, proxy `/_terminal/ws` to the terminal server. Same-origin avoids Chrome PNA issues.

4. **node-pty over raw child_process**: node-pty provides a proper pseudo-terminal with full terminal emulation (colors, cursor positioning, vim, tmux). child_process.spawn would lose all of this.

5. **tmux session attachment over direct Claude Code spawning**: The terminal server should attach to an existing tmux session, not spawn Claude Code itself. This gives users full control over their Claude Code session and lets them use it from both the browser and their regular terminal.

6. **npm package over Homebrew**: npm is already in the student's workflow. Homebrew adds a separate package manager. npx provides zero-install trial. Homebrew can be added later as an optional convenience.

### Risk Factors

| Risk                                             | Mitigation                                                    |
| ------------------------------------------------ | ------------------------------------------------------------- |
| Chrome PNA blocks localhost WebSocket            | Use devServer proxy (same-origin)                             |
| node-pty native addon compilation fails          | Provide prebuilt binaries via node-pre-gyp                    |
| tmux session doesn't exist when connecting       | Show clear setup instructions; optionally auto-create         |
| Multiple browser tabs connecting to same session | tmux handles this natively (shared view)                      |
| WebSocket connection drops silently              | Heartbeat ping every 5s + reconnection logic                  |
| Student on Windows without tmux                  | Provide WSL instructions; or fallback to raw PTY without tmux |

---

## Appendix: Key Technical References

### Essential Libraries

- [xterm.js](https://xtermjs.org/) - Terminal emulator for the browser
- [node-pty](https://github.com/nickg/node-pty) - Fork pseudoterminals in Node.js
- [ws](https://github.com/websockets/ws) - WebSocket client and server for Node.js
- [ttyd](https://github.com/tsl0922/ttyd) - Share terminal over the web (C binary)

### Reference Implementations

- [WebTMUX](https://github.com/nonoxz/webtmux) - Browser tmux viewer (Express + Socket.io + xterm.js)
- [webmux](https://github.com/nooesc/webmux) - Web-based tmux session viewer (Rust + Vue.js)
- [Crosis](https://github.com/replit/crosis) - Replit's container protocol client (JavaScript)
- [ttyx](https://github.com/risacher/ttyx) - Terminal via Node + Express + Socket.io

### Architecture References

- [Vercel Hive deep dive](https://vercel.com/blog/a-deep-dive-into-hive-vercels-builds-infrastructure)
- [Replit Eval proxy](https://blog.replit.com/eval)
- [Replit IDE architecture](https://blog.replit.com/ide)
- [Chrome Local Network Access](https://developer.chrome.com/blog/local-network-access)
- [Turborepo monorepo patterns](https://vercel.com/blog/monorepos)
