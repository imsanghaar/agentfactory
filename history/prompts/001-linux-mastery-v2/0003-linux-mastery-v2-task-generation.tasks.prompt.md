---
id: "0003"
title: "Linux Mastery v2 Task Generation"
stage: tasks
date: 2026-02-08
surface: claude-code
model: claude-opus-4-6
feature: 001-linux-mastery-v2
branch: 001-linux-mastery-v2
user: user
command: /sp.tasks
labels: [linux, task-generation, v2, content-work]
links:
  spec: specs/001-linux-mastery-v2/spec.md
  plan: specs/001-linux-mastery-v2/plan.md
  ticket: ""
  adr: ""
  pr: ""
files:
  - specs/001-linux-mastery-v2/tasks.md
tests:
  - 27 tasks generated across 5 phases
  - All 14 lessons + quiz covered
  - Cross-cutting validation tasks for FR-004/005/006/012/016/019
---

## Prompt

User invoked `/sp.tasks` for feature `001-linux-mastery-v2`. Prerequisites checked: spec.md (340 lines) and plan.md (1591 lines) both present. Generated actionable task breakdown from plan with content-implementer subagent embedding per lesson task.

## Response snapshot

Generated 27 tasks organized across 5 phases:
- **Phase 1: Setup (T001-T002)** — README update with corrected prerequisites, agent_main.py asset creation (45-line FastAPI sample from plan Section V)
- **Phase 2: L1 Foundation (T003-T006)** — Lessons 01-04 (CLI Mindset, File Operations [NEW], Text Editing & Pipes [NEW], Package Management & Shell Config). All B1/L1/Manual with 3+ exercises each.
- **Phase 3: L2 Collaboration (T007-T013)** — Lessons 05-11 (tmux, Users & Permissions [SPLIT], File Permissions & Ownership [SPLIT], Process Management, Networking & SSH [NEW], systemd & Services, Shell Scripting). All B2/L2 with invisible Three Roles.
- **Phase 4: L3/L4 Advanced (T014-T016)** — Lessons 12-14 (Troubleshooting Toolkit [SPLIT], Performance & Monitoring [SPLIT], Capstone Digital FTE Deployment). C1 proficiency, L3/L4 layers.
- **Phase 5: Quiz & Validation (T017-T027)** — Quiz generation (50 questions), 6 cross-cutting validation tasks (FR-006 meta-commentary, FR-004 Three Roles, FR-005 Try With AI, FR-016 exercises, FR-019 factual accuracy, FR-012 cognitive load), summary generation, cleanup, final A- scoring target.

Each lesson task embeds: content-implementer subagent + educational-validator + relevant skills (learning-objectives, ai-collaborate-teaching for L2+, fact-check-lesson).

## Outcome

- Impact: Complete task breakdown ready for implementation execution
- Tests: All 14 lessons + quiz mapped to tasks, all cross-cutting FRs have validation tasks
- Files: 1 file written (tasks.md, 27 tasks)
- Next prompts: Implementation via content-implementer subagents per task, starting with T001 (README) and T002 (agent_main.py)
- Reflection: Tasks correctly embed subagent protocol (autonomous execution, absolute paths, returns confirmation not content). Parallel markers [P] enable efficient multi-lesson execution within phases.

## Evaluation notes (flywheel)

- Failure modes observed: `check-prerequisites.sh` warned about multiple `001-*` spec directories (non-blocking)
- Graders run and results (PASS/FAIL): Task coverage check PASS (all lessons + quiz + validation covered)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Execute T001-T002 setup tasks first, then parallel L1 lessons T003-T006
