---
id: "0003"
title: "ch60-cloud-deployment-plan"
stage: plan
date: 2025-12-30
surface: cli
model: claude-opus-4-5
feature: 001-ch60-cloud-deployment
branch: 001-ch60-cloud-deployment
user: mjs
command: /sp.plan
labels: [chapter-60, cloud-deployment, implementation-plan]
links:
  spec: specs/001-ch60-cloud-deployment/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-ch60-cloud-deployment/plan.md
tests:
  - null
---

## Prompt

Create implementation plan for Chapter 60: Real Cloud Deployment based on specs/001-ch60-cloud-deployment/spec.md

## Response snapshot

Generated comprehensive implementation plan (1074 lines) using chapter-planner subagent:

**Chapter Analysis**:
- Type: Technical/Code-Focused
- Proficiency: B1 (Intermediate)
- Concept Density: 12 core concepts across 11 lessons

**Lesson Structure**:
| Layer | Lessons | Focus |
|-------|---------|-------|
| L3 (Skill-First) | L00 | Create multi-cloud-deployer skill |
| L1 (Manual) | L01-L04, L07 | Cloud fundamentals, CLI tools |
| L2 (AI Collab) | L05-L06, L08-L09 | Full stack deployment, verification |
| L4 (Capstone) | L10 | Spec-driven production deployment |

**Key Features**:
- Skill-First pattern enforced (L00 first)
- "Reflect on Your Skill" in every lesson
- Three Roles Framework invisible in L2 lessons
- Expected output blocks for all commands
- Multi-cloud comparison (DOKS, Hetzner, AKS, GKE, EKS, Civo)

**Assessment Plan**:
- Formative: Verification checks per lesson
- Summative: L10 capstone rubric (spec completeness, deployment success, skill quality, teardown)

## Outcome

- ✅ Impact: Complete implementation plan ready for task generation
- 🧪 Tests: All validation checklists passed (Stage, Cognitive Load, Three Roles, Skill-First)
- 📁 Files: specs/001-ch60-cloud-deployment/plan.md (1074 lines)
- 🔁 Next prompts: /sp.tasks
- 🧠 Reflection: chapter-planner subagent produced comprehensive plan with proper constitutional alignment

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All validation sections PASS
- Prompt variant (if applicable): Standard chapter planning with Skill-First pattern
- Next experiment (smallest change to try): N/A - proceed to task generation
