---
sidebar_position: 5
title: "Async Session Management"
description: "Master AsyncSession lifecycle and FastAPI dependency injection"
keywords: [asyncsession, sqlmodel, fastapi, dependency, async]
chapter: 44
lesson: 5
duration_minutes: 25

skills:
  - name: "AsyncSession Usage"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Technical Literacy"
    measurable_at_this_level: "Student correctly imports and uses AsyncSession from sqlmodel.ext.asyncio.session"

  - name: "FastAPI Dependency Pattern"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Technical Literacy"
    measurable_at_this_level: "Student implements get_session as async generator dependency"

  - name: "Session Lifecycle Understanding"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Technical Literacy"
    measurable_at_this_level: "Student explains session create-use-close lifecycle"

learning_objectives:
  - objective: "Import and configure AsyncSession from correct module"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Uses sqlmodel.ext.asyncio.session.AsyncSession correctly"

  - objective: "Implement session dependency for FastAPI endpoints"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Endpoint receives session via Depends(get_session)"

  - objective: "Prevent MissingGreenlet errors in async code"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Avoids lazy loading patterns that trigger errors"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (AsyncSession, dependency, lifecycle, MissingGreenlet, expire_on_commit) within B1 capacity"

differentiation:
  extension_for_advanced: "Implement session factory with configurable expire_on_commit for different use cases"
  remedial_for_struggling: "Focus on basic get_session pattern, defer MissingGreenlet prevention to later"
---

# Async Session Management

The engine connects to the database. Sessions manage individual operations—queries, inserts, updates, deletes. Each request to your FastAPI app gets its own session.

Getting sessions right prevents subtle bugs that crash your agent.

## The Correct Import

SQLModel provides an async session wrapper. The import path matters:

```python
# CORRECT - SQLModel's async session
from sqlmodel.ext.asyncio.session import AsyncSession

# WRONG - SQLAlchemy's directly (works but loses SQLModel features)
from sqlalchemy.ext.asyncio import AsyncSession
```

**Why it matters:** SQLModel's `AsyncSession` extends SQLAlchemy's with `exec()` method that works with `select()` statements properly.

## Session as FastAPI Dependency

Create a dependency that yields sessions:

```python
from sqlmodel.ext.asyncio.session import AsyncSession
from collections.abc import AsyncGenerator

async def get_session() -> AsyncGenerator[AsyncSession]:
    """Dependency that yields async database sessions."""
    async with AsyncSession(engine) as session:
        yield session
```

**The pattern explained:**

1. `async with AsyncSession(engine)` creates a session
2. `yield session` provides it to the endpoint
3. After endpoint completes, `async with` closes the session

Use in endpoints:

```python
from fastapi import Depends

@router.get("/tasks/{task_id}")
async def get_task(
    task_id: int,
    session: AsyncSession = Depends(get_session),
):
    task = await session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
```

**Output:**
```json
{
  "id": 42,
  "title": "Fix authentication",
  "status": "pending"
}
```

## Session Lifecycle

Each session has a clear lifecycle:

```
Create → Use → Commit/Rollback → Close
   ↑                              ↓
   └──── Managed by async with ───┘
```

**Within a session:**

```python
async with AsyncSession(engine) as session:
    # 1. Create - session starts
    task = Task(title="New task")
    session.add(task)

    # 2. Use - operations queued
    await session.flush()  # Writes to DB, gets ID

    # 3. Commit - makes permanent
    await session.commit()

    # 4. Close - handled by async with
```

**After `async with` exits:**
- Session is closed
- Connection returns to pool
- Any uncommitted changes are rolled back

## The MissingGreenlet Error

This error crashes agents that access relationships incorrectly:

```python
# This CRASHES in async code
task = await session.get(Task, task_id)
print(task.assignee.name)  # MissingGreenlet!
```

**Why it happens:** `task.assignee` triggers a "lazy load"—a database query. But in async code, lazy loads need special handling that isn't automatic.

**Solutions:**

### Solution 1: Eager Loading (Recommended)

Load relationships upfront:

```python
from sqlalchemy.orm import selectinload

stmt = (
    select(Task)
    .options(selectinload(Task.assignee))
    .where(Task.id == task_id)
)
result = await session.exec(stmt)
task = result.one()
print(task.assignee.name)  # Works! Already loaded
```

### Solution 2: Explicit Query

Fetch related data separately:

```python
task = await session.get(Task, task_id)
assignee = await session.get(Worker, task.assignee_id)
print(assignee.name)  # Works! Explicit query
```

### Solution 3: AsyncAttrs (Advanced)

Use SQLAlchemy's AsyncAttrs mixin:

```python
from sqlalchemy.ext.asyncio import AsyncAttrs

class Task(AsyncAttrs, SQLModel, table=True):
    assignee: "Worker" = Relationship(back_populates="tasks")

# Usage
task = await session.get(Task, task_id)
assignee = await task.awaitable_attrs.assignee  # Awaitable lazy load
print(assignee.name)
```

## expire_on_commit=False

By default, SQLAlchemy expires (invalidates) object attributes after commit. This triggers lazy loads when you access them:

```python
# Default behavior (expire_on_commit=True)
session.add(task)
await session.commit()
print(task.title)  # Triggers lazy load → MissingGreenlet!
```

**Solution:** Disable expiration:

```python
from sqlalchemy.ext.asyncio import async_sessionmaker

async_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session:
        yield session
```

**Or:** Always refresh after commit:

```python
session.add(task)
await session.commit()
await session.refresh(task)  # Reloads from DB
print(task.title)  # Works!
```

## Complete Session Configuration

Production-ready session setup. Create `database.py`:

```python
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from collections.abc import AsyncGenerator

engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
)

# Session factory with expire_on_commit=False
async_session_factory = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_session() -> AsyncGenerator[AsyncSession]:
    """Dependency that yields async database sessions."""
    async with async_session_factory() as session:
        yield session
```

**Output (using in endpoint):**
```python
@router.post("/tasks")
async def create_task(
    data: TaskCreate,
    session: AsyncSession = Depends(get_session),
):
    task = Task(**data.model_dump())
    session.add(task)
    await session.commit()
    # No refresh needed - expire_on_commit=False
    return task
```

## Try With AI

### Prompt 1: Debug MissingGreenlet

```
I'm getting this error in my FastAPI endpoint:
"sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called"

The error happens on this line:
    return task.project.name

My endpoint code:
async def get_task(task_id: int, session: AsyncSession = Depends(get_session)):
    task = await session.get(Task, task_id)
    return {"title": task.title, "project": task.project.name}

What's wrong and how do I fix it?
```

**What you're learning:** MissingGreenlet debugging—recognizing and fixing async relationship access issues.

### Prompt 2: Session Factory Configuration

```
I want to configure my AsyncSession to:
1. Not expire attributes after commit
2. Use a specific pool size
3. Log all SQL statements in development

Show me the complete database.py with async_sessionmaker
and get_session dependency.
```

**What you're learning:** Session factory—centralizing session configuration for consistency.

### Prompt 3: Request Scoping

```
Explain why each FastAPI request should get its own database session.
What problems occur if I share a session across requests?
Include code examples showing the wrong and right approach.
```

**What you're learning:** Request scoping—understanding isolation requirements for concurrent access.

### Safety Note

Never share a session across async tasks. Each `asyncio.gather()` coroutine needs its own session. Sharing causes race conditions and data corruption.

---

## Reflect on Your Skill

You built a `relational-db-agent` skill in Lesson 0. Test its session management knowledge.

### Test Your Skill

```
Using my relational-db-agent skill, generate:
1. A get_session() dependency with expire_on_commit=False
2. An endpoint that creates a Task and returns it immediately
3. Proper error handling if creation fails
```

### Identify Gaps

Ask yourself:
- Did my skill use `sqlmodel.ext.asyncio.session.AsyncSession`?
- Did it configure `expire_on_commit=False`?
- Did it structure the dependency with `async with` and `yield`?
- Did it include proper imports?

### Improve Your Skill

If you found gaps:

```
My relational-db-agent skill uses wrong AsyncSession import.
Update it to always use:
from sqlmodel.ext.asyncio.session import AsyncSession

And when creating session factory, use:
from sqlalchemy.ext.asyncio import async_sessionmaker

async_session_factory = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
```

Your skill now generates correct async session patterns.
