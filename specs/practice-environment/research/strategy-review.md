# Strategy Review: 1-Click Practice Environment

**Reviewer**: reviewer agent
**Date**: 2026-02-12
**Reviewed document**: `implementation-strategy.md`
**Supporting research**: `existing-implementations.md`, `vercel-approach.md`, `requirements-finalization.md`, `cross-platform-install.md`

**Review criteria**: Does this strategy deliver a practice environment that (1) works on Windows, macOS, Linux, (2) is as simple as installing Claude Code itself (1-click / 1 command), (3) works with existing exercises, and (4) doesn't add unnecessary complexity?

---

## Verdict: STRONG STRATEGY WITH 5 CRITICAL ISSUES

The Go binary pivot is the right call. The npx assumption was dead wrong given that Claude Code ships as a standalone Bun binary. The 4-phase plan is sensible. But there are 5 issues that will bite hard if not addressed before implementation.

---

## CRITICAL ISSUES (Must Fix Before Implementation)

### ISSUE 1: "1-click" is actually 3+ clicks on first use

**The user requirement**: "1-click setup, as simple as installing Claude Code."

**What the strategy actually requires for first-time setup:**

1. Open terminal
2. Run install script (`curl | bash` or `irm | iex`)
3. Wait for download
4. Run `af-practice`
5. Switch to browser
6. Click "Practice" button

That's 5-6 steps. Claude Code itself is a single command (`curl | bash`) and then you type `claude`. The practice server adds a SECOND background process the student must manage.

**The fundamental simplicity violation**: The student must remember to start `af-practice` every time they want to practice. They will forget. They will see the "server not running" card. They will be annoyed.

**Options to fix:**

- **A: Auto-start on login (launchd/systemd/Task Scheduler)**: Install script registers `af-practice` as a user-level daemon. It's always running. Student never thinks about it. **This is what Docker Desktop does.** Downside: background process consuming resources when not practicing.
- **B: Start from the "Practice" button**: When the health check fails, the browser shows "Click to start" which opens a deep-link or browser-spawnable command that starts the server. Fragile cross-browser.
- **C: Docusaurus plugin starts it**: The learn-app dev server spawns `af-practice` as a child process when it starts. Student runs `pnpm nx serve learn-app` and gets both. Downside: coupling, crash isolation.
- **D: Accept the 2-command flow but make it friction-free**: Student runs `af-practice` in a terminal, it stays running. Auto-retry in the browser makes it feel seamless once running.

**Recommendation**: Option D for Phase 1 (simplest, works), Option A for Phase 3 (true 1-click). But the strategy MUST acknowledge this gap honestly. Right now it pretends the flow is simpler than it is.

---

### ISSUE 2: Go binary introduces a new language to a JavaScript/Python codebase

**The entire codebase is JavaScript/TypeScript (Docusaurus, Next.js, ChatKit) and Python (study-mode-api).** There is zero Go anywhere.

Introducing Go means:

- New CI/CD pipeline for building Go binaries
- New language for the team to maintain
- Can't share types/schemas between practice server and learn-app
- Contributors need Go knowledge to modify the practice server
- Go PTY libraries (creack/pty, go-winpty) are less battle-tested than node-pty for this exact use case

**The strategy's argument for Go**: "Need single binary, zero-dependency. Go cross-compiles trivially."

**Counter-argument**: The research itself noted that Claude Code ships a Bun-compiled binary. **Bun can also compile to standalone binaries.** A TypeScript/Bun practice server would:

- Stay in the existing language ecosystem
- Share types with learn-app
- Use node-pty (battle-tested, used by VS Code)
- Compile to standalone binary via `bun build --compile`
- Cross-compile via `bun build --compile --target=bun-linux-x64` etc.

**Bun standalone binary limitations** (from research): ~50-80 MB size, cross-compilation is limited. These are real drawbacks. But the Go approach has its own drawback: team maintenance burden of a foreign language.

**This is a genuine tradeoff, not a clear winner.** The strategy presents Go as obvious. It's not. The user should decide.

**What's missing from the strategy**: A fair comparison of Go vs. Bun standalone binary, considering that this team's language expertise is JS/TS/Python, not Go.

---

### ISSUE 3: Windows native support is hand-waved

The strategy upgrades Windows from "Tier 2 (WSL only)" to "Tier 1 (native via ConPTY)" but provides almost no detail on HOW.

**Specific gaps:**

1. **ConPTY in Go**: The strategy mentions `github.com/iamacarpet/go-winpty` but that library wraps the OLD winpty, not ConPTY. The Go ecosystem for ConPTY is thin. Who has actually shipped a Go binary using ConPTY? No evidence provided.

2. **Shell selection on Windows**: When the practice server spawns a PTY on Windows, what shell does it use? PowerShell? CMD? Git Bash? Claude Code on Windows requires Git Bash. Does the Go binary detect and use Git Bash automatically?

3. **Path handling**: Windows paths use backslashes. The exercise workspace `~/af-practice/<id>/` uses Unix-style `~` expansion. How does this work on Windows? `%USERPROFILE%\af-practice\<id>\`?

4. **Testing**: Phase 1 explicitly excludes Windows (`"Windows build (add in Phase 2)"`), but the strategy claims Windows is "Tier 1". You can't claim Tier 1 and defer it to Phase 2. That's Tier 2 by definition.

**Recommendation**: Either honestly say Windows is Tier 2 until Phase 3 (when it's actually built and tested), or move Windows support into Phase 1.

---

### ISSUE 4: Exercise content sync has an unresolved chicken-and-egg problem

The strategy says the Go binary fetches exercises from `http://localhost:3000/exercises/<id>/` (the learn-app dev server).

**Problem**: This means the student must have BOTH `af-practice` AND `learn-app` running simultaneously. The strategy acknowledges this for development but doesn't address:

1. **What if learn-app is served from a deployed URL** (not localhost:3000)? Students reading the book online won't have localhost:3000.

2. **What about the production case?** The book is deployed at a public URL. The practice button is visible. The student has `af-practice` running locally. But the Go binary can't fetch exercises from the public URL because... actually, why not? This should work fine with CORS. But the strategy doesn't discuss it.

3. **Offline scenarios**: Student downloads learn-app content, goes offline. Practice server can't fetch exercises. Cached copy works for previously-started exercises, but not for new ones.

**The requirements-finalization.md (Section 5.3) already made the right call: "Exercises live as static files in learn-app."** But the Go binary's dependency on fetching from learn-app's HTTP server at runtime is fragile.

**Better approach**: The Go binary should support BOTH:

- Fetch from learn-app URL (default, works for dev and production)
- Bundled exercises as fallback (ship a default set in the binary via `go:embed`)

This is not mentioned in the strategy.

---

### ISSUE 5: No WebSocket security on localhost

The strategy says: "Security model: same (localhost only, origin validation)"

But the detailed research (`existing-implementations.md` Section 5) makes a STRONG case for WebSocket security:

> "WebSockets bypass CORS entirely. Any website can open a WebSocket to localhost unless the server explicitly validates the Origin header."

The strategy mentions origin validation in passing but doesn't include it in the Phase 1 scope. Phase 1 just has `GET /` and `GET /ws`. No origin checking. No token auth.

**Why this matters even on localhost**: A malicious website could open a WebSocket to `ws://localhost:3100/ws/` and execute commands on the student's machine through their Claude Code session. This is a real attack vector (see Gitpod vulnerability in the research).

**Recommendation**: Origin validation MUST be in Phase 1, not deferred. It's ~10 lines of Go code in the WebSocket upgrade handler. There's no excuse to ship without it.

---

## NON-CRITICAL ISSUES (Should Fix, Not Blockers)

### ISSUE 6: Reconnection without scrollback is a bad UX

The strategy says:

> "There is no 'replay' of history -- the student sees the current screen, not scrollback."

This means if a student refreshes their browser tab, they lose all visible terminal history. They see only what's currently on the screen (probably Claude Code's prompt). Everything they typed, every response Claude gave -- gone from view.

This is terrible UX for a learning environment where students need to reference previous instructions.

**tmux solves this** (it maintains a scrollback buffer server-side), but tmux is deferred to Phase 2.

**Alternative for Phase 1**: The Go binary could maintain a ring buffer of the last N bytes of PTY output and replay it on WebSocket reconnect. This is how ttyd handles reconnection. ~30 lines of code.

### ISSUE 7: No consideration of learn-app production deployment

The entire strategy assumes `learn-app` runs locally via `pnpm nx serve learn-app`. But what about students who access the book at the production URL?

- The "Practice" button would appear (it's in the frontend code)
- They'd need `af-practice` running locally
- The practice server would need to know where to fetch exercises from

This requires the browser component to try multiple sources for exercises:

1. `localhost:3000` (local dev)
2. Production URL (for deployed book)

The strategy doesn't address this at all.

### ISSUE 8: `curl | bash` is a security anti-pattern

Many organizations and security-conscious users refuse to run `curl | bash`. The strategy acknowledges this is the Claude Code / Tailscale pattern, but both of those are from well-known companies with established trust.

AgentFactory is an educational project. Students may be in corporate environments with policies against piping curl to bash.

**Alternative**: Also provide direct binary download links from GitHub Releases. The install script is a convenience, not the only path.

This is mentioned implicitly (GitHub releases are referenced) but should be explicit in the distribution section as a first-class option.

### ISSUE 9: The "existing exercises" integration plan is vague

The user explicitly said "must work with EXISTING exercises." Chapter 3 has ~100 exercises.

The strategy says:

> "A conversion script transforms INSTRUCTIONS.md -> CLAUDE.md format"

But:

1. Where are these existing exercises? The strategy references "Chapter 3" but doesn't specify the actual path.
2. What does INSTRUCTIONS.md look like? We don't know if conversion is trivial or requires manual work per exercise.
3. The conversion script doesn't exist yet and isn't assigned to any phase.
4. Phase 2 says "Convert 5-10 Chapter 3 exercises." That's 5-10 out of ~100. What about the other 90?

**Recommendation**: Read the actual existing exercises NOW (before committing to the strategy) and assess the conversion effort. If conversion requires significant manual work per exercise, the timeline is wrong.

### ISSUE 10: Phase timing is optimistic

| Phase   | Claimed Duration | Reality Check                                                                      |
| ------- | ---------------- | ---------------------------------------------------------------------------------- |
| Phase 0 | Days 1-2         | Realistic if ttyd is already installed                                             |
| Phase 1 | Days 3-7         | 5 days for a working Go binary with WebSocket + PTY + embedded xterm.js? Tight.    |
| Phase 2 | Days 8-14        | REST API + exercise management + React components + Docusaurus integration? Tight. |
| Phase 3 | Days 15-21       | Windows ConPTY + CI/CD + install scripts + self-update? VERY tight.                |
| Phase 4 | Days 22-28       | tmux + 100 exercises + docs + testing? No way in 7 days.                           |

Total: 28 days for a complete practice environment from scratch. This assumes no bugs, no blockers, no scope creep. Go binary development, Windows ConPTY, and CI/CD pipelines each routinely take longer than estimated.

**Recommendation**: Double the Phase 1 and Phase 3 estimates at minimum. The user values accuracy over optimism.

---

## OVER-ENGINEERING DETECTION

The user said the proof is: "student opens browser terminal, Claude Code works, exercise loads. Everything else is v0.2+."

Let's test the strategy against that bar.

### Things in v0.1 scope that ARE necessary:

- Go binary with WebSocket + PTY bridge (core)
- Health check endpoint (needed for setup card UX)
- Exercise start endpoint (needed to create workspaces)
- xterm.js React component (core)
- Practice button on lesson page (core)
- Origin validation on WebSocket (security, non-negotiable)

### Things in the strategy that are OVER-ENGINEERED for v0.1:

1. **Self-update mechanism (`af-practice update`)** -- Phase 3 feature creep. For v0.1, if you need a new version, re-run the install script. Self-update is a nice-to-have that requires implementing binary self-replacement, version checking against GitHub API, and atomic file swaps. Cut it.

2. **Port fallback range (3100-3110) with discovery** -- Phase 1 should use a fixed port. If it's taken, print an error: "Port 3100 in use. Kill the other process or use AF_PORT=3101 af-practice." Port scanning from the browser (trying 3100-3110 sequentially) adds ~100ms per port and unnecessary complexity. A fixed port with an env var override is simpler.

3. **Protocol version negotiation** -- The strategy describes version handshake (`{ type: 'hello', protocolVersion: 2 }`). For v0.1 there is one version. Add versioning when there's a second version. YAGNI.

4. **Session tracking for multiple concurrent exercises** -- The requirements doc allows multiple simultaneous exercises with resource warnings. For v0.1, support ONE exercise at a time. If the student starts a new exercise, the old one gets a clean shutdown prompt. Multiple concurrent exercises adds session management complexity that doesn't prove the core concept.

5. **Completion verification (`verify.sh` scripts)** -- The user said "exercise loads." Verification is valuable but is a separate feature. For v0.1, the student and Claude Code decide together if they're done. Script-based verification can come in v0.2 when there are enough exercises to justify the authoring investment.

**Bottom line**: The strategy's Phase 1 is lean enough, but Phases 2-4 pack in features (self-update, port scanning, protocol negotiation, multi-session tracking) that should be explicitly marked as stretch goals, not commitments.

---

## MISSING USER JOURNEYS

The strategy covers: first-time setup, happy path exercise, returning to in-progress, completion. These are the obvious ones. Here's what's missing:

### Journey A: Student already has exercises downloaded (offline/local copy)

**Scenario**: Student cloned the learn-app repo and has `apps/learn-app/static/exercises/` on their machine. They're not running the Docusaurus dev server because they're reading a PDF or hardcopy of the book.

**Current strategy**: Go binary fetches from `http://localhost:3000/exercises/<id>/`. If learn-app isn't running, the fetch fails and the exercise can't start.

**Gap**: No fallback for local filesystem exercises. The Go binary should accept a `--exercises-dir` flag pointing to a local directory:

```bash
af-practice --exercises-dir ./apps/learn-app/static/exercises/
```

### Journey B: Student is fully offline

**Scenario**: Student on an airplane, no internet, no local dev server.

**Current strategy**: Go binary needs to fetch exercises from learn-app's HTTP server. Dead on arrival.

**Gap**: If exercises were bundled in the binary (via `go:embed`) or previously cached in `~/af-practice/`, offline would work. Currently neither is guaranteed. The binary should cache every exercise it fetches, and on failure, check the local cache before giving up.

### Journey C: Practice server crashes mid-exercise

**Scenario**: `af-practice` crashes or gets killed (OOM, user accidentally Ctrl+C'd, system restart).

**Current strategy (Phase 1, no tmux)**: "PTY lost. Claude Code `--resume` reloads conversation." This means the student loses their current terminal state but not their conversation history.

**Gap that IS addressed**: The strategy handles this correctly via Claude Code's `--resume`. However, the **student doesn't know what happened**. The browser shows "Reconnecting..." and eventually "Connection lost." There's no message explaining: "The practice server stopped. Your work is saved. Restart `af-practice` and click Practice again to resume."

The error message must be specific, not generic.

### Journey D: Multiple students on the same machine (classroom/lab)

**Scenario**: Computer lab, 30 students, 10 shared machines. Each student logs in with their own OS account.

**Current strategy**: Not addressed at all.

**Analysis**: This actually works fine IF each student has their own OS user account. The practice server runs per-user, workspaces are in `~/af-practice/` (per-user home), and each student has their own Anthropic API key. No conflicts.

**But**: If students share an OS account (common in underfunded labs), they'd share the same `af-practice` instance and the same workspaces. Exercise state would be intermingled. This is unlikely but worth noting in the docs as "not supported."

### Journey E: Firewall or security software blocks localhost WebSocket

**Scenario**: Student is on a corporate network. Security software (Cisco AnyConnect, Zscaler, CrowdStrike) intercepts localhost traffic or blocks WebSocket connections.

**Current strategy**: Not addressed.

**Analysis**: This is a real issue. Corporate VPNs sometimes route ALL traffic (including localhost) through their tunnel. Antivirus can flag a binary that opens a WebSocket server as suspicious.

**Mitigation options**:

- Document as a known limitation with workaround ("add `af-practice` to your security software's allowlist")
- Support `--bind-address` flag for binding to custom interfaces if localhost is blocked
- Fallback to HTTP long-polling (like Replit's Crosis) -- but this is complex and likely not worth it

This is probably the weakest kill-shot risk. Most students in this educational program are NOT in locked-down corporate environments. But it should be documented.

### Journey F: Student wants to use their own terminal instead of the browser terminal

**Scenario**: Power user. Prefers iTerm2/Windows Terminal. Doesn't want to use xterm.js in the browser.

**Current strategy**: Browser-embedded terminal is the only interface.

**Gap**: The exercise CLAUDE.md and workspace creation are valuable even without the browser terminal. The Go binary should support a "headless" mode:

```bash
af-practice start --exercise ch34-first-agent --no-browser
# Creates workspace, writes CLAUDE.md, prints:
# "Workspace created at ~/af-practice/ch34-first-agent/"
# "Open a terminal there and run: claude"
```

This is low-cost to implement and serves power users who just want the exercise scaffolding.

---

## ALTERNATIVE APPROACHES COMPARISON

The strategy presents its architecture (custom Go binary) as the conclusion of careful research. But some simpler alternatives were dismissed too quickly.

### Alternative 1: Just use ttyd directly

**What it would look like:**

```bash
# Install ttyd (one-time)
brew install ttyd          # macOS
apt install ttyd           # Linux
# Windows: download from GitHub releases

# Start exercise (each time)
mkdir -p ~/af-practice/my-exercise && cd ~/af-practice/my-exercise
# Student copies exercise CLAUDE.md manually or uses a small script
ttyd -W -p 3100 claude
# Open http://localhost:3100 in browser
```

**Pros**: Zero custom code. Battle-tested. Ships today.

**Cons**:

- No exercise management (workspace creation, CLAUDE.md delivery)
- No health check integration with learn-app
- No macOS binary in ttyd releases (need Homebrew)
- Only 32-bit Windows binary
- Student must manage ttyd themselves (worse UX than the strategy)
- No way to embed the terminal in the learn-app page (ttyd serves its own HTML)

**Verdict**: ttyd is the right Phase 0 proof-of-concept tool. But it's not a product. The strategy correctly identifies this. The gap between "ttyd works" and "integrated practice environment" is real.

However, there's a middle ground: **use ttyd AS the PTY bridge, with a thin wrapper script for exercise management.** The thin wrapper would be a ~100 line bash/python script (not a Go binary) that:

1. Downloads ttyd if not present
2. Creates workspace and copies exercise files
3. Starts `ttyd -W -p 3100 claude` in the workspace
4. Learns learn-app communicates with it via the ttyd WebSocket

This avoids building a custom Go PTY bridge from scratch. The trade-off is less control over the WebSocket protocol and no exercise REST API.

**This middle-ground approach is worth serious consideration.** It trades engineering effort for deployment simplicity.

### Alternative 2: VS Code terminal extension

**What it would look like**: A VS Code extension that:

- Adds an "AgentFactory Practice" sidebar
- Lists available exercises from the registry
- Creates workspaces
- Opens integrated terminal with Claude Code

**Pros**:

- Most students likely have VS Code (the book teaches it in Part 3)
- No separate server process
- VS Code's terminal is the gold standard for xterm.js rendering (same library)
- Extension marketplace distribution (one-click install)
- Cross-platform (Windows, macOS, Linux) built in
- Inherits VS Code's PTY handling (battle-tested node-pty)

**Cons**:

- Students must use VS Code (not browser-first)
- Doesn't embed in the learn-app browser page
- Separate from the lesson content (context switch)
- Extension development and publishing is its own skill/overhead
- Not "in the browser" which is a core requirement

**Verdict**: This is a genuinely strong alternative that the strategy never considers. If the requirement "terminal must be IN the browser" were relaxed, a VS Code extension would be simpler, more reliable, and ship faster. Worth raising with the user as a "have you considered?" question. The core value proposition -- guided exercises with CLAUDE.md -- works identically in VS Code or in a browser terminal.

### Alternative 3: "Just open your terminal" with a CLI tool

**What it would look like**: No browser terminal at all. A CLI tool that manages exercises:

```bash
# Install
curl -fsSL https://agentfactory.dev/install.sh | bash

# List exercises
af-practice list

# Start exercise
af-practice start ch34-first-agent
# Output: "Workspace created at ~/af-practice/ch34-first-agent/"
# Output: "Starting Claude Code..."
# Claude Code opens in the current terminal with exercise CLAUDE.md loaded
```

**Pros**:

- Vastly simpler (no WebSocket, no xterm.js, no browser component)
- Works on every platform where Claude Code works
- No rendering fidelity risk (student's native terminal)
- No server process to manage
- Could ship in ~3 days

**Cons**:

- Not embedded in the lesson page (biggest loss)
- Student must context-switch from browser to terminal
- Can't show exercise alongside lesson content
- Loses the "click Practice and a terminal appears" UX vision

**Verdict**: This is the "minimum viable" approach. If the browser-embedded terminal proves too complex or the Phase 0 kill-shot fails, this is the smart fallback. The exercise CLAUDE.md system, workspace management, and completion verification all work identically. Only the presentation layer differs.

**The strategy should explicitly acknowledge this as the fallback plan**, not just the headless mode of Claude Code (`-p` flag). A CLI-only exercise tool is more useful than headless mode because it preserves the full Claude Code TUI experience in the student's native terminal.

---

## ADDITIONAL KILL SHOT RISKS (Not Covered in Strategy)

### Kill Shot: Chrome Private Network Access (PNA) breaking localhost WebSocket

The research (`vercel-approach.md` Section 9) documents that **Chrome 142+** introduces permission prompts for websites accessing localhost. If the student accesses the learn-app from a production URL (not localhost), Chrome will prompt "Allow this site to access your network?" before the WebSocket connection to `localhost:3100` can be established.

**Impact**: Every Chrome update could break this. The strategy mentions proxying through the Docusaurus dev server as mitigation, but this only works for local development. In production, there's no proxy.

**Mitigation**: The learn-app frontend must handle this gracefully -- detect PNA failures and show a clear "Allow network access" instruction to the student.

### Kill Shot: Antivirus flagging the Go binary

A standalone binary downloaded via `curl | bash` that opens a WebSocket server and spawns shell processes will trigger heuristic detection in many antivirus products. Windows Defender in particular is aggressive about flagging unsigned binaries that perform network operations.

**Impact**: Students see scary warnings or the binary is quarantined silently.

**Mitigation**: Code-sign the binaries (Apple notarization for macOS, Authenticode for Windows). This is not mentioned in the strategy and adds significant CI/CD complexity plus annual certificate costs (~$200-400/year for code signing).

---

## WHAT THE STRATEGY GETS RIGHT

1. **Go binary pivot**: Correct. The npx assumption was invalidated by research. Single binary is the right architecture for this tool.

2. **Phase 0 proof-of-concept**: Excellent. Testing the kill-shot risk before building anything is the highest-leverage work. This should be Phase 0, and it is.

3. **Deferring tmux**: Smart. tmux adds friction (install, cross-platform gaps) and only helps with one scenario (server restart). Direct PTY is simpler for Phase 1.

4. **Tab in Sheet panel (not ChatKit widget)**: Correct. Research proves ChatKit can't host custom React components. Tab approach is the right call.

5. **Exercise registry as static files**: Correct. Co-locating exercises with lesson content keeps them versioned together.

6. **Fallback plan for TUI rendering failure**: Good. The headless mode pivot is a viable backup.

7. **Section 7 (What Changed)**: Excellent. Clear diff between old and new decisions with rationale for each change. This is how strategy documents should communicate changes.

---

## SIMPLICITY SCORECARD

The user said: "Simplicity is king -- if any step is more than 1 action, flag it."

| Action                       | Steps Required | Simplicity Verdict  |
| ---------------------------- | -------------- | ------------------- |
| **Install af-practice**      | 1 command      | PASS                |
| **Start af-practice**        | 1 command      | PASS                |
| **Click Practice in lesson** | 1 click        | PASS                |
| **First-time complete flow** | 3+ actions     | FAIL (see Issue 1)  |
| **Returning flow**           | 2 actions      | BORDERLINE          |
| **Windows setup**            | Unknown        | FAIL (see Issue 3)  |
| **Exercise works instantly** | 1 click        | PASS (if server up) |

---

## RECOMMENDATIONS SUMMARY

| Issue                                      | Severity | Action                                                       |
| ------------------------------------------ | -------- | ------------------------------------------------------------ |
| #1 First-time flow is 3+ steps             | CRITICAL | Acknowledge gap, plan auto-start for Phase 3                 |
| #2 Go is foreign to this codebase          | CRITICAL | Present fair Go vs. Bun comparison, let user decide          |
| #3 Windows is hand-waved                   | CRITICAL | Downgrade to Tier 2 until actually built, or move to Phase 1 |
| #4 Exercise fetch chicken-and-egg          | CRITICAL | Add bundled exercises fallback                               |
| #5 No WebSocket security in Phase 1        | CRITICAL | Add origin validation to Phase 1 scope                       |
| #6 No scrollback on reconnect              | MEDIUM   | Add ring buffer replay to Phase 1                            |
| #7 Production deployment not addressed     | MEDIUM   | Add production URL as exercise source                        |
| #8 curl-pipe-bash anti-pattern             | LOW      | Add direct download as first-class option                    |
| #9 Existing exercises integration vague    | MEDIUM   | Read actual exercises before committing                      |
| #10 Timeline is optimistic                 | LOW      | Double Phase 1 and 3 estimates                               |
| #11 Over-engineering in v0.1 scope         | MEDIUM   | Cut self-update, port scanning, protocol versioning          |
| #12 Chrome PNA may block production use    | HIGH     | Handle PNA failures in frontend, document workaround         |
| #13 Unsigned binaries flagged by antivirus | HIGH     | Plan code signing for macOS (notarization) and Windows       |
| #14 No CLI-only fallback acknowledged      | MEDIUM   | Add CLI-only exercise tool as explicit fallback plan         |
| #15 VS Code extension never considered     | LOW      | Raise as alternative with user (relaxes browser requirement) |

---

## KEY QUESTION FOR THE USER

Before proceeding to implementation, one question should be answered:

**Is "terminal embedded IN the browser page" a hard requirement, or is "students can easily practice exercises with Claude Code" the actual requirement?**

If the former: the strategy (with the fixes above) is the right path. Build the Go binary, embed xterm.js, solve the cross-platform PTY problems.

If the latter: a CLI-only tool (`af-practice start <exercise-id>` which opens Claude Code in the student's terminal) ships in 3 days, works on every platform, has zero rendering risk, and delivers 90% of the value. The browser-embedded terminal can be added later as an enhancement.

The answer to this question changes the timeline from 4+ weeks to ~3 days.
