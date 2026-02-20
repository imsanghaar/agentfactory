---
sidebar_position: 4
title: "Phase 1: Parallel Research with Subagents"
description: "Transform hours of sequential investigation into minutes of parallel discovery using Claude's subagent architecture"
keywords:
  [
    "spec-driven development",
    "parallel research",
    "subagents",
    "claude code",
    "context isolation",
    "reference implementation",
    "research pattern",
  ]
chapter: 5
lesson: 4
duration_minutes: 30

# HIDDEN SKILLS METADATA
skills:
  - name: "Execute Parallel Research Pattern"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can invoke parallel subagent research using the correct prompt pattern"

  - name: "Decompose Research Questions"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can break a complex investigation into 3-5 independent research threads"

  - name: "Synthesize Multi-Agent Findings"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can compare findings from multiple research agents and identify patterns or conflicts"

learning_objectives:
  - objective: "Apply the parallel research prompt pattern to spawn multiple investigation agents"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student successfully invokes parallel research and receives findings from multiple subagents"

  - objective: "Decompose a research problem into independent investigation threads"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student creates a research breakdown with 3-5 non-overlapping focus areas"

  - objective: "Explain why context isolation makes parallel research superior to sequential investigation"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can articulate the benefits of fresh context per agent versus accumulated context"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (parallel research pattern, subagent spawning, context isolation, research decomposition, finding synthesis) within A2-B1 range"

differentiation:
  extension_for_advanced: "Compare Claude's parallel subagent approach to traditional web scraping or API-based research automation"
  remedial_for_struggling: "Focus on the single prompt pattern first, then understand decomposition after seeing results"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 2
  session_title: "Deep-Dive into SDD Phases"
  key_points:
    - "The trigger phrase 'Spin up multiple subagents' activates parallel research — students need to remember this exact prompt pattern"
    - "Context isolation is the real advantage over sequential research — each agent starts fresh without assumptions from other agents' findings"
    - "Research decomposition quality determines output quality — threads must be independent, focused, bounded, and complementary"
    - "Conflicts between agents are features, not bugs — they surface genuine design decisions that would otherwise be hidden assumptions"
  misconceptions:
    - "Students think parallel research is just 'faster reading' — emphasize that context isolation changes research quality, not just speed"
    - "Students assume agents collaborate during research — each agent works in complete isolation and reports back independently"
    - "Students create overlapping research threads — demonstrate how overlap causes redundant findings while gaps miss critical information"
  discussion_prompts:
    - "When you research something manually, do you notice how learning about topic A changes how you interpret topic B? Is that always helpful?"
    - "What kind of research question would be WRONG for parallel investigation — where sequential dependency is actually needed?"
  teaching_tips:
    - "Have students run the IndexedDB example prompt live to see agents spawn and return — the experience is more convincing than explanation"
    - "The sequential vs parallel comparison table is worth drawing out — focus on the 'Conflicts: hidden vs visible' row"
    - "Walk through the decomposition template step by step with a student-chosen example before the lab exercise"
    - "The Agent Teams callout box (for inter-agent debate) is a forward reference to Ch4 L9 — mention it but don't dwell on it"
  assessment_quick_check:
    - "Write a 3-thread research decomposition for a topic of your choice using the template"
    - "Explain why two agents finding conflicting recommendations is more valuable than one agent picking a winner"
---

# Phase 1: Parallel Research with Subagents

In Lesson 3, you learned the four-phase SDD workflow. Now you'll execute the first phase: research that transforms hours of sequential reading into parallel minutes.

Here's the economics that makes this lesson worth your time. That reference implementation you've been meaning to understand? The library documentation you've been piecing together? The architecture decisions scattered across multiple files? What would take you four hours of sequential reading, Claude can investigate in twenty minutes using parallel research agents.

This isn't about AI reading faster. It's about architecture. Claude's subagent system lets you spawn multiple independent investigators, each with fresh context, each focused on a specific question. While one agent studies CRDT data structures, another examines WebSocket protocols, a third analyzes storage patterns, and a fourth maps overall architecture. They don't wait for each other. They don't cross-contaminate each other's understanding. They report back simultaneously.

## The Prompt Pattern

The pattern that activates parallel research is direct:

```
Spin up multiple subagents for your research task
```

That's the trigger. When Claude sees this instruction alongside a research goal, it spawns 3-5 independent agents. Each agent operates in isolation, investigates one aspect, and returns findings. You receive parallel perspectives without the accumulated confusion of sequential conversation.

### What Happens Behind the Scenes

When you invoke parallel research, Claude:

1. **Analyzes your research goal** to identify distinct investigation threads
2. **Spawns independent subagents** (typically 3-5, depending on complexity)
3. **Assigns each agent a focused question** without overlap
4. **Collects findings** as agents complete their work
5. **Synthesizes results** into a consolidated summary

The key architectural insight: each subagent starts with fresh context. When Agent 2 investigates WebSocket patterns, it doesn't carry assumptions from Agent 1's CRDT analysis. This isolation prevents the cross-contamination that plagues sequential research conversations.

## A Real Example: IndexedDB Migration Research

Here's what parallel research looks like in practice. Alex, a developer building a local-first application, needed to migrate from SQLite to IndexedDB while adding real-time sync capabilities. The investigation required understanding:

- CRDT (Conflict-free Replicated Data Types) for sync
- WebSocket protocols for real-time updates
- IndexedDB persistence patterns
- Overall architectural integration

Sequential approach: research CRDTs, then WebSockets, then IndexedDB, then architecture. Each phase builds on the previous. Estimated time: 3-4 hours of reading and note-taking.

Parallel approach: spawn four agents simultaneously.

**Alex's prompt:**

```
I need to understand how to implement local-first sync with IndexedDB.

Spin up multiple subagents for your research task:

1. CRDT data structures — focus on CoMap, CoList patterns for collaborative data
2. WebSocket sync protocols — focus on the 4-message handshake pattern
3. Storage persistence — focus on IndexedDB patterns for offline-first apps
4. Overall architecture — how these pieces integrate together

Reference repo: [link to jazz.tools or similar implementation]
```

**What returned:**

- **Agent 1** reported on CRDT primitives, comparing CoMap (key-value) vs CoList (ordered sequences), with code examples from the reference
- **Agent 2** documented the WebSocket handshake: `connect → authenticate → subscribe → sync`, with message formats
- **Agent 3** analyzed IndexedDB transaction patterns, noting the async nature and common gotchas
- **Agent 4** mapped how CRDT changes flow through WebSocket to IndexedDB, identifying the sync manager as the central orchestrator

**Time elapsed**: 18 minutes instead of 4 hours.

More importantly, the findings were independent. Agent 1's CRDT understanding didn't assume anything about storage. When Alex later found that IndexedDB had limitations Agent 3 hadn't considered, it didn't invalidate the CRDT or WebSocket research.

## Why Parallel Works Better

The advantage isn't just speed. Context isolation changes the quality of research.

| Aspect            | Sequential Research                               | Parallel Research                          |
| ----------------- | ------------------------------------------------- | ------------------------------------------ |
| **Context**       | Accumulates with each topic                       | Fresh per agent                            |
| **Assumptions**   | Early findings influence later investigation      | Each agent investigates independently      |
| **Conflicts**     | Hidden (later research adapts to earlier)         | Visible (agents may report contradictions) |
| **Revision cost** | High (must re-research if early assumption wrong) | Low (only affected thread needs revision)  |

**Hidden conflicts become visible.** When you research sequentially, you unconsciously reconcile contradictions as you go. Agent 1 says "use approach A." By the time you get to related research, you're looking for information that supports A, not challenges it.

With parallel research, Agent 1 might recommend approach A while Agent 3 recommends approach B for the same problem. That conflict is valuable information. It means you have a genuine design decision to make, not an assumption that slipped through.

**Revision stays surgical.** If you discover Agent 2's WebSocket analysis missed something critical, you re-run Agent 2. Agents 1, 3, and 4 are unaffected. In sequential research, late-stage discoveries often invalidate earlier work because of accumulated assumptions.

> **Beyond subagents:** For research tasks where investigators need to _challenge each other's findings_ rather than report independently, Claude Code's **Agent Teams** (Chapter 4, Lesson 9) enable direct inter-agent communication. Subagents work well when only the result matters. Agent teams work better when the debate between investigators produces the real insight.

## Constructing Effective Research Requests

The quality of parallel research depends on how you decompose your investigation. Effective decomposition creates threads that are:

- **Independent**: Each agent can complete without information from others
- **Focused**: Each agent has a clear, answerable question
- **Bounded**: Each agent knows what's in scope and what's not
- **Complementary**: Together, agents cover the full problem space

### Decomposition Template

```markdown
Research Task: [HIGH-LEVEL GOAL]

Spawn parallel subagents to investigate:

1. [ASPECT 1] — focus on [SPECIFIC QUESTION]
2. [ASPECT 2] — focus on [SPECIFIC QUESTION]
3. [ASPECT 3] — focus on [SPECIFIC QUESTION]
   [4-5. Add more if complexity warrants]

Reference: [CODEBASE/DOCUMENTATION/EXAMPLE]

Return: Written summary of findings for each aspect
```

### Example Decompositions

**For understanding an authentication system:**

```markdown
Research Task: Understand how [app] implements OAuth

Spawn parallel subagents to investigate:

1. Token management — how are tokens stored, refreshed, and validated?
2. Session handling — how does the app track logged-in state?
3. Provider integration — how are external OAuth providers configured?
4. Security measures — what protections exist against token theft?

Reference: @src/auth/
```

**For evaluating a new library:**

```markdown
Research Task: Evaluate FastAPI for our agent API layer

Spawn parallel subagents to investigate:

1. Async patterns — how does FastAPI handle concurrent requests?
2. Validation — how does Pydantic integration work for request/response?
3. Dependency injection — how do we structure shared services?
4. Testing — what testing patterns does FastAPI support?

Reference: FastAPI documentation and @existing-api/
```

**For analyzing a performance issue:**

```markdown
Research Task: Investigate why dashboard loads slowly

Spawn parallel subagents to investigate:

1. Database queries — which queries take longest? Are indexes used?
2. API response times — where is latency introduced?
3. Frontend rendering — what's the component render timeline?
4. Network waterfall — what resources block first paint?

Reference: @src/dashboard/ and browser profiling data
```

## Receiving and Using Research Findings

When parallel research completes, you receive structured findings from each agent. Your job is synthesis: identifying patterns, conflicts, and implications.

### Pattern Recognition

Look for themes that appear across multiple agents:

- "Agent 1 and Agent 3 both mention the importance of idempotent operations"
- "All four agents reference the event bus as the integration point"
- "Agents 2, 3, and 4 assume a specific data model—Agent 1 challenges that assumption"

### Conflict Identification

Conflicts between agents often indicate genuine design decisions:

- "Agent 2 recommends optimistic updates; Agent 4 recommends pessimistic locking"
- "Agent 1 uses sync storage; Agent 3 assumes async transactions"
- "Agent 3 and Agent 4 disagree on error handling responsibility"

These conflicts become inputs to Phase 3 (Refinement) where you'll resolve ambiguities before implementation.

### Implications for Specification

Research findings directly feed your specification:

| Finding Type           | Spec Section It Informs                 |
| ---------------------- | --------------------------------------- |
| Discovered patterns    | Part 1: Reference Architecture Analysis |
| Current state analysis | Part 2: Current Architecture Analysis   |
| Identified conflicts   | Input for Phase 3 interview questions   |
| Best practices         | Part 3: Implementation Plan             |
| Constraints discovered | Constraints section                     |

## Common Research Scenarios

### Scenario 1: Understanding a Reference Implementation

You found a project that does something similar to what you need. Parallel research can dissect it:

```markdown
Research Task: Understand how [repo] implements real-time collaboration

Spawn parallel subagents to investigate:

1. Data model — what entities exist and how do they relate?
2. Sync mechanism — how do changes propagate between clients?
3. Conflict resolution — how are simultaneous edits handled?
4. Offline support — how does the app work without network?

Reference: [repo URL]
```

### Scenario 2: Evaluating Technology Options

You're deciding between two approaches. Research can inform the decision:

```markdown
Research Task: Compare WebSocket vs Server-Sent Events for our use case

Spawn parallel subagents to investigate:

1. WebSocket capabilities — bidirectional, connection management, scaling
2. SSE capabilities — unidirectional, reconnection, browser support
3. Our requirements — what do we actually need? (broadcast? bidirectional?)
4. Infrastructure impact — how does each choice affect our deployment?

Reference: Our architecture docs at @docs/architecture.md
```

### Scenario 3: Auditing Existing Code

You inherited code and need to understand it:

```markdown
Research Task: Audit the payment processing module

Spawn parallel subagents to investigate:

1. Transaction flow — how does a payment move through the system?
2. Error handling — how are failures captured and recovered?
3. Security — what sensitive data exists and how is it protected?
4. External dependencies — what third-party services are involved?

Reference: @src/payments/
```

## Lab: Execute Your First Parallel Research

**Objective:** Apply the parallel research pattern to a real investigation need.

### Task

Choose a research goal that's been on your backlog. Maybe it's understanding a library, auditing code you inherited, or investigating how a reference project implements something.

Construct a research request using the template:

```markdown
Research Task: [Your goal]

Spawn parallel subagents to investigate:

1. [Aspect] — focus on [question]
2. [Aspect] — focus on [question]
3. [Aspect] — focus on [question]

Reference: [What agents should examine]

Return: Written summary of findings for each aspect
```

### Evaluation Criteria

Your decomposition is effective if:

- [ ] Each aspect can be investigated independently (no "first do X, then Y")
- [ ] Each focus question is specific enough to answer definitively
- [ ] Together, the aspects cover your full research need
- [ ] No two aspects substantially overlap

Run the research. When findings return, identify:

- What patterns appeared across multiple agents?
- Did any agents report conflicting information?
- What design decisions do the findings imply?

## Try With AI

**Running Example Continued:** We're writing "Personal AI Employees in 2026" for CTOs. Now we research the landscape in parallel.

**Prompt 1: Parallel Research on AI Tools**

```
I'm writing a report on personal AI employees for CTOs evaluating
tools like Claude Code, Cursor, and GitHub Copilot.

Spin up multiple subagents for your research task:

1. Tool capabilities — What can each tool actually do today?
2. Business ROI — What cost/productivity data exists?
3. Implementation risks — What do companies struggle with?
4. Future trajectory — Where is this category heading?

Write findings to research.md with a section per agent.
```

**What you're learning:** Each agent investigates independently. Agent 1 discovers Claude Code can run autonomously while Copilot needs more guidance. Agent 2 finds ROI studies. Neither pollutes the other's findings. Conflicts (Agent 1 says X is best, Agent 4 says Y is trending) surface real decisions.

**Prompt 2: Synthesis**

```
Read research.md. Create a synthesis section:
- What appeared in multiple agents' findings?
- Where did agents find conflicting information?
- What structure does this suggest for our report?
```

**What you're learning:** Four agents produce four perspectives. Synthesis reveals what CTOs must know (appears everywhere) versus what's optional depth. Conflicts become explicit: "Agent 2 found ROI data, Agent 3 found skepticism"—both belong in an honest report.

**Prompt 3: Gap Analysis**

```
Based on research.md, what's MISSING that a CTO would need?
We have tool capabilities and ROI, but what practical questions
would a CTO ask that our research doesn't answer?
```

**What you're learning:** Research isn't just collecting data—it's identifying gaps. CTOs might ask: "How do we measure success?" "What's the learning curve?" "How do we handle security review?" If research.md doesn't answer these, the spec needs to address how we'll fill them.
