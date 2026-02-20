---
id: 0003
title: chapter-8-tasks-generation
stage: tasks
date: 2025-11-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-chapter-8-redesign
branch: 08-redesign
user: HP
command: /sp.tasks
labels: ["chapter-8", "git-github", "tasks", "lesson-implementation", "aidd", "colearning-format"]
links:
  spec: specs/001-chapter-8-redesign/spec.md
  plan: specs/001-chapter-8-redesign/plan.md
  tasks: specs/001-chapter-8-redesign/tasks.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-chapter-8-redesign/tasks.md
tests:
  - Task format validation (all tasks follow checkbox + ID + [P?] + [Lesson] + description format)
  - Story-to-lesson mapping (all 6 user stories mapped to appropriate lessons)
  - Dependency validation (foundational tasks identified as blocking)
---

## Prompt

User requested task generation after spec and plan approval for Chapter 8 redesign.

**Context**:
- Specification: 6 user stories (US1-US6) with priorities P1, P2, P3
- Plan: 5 lessons with conversational CoLearning format, CEFR proficiency mapping, AIDD integration
- Requirement: Generate actionable task checklist for lesson-writer agent implementation

**Key Requirements**:
1. Organize tasks by lesson (which map to user stories)
2. Mark parallelizable tasks with [P]
3. Label tasks with [L1], [L2], [L3], [L4], [L5] for lesson assignment
4. Include exact file paths for all content creation
5. Validate dependencies (templates before content, foundation before lessons)
6. Map success criteria from spec to tasks

## Response snapshot

Generated comprehensive 60-task checklist organized into 8 phases:

**Phase Structure**:

**Phase 1: Setup (4 tasks)**
- Chapter README with CoLearning format overview
- 5-lesson architecture documentation
- AIDD integration overview
- "Try With AI" policy documentation

**Phase 2: Foundational Templates (4 tasks - BLOCKING)**
- Conversational template with 3 examples
- Validation commit template (3 progressive levels)
- Checkpoint pattern template (3 contexts)
- "Your Turn: Practice" format documentation
- **Critical**: All content creation depends on these templates

**Phase 3-7: Five Lessons (39 tasks)**

**Lesson 1 (6 tasks)**: Why Git Matters
- Maps to US1 (Learning through conversation)
- CEFR A1 Understand, 3 concepts, 30 minutes
- Tasks: Opening hook, 3 problems Git solves, 4-5 scenarios, analogies, reflection prompts, Try With AI

**Lesson 2 (9 tasks)**: Git Essentials
- Maps to US1 (conversation) + US2 (validation commits)
- CEFR A1 Apply, 4 concepts, 90 minutes
- Tasks: Installation conversations (3 platforms), configuration, core workflow, 3 validation commit examples, output interpretation, 5 practice prompts, troubleshooting, Try With AI
- **Key**: Introduces AIDD validation commit format

**Lesson 3 (8 tasks)**: Safe Experimentation
- Maps to US3 (spec branching) + US4 (checkpoints)
- CEFR A2 Apply, 4 concepts, 90 minutes
- Tasks: Checkpoint pattern, spec-driven branching, 3 branch experiments, undoing options, merge + conflicts, rollback scenario, 6 practice prompts, Try With AI
- **Key**: Teaches specification-first branching + checkpoint before AI

**Lesson 4 (8 tasks)**: Pull Requests & Collaboration
- Maps to US5 (PR as spec review)
- CEFR A2 Apply, 3 concepts, 75 minutes
- Tasks: Understanding PRs, creating PR with AIDD template, code review conversation, iteration/feedback, merging strategies, handling conflicts, 7 practice prompts, Try With AI
- **Key**: PR description shows spec fulfillment

**Lesson 5 (8 tasks)**: Natural Language Git
- Maps to US6 (troubleshooting) + synthesizes all prior
- CEFR A2 Apply, 2 concepts, 45 minutes
- Tasks: Mindset conversation, 10+ command translations, complex workflow prompts, troubleshooting library, best practices, when to use comparison, 6 practice prompts, Try With AI
- **Key**: AI as convenience layer while maintaining understanding

**Phase 8: Polish & Cross-Cutting (13 tasks)**
- Conversational format consistency review
- CEFR proficiency validation
- Cognitive load verification (all lessons within limits)
- Pattern recognition validation (checkpoint shown 3x)
- AIDD integration cross-check (4 patterns)
- Practice prompts validation (all copy-paste ready)
- Try With AI policy check
- Reading level validation (Grade 7)
- Cross-platform compatibility
- GitHub free-tier verification
- Chapter README completion summary
- End-of-chapter comprehensive project
- Chapter-level resources (quick reference, AIDD cheat sheet, troubleshooting guide)

**Task Format Compliance**:
- All 60 tasks follow: `- [ ] T### [P?] [L#] Description with file path`
- 28 tasks marked [P] for parallel execution (47%)
- All lesson tasks labeled [L1] through [L5]
- Setup and Polish tasks have no story label (cross-cutting)

**Dependencies Identified**:
```
Setup (T001-T004) → Foundation (T005-T008 - BLOCKING)
    ↓
Lesson 1 (T009-T014)
    ↓
Parallel: Lesson 2, Lesson 4, Lesson 5 (can write simultaneously)
Lesson 3 depends on Lesson 2 (builds on validation format)
    ↓
Polish (T048-T060) after all lessons exist
```

**Story-to-Lesson Mapping**:

| User Story | Lessons | Tasks | Test Criteria |
|------------|---------|-------|---------------|
| US1: Learning via Conversation | L1, L2 | T009-T023 | Complete Git workflow conversationally |
| US2: Validation Commits | L2, L3, L4 | T015-T039 | Create commit with AI attribution + tests |
| US3: Spec Branching | L3 | T024-T031 | Spec file → branch → implement → validate |
| US4: Checkpoint Pattern | L2, L3, L5 | T015-T031, T040-T047 | Checkpoint → AI → validate → keep/rollback |
| US5: PR as Spec Review | L4 | T032-T039 | PR with spec fulfillment evidence |
| US6: Troubleshooting | L5 | T040-T047 | Error → AI explains → guided resolution |

**Success Criteria Coverage**:
All 8 success criteria from spec mapped to specific tasks with validation methods.

**MVP Scope Defined**:
- Phases 1-2 + Lesson 1 + Lesson 2 = Minimum viable chapter
- Delivers: Motivation + core workflow + AIDD validation pattern
- Learners can make first validation commit

**Incremental Delivery**:
- Iteration 2: Add Lesson 3 (branching safety)
- Iteration 3: Add Lesson 4 (GitHub collaboration)
- Iteration 4: Add Lesson 5 (natural language layer)
- Final: Polish phase (consistency, resources)

**Estimated Effort**: 31-41 hours total for complete chapter implementation

## Outcome

- ✅ **Impact**: Comprehensive 60-task checklist created for Chapter 8 implementation. Tasks organized by lesson (mapping to user stories), with clear dependencies, parallel opportunities, and file paths. Ready for lesson-writer agent execution.

- 🧪 **Tests**:
  - Task format validation: ✅ All 60 tasks follow required format (checkbox + ID + [P?] + [Lesson] + description + file path)
  - Story-to-lesson mapping: ✅ All 6 user stories covered across appropriate lessons
  - Dependency validation: ✅ Foundational tasks (T005-T008) identified as blocking
  - Parallel opportunities: ✅ 28 tasks (47%) marked [P] for concurrent execution

- 📁 **Files**:
  - Created: specs/001-chapter-8-redesign/tasks.md (60 tasks across 8 phases)
  - Contains: Lesson-by-lesson breakdown, dependency graph, parallel execution strategy, MVP scope definition, success criteria mapping

- 🔁 **Next prompts**:
  - Begin lesson implementation with lesson-writer agent (start with foundational templates T005-T008)
  - Execute MVP scope first: Setup + Foundation + Lesson 1 + Lesson 2
  - Review completed lessons against plan.md and spec.md requirements
  - Proceed to incremental delivery: Lessons 3, 4, 5, then Polish

- 🧠 **Reflection**: Successfully mapped educational content creation to task-based workflow. Key insight: Educational chapters require different task structure than software features—organized by lesson (pedagogical units) rather than technical components. Template creation (Phase 2) is critical blocking dependency—all content depends on conversational format templates, validation commit templates, and practice prompt formats. MVP scope (Lessons 1-2) delivers core value: learners understand WHY Git matters and CAN execute basic workflow with AIDD validation pattern. Incremental delivery enables early validation of conversational format before completing all 5 lessons.

## Evaluation notes (flywheel)

- **Failure modes observed**: None. Tasks successfully translated from educational plan to actionable checklist. Potential risk: Template creation (T005-T008) quality determines all downstream content quality—these 4 tasks are single point of failure for pedagogical consistency.

- **Graders run and results (PASS/FAIL)**:
  - Task format compliance: ✅ PASS (all 60 tasks follow required format)
  - Story coverage: ✅ PASS (all 6 user stories mapped to lessons)
  - Dependency identification: ✅ PASS (foundational templates marked as blocking)
  - Success criteria mapping: ✅ PASS (all 8 SC from spec covered)
  - Parallel opportunities: ✅ PASS (28 tasks marked [P], realistic for content creation)

- **Prompt variant (if applicable)**: Educational content task generation (variant: software feature tasks would organize by API endpoints, data models, services rather than pedagogical lessons)

- **Next experiment (smallest change to try)**:
  - Execute foundational templates (T005-T008) first and validate quality before all other work
  - Implement MVP (Lessons 1-2) and test conversational format with real learner feedback
  - Prototype one complete conversational example from each lesson to validate 5-component pattern is not too verbose
