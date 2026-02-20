---
slug: /General-Agents-Foundations/general-agents/hooks-and-extensibility
title: "Hooks: Event-Driven Automation"
sidebar_position: 15
chapter: 3
lesson: 15
duration_minutes: 12

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration)"
layer_1_foundation: "N/A"
layer_2_collaboration: "AI helps design hooks for specific workflows, student provides context about automation needs"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Implementing Event-Driven Automation with Hooks"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can configure hooks in settings.json, understand hook events, and create simple hook scripts"

learning_objectives:
  - objective: "Understand hooks as event-triggered automation"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explanation of when each hook type fires"
  - objective: "Configure hooks in settings.json"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Creation of working hook configuration"
  - objective: "Recognize the five main hook events"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Identification of appropriate hook events for automation scenarios"
  - objective: "Create a simple hook script"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Creation of hook script that receives JSON and produces output"

# Cognitive load tracking
cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (hook definition, event types, settings.json config, matcher patterns, stdin/stdout pattern) - within B1 limit of 10 ✓"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Create PreToolUse validation hooks; design permission auto-approval workflows"
  remedial_for_struggling: "Start with SessionStart hook that prints a message; understand events before writing scripts"

# Generation metadata
generated_by: "content-implementer v1.0.0"
source_spec: "specs/029-chapter-5-refinement/spec.md"
created: "2025-01-17"
last_modified: "2026-01-19"
git_author: "Claude Code"
workflow: "/sp.implement"
version: "3.0.0"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 5
  session_title: "Settings, Hooks, and Plugin Synthesis"
  key_points:
    - "Hooks guarantee behavior that CLAUDE.md only suggests — the shift from 'Claude might forget' to 'it always happens' is the core insight"
    - "The five hook events (PreToolUse, PostToolUse, UserPromptSubmit, SessionStart, SessionEnd) each fire at a different lifecycle point — students must know WHEN, not just WHAT"
    - "Exit code 2 blocks the action while exit code 0 allows it — this is the mechanism for building safety guardrails"
    - "Hooks receive JSON via stdin and produce output via stdout — the stdin/stdout pattern is how all hook scripts communicate with Claude Code"
  misconceptions:
    - "Students confuse PreToolUse (fires before the tool runs, can block it) with PostToolUse (fires after, can only react) — leads to hooks that log instead of prevent"
    - "Students think hooks replace CLAUDE.md instructions — hooks enforce mechanical rules while CLAUDE.md provides contextual guidance; they complement each other"
    - "Students forget that hook scripts need executable permissions (chmod +x) — the most common reason a hook 'doesn't work'"
  discussion_prompts:
    - "What repetitive task do you currently rely on Claude to remember? How would encoding it as a hook change your confidence in the outcome?"
    - "When would a PreToolUse hook that blocks an action be better than a CLAUDE.md rule that asks Claude not to do it?"
    - "If you could add one hook to your daily workflow right now, which event would you choose and what would the hook do?"
  teaching_tips:
    - "Start with the 'Your First Hook' exercise (logging Bash commands) — it is the simplest end-to-end example and builds confidence before complex hooks"
    - "Use the five-event table as a quick reference card; have students match real scenarios to events before showing configurations"
    - "When demonstrating the UserPromptSubmit hook example, show the JSON input format first so students understand what data their script receives"
    - "Pair this lesson with Exercise 2.1 from Lesson 19 immediately — the hands-on reinforcement is designed to follow this lesson directly"
  assessment_quick_check:
    - "Which hook event fires when Claude is about to run a Bash command, and what exit code would you use to block it?"
    - "What does a hook script receive as input and how does it produce output?"
    - "Name one task that a PostToolUse hook on Write|Edit could automate after every file change"

# Legacy compatibility
prerequisites:
  - "Lessons 01-14: Claude Code features, skills, subagents, settings"
---

# Hooks: Event-Driven Automation

**Hooks are your commands that run automatically when Claude does something.**

- Claude edits a file → your formatting command runs
- Claude runs a bash command → your logging command runs
- You submit a prompt → your context injection runs
- Session starts → your setup script runs

**Why this matters**: You can _tell_ Claude "always format code after editing"—but it might forget. A hook _guarantees_ it happens every time, because it's your code running automatically, not Claude choosing to run it.

---

## Why Hooks?

**Without hooks**, you hope Claude remembers to:

- Format code after editing
- Run tests after changes
- Follow your naming conventions
- Avoid touching sensitive files

**With hooks**, you **guarantee** these happen:

- `PostToolUse` hook runs Prettier after every file edit
- `PreToolUse` hook blocks edits to `.env` files
- `SessionStart` hook loads project context automatically
- `Notification` hook sends Slack alerts when Claude needs input

**The key insight**: By encoding rules as hooks instead of prompting instructions, you turn suggestions into **app-level code** that executes every time.

---

## The Five Main Hook Events

| Event                | When It Fires            | Common Use Cases                                             |
| -------------------- | ------------------------ | ------------------------------------------------------------ |
| **PreToolUse**       | Before a tool runs       | Validate commands, block dangerous operations, modify inputs |
| **PostToolUse**      | After a tool completes   | Format code, run tests, log activity                         |
| **UserPromptSubmit** | When you submit a prompt | Add context, validate input, inject system info              |
| **SessionStart**     | When Claude Code starts  | Load environment variables, show project info                |
| **SessionEnd**       | When session closes      | Cleanup, save logs                                           |

There are also advanced events (`Stop`, `SubagentStop`, `PermissionRequest`, `Notification`) for specialized workflows.

---

## How Hooks Work

```
Event fires → Hook script runs → Script output affects Claude
```

**The pattern**:

1. An event occurs (e.g., you submit a prompt)
2. Claude Code runs your hook script
3. Script receives **JSON input via stdin**
4. Script produces **output via stdout**
5. Output gets injected into Claude's context

**Exit codes matter**:

- `0` = Success (stdout processed)
- `2` = Block the action (show error)
- Other = Non-blocking warning

---

## Configuring Hooks

### Option 1: Use the /hooks Command (Easiest)

Run:

```
/hooks
```

This opens an interactive menu where you:

1. Select an event (PreToolUse, PostToolUse, etc.)
2. Add a matcher (which tools to match)
3. Add your hook command
4. Choose storage location (User or Project)

### Option 2: Edit settings.json Directly

Hooks are configured in `.claude/settings.json`:

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/your-script.sh"
          }
        ]
      }
    ]
  }
}
```

**Key fields**:

- `EventName`: Which event triggers this (`PreToolUse`, `PostToolUse`, etc.)
- `matcher`: Which tools to match (e.g., `Bash`, `Write`, `Edit`, `Read`)
- `command`: The script to run

### Matcher Patterns

| Pattern         | Matches                    |
| --------------- | -------------------------- |
| `"Bash"`        | Only Bash tool             |
| `"Write\|Edit"` | Write OR Edit tools        |
| `"Notebook.*"`  | All Notebook tools         |
| `""` or omit    | All tools (for that event) |

---

## Try It Now: Your First Hook

Let's log every Bash command Claude runs.

**Prerequisite**: Install `jq` for JSON processing (`brew install jq` on macOS, `apt install jq` on Linux).

### Method 1: Using /hooks (Quickest)

1. Run `/hooks` in Claude Code
2. Select `PreToolUse`
3. Add matcher: `Bash`
4. Add hook command:
   ```bash
   jq -r '"\(.tool_input.command) - \(.tool_input.description // "No description")"' >> ~/.claude/bash-log.txt
   ```
5. Choose `User settings` for storage
6. Press `Esc` to save

Now ask Claude to run `ls` and check your log:

```bash
cat ~/.claude/bash-log.txt
```

### Method 2: Edit settings.json Directly

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"\\(.tool_input.command) - \\(.tool_input.description // \"No description\")\"' >> ~/.claude/bash-log.txt"
          }
        ]
      }
    ]
  }
}
```

Restart Claude Code and test it.

---

## Real Example: UserPromptSubmit Hook

Here's a real hook that tracks prompts (from this book's codebase):

**Script** (`.claude/hooks/track-prompt.sh`):

```bash
#!/usr/bin/env bash
# Track user prompt submissions

# Read JSON input from stdin
INPUT=$(cat)

# Parse the prompt field
PROMPT=$(echo "$INPUT" | jq -r '.prompt // empty')

# Skip if no prompt
[ -z "$PROMPT" ] && exit 0

# Log it
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
echo "{\"timestamp\": \"$TIMESTAMP\", \"prompt\": \"$PROMPT\"}" >> .claude/activity-logs/prompts.jsonl

exit 0
```

**Configuration**:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/track-prompt.sh"
          }
        ]
      }
    ]
  }
}
```

**What happens**:

1. You submit a prompt
2. Hook receives JSON: `{"prompt": "your message", "session_id": "..."}`
3. Script extracts prompt, logs it with timestamp
4. Session continues normally

---

## Real Example: PreToolUse Hook

Track when skills are invoked:

**Configuration**:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Skill",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/track-skill-invoke.sh"
          }
        ]
      }
    ]
  }
}
```

**What this does**:

- Fires **before** the Skill tool runs
- Only matches the `Skill` tool (not Bash, Write, etc.)
- Can log, validate, or modify the tool call

---

## Real Example: PostToolUse Hook

Track subagent results:

**Configuration**:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Task",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/track-subagent-result.sh"
          }
        ]
      }
    ]
  }
}
```

**What this does**:

- Fires **after** the Task tool completes
- Receives the task result in JSON input
- Can log, analyze, or trigger follow-up actions

---

## Hook Input Format

All hooks receive JSON via stdin. Common fields:

```json
{
  "session_id": "abc123",
  "cwd": "/path/to/project",
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": {
    "command": "npm test",
    "description": "Run tests"
  }
}
```

**Event-specific fields**:

- `UserPromptSubmit`: `{"prompt": "user's message"}`
- `PreToolUse/PostToolUse`: `{"tool_name": "...", "tool_input": {...}}`
- `SessionStart`: Basic session info

---

## Hook Output Format

**Simple**: Just print text to stdout:

```bash
echo "Current time: $(date)"
exit 0
```

**Advanced**: Output JSON for more control:

```bash
echo '{"decision": "allow", "reason": "Auto-approved"}'
exit 0
```

**Block an action**:

```bash
echo "Blocked: dangerous command" >&2
exit 2
```

---

## Combining Multiple Hooks

You can have multiple hooks for the same event:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/validate-bash.sh"
          }
        ]
      },
      {
        "matcher": "Write|Edit",
        "hooks": [
          { "type": "command", "command": "bash .claude/hooks/check-files.sh" }
        ]
      }
    ]
  }
}
```

Different matchers trigger different scripts based on which tool is used.

---

## Debugging Hooks

If hooks aren't working:

1. **Check the script is executable**: `chmod +x .claude/hooks/your-script.sh`
2. **Test manually**: `echo '{"test": "data"}' | bash .claude/hooks/your-script.sh`
3. **Check settings.json syntax**: Valid JSON? Correct structure?
4. **Use debug mode**: `claude --debug` shows hook execution

---

## Where Hooks Live

```
.claude/
├── settings.json      # Hook configuration
└── hooks/             # Hook scripts
    ├── _common.sh     # Shared utilities (optional)
    ├── session-info.sh
    ├── track-prompt.sh
    └── validate-bash.sh
```

**Tip**: Use a `_common.sh` file for shared functions like JSON parsing.

---

### What's Next

Lesson 16 introduces **Plugins**—pre-packaged bundles of skills, hooks, agents, and MCP servers that you can install from marketplaces. Where hooks let you customize Claude Code's behavior, plugins let you install complete capability packages built by others.

---

## Try With AI

**📝 Create a Simple Hook:**

> "Help me create a SessionStart hook that shows the git branch and last commit message when I start Claude Code. Walk me through: the script, the settings.json config, and how to test it."

**What you're learning:** The complete hook lifecycle—from script to configuration to testing. This pattern applies to all hook types.

**🔍 Understand Hook Events:**

> "I want to automatically run prettier after Claude edits a JavaScript file. Which hook event should I use? What would the matcher be? Show me the complete configuration."

**What you're learning:** Event selection and pattern matching—choosing the right trigger and scope for automated behavior.

**🛡️ Validation Hook:**

> "Help me create a PreToolUse hook that warns me before Claude runs any command with 'rm' or 'delete' in it. The hook should print a warning but not block the command."

**What you're learning:** Safety guardrails through hooks—implementing "soft" warnings that inform without blocking, a pattern used in production systems.

**📊 Logging Hook:**

> "I want to log all the tools Claude uses during a session. Help me create a PostToolUse hook that appends tool names and timestamps to a log file."

**What you're learning:** Observability through hooks—instrumenting AI behavior for debugging and analysis. This is how production systems gain visibility.

**🔧 Debug a Hook:**

> "My hook isn't running. Help me debug: How do I test the script manually? How do I check if settings.json is correct? What does claude --debug show?"

**What you're learning:** Hook debugging methodology—the systematic approach when automation doesn't work. This skill saves significant debugging time.
