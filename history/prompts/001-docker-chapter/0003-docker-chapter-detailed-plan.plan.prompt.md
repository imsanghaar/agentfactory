---
id: "0003"
title: "docker-chapter-detailed-plan"
stage: plan
date: 2025-12-22
surface: claude-code
model: claude-opus-4-5-20251101
feature: 001-docker-chapter
branch: 001-docker-chapter
user: mjs
command: /sp.plan
labels: [chapter-planning, pedagogical-arc, content-work]
links:
  spec: specs/001-docker-chapter/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-docker-chapter/plan.md
tests:
  - null
---

## Prompt

/sp.plan Now we have to carefully plan the content for our chapter.

Context: 9-lesson Docker chapter spec ready, need detailed pedagogical planning.

## Response snapshot

Created comprehensive implementation plan via chapter-planner agent.

**Plan Structure (569 lines)**:
1. **Pedagogical Architecture**: 9-lesson arc (Foundation → Application → Integration → Validation → Mastery)

2. **Per-Lesson Planning** (all 9 lessons):
   - Learning Objectives (Bloom's taxonomy aligned)
   - Concepts Inventory (4-7 per lesson, within B1-B2 limits)
   - Teaching Modality (varied across all lessons)
   - Hands-On Exercises (4+ per lesson)
   - Assessment Strategy
   - Prerequisites chain
   - Expected Outputs

3. **Teaching Modality Variation** (anti-convergence):
   | Lesson | Modality |
   |--------|----------|
   | 1 | Guided Installation |
   | 2 | Hands-On Discovery |
   | 3 | Hands-On Creation |
   | 4 | Error Analysis |
   | 5 | Iterative Optimization |
   | 6 | Specification-First |
   | 7 | Audit & Remediation |
   | 8 | AI Collaboration |
   | 9 | Capstone Project |

4. **Constitution Compliance (v6.0.1)**:
   - ✅ Layer progression: L1 (1-7) → L2 (8) → L4 (9)
   - ✅ Three Roles INVISIBLE (no framework labels)
   - ✅ Meta-commentary prohibited
   - ✅ Cognitive load within CEFR B1-B2 limits

5. **Intelligence Creation Opportunities**:
   - `docker-hardening` skill
   - `dockerfile-optimization` skill
   - `docker-troubleshooting` skill

6. **Capstone Composition Strategy**:
   - Phase 1: Specification (20-30 min)
   - Phase 2: Composition (40-50 min)
   - Phase 3: Validation (15-20 min)
   - Phase 4: Reflection (10 min)

## Outcome

- ✅ Impact: Complete pedagogical plan for 9-lesson Docker chapter
- 🧪 Tests: N/A (planning phase)
- 📁 Files: plan.md (569 lines)
- 🔁 Next prompts: /sp.tasks to generate implementation tasks
- 🧠 Reflection: chapter-planner agent produced comprehensive plan with varied teaching modalities, constitution-compliant structure, and clear implementer instructions

## Evaluation notes (flywheel)

- Failure modes observed: None - chapter-planner successfully created detailed per-lesson plans
- Graders run and results (PASS/FAIL): Constitution compliance verified (all 7 gates PASS)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Proceed to /sp.tasks and validate task granularity produces 4-8 hour implementation chunks per lesson
