---
id: "0006"
title: "analysis-remediation-plus-lesson-10"
stage: tasks
date: 2025-12-22
surface: claude-code
model: claude-opus-4-5-20251101
feature: 001-docker-chapter
branch: 001-docker-chapter
user: mjs
command: manual iteration
labels: [remediation, lesson-10, layer-3, intelligence-design]
links:
  spec: specs/001-docker-chapter/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-docker-chapter/spec.md
  - specs/001-docker-chapter/tasks.md
tests:
  - null
---

## Prompt

User request following /sp.analyze:

1. Fix both MEDIUM issues identified in analysis (FR-025 coverage gap, Gordon availability)
2. Add Lesson 10: Building an agent skill to build production-ready multi-stage images

Context: Analysis found 97.6% coverage, 2 MEDIUM issues. User wants to add Layer 3 (Intelligence Design) lesson to complete the 4-Layer Teaching Method progression.

## Response snapshot

Addressed all requests with comprehensive updates to spec.md and tasks.md.

**MEDIUM Issue Fixes**:

1. **C1 (FR-025 coverage)**: Added T056a to L5: "Write hands-on exercise: handle large model files (>1GB) with volume mounts instead of COPY"

2. **U1 (Gordon availability)**: Added T086a to L8: "Write Gordon availability note: Requires Docker Desktop 4.55+. Fallback: manual Dockerfile writing with optimization principles from L5-L7"

**Lesson 10 Addition** (Layer 3: Intelligence Design):

New lesson: "Building the Production Dockerfile Skill"
- 16 new tasks (T109-T124)
- User Story 7 added to spec.md
- 7 new Functional Requirements (FR-043 to FR-049)
- Success Criterion SC-011 added
- Teaching modality: Intelligence Design (Persona+Questions+Principles)

**Updated Totals**:
- Lessons: 9 → 10
- Tasks: 115 → 133
- Phases: 12 → 13
- FRs: 42 → 49
- SCs: 10 → 11
- Implementation time: 26-34h → 30-40h

**Layer Progression Now Complete**:
| Layer | Lessons | Purpose |
|-------|---------|---------|
| L1 (Manual) | 1-7 | Build mental models |
| L2 (AI Collaboration) | 8 | Gordon workflows |
| L4 (Spec-Driven) | 9 | Capstone project |
| L3 (Intelligence Design) | 10 | Create reusable skill |

**Key Design Decision**: L3 comes AFTER L4 because students need complete end-to-end experience before they can identify patterns worth encoding as reusable intelligence.

## Outcome

- ✅ Impact: Chapter expanded from 9 to 10 lessons with full 4-Layer coverage; both MEDIUM issues resolved
- 🧪 Tests: N/A (content planning)
- 📁 Files: spec.md (updated), tasks.md (updated)
- 🔁 Next prompts: /sp.implement or manual lesson writing
- 🧠 Reflection: Lesson 10 demonstrates the book's core thesis ("specs are the new syntax" → "skills are the new libraries"). Students don't just LEARN Docker—they CREATE reusable intelligence that compounds across future projects.

## Evaluation notes (flywheel)

- Failure modes observed: None - clean integration of new lesson
- Graders run and results (PASS/FAIL): Coverage now 100% (49/49 FRs have tasks)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Track whether skill-building lesson (L10) produces skills that students actually reuse in subsequent chapters
