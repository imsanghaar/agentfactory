---
id: "0002"
title: chapter-53-dapr-core-spec
stage: spec
date: 2025-12-29
surface: claude-code
model: claude-opus-4-5-20250514
feature: chapter-53-dapr-core
branch: main
user: mjs
command: /sp.specify
labels: [chapter, dapr, part-7, educational-content]
links:
  spec: specs/chapter-53-dapr-core/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/chapter-53-dapr-core/spec.md
  - specs/chapter-53-dapr-core/checklists/requirements.md
tests:
  - null
---

## Prompt

Create specification for Chapter 53: Dapr Core - Sidecar Building Blocks for AI Microservices

CONTEXT:
- Part: 7 (AI Cloud-Native Development)
- Chapter Number: 53
- Prerequisites: Ch49 (Docker), Ch50 (Kubernetes), Ch51 (Helm), Ch52 (Kafka)
- Running example: Task API (FastAPI agent from Part 6, deployed throughout Part 7)
- Target proficiency: B1 (intermediate)
- Platform: Docker Desktop Kubernetes
- Expertise skill created: .claude/skills/building-with-dapr/SKILL.md

SCOPE FOR CH53 (Core only - Actors/Workflows deferred to Ch59):
- Dapr sidecar architecture and building block concept
- Service invocation, state management, pub/sub, bindings, secrets, configuration
- Dapr CLI and local development
- Deploying Dapr on Kubernetes with Helm

SKILL-FIRST PATTERN (MANDATORY):
- L00: "Build Your Dapr Skill" - students create `dapr-deployment` skill FIRST
- Every lesson L01+ ends with "Reflect on Your Skill" section
- Student skill name: dapr-deployment

## Response snapshot

Created comprehensive specification for Chapter 53: Dapr Core with:
- 11 lessons (L00-L10) following Skill-First Learning Pattern
- L00: Build Your Dapr Skill using /fetching-library-docs and /skill-creator
- L01-02: Dapr Foundations (sidecar pattern, building blocks concept)
- L03-08: Core Building Blocks (Helm deployment, state, invoke, pubsub, bindings, secrets)
- L09: Capstone - Dapr-Enabled Task API (spec-driven refactoring of Part 6 agent)
- L10: Finalize Your Dapr Skill
- Layer progression: L1 (conceptual) → L2 (AI collaboration) → L3 (skill) → L4 (capstone)
- Clear scope: Core building blocks only, Actors/Workflows deferred to Ch59
- Technology choices: Dapr 1.14+, Redis for state/pubsub, Docker Desktop K8s

## Outcome

- ✅ Impact: Complete specification ready for planning and implementation
- 🧪 Tests: Checklist validated all items pass
- 📁 Files: 2 (spec.md, checklists/requirements.md)
- 🔁 Next prompts: /sp.clarify, /sp.plan
- 🧠 Reflection: Specification follows Ch52 quality reference, includes Assumed Knowledge section and layer progression

## Evaluation notes (flywheel)

- Failure modes observed: None - spec created successfully
- Graders run and results (PASS/FAIL): Manual checklist PASS
- Prompt variant (if applicable): Educational content with Skill-First pattern
- Next experiment (smallest change to try): Proceed to clarification and planning
