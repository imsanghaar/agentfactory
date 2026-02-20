---
id: "0004"
title: "docker-chapter-implementation-tasks"
stage: tasks
date: 2025-12-22
surface: claude-code
model: claude-opus-4-5-20251101
feature: 001-docker-chapter
branch: 001-docker-chapter
user: mjs
command: /sp.tasks
labels: [task-generation, content-implementation, 9-lessons]
links:
  spec: specs/001-docker-chapter/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-docker-chapter/tasks.md
tests:
  - null
---

## Prompt

/sp.tasks Now let's plan the tasks to implement

Context: Spec (654 lines, 9 lessons) and Plan (569 lines) complete. Ready to generate implementation tasks for content writers.

## Response snapshot

Generated comprehensive tasks.md (384 lines, 115 tasks) for Chapter 49 Docker content implementation.

**Task Structure (12 Phases)**:

1. **Phase 1: Setup** (4 tasks) - Chapter infrastructure
2. **Phase 2: Foundational** (5 tasks) - Shared assets (BLOCKING)
3. **Phases 3-11** (99 tasks) - One phase per lesson (L1-L9)
4. **Phase 12: Polish** (7 tasks) - Validation and cross-cutting

**Per-Lesson Task Breakdown**:

| Lesson | Tasks | Key Deliverables |
|--------|-------|------------------|
| L1: Installation | 9 | Platform guides, verification exercises |
| L2: Fundamentals | 9 | Concept diagrams, hands-on discovery |
| L3: First Dockerfile | 10 | Step-by-step creation, DHI introduction |
| L4: Debugging | 11 | Error analysis, broken container exercise |
| L5: Optimization | 11 | Multi-stage refactoring, size measurement |
| L6: Compose | 12 | Multi-service setup, health checks |
| L7: Security | 12 | Scout scanning, CVE remediation |
| L8: AI-Assisted | 11 | Gordon workflows, Three Roles INVISIBLE |
| L9: Capstone | 14 | Spec-first project, registry push |

**Key Design Decisions**:

1. **Lesson-based phases** (not user-story based): Content chapters organize better by lesson progression than by user stories
2. **Shared assets phase**: Sample FastAPI agent code created ONCE, reused L3-L9
3. **Constitution validation tasks**: Explicit grep validation for Three Roles invisibility
4. **Success criteria mapping**: Table mapping SC-001 through SC-010 to specific tasks
5. **Parallel opportunities**: [P] markers for tasks that can run concurrently

**Implementation Timeline**:
- Single author: 26-34 hours
- Multi-author (3 writers): 12-15 hours per author

## Outcome

- ✅ Impact: Complete task list for 9-lesson Docker chapter implementation
- 🧪 Tests: N/A (content authoring, not code)
- 📁 Files: tasks.md (384 lines, 115 tasks)
- 🔁 Next prompts: Begin content implementation with content-implementer agent, or manual lesson writing
- 🧠 Reflection: Lesson-based task organization more appropriate for content chapters than user-story grouping used in engineering features

## Evaluation notes (flywheel)

- Failure modes observed: None - template adapted well to content authoring context
- Graders run and results (PASS/FAIL): Task count verified (115), lesson tags verified (99), parallel markers verified (17)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Track actual implementation time against 26-34 hour estimate to calibrate future content chapter estimates
