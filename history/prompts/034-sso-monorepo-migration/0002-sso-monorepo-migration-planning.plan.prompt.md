---
id: "0002"
title: sso-monorepo-migration-planning
stage: plan
date: 2025-12-16
surface: cli
model: claude-opus-4-5-20251101
feature: 034-sso-monorepo-migration
branch: 034-sso-monorepo-migration
user: mjs
command: /sp.plan 034-sso-monorepo-migration
labels: [monorepo, migration, sso, nx, git-subtree, planning]
links:
  spec: specs/034-sso-monorepo-migration/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/034-sso-monorepo-migration/plan.md
tests:
  - null
---

## Prompt

Create implementation plan for SSO monorepo migration based on approved spec.

## Response snapshot

Created comprehensive 7-phase implementation plan (1129 lines):

**Phases:**
1. Phase 0: Pre-Migration Verification (verify git state, Nx, baseline)
2. Phase 1: Git Subtree Import (add remote, fetch, subtree add)
3. Phase 2: Post-Import Cleanup (delete foundation/, lockfile)
4. Phase 3: Nx Integration (@nx/next plugin, project.json)
5. Phase 4: Dependency Resolution (pnpm install, merge deps)
6. Phase 5: Verification (SC-001 through SC-008)
7. Phase 7: Final Verification & Completion

**Key Artifacts:**
- Detailed shell commands for each step
- Complete project.json configuration
- ESLint and Jest configuration
- Verification script for all success criteria
- Rollback plan with two options
- Risk mitigation strategies
- MIGRATION.md template for apps/sso/

**Estimated Time:** 2-3 hours

## Outcome

- ✅ Impact: Complete implementation plan ready for task generation
- 🧪 Tests: Verification script included for SC-001 through SC-008
- 📁 Files: plan.md (1129 lines)
- 🔁 Next prompts: /sp.tasks 034-sso-monorepo-migration
- 🧠 Reflection: Infrastructure migration requires detailed command sequences; git subtree complexity well documented

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A (plan phase)
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
