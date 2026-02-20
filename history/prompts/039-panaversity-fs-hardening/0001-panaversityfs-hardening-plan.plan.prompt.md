---
id: 0001
title: PanaversityFS Hardening Implementation Plan
stage: plan
date: 2025-12-04
surface: agent
model: claude-opus-4-5-20251101
feature: 039-panaversity-fs-hardening
branch: 039-panaversity-fs-hardening
user: mjs
command: /sp.plan
labels: ["panaversity-fs", "storage", "postgresql", "streaming", "overlays"]
links:
  spec: specs/039-panaversity-fs-hardening/spec.md
  ticket: null
  adr: history/adr/0018-panaversityfs-docusaurus-aligned-structure.md
  pr: null
files:
 - specs/039-panaversity-fs-hardening/plan.md
tests:
 - none (planning phase)
---

## Prompt

Generate implementation plan for 039-panaversity-fs-hardening via /sp.plan command. Specification includes 31 functional requirements, 7 Alloy-style invariants, and 6 user stories covering:
- PostgreSQL metadata journal (asyncpg/aiosqlite)
- Streaming archives with 64MB memory bounds
- Personalization overlays via user namespaces
- Hash-based conflict detection with expected_hash
- Append-only audit with hash chain integrity
- Delta build API for incremental Docusaurus builds

User feedback incorporated:
1. FR-003/004/005 explicit agent contract documentation
2. Manifest hash computation algorithm documented
3. Shared path validation module specified
4. Instrumentation hooks mapped to success criteria
5. Alloy snippets enhanced with pytest assertions and DB constraints

## Response snapshot

Generated comprehensive 4-phase implementation plan:

**Phase 1 (Foundations)**: Database layer, path validation, Prometheus metrics - parallel execution
**Phase 2 (Core Refactoring)**: Journal integration for write/read/delete, audit hardening - sequential
**Phase 3 (New Features)**: Streaming archives, overlay support, delta build API - parallel after Phase 2
**Phase 4 (Validation)**: Integration tests, performance benchmarks, property-based invariant verification

Key technical decisions:
- SQLAlchemy 2.0 async with asyncpg (prod) / aiosqlite (dev)
- Alembic migrations with auto-upgrade on startup
- prometheus-client for instrumentation
- hypothesis for property-based testing (R1-R7 invariants)

Component architecture organized in 4 dependency layers with clear file paths for all modifications.

## Outcome

- ✅ Impact: Complete implementation plan with 4 phases, 11 tasks, 15-19 day timeline, and dependency ordering
- 🧪 Tests: Test strategy defined for unit (80%+), integration, property-based (R1-R7), and performance (SC-001, SC-006)
- 📁 Files: specs/039-panaversity-fs-hardening/plan.md (884 lines)
- 🔁 Next prompts: /sp.tasks to generate actionable task breakdown
- 🧠 Reflection: Routing to general-purpose agent (not chapter-planner) correct for engineering work

## Evaluation notes (flywheel)

- Failure modes observed: None - clean routing based on work type classification
- Graders run and results (PASS/FAIL): N/A (planning phase)
- Prompt variant (if applicable): Standard /sp.plan with engineering routing
- Next experiment (smallest change to try): Validate plan coverage against all 31 FRs before task generation
