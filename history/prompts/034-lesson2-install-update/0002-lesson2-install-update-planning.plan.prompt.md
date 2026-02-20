---
id: 0002
title: lesson2-install-update-planning
stage: plan
date: 2025-12-06
surface: terminal
model: claude-sonnet-4-5
feature: 034-lesson2-install-update
branch: 034-lesson2-install-update
user: orchestrator
command: /sp.plan
labels: [content-planning, lesson-revision, pedagogical-design, platform-specific, chapter-planner]
links:
  spec: specs/034-lesson2-install-update/spec.md
  plan: specs/034-lesson2-install-update/plan.md
files:
  - specs/034-lesson2-install-update/plan.md
---

## Prompt

Create implementation plan for Chapter 5 Lesson 2 installation update.

Work Type: CONTENT (educational lesson revision) → chapter-planner subagent

Context:
- Layer 1 (Manual Foundation), B1 proficiency (≤10 concepts)
- Problem: npm-centric outdated, no platform-specific guidance
- Solution: Platform-organized installation (Windows/macOS/Linux)

## Response

Plan created: specs/034-lesson2-install-update/plan.md (304 lines)

5 Implementation Phases:
- Phase 0: Research & Validation (1-2 hrs)
- Phase 1: Main Lesson Update (4 hrs) - platform sections
- Phase 2: Summary Rewrite (1 hr)
- Phase 3: Cross-Reference Validation (0.5 hrs)
- Phase 4: Validation & Testing (2 hrs) - factual-verifier
- Phase 5: Final Review (0.5 hrs)

Total: 8-12 hours | Timeline: Dec 6-9

Cognitive Load: 8 concepts (unchanged), platform organization reduces effective load ✅

## Outcome

- ✅ Plan complete, ready for Phase 0
- 📁 plan.md (5 phases, constitutional alignment verified)
- 🔁 Next: /sp.tasks 034-lesson2-install-update
