---
id: "0001"
title: "freemium-tracker-spec"
stage: spec
date: 2026-02-04
surface: cli
model: claude-opus-4-5
feature: 001-freemium-tracker
branch: 001-freemium-tracker
user: mjunaidca
command: /sp.specify
labels: [metering, billing, freemium, token-tracking]
links:
  spec: specs/001-freemium-tracker/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-freemium-tracker/spec.md
  - specs/001-freemium-tracker/checklists/requirements.md
tests:
  - null
---

## Prompt

Agent Factory Freemium Token Tracking System - Custom token metering and billing-ready service for study-mode-api with flexible limits, credit system, and 20% markup calculation.

Core Requirements:

1. Token Tracking: Track input/output tokens per user per request
2. Flexible Limits: Support lifetime (5 uses), daily, monthly, or balance-based limits per tier
3. Real-time Blocking: Pre-request check, block with 402 if limit exceeded
4. Credit System: Topped-up balance (paid) + Granted balance (students)
5. 20% Markup: Calculate marked-up cost, deduct from user credits
6. Agent Hooks: Integrate with OpenAI Agents SDK RunHooks
7. Audit Log: Immutable transaction log in PostgreSQL
8. Cache Layer: Redis for fast balance checks (<1ms)

Technical Constraints: Python 3.13+ functional programming, extend existing study-mode-api, use existing Redis/PostgreSQL, no external billing dependencies.

## Response snapshot

Created comprehensive specification with:

- 5 prioritized user stories (P1-P5): free limits, student grants, top-ups, analytics, lifetime trials
- 19 functional requirements across core metering, credit system, tier management, audit, and integration
- 8 measurable success criteria (all technology-agnostic)
- 6 edge cases with expected behavior
- Clear assumptions, constraints, and out-of-scope definitions
- 3 key entities: TokenTier, TokenAccount, TokenTransaction

## Outcome

- ✅ Impact: Complete spec ready for planning phase
- 🧪 Tests: N/A (spec phase)
- 📁 Files: spec.md, checklists/requirements.md
- 🔁 Next prompts: /sp.plan to create implementation plan
- 🧠 Reflection: Spec covers all user requirements without implementation details; functional programming constraint documented

## Evaluation notes (flywheel)

- Failure modes observed: None - spec created successfully
- Graders run and results (PASS/FAIL): Manual checklist review - PASS (all items checked)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
