---
id: "0002"
title: "Linux Mastery v2 Chapter Plan"
stage: plan
date: 2026-02-08
surface: claude-code
model: claude-opus-4-6
feature: 001-linux-mastery-v2
branch: 001-linux-mastery-v2
user: user
command: /sp.plan
labels: [linux, chapter-plan, v2, content-work]
links:
  spec: specs/001-linux-mastery-v2/spec.md
  ticket: ""
  adr: ""
  pr: ""
files:
  - specs/001-linux-mastery-v2/plan.md
tests:
  - chapter-planner subagent completed (1591 lines)
  - validation checklist all items PASS
---

## Prompt

User invoked `/sp.plan` for feature `001-linux-mastery-v2`. Classified as CONTENT work (lessons, chapter, pedagogical layers, proficiency levels). Routed to `chapter-planner` subagent per mandatory orchestration rules. Spec at `specs/001-linux-mastery-v2/spec.md` provides 27 FRs, 12 SCs, 12 user stories, 21-issue resolution matrix, and lesson structure table (13 lessons + quiz).

## Response snapshot

Chapter-planner produced 1,591-line plan covering 12 sections: (I) Chapter Analysis, (II) Success Evals, (III) Lesson-by-Lesson Architecture (all 14 lessons + quiz with LOs, CEFR, Bloom's, modality, exercises), (IV) Dependency Graph with critical path, (V) Sample Agent File (exact 45-line agent_main.py), (VI) Content Migration Map (per-section preserve/remove/add/move for all 9 v1 lessons), (VII) Three Roles Invisibility Strategy (BEFORE/AFTER transformation pattern), (VIII) Cross-Cutting Validation (bash scripts for FR-004/005/006/016/018), (IX) Quiz Regeneration Plan (50 questions, 3-5 per lesson), (X) Implementation Sequence (4 phases, ~42 hours), (XI) Skills Proficiency Progression Map (16 tracks across 14 lessons), (XII) Validation Checklist (all items passing).

## Outcome

- Impact: Complete implementation plan ready for task generation and content-implementer execution
- Tests: Validation checklist in Section XII — all items passing
- Files: 1 file written (plan.md, 1591 lines)
- Next prompts: `/sp.tasks` or native TaskCreate to generate task breakdown, then content-implementer subagents for each lesson
- Reflection: Chapter-planner correctly identified FR-005 vs Constitution L1 tension (Try With AI in manual lessons) and proposed resolution (conceptual prompts, not collaborative implementation). Good constitutional alignment.

## Evaluation notes (flywheel)

- Failure modes observed: None significant. Plan is comprehensive.
- Graders run and results (PASS/FAIL): chapter-planner PASS, validation checklist PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Test content-implementer output against cross-cutting validation script from Section VIII
