# Phase 0: Proof of Concept — Claude Code TUI Rendering in Browser

**Purpose**: Prove or disprove the kill-shot risk before writing any code.
**Time**: ~5 minutes to run, ~10 minutes to evaluate.
**Date**: 2026-02-12

---

## Quick Summary

```
Install ttyd → launch Claude Code through it → open browser → check 8 criteria → go/no-go
```

---

## Step 1: Install ttyd

```bash
# macOS (Homebrew)
brew install ttyd

# Linux (pre-built binary)
curl -fsSL https://github.com/tsl0922/ttyd/releases/latest/download/ttyd.x86_64 -o /usr/local/bin/ttyd
chmod +x /usr/local/bin/ttyd

# Verify
ttyd --version
```

## Step 2: Launch Claude Code Through ttyd

```bash
# Basic launch — writable terminal running Claude Code
ttyd -W -p 7681 claude

# What this does:
#   -W    = enable write (browser can send keystrokes)
#   -p 7681 = listen on port 7681
#   claude = the command to run inside the PTY
```

If Claude Code needs specific environment variables (API key), make sure they're set in the shell where you run ttyd:

```bash
# If needed, export API key first
export ANTHROPIC_API_KEY=sk-ant-...
ttyd -W -p 7681 claude
```

## Step 3: Open in Browser

Open: **http://localhost:7681**

You should see Claude Code's TUI rendered in the browser.

## Step 4: Run the Validation Checklist

Test each criterion below. Record PASS/FAIL and take a screenshot for evidence.

---

### Test 1: Initial TUI Render

**What to check**: Does Claude Code's welcome screen render correctly?

- [ ] Status bar visible at top or bottom (shows model name, token count, etc.)
- [ ] Colors render (syntax highlighting, colored text, not all monochrome)
- [ ] Box-drawing characters render (borders around UI elements) OR gracefully degrade to ASCII (`+`, `-`, `|`)
- [ ] Text is readable (no overlapping characters, no garbled escape codes visible as raw text)
- [ ] Cursor is visible and positioned correctly

**PASS criteria**: Welcome screen is readable and visually coherent. Minor cosmetic differences from native terminal are acceptable.
**FAIL criteria**: Raw escape codes visible (e.g., `[32m`, `[0m`), garbled text, completely broken layout, or blank screen.

---

### Test 2: Keyboard Input

**What to check**: Can you type normally?

- [ ] Type a simple prompt: "What is 2 + 2?" and press Enter
- [ ] Characters appear as you type (no input lag visible to the eye)
- [ ] Enter key submits the prompt
- [ ] Backspace works (deletes characters)
- [ ] Arrow keys work in input field (if Claude Code supports them)

**PASS criteria**: Typing feels responsive and correct. Round-trip latency (type -> echo) is imperceptible on localhost.
**FAIL criteria**: Keystrokes lost, duplicate characters, wrong characters, or visible input delay (>200ms).

---

### Test 3: Claude Code Response Rendering

**What to check**: Does Claude Code's response render correctly?

- [ ] Response text appears progressively (streaming)
- [ ] Markdown formatting renders (bold, code blocks, lists) — as Claude Code formats them in the terminal
- [ ] Code blocks have syntax highlighting (colored text)
- [ ] Long responses scroll correctly (content doesn't overflow or overlap)

**PASS criteria**: Response is fully readable and looks similar to running Claude Code in a native terminal.
**FAIL criteria**: Text overlaps itself, streaming causes visual corruption, or formatting is completely lost.

---

### Test 4: Tool Approval UI

**What to check**: Claude Code's permission prompts (the Y/N confirmation for tool use) work correctly.

**How to trigger**: Ask Claude Code to do something that requires tool approval:

```
Create a file called test-poc.txt with the content "hello world"
```

- [ ] Permission prompt appears (asking to approve file creation)
- [ ] The prompt UI renders correctly (buttons/options visible)
- [ ] You can press 'y' or 'n' to approve/reject
- [ ] After approval, the action executes and result displays

**PASS criteria**: Full tool approval flow works end-to-end.
**FAIL criteria**: Permission prompt is garbled, keystrokes for Y/N don't register, or the UI hangs waiting for input.

---

### Test 5: Multi-line Input

**What to check**: Can you enter multi-line prompts?

**How to trigger**: In Claude Code, try entering a multi-line message (Shift+Enter or whatever Claude Code uses for newlines):

```
Explain the difference between:
1. A list
2. A tuple
3. A dictionary
```

- [ ] Multi-line input renders correctly (each line on its own line)
- [ ] Cursor navigation within multi-line input works
- [ ] Submitting multi-line input works

**PASS criteria**: Multi-line input works as expected.
**FAIL criteria**: Newlines don't register, lines collapse into one, or cursor jumps unpredictably. (NOTE: If Claude Code uses Shift+Enter for newlines and this specific key combo doesn't pass through, that's a MEDIUM issue, not a kill shot — there may be alternative input methods.)

---

### Test 6: Scrolling and Scrollback

**What to check**: Can you scroll through conversation history?

- [ ] Mouse scroll works (scroll up to see previous messages)
- [ ] Scroll bar appears (if xterm.js shows one)
- [ ] After scrolling up, new output auto-scrolls back to bottom (or shows "new content" indicator)
- [ ] Keyboard scrollback works (Shift+PageUp/PageDown if supported)

**PASS criteria**: Can review previous conversation content.
**FAIL criteria**: No scrollback at all, or scrolling causes rendering corruption.

---

### Test 7: Terminal Resize

**What to check**: Does resizing the browser window properly resize the terminal?

- [ ] Resize browser window — does the terminal re-render to fit?
- [ ] Claude Code's UI adapts to new dimensions (status bar, text wrapping)
- [ ] No rendering artifacts after resize (no "ghost" characters from previous layout)

**PASS criteria**: Terminal is responsive to window size changes.
**FAIL criteria**: Resize causes permanent rendering corruption, or terminal stays fixed-size ignoring window changes.

---

### Test 8: Extended Session (Stress Test)

**What to check**: Does the terminal remain stable over a longer interaction?

- [ ] Have a 5-message conversation (ask multiple questions)
- [ ] No progressive degradation (each response renders as well as the first)
- [ ] No memory leaks visible (browser tab doesn't become sluggish)
- [ ] Ctrl+C works (interrupts Claude Code if it's generating)

**PASS criteria**: Stable through a full multi-turn conversation.
**FAIL criteria**: Browser tab crashes, freezes, or rendering degrades over time.

---

## Step 5: Record Results

Fill in this table:

| #   | Test               | Result      | Notes |
| --- | ------------------ | ----------- | ----- |
| 1   | Initial TUI Render | PASS / FAIL |       |
| 2   | Keyboard Input     | PASS / FAIL |       |
| 3   | Response Rendering | PASS / FAIL |       |
| 4   | Tool Approval UI   | PASS / FAIL |       |
| 5   | Multi-line Input   | PASS / FAIL |       |
| 6   | Scrolling          | PASS / FAIL |       |
| 7   | Terminal Resize    | PASS / FAIL |       |
| 8   | Extended Session   | PASS / FAIL |       |

**Take a screenshot of the initial TUI render and at least one response.** Attach to this document or save as `phase0-screenshot-*.png` in this directory.

---

## Decision Matrix

| Result                                           | Action                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **All 8 PASS**                                   | Proceed to Phase 1 as designed.                                                                                                                                                                                                                                                                                       |
| **Tests 1-4 PASS, 5-8 have minor issues**        | Proceed to Phase 1. File issues for minor problems. Likely fixable with xterm.js configuration or Claude Code flags.                                                                                                                                                                                                  |
| **Test 4 (Tool Approval) FAILS**                 | **BLOCKER.** Tool approval is the core interaction loop. Investigate: try different TERM values (`xterm-256color`, `xterm`, `vt100`). Try `ttyd -t fontSize=14 -t 'theme={"background":"#1e1e1e"}'` for configuration tweaks. If still broken, test direct PTY without ttyd (write minimal Go/Node WebSocket bridge). |
| **Test 1 FAILS (TUI doesn't render at all)**     | **KILL SHOT.** Try: (1) `TERM=xterm-256color ttyd -W claude`, (2) `ttyd -W bash` then run `claude` inside it, (3) different browser. If all fail, pivot to headless mode (Claude Code `-p` flag with chat UI).                                                                                                        |
| **Tests 1-3 PASS but Test 2 has >200ms latency** | Investigate buffering. Try: `ttyd -W -p 7681 -B 0 claude` (buffer size 0). On localhost, latency should be <10ms. If laggy, it's likely a ttyd buffering issue, not fundamental.                                                                                                                                      |

---

## Variant Tests (If Primary Passes)

If the basic test passes, run these variants to stress-test the pipeline:

### Variant A: tmux in the Middle

```bash
# Does adding tmux break anything?
tmux new-session -d -s poc-test 'claude'
ttyd -W -p 7681 tmux attach -t poc-test
# Open http://localhost:7681
# Run the same 8 tests
```

### Variant B: Specific Exercise Flow

```bash
# Simulate the actual exercise flow
mkdir -p /tmp/af-poc-test
cat > /tmp/af-poc-test/CLAUDE.md << 'EXERCISE_EOF'
# Exercise: PoC Validation

## Your Task
Create a Python file called hello.py that prints "Hello, Agent Factory!"

## Rules
- Guide me step by step. Do not write the code for me.
- When I'm stuck, give ONE hint, not the answer.

## Success Criteria
- [ ] hello.py exists
- [ ] Running `python3 hello.py` prints "Hello, Agent Factory!"
EXERCISE_EOF

# Launch Claude Code in the exercise workspace
cd /tmp/af-poc-test
ttyd -W -p 7681 claude
# Open browser, verify Claude Code reads the CLAUDE.md and starts the exercise
```

### Variant C: Reconnection

```bash
# Start ttyd + Claude Code
ttyd -W -p 7681 claude
# Open browser, start a conversation
# Close the browser tab
# Reopen http://localhost:7681
# Does Claude Code still show? (ttyd spawns a new process per connection by default)
# For session persistence, need: ttyd -W -p 7681 -O tmux new -A -s test-session
```

**Note on Variant C**: By default, ttyd spawns a new command per browser connection. To test reconnection (session persistence), use tmux:

```bash
ttyd -W -p 7681 -O tmux new-session -A -s poc-session
# -O = enable WebSocket reconnection
# tmux new-session -A -s = attach to existing session or create new one
```

---

## Cleanup

```bash
# After testing, stop everything
# Ctrl+C the ttyd process

# Remove test workspace
rm -rf /tmp/af-poc-test

# Optionally uninstall ttyd (if you don't need it anymore)
# brew uninstall ttyd
```

---

## Time Estimate

| Step                     | Time           |
| ------------------------ | -------------- |
| Install ttyd             | 1 min          |
| Launch + open browser    | 30 sec         |
| Run 8 tests              | 5-8 min        |
| Record results           | 2 min          |
| Variant tests (optional) | 5-10 min       |
| **Total**                | **~10-20 min** |
