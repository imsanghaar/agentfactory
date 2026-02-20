---
id: "0001"
title: "ch60-cloud-deployment-spec"
stage: spec
date: 2025-12-30
surface: cli
model: claude-opus-4-5
feature: 001-ch60-cloud-deployment
branch: 001-ch60-cloud-deployment
user: mjs
command: /sp.specify
labels: [chapter-60, cloud-deployment, doks, hetzner-k3s, multi-cloud]
links:
  spec: specs/001-ch60-cloud-deployment/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-ch60-cloud-deployment/spec.md
  - specs/001-ch60-cloud-deployment/checklists/requirements.md
tests:
  - null
---

## Prompt

Create specification for Chapter 60: Real Cloud Deployment

CONTEXT:
- Part 7: AI Cloud Native Development (Enterprise Tier - FINAL)
- Prerequisites: Ch49-59 (Full Foundation + Enterprise)
- Running example: Task API (deploy to real cloud)
- Target proficiency: B1 (intermediate)
- Expertise skill created: .claude/skills/building-with-multi-cloud/SKILL.md

KEY INSIGHT:
Only cluster provisioning differs between clouds. Everything else is identical:
- kubectl commands: same
- Helm deployments: same
- Ingress/cert-manager: same
- Dapr installation: same
- Secrets management: same

TWO PATHS FOR STUDENTS:
1. Production path: DigitalOcean DOKS (~$24+/mo managed)
2. Learning sandbox: Hetzner + K3s (~$5/mo self-managed)

LESSON STRUCTURE: L00-L10 (11 lessons), Skill-First pattern with L00 first

## Response snapshot

Created comprehensive specification for Chapter 60 with:
- 6 user stories (P1-P3 priorities)
- 14 functional requirements
- 8 success criteria
- 11-lesson structure with layer progression
- Assumed knowledge section
- Edge cases and dependencies documented

Key features:
- Skill-First pattern with L00 creating multi-cloud-deployer skill
- Two learning paths (DOKS production / Hetzner budget)
- Key insight articulated: only provisioning differs
- Full CEFR B1 proficiency alignment
- Educational checklist passed

## Outcome

- ✅ Impact: Specification complete and validated
- 🧪 Tests: All checklist items passed
- 📁 Files: spec.md + requirements.md checklist
- 🔁 Next prompts: /sp.clarify or /sp.plan
- 🧠 Reflection: Spec is comprehensive with clear scope boundaries

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Checklist PASS (all items)
- Prompt variant (if applicable): Standard chapter spec
- Next experiment (smallest change to try): N/A - proceed to planning
