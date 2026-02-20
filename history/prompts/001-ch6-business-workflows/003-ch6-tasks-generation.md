---
id: PHR-003-ch6-business-workflows-tasks
title: Chapter 6 Tasks Generation
stage: tasks
date: 2025-12-31
surface: claude-code
model: claude-opus-4-5-20250101
feature: 001-ch6-business-workflows
branch: 001-ch6-business-workflows
user: user
command: /sp.tasks
labels: [chapter, tasks, business-workflows, social-media, implementation]
links:
  spec: specs/001-ch6-business-workflows/spec.md
  plan: specs/001-ch6-business-workflows/plan.md
  ticket: "#554"
  adr: N/A
  pr: N/A
files:
  - specs/001-ch6-business-workflows/tasks.md
tests:
  - N/A
---

## Prompt

/sp.tasks (triggered from plan.md for Chapter 6: Business Workflows & Social Media)

## Response snapshot

Generated comprehensive tasks.md with 17 tasks organized by user story:

1. **Phase 1: Setup** (3 tasks)
   - T001: Verify directory
   - T002: Verify Chapter 5 prerequisite
   - T003: Create README.md with content-implementer subagent

2. **Phase 2: User Story 1 - Email** (2 tasks)
   - T004: Create Lesson 1 with content-implementer + educational-validator
   - T005: Generate summary file

3. **Phase 3: User Story 2 - WhatsApp** (2 tasks)
   - T006: Create Lesson 2 with content-implementer + educational-validator
   - T007: Generate summary file

4. **Phase 4: User Story 3 - LinkedIn** (2 tasks)
   - T008: Create Lesson 3 with content-implementer + educational-validator
   - T009: Generate summary file

5. **Phase 5: User Story 4 - Twitter/X** (2 tasks)
   - T010: Create Lesson 4 with content-implementer + educational-validator
   - T011: Generate summary file

6. **Phase 6: Chapter Quiz** (1 task)
   - T012: Create quiz with assessment-architect subagent

7. **Phase 7: Polish** (5 tasks)
   - T013-T017: Validation, frontmatter, build, Three Roles verification

**Key Implementation Decisions**:
- All lesson tasks embed subagent orchestration (content-implementer + educational-validator)
- Skills invoked: learning-objectives, exercise-designer, ai-collaborate-teaching, content-evaluation-framework
- MVP scope: T001-T005 (Setup + Email lesson)
- Parallel opportunities: T013-T016 (Polish phase), optionally US2-US4 after US1

## Outcome

- Impact: Task list complete, ready for implementation
- Tests: NOT requested (content chapter)
- Files: 1 file created (tasks.md - 17 tasks)
- Next prompts: /sp.implement to begin task execution
- Reflection: Tasks include mandatory subagent orchestration per CLAUDE.md requirements

## Evaluation notes (flywheel)

- Failure modes observed: None - followed content work task template with embedded subagent requirements
- Graders run and results (PASS/FAIL): Format validation PASS (all tasks have checkbox, ID, proper format)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A - proceed to implementation
