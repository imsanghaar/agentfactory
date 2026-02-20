### Core Concept
Relationships define how rows connect across tables. Correct joins and loading strategy prevent believable but wrong analytics — and the N+1 trap silently tanks performance.

### Continuity Bridge
From single-table CRUD (L3) to multi-table queries where related data lives in separate tables connected by foreign keys.

### Key Mental Models
- `relationship()` + `back_populates` = bidirectional navigation between parent and child.
- Explicit joins for cross-table filtering and aggregation.
- N+1 detection: 1 parent query + N child queries = silent performance disaster.
- Section A (relationships) before Section B (joins + loading) — scaffolded progression.

### Critical Patterns
- Bidirectional `back_populates` on both sides of the relationship.
- Selective `cascade="all, delete-orphan"` only where business logic requires it.
- `selectinload()` to batch-load children in one query instead of N lazy loads.
- Blog system (Author → Post → Comment) as alternative domain for the same pattern.

### Common Mistake
Looping parent rows and lazily loading children without recognizing N+1 behavior. With 5 users it's invisible; with 500 it's 501 queries instead of 2.
