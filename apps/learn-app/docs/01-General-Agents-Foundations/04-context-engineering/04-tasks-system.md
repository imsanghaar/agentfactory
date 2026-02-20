---
sidebar_position: 4
title: "The Tasks System: Persistent State for Context Management"
description: "How Claude Code's native Tasks system enables aggressive context management through filesystem-backed persistent state"
keywords:
  [
    "Tasks",
    "TaskCreate",
    "TaskUpdate",
    "TaskList",
    "context management",
    "persistent state",
    "DAG",
    "dependency graph",
    "cross-session coordination",
    "CLAUDE_CODE_TASK_LIST_ID",
  ]
chapter: 4
lesson: 4
duration_minutes: 25

# HIDDEN SKILLS METADATA
skills:
  - name: "Understanding Tasks as Context Engineering"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain why filesystem persistence enables aggressive context clearing without losing project state"

  - name: "Using Task Dependencies"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can create tasks with blockedBy relationships to represent work dependencies"

  - name: "Designing Multi-Session Workflows"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Communication"
    measurable_at_this_level: "Student can design task-based workflows that coordinate across multiple sessions or agents"

learning_objectives:
  - objective: "Explain why filesystem-backed Tasks enable aggressive context management"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student can articulate the relationship between plan-on-disk and context clearing"

  - objective: "Create tasks with dependency relationships by describing them to Claude"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student demonstrates creating a task DAG with blockedBy relationships"

  - objective: "Design a cross-session workflow using CLAUDE_CODE_TASK_LIST_ID"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Student configures two sessions to share the same task list"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (Tasks vs ephemeral state, filesystem persistence, dependency DAGs, context-clearing freedom, cross-session coordination) appropriate for B1"

differentiation:
  extension_for_advanced: "Design a Writer/Reviewer pattern with two sessions using shared task coordination"
  remedial_for_struggling: "Focus on the core insight first (plan on disk = context freedom), then the mechanics"

teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "Persistent State and Knowledge Transfer"
  key_points:
    - "The core insight is plan-on-disk enables context freedom — /clear destroys conversation but Tasks survive because they live in ~/.claude/tasks/, not in context"
    - "Task dependencies form DAGs (Directed Acyclic Graphs) — completing a blocking task automatically unblocks dependents, enabling wave-based execution"
    - "Cross-session coordination via CLAUDE_CODE_TASK_LIST_ID enables parallel workflows like Writer/Reviewer patterns across multiple terminals"
    - "Tasks track WHAT needs doing (action items), while progress files (lesson 07) track WHY (decisions and discoveries) — students need both"
  misconceptions:
    - "Students think /clear destroys their work — emphasize that Tasks survive because they are files on disk, not conversation state"
    - "Students confuse Tasks with simple todo lists — Tasks have dependency graphs, cross-session sharing, and automatic unblocking that make them a coordination system"
    - "Students try to call TaskCreate/TaskUpdate directly — they should describe what they need in natural language and let Claude handle the internal tool calls"
  discussion_prompts:
    - "Think of a multi-step project in your domain — what would the dependency graph look like? Which tasks could run in parallel?"
    - "Why is the plan-clear-execute pattern better than trying to keep everything in context and hoping quality doesn't degrade?"
  teaching_tips:
    - "Start with the opening scenario — every student has experienced losing their plan after /clear, so the problem resonates immediately"
    - "The DAG diagram (Tasks 1-4 with arrows) is worth drawing on a whiteboard — have students trace the execution order"
    - "Have students do the lab step-by-step: create tasks, run /clear, then verify tasks survived — the 'aha' moment happens when they see persistence firsthand"
    - "The domain-specific examples (legal due diligence, marketing campaign, research synthesis) help non-technical students see relevance"
  assessment_quick_check:
    - "Where do Tasks physically live, and why does this matter for /clear?"
    - "Draw a simple 4-task dependency graph and explain which tasks can run in parallel"
    - "What is CLAUDE_CODE_TASK_LIST_ID and what does it enable?"
---

# The Tasks System: Persistent State for Context Management

You're deep in a complex refactoring project. You've built a mental map of what needs to happen: fix the authentication module, then update the user service that depends on it, then run the integration tests. Claude knows this plan too. You've discussed it. It's all in context.

Then you hit the wall. Context is at 80%. Quality is degrading. You need to run `/clear`.

And the plan vanishes.

This is the ephemeral state problem. Your project roadmap lived only in the conversation. Clear the context, lose the roadmap.

Claude Code's Tasks system solves this. **Tasks are filesystem-backed persistent state.** Your plan lives on disk, not in context. Clear freely. The roadmap survives.

## The Old Problem: Ephemeral Todos

Before Tasks, Claude Code had Todos. You might have seen them in the sidebar: an orange sticky-note icon. They helped Claude remember what to do during a session.

The problem: Todos lived in the chat. When you ran `/clear` or `/compact`, they could disappear along with your conversation history. The plan existed only as long as the context existed.

| Aspect               | Old Todos       | New Tasks                          |
| -------------------- | --------------- | ---------------------------------- |
| **Storage**          | In conversation | On filesystem (`~/.claude/tasks/`) |
| **Survives /clear**  | No              | Yes                                |
| **Survives crashes** | No              | Yes                                |
| **Cross-session**    | No              | Yes (with environment variable)    |
| **Dependencies**     | No              | Yes (blockedBy, addBlocks)         |

This isn't a small upgrade. It's a paradigm shift in how plans relate to context.

## The Core Insight: Plan on Disk Enables Context Freedom

Here's the key insight, directly from the VentureBeat analysis of this feature:

> "Because the plan is stored on disk, users can run /clear or /compact to free up tokens for the model's reasoning, without losing the project roadmap."

This is context engineering in action. You've learned that context fills up and quality degrades. You've learned about the attention budget and position sensitivity. Now you have a tool that **decouples your plan from your context**.

**Before Tasks:**

- Plan lives in context
- Context fills up
- Can't clear without losing plan
- Quality degrades as you work

**After Tasks:**

- Plan lives on disk
- Context fills up
- Clear freely, plan persists
- Quality stays high through aggressive context management

## How You Work With Tasks

You interact with tasks by talking to Claude. Claude uses internal tools (TaskCreate, TaskUpdate, TaskList, TaskGet) behind the scenes—you don't call these directly.

### Creating Tasks

**What you say:**

```
Create a task to review the vendor contract. It should include extracting
key terms and identifying liability provisions.
```

**What Claude does internally:** Uses TaskCreate to store the task with a subject, description, and status.

**What you see:** The task appears in your task list (press `Ctrl+T` to toggle the view).

### Viewing Tasks

**What you say:**

```
Show me the current tasks.
```

or

```
What's available to work on?
```

**What you see:**

```
#1 [completed] Extract key contract terms
#2 [in_progress] Identify liability provisions [blocked by #1]
#3 [pending] Draft recommendations [blocked by #1, #2]
```

**A task is "available" when:**

1. Status is `pending` (not started yet)
2. No one is working on it
3. All its dependencies are complete (blockedBy list is empty)

### Setting Up Dependencies

**What you say:**

```
I need to review the contract, identify liability issues, compare to our
standard terms, and draft recommendations. Create tasks with dependencies.
```

Claude breaks this into discrete tasks and wires up the dependencies so tasks become available only when their prerequisites complete.

### Completing Tasks

**What you say:**

```
Mark task 1 as complete.
```

or Claude marks it complete automatically after finishing the work.

**What happens:** Task 1 moves to `completed`. Tasks 2 and 3 (which were blocked by #1) automatically become available.

### CLI Shortcuts

- **`Ctrl+T`**: Toggle the task list view in your terminal (shows up to 10 tasks)
- **Just ask**: "Show me all tasks", "Clear all tasks", or "What's next?"

## Why Tasks Survive /clear

Tasks are stored as files in `~/.claude/tasks/`, not in your conversation. That's why they persist when you clear context—they're on disk, not in memory.

## Dependency Graphs: Task DAGs

Tasks support **Directed Acyclic Graphs (DAGs)**. Task 3 can be blocked by Tasks 1 and 2. When both complete, Task 3 automatically becomes available.

This is powerful for complex projects:

```
┌─────────────────┐
│  1: Fix Auth    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│ 2: User Service │     │ 4: Admin Panel  │
└────────┬────────┘     └────────┬────────┘
         │                       │
         ▼                       │
┌─────────────────┐              │
│ 3: Integration  │◄─────────────┘
│    Tests        │
└─────────────────┘
```

Task 3 (integration tests) is blocked by Tasks 2 and 4. Both must complete before testing can begin.

**How you'd set this up:**

```
I need to fix authentication, update the user service and admin panel,
then run integration tests. The user service depends on auth being fixed.
Create tasks with the right dependencies.
```

Claude handles the internal mechanics—creating the tasks and wiring up the dependency graph. You describe WHAT you need; Claude figures out HOW to structure it.

## What Filesystem Persistence Means for You

Because tasks live on disk (`~/.claude/tasks/`), you get three benefits:

**1. Crash Recovery**: If your terminal crashes, your tasks persist. Resume your session, ask "What tasks do we have?", and continue where you left off.

**2. Session Independence**: Tasks don't consume context tokens. A 50-task project plan uses zero tokens in your conversation—it's all on disk.

**3. Clear Freely**: Run `/clear` whenever context fills up. Your roadmap survives because it was never in context to begin with.

## The Pattern: Plan, Clear, Execute

Armed with Tasks, here's the pattern for long-running work:

**Phase 1: Plan**
Create tasks at the beginning of a work session when context is fresh:

```
I need to review this contract and prepare negotiation recommendations.
Create a task plan with dependencies.
```

Claude breaks this into discrete tasks (extract terms, identify provisions, flag issues, cross-reference, draft recommendations) and sets up the dependency chain automatically.

**Phase 2: Clear**
When context fills up (60-80%), clear aggressively:

```
/clear
```

Your plan survives. The 6-task roadmap persists on disk.

**Phase 3: Execute**
After clearing, check what's available and continue:

```
What's next?
```

Claude checks the task list, finds which tasks are unblocked, and continues execution.

**The key insight**: You're not losing information when you clear. You're freeing context for reasoning while your strategic plan persists.

## Real-World Example: Multi-Phase Projects

Here's how Tasks enable complex projects across different domains:

**Legal: Due Diligence Review**

```
Task plan:
├── Task 1: Extract key terms from all contracts (no blockers)
├── Task 2: Identify liability provisions (blocked by #1)
├── Task 3: Flag regulatory compliance issues (blocked by #1)
├── Task 4: Cross-reference findings (blocked by #2, #3)
├── Task 5: Draft executive summary (blocked by #4)
```

**Marketing: Campaign Development**

```
Task plan:
├── Task 1: Analyze competitor positioning (no blockers)
├── Task 2: Define target personas (no blockers)
├── Task 3: Develop messaging framework (blocked by #1, #2)
├── Task 4: Create channel strategy (blocked by #3)
├── Task 5: Draft creative briefs (blocked by #3, #4)
```

**Research: Literature Synthesis**

```
Task plan:
├── Task 1: Search and gather sources (no blockers)
├── Task 2: Extract methodology patterns (blocked by #1)
├── Task 3: Identify key findings (blocked by #1)
├── Task 4: Map contradictions and debates (blocked by #2, #3)
├── Task 5: Draft synthesis narrative (blocked by #4)
```

**How execution flows:**

1. **Wave 1**: Independent tasks run (no blockers)
2. **Wave 2**: Tasks that only needed Wave 1 become available, can run in parallel
3. **Wave 3**: Synthesis tasks run after their dependencies complete
4. **Continue**: Each completed task automatically unblocks dependents

**Why this works**: Each task runs with focused context. The agent drafting the executive summary doesn't inherit the noise from analyzing 50 contracts—it gets the cross-referenced findings and writes clearly. Context stays clean at every stage.

This is the pattern: **plan → clear → delegate → synthesize**. The task system manages the coordination. You focus on the work.

## Cross-Session Coordination

For team workflows or parallel execution, multiple sessions can share the same task list using the `CLAUDE_CODE_TASK_LIST_ID` environment variable.

**Terminal A (Writer)**:

```bash
CLAUDE_CODE_TASK_LIST_ID=project-alpha claude
```

**Terminal B (Reviewer)**:

```bash
CLAUDE_CODE_TASK_LIST_ID=project-alpha claude
```

Both sessions now see the same tasks. When Writer marks a task complete, Reviewer sees it update. When Reviewer creates a feedback task, Writer sees it appear.

**The Writer/Reviewer Pattern**:

1. Session A writes code, marks `implement-feature` complete
2. System creates `review-feature` task blocked by `implement-feature`
3. When `implement-feature` completes, `review-feature` becomes available
4. Session B picks up `review-feature`, provides feedback
5. If issues found, Session B creates `fix-issues` task
6. Session A picks up `fix-issues`, continues work

This enables **parallel execution with coordination**. No stepping on each other's work. No duplicate effort. The task system manages handoffs.

## Tasks vs. Progress Files

You might wonder: "How are Tasks different from the progress files we'll learn about later in this chapter?"

| Aspect            | Tasks                           | Progress Files                    |
| ----------------- | ------------------------------- | --------------------------------- |
| **Purpose**       | Track what needs to be done     | Track what has been learned       |
| **Scope**         | Action items and dependencies   | Decisions, context, discoveries   |
| **Persistence**   | Automatic (via tools)           | Manual (you write them)           |
| **Cross-session** | Built-in (environment variable) | Manual (git or shared filesystem) |

**Use both together**: Tasks track the WHAT (action items). Progress files track the WHY (decisions and discoveries). Tasks tell you what to do next. Progress files tell you what you've learned along the way.

## Lab: Building a Task-Managed Workflow

**Objective:** Experience the plan-clear-execute pattern with real work.

**Setup:**

1. Choose a multi-step task in your domain (refactoring, content creation, analysis)
2. Start a fresh Claude Code session

**Protocol:**

**Step 1: Plan with Dependencies**

Ask Claude to create a task plan:

```
I need to [describe your project goal]. Create a task plan with dependencies.
```

Verify by pressing `Ctrl+T` or asking "Show me the tasks."

**Step 2: Work Until Context Fills**

Execute tasks until you notice quality degradation (typically 60-80% context usage).

Check with `/context`.

**Step 3: Clear and Verify**

Run `/clear`.

Then immediately ask: "What tasks do we have?" (or press `Ctrl+T`).

**Observation:** Your plan survived the clear. Your strategic roadmap persists even though your conversation history is gone.

**Step 4: Continue Execution**

Ask Claude to continue:

```
What's next? Let's keep going.
```

**Expected Finding:** The workflow continues seamlessly despite the context clear. This is the power of filesystem-backed state.

## What You Learned

1. **Tasks are filesystem-backed**: They live in `~/.claude/tasks/{session-id}/`, not in your conversation
2. **Plan on disk enables context freedom**: You can `/clear` aggressively without losing your roadmap
3. **Talk to Claude, not tools**: You describe what you need; Claude handles task creation and dependency wiring
4. **Dependencies form DAGs**: Tasks can block other tasks, automatically managing execution order
5. **Cross-session coordination**: `CLAUDE_CODE_TASK_LIST_ID` lets multiple sessions share task state
6. **CLI access**: Press `Ctrl+T` to toggle task view, or just ask Claude

## Try With AI

### Prompt 1: Create a Task Plan

Choose a project from your domain:

**Legal:**

```
I need to review a vendor contract and prepare negotiation recommendations.
Create a task plan with proper dependencies.
```

**Marketing:**

```
I need to develop a product launch strategy from competitive analysis
through launch timeline. Create a task plan with proper dependencies.
```

**Research:**

```
I need to write a literature review on [your topic]. Create a task plan
that takes me from source gathering through the final synthesis.
```

**What you're learning:** Notice how Claude breaks down your goal into discrete tasks and figures out which ones depend on others. You describe the outcome; Claude handles the structure.

**After Claude creates the tasks:** Press `Ctrl+T` to see them in your terminal.

### Prompt 2: Test Persistence

```
Show me the tasks.
```

Then run `/clear` in your terminal. After clearing:

```
Show me the tasks again.
```

**What you're learning:** Your tasks survived because they're on disk, not in context. You just freed your entire context window while keeping your project roadmap intact.

### Prompt 3: Complete a Task

```
Mark the first task as done and show me what's now available.
```

**What you're learning:** When a blocking task completes, dependent tasks automatically become available. This is the DAG in action—no manual coordination needed.

### Prompt 4: Cross-Session Setup (Advanced)

```
How do I share tasks between two terminal sessions?
```

**What you're learning:** Claude will explain the `CLAUDE_CODE_TASK_LIST_ID` pattern. Try it yourself:

```bash
# Terminal 1
CLAUDE_CODE_TASK_LIST_ID=my-project claude

# Terminal 2 (different window)
CLAUDE_CODE_TASK_LIST_ID=my-project claude
```

Both sessions now share the same task list.
