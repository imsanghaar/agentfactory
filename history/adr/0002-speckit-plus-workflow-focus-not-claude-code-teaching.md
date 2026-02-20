# ADR-0002: SpecKit Plus Workflow Focus Not Claude Code Teaching

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-11-06
- **Feature:** 002-chapter-32-redesign
- **Context:** Chapter 32 must teach PARALLEL EXECUTION of SpecKit Plus workflows (`/sp.specify`, `/sp.plan`, `/sp.tasks`, `/sp.implement`) without redundantly teaching Claude Code fundamentals (Chapter 5) or SpecKit Plus basics (Chapter 31). Content drift toward "learning tools" must be prevented - students need to learn running workflows in parallel, not tool syntax.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security? YES - affects how all future chapters reference prior learning
     2) Alternatives: Multiple viable options considered with tradeoffs? YES - reteach Claude Code, reteach SpecKit Plus, focus on parallel execution
     3) Scope: Cross-cutting concern (not an isolated detail)? YES - impacts content boundaries for all book chapters, defines what "prerequisite" means
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Chapter 32 content MUST focus exclusively on **parallel execution of SpecKit Plus workflows** and explicitly MUST NOT reteach:

**Prerequisites (already learned)**:
- Claude Code fundamentals (Chapter 5)
- SpecKit Plus workflow basics (Chapter 31)
- MCP configuration (Chapter 5 - removed redundant Lesson 6 from original plan)

**What Chapter 32 teaches**:
- Running `/sp.specify` across 3-5 worktrees simultaneously
- Running `/sp.plan` and `/sp.tasks` in parallel sessions
- Coordinating parallel `/sp.implement` workflows
- Programmatic execution via headless mode (`claude -p "/sp.specify"`)
- Spawning 10-15 SpecKit Plus workflows via Super Orchestrator script

**Content guardrails**:
1. Every code example shows SpecKit Plus commands (`/sp.specify`, `/sp.plan`, `/sp.tasks`, `/sp.implement`) NOT generic Claude Code usage
2. Headless mode lesson (Lesson 6) demonstrates `claude -p "/sp.specify"` as foundation for Super Orchestrator, NOT "learning headless mode in general"
3. Sandboxing lesson (Lesson 7) focuses on isolation for spawning 10-15 sessions, NOT general security practices
4. All lesson introductions include: "Students already learned Claude Code (Ch 5) and SpecKit Plus (Ch 31). This chapter teaches running SpecKit Plus workflows IN PARALLEL."

**Deleted content**:
- MCP lesson (Task 3.2 from original plan) - students configured MCP in Chapter 5, redundant to reteach

## Consequences

### Positive

- **Clear learning objective**: Students know exactly what they're learning (parallel execution) vs what they should already know (tools)
- **Avoids redundancy**: No wasted time reteaching Chapter 5 or Chapter 31 content
- **Sharper content boundaries**: Future chapters can confidently assume Chapter 32 = parallel workflows, not tool proficiency
- **Better prerequisite enforcement**: Students who skip Chapters 5 or 31 will clearly see gaps (can't run parallel workflows without knowing SpecKit Plus)
- **Stronger portfolio narrative**: "I learned decomposition thinking through parallel workflows" vs "I learned more Claude Code features"
- **Daily workflow template**: AI Product Managers organize work around workflows (specify → plan → tasks → implement) not tools (Claude, MCP, headless mode)
- **Reduced cognitive load**: One clear learning objective (parallel execution) instead of mixed objectives (tools + workflows)

### Negative

- **Prerequisite assumptions**: Students who skipped Chapters 5 or 31 will struggle (mitigated by clear prerequisite list in Lesson 1)
- **Temptation to over-explain tools**: Authors must resist explaining Claude Code or SpecKit Plus basics (mitigated by content guardrails)
- **Missing "intro to tools" students expect**: Some students want comprehensive tool guides (mitigated by referencing Chapters 5 and 31 for deep dives)
- **Risk of "too narrow" perception**: Chapter appears specialized vs comprehensive (actually a strength - focused learning)

## Alternatives Considered

**Alternative A: Reteach Claude Code Fundamentals**
- Structure: Include sections explaining Claude Code CLI, basic commands, configuration before teaching parallel workflows
- Why rejected: Redundant with Chapter 5 - wastes time, dilutes focus, treats students as if they forgot prior chapters
- Tradeoff: More "comprehensive" but less effective (students already know this)

**Alternative B: Reteach SpecKit Plus Basics**
- Structure: Recap `/sp.specify`, `/sp.plan`, `/sp.tasks` workflows before showing parallel execution
- Why rejected: Redundant with Chapter 31 - assumes students don't retain prior learning
- Tradeoff: "Gentler" introduction but disrespects students' prior work

**Alternative C: Generic "Multi-AI-Agent Coordination" Chapter**
- Structure: Teach parallel execution with any AI tool (Claude Code, Gemini CLI, Copilot), not SpecKit Plus specific
- Why rejected: Loses coherence with book's SDD methodology - students wouldn't see SpecKit Plus as THE workflow
- Tradeoff: Appears more flexible but loses pedagogical continuity

**Alternative D: Include MCP Lesson as "Advanced Configuration"**
- Structure: Keep original Lesson 6 (MCP Servers & Shared Context) for students who want deeper MCP understanding
- Why rejected: Students configured MCP in Chapter 5 - this is infrastructure, not a learning topic for Chapter 32
- Tradeoff: More "complete" feeling but redundant and off-topic

**Alternative E: Mix SpecKit Plus with Generic Claude Code Examples**
- Structure: Show both SpecKit Plus workflows AND generic Claude Code patterns in same chapter
- Why rejected: Dilutes focus - students would confuse "learning parallel workflows" with "learning more Claude Code tricks"
- Tradeoff: Appears more comprehensive but actually weakens core learning objective

## References

- Feature Spec: `/Users/mjs/Documents/code/panaversity-official/tutorgpt-build/bbb/specs/002-chapter-32-redesign/spec.md`
- Implementation Plan: `/Users/mjs/Documents/code/panaversity-official/tutorgpt-build/bbb/specs/002-chapter-32-redesign/plan.md`
- Implementation Tasks: `/Users/mjs/Documents/code/panaversity-official/tutorgpt-build/bbb/specs/002-chapter-32-redesign/tasks.md`
- Related ADRs: ADR-0001 (Two-Climax Pedagogical Structure)
- Evaluator Evidence:
  - PHR 0005: `/Users/mjs/Documents/code/panaversity-official/tutorgpt-build/bbb/history/prompts/002-chapter-32-redesign/0005-two-climaxes-speckit-plus-focus-final.tasks.prompt.md`
  - User feedback: "Makes sense and this is married with spec kit plus at core as this is not about learning claude code that was already taught in ch 5 remember this"
  - User feedback: "what we are not teaching claude code that was chapter 5 and speckitplus that was chapter 31"
