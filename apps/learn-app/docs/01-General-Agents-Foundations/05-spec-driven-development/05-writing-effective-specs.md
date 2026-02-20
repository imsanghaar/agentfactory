---
sidebar_position: 5
title: "Phase 2: Writing Effective Specifications"
description: "Create specifications that AI agents can implement reliably"
keywords:
  [
    "specification writing",
    "spec template",
    "constraints",
    "success criteria",
    "implementation checklist",
    "SDD",
    "spec-driven development",
  ]
chapter: 5
lesson: 5
duration_minutes: 30

# HIDDEN SKILLS METADATA
skills:
  - name: "Specification Structure Design"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can create a four-part specification document following the standard template"

  - name: "Constraint Definition"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify what NOT to build and articulate boundaries clearly"

  - name: "Success Criteria Specification"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can write measurable, testable success criteria"

learning_objectives:
  - objective: "Apply the four-part specification template to structure implementation plans"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student produces spec document with all four parts correctly populated"

  - objective: "Define explicit constraints that prevent scope creep and wrong choices"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student identifies missing constraints in sample specifications"

  - objective: "Write measurable success criteria that enable verification"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student converts vague requirements into quantified metrics"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (four-part template, reference architecture, current architecture, implementation plan, checklist, constraints, success criteria) within B1 range"

differentiation:
  extension_for_advanced: "Design specifications for multi-agent orchestration scenarios"
  remedial_for_struggling: "Focus on constraints and success criteria sections only, then expand to full template"

teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "Deep-Dive into SDD Phases"
  key_points:
    - "The four-part template (Reference Architecture, Current Architecture, Implementation Plan, Checklist) is the spec structure students will use throughout the book"
    - "Constraints are more important than requirements — they prevent Claude from making reasonable but wrong choices specific to your project"
    - "Success criteria must be testable: ask 'How would I know if this failed?' to convert vague goals into measurable outcomes"
    - "Checklist items must be atomic enough to delegate to a subagent — the 'junior developer test' (one sentence explanation) is the litmus test"
  misconceptions:
    - "Students confuse specs with to-do lists — the Reference Architecture and Current Architecture sections capture WHY decisions were made, not just WHAT to build"
    - "Students write HOW specs instead of WHAT specs — emphasize the 'describe behavior, not implementation' distinction with the HashMap vs user-lookup example"
    - "Students think constraints are optional — without constraints, Claude optimizes for the general case which is almost never your specific case"
  discussion_prompts:
    - "Look at the 'vague spec vs explicit constraints' table — for your current project, what wrong choice would Claude reasonably make without constraints?"
    - "Why might prescribing implementation details in a spec actually produce worse code than describing behavior?"
    - "What's a success criterion you've used before that was actually unmeasurable — and how would you rewrite it?"
  teaching_tips:
    - "The Offline-First Sync example is the centerpiece — walk through each section showing how it answers Claude's potential questions"
    - "Use the vague vs explicit comparison tables as pair exercises: students rewrite vague versions into explicit ones"
    - "The Addy Osmani quote (PRD thinking + SRS precision) is a useful anchor for students with software engineering background"
    - "Spend extra time on the anti-patterns section — students learn more from what NOT to do than from templates"
  assessment_quick_check:
    - "Name the four parts of the specification template and explain what each prevents"
    - "Convert this vague success criterion into a measurable one: 'The system should be fast and reliable'"
    - "Write two explicit constraints for a hypothetical 'add search to our app' spec"
---

# Phase 2: Writing Effective Specifications

A spec is a contract between you and Claude. Vague contracts produce vague results.

In the previous lesson, you learned how to spawn parallel subagents to research a problem from multiple angles. Now that you have research findings, you need to capture them in a document that Claude can execute flawlessly. This is where most developers fail—not because they lack research, but because they write specs that leave too much to interpretation.

Consider this: when you hand a specification to a human developer, they ask clarifying questions. When you hand the same specification to Claude, it makes assumptions. Every assumption is a potential bug. Every ambiguity becomes a decision made without your input. The goal of specification writing is to answer questions before they're asked.

Addy Osmani (Chrome Engineering Lead) describes effective specifications as combining **PRD thinking** (why we're building this) with **SRS precision** (how it should behave). Your spec should give Claude both the motivation and the mechanics.

## The Four-Part Specification Template

Every effective specification follows a consistent structure. Here's the template that separates sellable Digital FTEs from weekend experiments:

```markdown
# [Feature Name] Specification

## Part 1: Reference Architecture Analysis

- Patterns discovered in research
- Key design decisions and rationale
- What similar implementations do well
- What they do poorly (mistakes to avoid)

## Part 2: Current Architecture Analysis

- Existing implementation details relevant to this feature
- Pain points and limitations in current system
- Constraints imposed by existing code
- Files and modules that will be affected

## Part 3: Implementation Plan

- Phased approach (what order to build)
- Risk mitigation strategies
- Dependencies between phases
- Rollback strategy if things go wrong

## Part 4: Implementation Checklist

- [ ] Task 1: Description of first atomic unit
- [ ] Task 2: Description of second atomic unit
- [ ] Task N: Final cleanup and validation

## Constraints

- What NOT to build (explicit exclusions)
- Technology boundaries (must use X, cannot use Y)
- Performance requirements (latency, throughput)
- Security requirements (authentication, authorization)
- Compatibility requirements (browsers, platforms)

## Success Criteria

- Measurable outcome 1 (e.g., "< 100ms p95 latency")
- Measurable outcome 2 (e.g., "All existing tests pass")
- Measurable outcome 3 (e.g., "Works offline after initial load")
- Acceptance tests that prove completion
```

**Why this structure works**: Each part serves a distinct purpose. Reference Architecture tells Claude what good looks like. Current Architecture shows Claude where you are. Implementation Plan provides the path. Checklist enables task extraction for Phase 4. Constraints prevent wrong turns. Success Criteria define done.

## What Makes Specs Effective

Three qualities separate specifications that work on first attempt from those requiring five iterations:

### 1. Explicit Constraints (What NOT to Do)

Constraints are often more important than requirements. They prevent Claude from making reasonable but wrong choices.

| Vague Spec              | Explicit Constraints                                                                                               |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------ |
| "Build a caching layer" | "Do NOT modify database schema. Do NOT add Redis (use in-memory only). Do NOT cache user-specific data."           |
| "Add authentication"    | "Use existing OAuth provider only. Do NOT implement custom password hashing. Do NOT store tokens in localStorage." |
| "Improve performance"   | "Do NOT pre-fetch more than 3 items. Do NOT change API contracts. Do NOT sacrifice correctness for speed."         |

**Why constraints matter**: Without them, Claude optimizes for the general case. Your system is not the general case. Constraints encode your specific context.

### 2. Measurable Success Criteria (Not "Fast", Not "Good")

Every success criterion must be testable. If you can't write a test for it, it's not a criterion—it's a wish.

| Vague Criteria              | Measurable Criteria                                                               |
| --------------------------- | --------------------------------------------------------------------------------- |
| "Should be fast"            | "P95 latency < 100ms for queries under 1000 results"                              |
| "Works on mobile"           | "Renders correctly on viewport widths 320px-768px"                                |
| "Handles errors gracefully" | "All API errors return structured JSON with error code and user-friendly message" |
| "Scales well"               | "Supports 1000 concurrent connections with < 5% degradation"                      |

**How to convert vague to measurable**: Ask "How would I know if this failed?" The answer is your criterion.

### 3. Checklist Format for Task Extraction

Phase 4 of SDD uses the Task system to delegate work to subagents. Each checklist item becomes a potential task. Write them as atomic units of work.

**Bad checklist items** (too vague, can't be delegated):

- [ ] Set up the system
- [ ] Make it work
- [ ] Test everything

**Good checklist items** (atomic, delegatable):

- [ ] Create `/lib/cache.ts` with LRU implementation (max 1000 entries)
- [ ] Add cache middleware to `/api/products` endpoint
- [ ] Write tests for cache hit/miss/eviction scenarios
- [ ] Update `/docs/caching.md` with new configuration options

**Rule of thumb**: If you can't explain the task to a junior developer in one sentence, it's not atomic enough.

## Anti-Patterns to Avoid

### Anti-Pattern 1: HOW Instead of WHAT

Specifications describe **behavior**, not **implementation**. Let Claude choose the how.

```markdown
<!-- WRONG: Prescribing implementation -->

Use a HashMap with String keys and User values.
Iterate through the map using a for-each loop.
Check if the user exists before adding.

<!-- CORRECT: Describing behavior -->

Maintain a user lookup that:

- Returns user by ID in O(1) time
- Prevents duplicate IDs
- Supports 10,000+ users without degradation
```

**Why this matters**: Claude often knows better implementation patterns than you. By specifying behavior, you get the benefit of its knowledge. By specifying implementation, you lock in your assumptions.

### Anti-Pattern 2: Missing Constraints

No constraints means Claude decides everything. This is Vibe Coding with extra steps.

```markdown
<!-- WRONG: No boundaries -->

## Constraints

(none specified)

<!-- CORRECT: Clear boundaries -->

## Constraints

- Do NOT modify the User model schema
- Do NOT add new npm dependencies without approval
- Do NOT use any beta or experimental APIs
- Must work with existing PostgreSQL 14 installation
- Must maintain backward compatibility with v2 API clients
```

### Anti-Pattern 3: Vague Success Criteria

"Works correctly" is not a success criterion. Neither is "user-friendly" or "efficient."

```markdown
<!-- WRONG: Unmeasurable -->

## Success Criteria

- System works correctly
- Good user experience
- Performs efficiently

<!-- CORRECT: Measurable -->

## Success Criteria

- All 47 existing API tests pass (regression)
- New endpoints return within 200ms for 95th percentile
- Error responses include machine-readable error codes
- Swagger documentation auto-generates from code annotations
```

## A Complete Specification Example

Here's a real specification that follows all principles:

```markdown
# Offline-First Sync Specification

## Part 1: Reference Architecture Analysis

Research of similar implementations (linear.app, notion.so) revealed:

- CRDT-based conflict resolution prevents data loss during offline edits
- Local-first storage (IndexedDB) enables immediate UI response
- Background sync queues batch operations for efficiency
- Retry logic with exponential backoff handles network flakiness

Key insight: Notion uses operation log rather than state sync—each edit is an operation that can be replayed. This enables undo/redo for free.

## Part 2: Current Architecture Analysis

Current system uses synchronous API calls:

- Each save triggers POST request (blocking)
- No offline support (fails silently)
- Conflict resolution: last-write-wins (data loss risk)

Files affected:

- `/src/stores/document.ts` - state management
- `/src/api/documents.ts` - API layer
- `/src/components/Editor.tsx` - UI integration

Constraint: Must maintain existing API contract for mobile app compatibility.

## Part 3: Implementation Plan

Phase 1: Local persistence (IndexedDB integration)
Phase 2: Operation queue (batch and retry logic)
Phase 3: Conflict detection (CRDT comparison)
Phase 4: UI indicators (sync status display)

Rollback: Each phase is independently revertible via feature flag.

## Part 4: Implementation Checklist

- [ ] Create IndexedDB wrapper in `/src/lib/local-db.ts`
- [ ] Add operation queue with retry in `/src/lib/sync-queue.ts`
- [ ] Implement CRDT merge in `/src/lib/conflict-resolver.ts`
- [ ] Add sync status component to Editor
- [ ] Write integration tests for offline scenarios
- [ ] Update documentation with offline behavior

## Constraints

- Do NOT change API response formats (mobile app compatibility)
- Do NOT add dependencies larger than 50KB gzipped
- Do NOT modify existing database schema
- Use existing auth tokens (no separate offline auth)
- Support last 2 versions of Chrome, Firefox, Safari

## Success Criteria

- Documents save locally within 50ms
- Sync completes within 5 seconds of connectivity restoration
- Zero data loss in conflict scenarios (verified by test suite)
- Offline indicator visible within 1 second of connection loss
- All existing e2e tests pass without modification
```

**Notice**: This spec answers every question Claude might ask. Reference Architecture shows what good looks like. Current Architecture shows where we're starting. Implementation Plan provides sequence. Checklist enables task delegation. Constraints prevent wrong turns. Success Criteria define done.

## Try With AI

**Running Example Continued:** We have research.md from parallel investigation. Now we write report-spec.md.

**Prompt 1: Draft Specification from Research**

```
Based on research.md, write report-spec.md for "Personal AI Employees in 2026."

Use the four-part template:
- Part 1: Reference Analysis (what makes good CTO-facing reports?)
- Part 2: Current State (what does research.md tell us?)
- Part 3: Implementation Plan (sections and order)
- Part 4: Checklist (atomic writing tasks)

Plus Constraints and Success Criteria.
```

**What you're learning:** The spec transforms research findings into a writing plan. Research.md's "tool capabilities" becomes the comparison section. "ROI data" becomes the business case section. "Gaps CTOs would ask about" become sections we must address or explicitly scope out.

**Prompt 2: Strengthen Constraints**

```
Review report-spec.md. The constraints section is weak.

Add explicit constraints for:
- What this report is NOT (not a tutorial, not a product pitch)
- Length limits (CTOs won't read 50 pages)
- Assumed knowledge (what do readers already know about AI?)
- What to skip (implementation details, they have engineers for that)

For each constraint, explain why it prevents a specific failure mode.
```

**What you're learning:** Constraints prevent scope creep. Without "NOT a tutorial," you'd explain how to use each tool. Without "CTOs have engineers," you'd dive into technical setup. Constraints encode audience judgment.

**Prompt 3: Make Criteria Testable**

```
The success criteria in report-spec.md say "actionable" and "balanced."
These can't be tested.

Rewrite each criterion so I could verify it:
- "Actionable" → specific recommendation requirement
- "Balanced" → specific comparison structure
- Add: what would a CTO be able to DO after reading?
```

**What you're learning:** Vague criteria let anything pass. "Each tool section includes pricing and limitations" is testable. "CTO can justify tool selection to their board" defines actual success.
