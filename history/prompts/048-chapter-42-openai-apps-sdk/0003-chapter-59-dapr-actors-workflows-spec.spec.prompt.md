---
id: "0003"
title: chapter-59-dapr-actors-workflows-spec
stage: spec
date: 2025-12-29
surface: claude-code
model: claude-opus-4-5-20251101
feature: 048-chapter-42-openai-apps-sdk
branch: main
user: mjs
command: /sp.specify
labels: [chapter-59, dapr, actors, workflows, specification]
links:
  spec: specs/chapter-59-dapr-actors-workflows/spec.md
  ticket:
  adr:
  pr:
files:
  - specs/chapter-59-dapr-actors-workflows/spec.md
  - specs/chapter-59-dapr-actors-workflows/checklists/requirements.md
tests:
---

## Prompt

Create specification for Chapter 59: Dapr Actors & Workflows for Stateful Agents

CONTEXT:
- Part 7: AI Cloud Native Development
- Framework/SDK: Dapr Actors (dapr-ext-fastapi) and Dapr Workflows (dapr-ext-workflow)
- Running example: Task API (extend with stateful TaskActor and TaskProcessingWorkflow)
- Target proficiency: B1 (intermediate)
- Prerequisites: Ch53 (Dapr Core)
- Platform: Docker Desktop Kubernetes

SKILL-FIRST PATTERN:
- L00: "Extend Your Dapr Skill" - students extend existing `dapr-deployment` skill
- Every lesson L01+ ends with "Reflect on Your Skill" section

LESSON STRUCTURE (L00-L09):
- L00: Extend Your Dapr Skill with Actors & Workflows
- L01: The Actor Model - Concepts and Mental Model
- L02: Dapr Actors Fundamentals - Implementation with Python
- L03: Actor State Management - Persistence and Concurrency
- L04: Timers and Reminders - Scheduling in Actors
- L05: Dapr Workflows Overview - Durable Orchestration
- L06: Workflow Implementation - Activities and Patterns
- L07: Workflow Patterns - Chaining, Fan-Out, Saga
- L08: Capstone - Stateful Task Agent with Workflows
- L09: Finalize Your Dapr Skill

## Response snapshot

Created comprehensive chapter specification with:
- 10 lessons following Skill-First pattern (L00-L09)
- 4 learner journeys (actors, workflows, patterns, skill extension)
- 30 functional requirements mapped to lessons
- 6 measurable success criteria
- Layer progression: L1 (conceptual) → L2 (implementation) → L3 (skill) → L4 (capstone)
- Assumed Knowledge section distinguishing Ch53 prerequisites from new content
- Running example: TaskActor + TaskProcessingWorkflow extending Task API

## Outcome

- ✅ Impact: Complete chapter specification ready for planning
- 🧪 Tests: N/A (specification phase)
- 📁 Files: spec.md, checklists/requirements.md
- 🔁 Next prompts: /sp.clarify, /sp.plan
- 🧠 Reflection: Specification includes all educational content requirements - Assumed Knowledge, proficiency level, layer progression, Skill-First pattern

## Evaluation notes (flywheel)

- Failure modes observed: None - specification complete on first pass
- Graders run and results (PASS/FAIL): All checklist items PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
