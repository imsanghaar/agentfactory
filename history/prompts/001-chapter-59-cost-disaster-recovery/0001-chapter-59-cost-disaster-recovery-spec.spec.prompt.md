---
id: 0001
title: chapter-59-cost-disaster-recovery-spec
stage: spec
date: 2025-12-30
surface: claude-code
model: claude-opus-4
feature: 001-chapter-59-cost-disaster-recovery
branch: 001-chapter-59-cost-disaster-recovery
user: mjs
command: /sp.specify
labels: [chapter, part7, cost, disaster-recovery, operational-excellence]
links:
  spec: specs/001-chapter-59-cost-disaster-recovery/spec.md
  ticket:
  adr:
  pr:
files:
  - specs/001-chapter-59-cost-disaster-recovery/spec.md
  - specs/001-chapter-59-cost-disaster-recovery/checklists/requirements.md
tests:
  - N/A (specification phase)
---

## Prompt

Create specification for Chapter 59: Cost & Disaster Recovery

CONTEXT:
- Part 7: AI Cloud Native Development (Enterprise Tier)
- Prerequisites: Ch49-58 (Foundation + Security)
- Running example: Task API (make it cost-aware and resilient)
- Target proficiency: B1 (intermediate)
- Platform: Docker Desktop Kubernetes (with cloud cost concepts)

SKILL-FIRST PATTERN (MANDATORY):
- L00: "Build Your Operational Excellence Skill" - students create `operational-excellence` skill
- Every lesson L01+ ends with "Reflect on Your Skill" section
- Student skill name: operational-excellence

LESSON STRUCTURE (L00-L09, 10 lessons):
- L00: Build Your Operational Excellence Skill
- L01: Cloud Cost Fundamentals
- L02: Right-Sizing with VPA
- L03: OpenCost/Kubecost Visibility
- L04: FinOps Practices & Budget Alerts
- L05: Backup Fundamentals
- L06: Velero for K8s Backup/Restore
- L07: Chaos Engineering Basics
- L08: Data Sovereignty & Compliance
- L09: Capstone - Resilient, Cost-Aware Task API

## Response snapshot

Created comprehensive specification for Chapter 59 with:
- 10 lessons (L00-L09) following skill-first pattern
- 8 user stories covering skill building, cost management, DR, and chaos engineering
- 19 functional requirements with clear testability
- 10 success criteria aligned with learning objectives
- 4-layer teaching progression documented
- Technology choices justified (OpenCost, VPA, Velero, Chaos Mesh)
- Assumed knowledge and dependencies clearly listed
- Out of scope items defined to prevent scope creep

All checklist items pass - no [NEEDS CLARIFICATION] markers.

## Outcome

- ✅ Impact: Complete chapter specification ready for planning
- 🧪 Tests: N/A (specification phase)
- 📁 Files: spec.md, checklists/requirements.md
- 🔁 Next prompts: /sp.clarify → /sp.plan
- 🧠 Reflection: Skill-first pattern well-integrated with lesson structure

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All checklist items PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
