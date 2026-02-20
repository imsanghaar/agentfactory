---
id: 0005
title: chapter-59-taskstoissues
stage: tasks
date: 2025-12-30
surface: claude-code
model: claude-opus-4
feature: 001-chapter-59-cost-disaster-recovery
branch: 001-chapter-59-cost-disaster-recovery
user: mjs
command: /sp.taskstoissues
labels: [chapter, tasks, github-issues]
links:
  spec: specs/001-chapter-59-cost-disaster-recovery/spec.md
  ticket:
  adr:
  pr:
files:
  - specs/001-chapter-59-cost-disaster-recovery/tasks.md
tests:
  - N/A (issue creation phase)
---

## Prompt

/sp.taskstoissues

(Automatically invoked after /sp.analyze to create GitHub issues from tasks.md)

## Response snapshot

Created 18 GitHub issues for Chapter 59: Cost & Disaster Recovery tasks.

Issue mapping:
- T001 (#572): Create chapter directory structure
- T002 (#573): Create chapter README.md
- T003 (#574): L00: Build Your Operational Excellence Skill
- T004 (#575): L01: Cloud Cost Fundamentals
- T005 (#576): L02: Right-Sizing with VPA
- T006 (#577): L03: OpenCost/Kubecost Visibility
- T007 (#583): L04: FinOps Practices and Budget Alerts
- T008 (#584): L05: Backup Fundamentals
- T009 (#585): L06: Velero for K8s Backup/Restore
- T010 (#586): L07: Chaos Engineering Basics
- T011 (#587): L08: Data Sovereignty and Compliance
- T012 (#588): L09: Capstone - Resilient, Cost-Aware Task API
- T013 (#589): Run educational-validator on all lessons
- T014 (#590): Run factual-verifier on all lessons
- T015 (#591): Run pedagogical-designer review
- T016 (#592): Create chapter assessment
- T017 (#593): Update README with final lesson list
- T018 (#594): Run canonical-format-checker on skill references

## Outcome

- ✅ Impact: 18 GitHub issues created for tracking chapter implementation
- 🧪 Tests: N/A (issue creation phase)
- 📁 Files: tasks.md (read), 18 GitHub issues created
- 🔁 Next prompts: Phase B.7: Implement all 10 lessons via content-implementer
- 🧠 Reflection: Labels didn't exist in repo, created issues without labels

## Evaluation notes (flywheel)

- Failure modes observed: Initial attempts failed due to non-existent labels; resolved by omitting labels
- Graders run and results (PASS/FAIL): PASS (all 18 issues created)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Pre-check label existence before issue creation
