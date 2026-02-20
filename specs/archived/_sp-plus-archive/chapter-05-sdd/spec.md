# Chapter 5: Spec-Driven Development with Claude Code

## Specification Document

**Version**: 1.0
**Status**: Draft
**Author**: AI Agent Factory Curriculum Team
**Date**: 2026-02-03

---

## 1. Executive Summary

Chapter 5 teaches Spec-Driven Development (SDD) using **native Claude Code capabilities only**—no external frameworks. Students learn to orchestrate complex projects by treating specifications as the primary artifact, with code as generated output.

**Key distinction**: This chapter teaches SDD workflow using Claude Code's built-in features (CLAUDE.md, Subagents, Tasks, Hooks) rather than external tools like Spec-Kit, Kiro, or Tessl. External tooling is acknowledged but positioned as "abstractions built on top" of what students learn here.

---

## 2. Prerequisites (What Students Already Know)

After Chapters 1-4, students can:

| Chapter | Capability Gained                                                                                     |
| ------- | ----------------------------------------------------------------------------------------------------- |
| Ch1     | Explain General vs Custom Agents; understand Digital FTE business model; know SDD exists conceptually |
| Ch2     | Write markdown specifications that AI agents can parse; structure requirements clearly                |
| Ch3     | Use Claude Code effectively; configure Skills; orchestrate subagents; integrate MCP                   |
| Ch4     | Design context architecture; audit signal vs noise; manage context lifecycle                          |

**Critical assumption**: Students have hands-on experience with `CLAUDE.md`, Skills, Subagents, and the Task system from Chapters 3-4. This chapter operationalizes that knowledge into a cohesive workflow.

---

## 3. Learning Objectives

By the end of this chapter, students will be able to:

1. **Explain** why vibe coding fails for production systems (context loss, assumption drift, pattern violations)
2. **Distinguish** between the three SDD implementation levels (Spec-First, Spec-Anchored, Spec-as-Source)
3. **Execute** the four-phase SDD workflow using native Claude Code features
4. **Design** effective specifications that AI agents can implement reliably
5. **Apply** parallel research patterns with subagents
6. **Use** the Task system for dependency-aware orchestration with atomic commits
7. **Decide** when SDD adds value vs when simpler approaches suffice

---

## 4. Chapter Structure

### Lesson Breakdown (9 Lessons including Quiz)

| #   | Title                              | Duration | Layer | Focus                                             |
| --- | ---------------------------------- | -------- | ----- | ------------------------------------------------- |
| 00  | Why Specs Beat Vibe Coding         | 15 min   | L1    | Problem statement: context loss, assumption drift |
| 01  | The Three Levels of SDD            | 20 min   | L1→L2 | Spec-First vs Spec-Anchored vs Spec-as-Source     |
| 02  | The Four-Phase Workflow            | 25 min   | L2    | Research → Spec → Refine → Implement              |
| 03  | Phase 1: Parallel Research         | 30 min   | L2→L3 | Spawning multiple subagents; prompt patterns      |
| 04  | Phase 2: Writing Effective Specs   | 30 min   | L2    | Spec structure, templates, what to include        |
| 05  | Phase 3: Refinement via Interview  | 20 min   | L2    | AskUserQuestion patterns; surfacing ambiguities   |
| 06  | Phase 4: Task-Based Implementation | 35 min   | L3    | Task system for orchestration; atomic commits     |
| 07  | The Decision Framework             | 20 min   | L2    | When SDD excels vs overkill; the judgment call    |
| 08  | Chapter Quiz                       | 15 min   | —     | Standard 50-question interactive assessment       |

**Total estimated time**: ~3.5 hours

---

## 5. Detailed Lesson Specifications

### Lesson 00: Why Specs Beat Vibe Coding

**Objective**: Understand the failure modes of conversational AI coding that SDD solves.

**Content**:

- The vibe coding pattern: prompt → code → "no, I meant..." → code → repeat
- Three failure modes:
  1. **Context loss** — each iteration loses discoveries
  2. **Assumption drift** — agent makes reasonable but wrong guesses
  3. **Pattern violations** — generated code doesn't match project architecture
- Real example: notification system conversation that spirals
- The insight: Claude needs the complete picture upfront, not iterative discovery

**Try With AI prompts**:

1. Experience the problem: Ask Claude to "add a notification system" without specs
2. Observe the iteration cycle and what gets lost
3. Reflect: What would Claude need to know upfront?

---

### Lesson 01: The Three Levels of SDD

**Objective**: Understand the spectrum of SDD implementations and their trade-offs.

**Content**:
| Level | Creation | Maintenance | Use Case |
|-------|----------|-------------|----------|
| **Spec-First** | Spec guides implementation | Spec discarded after | Most common; quick tasks |
| **Spec-Anchored** | Spec written first | Both spec + code maintained | Team projects; living documentation |
| **Spec-as-Source** | Spec is primary artifact | Only spec edited; code regenerated | Experimental; Tessl approach |

- Most practitioners operate at Spec-First level
- Spec-Anchored provides onboarding value (specs = documentation)
- Spec-as-Source is emerging but introduces determinism challenges

**Try With AI prompts**:

1. "Explain the trade-offs between maintaining specs alongside code vs regenerating code from specs"
2. "When would Spec-as-Source fail in a real project?"

---

### Lesson 02: The Four-Phase Workflow

**Objective**: Understand the complete SDD workflow before diving into each phase.

**Content**:

```
Phase 1: Research (Parallel Subagents)
    ↓ Multiple agents investigate reference implementations
Phase 2: Specification (Written Artifact)
    ↓ Comprehensive markdown document
Phase 3: Refinement (Interview)
    ↓ AskUserQuestion surfaces ambiguities
Phase 4: Implementation (Task Delegation)
    ↓ Atomic tasks with commits
```

- Why this order matters: research informs spec, spec prevents pivot, tasks enable rollback
- The spec becomes the source of truth that survives session restarts
- Unlike vibe coding, each phase has a clear deliverable

**Key insight**: SDD separates **planning** from **execution**. Review happens at phase gates, not during coding.

---

### Lesson 03: Phase 1 — Parallel Research with Subagents

**Objective**: Use Claude's subagent system to parallelize research.

**Content**:

- **Prompt pattern**: "Spin up multiple subagents for your research task"
- What happens: Claude spawns 3-5 independent agents, each investigating a different aspect
- Example research distribution:
  - Agent 1: CRDT data structures
  - Agent 2: WebSocket sync protocols
  - Agent 3: Storage persistence patterns
  - Agent 4: Overall architecture

**Why parallel works**:

- Each agent has independent context (no cross-contamination)
- Research that takes sequential hours becomes parallel minutes
- Different agents may discover different insights

**Prompt templates**:

```markdown
Research Task: [TOPIC]

Spawn parallel subagents to investigate:

1. [Aspect 1] — focus on [specific question]
2. [Aspect 2] — focus on [specific question]
3. [Aspect 3] — focus on [specific question]

Return: Written summary of findings for each aspect
```

**Try With AI prompts**:

1. "I want to understand how [reference repo] implements [feature]. Spawn multiple subagents for your research task."
2. Observe the parallel execution pattern
3. Compare findings across agents

---

### Lesson 04: Phase 2 — Writing Effective Specifications

**Objective**: Create specifications that AI agents can implement reliably.

**Content**:
**Spec template structure**:

```markdown
# [Feature] Specification

## Part 1: Reference Architecture Analysis

- Patterns discovered in research
- Key design decisions and rationale

## Part 2: Current Architecture Analysis

- Existing implementation details
- Pain points and limitations

## Part 3: Implementation Plan

- Phased approach (what order to build)
- Risk mitigation strategies

## Part 4: Implementation Checklist

- [ ] Task 1: Core utilities
- [ ] Task 2: Integration layer
- [ ] Task N: Testing and cleanup

## Constraints

- What NOT to build
- Technology boundaries
- Performance requirements

## Success Criteria

- Measurable outcomes (e.g., "95% of X within Y seconds")
- Acceptance tests
```

**What makes specs effective**:

1. **Explicit constraints** — what NOT to do is as important as what to do
2. **Measurable success** — "fast" fails; "< 100ms p95" succeeds
3. **Edge cases defined** — what happens when things fail?
4. **Checklist format** — enables task extraction in Phase 4

**Anti-patterns**:

- Specs that describe HOW (implementation) instead of WHAT (behavior)
- Missing constraints (agent makes reasonable but wrong choices)
- Vague success criteria

**Try With AI prompts**:

1. "Convert these requirements into a structured specification: [paste requirements]"
2. "What's missing from this spec that could cause implementation issues?"
3. "Add explicit constraints and success criteria to this spec"

---

### Lesson 05: Phase 3 — Refinement via Interview

**Objective**: Use the interview pattern to surface ambiguities before coding.

**Content**:

- **Prompt pattern**: "Use the ask_user_question tool before we implement"
- Purpose: Surface design decisions that would otherwise become mid-implementation pivots

**Common interview questions**:

- Should we migrate existing data or start fresh?
- What's the conflict resolution strategy?
- Which pattern from [reference] should we adopt: A or B?
- What's the failure recovery approach?

**Why this matters**:

- Each ambiguity found now saves 10x time during implementation
- The spec becomes more precise
- You maintain control of architectural decisions

**Interview checklist**:

```markdown
Before implementation, clarify:
[ ] Data migration strategy
[ ] Error handling approach
[ ] Performance constraints
[ ] Technology boundaries
[ ] Integration points with existing code
```

**Try With AI prompts**:

1. "Here's my spec. Use ask_user_question to surface any ambiguities before implementation."
2. Answer the questions, then ask: "Update the spec with my answers"

---

### Lesson 06: Phase 4 — Task-Based Implementation

**Objective**: Use Claude's Task system for dependency-aware orchestration with atomic commits.

**Content**:
**Core prompt pattern**:

```markdown
Implement @docs/my-spec.md

Use the task tool and each task should only be done by a subagent
so that context is clear. After each task do a commit before you continue.

You are the main agent and your subagents are your devs.
```

**What happens**:

1. Main agent extracts tasks from spec checklist
2. Each task delegated to fresh subagent (context isolation)
3. Subagent completes task → commits → returns
4. Main agent tracks progress, handles blockers

**Task system operations**:
| Tool | Purpose |
|------|---------|
| `TaskCreate` | Define task with dependencies |
| `TaskUpdate` | Transition status (pending → in_progress → completed) |
| `TaskList` | View all tasks and blockers |
| `TaskGet` | Retrieve full task details |

**Why context isolation matters**:

- Each subagent starts fresh — no accumulated clutter
- If task fails, only that context is affected
- Parallel tasks don't pollute each other

**Backpressure pattern**: Pre-commit hooks

```bash
# .husky/pre-commit
pnpm typecheck && pnpm lint && pnpm test-run
```

When commit fails, agent sees error output and self-corrects.

**Try With AI prompts**:

1. "Create a task breakdown for this spec: [paste spec]"
2. "Implement task 1. After completion, commit with atomic message."
3. "What tasks can run in parallel vs which have dependencies?"

---

### Lesson 07: The Decision Framework

**Objective**: Know when SDD adds value vs when simpler approaches work better.

**Content**:
**SDD excels for**:
| Scenario | Why SDD Helps |
|----------|---------------|
| Large refactors (15+ files) | Upfront spec prevents mid-refactor pivots |
| Unclear requirements | Research phase surfaces what you don't know |
| Learning new libraries | Parallel research accelerates understanding |
| Team coordination | Spec serves as contract between implementers |
| Legacy modernization | Captures original intent before rebuilding |

**SDD is overkill for**:
| Scenario | Why Skip SDD |
|----------|--------------|
| Single-file bug fixes | Three-document workflow for one-line fix wastes time |
| Well-defined simple features | Implementation is obvious; spec adds no value |
| Exploratory prototyping | You're discovering requirements; vibe coding is faster |
| Production incidents | Need immediate action, not spec documents |

**Decision heuristic**:

```
IF files_affected > 5 OR requirements_unclear OR learning_new_tech:
    Use SDD
ELSE IF single_file AND bug_fix:
    Skip SDD
ELSE:
    Judgment call — try lightweight spec first
```

**The judgment skill**: Experienced practitioners develop intuition for when spec ceremony pays off. Start with lightweight specs (just constraints + success criteria) and add structure as needed.

**Try With AI prompts**:

1. "I need to [describe task]. Should I use SDD or direct implementation? Why?"
2. "What's the minimum spec I'd need for this task?"

---

## 6. Key Prompt Patterns Summary

| Pattern               | When to Use            | Example                                                       |
| --------------------- | ---------------------- | ------------------------------------------------------------- |
| **Parallel Research** | Starting investigation | "Spin up multiple subagents for your research task"           |
| **Spec-First**        | Force written artifact | "Your goal is to write a report/document"                     |
| **Interview**         | Surface ambiguities    | "Use ask_user_question tool before we implement"              |
| **Task Delegation**   | Complex implementation | "Use the task tool, each task by subagent, commit after each" |
| **Role Assignment**   | Set expectations       | "You are the main agent and your subagents are your devs"     |

---

## 7. Connection to Other Chapters

| Chapter | Connection                                                                         |
| ------- | ---------------------------------------------------------------------------------- |
| Ch1     | SDD operationalizes the conceptual framework introduced there                      |
| Ch2     | Markdown specs use the skills taught in Ch2                                        |
| Ch3     | Subagents, Tasks, and CLAUDE.md from Ch3 are the implementation tools              |
| Ch4     | Context architecture decisions inform spec design                                  |
| Ch6     | Seven Principles explain WHY SDD patterns work (verification, decomposition, etc.) |

---

## 8. Assessment Criteria

Students demonstrate mastery by:

1. **Diagnostic**: Given a failed vibe-coding conversation, identify what spec would have prevented the failure
2. **Application**: Create a complete spec for a provided feature requirement
3. **Analysis**: Given a task, decide whether SDD is appropriate and justify
4. **Synthesis**: Execute the four-phase workflow on a real refactoring task

---

## 9. Chapter Quiz Topics

- Failure modes of vibe coding
- Three SDD levels and their trade-offs
- Four-phase workflow sequence
- Effective spec components
- When to use/skip SDD
- Task system operations
- Prompt patterns for each phase

---

## 10. Success Metrics

Chapter is successful if students can:

- [ ] Explain why SDD exists (the problems it solves)
- [ ] Execute the four-phase workflow without external tools
- [ ] Write specs that AI agents implement correctly on first attempt
- [ ] Use the Task system for orchestrated implementation
- [ ] Make sound decisions about when SDD applies

---

## 11. Chapter Quiz (Lesson 08)

Standard format quiz covering:

- Failure modes of vibe coding (context loss, assumption drift, pattern violations)
- Three SDD implementation levels and their trade-offs
- Four-phase workflow sequence and deliverables
- Effective spec components (constraints, success criteria, checklists)
- When to use SDD vs when simpler approaches work better
- Task system operations and context isolation
- Prompt patterns for each phase (parallel research, spec-first, interview, task delegation)

---

## Appendix A: Primary Source Materials

### Paper 1: Panaversity Research Paper (Feb 2026)

"Spec-Driven Development with Claude Code: A Comprehensive Guide to AI-Native Software Development"

Provides:

- Theoretical foundations and definitions
- Three levels of SDD implementation
- Claude Code architecture (Memory, Subagents, Tasks)
- Critiques and limitations (Waterfall concern, diminishing returns)
- Future directions (runtime observation, multi-agent orchestration)

### Paper 2: alexop.dev Practical Guide (Feb 2026)

"Spec-Driven Development with Claude Code in Action"

Provides:

- Real-world example: SQLite to IndexedDB migration
- Exact prompts used at each phase
- Task persistence structure (JSON format)
- Context efficiency metrics (71% usage after 14 tasks)
- Backpressure pattern with pre-commit hooks
- Results: 45 minutes, 14 commits, 15+ files

### Additional References

- Claude Code Documentation: Subagents, Tasks, Memory
- Steve Yegge's Beads project (inspiration for Task system)

---

_End of Specification_
