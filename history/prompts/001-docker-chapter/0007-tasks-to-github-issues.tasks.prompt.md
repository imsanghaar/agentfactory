---
id: "0007"
title: "tasks-to-github-issues"
stage: tasks
date: 2025-12-22
surface: claude-code
model: claude-opus-4-5-20251101
feature: 001-docker-chapter
branch: 001-docker-chapter
user: mjs
command: /sp.taskstoissues
labels: [github-issues, project-management, task-tracking]
links:
  spec: specs/001-docker-chapter/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-docker-chapter/tasks.md
tests:
  - null
---

## Prompt

/sp.taskstoissues

Also: Update tasks to include Docker Deep Dive book and official Docker docs as study requirements.

## Response snapshot

Created 14 GitHub issues for Chapter 49 Docker implementation, one per phase.

**Issues Created**:

| Issue | Phase | Title |
|-------|-------|-------|
| #356 | 0 | Study & Context Gathering |
| #357 | 1 | Setup - Chapter Infrastructure |
| #358 | 2 | Foundational - Shared Assets |
| #359 | 3 | Lesson 1 - Docker Installation & Setup |
| #360 | 4 | Lesson 2 - Container Fundamentals |
| #361 | 5 | Lesson 3 - Writing Your First Dockerfile |
| #362 | 6 | Lesson 4 - Container Lifecycle & Debugging |
| #363 | 7 | Lesson 5 - Multi-Stage Builds & Optimization |
| #364 | 8 | Lesson 6 - Docker Compose for Development |
| #365 | 9 | Lesson 7 - Security & Best Practices |
| #366 | 10 | Lesson 8 - AI-Assisted Docker with Gordon |
| #367 | 11 | Lesson 9 - Capstone: Production-Ready Agent |
| #368 | 12 | Lesson 10 - Building the Production Dockerfile Skill |
| #369 | 13 | Polish & Cross-Cutting Concerns |

**Tasks.md Updates**:
1. Added GitHub Issues table at top with all 14 issues
2. Added issue references to each phase header
3. Added `Close Issue` command for each phase
4. Added domain study requirements:
   - Docker Deep Dive book (`cloud-books/docker_deep_dive.md`)
   - Official Docker docs (Get Started, DHI, Scout, Compose)

**Closing Issues**:
When a phase is complete, run:
```bash
gh issue close <issue-number> --repo panaversity/ai-native-software-development
```

Or include `Closes #<issue-number>` in commit messages for auto-close.

## Outcome

- ✅ Impact: 14 GitHub issues created for project tracking; tasks.md updated with issue references and close commands
- 🧪 Tests: N/A (project management)
- 📁 Files: tasks.md (updated with issue table and references)
- 🔁 Next prompts: /sp.implement to begin content writing, or assign issues to team members
- 🧠 Reflection: Grouped 147 tasks into 14 phase-based issues for manageable tracking. Individual task granularity maintained in tasks.md while issues provide milestone visibility.

## Evaluation notes (flywheel)

- Failure modes observed: Initial attempt to add labels failed (labels don't exist in repo); proceeded without labels
- Graders run and results (PASS/FAIL): All 14 issues created successfully (verified via gh CLI)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Consider creating labels (content, chapter-49) in repo for better issue filtering
