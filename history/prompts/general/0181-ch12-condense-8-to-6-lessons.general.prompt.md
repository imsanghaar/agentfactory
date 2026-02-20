---
id: "0181"
title: "Ch12 condense 8 to 6 lessons"
stage: general
date: 2026-02-17
surface: claude-code
model: claude-opus-4-6
feature: none
branch: ch12-condense-8-to-6-lessons
user: mjs
command: /sp.git.commit_pr
labels: [ch12, restructure, content]
links:
  spec: none
  ticket: none
  adr: none
  pr: https://github.com/panaversity/agentfactory/pull/736
files:
  - apps/learn-app/docs/02-Agent-Workflow-Primitives/12-meet-your-first-ai-employee/04-how-your-employee-works.md
  - apps/learn-app/docs/02-Agent-Workflow-Primitives/12-meet-your-first-ai-employee/06-chapter-assessment.md
  - apps/learn-app/docs/02-Agent-Workflow-Primitives/12-meet-your-first-ai-employee/README.md
  - apps/learn-app/docs/02-Agent-Workflow-Primitives/13-build-first-ai-employee/14-when-your-employee-codes.md
tests:
  - none
---

## Prompt

Phase A: condense Ch12 from 8 to 6 lessons. Merge L06 into L04, move L07 to Ch13, rename L08 to L06, update all cross-references, fix dates, add "What OpenClaw Proved/Didn't Solve" to assessment.

## Response snapshot

Condensed Ch12 from 8 to 6 lessons: merged L06 (Patterns That Transfer) synthesis content into L04 (4-framework table, "Why These 6", Agent Autopsy prompt), moved L07 (When Your Employee Codes) to Ch13 as L14, renamed L08 assessment to L06 (removed L07-dependent Q11/Q12, updated scoring /12→/10, added "What OpenClaw Proved/Didn't Solve" tables). Updated all frontmatter, cross-references, README. Net: -212 lines, 11 files changed. PR #736.

## Outcome

- ✅ Impact: Ch12 reduced from 8 to 6 lessons, eliminating pattern repetition and chatbot-task gap
- 🧪 Tests: Manual verification of cross-references and file structure
- 📁 Files: 11 files (3 modified, 3 renamed/moved, 2 deleted, 2 summaries updated, 1 README)
- 🔁 Next prompts: Phase B (move Ch12 to Part 1, renumber Ch7-11)
- 🧠 Reflection: Large restructure executed cleanly by batching edits systematically

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A (content restructure)
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): Phase B cross-reference cascade
