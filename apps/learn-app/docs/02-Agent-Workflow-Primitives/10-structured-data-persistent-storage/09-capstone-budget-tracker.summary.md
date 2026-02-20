### Core Concept
Integrate all chapter primitives (schema, CRUD, transactions, Neon, verification) into one working application with a 5-gate evidence pipeline.

### Continuity Bridge
From individual patterns (L1-L7) to proof that all pieces hold together under one roof.

### Key Mental Models
- Evidence bundle: collection of test results proving the system works.
- Release gate: checkpoint that must pass before shipping.
- "Ready for demo" (happy path) vs "ready for release" (failure evidence + verification gate).
- Five gates: Schema, CRUD, Rollback, Neon, Verification.

### Critical Patterns
- Sequential evidence pipeline: each gate must pass before the next runs.
- No-N+1 monthly summary using GROUP BY + JOIN.
- User-scoped verification comparing SQL totals to raw CSV.
- One JSON evidence bundle artifact capturing all gate results.

### Common Mistake
Publishing reports after a mismatch because "the SQL looks right." Also: claiming production-ready without failure-path proof.
