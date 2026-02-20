---
id: 0005
title: Plan Iteration - R4 and SC-002 Test Coverage
stage: plan
date: 2025-12-04
surface: agent
model: claude-opus-4-5-20251101
feature: 039-panaversity-fs-hardening
branch: 039-panaversity-fs-hardening
user: mjs
command: user-feedback
labels: ["panaversity-fs", "plan-iteration", "testing", "invariants"]
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

User feedback on plan.md test coverage:

1. **High**: Property-based test coverage lists R1, R2, R3, R5, R6, R7 but never mentions R4. Plan claims "All requirements (R1-R7) are testable" but R4 verification is missing.

2. **Medium**: Success criteria include SC-002 ("Zero orphaned storage writes") but Performance Test table only exercises SC-001 and SC-006. No defined test for SC-002.

Open Questions:
- What is intended definition of R4 and where should its verification live?
- How to validate SC-002—fault-injection integration test?

## Response snapshot

Resolved both coverage gaps:

### R4 (Archive Throughput Bound)
**Clarification**: R4 is a **performance invariant**, not a logical property. Cannot be verified symbolically—only empirically.

**Resolution**: Added note to Property-Based Tests section:
> "Note on R4 (Archive Throughput Bound): R4 is a **performance invariant**, not a logical property. It cannot be verified symbolically—only empirically. R4 is covered by `tests/performance/test_archive_throughput.py` (see Performance Tests section), not property-based testing."

Updated Performance Tests table to show SC-001 / R4 together.

### SC-002 (Zero Orphaned Writes)
**Resolution**: Added new **Fault-Injection Tests** section with explicit strategies:

| Success Criteria | Test File | Strategy |
|-----------------|-----------|----------|
| SC-002 | `test_journal_storage_atomic.py` | Inject storage failure mid-write, verify journal rolls back, no orphan in storage |
| SC-002 | `test_journal_storage_atomic.py` | Inject DB failure after storage write, verify storage write rolls back |
| SC-003 | `test_conflict_detection.py` | Concurrent writes with stale hash, verify exactly one succeeds, one gets CONFLICT |

Also added `test_conflict_detection.py` to project structure and integration test table.

## Outcome

- ✅ Impact: All invariants (R1-R7) and success criteria (SC-001, SC-002, SC-003, SC-006) now have explicit test coverage
- 🧪 Tests: Fault-injection tests added for SC-002
- 📁 Files: specs/039-panaversity-fs-hardening/plan.md (updated 3 sections)
- 🔁 Next prompts: /sp.tasks to generate task breakdown
- 🧠 Reflection: Performance invariants (R4) require different verification approach than logical invariants (R1-R3, R5-R7)

## Evaluation notes (flywheel)

- Failure modes observed: Over-promised "all invariants testable via property-based tests" when R4 is performance-only
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): Direct user feedback iteration
- Next experiment (smallest change to try): Classify invariants by type (logical vs performance) during spec phase to set correct verification expectations
