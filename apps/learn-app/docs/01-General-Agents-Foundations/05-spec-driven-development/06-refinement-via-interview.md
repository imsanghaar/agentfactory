---
sidebar_position: 6
title: "Phase 3: Refinement via Interview"
description: "Surface design decisions and ambiguities before implementation through structured AI interviews using the ask_user_question tool"
keywords:
  [
    "spec-driven development",
    "refinement phase",
    "ask_user_question",
    "design decisions",
    "ambiguity resolution",
    "interview pattern",
    "implementation planning",
  ]
chapter: 5
lesson: 6
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "Apply Interview Pattern for Spec Refinement"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can trigger the interview pattern and respond to AI questions to refine their specification"

  - name: "Identify Common Ambiguity Categories"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can list the five categories where ambiguities commonly hide in specifications"

  - name: "Evaluate Specification Completeness"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can use the interview checklist to assess whether their specification is implementation-ready"

learning_objectives:
  - objective: "Apply the ask_user_question prompt pattern to surface specification ambiguities"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student successfully triggers an AI interview and responds to clarifying questions"

  - objective: "Explain why each ambiguity found before coding saves 10x time during implementation"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can articulate the cost multiplier of mid-implementation pivots"

  - objective: "Use the interview checklist to validate specification completeness"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student can apply the checklist categories to their own specifications"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (interview pattern, ask_user_question tool, ambiguity categories, 10x cost multiplier, interview checklist) within B1 range"

differentiation:
  extension_for_advanced: "Design custom interview questions for domain-specific specifications beyond the standard checklist"
  remedial_for_struggling: "Focus on the five ambiguity categories first, then practice the prompt pattern"

teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "Deep-Dive into SDD Phases"
  key_points:
    - "The role reversal is the key insight — in refinement, Claude asks questions and you answer, which surfaces gaps you didn't know existed"
    - "The 10x cost multiplier table (5 min during spec → 8-16 hours in production) is the most persuasive argument for why this phase can't be skipped"
    - "Five ambiguity categories (data decisions, conflict resolution, pattern selection, failure recovery, boundary conditions) give students a repeatable checklist"
    - "The 'handle conflicts optimistically' example shows how a two-word ambiguity can cost three days of refactoring"
  misconceptions:
    - "Students think refinement means 'Claude proofreading the spec' — it's Claude interrogating your unstated assumptions, not checking grammar"
    - "Students skip refinement because their spec 'feels complete' — the whole point is surfacing assumptions so natural you didn't think to write them down"
    - "Students get annoyed by Claude's questions and cut the interview short — annoyance often signals you haven't thought through those decisions"
  discussion_prompts:
    - "Think of a project where a 'small detail' you didn't specify upfront caused a major rework — which ambiguity category did it fall into?"
    - "Why is it harder to find your own unstated assumptions than to find someone else's?"
  teaching_tips:
    - "Have students run the interview prompt live on their Lesson 5 spec — the experience of Claude finding real gaps is more convincing than any lecture"
    - "The cost multiplier table is worth dwelling on — ask students to estimate their own 'most expensive late-found ambiguity'"
    - "Walk through the report-spec interview example step by step: question → answer → spec update. Show how three questions prevented three rewrites"
    - "The 'when to stop' section prevents analysis paralysis — emphasize that implementation details are not design decisions"
  assessment_quick_check:
    - "Name the five ambiguity categories and give an example question for each"
    - "What's the prompt pattern that triggers Claude's interview mode, and why does the role reversal matter?"
---

# Phase 3: Refinement via Interview

Every ambiguity you find before coding saves 10x the time it would cost to fix mid-implementation.

In Lesson 4, you learned to write effective specifications. But even well-structured specs contain hidden assumptions. You know what "conflict resolution" means in your head. Does Claude? You imagine the error handling approach. Did you write it down?

This lesson teaches the refinement phase: a structured interview where Claude surfaces every design decision that would otherwise become a mid-implementation pivot. The result is a specification precise enough that implementation becomes execution of a well-understood plan.

## The Interview Pattern

The refinement phase uses a specific prompt pattern that triggers Claude's ask_user_question tool:

```
Here's my spec. Use the ask_user_question tool to surface any ambiguities
before we implement.
```

When you give this instruction, Claude shifts from implementation mode to investigation mode. Instead of generating code, Claude reads your specification critically and asks questions about anything unclear, unstated, or potentially problematic.

**What makes this different from conversation:**

In normal prompting, you ask questions and Claude answers. In the interview pattern, the roles reverse. Claude asks questions and you answer. This shift matters because Claude can identify gaps you didn't know existed—assumptions so natural to you that you didn't think to document them.

## Why Ambiguities Are Expensive

Consider what happens when an ambiguity survives to implementation:

| When Discovered        | What Happens                                     | Time Cost  |
| ---------------------- | ------------------------------------------------ | ---------- |
| **During spec**        | Add clarification, continue                      | 5 minutes  |
| **During interview**   | Answer question, update spec                     | 10 minutes |
| **During coding**      | Stop, discuss, decide, restart                   | 30 minutes |
| **After first commit** | Code review reveals issue, refactor needed       | 2-4 hours  |
| **In production**      | Bug report, investigation, emergency fix, review | 8-16 hours |

The 10x multiplier is conservative. A decision that takes 10 minutes to clarify in an interview can cost days when discovered after deployment.

**Real example:** A developer's specification said "handle conflicts optimistically." The developer meant "last write wins." Claude interpreted this as "prompt user to resolve." Implementation proceeded with user prompts. The developer discovered this three days later during testing. Refactoring took an entire afternoon—time that a single interview question would have prevented.

## The Five Ambiguity Categories

Claude's interview questions cluster around five categories. Understanding these helps you anticipate questions and write better specs proactively.

### 1. Data Decisions

How existing information transitions to the new system:

- Should we migrate existing data or start fresh?
- What happens to records that don't match the new schema?
- How do we handle data from the old system during the transition period?

**Why this matters:** Data decisions are often unstated because developers assume "obviously we keep our data." But the HOW requires explicit decisions.

### 2. Conflict Resolution

What happens when systems disagree:

- What's the conflict resolution strategy? (Last write wins? User resolves? Merge automatically?)
- If two users edit simultaneously, who wins?
- What happens when local and server state diverge?

**Why this matters:** Every multi-user or distributed system faces conflicts. The absence of a stated strategy means Claude chooses one—possibly not the one you wanted.

### 3. Pattern Selection

Which approach among valid alternatives:

- The research found two patterns for this. Which matches your constraints?
- Should we use the approach from [reference A] or [reference B]?
- Given your performance requirements, which architecture fits?

**Why this matters:** Research often surfaces multiple valid approaches. Without explicit selection, Claude picks based on its training distribution—not your project's needs.

### 4. Failure Recovery

What happens when things go wrong:

- What's the failure recovery approach?
- If the external API times out, do we retry, queue, or fail?
- What state should the system preserve after a crash?

**Why this matters:** Happy path specifications are common. Error path specifications are rare. But production systems spend significant time in error states.

### 5. Boundary Conditions

Where the system's scope ends:

- What happens at the rate limit boundary?
- How do we handle users who exceed storage quotas?
- What's the maximum scale this needs to support?

**Why this matters:** Specifications often describe the normal case. Edge cases at boundaries are where implementations diverge from intent.

## The Interview in Action

Here's what a refinement interview looks like with our report specification:

**Your specification includes:**

```markdown
## Tool Comparison Section

Compare Claude Code, Cursor, and GitHub Copilot on key dimensions
relevant to CTO decision-making.
```

**Claude's interview questions:**

> Question 1: For the tool comparison—should we include pricing? Enterprise pricing is often confidential or negotiated. Do we use list prices, price ranges, or skip pricing entirely?

Your answer: "Include list prices where public, note 'contact for enterprise pricing' otherwise. CTOs need ballpark numbers to budget."

> Question 2: The spec mentions 'key dimensions.' Which dimensions matter most to CTOs? Technical capabilities? Security compliance? Learning curve? Integration difficulty?

Your answer: "Good catch. Prioritize: (1) security/compliance, (2) integration with existing tools, (3) learning curve, (4) technical capabilities. CTOs care about adoption risk before features."

> Question 3: How should we handle rapidly changing information? Tool capabilities change monthly. Should we include version numbers? Publish dates? Caveats about currency?

Your answer: "Include 'as of [date]' header. Note that capabilities change rapidly. Link to official docs for current features."

**Specification updates based on answers:**

```markdown
## Tool Comparison Section

Compare Claude Code, Cursor, and GitHub Copilot on key dimensions.

### Comparison Dimensions (in priority order)

1. Security and compliance certifications
2. Integration with enterprise tools (SSO, audit logs)
3. Learning curve and adoption timeline
4. Technical capabilities

### Pricing Approach

Include public list prices. Note "contact for enterprise" where applicable.

### Currency Handling

Header: "Comparison current as of [Month 2026]"
Link to official documentation for latest capabilities.
```

Three questions. Three decisions documented. Three mid-writing pivots prevented.

## The Interview Checklist

Use this checklist to ensure your specification addresses common ambiguity areas before implementation:

```markdown
## Pre-Implementation Interview Checklist

### Data Decisions

[ ] Migration strategy defined (migrate existing / start fresh / hybrid)
[ ] Schema transition plan documented
[ ] Data validation rules specified

### Conflict Resolution

[ ] Multi-user edit strategy defined
[ ] Local/server sync behavior documented
[ ] Tie-breaking rules specified

### Pattern Selection

[ ] Architectural approach chosen from research options
[ ] Performance tradeoffs acknowledged
[ ] Scalability approach defined

### Failure Recovery

[ ] Timeout handling specified
[ ] Retry strategy documented
[ ] Crash recovery behavior defined
[ ] Error state persistence rules specified

### Boundary Conditions

[ ] Rate limits defined
[ ] Resource quotas documented
[ ] Scale limits acknowledged
[ ] Edge case behaviors specified
```

You don't need to fill every checkbox for every specification. A small utility script doesn't need crash recovery documentation. But running through the checklist surfaces which categories apply to your project.

## When to Stop Interviewing

The interview phase ends when:

1. **Questions become repetitive** — Claude asks variations of questions you've already answered
2. **New questions are trivial** — Questions about details that don't affect architecture
3. **Specification feels complete** — You can read through it and imagine implementation without guessing

If Claude's questions feel like implementation details rather than design decisions, you're ready for Phase 4.

**Warning sign:** If you're annoyed by the questions, that's often a signal that you haven't thought through those decisions. The annoyance comes from realizing you need to think harder, not from Claude being pedantic.

## Lab: Interview Your Specification

**Objective:** Practice the interview pattern on a real specification.

### Task

Take a specification you've written (or use the one from Lesson 5's lab). Run it through the interview pattern:

1. **Trigger the interview:**

   ```
   Here's my spec. Use the ask_user_question tool to surface any ambiguities
   before we implement.

   [paste your spec]
   ```

2. **Answer the questions thoughtfully.** Don't rush. Each question represents a potential mid-implementation pivot.

3. **Update your specification** with decisions from your answers.

4. **Check the checklist.** Which categories did Claude's questions address? Which categories weren't relevant to your spec?

The goal isn't to fill checkboxes—it's to surface decisions you hadn't consciously made.

## Try With AI

**Running Example Continued:** We have report-spec.md. Now we refine it through interview before writing.

**Prompt 1: Interview the Report Spec**

```
Read report-spec.md. Use ask_user_question to surface ambiguities.

Focus on decisions that would cause rewrites if wrong:
- Which CTOs exactly? (Startup vs enterprise? Tech company vs traditional?)
- What's their current AI adoption level?
- What decision are they trying to make after reading this?
```

**What you're learning:** The interview surfaces implicit assumptions. "CTOs evaluating AI tools" is vague—a startup CTO has different concerns than an enterprise CTO. Each answer sharpens the spec and prevents writing for the wrong audience.

**Prompt 2: Update Spec with Decisions**

```
Based on my answers:
- Target: CTOs at mid-size companies (100-1000 employees) considering first AI tool adoption
- Assumed: They've seen demos but haven't deployed; have security/compliance concerns
- Decision: Whether to pilot Claude Code, Cursor, or wait

Update report-spec.md with these decisions. Add them as explicit constraints.
```

**What you're learning:** Interview answers must persist. "First AI tool adoption" means we explain basics enterprise CTOs already know. "Security/compliance concerns" becomes a required section. The spec now encodes these CTO-specific needs.

**Prompt 3: Identify Remaining Gaps**

```
Review updated report-spec.md. What questions would a writer still have?

For each gap:
- Add to spec now (important for structure)
- Leave for writer judgment (minor detail)
- Flag for research (we don't have the data yet)
```

**What you're learning:** Perfect specs don't exist. The goal is specs good enough that writing doesn't require restructuring. Whether to use bullet points vs prose can stay flexible; whether to include a security section cannot.
