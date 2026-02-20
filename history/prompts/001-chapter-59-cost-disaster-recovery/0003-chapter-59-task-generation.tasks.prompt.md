---
id: 0003
title: chapter-59-task-generation
stage: tasks
date: 2025-12-30
surface: claude-code
model: claude-opus-4
feature: 001-chapter-59-cost-disaster-recovery
branch: 001-chapter-59-cost-disaster-recovery
user: mjs
command: /sp.tasks
labels: [chapter, part7, cost, disaster-recovery, tasks]
links:
  spec: specs/001-chapter-59-cost-disaster-recovery/spec.md
  ticket:
  adr:
  pr:
files:
  - specs/001-chapter-59-cost-disaster-recovery/tasks.md
tests:
  - N/A (task generation phase)
---

## Prompt

Generate task list for Chapter 59: Cost & Disaster Recovery

Based on:
- spec.md with 8 user stories (P1-P3)
- plan.md with 10 lessons (L00-L09)
- Skill-first pattern requiring L00 before content lessons
- Educational content tasks with subagent orchestration

## Response snapshot

Generated comprehensive tasks.md with 18 tasks organized by phase:

| Phase | Tasks | Purpose |
|-------|-------|---------|
| Setup | T001-T002 | Chapter directory structure |
| Foundational | T003 | L00 skill-first (US1) |
| Cost Management | T004-T007 | L01-L04 (US2, US3, US4) |
| Disaster Recovery | T008-T009 | L05-L06 (US5, US6) |
| Resilience | T010-T011 | L07-L08 (US7, US8) |
| Capstone | T012 | L09 integration (US8) |
| Validation | T013-T018 | Validators, assessment |

All lesson tasks include:
- SUBAGENT: content-implementer with absolute output path
- VALIDATION: educational-validator
- SKILLS: learning-objectives, exercise-designer, ai-collaborate-teaching (L2+)
- Content requirements from plan.md
- Maps to spec success criteria

## Outcome

- ✅ Impact: Complete task list ready for execution
- 🧪 Tests: N/A (task generation phase)
- 📁 Files: tasks.md
- 🔁 Next prompts: /sp.analyze → /sp.taskstoissues → implementation
- 🧠 Reflection: Tasks follow Direct-Write Protocol with subagent embedding

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All tasks have proper format
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
