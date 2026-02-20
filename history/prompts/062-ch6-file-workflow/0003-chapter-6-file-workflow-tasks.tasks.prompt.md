---
id: 0003
title: chapter-6-file-workflow-tasks
stage: tasks
date: 2025-01-27
surface: agent-factory-book
model: glm-4.7
feature: 062-ch6-file-workflow
branch: 062-ch6-file-workflow
user: Rehan-Ul-Haq
command: /sp.tasks
labels: [task-generation, content-work, educational-content]
links:
  spec: specs/062-ch6-file-workflow/spec.md
  plan: specs/062-ch6-file-workflow/plan.md
  tasks: specs/062-ch6-file-workflow/tasks.md
  ticket:
  adr:
  pr:
files:
  - specs/062-ch6-file-workflow/spec.md
  - specs/062-ch6-file-workflow/plan.md
  - specs/062-ch6-file-workflow/tasks.md
tests:
  - Each lesson task includes subagent orchestration
  - Each lesson task includes validation step
  - Each lesson task includes skill invocations
---

## Prompt

Create comprehensive tasks for chapter 06.

**User Intent**: Generate complete implementation checklist for Chapter 6 file organization workflow with proper subagent orchestration for educational content.

**Routing Decision**: Content work detected → followed /sp.tasks mandatory skill invocation requirements for educational content (learning-objectives, ai-collaborate-teaching, fact-check-lesson, content-evaluation-framework).

**Input Documents**:

- spec.md: User stories (US1-US6), success criteria (SC-001 through SC-018)
- plan.md: Lesson-by-lesson breakdown with learning objectives, bash commands, "Try With AI" prompts
- Chapter path: `apps/learn-app/docs/02-Applied-General-Agent-Workflows/06-file-processing/`
- Quality reference: `apps/learn-app/docs/02-Applied-General-Agent-Workflows/10-version-control/01-your-first-git-repository.md`

**Task Generation Approach**:

1. Organized by lesson (L01-L06) to enable independent implementation
2. Each lesson task includes SUBAGENT block with content-implementer
3. Each lesson task includes VALIDATION block with educational-validator
4. Each lesson task includes SKILLS block with required skill invocations
5. State persistence architecture documented (L01→L02→L03→L04→L05→L06)
6. All bash commands from plan.md included in subagent prompts
7. All "Try With AI" prompts from plan.md included
8. Cross-platform compatibility noted (Windows Git Bash, macOS, Linux)

**Content Work Requirements Met**:

- learning-objectives skill invoked for each lesson
- ai-collaborate-teaching skill invoked for L03, L04 (Layer 2 lessons)
- fact-check-lesson skill invoked for bash command accuracy
- content-evaluation-framework skill invoked for quality validation
- educational-validator subagent specified for each lesson
- Direct-write protocol: content-implementer writes directly, returns confirmation only
- Absolute paths used for all lesson outputs

**Output**: 41 tasks organized into 8 phases:

- Phase 1: Setup (5 tasks)
- Phase 2-7: Lessons L01-L06 (4 tasks each lesson)
- Phase 8: Polish & Validation (10 tasks)

## Response snapshot

**Output**: Successfully created tasks.md (438 lines) with comprehensive implementation checklist for Chapter 6.

**Key Deliverables**:

- 41 total tasks organized by lesson
- Each lesson includes: skill invocation, subagent creation, validation step
- State persistence architecture documented (each lesson builds on previous)
- All bash commands from plan included in subagent prompts
- All "Try With AI" prompts from plan included
- Cross-platform compatibility requirements specified
- Quality reference path included (Chapter 10)
- Success criteria from spec mapped to tasks

**Task Breakdown by Phase**:

- Phase 1 (Setup): 5 tasks - verify directory, read reference documents
- Phase 2 (L01): 4 tasks - learning-objectives, content-implementer, validation, fact-check
- Phase 3 (L02): 4 tasks - learning-objectives, content-implementer, validation, fact-check
- Phase 4 (L03): 5 tasks - learning-objectives, ai-collaborate-teaching, content-implementer, validation, evaluation
- Phase 5 (L04): 5 tasks - learning-objectives, ai-collaborate-teaching, content-implementer, validation, fact-check
- Phase 6 (L05): 4 tasks - learning-objectives, content-implementer, validation, evaluation
- Phase 7 (L06): 4 tasks - learning-objectives, content-implementer, validation, evaluation
- Phase 8 (Polish): 10 tasks - chapter evaluation, verification, final validation

**Subagent Orchestration**:

- Each lesson task includes SUBAGENT block with content-implementer
- Direct-write protocol: subagent writes file, returns confirmation only (~50 lines)
- Absolute output paths specified for all 6 lesson files
- Quality reference lesson path included
- Execute autonomously without confirmation specified

## Outcome

- ✅ Impact: Comprehensive 438-line tasks.md created with 41 implementation tasks organized by lesson. Each task includes proper subagent orchestration, skill invocations, and validation steps per content-work requirements.
- 🧪 Tests: Format validation - all tasks follow checkbox format with IDs and labels. Lesson dependencies - state persistence architecture verified (L01→L02→L03→L04→L05→L06). Subagent blocks - all lesson tasks include content-implementer with absolute paths.
- 📁 Files:
  - Created: specs/062-ch6-file-workflow/tasks.md (438 lines)
  - Referenced: spec.md, plan.md, chapter directory, quality reference lesson
- 🔁 Next prompts: /sp.implement to execute tasks.md using content-implementer subagents, or human review of tasks.md first
- 🧠 Reflection: Successfully applied content-work task generation requirements. Each lesson task includes mandatory skill invocations (learning-objectives, ai-collaborate-teaching for L03/L04, fact-check-lesson, content-evaluation-framework). State persistence architecture is critical - later lessons build on earlier outputs (L02 backup enables L05 recovery). Subagent orchestration uses direct-write protocol to minimize token bloat.

## Evaluation notes (flywheel)

- Failure modes observed: None. Task generation completed successfully with all required components.
- Graders run and results (PASS/FAIL): Format validation - PASS (all tasks use checkbox format with IDs). Content-work requirements - PASS (all lesson tasks include subagent, validation, skill blocks). State persistence - PASS (dependency architecture documented).
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to /sp.implement to begin executing tasks, starting with Setup phase (T001-T005) then Lesson 1 (T006-T009)
