---
id: 0004
title: Plan Iteration - Fresh Start Deployment
stage: plan
date: 2025-12-04
surface: agent
model: claude-opus-4-5-20251101
feature: 039-panaversity-fs-hardening
branch: 039-panaversity-fs-hardening
user: mjs
command: user-feedback
labels: ["panaversity-fs", "plan-iteration", "migration", "fresh-start"]
links:
  spec: specs/039-panaversity-fs-hardening/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/039-panaversity-fs-hardening/plan.md
tests:
 - none (plan iteration)
---

## Prompt

User feedback on plan.md:

> There are no migrations this was POC we start fresh for -> Migration path from JSONL to Postgres is explicitly staged with dual write + replay, plus rollback flag, which should calm ops nerves.

Issues identified:
1. **High**: plan.md lists "Zero Downtime Migration … (migration from JSONL audit)" under Constraints while Deployment Strategy says "No Migration Required… clean-slate deployment." Contradiction.
2. **Medium**: Plan invests in Alembic migration stack (Task 1.1, alembic.ini, Risk 3) but "fresh start" means no data migration needed.
3. **Medium**: Risk 3 ("Schema Migration Breaks Existing Content") and pre-deployment checklist ("migrations tested on production snapshot") contradict fresh-start scenario.

Open Questions:
- Should Alembic remain for baseline schema management even though we are not migrating existing data?
- Can we remove "Zero Downtime Migration" constraint?

## Response snapshot

Resolved contradictions by updating plan.md:

1. **Constraint updated**: "Zero Downtime Migration" → "Fresh Start Deployment: No legacy data migration required (POC had no production content)"

2. **Risk 3 reframed**: "Schema Migration Breaks Existing Content" (High) → "Future Schema Changes Break Running System" (Medium) with note that initial deployment is fresh start

3. **Pre-deployment checklist updated**: "migrations tested on production snapshot" → "Alembic migration creates schema correctly (`alembic upgrade head` on empty DB)"

4. **Task 1.1 clarified**: Added note "Alembic is for **forward schema management** (future column additions, indexes), not data migration. Initial deployment is fresh start on empty database."

5. **Deployment Strategy rewritten**: Removed dual-write period, JSONL replay, conversion scripts. Now states clean-slate approach with simple rollback via feature flag.

**Decision**: Alembic stays for forward schema management (adding columns/indexes later), but migration complexity removed.

## Outcome

- ✅ Impact: Plan internally consistent—fresh start deployment, no migration tooling
- 🧪 Tests: N/A
- 📁 Files: specs/039-panaversity-fs-hardening/plan.md (updated 4 sections)
- 🔁 Next prompts: Continue plan review
- 🧠 Reflection: Contradictions between Constraints and Deployment Strategy would have caused implementation confusion

## Evaluation notes (flywheel)

- Failure modes observed: Plan had conflicting narratives (migration vs fresh-start) that user caught during review
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): Direct user feedback iteration
- Next experiment (smallest change to try): Add plan consistency check before presenting for approval (verify Constraints align with Deployment Strategy)
