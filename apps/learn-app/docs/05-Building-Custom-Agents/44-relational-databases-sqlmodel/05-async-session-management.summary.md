### Core Concept
Use `AsyncSession` from `sqlmodel.ext.asyncio.session` (not SQLAlchemy directly), configure `expire_on_commit=False`, and implement as FastAPI dependency with `async with` and `yield`.

### Key Mental Models
- Session lifecycle: Create -> Use -> Commit/Rollback -> Close (managed by async with)
- MissingGreenlet = async relationship access problem: Lazy loads need await
- expire_on_commit=False prevents object expiration after commit
- Each request gets its own session: Never share across async tasks

### Critical Patterns
- Correct import: `from sqlmodel.ext.asyncio.session import AsyncSession`
- Session factory: `async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)`
- FastAPI dependency: `async with async_session_factory() as session: yield session`
- Eager loading prevents MissingGreenlet: `selectinload(Task.assignee)`
- Refresh after commit if not using expire_on_commit=False: `await session.refresh(task)`

### AI Collaboration Keys
- Debug MissingGreenlet by identifying lazy-loaded relationship access
- Configure session factory with proper expire_on_commit setting
- Understand request scoping for concurrent access isolation

### Common Mistakes
- Wrong import: `from sqlalchemy.ext.asyncio import AsyncSession` loses SQLModel features
- Accessing relationships without eager loading (MissingGreenlet)
- Missing `await` on session operations
- Sharing session across `asyncio.gather()` coroutines (race conditions)

### Connections
- **Builds on**: L04 - Implementing data models
- **Leads to**: L06 - CRUD operations pattern
