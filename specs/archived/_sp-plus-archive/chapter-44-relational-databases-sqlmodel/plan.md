# Implementation Plan: Chapter 44 - Relational Databases for Agents with SQLModel

## Pedagogical Arc

```
Foundation → Practice → Integration → Mastery
    L00-L01      L02-L05     L06-L07      L08-L09
```

## Lesson Implementation Details

### L00: Build Your Database Skill
**File**: `00-build-your-database-skill.md`
**Layer**: L3 (Skill Creation)
**Proficiency**: B1
**Duration**: 25 min
**Cognitive Load**: 4 concepts (skill-first pattern, LEARNING-SPEC, docs fetching, skill creation)

**Key Activities**:
1. Clone skills-lab fresh: `git clone https://github.com/panaversity/claude-code-skills-lab.git`
2. Create LEARNING-SPEC.md defining what the skill should know
3. Use `/fetching-library-docs sqlmodel --topic "async"` for official patterns
4. Create `relational-db-agent` skill with `/skill-creator`
5. Test: Generate a basic model and verify syntax

**"Reflect on Your Skill"**: Initial skill test - can it generate a valid SQLModel class?

---

### L01: Why Agents Need Structured Data
**File**: `01-why-agents-need-structured-data.md`
**Layer**: L1 (Conceptual)
**Proficiency**: A2
**Duration**: 15 min
**Cognitive Load**: 3 concepts (persistence need, structured vs unstructured, ACID)

**Key Activities**:
1. Narrative: Agent loses all work on restart - the problem
2. Compare: Vector DB (semantic search) vs Relational DB (structured queries)
3. Explain ACID properties for agent reliability
4. Why async matters for non-blocking agent backends

**"Reflect on Your Skill"**: Does skill understand when to use relational vs vector DB?

---

### L02: SQLModel + Async Engine Setup
**File**: `02-sqlmodel-async-engine-setup.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Duration**: 25 min
**Cognitive Load**: 5 concepts (async engine, pooling, URL conversion, SQLite testing, table creation)

**Key Activities**:
1. Install stack: `pip install sqlmodel sqlalchemy[asyncio] asyncpg alembic`
2. Create async engine with proper pooling
3. Convert sync URL to async format
4. Test with SQLite async

**Code Examples**:
```python
from sqlalchemy.ext.asyncio import create_async_engine
engine = create_async_engine(
    "postgresql+asyncpg://user:pass@localhost/db",
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
)
```

**"Reflect on Your Skill"**: Can skill generate engine setup with correct pooling params?

---

### L03: Designing Agent Data Models
**File**: `03-designing-agent-data-models.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Duration**: 30 min
**Cognitive Load**: 6 concepts (table=True, Field types, JSONB, primary keys, indexes, timestamps)

**Key Activities**:
1. Create Task model with basic fields
2. Add JSONB column for tags list
3. Configure indexes for foreign keys
4. Implement timestamp pattern

**Code Examples**:
```python
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(max_length=500)
    tags: list[str] = Field(
        default_factory=list,
        sa_column=Column(JSONB, nullable=False, server_default="[]"),
    )
    created_at: datetime = Field(default_factory=datetime.utcnow)
```

**"Reflect on Your Skill"**: Can skill generate model with JSONB column correctly?

---

### L04: Async Session Management
**File**: `04-async-session-management.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Duration**: 25 min
**Cognitive Load**: 5 concepts (AsyncSession, dependency, lifecycle, MissingGreenlet, expire_on_commit)

**Key Activities**:
1. Create AsyncSession from `sqlmodel.ext.asyncio.session`
2. Implement `get_session()` FastAPI dependency
3. Understand session lifecycle
4. Prevent MissingGreenlet errors

**Code Examples**:
```python
from sqlmodel.ext.asyncio.session import AsyncSession
from collections.abc import AsyncGenerator

async def get_session() -> AsyncGenerator[AsyncSession]:
    async with AsyncSession(engine) as session:
        yield session
```

**"Reflect on Your Skill"**: Does skill understand async session lifecycle and MissingGreenlet prevention?

---

### L05: CRUD Operations Pattern
**File**: `05-crud-operations-pattern.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Duration**: 30 min
**Cognitive Load**: 6 concepts (add, flush, get, exec/select, commit, refresh)

**Key Activities**:
1. Create: `session.add()` + `await session.flush()` + `await session.commit()`
2. Read: `await session.get()` and `await session.exec(select(...))`
3. Update: Modify model + `await session.commit()` + `await session.refresh()`
4. Delete: `await session.delete()` + `await session.commit()`

**Code Examples**:
```python
# Create
session.add(task)
await session.flush()  # Get ID before commit
await session.commit()
await session.refresh(task)

# Read
task = await session.get(Task, task_id)
tasks = (await session.exec(select(Task).where(...))).all()
```

**"Reflect on Your Skill"**: Can skill generate proper CRUD with flush/commit distinction?

---

### L06: Relationships and Eager Loading
**File**: `06-relationships-and-eager-loading.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Duration**: 35 min
**Cognitive Load**: 7 concepts (one-to-many, many-to-one, self-referential, N+1, selectinload, unique, sa_relationship_kwargs)

**Key Activities**:
1. Define one-to-many (Project → Tasks)
2. Define many-to-one with multiple FKs (Task → Worker for assignee and creator)
3. Define self-referential (Task → parent/subtasks)
4. Demonstrate N+1 problem
5. Fix with `selectinload()`

**Code Examples**:
```python
from sqlalchemy.orm import selectinload

stmt = (
    select(Task)
    .options(selectinload(Task.assignee), selectinload(Task.subtasks))
    .where(Task.project_id == project_id)
)
result = await session.exec(stmt)
tasks = result.unique().all()  # unique() required!
```

**"Reflect on Your Skill"**: Does skill include selectinload and unique() pattern?

---

### L07: Transactions and Error Handling
**File**: `07-transactions-and-error-handling.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Duration**: 25 min
**Cognitive Load**: 5 concepts (flush vs commit, multi-op transaction, rollback, context manager, IntegrityError)

**Key Activities**:
1. Understand flush() vs commit()
2. Multiple operations in single transaction
3. Implement rollback on error
4. Use `async with session.begin()` pattern
5. Handle IntegrityError

**Code Examples**:
```python
try:
    session.add(task)
    await session.flush()  # Get task.id
    audit = AuditLog(entity_id=task.id, action="created")
    session.add(audit)
    await session.commit()  # Single commit for both
except IntegrityError:
    await session.rollback()
    raise HTTPException(400, "Constraint violation")
```

**"Reflect on Your Skill"**: Can skill generate proper transaction patterns with rollback?

---

### L08: Migrations with Alembic
**File**: `08-migrations-with-alembic.md`
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**Duration**: 30 min
**Cognitive Load**: 6 concepts (init async, env.py config, model import, autogenerate, upgrade, data migration)

**Key Activities**:
1. Initialize Alembic with async template
2. Configure env.py for async
3. Import all models in env.py
4. Autogenerate migration
5. Run migrations
6. Write data migration

**Code Examples**:
```bash
alembic init -t async alembic
alembic revision --autogenerate -m "Add tasks table"
alembic upgrade head
```

**"Reflect on Your Skill"**: Does skill know Alembic async setup and model import requirement?

---

### L09: Capstone - Complete Task API Database Layer
**File**: `09-capstone-complete-database-layer.md`
**Layer**: L4 (Orchestration)
**Proficiency**: B1
**Duration**: 45 min
**Cognitive Load**: Integration of all prior concepts

**Key Activities**:
1. Create `database.py` with async engine configuration
2. Create models: Task, Project, Worker with all relationships
3. Implement CRUD service layer with eager loading
4. Add transaction handling for complex operations
5. Set up Alembic migrations
6. Verify with provided tests

**Reference Implementation**: Study `/Users/mjs/Documents/code/mjunaidca/taskforce_agent1/apps/api/src/taskflow_api/`

**Final "Reflect on Your Skill"**: Student skill should now match expertise skill capability

---

## Dependencies

```
L00 (skill creation) → Independent
L01 (conceptual) → Independent
L02 (engine) → L01
L03 (models) → L02
L04 (sessions) → L02
L05 (CRUD) → L03, L04
L06 (relationships) → L03, L05
L07 (transactions) → L05
L08 (migrations) → L03
L09 (capstone) → All
```

## Quality Gates

### Per Lesson
- Full YAML frontmatter with skills, learning_objectives, cognitive_load
- 3 "Try With AI" prompts with "What you're learning" explanations
- Evidence blocks for all code examples
- "Reflect on Your Skill" section at end
- No sections after "Try With AI" (no Summary, no What's Next)

### Chapter
- README.md with chapter overview
- Chapter quiz (15 questions)
- All validators pass before commit

## Output Paths

```
apps/learn-app/docs/06-AI-Native-Software-Development/44-relational-databases-sqlmodel/
├── 00-build-your-database-skill.md
├── 01-why-agents-need-structured-data.md
├── 02-sqlmodel-async-engine-setup.md
├── 03-designing-agent-data-models.md
├── 04-async-session-management.md
├── 05-crud-operations-pattern.md
├── 06-relationships-and-eager-loading.md
├── 07-transactions-and-error-handling.md
├── 08-migrations-with-alembic.md
├── 09-capstone-complete-database-layer.md
├── 10-chapter-quiz.md
└── README.md
```
