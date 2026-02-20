---
id: 0003
title: PanaversityFS Hardening Specification
stage: spec
date: 2025-12-04
surface: agent
model: claude-opus-4-5-20251101
feature: 039-panaversity-fs-hardening
branch: 039-panaversity-fs-hardening
user: mjs
command: /sp.orchestrator
labels: ["panaversity-fs", "storage", "specification", "alloy", "formal-verification"]
links:
  spec: specs/039-panaversity-fs-hardening/spec.md
  ticket: null
  adr: history/adr/0018-panaversityfs-docusaurus-aligned-structure.md
  pr: null
files:
 - specs/039-panaversity-fs-hardening/spec.md
 - specs/039-panaversity-fs-hardening/checklists/requirements.md
tests:
 - none (specification phase)
---

## Prompt

Review PanaversityFS and relevant specs/history, discuss production hardening requirements from POC failures:
- Issue 1: Full book downloads for Docusaurus build mostly failed (502/timeout on 50MB+ books)
- Issue 2: No structure, guidelines, or versioning
- Delete/edit content operations unreliable
- Need personalization support for user-specific books
- Need database/file for path+hash tracking to distinguish update vs add

Requirements must be unambiguous, measurable, and formally verifiable using Alloy-style formal verification (Software Abstractions by Daniel Jackson): invariant identification, small scope testing (3-5 objects), counterexample generation.

User challenged initial SQLite choice, requested PostgreSQL from the start citing production best practices.

## Response snapshot

Created comprehensive specification with:

**6 User Stories** (prioritized P1-P3):
- US1: Docusaurus Build Fetches Complete Book (P1)
- US2: Agent Updates Lesson with Conflict Detection (P1)
- US3: System Administrator Queries Audit Trail (P2)
- US4: Personalized Book for Individual User (P2)
- US5: Book Schema Validation on Write (P2)
- US6: Delta Build Detection (P3)

**31 Functional Requirements** (FR-001 to FR-031) covering:
- Metadata Journal (PostgreSQL/SQLite)
- Schema Enforcement
- Archive Streaming
- Personalization Overlays
- Audit Provenance
- Docusaurus Contract
- Database Configuration

**7 Alloy-Style Invariants** (R1-R7):
- R1: Deterministic Book Schema
- R2: Hash Journal Integrity
- R3: Idempotent Delete
- R4: Archive Throughput Bound
- R5: Overlay Exclusivity
- R6: Audit Hash Chain
- R7: Agent Provenance

**Key Additions from User Feedback**:
- Agent Contract documentation (expected_hash protocol)
- Manifest Hash Computation algorithm
- Shared Path Validation module interface
- Instrumentation Requirements mapped to success criteria

## Outcome

- ✅ Impact: Production-grade specification with formally verifiable requirements covering all POC failures
- 🧪 Tests: Alloy snippets include pytest assertions and small-scope test guidance
- 📁 Files: specs/039-panaversity-fs-hardening/spec.md (615 lines), checklists/requirements.md
- 🔁 Next prompts: /sp.plan to generate implementation plan
- 🧠 Reflection: User feedback on PostgreSQL was correct—researching industry patterns (Cloudflare, Supabase, Vercel) confirmed external metadata DB is standard

## Evaluation notes (flywheel)

- Failure modes observed: Initial assumption of SQLite challenged by user; research validated PostgreSQL choice
- Graders run and results (PASS/FAIL): spec-architect validation: 9.5/10 READY FOR PLANNING
- Prompt variant (if applicable): /sp.orchestrator with Alloy-style formal verification request
- Next experiment (smallest change to try): Include industry pattern research earlier in spec phase
