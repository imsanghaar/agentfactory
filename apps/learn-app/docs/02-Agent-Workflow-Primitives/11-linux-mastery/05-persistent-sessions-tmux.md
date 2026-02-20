---
sidebar_position: 5
title: "Persistent Sessions with tmux"
description: "Create terminal sessions that survive disconnections, split panes for multi-task monitoring, write session scripts for repeatable layouts, and manage windows for complex agent workflows"
keywords: ["tmux", "terminal multiplexer", "persistent sessions", "pane splitting", "named sessions", "session scripts", "window management", "copy mode", "SSH persistence"]
chapter: 11
lesson: 5
duration_minutes: 55

# HIDDEN SKILLS METADATA
skills:
  - name: "tmux Session Lifecycle"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can create named tmux sessions, detach, reattach, list sessions, and kill sessions without confusion about session state"

  - name: "Pane Splitting and Navigation"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can split tmux panes horizontally and vertically, navigate between panes, and resize panes to create monitoring layouts"

  - name: "Named Sessions for Context Switching"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can create multiple named sessions for different projects, switch between them, and explain why named sessions improve workflow organization"

  - name: "Session Scripts for Reproducible Layouts"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can write a bash script that creates a tmux session with named windows, split panes, and commands sent to each pane"

  - name: "Window Management"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can create, rename, and switch between tmux windows within a single session"

  - name: "Copy Mode for Scrollback"
    proficiency_level: "B2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can enter copy mode, scroll through output history, and search within scrollback buffer"

learning_objectives:
  - objective: "Create, detach from, and reattach to tmux sessions"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates a named session, starts a long-running process, detaches, verifies the session persists with tmux ls, and reattaches to confirm the process continued"

  - objective: "Split tmux panes horizontally and vertically for multi-task workflows"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates a 3-pane layout with agent process, log tail, and system monitor running simultaneously"

  - objective: "Create named sessions for different project contexts"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student creates at least two named sessions, switches between them, and explains how each maintains independent state"

  - objective: "Write session scripts for reproducible tmux layouts"
    proficiency_level: "B2"
    bloom_level: "Apply"
    assessment_method: "Student writes a bash script that creates a tmux session with specific pane layout and commands, runs the script, and verifies the layout with tmux list-panes"

cognitive_load:
  new_concepts: 6
  concepts_list:
    - "tmux session lifecycle (new, detach, attach, kill)"
    - "Pane splitting (horizontal/vertical)"
    - "Named sessions for project isolation"
    - "Session scripts for repeatable layouts"
    - "Window management within sessions"
    - "Copy mode for scrollback navigation"
  assessment: "6 concepts within B2 limit of 7-10. Hands-on exercises after each concept keep working memory manageable."

differentiation:
  extension_for_advanced: "Explore tmuxinator or tmux-resurrect plugins for persistent session saving across reboots. Investigate tmux hooks for automated actions on session events. Compare tmux with Zellij (modern Rust-based terminal multiplexer)."
  remedial_for_struggling: "Focus on create, detach, and reattach first. Practice the basic lifecycle 3-4 times until it feels natural before attempting pane splitting. Use tmux ls after every action to verify session state."

teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "Shell Customization and Tooling"
  key_points:
    - "tmux sessions survive disconnections — this is non-negotiable for production agent management where SSH drops would otherwise kill running processes"
    - "The four-operation lifecycle (create, detach, attach, kill) is the foundation — all advanced tmux usage builds on these four commands"
    - "Session scripts make layouts reproducible across servers — this is the first time students write a bash script, previewing lesson 6 (bash scripting)"
    - "Named sessions provide project isolation — each agent project gets its own tmux session with independent state, working directory, and processes"
  misconceptions:
    - "Students confuse detaching (Ctrl+b then d, session lives on) with closing the terminal (may kill the session) — drill the difference explicitly"
    - "Students think panes are separate sessions — panes are views within the same session window, sharing the same session lifecycle"
    - "Students expect tmux to save sessions across server reboots — tmux sessions are lost on reboot unless using plugins like tmux-resurrect"
  discussion_prompts:
    - "Your AI agent is processing a 4-hour data pipeline over SSH. Your laptop battery is dying. What do you do, and why does tmux make this a non-issue?"
    - "How would you organize tmux sessions for managing 5 different AI agents on the same server — one session per agent, or one session with 5 windows?"
  teaching_tips:
    - "Demo the detach-reattach cycle live with a running counter — students seeing a process continue while 'disconnected' is the most powerful moment in this lesson"
    - "The tmux quick reference table is a handout moment — students will reference it constantly during exercises and the capstone (lesson 14)"
    - "Build the 3-pane monitoring layout step by step before showing the session script — students need to understand what the script automates"
    - "Pane splitting shortcuts (Ctrl+b % and Ctrl+b \") look arbitrary — explain that % looks like two side-by-side panes and \" looks like a horizontal line"
  assessment_quick_check:
    - "Ask students to create a named session, detach, verify it exists with tmux ls, and reattach — the complete lifecycle in 4 commands"
    - "Ask: what happens to processes running inside a tmux session when you detach? (Expected: they continue running)"
    - "Ask students to split a pane vertically and horizontally, resulting in 3 panes — verify with tmux list-panes"

generated_by: "content-implementer"
created: "2026-02-09"
version: "2.0.0"
---

# Persistent Sessions with tmux

In Lesson 4, you customized your shell with aliases, installed tools with `apt`, and added smart navigation with `zoxide` and `fzf`. Your terminal is now fast and personalized. But there is a critical gap: **your terminal dies when your connection drops.**

When you SSH into a server to run a long-running agent process, what happens when your laptop sleeps, your WiFi drops, or the SSH connection times out? Everything stops. Your agent halts mid-task. Your data pipeline aborts. Your debug session vanishes. Hours of work, gone -- because your process was tied to your terminal session.

**tmux** (terminal multiplexer) solves this by creating sessions that live on the server, independent of your connection. Think of tmux as a persistent workspace: you walk into a room, set up your work, walk out, and when you come back everything is exactly as you left it. For Digital FTE deployment, where agents run for hours or days, tmux is non-negotiable. Your connection should never be your agent's single point of failure.

## The tmux Session Lifecycle

Every tmux workflow follows four operations: create, detach, attach, kill. Master these four and you control session persistence.

### Create a Named Session

```bash
tmux new-session -s agent-training
```

**Output:**
```
[You are now inside a tmux session. The bottom of the screen shows
a green status bar with: [agent-training] 0:bash  "hostname" HH:MM DD-MMM-YY]
```

The `-s agent-training` flag gives your session a meaningful name. Without it, tmux assigns numbers (0, 1, 2), which become confusing when you have multiple sessions.

### Start a Long-Running Process

Inside your tmux session, start something that takes time:

```bash
for i in $(seq 1 60); do echo "$(date): Training iteration $i/60"; sleep 3; done
```

**Output:**
```
Sun Feb  9 14:32:01 UTC 2026: Training iteration 1/60
Sun Feb  9 14:32:04 UTC 2026: Training iteration 2/60
Sun Feb  9 14:32:07 UTC 2026: Training iteration 3/60
```

This simulates a 3-minute training run. In production, this would be hours of model training or data processing.

### Detach Without Stopping

While the process runs, press `Ctrl+b`, then `d` (press Ctrl+b together, release, then press d alone).

**Output:**
```
[detached (from session agent-training)]
```

You are back in your normal terminal. The training process continues running inside the tmux session on the server.

### Verify the Session Exists

```bash
tmux ls
```

**Output:**
```
agent-training: 1 windows (created Sun Feb  9 14:31:45 2026)
```

Your session is alive and your process is still running inside it.

### Reattach to Your Session

```bash
tmux attach -t agent-training
```

**Output:**
```
Sun Feb  9 14:33:10 UTC 2026: Training iteration 24/60
Sun Feb  9 14:33:13 UTC 2026: Training iteration 25/60
```

The training continued the entire time you were detached. It never stopped, never paused, never knew you left.

### Kill a Session When Done

When you no longer need a session, destroy it:

```bash
tmux kill-session -t agent-training
```

**Output:**
```
(no output -- session is gone)
```

Verify:

```bash
tmux ls
```

**Output:**
```
no server running on /tmp/tmux-1000/default
```

:::warning
`tmux kill-session` permanently destroys a session and terminates all processes inside it. Always verify you are targeting the correct session name before running this command.
:::

## Pane Splitting: Multiple Views in One Window

A single terminal pane limits you to one task at a time. tmux lets you split your window into multiple panes so you can run an agent, watch its logs, and monitor system resources simultaneously.

### Create a Session and Split Vertically

```bash
tmux new-session -s monitoring
```

Inside the session, split into left and right panes:

Press `Ctrl+b`, then `%`

**Output:**
```
[Screen splits into two side-by-side panes with a vertical divider.
 Your cursor is in the right pane.]
```

### Split Horizontally

With the right pane selected, split it top and bottom:

Press `Ctrl+b`, then `"`

**Output:**
```
[Right side splits into top and bottom. You now have 3 panes:
 Left (full height) | Right-top | Right-bottom]
```

Your layout now looks like this:

```
+------------------+------------------+
|                  |   Right-top      |
|   Left pane      |                  |
|   (full height)  +------------------+
|                  |   Right-bottom   |
|                  |                  |
+------------------+------------------+
```

### Navigate Between Panes

Move to the next pane:

Press `Ctrl+b`, then `o`

Each press of `Ctrl+b` then `o` cycles to the next pane. For direct navigation to a specific direction:

- `Ctrl+b`, then arrow key (up/down/left/right) -- jump to the pane in that direction

### Resize Panes

Hold `Ctrl+b`, then press and hold an arrow key to resize:

- `Ctrl+b` then hold `Left` -- make current pane wider
- `Ctrl+b` then hold `Down` -- make current pane taller

:::note
Resizing uses `Ctrl+b` followed by holding the arrow key, not pressing it once. If the pane does not resize, try `Ctrl+b` then `Alt+arrow` which resizes in larger increments on some configurations.
:::

### Set Up Each Pane for Agent Monitoring

Navigate to each pane (`Ctrl+b` then `o`) and run a different command:

**Left pane** -- simulate an agent process:

```bash
for i in $(seq 1 200); do echo "[Agent] Processing request $i"; sleep 2; done
```

**Output:**
```
[Agent] Processing request 1
[Agent] Processing request 2
```

**Right-top pane** -- monitor system resources:

```bash
top -d 2
```

**Output:**
```
top - 14:45:03 up 2 days,  3:22,  1 user,  load average: 0.15, 0.10, 0.08
Tasks: 102 total,   1 running, 101 sleeping,   0 stopped,   0 zombie
%Cpu(s):  2.3 us,  1.0 sy,  0.0 ni, 96.5 id,  0.0 wa,  0.2 hi,  0.0 si
```

**Right-bottom pane** -- watch a log file:

```bash
echo "Starting log watch..." && tail -f /var/log/syslog 2>/dev/null || echo "No syslog available -- create a test log:" && touch /tmp/agent.log && tail -f /tmp/agent.log
```

**Output:**
```
Starting log watch...
(waiting for new log entries)
```

You now have a complete monitoring dashboard: agent process on the left, system resources on the top right, logs on the bottom right. All in one terminal window, all persisting across disconnections.

### Verify Your Pane Count

```bash
tmux list-panes -t monitoring
```

**Output:**
```
0: [80x24] [history 0/2000] [flags=]
1: [80x12] [history 0/2000] [flags=]
2: [80x12] [history 0/2000] [flags=*]
```

Three panes, exactly as designed.

## Window Management

Panes divide a single screen. **Windows** give you entirely separate screens within the same session. Think of windows as tabs in a browser -- each has its own set of panes and content.

### Create a New Window

Inside your `monitoring` session:

Press `Ctrl+b`, then `c`

**Output:**
```
[Status bar shows: [monitoring] 0:bash  1:bash*
 The asterisk (*) marks the active window]
```

You are now in window 1, a fresh full-screen terminal. Window 0 still has your 3-pane monitoring layout.

### Name Your Windows

Give windows meaningful names:

Press `Ctrl+b`, then `,` (comma)

**Output:**
```
[Status bar shows rename prompt: (rename-window)]
```

Type `editor` and press Enter.

**Output:**
```
[Status bar shows: [monitoring] 0:bash  1:editor*]
```

### Switch Between Windows

- `Ctrl+b`, then `n` -- next window
- `Ctrl+b`, then `p` -- previous window
- `Ctrl+b`, then `0` -- jump to window 0
- `Ctrl+b`, then `1` -- jump to window 1

Press `Ctrl+b`, then `0` to return to your monitoring panes:

**Output:**
```
[Your 3-pane monitoring layout reappears exactly as you left it]
```

### List All Windows

Press `Ctrl+b`, then `w`

**Output:**
```
(0) 0: bash (3 panes) [162x44]
(1) 1: editor (1 pane) [162x44]
```

This overview shows every window, its pane count, and dimensions.

## Copy Mode: Scrolling Through History

Normal terminal output scrolls off the screen. tmux copy mode lets you scroll back through output history, search for text, and copy content.

### Enter Copy Mode

Press `Ctrl+b`, then `[`

**Output:**
```
[Top-right corner shows: [0/2000] indicating you are in copy mode
 with 2000 lines of scrollback available]
```

### Navigate in Copy Mode

- Arrow keys -- move cursor
- `Page Up` / `Page Down` -- scroll one page
- `g` -- jump to top of history
- `G` -- jump to bottom of history

### Search in Copy Mode

Press `/` to search forward, type your search term, and press Enter:

```
/error
```

**Output:**
```
[Cursor jumps to the first occurrence of "error" in scrollback.
 Press n for next match, N for previous match.]
```

### Exit Copy Mode

Press `q` or `Escape` to leave copy mode and return to normal terminal interaction.

:::note
Copy mode is essential for diagnosing agent failures. When your agent logs scroll past quickly, copy mode lets you scroll back and find the exact error message that caused the crash.
:::

## Named Sessions for Project Isolation

When you work on multiple projects, each project deserves its own session with its own layout, working directory, and running processes.

### Create Project Sessions

```bash
tmux new-session -d -s api-agent
tmux new-session -d -s data-pipeline
tmux new-session -d -s debug
```

**Output:**
```
(no output -- sessions created in detached mode)
```

The `-d` flag creates sessions without attaching to them, so you can create several in sequence.

### List All Sessions

```bash
tmux ls
```

**Output:**
```
api-agent: 1 windows (created Sun Feb  9 15:10:22 2026)
data-pipeline: 1 windows (created Sun Feb  9 15:10:23 2026)
debug: 1 windows (created Sun Feb  9 15:10:24 2026)
```

Three isolated workspaces, each maintaining its own state.

### Switch Between Sessions

Attach to one:

```bash
tmux attach -t api-agent
```

From inside a session, switch to another without detaching first:

Press `Ctrl+b`, then `s`

**Output:**
```
(0) api-agent: 1 windows
(1) data-pipeline: 1 windows
(2) debug: 1 windows
```

Use arrow keys to select a session and press Enter. You switch instantly. Each session keeps its own working directory, command history, pane layout, and running processes.

## Session Scripts: Reproducible Layouts

Manually splitting panes and running commands every time you start work is tedious. A session script creates your entire layout with one command.

### Write a Session Script

Create a script that builds a 3-pane agent monitoring layout:

```bash
nano ~/tmux-agent-monitor.sh
```

Add this content:

```bash
#!/bin/bash

SESSION_NAME="agent-monitor"

# Kill existing session if it exists (start fresh)
tmux kill-session -t "$SESSION_NAME" 2>/dev/null

# Create session with a named window
tmux new-session -d -s "$SESSION_NAME" -n dashboard

# Split vertically (left | right)
tmux split-window -h -t "$SESSION_NAME:dashboard"

# Split the right pane horizontally (right-top / right-bottom)
tmux split-window -v -t "$SESSION_NAME:dashboard.1"

# Send commands to each pane
tmux send-keys -t "$SESSION_NAME:dashboard.0" 'echo "=== Agent Process ===" && date' Enter
tmux send-keys -t "$SESSION_NAME:dashboard.1" 'echo "=== System Monitor ===" && top -d 5' Enter
tmux send-keys -t "$SESSION_NAME:dashboard.2" 'echo "=== Log Watcher ===" && echo "Watching for logs..."' Enter

# Attach to the session
tmux attach -t "$SESSION_NAME"
```

Save and exit (`Ctrl+O`, Enter, `Ctrl+X`).

### Make It Executable and Run

```bash
chmod +x ~/tmux-agent-monitor.sh
```

**Output:**
```
(no output -- permissions updated)
```

```bash
~/tmux-agent-monitor.sh
```

**Output:**
```
[A 3-pane tmux session appears:
 Left: "=== Agent Process ===" with timestamp
 Right-top: "=== System Monitor ===" with top running
 Right-bottom: "=== Log Watcher ===" waiting for input]
```

### Verify the Layout

From another terminal (or detach with `Ctrl+b`, `d` first):

```bash
tmux list-panes -t agent-monitor
```

**Output:**
```
0: [80x44] [history 2/2000] [flags=]
1: [81x22] [history 3/2000] [flags=]
2: [81x21] [history 1/2000] [flags=*]
```

Three panes, created automatically from your script. Run this script on any server and get the exact same layout every time.

## Quick Reference: Essential tmux Commands

| Action | Key/Command |
|--------|-------------|
| **Sessions** | |
| Create named session | `tmux new-session -s name` |
| Detach | `Ctrl+b`, `d` |
| List sessions | `tmux ls` |
| Attach | `tmux attach -t name` |
| Switch sessions | `Ctrl+b`, `s` |
| Kill session | `tmux kill-session -t name` |
| **Panes** | |
| Split vertical | `Ctrl+b`, `%` |
| Split horizontal | `Ctrl+b`, `"` |
| Navigate panes | `Ctrl+b`, arrow key |
| Cycle panes | `Ctrl+b`, `o` |
| Close pane | `exit` or `Ctrl+d` |
| **Windows** | |
| New window | `Ctrl+b`, `c` |
| Next window | `Ctrl+b`, `n` |
| Previous window | `Ctrl+b`, `p` |
| Rename window | `Ctrl+b`, `,` |
| List windows | `Ctrl+b`, `w` |
| **Copy Mode** | |
| Enter copy mode | `Ctrl+b`, `[` |
| Search forward | `/` then search term |
| Exit copy mode | `q` or `Escape` |

## Safety Note

**Detaching vs closing**: Always detach from tmux sessions with `Ctrl+b`, `d` before closing your terminal window. Closing the terminal without detaching may work -- tmux tries to handle this gracefully -- but explicit detachment is the reliable habit.

**Session cleanup**: Forgotten sessions consume server memory. Periodically run `tmux ls` and kill sessions you no longer need with `tmux kill-session -t name`. On shared servers, abandoned sessions also confuse other administrators.

## Exercises

### Exercise 1: Create a Multi-Pane Monitoring Layout

**Task:** Create a tmux session named `agent-monitor` and split it into 3 panes.

```bash
tmux new-session -d -s agent-monitor
tmux split-window -h -t agent-monitor
tmux split-window -v -t agent-monitor
```

**Verify:**

```bash
tmux list-panes -t agent-monitor | wc -l
```

**Output:**
```
3
```

Three panes created and verified.

### Exercise 2: Detach and Reattach

**Task:** Attach to your `agent-monitor` session, start a process in one pane, detach, then reattach and confirm everything persisted.

```bash
tmux attach -t agent-monitor
```

Inside the session, run a long command in any pane:

```bash
while true; do echo "$(date): Agent running"; sleep 5; done
```

Detach: `Ctrl+b`, `d`

**Verify the session still exists:**

```bash
tmux ls
```

**Output:**
```
agent-monitor: 3 windows (created Sun Feb  9 15:45:00 2026)
```

Reattach:

```bash
tmux attach -t agent-monitor
```

**Verify:** The process is still printing timestamps. All 3 panes are intact.

### Exercise 3: Write and Run a Session Script

**Task:** Write a session script that creates your preferred layout with a custom session name.

```bash
nano ~/my-workspace.sh
```

Write a script that creates a session with at least 2 panes and sends a command to each pane (use the session script section above as a template).

Make it executable and run it:

```bash
chmod +x ~/my-workspace.sh && ~/my-workspace.sh
```

**Verify** (from another terminal or after detaching):

```bash
tmux ls | grep my-workspace
```

**Output:**
```
my-workspace: 1 windows (created Sun Feb  9 15:50:00 2026)
```

Your script created the session. Run it on any machine for the same layout.

## Try With AI

You have the fundamentals of tmux sessions, panes, windows, and scripts. Now use AI to design workflows tailored to your specific agent management needs.

```
I manage 3 AI agents that each need monitoring: application logs,
resource usage, and health checks. Design a tmux session layout
that lets me monitor all 3 simultaneously. Show me the complete
session script I can save and run.
```

**What you're learning:** AI suggests monitoring patterns you may not have considered -- such as organizing panes by function (all logs together) versus by agent (each agent's tools grouped). The layout it proposes combines tmux commands from this lesson with monitoring commands from earlier lessons.

```
Copy the session script Claude generated. Now tell Claude:
"This layout needs adjustment -- I also need a pane for editing
config files with nano, and the log panes should be smaller since
I mostly glance at them. Compare the original and updated versions."
```

**What you're learning:** Refining AI output by adding your specific workspace constraints produces a better result than the generic first draft. You know how you actually work -- AI does not -- and translating that knowledge into concrete requirements improves the output.

```
Take your final tmux script and ask Claude: "Review this script
for edge cases. What happens if a session with this name already
exists? What if one of the log files doesn't exist yet? What if
tmux isn't installed? Add error handling for each case."
```

**What you're learning:** Iterative review catches problems that neither you nor AI considered in the initial design. Error handling transforms a working script into a production-ready script -- the difference between a tool that works on your machine and one that works on any server.
