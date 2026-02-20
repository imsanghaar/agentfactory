### Core Concept
Use `flush()` to get auto-assigned IDs within a transaction, single `commit()` for atomicity across multiple operations, and always `rollback()` in exception handlers.

### Key Mental Models
- flush vs commit: flush writes for ID, commit makes permanent
- Atomicity: All operations succeed or all fail together
- Never catch exceptions without rollback: Corrupts subsequent operations
- Context manager pattern: `async with session.begin()` for auto commit/rollback

### Critical Patterns
- Multi-operation: `add(parent) -> flush() -> add(children with parent.id) -> commit()`
- Error handling: `try: commit() except IntegrityError: await rollback(); raise HTTPException`
- Context manager: `async with session.begin(): ...` (don't call commit inside)
- Nested functions share transaction: Inner function adds, outer function commits

### AI Collaboration Keys
- Design atomic bulk updates with single transaction
- Implement retry with exponential backoff for deadlock recovery
- Balance atomicity vs partial success for batch imports

### Common Mistakes
- Calling `commit()` inside `async with session.begin()` block
- Catching exceptions without `await session.rollback()`
- Using flush() when you meant commit() (data not persisted)
- Inner functions calling commit() (breaks outer transaction atomicity)

### Connections
- **Builds on**: L08 - Relationships and eager loading
- **Leads to**: L10 - Migrations with Alembic
