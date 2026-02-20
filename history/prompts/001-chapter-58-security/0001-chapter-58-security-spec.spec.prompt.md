---
id: 0001
title: chapter-58-security-spec
stage: spec
date: 2025-12-30
surface: cli
model: claude-opus-4-5-20250514
feature: 001-chapter-58-security
branch: 001-chapter-58-security
user: mjs
command: /sp.specify
labels: [chapter-58, security, kubernetes, rbac, networkpolicy, pss]
links:
  spec: specs/001-chapter-58-security/spec.md
  ticket:
  adr:
  pr:
files:
  - specs/001-chapter-58-security/spec.md
  - specs/001-chapter-58-security/checklists/requirements.md
tests:
  - checklist validation passed
---

## Prompt

Create specification for Chapter 58: Production Security & Compliance

CONTEXT (from Phase A skill):
- Framework/SDK: Kubernetes Security (RBAC, NetworkPolicy, PSS, Secrets, Trivy, Cosign, Dapr Security)
- Expertise skill created: .claude/skills/building-with-cloud-security/SKILL.md
- Running example: Task API (secure it for production)
- Target proficiency: B1 (intermediate)
- Part 7: AI Cloud Native Development (Enterprise Tier)
- Prerequisites: Ch49-57 (Foundation), Ch55-56 (Observability, Traffic)
- Platform: Docker Desktop Kubernetes

REQUIRED IN SPEC:
1. Chapter overview with learning outcomes
2. Lesson breakdown with L00 FIRST (Skill-First pattern)
3. Layer progression: L1 (manual) → L2 (collaboration) → L3 (skill) → L4 (orchestration)
4. Prerequisites from earlier chapters
5. Reference to expertise skill for accurate API patterns
6. Student skill name: cloud-security

OUTPUT: specs/chapter-58-production-security-compliance/spec.md

## Response snapshot

Created comprehensive specification for Chapter 58: Production Security & Compliance including:
- 10 lessons (L00-L09) following Skill-First pattern
- 10 user stories with acceptance scenarios
- 14 functional requirements
- 8 measurable success criteria
- Layer progression from L1 (manual RBAC/NetworkPolicy/PSS) through L4 (capstone)
- Assumed knowledge and prerequisites documented
- Edge cases and scope boundaries defined

## Outcome

- ✅ Impact: Specification complete, ready for planning
- 🧪 Tests: Checklist validation passed (all items checked)
- 📁 Files: spec.md, checklists/requirements.md created
- 🔁 Next prompts: /sp.clarify, then /sp.plan
- 🧠 Reflection: Expertise skill created in Phase A provides accurate patterns for content

## Evaluation notes (flywheel)

- Failure modes observed: None - followed /sp.chapter workflow
- Graders run and results (PASS/FAIL): Checklist PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
