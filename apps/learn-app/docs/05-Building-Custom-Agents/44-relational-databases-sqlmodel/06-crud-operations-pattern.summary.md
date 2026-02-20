### Core Concept
Async CRUD follows the pattern: add -> flush (get ID) -> commit -> refresh, with proper `await` on all session operations and soft delete for data preservation.

### Key Mental Models
- flush vs commit: flush writes to DB for ID, commit makes permanent
- session.get() for ID lookup, select() for filtered queries
- Soft delete preserves data: Set `deleted_at` instead of hard delete
- Always update `updated_at` timestamp on modifications

### Critical Patterns
- Create: `add(obj) -> await flush() -> await commit() -> await refresh(obj)`
- Read by ID: `await session.get(Task, task_id)`
- Read with filters: `await session.exec(select(Task).where(Task.status == status))`
- Update: Modify fields, `session.add(task)`, `await commit()`
- Soft delete: `task.deleted_at = datetime.utcnow()`, filter `deleted_at.is_(None)` in queries
- Bulk update: Use `update(Task).where(...).values(...)` without fetching

### AI Collaboration Keys
- Implement text search with `ilike()` for case-insensitive partial matching
- Design bulk operations that don't fetch individual records
- Debug empty results by checking for missing `await`

### Common Mistakes
- Missing `await` on `session.exec()` (MissingGreenlet or empty results)
- Forgetting to update `updated_at` on modifications
- Hard deleting when soft delete is needed for audit trails
- N+1 queries in list comprehensions accessing relationships

### Connections
- **Builds on**: L05 - Async session management
- **Leads to**: L07 - Testing database code
