---
sidebar_position: 7
title: "Phase 4: Task-Based Implementation"
description: "Transform specifications into parallel work streams using Claude Code's task system where subagents execute with context isolation and atomic commits"
keywords:
  [
    "spec-driven development",
    "task-based implementation",
    "subagents",
    "context isolation",
    "parallel execution",
    "atomic commits",
    "pre-commit hooks",
    "backpressure",
    "task system",
  ]
chapter: 5
lesson: 7
duration_minutes: 35

# HIDDEN SKILLS METADATA
skills:
  - name: "Apply Task-Based Implementation Pattern"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can invoke the task pattern prompt and observe subagent delegation in action"

  - name: "Explain Context Isolation Benefits"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can articulate why fresh context per task prevents error propagation"

  - name: "Configure Backpressure Mechanisms"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can set up pre-commit hooks that validate work before it enters the codebase"

  - name: "Analyze Task Dependencies"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify which tasks can run in parallel vs which must be sequential"

learning_objectives:
  - objective: "Apply the task-based implementation prompt pattern to transform specifications into parallel work streams"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student successfully invokes the pattern and observes task delegation"

  - objective: "Explain why context isolation prevents error propagation across implementation tasks"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can articulate the contamination problem and isolation solution"

  - objective: "Configure pre-commit hooks as backpressure mechanisms that validate work quality"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates a working pre-commit configuration"

  - objective: "Analyze task dependencies to identify parallel vs sequential execution requirements"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student can diagram task dependencies for a given specification"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (task system, subagent delegation, context isolation, atomic commits, backpressure, pre-commit hooks) within B1 range"

differentiation:
  extension_for_advanced: "Design custom task dependency graphs with conditional execution paths based on intermediate results"
  remedial_for_struggling: "Focus on the core prompt pattern first, then gradually introduce context isolation and backpressure concepts"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 3
  session_title: "Implementation and Judgment"
  key_points:
    - "The core prompt ('You are the main agent and your subagents are your devs') transforms Claude from solo coder to orchestrated development team"
    - "Context isolation solves two named problems: Agent Amnesia (progress lost on restart) and Context Pollution (accumulated errors contaminate later work)"
    - "Atomic commits per task create rollback boundaries — if task 7 fails, tasks 1-6 are safely committed"
    - "Backpressure via pre-commit hooks ensures even AI-written code passes quality gates before entering the repository"
  misconceptions:
    - "Students think subagents share context with the main agent — each subagent starts completely fresh, which is the entire point"
    - "Students assume more tasks means better decomposition — tasks should be 5-15 minutes each; too granular creates coordination overhead"
    - "Students think task-based implementation is always better — for a two-line bug fix, the overhead of task extraction isn't justified"
  discussion_prompts:
    - "Looking at the alexop.dev results (14 tasks, 45 minutes, 0 rollbacks), what would have happened in a single-session approach if task 10 introduced a bug?"
    - "When does the overhead of task extraction and subagent coordination NOT pay off?"
  teaching_tips:
    - "The contamination timeline (minute 10 assumption → minute 55 failure) vs isolation timeline is the best visual to draw on the whiteboard"
    - "Have students set up a real pre-commit hook with husky — the hands-on experience of seeing a commit rejected is memorable"
    - "The alexop.dev results table is concrete proof — 14 commits in 45 minutes with zero rollbacks makes the pattern real"
    - "Walk through the dependency graph drawing exercise from the lab — students need to see parallel vs sequential visually"
  assessment_quick_check:
    - "What's the implementation prompt pattern, and what does 'You are the main agent' specifically trigger?"
    - "Explain how atomic commits per task enable surgical rollbacks that single-session implementation cannot"
---

# Phase 4: Task-Based Implementation

"You are the main agent and your subagents are your devs."

This single prompt transforms Claude from a solo coder into a development team. In Lesson 5, you refined your specification through interview until ambiguities disappeared. Now you have a spec precise enough that implementation becomes execution of a well-understood plan.

But here's the problem: even with a perfect spec, a single AI context accumulates errors. Decisions made in minute 5 affect code written in minute 45. A wrong assumption early contaminates everything downstream. And when something breaks after an hour of work, you're left debugging a massive context with no clear rollback point.

Task-based implementation solves this. Instead of one long implementation session, you decompose the spec into independent tasks. Each task executes in a fresh subagent context. Each completed task commits before the next begins. If task 7 fails, tasks 1-6 are safely committed. You roll back only what broke.

## The Core Prompt Pattern

The implementation phase begins with this prompt:

```
Implement @docs/my-spec.md
Use the task tool and each task should only be done by a subagent
so that context is clear. After each task do a commit before you continue.
You are the main agent and your subagents are your devs.
```

This prompt triggers a specific behavior mode in Claude Code. Let's break down what happens.

## What Happens When You Run This

**Step 1: Task Extraction**

Claude reads your specification and extracts the implementation checklist. Each checkbox becomes a task. Dependencies between tasks are identified—some must complete before others can start.

**Step 2: Subagent Delegation**

For each task, Claude spawns a fresh subagent. This subagent receives:

- The specific task description
- Relevant context from the spec
- Access to the codebase state

The subagent does NOT receive the main agent's accumulated conversation history. It starts fresh.

**Step 3: Task Execution and Commit**

The subagent completes its assigned task, then commits the changes with an atomic commit message describing exactly what changed. Control returns to the main agent.

**Step 4: Progress Tracking**

The main agent updates task status and moves to the next task. If a task fails, the main agent can retry, skip, or escalate based on the error.

## The Task System Tools

Claude Code provides four tools for managing this workflow:

| Tool           | Purpose                                                      | When Used                           |
| -------------- | ------------------------------------------------------------ | ----------------------------------- |
| **TaskCreate** | Define a new task with description and dependencies          | Main agent extracts tasks from spec |
| **TaskUpdate** | Change task status (pending, in_progress, completed, failed) | Subagent completes or fails task    |
| **TaskList**   | View all tasks with current status and blockers              | Main agent tracks overall progress  |
| **TaskGet**    | Retrieve full details of a specific task                     | Before starting work on a task      |

The main agent orchestrates. The subagents execute. Tasks provide the coordination layer between them.

## Why Context Isolation Matters

Chapter 4 (Lesson 9) introduced context isolation—why subagents use clean slates. Here we see that principle in action, solving two named problems from the SDD research literature:

**Agent Amnesia**: Starting a new session mid-task loses all progress unless documented. The specification and task list persist across sessions, providing external memory that survives restarts. This is why Phase 2 produces a written spec—it's your insurance against amnesia.

**Context Pollution**: A full context window causes agents to drop discovered bugs instead of tracking them. Fresh subagent context per task prevents accumulated errors from propagating. The Tasks system you learned in Chapter 4 (Lesson 4) enables this—persistent state that coordinates isolated subagents.

Consider what happens without isolation:

```
Minute 10: Main agent makes assumption about data format
Minute 25: Writes validation logic based on assumption
Minute 40: Implements API endpoint using validation
Minute 55: Tests fail - original assumption was wrong
Result: 45 minutes of contaminated work to untangle
```

Now with context isolation:

```
Task 1: Define data schema (subagent 1, commits)
Task 2: Write validation logic (subagent 2, commits)
Task 3: Implement API endpoint (subagent 3, commits)
Task 4: Add tests (subagent 4, fails - schema assumption wrong)
Result: Roll back task 4, fix schema in task 1, tasks 2-3 still valid
```

Each subagent starts with clean context. If it makes a wrong assumption, that assumption dies with the subagent. The contamination doesn't spread to other tasks.

**Parallel execution benefit**: Tasks without dependencies can run simultaneously. Task 2 doesn't need to wait for task 1 if they're independent. The main agent can spawn multiple subagents working in parallel—like a development team where each developer handles their assigned feature.

## The Backpressure Pattern

Fast execution without validation creates a different problem: you might commit broken code faster. The backpressure pattern (inspired by Steve Yegge's "Beads" project) adds quality gates that slow implementation when quality drops.

**Pre-commit hooks** are the primary backpressure mechanism:

```bash
# .husky/pre-commit
pnpm typecheck && pnpm lint && pnpm test-run
```

When a subagent attempts to commit, this hook runs automatically. If typechecking fails, the commit is rejected. If linting fails, the commit is rejected. If tests fail, the commit is rejected.

The subagent must fix the issues before the commit succeeds. This prevents broken code from entering the repository—even when AI is writing it.

**Setting up pre-commit hooks:**

```bash
# Install husky (if using npm/pnpm)
pnpm add -D husky
pnpm exec husky init

# Create the pre-commit hook
echo "pnpm typecheck && pnpm lint && pnpm test-run" > .husky/pre-commit
```

Now every commit—whether from you or from a subagent—must pass the quality gates.

## Real Results: The alexop.dev Implementation

Here's what task-based implementation looks like on a real project (alexop.dev redesign):

| Metric               | Result                  |
| -------------------- | ----------------------- |
| **Total time**       | 45 minutes              |
| **Tasks completed**  | 14                      |
| **Commits made**     | 14 (one per task)       |
| **Context usage**    | 71% of available window |
| **Rollbacks needed** | 0                       |

Each task averaged about 3 minutes. Each commit was atomic and self-contained. The final 29% of context remained available for any follow-up work.

Compare this to a single-session approach: 45 minutes of accumulated context would have consumed nearly the entire window, with no clear rollback points if something broke late in the process.

## When to Use Task-Based Implementation

**Use task-based implementation when:**

- Specification has 5+ distinct implementation items
- Work can be parallelized across independent components
- You need clear rollback boundaries
- Implementation will exceed 30 minutes

**Use simpler approaches when:**

- Specification is small (1-3 items)
- Work is inherently sequential with no parallel opportunities
- Quick prototype or exploration (not production code)
- Entire implementation fits in single commit

The overhead of task extraction and subagent coordination isn't free. For a two-line bug fix, just fix it directly. For a feature implementation with database changes, API updates, and frontend modifications—use tasks.

## Lab: Task Decomposition

**Objective:** Practice identifying task structure from a specification.

### Task

Take a specification (your own or from previous labs) and extract its task structure:

1. **List all implementation items** from the spec's checklist or requirements

2. **Identify dependencies:**
   - Which tasks require others to complete first?
   - Which tasks can run in parallel?

3. **Estimate task sizes:**
   - Tasks should be 5-15 minutes of work each
   - If larger, split into subtasks
   - If smaller, consider combining

4. **Draw the dependency graph:**
   ```
   Task 1 (schema) ─┬─> Task 3 (API)
                    │
   Task 2 (utils) ──┴─> Task 4 (tests)
   ```

Don't implement yet—just map the structure. Understanding task relationships before implementation prevents mid-execution surprises.

## Try With AI

**Running Example Continued:** We have a refined report-spec.md. Now we implement by extracting tasks and delegating to subagents.

**Prompt 1: Extract Tasks from Spec**

```
Read report-spec.md. Extract the implementation checklist into tasks.

For each task:
- One sentence description
- Dependencies (what must complete first?)
- Can it run in parallel with others?

Write to tasks.md.
```

**What you're learning:** The spec's checklist becomes your task list. "Write executive summary" depends on other sections (summarizes them). "Write tool comparison section" and "Write ROI section" might be independent. Making dependencies explicit prevents blocked subagents.

**Prompt 2: Implement First Task**

```
Implement report-spec.md using tasks.md.
Use the task tool. Each task should be done by a subagent.
After each task, commit before continuing.
You are the main agent; your subagents are your writers.

Start with task 1 only. Verify it meets the spec before proceeding.
```

**What you're learning:** The main agent orchestrates; subagents execute. Each subagent reads the spec and writes one section. Fresh context means the subagent writing "ROI Analysis" doesn't carry assumptions from the subagent that wrote "Tool Comparison."

**Prompt 3: Parallel Execution**

```
"Tool Comparison" and "Implementation Risks" in tasks.md have no
dependencies on each other. Execute them in parallel using separate
subagents. Commit each independently when complete.
```

**What you're learning:** Independent sections can be written simultaneously. If "Tool Comparison" and "Implementation Risks" don't cross-reference, parallel execution halves the time. The spec keeps both subagents aligned on audience, tone, and depth.
