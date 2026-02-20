---
id: 0003
title: lesson2-install-update-tasks
stage: tasks
date: 2025-12-06
surface: terminal
model: claude-sonnet-4-5
feature: 034-lesson2-install-update
branch: 034-lesson2-install-update
user: orchestrator
command: /sp.tasks
labels: [task-generation, user-story-organization, lesson-content, platform-specific]
links:
  spec: specs/034-lesson2-install-update/spec.md
  plan: specs/034-lesson2-install-update/plan.md
  tasks: specs/034-lesson2-install-update/tasks.md
files:
  - specs/034-lesson2-install-update/tasks.md
---

## Prompt

Generate tasks.md for Chapter 5 Lesson 2 installation update.

Input: 6 user stories from spec.md, 5 implementation phases from plan.md

Organization: By user story for independent validation
- US1: Windows installation (P1)
- US2: macOS installation (P1)
- US3: Linux/WSL installation (P1)
- US4: npm alternative (P2)
- US5: Authentication (P1)
- US6: Summary update (P2)

## Response

tasks.md created: 74 tasks across 11 phases

Task Breakdown:
- Phase 1: Setup & Research (9 tasks) - Extract commands from official docs
- Phase 2: Foundational (5 tasks) - Preserve frontmatter, prerequisites
- Phase 3: US1 Windows (8 tasks) - PowerShell/Git Bash/CMD/npm
- Phase 4: US2 macOS (7 tasks) - Homebrew/curl/npm
- Phase 5: US3 Linux/WSL (6 tasks) - curl/npm
- Phase 6: US4 npm (4 tasks) - Cross-platform alternative
- Phase 7: US5 Auth (7 tasks) - 3 authentication paths
- Phase 8: US6 Summary (7 tasks) - Rewrite matching main lesson
- Phase 9: Cross-Cutting (6 tasks) - Try With AI, auto-update
- Phase 10: Validation (10 tasks) - Factual accuracy, constitutional
- Phase 11: Polish (5 tasks) - Final checks

Parallel Execution:
- Platform sections (Windows/macOS/Linux) independent
- 45 tasks (61%) marked [P] for parallelization
- Auth section independent of platform sections

MVP Scope: US1+US2+US3+US5 (6 hours)
Full Delivery: All 6 user stories (8-12 hours per plan)

## Outcome

- ✅ Tasks generated, ready for implementation
- 📁 tasks.md (74 tasks, 11 phases, dependency graph)
- 🔁 Next: /sp.implement 034-lesson2-install-update
