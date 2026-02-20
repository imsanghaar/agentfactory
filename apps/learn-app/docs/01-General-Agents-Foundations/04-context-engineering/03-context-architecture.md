---
sidebar_position: 3
title: "Context Architecture"
description: "How CLAUDE.md, Skills, Subagents, and Hooks work together as a complete context management system"
keywords:
  [
    "context architecture",
    "CLAUDE.md",
    "Skills",
    "Subagents",
    "Hooks",
    "context management",
    "on-demand loading",
  ]
chapter: 4
lesson: 3
duration_minutes: 25

# HIDDEN SKILLS METADATA
skills:
  - name: "Understanding Context Loading Patterns"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain when each tool loads context and its cost impact"

  - name: "Designing Context Architecture"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can map project requirements to appropriate context tools"

  - name: "Calculating Context Cost"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can estimate token cost of different architecture approaches"

learning_objectives:
  - objective: "Explain how the four context tools load and cost differently"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student can describe loading timeline and cost for each tool"

  - objective: "Apply the decision framework to choose appropriate tools"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student selects correct tool for given information type"

  - objective: "Design a context architecture for a project"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Student produces architecture map distributing information across tools"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (context loading timeline, decision framework, cost calculation, architecture design, tool orchestration) appropriate for B1"

differentiation:
  extension_for_advanced: "Design multi-layer architecture with Skills that invoke Subagents"
  remedial_for_struggling: "Focus on the decision framework table first, then practice with concrete examples"

teaching_guide:
  lesson_type: "core"
  session_group: 1
  session_title: "Understanding Context Engineering"
  key_points:
    - "Four tools have four distinct loading patterns — CLAUDE.md always loads, Skills on-demand, Subagents in isolated context, Hooks externally with zero context cost"
    - "The decision framework maps information type to tool: always-needed to CLAUDE.md, sometimes-needed to Skills, fresh-analysis to Subagents, deterministic to Hooks"
    - "The marketing consultant example shows a 13x reduction in baseline context (7,300 to 550 tokens) — this quantifies why architecture matters"
  misconceptions:
    - "Students think putting everything in CLAUDE.md is safest because Claude 'always sees it' — this actually dilutes attention and causes Claude to ignore important instructions"
    - "Students confuse Skills with Subagents — Skills load into YOUR context on demand, Subagents run in their OWN isolated context and return summaries"
    - "Students assume Hooks are advanced/optional — they are the simplest tool (zero context cost, deterministic) and should be the first choice for validation tasks"
  discussion_prompts:
    - "In your own project, what information does Claude need for EVERY task vs only SOME tasks? How would you split it across tools?"
    - "Why would a 300-line CLAUDE.md with everything in it perform WORSE than a 50-line one with Skills handling the rest?"
  teaching_tips:
    - "The four-tool loading table is the anchor of this lesson — have students copy it and reference it during the lab exercise"
    - "Walk through the marketing consultant example end-to-end: inventory, tool assignment, cost calculation — this makes the abstract framework concrete"
    - "Common mistake 1 (everything in CLAUDE.md) resonates with most students — ask who has a CLAUDE.md over 100 lines before presenting the fix"
    - "The 13x reduction math is a strong persuasion moment — write the two numbers (7,300 vs 550) on the board side by side"
  assessment_quick_check:
    - "Name the four context tools and their loading patterns (when and what they load)"
    - "Given a piece of information, explain which tool you would use and why"
    - "What is the context cost of a Subagent in the main session, and why is this significant?"
---

# Context Architecture: The Complete System

You learned HOW to create CLAUDE.md files, Skills, Subagents, and Hooks in Chapter 3. This lesson teaches WHY each exists and WHEN to use each one—as parts of a complete context management system.

## Four Tools, Four Loading Patterns

Each tool has a different relationship with your context window:

| Tool          | When It Loads                               | What Loads                                       | Context Cost         |
| ------------- | ------------------------------------------- | ------------------------------------------------ | -------------------- |
| **CLAUDE.md** | Session start                               | Full content                                     | Every request        |
| **Skills**    | Descriptions at start; content when invoked | ~100 tokens per description; full content on use | Low until needed     |
| **Subagents** | When spawned                                | Fresh, isolated context                          | Zero in main session |
| **Hooks**     | On trigger                                  | Nothing (runs externally)                        | Zero                 |

Understanding this table is understanding context architecture.

## The Loading Timeline

**At session start**, Claude loads:

1. System prompt (you don't control this)
2. Your CLAUDE.md (full content)
3. Skill descriptions (names and one-line summaries)
4. MCP tool definitions (if any)
5. Git status and workspace info

**During the session**, Claude loads:

- Skill full content (when you invoke `/skill-name` or Claude decides it's relevant)
- Subagent results (summaries returned, not full work)
- Hook output (only if the hook returns messages)

**What this means**: CLAUDE.md consumes context from turn 1. Skills consume context only when needed. Subagents never consume your main context. Hooks run outside the context entirely.

## The Decision Framework

Use this framework to choose the right tool:

| Information Type             | Best Tool | Why                                     |
| ---------------------------- | --------- | --------------------------------------- |
| **Always needed, stable**    | CLAUDE.md | Pay the cost once, available everywhere |
| **Sometimes needed, stable** | Skill     | On-demand loading saves context         |
| **Needs fresh analysis**     | Subagent  | Isolated context prevents pollution     |
| **Must happen every time**   | Hook      | Deterministic, no LLM variance          |

### When to Use CLAUDE.md

Put information in CLAUDE.md when:

- Claude needs it for EVERY task (project conventions, build commands)
- It rarely changes (architectural decisions, team agreements)
- Removing it would cause Claude to make mistakes

**Examples**:

- `pnpm, not npm` (always relevant)
- `Run tests with pytest -v` (needed whenever testing)
- `Use snake_case for Python, camelCase for JavaScript` (affects all code)

### When to Use Skills

Put information in Skills when:

- Claude needs it SOMETIMES (domain-specific workflows)
- It's substantial (more than a few lines)
- You might invoke it manually (`/skill-name`)

**Examples**:

- Code review checklist (only when reviewing)
- Deployment procedures (only when deploying)
- API documentation (only when integrating)

### When to Use Subagents

Use Subagents when:

- Work requires reading many files or extensive research
- You need a fresh perspective without accumulated bias
- The work should happen in parallel

**Examples**:

- Research task: "Find all usages of deprecated API"
- Analysis task: "Review security across all auth files"
- Parallel work: Three agents tackle three modules simultaneously

### When to Use Hooks

Use Hooks when:

- Something must happen EVERY time, no exceptions
- It's deterministic (no LLM judgment needed)
- It should run externally without consuming context

**Examples**:

- Lint check after every file edit
- Format validation before every commit
- Logging for audit purposes

## Context Architecture in Practice

### Example: A Marketing Consultant

A marketing consultant uses Claude Code for campaign analysis:

**CLAUDE.md** (~50 lines, always loaded):

```markdown
# Project Context

- Client: TechStartup Inc.
- Brand voice: Professional but approachable
- Avoid: Industry jargon, corporate speak

# Workflow

- All reports in Markdown
- Include metrics with sources
- Weekly summary format: Executive → Details → Recommendations
```

**Skills** (loaded when relevant):

- `/competitor-analysis` — Framework for analyzing competitor campaigns
- `/metrics-dashboard` — Standard metrics definitions and benchmarks
- `/campaign-brief` — Template for new campaign proposals

**Subagent** (isolated, returns summary):

- Research agent scans 50 competitor social posts, returns "Top 5 patterns"
- Main context never sees 50 posts, just the summary

**Hook** (zero context cost):

- After every report edit, hook validates required sections exist
- Returns only pass/fail, doesn't consume context

### The Math

**Without architecture** (everything in CLAUDE.md):

- 500-line CLAUDE.md = ~4,000 tokens
- Competitor analysis framework = ~1,500 tokens
- Metrics definitions = ~1,000 tokens
- Campaign template = ~800 tokens
- **Total baseline**: ~7,300 tokens every request

**With architecture**:

- 50-line CLAUDE.md = ~400 tokens (always)
- 3 skill descriptions = ~150 tokens (always)
- Skill content = ~3,300 tokens (only when invoked)
- Research via subagent = 0 tokens in main context
- **Total baseline**: ~550 tokens every request

**Result**: 13x reduction in baseline context load. The saved tokens go to your actual work instead of always-loaded content.

## Common Architecture Mistakes

### Mistake 1: Everything in CLAUDE.md

**Symptom**: 300+ line CLAUDE.md, Claude ignores important instructions

**Problem**: Attention diluted across content that's only sometimes relevant

**Fix**: Move domain-specific content to Skills, keep CLAUDE.md under 60 lines

### Mistake 2: Never Using Subagents

**Symptom**: Context fills quickly during research tasks, quality degrades

**Problem**: All file reads and searches accumulate in main context

**Fix**: Delegate research to Subagents, receive summaries instead of raw data

### Mistake 3: Skills for Everything

**Symptom**: Many skills exist but Claude rarely invokes them correctly

**Problem**: Skill descriptions don't clearly signal when to use them

**Fix**: Write clear descriptions, or set `disable-model-invocation: true` for manual-only skills

### Mistake 4: Forgetting Hooks Exist

**Symptom**: Repetitive validation tasks consume LLM calls

**Problem**: Using Claude for deterministic checks it doesn't need to reason about

**Fix**: Move deterministic validations to Hooks, save context for actual reasoning

## Lab: Map Your Context Architecture

**Objective:** Design a context architecture for your project or domain.

**Step 1: Inventory Your Information**

List everything Claude needs to know for your work:

```markdown
# Information Inventory

## Always Needed

- [List items Claude needs every single time]

## Sometimes Needed

- [List domain-specific workflows, templates, procedures]

## Research-Heavy

- [List tasks requiring extensive file reading or analysis]

## Deterministic Checks

- [List validations that don't require reasoning]
```

**Step 2: Apply the Framework**

For each item, assign the appropriate tool:

| Information | Tool                                | Rationale       |
| ----------- | ----------------------------------- | --------------- |
| [Item 1]    | CLAUDE.md / Skill / Subagent / Hook | [Why this tool] |
| [Item 2]    | ...                                 | ...             |

**Step 3: Calculate the Cost**

Estimate token impact:

```markdown
# Context Cost Analysis

## Without Architecture

- All content in CLAUDE.md: ~[X] tokens every request

## With Architecture

- CLAUDE.md baseline: ~[Y] tokens
- Skill descriptions: ~[Z] tokens
- Average skill invocation: ~[W] tokens (only when needed)

## Savings

- Baseline reduction: [percentage]
- Context available for work: [additional tokens]
```

**Step 4: Implement One Piece**

Choose the highest-impact change and implement it:

- Move one section from CLAUDE.md to a Skill, OR
- Create one Subagent for research tasks, OR
- Add one Hook for deterministic validation

## What You Learned

1. **Four tools have four loading patterns** — CLAUDE.md always loads, Skills load on-demand, Subagents use isolated context, Hooks run externally
2. **The decision framework** maps information type to appropriate tool — always-needed → CLAUDE.md, sometimes-needed → Skill, fresh-analysis → Subagent, deterministic → Hook
3. **Context architecture dramatically reduces baseline load** — 10x+ reduction is achievable by distributing information appropriately
4. **Common mistakes** include overloading CLAUDE.md, avoiding Subagents, unclear skill descriptions, and forgetting Hooks

## Try With AI

### Prompt 1: Architecture Audit

```
Review my current context setup:
- CLAUDE.md has [X] lines
- I have [Y] skills
- I never use subagents
- I have no hooks

Analyze where I'm wasting context.
What should I move to Skills?
What should become Subagent tasks?
What deterministic checks could be Hooks?
```

**What you're learning:** Identifying architecture inefficiencies in your own setup.

### Prompt 2: Design Challenge

```
I'm a [your profession] working on [your project type].
My recurring tasks are:
1. [Task 1]
2. [Task 2]
3. [Task 3]

Design a context architecture:
- What goes in CLAUDE.md (under 60 lines)?
- What Skills should I create?
- What Subagent patterns would help?
- What Hooks would reduce context waste?
```

**What you're learning:** Applying the framework to your actual work.

### Prompt 3: Migration Plan

```
I have a 400-line CLAUDE.md that I need to refactor.
Here's the current content: [paste content]

Create a migration plan:
1. What stays in CLAUDE.md? (under 60 lines)
2. What becomes Skills? (list with descriptions)
3. What changes to Subagent patterns?
4. What becomes Hooks?

Include rationale for each decision.
```

**What you're learning:** Practical migration from overloaded setup to proper architecture.
