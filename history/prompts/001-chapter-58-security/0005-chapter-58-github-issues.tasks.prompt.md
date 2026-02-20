---
id: 0005
title: chapter-58-github-issues
stage: tasks
date: 2025-12-30
surface: cli
model: claude-opus-4-5-20250514
feature: 001-chapter-58-security
branch: 001-chapter-58-security
user: mjs
command: /sp.taskstoissues
labels: [chapter-58, github-issues, tasks]
links:
  spec: specs/001-chapter-58-security/spec.md
  ticket: https://github.com/panaversity/agentfactory/issues/563
  adr:
  pr:
files:
  - specs/001-chapter-58-security/tasks.md
tests:
  - 14 GitHub issues created successfully
---

## Prompt

Convert tasks from specs/001-chapter-58-security/tasks.md into GitHub issues.

Create issues for all 14 tasks:
- Phase 1: T58.R (README)
- Phase 2: T58.L00-L03 (P1 Stories)
- Phase 3: T58.L04-L07 (P2 Stories)
- Phase 4: T58.L08-L09 (P3 + Capstone)
- Phase 5: T58.C, T58.V, T58.A (Validation)

Execute autonomously. DO NOT ask "Should I proceed?"

## Response snapshot

Created 14 GitHub issues in panaversity/agentfactory:

| Task | Issue | Title |
|------|-------|-------|
| T58.R | #563 | Create Chapter 58 README and Directory |
| T58.L00 | #564 | Build Your Cloud Security Skill |
| T58.L01 | #565 | Cloud Native Security Model (4Cs) |
| T58.L02 | #566 | RBAC Deep Dive |
| T58.L03 | #567 | NetworkPolicies |
| T58.L04 | #568 | Secrets Management |
| T58.L05 | #569 | Pod Security Standards |
| T58.L06 | #570 | Image Scanning & Supply Chain |
| T58.L07 | #571 | Dapr Security (Three Roles) |
| T58.L08 | #578 | Compliance Fundamentals |
| T58.L09 | #579 | Capstone - Secure Task API |
| T58.C | #580 | Create Security Checklist Asset |
| T58.V | #581 | Validate All Lessons |
| T58.A | #582 | Run Assessment Architect |

Updated tasks.md with issue links.

## Outcome

- ✅ Impact: 14 GitHub issues created for tracking implementation
- 🧪 Tests: All issues created successfully
- 📁 Files: tasks.md updated with issue links
- 🔁 Next prompts: /sp.implement (start with T58.R)
- 🧠 Reflection: gh CLI worked well for bulk issue creation

## Evaluation notes (flywheel)

- Failure modes observed: Initial label creation failed (label didn't exist), resolved by removing labels
- Graders run and results (PASS/FAIL): Issue creation PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Pre-create labels before issue creation
