---
id: "0001"
title: consolidated-exercises-spec
stage: spec
date: 2026-02-08
surface: claude-code
model: claude-opus-4-6
feature: 041-consolidated-exercises
branch: 041-consolidated-exercises
user: mjunaidca
command: /sp.specify
labels: [exercises, chapter-2, consolidation, github-actions]
links:
  spec: specs/041-consolidated-exercises/spec.md
  ticket: ""
  adr: ""
  pr: ""
files:
  - specs/041-consolidated-exercises/spec.md
  - specs/041-consolidated-exercises/checklists/requirements.md
tests:
  - ""
---

## Prompt

Feature: Consolidated Exercise Lessons with Auto-ZIP Downloads. Consolidate exercises scattered across 4 lessons (L04, L07, L08, L09) in Chapter 2 (general-agents) into 2 dedicated exercise lessons with one-click ZIP downloads. Create 2 new GitHub repos (basics + skills) with GitHub Actions auto-release, 2 new lessons with full exercise walkthroughs, remove exercise sections from existing lessons, and renumber L09-L26 to L10-L28.

## Response snapshot

Created comprehensive spec with 34 functional requirements, 14 success criteria, 5 user stories with acceptance scenarios, and 6 edge cases. Spec covers: 2 new repos, GitHub Actions auto-ZIP release, 2 new exercise lessons (basics after L08, skills after L10), removal of exercise sections from 4 existing lessons, and renumbering of 17 lessons. One NEEDS CLARIFICATION marker remains (FR-034: old repo retention policy). Validation checklist created with all items passing except the clarification marker.

## Outcome

- Impact: Spec ready for clarification and planning
- Tests: N/A (spec phase)
- Files: spec.md (442 lines), checklists/requirements.md
- Next prompts: Resolve FR-034 clarification, then /sp.plan
- Reflection: Feature well-scoped from voice notes + artifact. Spec-first approach avoided the scattered implementation that caused the original problem.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Manual checklist — 15/16 PASS (1 pending clarification)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
