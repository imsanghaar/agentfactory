---
id: "0004"
title: "ch60-cloud-deployment-tasks"
stage: tasks
date: 2025-12-30
surface: cli
model: claude-opus-4-5
feature: 001-ch60-cloud-deployment
branch: 001-ch60-cloud-deployment
user: mjs
command: /sp.tasks
labels: [chapter-60, cloud-deployment, task-generation]
links:
  spec: specs/001-ch60-cloud-deployment/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-ch60-cloud-deployment/tasks.md
tests:
  - null
---

## Prompt

Generate implementation tasks for Chapter 60: Real Cloud Deployment based on specs/001-ch60-cloud-deployment/plan.md

## Response snapshot

Generated comprehensive tasks.md (413 lines) with 22 tasks across 9 phases:

**Phase Organization**:
| Phase | Purpose | Tasks |
|-------|---------|-------|
| Phase 1 | Setup | T001-T003 |
| Phase 2 | US1 - Skill-First L00 | T004 |
| Phase 3 | US2 - DOKS path L01-L06 | T005-T010 |
| Phase 4 | US3 - Hetzner L07 | T011 |
| Phase 5 | US4 - Multi-cloud L09 | T012 |
| Phase 6 | US5 - Production checklist L08 | T013 |
| Phase 7 | US6 - Cost management | (integrated) |
| Phase 8 | Capstone L10 | T014 |
| Phase 9 | Polish & validation | T015-T022 |

**Key Features**:
- Each lesson task includes SUBAGENT, SKILLS, VALIDATION blocks
- Absolute output paths for all lessons
- Quality reference lesson path included
- User story labels ([US1]-[US6]) for traceability
- Dependency graph showing execution order
- MVP-first implementation strategy (Skill + DOKS path first)

**Task Breakdown**:
- 11 lessons (L00-L10)
- 22 total tasks
- Teaching stage progression: L3 (L00) -> L1 (L01-L04, L07) -> L2 (L05-L06, L08-L09) -> L4 (L10)

## Outcome

- ✅ Impact: Complete task list ready for implementation
- 🧪 Tests: Format validation passed (checkbox + ID + story label + path)
- 📁 Files: specs/001-ch60-cloud-deployment/tasks.md (413 lines)
- 🔁 Next prompts: Implement Phase 1 (Setup) then Phase 2 (L00)
- 🧠 Reflection: Tasks properly embed subagent requirements, skill invocations, and validation gates per content workflow protocol

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Format validation PASS (all tasks have checkbox, ID, story label, file path)
- Prompt variant (if applicable): Standard task generation with content workflow embedding
- Next experiment (smallest change to try): N/A - proceed to implementation
