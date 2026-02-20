---
id: 0003
title: chapter-58-task-generation
stage: tasks
date: 2025-12-30
surface: cli
model: claude-opus-4-5-20250514
feature: 001-chapter-58-security
branch: 001-chapter-58-security
user: mjs
command: /sp.tasks
labels: [chapter-58, tasks, security, kubernetes, lessons]
links:
  spec: specs/001-chapter-58-security/spec.md
  ticket:
  adr:
  pr:
files:
  - specs/001-chapter-58-security/tasks.md
tests:
  - task format validation passed
---

## Prompt

Generate tasks from plan: specs/001-chapter-58-security/plan.md

FOR EACH LESSON (L00-L09), CREATE TASK WITH:
- Task ID: T58.L[X] format
- Description: "Create lesson X: [Title]"
- Output path: apps/learn-app/docs/07-AI-Cloud-Native-Development/58-production-security/[lesson-slug].md
- Dependencies: List prior lessons if any
- Acceptance criteria from plan
- Estimated duration from plan

ADDITIONAL TASKS:
- T58.R: Create chapter README
- T58.V: Validate all lessons
- T58.C: Create capstone security checklist asset

OUTPUT: specs/001-chapter-58-security/tasks.md

Execute autonomously. DO NOT ask "Should I proceed?"

## Response snapshot

Generated comprehensive tasks.md with 14 tasks organized into 5 phases:

**Phase 1: Setup**
- T58.R: Create chapter README

**Phase 2: P1 User Stories (Core Security)**
- T58.L00: Build Your Cloud Security Skill (Layer 3, 15 min)
- T58.L01: Cloud Native Security Model (Layer 1, 25 min)
- T58.L02: RBAC Deep Dive (Layer 1, 30 min)
- T58.L03: NetworkPolicies (Layer 1, 30 min)

**Phase 3: P2 User Stories (Container & Runtime)**
- T58.L04: Secrets Management (Layer 1, 25 min)
- T58.L05: Pod Security Standards (Layer 1, 25 min)
- T58.L06: Image Scanning & Supply Chain (Layer 1, 25 min)
- T58.L07: Dapr Security (Layer 2 with Three Roles, 25 min)

**Phase 4: P3 + Capstone**
- T58.L08: Compliance Fundamentals (Layer 1, 20 min)
- T58.L09: Capstone - Secure Task API (Layer 4, 40 min)

**Phase 5: Validation & Assets**
- T58.C: Security checklist asset
- T58.V: Validate all lessons
- T58.A: Chapter assessment

All tasks include SUBAGENT blocks for content-implementer, VALIDATION blocks for educational-validator, and SKILLS blocks with required skill invocations.

## Outcome

- ✅ Impact: Task list ready for implementation, all 10 lessons mapped to user stories
- 🧪 Tests: Task format validation passed (all tasks have ID, story, subagent blocks)
- 📁 Files: specs/001-chapter-58-security/tasks.md created (14 tasks, 5 phases)
- 🔁 Next prompts: /sp.analyze, then /sp.taskstoissues or direct implementation
- 🧠 Reflection: Organized by user story priority enables MVP-first delivery (P1 stories = core security foundation)

## Evaluation notes (flywheel)

- Failure modes observed: None - plan.md provided comprehensive lesson details
- Graders run and results (PASS/FAIL): Task format PASS, skill blocks PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
