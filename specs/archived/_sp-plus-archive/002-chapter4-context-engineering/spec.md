# Feature Specification: Chapter 4 — Effective Context Engineering with General Agents

**Feature Branch**: `002-chapter4-context-engineering`
**Created**: 2026-01-29
**Revised**: 2026-01-29
**Status**: Draft
**Input**: User description: "NEW Chapter 4 for Part 1 — Context Engineering as Quality Control for Digital FTE Manufacturing"
**Primary Sources**:

- "Lost in the Middle: How Language Models Use Long Contexts" (Stanford/Berkeley, Liu et al. 2023)
- "Context Rot Research" (Chroma Research)
- "Better Context Will Always Beat a Better Model" (The New Stack)
- OpenAI Agents SDK: Context Personalization patterns
- LangChain Deep Agents research

---

## Executive Summary

Chapter 4 introduces **Context Engineering** as the quality control discipline for Digital FTE manufacturing. This chapter teaches students **WHY** context matters, **WHEN** to apply different context strategies, and **HOW** to engineer context that produces sellable agent quality.

**Critical Positioning**: This chapter goes between Chapter 3 (General Agents tools) and the new Chapter 5 (Seven Principles). Students already know HOW to use CLAUDE.md, Skills, Subagents, Hooks, and MCP. This chapter teaches WHY those tools work and WHEN to use each one.

**Core Thesis Connection**: "General Agents BUILD Custom Agents" — Context engineering IS the quality control discipline that determines whether your Digital FTE is worth $500/month or $50,000/month.

**Principle 5 Bridge**: This chapter provides the WHY and HOW behind "Persisting State in Files" (upcoming Chapter 5). Without understanding attention mechanics, position sensitivity, and context rot, "persisting state in files" becomes cargo cult—doing the motion without understanding the physics.

**Proficiency Level**: B1 (Intermediate) — Students have practical Claude Code experience from Chapter 3

---

## What This Chapter IS and IS NOT

### What This Chapter IS

| Teaches                                       | Example                                                                     |
| --------------------------------------------- | --------------------------------------------------------------------------- |
| **WHY** more context isn't better             | 47-line CLAUDE.md outperforming 400-line one because of attention mechanics |
| **WHY** Claude forgets middle content         | Position sensitivity research (Lost in the Middle)                          |
| **WHEN** to /clear vs /compact                | Decision framework based on context zones                                   |
| **HOW** to structure for position sensitivity | Three-zone strategy (beginning, middle, end)                                |
| **HOW** to persist state across sessions      | Progress files, session architecture                                        |
| **HOW** to prevent workflow drift             | Memory injection patterns                                                   |
| **HOW** to isolate context in multi-agent     | Clean slate vs dirty slate comparison                                       |

### What This Chapter IS NOT

| Does NOT Teach                       | Why (Covered Elsewhere)          |
| ------------------------------------ | -------------------------------- |
| How to create CLAUDE.md files        | Chapter 3, Lesson 5-6            |
| How to create Skills                 | Chapter 3, Lesson 7-8            |
| How to use Subagents                 | Chapter 3, Lesson 9              |
| How to configure Hooks               | Chapter 3, Lesson 13             |
| How to set up MCP servers            | Chapter 3, Lesson 10             |
| What /clear and /compact commands do | Chapter 3 basics                 |
| Seven Principles framework           | Chapter 5 (follows this chapter) |

---

## User Scenarios & Testing

### User Story 1 — Understanding Why Context Quality Determines Agent Value (Priority: P1)

A student who has built several agents in Chapter 3 notices inconsistent results—sometimes Claude follows conventions, sometimes it doesn't. They want to understand WHY this happens.

**Why this priority**: Foundation for all subsequent lessons. Without understanding the manufacturing quality problem, students treat context engineering as optional instead of essential.

**Independent Test**: Student can explain why two engineers using the same model produce agents of vastly different quality—and identify context quality as the differentiator.

**Acceptance Scenarios**:

1. **Given** a student has used Claude Code for several projects, **When** they complete Lesson 1, **Then** they can articulate why a $50/month agent differs from a $5,000/month agent—citing context quality as the primary factor.

2. **Given** a student understands the manufacturing analogy, **When** asked about quality control, **Then** they can map Toyota's quality control practices to Digital FTE manufacturing: raw materials (context), assembly precision (information organization), testing protocols (verification workflows).

3. **Given** a student understands context composition, **When** asked what determines agent output quality, **Then** they can list the 5 context components (system prompt ~5-10%, CLAUDE.md ~5-10%, tool definitions ~10-15%, message history ~30-40%, tool outputs ~20-30%) and explain why optimizing each matters.

---

### User Story 2 — Diagnosing Context Degradation (Priority: P1)

A student notices Claude gets worse as conversations get longer, even though they're using the same model. They want to understand WHY and WHEN this happens.

**Why this priority**: Attention budget is the foundational concept that explains most context-related quality issues.

**Independent Test**: Student can predict when context degradation will occur (70% threshold), identify the 4 types of context rot, and take appropriate action.

**Acceptance Scenarios**:

1. **Given** a student understands the attention budget, **When** they check `/usage` and see 75% utilization, **Then** they recognize they're in the "orange zone" and proactively `/compact`.

2. **Given** a student sees quality decline, **When** they audit their context, **Then** they can classify the issue as one of 4 rot types: Poisoning (outdated info), Distraction (irrelevant content), Confusion (similar concepts conflate), or Clash (contradictory instructions).

3. **Given** a student understands the U-shaped attention curve, **When** they structure context, **Then** they place critical constraints at beginning (Zone 1) and workflow instructions at end (Zone 3), leaving reference material in the middle (Zone 2).

---

### User Story 3 — Optimizing CLAUDE.md Signal-to-Noise (Priority: P1)

A student has a 300-line CLAUDE.md but notices Claude often ignores important instructions. They want to understand WHY and HOW to optimize.

**Why this priority**: This is the most immediately actionable improvement—reducing noise to amplify signal.

**Independent Test**: Student can audit their CLAUDE.md, classify each section as SIGNAL or NOISE using the 4-question framework, and reduce to <60 lines while improving effectiveness.

**Acceptance Scenarios**:

1. **Given** a student has a 300+ line CLAUDE.md, **When** they apply the signal-to-noise audit, **Then** they can identify 30-60% of content as noise (things Claude can figure out, default conventions, frequently-changing info).

2. **Given** a student understands the <60 line rule, **When** they refactor their CLAUDE.md, **Then** the result contains only: bash commands Claude can't guess, code style rules that differ from defaults, testing instructions, repository etiquette, and architectural decisions.

3. **Given** a student has optimized their CLAUDE.md, **When** they compare before/after performance, **Then** Claude's instruction compliance improves (fewer ignored conventions, fewer redundant questions).

---

### User Story 4 — Managing Multi-Session Work (Priority: P2)

A student is working on a feature that spans multiple sessions. They lose context between sessions and waste time re-establishing state. They want to learn HOW to persist progress effectively.

**Why this priority**: Multi-session work is where context engineering pays the biggest dividends—it's the difference between professional and amateur agent development.

**Independent Test**: Student can design a progress file architecture, implement session resumption, and complete a multi-session feature without significant context loss.

**Acceptance Scenarios**:

1. **Given** a student has a 5-session feature, **When** they use progress file architecture, **Then** each session starts by reading `claude-progress.txt`, immediately understands what's completed/in-progress/blocked, and continues without re-explanation.

2. **Given** a student ends a session, **When** they follow the commit checkpoint pattern, **Then** they commit working code and update the progress file before closing—ensuring the next session has clean state.

3. **Given** a student uses `claude --continue`, **When** they resume after 24+ hours, **Then** they can pick up exactly where they left off because progress files contain: completed items, in-progress items, blocked items, decisions made, and known issues.

---

### User Story 5 — Preventing Workflow Drift (Priority: P2)

A student notices that Claude starts following their instructions at turn 1, but by turn 20 has drifted significantly from original intent. They want to understand WHY this happens and HOW to prevent it.

**Why this priority**: Workflow drift is the subtle quality killer—the difference between agents that maintain consistency and agents that gradually diverge.

**Independent Test**: Student can explain the workflow drift problem, implement PreToolUse memory injection, and maintain instruction compliance throughout a 50+ turn conversation.

**Acceptance Scenarios**:

1. **Given** a student understands workflow drift, **When** they trace a 30-turn conversation, **Then** they can identify where original instructions became less relevant to current work.

2. **Given** a student implements memory injection, **When** Claude prepares to call a tool (PreToolUse), **Then** relevant memories are injected based on Claude's current thinking—not just the original prompt.

3. **Given** a student has deduplication in place, **When** the same memory is relevant across multiple tool calls, **Then** it's injected once with a temp log hash—not repeatedly cluttering context.

---

### User Story 6 — Coordinating Multi-Agent Systems (Priority: P2)

A student is building a system with multiple subagents. They notice agents sometimes conflict or make inconsistent assumptions. They want to learn HOW to isolate context effectively.

**Why this priority**: Multi-agent systems are where context engineering becomes architecture—the patterns here directly apply to production Digital FTEs.

**Independent Test**: Student can compare dirty slate vs clean context patterns, implement orchestrator-based isolation, and demonstrate improved quality in multi-agent workflows.

**Acceptance Scenarios**:

1. **Given** a student has a 3-step task (Research → Analyze → Write), **When** they compare dirty slate (single agent) vs clean context (orchestrator with 3 isolated subagents), **Then** the clean context version produces higher quality outputs with fewer confusion errors.

2. **Given** a student understands context amnesia, **When** they launch a subagent, **Then** they preload project knowledge via Skills or include critical context in the delegation prompt—never assuming subagents inherit parent context.

3. **Given** a student designs multi-agent architecture, **When** they choose between stateless (subagent), stateful (handoff), and shared (network) patterns, **Then** they can justify their choice based on use case requirements.

---

### User Story 7 — Applying Decision Frameworks (Priority: P3)

A student has learned all the context engineering techniques. They want a systematic way to decide WHICH technique to apply WHEN.

**Why this priority**: Integration lesson that transforms knowledge into practice. Without decision frameworks, students apply techniques randomly.

**Independent Test**: Student can analyze a context-related quality issue, traverse the decision tree to identify the appropriate technique, and apply it correctly.

**Acceptance Scenarios**:

1. **Given** a student encounters context noise, **When** they use the decision tree, **Then** they identify "Signal-to-noise audit (Lesson 4)" as the solution and apply it.

2. **Given** a student encounters workflow drift, **When** they use the decision tree, **Then** they identify "Memory injection (Lesson 8)" as the solution and implement it.

3. **Given** a student builds a production agent, **When** they apply the full toolkit, **Then** the agent demonstrates: consistent quality at turn 1 and turn 50 (attention management), session resumption after 24h (progress files), no workflow drift (memory injection), and clean multi-agent coordination (context isolation).

---

### Edge Cases

- **Student confusion**: What if student thinks this is about writing better prompts (prompt engineering)?
  - Address explicitly: Prompt engineering is 2023. Context engineering is 2026. Prompts are 50-200 tokens; context windows are 200,000+. This is about engineering the ENTIRE context, not just the prompt.

- **Tool confusion**: What if student confuses Chapter 3 (HOW to use tools) with Chapter 4 (WHY tools work)?
  - Address: Chapter 3 taught you to create a CLAUDE.md. Chapter 4 teaches you why a 47-line CLAUDE.md outperforms a 400-line one.

- **Premature optimization**: What if student tries to optimize context before they have quality issues?
  - Address: Context engineering is quality control. You apply it when quality matters. For throwaway experiments, it's overkill. For sellable Digital FTEs, it's essential.

- **Tool-specific thinking**: What if student thinks these techniques only work with Claude Code?
  - Address: Labs must be GENERAL. The principles (attention budget, position sensitivity, context rot) apply to ANY General Agent. Examples use Claude Code because students know it; the concepts transfer.

---

## Requirements

### Functional Requirements

**Core Frameworks (MUST teach)**:

- **FR-001**: Chapter MUST teach the **Attention Budget** model:
  - Context window != equal attention (U-shaped curve)
  - Beginning 10% and End 10% get ~70% accuracy
  - Middle 80% gets ~40% accuracy
  - 70% utilization threshold for quality degradation
  - Zone system: Green (0-50%), Yellow (50-70%), Orange (70-85%), Red (85-95%), Black (95%+)

- **FR-002**: Chapter MUST teach **Position Sensitivity** (Lost in the Middle research):
  - Primacy effect (first items anchor attention)
  - Recency effect (last items freshest in memory)
  - Middle blindness (attention is finite)
  - Three-zone CLAUDE.md strategy (critical → beginning, reference → middle, workflow → end)
  - 30% accuracy drop for middle vs edge positioning

- **FR-003**: Chapter MUST teach the **4 Types of Context Rot**:
  - Poisoning: Outdated information persists
  - Distraction: Irrelevant content dilutes attention
  - Confusion: Similar concepts conflate
  - Clash: Contradictory instructions compete

- **FR-004**: Chapter MUST teach **Signal vs Noise Audit** framework:
  - 4-question classification: Would Claude ask? Could Claude figure out? Does this change frequently? Is this default convention?
  - <60 line CLAUDE.md target (research shows ~150-200 instruction limit)
  - Progressive disclosure via file references

- **FR-005**: Chapter MUST teach **Context Lifecycle Management**:
  - /clear vs /compact decision framework
  - Custom compaction instructions
  - Session persistence (--continue, --resume)
  - 3-day conversation viability rule

- **FR-006**: Chapter MUST teach **Long-Horizon Progress Architecture**:
  - Initializer agent + Coding agent pattern (Harrison Chase)
  - Progress file template (Completed, In Progress, Blocked, Decisions Made, Known Issues)
  - Feature decomposition (10-15 granular tasks)
  - Commit checkpoint pattern

- **FR-007**: Chapter MUST teach **Mid-Stream Memory Injection**:
  - UserPromptSubmit vs PreToolUse injection timing
  - Thinking block extraction for semantic memory
  - Deduplication with temp log + thinking hash
  - <500ms performance target

- **FR-008**: Chapter MUST teach **Context Isolation Patterns**:
  - Dirty slate problem (linear pipeline with accumulated pollution)
  - Clean context pattern (orchestrator with fresh context per subagent)
  - Subagent design patterns: Stateless, Stateful (Handoff), Shared (Network)
  - Context amnesia workarounds

**Pedagogical Requirements**:

- **FR-009**: Each lesson MUST follow structure: Question → Mental Model → Claude Code Application → Lab → Try With AI (3 prompts)

- **FR-010**: Labs MUST be tool-agnostic in principle (work with any General Agent), though examples use Claude Code

- **FR-011**: Each lesson MUST end with "Try With AI" section (action prompts, not meta-commentary per Constitution v6.0.1)

- **FR-012**: Chapter MUST NOT repeat Chapter 3 content (tool usage); must focus on WHY and WHEN

- **FR-013**: Chapter MUST explicitly connect to Principle 5 "Persisting State in Files" as the implementation discipline

- **FR-014**: All statistics and research claims MUST be cited from authoritative sources

### Key Entities

- **Attention Budget**: The finite attention resource distributed across context; not all tokens receive equal weight
- **Position Sensitivity**: The phenomenon where information recall varies by position (U-shaped curve)
- **Context Rot**: Degradation of context quality over time through 4 mechanisms
- **Signal-to-Noise Ratio**: Proportion of useful context vs wasteful context
- **Context Zone**: Classification of context utilization (Green/Yellow/Orange/Red/Black)
- **Progress File**: Persistent file tracking multi-session work state
- **Memory Injection**: Technique to insert relevant context at execution time
- **Context Isolation**: Pattern to prevent context pollution between agents

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: 80%+ students can correctly identify context zone from `/usage` output and recommend appropriate action
- **SC-002**: 80%+ students can classify CLAUDE.md content as SIGNAL or NOISE using 4-question framework
- **SC-003**: 75%+ students can restructure CLAUDE.md using three-zone position strategy
- **SC-004**: 75%+ students can design progress file architecture for multi-session feature
- **SC-005**: 70%+ students can explain workflow drift and propose PreToolUse injection solution
- **SC-006**: 70%+ students can compare dirty slate vs clean context patterns and identify when to use each
- **SC-007**: 90%+ students can traverse context engineering decision tree to identify appropriate technique
- **SC-008**: 80%+ students demonstrate improved agent quality after applying chapter techniques (measured via lab outcomes)
- **SC-009**: 100% of statistics and research claims are verifiable from cited sources
- **SC-010**: All lessons pass anti-convergence checklist (no meta-commentary, framework invisible)

### Quality Gates

- **QG-001**: Chapter validates Principle 5 connection explicitly in Lesson 1 and Lesson 10
- **QG-002**: No lesson repeats Chapter 3 HOW content; all lessons focus on WHY and WHEN
- **QG-003**: All labs produce concrete artifacts (audit report, optimized CLAUDE.md, progress template, memory hook, comparison evidence)
- **QG-004**: Capstone lab produces production-quality agent demonstrating all techniques

---

## Constraints

- **No code implementations** beyond configuration and shell commands—this is engineering discipline, not programming
- **No Chapter 3 repetition**—students already know how to use the tools
- **Labs must be tool-agnostic in principle**—concepts transfer to any General Agent
- **All statistics must be cited**—no hallucinated numbers
- **B1 proficiency level**—assume intermediate Claude Code experience
- **Framework invisible in student-facing content**—Three Roles, Layer terminology not exposed

---

## Non-Goals

- Teaching how to create CLAUDE.md files (Chapter 3, Lesson 5)
- Teaching how to create Skills (Chapter 3, Lessons 7-8)
- Teaching how to configure Subagents (Chapter 3, Lesson 9)
- Teaching how to set up Hooks (Chapter 3, Lesson 13)
- Teaching how to install MCP servers (Chapter 3, Lesson 10)
- Seven Principles framework (Chapter 5)
- Custom Agent SDK development (Part 5, Chapters 34-36)
- Production deployment (Part 6)

---

## Assumptions

- Students have completed Chapter 3 (General Agents tools proficiency)
- Students have created at least one CLAUDE.md file
- Students have used Claude Code for at least one multi-session task
- Students have encountered context-related quality issues (even if they didn't identify them as such)
- Internet access for "Try With AI" sections
- Claude Pro/Max subscription or equivalent backend for labs

---

## References

### Research Sources

- **Liu et al. 2023**: "Lost in the Middle: How Language Models Use Long Contexts" (Stanford/Berkeley) — https://arxiv.org/abs/2307.03172
- **Chroma Research**: "Context Rot Research" — https://research.trychroma.com/context-rot
- **TALE Framework**: "Token-Budget-Aware LLM Reasoning" — https://arxiv.org/abs/2412.18547

### Industry Sources

- **The New Stack**: "Better Context Will Always Beat a Better Model" — Srinivasan Sekar
- **The New Stack**: "Context is AI Coding's Real Bottleneck in 2026" — Greg Foster
- **HumanLayer**: "Writing a Good CLAUDE.md" — https://www.humanlayer.dev/blog/writing-a-good-claude-md

### Technical Sources

- **GitHub**: "Agent Skills for Context Engineering" — Muratcan Koylan — https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering
- **OpenAI Cookbook**: "Agents SDK: Context Personalization" — https://cookbook.openai.com/examples/agents_sdk/context_personalization
- **LangChain**: "Deep Agents" — https://docs.langchain.com/oss/python/deepagents/overview
- **Twitter/X**: @PerceptualPeak on PreToolUse Memory Injection — January 2026

### Project References

- **Constitution**: `.specify/memory/constitution.md` (v7.0.0)
- **Chapter 3**: `apps/learn-app/docs/01-General-Agents-Foundations/03-general-agents/`
- **Chapter 4 (current, becomes 5)**: `apps/learn-app/docs/01-General-Agents-Foundations/04-seven-principles/`
- **Research Notes**: `workspace/chapter4-context-engineering-DEEP-v3.md`

---

## Suggested Lesson Structure

Based on user stories and research alignment, suggested **10-lesson structure**:

| Lesson | Title                                                                 | Core Teaching                                            | User Story | Primary Deliverable                               |
| ------ | --------------------------------------------------------------------- | -------------------------------------------------------- | ---------- | ------------------------------------------------- |
| 1      | The Manufacturing Quality Problem: Why Context Determines Agent Value | Context as quality control for Digital FTE manufacturing | US1        | Diagnostic report of context-related quality gaps |
| 2      | The Attention Budget: Why More Context ≠ Better Results               | U-shaped attention curve, 70% threshold, zone system     | US2        | Graph of quality vs context utilization           |
| 3      | Lost in the Middle: Where Information Goes to Die                     | Position sensitivity, three-zone strategy                | US2        | Compliance rates by position (test results)       |
| 4      | Signal vs Noise: Auditing Your Context for Quality                    | 4-question audit framework, <60 line target              | US3        | Optimized <60 line CLAUDE.md                      |
| 5      | The Two-Way Problem: Getting Tacit Knowledge In and Out               | Tacit knowledge extraction, memory lifecycle             | US4        | Tacit knowledge document                          |
| 6      | Context Lifecycle: Knowing When to Reset vs Compress                  | /clear vs /compact decision framework, zones             | US2        | Context utilization growth log                    |
| 7      | Long-Horizon Work: Progress Files and Session Architecture            | Progress file template, commit checkpoint pattern        | US4        | Working feature + progress template               |
| 8      | Mid-Stream Memory: Injecting Context at Execution Time                | PreToolUse injection, thinking block extraction          | US5        | Working semantic memory hook                      |
| 9      | Context Isolation: Why Clean Slates Beat Dirty States                 | Dirty vs clean comparison, orchestrator pattern          | US6        | Quality comparison evidence                       |
| 10     | The Context Engineering Playbook: Decision Frameworks for Quality     | Decision tree, full toolkit integration                  | US7        | Production-quality specialized agent              |

**Lesson Justification** (from research):

- Lessons 1-4: Foundation (understanding WHY context matters)
- Lessons 5-7: Persistence (HOW to maintain state across sessions)
- Lessons 8-9: Advanced (preventing drift, isolating agents)
- Lesson 10: Integration (applying the full toolkit)

**Total Lab Time**: ~15 hours of hands-on practice producing 10 concrete artifacts

---

## Chapter Renumbering Impact

This chapter insertion requires renumbering:

| Current                                | After Insertion                                    |
| -------------------------------------- | -------------------------------------------------- |
| Chapter 3: Working with General Agents | Chapter 3: Working with General Agents (unchanged) |
| Chapter 4: Seven Principles            | Chapter 5: Seven Principles                        |
| —                                      | Chapter 4: Effective Context Engineering (NEW)     |

**Files to update**:

- `apps/learn-app/docs/01-General-Agents-Foundations/04-seven-principles/` → rename to `05-seven-principles/`
- Create `apps/learn-app/docs/01-General-Agents-Foundations/04-context-engineering/`
- Update all internal links referencing "Chapter 4" or "Chapter 5"
- Update `sidebar_position` in affected README.md files

---

## Success Validation

**This chapter succeeds when**:

1. Students understand WHY context quality determines agent value (not just HOW to use tools)
2. Students can diagnose context-related issues using specific frameworks (attention budget, position sensitivity, rot types)
3. Students apply context engineering as a systematic discipline (not random optimization)
4. Students connect context engineering to Digital FTE manufacturing quality (thesis alignment)
5. Students are prepared for Principle 5 "Persisting State in Files" with deep understanding of WHY it works

**This chapter fails when**:

- Students learn techniques without understanding underlying mechanics
- Content repeats Chapter 3 tool usage instead of engineering discipline
- Labs produce no artifacts or non-transferable artifacts
- Thesis connection (Digital FTE manufacturing quality) is missing or weak
- Principle 5 connection is not explicit
