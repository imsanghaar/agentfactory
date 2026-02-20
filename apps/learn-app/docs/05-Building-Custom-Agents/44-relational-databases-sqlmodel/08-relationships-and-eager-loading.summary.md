### Core Concept
Define relationships with `Relationship()` and `back_populates`, use `sa_relationship_kwargs` for multi-FK and self-referential cases, and always use `selectinload` with `result.unique().all()` to prevent N+1 queries.

### Key Mental Models
- N+1 problem: 1 query for parents + N queries for each child relationship
- selectinload: Single IN query for all related objects (2 queries total)
- unique() required: selectinload can create duplicate parent objects
- TYPE_CHECKING prevents circular imports for type hints

### Critical Patterns
- Basic relationship: `Relationship(back_populates="tasks")`
- Multi-FK: `sa_relationship_kwargs={"foreign_keys": "[Task.assignee_id]"}`
- Self-referential parent: `sa_relationship_kwargs={"remote_side": "Task.id", "foreign_keys": "[Task.parent_task_id]"}`
- Eager loading: `select(Task).options(selectinload(Task.assignee))`
- Always: `result = await session.exec(stmt); items = result.unique().all()`

### AI Collaboration Keys
- Debug "Could not determine join condition" with sa_relationship_kwargs
- Optimize slow endpoints by identifying N+1 in list comprehensions
- Handle recursive relationships with nested selectinload

### Common Mistakes
- Accessing relationships without selectinload (MissingGreenlet)
- Forgetting `unique().all()` with selectinload (duplicate results)
- Missing `sa_relationship_kwargs` with multiple FKs to same table
- N+1 hidden in list comprehensions: `[t.assignee.handle for t in tasks]`

### Connections
- **Builds on**: L07 - Testing database code
- **Leads to**: L09 - Transactions and error handling
