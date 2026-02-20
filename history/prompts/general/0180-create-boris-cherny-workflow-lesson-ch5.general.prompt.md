---
id: "0180"
title: "Create Boris Cherny Workflow Lesson Ch5"
stage: general
date: 2026-01-08
surface: agent
model: claude-opus-4-5-20251101
feature: none
branch: ch5-cc-workflow
user: Rehan-Ul-Haq
command: /sp.chapter
labels: ["chapter-5", "claude-code", "boris-cherny", "workflow", "lesson-creation", "content-implementation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/16-creator-workflow.md
  - apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/16-creator-workflow.summary.md
  - apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/README.md
tests:
  - none
---

## Prompt

> /sp.chapter we have written ch5 @apps\learn-app\docs\02-AI-Tool-Landscape\05-claude-code-features-and-workflows . Now there is an article from creator of claude code how he uses claude code. follow this link https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are to get complete article. We have covered the claude code concepts now we want to add last lessons for students to provide how claude code creator uses claude code and connect with concepts.

## Response snapshot

Created Lesson 16 "The Creator's Workflow: How Boris Uses Claude Code" for Chapter 5. The lesson maps Boris Cherny's production workflow techniques to chapter concepts: parallel sessions (L01+L11), Plan Mode discipline (L11), team CLAUDE.md practices (L08), specialized subagents (L11), verification loops (L09+L13), PostToolUse hooks (L13), permissions management (L12), and Opus 4.5 model selection (L12). Includes 4 "Try With AI" prompts and chapter summary. Also created summary file and updated README.

## Outcome

- ✅ Impact: Added final capstone lesson connecting expert practice to learned concepts, completing Chapter 5 pedagogical arc
- 🧪 Tests: none (content lesson, no code)
- 📁 Files: 3 files (1 new lesson, 1 summary, 1 README update)
- 🔁 Next prompts: Validate lesson against constitution; consider adding quiz questions for lesson 16
- 🧠 Reflection: Synthesis lessons that map expert practice to taught concepts provide powerful "aha" moments for students seeing how pieces fit together

## Evaluation notes (flywheel)

- Failure modes observed: Initial WebFetch to VentureBeat returned 429 (rate limit); resolved via WebSearch + alternative sources (paddo.dev, substack)
- Graders run and results (PASS/FAIL): Manual review - content aligns with chapter structure and quality patterns
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Add verification via educational-validator subagent for constitutional compliance check
