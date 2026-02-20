---
id: 0003
title: metadata-driven-slides-tasks
stage: tasks
date: 2025-11-23T20:00:00Z
surface: claude-code
model: claude-sonnet-4-5-20250929
feature: 035-metadata-driven-slides
branch: 035-metadata-driven-slides
user: mjs
command: /sp.tasks
labels: [tasks, implementation, dependency-ordering, user-stories]
links:
  spec: specs/035-metadata-driven-slides/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - path: specs/035-metadata-driven-slides/tasks.md
    status: created
tests:
  - type: task-organization
    result: PASS
    score: 4 user stories mapped to phases
---

## Prompt

**User Request**: "approved utnoumly continue and present final work implemented after all phases"

**Context from Phase 2**: Implementation plan completed with architecture diagrams, research decisions, and data model. All technical unknowns resolved.

**Command Execution**: `/sp.tasks 035-metadata-driven-slides`

**Task**: Generate implementation tasks (tasks.md) with:
1. Extract user stories from spec.md (4 stories: US1-P1, US2-P1, US3-P2, US4-P3)
2. Organize tasks by user story for independent implementation/testing
3. Define phase structure (Setup → Foundational → User Stories → Polish)
4. Map components to stories (transformer, utils, path detection, error handling)
5. Identify parallel opportunities ([P] markers)
6. Define dependency graph (phase and story dependencies)
7. Provide implementation strategies (MVP first, incremental delivery)
8. Include success criteria validation checklist

## Response snapshot

**Task Organization** (44 tasks across 7 phases):

**Phase 1: Setup** (5 tasks)
- Create plugin directory structure
- Install dependencies (unist-util-visit, mdast-util-to-string)
- Create skeleton files (index.ts, transformer.ts, utils.ts)
- Parallel opportunities: T003-T005 (file creation)

**Phase 2: Foundational** (6 tasks) **CRITICAL BLOCKER**
- Implement utility functions (detectPathType, normalizePath, findHeading)
- Implement node generators (import, JSX)
- Register plugin in docusaurus.config.ts
- Parallel opportunities: T007-T008, T010 (utility functions)

**Phase 3: User Story 1 - Local Path Slides** (8 tasks) **MVP CORE**
- Implement main transformer (frontmatter parsing, AST injection)
- Test with Chapter 2 (local path)
- Remove manual JSX to validate metadata approach
- Independent test: Local path slides work end-to-end

**Phase 4: User Story 2 - Cloud URL Support** (5 tasks) **MVP CORE**
- Extend transformer with path type detection
- Test with Chapter 3 (cloud URL)
- Validate mixed scenario (local + URL simultaneously)
- Independent test: Cloud URLs work identically to local paths

**Phase 5: User Story 3 - Centralized Maintenance** (5 tasks)
- Document modification points
- Test centralized changes propagate globally
- Validate across all chapters with slides
- Independent test: Single change affects all chapters

**Phase 6: User Story 4 - Graceful Degradation** (7 tasks)
- Add error handling with try-catch
- Implement warning logging (missing heading, malformed frontmatter)
- Test build succeeds despite invalid references
- Independent test: Warnings logged, build doesn't fail

**Phase 7: Polish & Cross-Cutting** (8 tasks)
- Update documentation with real examples
- Add TypeScript types
- Backward compatibility validation
- Full build performance test (<5% increase)

**Dependencies Mapped**:
- Setup → Foundational (BLOCKS all stories)
- Foundational → All User Stories
- US1 → US2 (extends path handling)
- US1 → US3 (tests centralization)
- US1 → US4 (adds error handling)
- All Stories → Polish

**Parallel Opportunities Identified**:
- Setup: 3 file creation tasks
- Foundational: 3 utility function tasks
- User Story 1: 2 Chapter 2 update tasks
- Polish: 3 documentation tasks

**Implementation Strategies Provided**:
1. **MVP First**: Setup + Foundational + US1 + US2 (~2 hours)
2. **Incremental Delivery**: Add stories sequentially, validate independently
3. **Sequential Implementation**: Complete order with estimated times

## Outcome

- ✅ Impact: Phase 3 completed with dependency-ordered task breakdown (44 tasks)
- 🧪 Tests: Task organization validated (4 user stories → 4 phases + setup/foundational/polish)
- 📁 Files: tasks.md (371 lines) with complete implementation guide
- 🔁 Next prompts: Begin Phase 4 implementation starting with T001 (Setup)
- 🧠 Reflection: User story organization enables independent testing at each checkpoint. MVP scope (US1+US2) delivers core value in ~2 hours. Parallel opportunities identified but sequential execution recommended for single developer. All 44 tasks have exact file paths and clear completion criteria.

## Evaluation notes (flywheel)

- Failure modes observed: None - all user stories mapped to phases successfully
- Graders run and results (PASS/FAIL): Task organization PASS (4 stories → 7 phases)
- Prompt variant (if applicable): /sp.tasks with user story priority mapping
- Next experiment (smallest change to try): Begin implementation with T001, validate parallel execution opportunities during actual coding
