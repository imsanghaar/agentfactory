---
id: 0001
title: ch46-tdd-agents-spec
stage: spec
date: 2025-12-30
surface: claude-code
model: claude-opus-4-5-20250514
feature: 001-ch46-tdd-agents
branch: 001-ch46-tdd-agents
user: mjs
command: /sp.specify
labels: [chapter, tdd, testing, agents, part6]
links:
  spec: specs/001-ch46-tdd-agents/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-ch46-tdd-agents/spec.md
  - specs/001-ch46-tdd-agents/checklists/requirements.md
tests:
  - null
---

## Prompt

Create specification for Chapter 46: TDD for Agents

CONTEXT:
- Part 6: AI Native Software Development (Chapter 46)
- This is Phase 4: Quality Assurance in the Part 6 learning arc
- Prerequisites: Ch40-45 (complete agent stack), basic pytest knowledge from Part 5
- Running example: Task API from Chapter 40 (add comprehensive test suite)
- Target proficiency: B1-B2 (intermediate to upper-intermediate)
- Platform: pytest, pytest-asyncio, httpx for async testing, respx for mocking

EXPERTISE SKILL CREATED:
- .claude/skills/testing-ai-agents/SKILL.md (Phase A complete)

CRITICAL DISTINCTION - TDD vs EVALS:
- TDD (This Chapter): Code correctness (deterministic, passes/fails)
- EVALS (Chapter 47): Reasoning quality (probabilistic, scores)

SKILL-FIRST PATTERN (MANDATORY):
- L00: "Build Your Testing Skill" - students create `agent-tdd` skill
- Every lesson ends with "Reflect on Your Skill" section
- Student skill name: agent-tdd

LESSON STRUCTURE (L00-L08, 9 lessons total)

## Response snapshot

Created comprehensive specification for Chapter 46: TDD for Agents with:
- 7 user stories covering skill creation, FastAPI testing, LLM mocking, SQLModel testing, tool testing, integration testing, and capstone
- 27 functional requirements organized by category
- 10 success criteria (measurable outcomes + learning validation)
- Clear lesson structure with layer progression L1→L2→L3→L4
- Assumed Knowledge section documenting prerequisites
- Output file structure for 9 lessons + quiz + README

## Outcome

- ✅ Impact: Specification ready for planning phase
- 🧪 Tests: N/A (spec phase)
- 📁 Files: 2 files created (spec.md, requirements.md checklist)
- 🔁 Next prompts: /sp.plan for implementation planning
- 🧠 Reflection: Clear TDD vs Evals boundary established; Skill-First pattern properly integrated

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All checklist items PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
