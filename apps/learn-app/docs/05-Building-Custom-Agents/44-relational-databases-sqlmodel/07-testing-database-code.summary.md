### Core Concept
Use pytest-asyncio with in-memory SQLite (`sqlite+aiosqlite:///:memory:`) for fast isolated tests, wrapping each test in a transaction that rolls back for perfect isolation.

### Key Mental Models
- In-memory SQLite for speed: No server, per-test isolation
- Transaction rollback for isolation: Each test starts clean
- Fixtures chain dependencies: task fixture depends on project and worker
- Test the service layer, not raw SQL

### Critical Patterns
- Config: `asyncio_mode = "auto"` in pytest.ini
- Engine fixture: Create tables in setup, drop in teardown, dispose engine
- Session fixture: Begin transaction, yield session, rollback on exit
- Data fixtures: `session.add(obj) -> await session.flush()` (no commit)
- Test error cases with `pytest.raises(IntegrityError)`

### AI Collaboration Keys
- Generate test cases covering happy paths, edge cases, and error handling
- Debug async test errors like "Task attached to a different loop"
- Use factory_boy pattern for generating complex test data

### Common Mistakes
- Running tests against production database (always use TESTING env)
- Committing in fixtures instead of flush (pollutes other tests)
- Missing `await conn.rollback()` in session fixture (test pollution)
- Not using `expire_on_commit=False` (DetachedInstanceError)

### Connections
- **Builds on**: L06 - CRUD operations pattern
- **Leads to**: L08 - Relationships and eager loading
