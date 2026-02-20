### Core Concept
CRUD operations follow a predictable session lifecycle: open, add, flush, commit/rollback, close.

### Continuity Bridge
From defining schema (L2) to putting data in and getting it back out reliably.

### Key Mental Models
- session.add() stages in memory; session.commit() makes it permanent.
- session.flush() sends SQL to get IDs without committing -- needed for FK-dependent rows.
- Rollback undoes all pending changes -- the safety net for failed writes.
- .scalars() unwraps result objects to get model instances directly.

### Critical Patterns
- Insert with flush for FK-dependent rows, then commit atomically.
- try/except/rollback for every write that might fail.
- .scalars().all() for lists, .scalars().first() for single results.
- Read in a new session to prove data actually committed.

### Common Mistake
Calling session.add() without commit and wondering why data disappears. Also: reusing session state after an exception without rolling back first.
