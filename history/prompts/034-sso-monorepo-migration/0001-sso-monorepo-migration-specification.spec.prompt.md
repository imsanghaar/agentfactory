---
id: "0001"
title: sso-monorepo-migration-specification
stage: spec
date: 2025-12-16
surface: cli
model: claude-opus-4-5-20251101
feature: 034-sso-monorepo-migration
branch: 034-sso-monorepo-migration
user: mjs
command: /sp.specify sso-monorepo-migration
labels: [monorepo, migration, sso, nx, git-subtree]
links:
  spec: specs/034-sso-monorepo-migration/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/034-sso-monorepo-migration/spec.md
  - specs/034-sso-monorepo-migration/checklists/requirements.md
tests:
  - null
---

## Prompt

Migrate SSO repository (https://github.com/panaversity/sso) into this Nx monorepo using git subtree. Delete foundations/ folder, add Nx Next.js plugin, place SSO app in apps/sso/. Leave .claude/.specify/CLAUDE.md for human review.

## Response snapshot

Created specification for SSO monorepo migration with:
- 4 user stories (P1: local dev, P1: CI integration, P2: git history, P3: human review)
- 10 functional requirements covering git subtree, Nx setup, file preservation/deletion
- 8 success criteria with concrete verification commands
- 4 constraints (port 3001, Neon PostgreSQL, Next.js compatibility, scope limits)
- 5 non-goals preventing scope creep
- Comprehensive "Files to Review" table for human review phase

spec-architect validated spec as READY FOR PLANNING with 9/10 score. No critical issues.

## Outcome

- ✅ Impact: Specification ready for planning phase
- 🧪 Tests: N/A (spec phase)
- 📁 Files: spec.md, checklists/requirements.md created
- 🔁 Next prompts: /sp.plan 034-sso-monorepo-migration
- 🧠 Reflection: Spec is comprehensive for infrastructure migration; explicit human review gates important

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): spec-architect validation PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
