### Core Concept
Transactions guarantee all-or-nothing: multi-step writes either fully commit or fully rollback, preventing partial corruption.

### Continuity Bridge
From single-row CRUD safety (L3) to multi-step write safety where partial completion means data corruption.

### Key Mental Models
- Atomicity: both rows commit or neither does.
- One logical operation requires one session boundary.
- Schema-valid does not always mean business-valid -- input validation still needed.
- Invariant: transfer ledger entries always net to zero.

### Critical Patterns
- Single session wrapping all related writes with try/except/commit/rollback.
- Forced failure drill: intentionally fail step 2, verify zero new rows.
- Never split related operations across separate sessions.

### Common Mistake
Splitting one logical transaction across multiple sessions. Session A commits the debit, Session B fails the credit -- money vanishes.
