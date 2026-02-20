---
id: "0002"
title: "spec-iteration-9-lessons"
stage: spec
date: 2025-12-22
surface: claude-code
model: claude-opus-4-5-20251101
feature: 001-docker-chapter
branch: 001-docker-chapter
user: mjs
command: spec iteration
labels: [spec-iteration, learning-sciences, 9-lessons]
links:
  spec: specs/001-docker-chapter/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-docker-chapter/spec.md
  - specs/001-docker-chapter/checklists/requirements.md
tests:
  - null
---

## Prompt

User feedback on initial 8-lesson spec:

1. Do we need docker compose? Maybe Yes.
2. I feel like something is missing after lesson 2, this is hello world we jump to lesson 3. And there can be a lesson just to install and setup docker. Then what about getting familiar with docker components manually and with AI agents and writing a simple docker file for hello world fastapi guide. Then we can go to Multi Stage Builds and then the following ones come? What do you suggest?

Reference: Gemini CLI lesson (03-built-in-tools-deep-dive.md) as format reference.

## Response snapshot

Revised spec from 8 lessons to 9 lessons based on learning sciences feedback.

**Key Changes:**

1. **Docker Compose**: Confirmed essential (keep as Lesson 6)

2. **Identified Cognitive Gap**: Original structure jumped from "Write Dockerfile" → "Multi-Stage Builds" too quickly. Students need to:
   - Install Docker first (was implicit)
   - Operate/debug containers before optimizing

3. **New Learning Progression**:
```
Install → Understand → Create → Operate → Optimize → Compose → Secure → AI-Assist → Capstone
   1          2           3         4          5          6         7          8          9
```

4. **Added Lessons**:
   - **Lesson 1**: Docker Installation & Setup (30-45 min)
   - **Lesson 4**: Container Lifecycle & Debugging (45-60 min)

5. **Key Principle Applied**: "You must be able to run and debug containers before you can optimize them"

6. **Updated Spec Metrics**:
   - User Stories: 7 (was 6) - added US-0 (install) and US-1.5 (debugging)
   - Functional Requirements: 42 (was 26) - organized by 9 lessons
   - Success Criteria: 10 (was 8) - added installation and debugging metrics

## Outcome

- ✅ Impact: Spec now follows concrete-first, operate-before-optimize pedagogy
- 🧪 Tests: N/A (specification phase)
- 📁 Files: spec.md updated (654 lines), requirements.md checklist updated
- 🔁 Next prompts: /sp.plan to generate lesson structure and tasks
- 🧠 Reflection: User feedback correctly identified missing "operate" phase. Learning sciences principle: students must debug before they optimize.

## Evaluation notes (flywheel)

- Failure modes observed: Initial spec skipped installation lesson and debugging lesson
- Graders run and results (PASS/FAIL): Requirements checklist PASS (all items validated post-revision)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to /sp.plan and validate 9-lesson breakdown produces balanced cognitive load per lesson
