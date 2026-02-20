---
id: "0003"
title: "chapter-07-finance-plan"
stage: plan
date: 2026-01-01
surface: claude-code
model: claude-opus-4-5
feature: 061-chapter-07-finance
branch: 061-chapter-07-finance
user: orchestrator
command: /sp.plan
labels: [chapter, finance, planning, educational-content]
links:
  spec: specs/061-chapter-07-finance/spec.md
  ticket: N/A
  adr: N/A
  pr: N/A
files:
  - specs/061-chapter-07-finance/plan.md
tests:
  - pedagogical arc validated
  - cognitive load limits verified
  - layer progression checked
---

## Prompt

Create implementation plan for Chapter 7: Claude Code for Finance Professionals

Context:
- Part 2, Position 07
- Target: Non-technical finance professionals (A2 to B1 proficiency)
- 10 lessons + quiz following L1 to L2 to L3 to L4 progression

Source materials:
- Agentic_Financial_Planning.pdf
- Claude_Xero_AI_Native_Accounting.pdf
- Annex-1_Learning_Outcomes_revised.pdf

Requirements:
- Lesson-by-lesson breakdown with learning objectives
- Pedagogical arc (Foundation to Practice to Integration to Mastery)
- Cognitive load assessment per lesson
- "Try With AI" prompt themes

## Response snapshot

Created comprehensive implementation plan via chapter-planner subagent:

**Pedagogical Arc (4 Phases)**:
- Phase 1 (Foundation): Lessons 1-2 - L1 paradigm shift, workspace setup
- Phase 2 (Practice): Lessons 3-6 - L2 prompting, modeling, sheets, accounting
- Phase 3 (Integration): Lessons 7-8 - L2->L3 scenarios, multi-agent concepts
- Phase 4 (Mastery): Lessons 9-10 - L2/L4 governance, capstone

**10 Lessons Planned**:
1. Finance AI Transformation (L1, A2, 15min)
2. Finance Workspace Setup (L1->L2, A2, 20min)
3. Prompt Engineering for Finance (L2, A2, 25min)
4. Intent-Driven Financial Modeling (L2, A2->B1, 25min)
5. Claude Code + Sheets Architecture (L2, B1, 25min)
6. AI-Native Accounting Workflows (L2, B1, 25min)
7. Scenario Analysis & Risk (L2->L3, B1, 25min)
8. Multi-Agent Finance Patterns (L3, B1, 20min)
9. Governance, Compliance, Safety (L2, B1, 20min)
10. Capstone Workflow (L4, B1, 30min)

All lessons include learning objectives, key concepts (5-7), source mappings, and 3 "Try With AI" themes.

## Outcome

- Impact: Complete implementation plan ready for task generation
- Tests: Layer progression validated, cognitive load within limits
- Files: specs/061-chapter-07-finance/plan.md (450+ lines)
- Next prompts: /sp.tasks
- Reflection: Plan properly routes through chapter-planner subagent

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Pedagogical validation PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to task generation
