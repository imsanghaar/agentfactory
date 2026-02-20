---
id: PHR-001-ch6-business-workflows-spec
title: Chapter 6 Business Workflows Specification
stage: spec
date: 2025-12-31
surface: claude-code
model: claude-opus-4-5-20250101
feature: 001-ch6-business-workflows
branch: 001-ch6-business-workflows
user: user
command: /sp.specify
labels: [chapter, specification, business-workflows, social-media]
links:
  spec: specs/001-ch6-business-workflows/spec.md
  ticket: "#554"
  adr: N/A
  pr: N/A
files:
  - specs/001-ch6-business-workflows/spec.md
  - specs/001-ch6-business-workflows/checklists/requirements.md
tests:
  - N/A
---

## Prompt

Chapter 6: Business Workflows & Social Media - A practical chapter teaching students to apply Claude Code skills learned in Chapter 5 to real-world business automation projects. Reference: #554, Gemini Share. Structure: README.md + L1: Email Communication (drafting, templates, summarization) + L2: WhatsApp Business Communication + L3: LinkedIn (profile, posts, connections) + L4: Twitter/X (threads, engagement, content calendar) + Chapter Quiz

## Response snapshot

Created comprehensive specification for Chapter 6: Business Workflows & Social Media with:

1. **Chapter Overview**: Bridges Chapter 5 (Claude Code fundamentals) to practical application
2. **Proficiency Level**: A2 (Elementary) - applying known tools to new contexts
3. **Pedagogical Layer**: L2 (Collaboration) - AI as Teacher/Student/Co-Worker
4. **4 User Stories**: Email (P1), WhatsApp (P2), LinkedIn (P2), Twitter/X (P3)
5. **14 Functional Requirements**: Covering lessons, skills, structure
6. **12 Success Criteria**: Measurable, technology-agnostic outcomes
7. **Detailed Lesson Structure**: Each lesson builds a working Agent Skill
8. **Assumptions & Dependencies**: Chapter 5 prerequisite, Chapter 7 follow-on

Deliverables:
- `/email-assistant` skill (L1)
- `/whatsapp-business` skill (L2)
- `/linkedin-creator` skill (L3)
- `/twitter-creator` skill (L4)

## Outcome

- Impact: Specification complete and validated, ready for planning phase
- Tests: N/A (specification phase)
- Files: 2 files created (spec.md, requirements.md checklist)
- Next prompts: /sp.clarify or /sp.plan to proceed with implementation planning
- Reflection: Spec created without clarification markers by applying reasonable defaults (character limits, lesson duration, language scope)

## Evaluation notes (flywheel)

- Failure modes observed: None - context reading prevented common issues
- Graders run and results (PASS/FAIL): Quality checklist PASS (all items validated)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A - proceed to planning
