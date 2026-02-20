# Distribution Strategy: Practice Server to 20k Users

**Date**: 2026-02-13
**Context**: practice-server v0.1 works locally. How do we ship it to 20k non-tech learners?

## Prerequisite Assumption

Students must have Claude Code CLI installed locally before reaching exercise lessons (Chapter 3+). This gives us:
- Node.js 18+ already installed
- npm/npx already available
- Anthropic API auth already configured
- Terminal familiarity already established

**The distribution problem reduces to: how do users start one more process?**

## Options Evaluated

### Option A: npx One-Liner (Recommended for Launch)

```bash
npx @agentfactory/practice-server
```

**How it works:**
1. Publish practice-server as `@agentfactory/practice-server` on npm
2. npm `optionalDependencies` pattern handles platform-specific node-pty prebuilt binaries
3. npx downloads, caches, and runs — subsequent starts are instant
4. Learn-app auto-detects via health polling when server starts

**Pros:**
- Familiar to Node.js users (they installed Claude Code with npm)
- npm handles platform-specific native binary distribution (well-tested pattern — VS Code, Cursor use it)
- Automatic versioning and updates
- CDN distribution via npm registry
- Caching built in

**Cons:**
- Still needs Node.js at runtime (but students have it)
- node-pty prebuilt binaries need to be built for each platform
- npx first-run can be slow (~10s download)

**Platform matrix (pre-built node-pty binaries):**
| Platform | Binary | Priority |
|----------|--------|----------|
| macOS arm64 | `@agentfactory/practice-server-darwin-arm64` | Tier 1 |
| macOS x64 | `@agentfactory/practice-server-darwin-x64` | Tier 1 |
| Linux x64 | `@agentfactory/practice-server-linux-x64` | Tier 1 |
| Windows x64 | WSL documentation | Tier 2 |

**Effort:** 1-2 days (package.json, prebuildify for node-pty, npm publish workflow)

### Option B1: Node Bundle + Prebuilt .node File

```bash
# Download once
curl -fsSL https://agentfactory.dev/install-practice | sh
# Run
af-practice
```

**How it works:**
- esbuild bundles all TypeScript into single `practice-server.mjs`
- Ship alongside pre-compiled node-pty `.node` file per platform
- Install script downloads correct binary for OS/arch
- User runs with their system Node.js: `node practice-server.mjs`

**Pros:**
- Slightly faster startup (no npm resolution)
- Can be placed in PATH for easy access

**Cons:**
- We own the platform binary matrix (not npm)
- Need to rebuild `.node` for each Node.js major version
- Install script needs maintenance
- No automatic updates

**Effort:** 3-4 days

### Option B2: Go Rewrite (True Standalone Binary)

```bash
# Download once
curl -fsSL https://agentfactory.dev/install-practice | sh
# Run
af-practice
```

**How it works:**
- Rewrite practice-server in Go (~400 lines)
- `creack/pty` for native PTY (no node-pty addon)
- `gorilla/websocket` for WebSocket
- Cross-compile: `GOOS=darwin GOARCH=arm64 go build`
- Single binary, ~10MB, zero runtime dependencies

**Pros:**
- Truly zero dependencies (no Node.js needed at runtime)
- Go cross-compilation is a solved problem
- Trivial maintenance once built
- Fastest startup
- Could add to Homebrew: `brew install af-practice`

**Cons:**
- Requires rewriting practice-server in Go (3-5 days)
- Two codebases to maintain during transition
- Team needs Go knowledge for maintenance

**Effort:** 3-5 days (rewrite) + ongoing Go maintenance

### Option C: Docker Container

```bash
docker run -p 3100:3100 -v ~/.claude:/root/.claude ghcr.io/panaversity/practice-server
```

**Pros:** Everything pre-installed, no native compilation
**Cons:** Docker is a heavy dependency for non-tech users, Claude Code auth needs volume mount, overhead
**Verdict:** Not suitable as primary distribution. Too much friction.

### Option D: Cloud-Hosted Terminals

**How it works:** practice-server runs in cloud, WebSocket proxied to browser
**Pros:** Zero local install
**Cons:** Each user needs Claude Code auth, server costs scale linearly, latency, security complexity
**Verdict:** Not viable for 20k users without significant infrastructure investment.

### Option E: Gitpod / GitHub Codespaces

```json
// .devcontainer/devcontainer.json
{
  "image": "mcr.microsoft.com/devcontainers/javascript-node:20",
  "postCreateCommand": "npm i -g @anthropic-ai/claude-code",
  "forwardPorts": [3100]
}
```

**How it works:**
- Exercise repos get `.devcontainer/devcontainer.json`
- "Open in Codespaces" button on exercise lessons
- Cloud IDE with Claude Code pre-installed

**Pros:**
- Works on any device with a browser
- No local installation at all

**Cons:**
- **Breaks seamless experience** — student leaves learn-app
- Can't embed Codespace terminal in our app (cross-origin restriction)
- User must re-authenticate Claude Code in cloud
- Limited free hours (Codespaces: 60 hrs/month, Gitpod: 50 hrs/month)
- Separate browser tab, no lesson side-by-side

**Verdict:** Useful as **fallback** for students who can't install locally, not as primary path.

## Recommendation

```
Primary:   Option A (npx)     — ships in 1-2 days, npm handles complexity
Fallback:  Option E (Codespaces) — for Chromebooks, corporate laptops
Future:    Option B2 (Go)     — when volume justifies it, or Windows demand appears
```

### Phase 1: npx (Now)

1. Create `@agentfactory/practice-server` npm package
2. Use prebuildify for node-pty binaries (macOS arm64/x64, Linux x64)
3. Setup card in learn-app shows `npx @agentfactory/practice-server`
4. Auto-detect when server starts (existing health polling)

### Phase 2: Go Binary (When Needed)

Trigger: >100 npm install failure reports, Windows demand, or Homebrew request.

The Go rewrite is ~400 lines:
- `net/http` for Express equivalent
- `gorilla/websocket` for WebSocket
- `creack/pty` for PTY (replaces node-pty)
- `os/exec` for Claude Code spawn
- `archive/zip` for exercise extraction

### Fallback: Codespaces (Always Available)

- Add `.devcontainer` to exercise repos
- Small "Can't install? Use cloud" link in setup card
- Degraded UX accepted for this path

## UX Flow for Students

```
1. Student reaches Chapter 3 exercise lesson
2. Clicks "Start" on Exercise 1.1
3. First time:
   ┌─────────────────────────────────────────┐
   │  Practice Server Required               │
   │                                         │
   │  Run this in any terminal:              │
   │  ┌───────────────────────────────────┐  │
   │  │ npx @agentfactory/practice-server │  │  ← click to copy
   │  └───────────────────────────────────┘  │
   │                                         │
   │  ● Waiting for server...               │
   │                                         │
   │  Can't install locally?                 │
   │  → Open in GitHub Codespaces            │
   └─────────────────────────────────────────┘
4. Student runs command → server starts on :3100
5. Setup card auto-disappears → terminal appears
6. Claude Code starts in exercise directory, reads INSTRUCTIONS.md
7. Student practices on right, reads lesson on left
```

Subsequent visits: `npx` starts instantly from cache.
