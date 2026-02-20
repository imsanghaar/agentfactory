# Chapter 44: Relational Databases for Agents with SQLModel

## Overview

This chapter teaches students to build production-ready async database layers for AI agent backends using SQLModel with PostgreSQL. Students learn async session management, model design with relationships, CRUD operations, N+1 query prevention, transactions, and Alembic migrations.

**Part**: 6 - AI Native Software Development
**Target Proficiency**: B1 (Intermediate)
**Prerequisites**:
- Chapter 40: FastAPI for Agents (basic SQLModel exposure)
- Chapter 43: Vector Databases (complementary - understanding data persistence)

**Running Example**: Task API database layer (deepening the Task API from Ch40)

## Learning Outcomes

By completing this chapter, students will be able to:

1. **Configure async database engines** for PostgreSQL with proper pooling and connection management
2. **Design SQLModel tables** with JSONB columns, foreign keys, and self-referential relationships
3. **Implement async CRUD operations** using AsyncSession with proper commit/flush patterns
4. **Prevent N+1 queries** using selectinload and other eager loading strategies
5. **Manage database transactions** with proper rollback and error handling
6. **Create and run migrations** using Alembic with async support
7. **Build a complete database layer** for the Task API running example

## Technology Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| SQLModel | 0.0.22+ | ORM combining Pydantic + SQLAlchemy |
| SQLAlchemy | 2.0+ | Async database engine |
| asyncpg | 0.29+ | PostgreSQL async driver |
| PostgreSQL | 15+ | Production database |
| Alembic | 1.13+ | Database migrations |
| aiosqlite | 0.20+ | SQLite async (testing) |

## Skill-First Pattern

### Student Skill

Students create their own `relational-db-agent` skill in L00.

### Expertise Skill

This chapter uses `.claude/skills/building-with-sqlmodel-async/SKILL.md` as the expertise source for accurate API patterns.

## Lesson Structure (10 lessons)

### L00: Build Your Database Skill (25 min)
**Layer**: L3 (Skill Creation)
**Proficiency**: B1

Students create their `relational-db-agent` skill:
1. Clone skills-lab fresh
2. Write LEARNING-SPEC.md for database patterns
3. Use `/fetching-library-docs sqlmodel` to get official docs
4. Create skill with `/skill-creator`
5. Test skill generates valid database code

**Ends with**: "Reflect on Your Skill" section

---

### L01: Why Agents Need Structured Data (15 min)
**Layer**: L1 (Conceptual Foundation)
**Proficiency**: A2

Concepts:
- Agents need persistent state (tasks, projects, users)
- Structured data vs unstructured (vector DB complement)
- ACID properties for agent reliability
- Why async matters for agent backends

**Key Question**: "What happens to your agent's work when the server restarts?"

**Ends with**: "Reflect on Your Skill" section

---

### L02: SQLModel + Async Engine Setup (25 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1

Topics:
- Installing the async stack (sqlmodel, asyncpg, alembic)
- Creating async engine with `create_async_engine`
- Connection pooling for production (`pool_pre_ping`, `pool_recycle`)
- Converting sync URLs to async format
- SQLite async for testing

**Code Focus**:
```python
from sqlalchemy.ext.asyncio import create_async_engine
engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_size=5,
)
```

**Ends with**: "Reflect on Your Skill" section

---

### L03: Designing Agent Data Models (30 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1

Topics:
- SQLModel with `table=True`
- Field types and constraints
- JSONB columns for list/dict fields (PostgreSQL)
- Primary keys and indexes
- Timestamps pattern

**Code Focus**:
```python
class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tags: list[str] = Field(
        default_factory=list,
        sa_column=Column(JSONB, nullable=False, server_default="[]"),
    )
```

**Ends with**: "Reflect on Your Skill" section

---

### L04: Async Session Management (25 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1

Topics:
- AsyncSession from `sqlmodel.ext.asyncio.session`
- Session as FastAPI dependency (`get_session`)
- Session lifecycle (create, use, close)
- MissingGreenlet errors and prevention
- `expire_on_commit=False` pattern

**Code Focus**:
```python
async def get_session() -> AsyncGenerator[AsyncSession]:
    async with AsyncSession(engine) as session:
        yield session
```

**Ends with**: "Reflect on Your Skill" section

---

### L05: CRUD Operations Pattern (30 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1

Topics:
- Create with `session.add()` and `await session.flush()`
- Read with `await session.get()` and `await session.exec(select(...))`
- Update by modifying model and `await session.commit()`
- Delete with `await session.delete()`
- The importance of `await session.refresh()`

**Code Focus**: Complete CRUD for Task model

**Ends with**: "Reflect on Your Skill" section

---

### L06: Relationships and Eager Loading (35 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1

Topics:
- One-to-many relationships
- Many-to-one with multiple foreign keys
- Self-referential relationships (parent-child tasks)
- The N+1 problem explained
- `selectinload()` for eager loading
- Why `result.unique().all()` is required

**Code Focus**:
```python
stmt = (
    select(Task)
    .options(selectinload(Task.assignee))
    .where(Task.project_id == project_id)
)
result = await session.exec(stmt)
tasks = result.unique().all()
```

**Ends with**: "Reflect on Your Skill" section

---

### L07: Transactions and Error Handling (25 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1

Topics:
- `flush()` vs `commit()` distinction
- Multiple operations in single transaction
- Rollback on errors
- Context manager pattern (`async with session.begin()`)
- IntegrityError handling

**Code Focus**:
```python
try:
    await session.commit()
except IntegrityError:
    await session.rollback()
    raise HTTPException(400, "Constraint violation")
```

**Ends with**: "Reflect on Your Skill" section

---

### L08: Migrations with Alembic (30 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1

Topics:
- Initializing Alembic with async template
- Configuring env.py for async
- Importing all models before migration
- Autogenerate vs manual migrations
- Running migrations (upgrade, downgrade)
- Data migrations

**Code Focus**:
```bash
alembic init -t async alembic
alembic revision --autogenerate -m "Add tasks table"
alembic upgrade head
```

**Ends with**: "Reflect on Your Skill" section

---

### L09: Capstone - Complete Task API Database Layer (45 min)
**Layer**: L4 (Orchestration)
**Proficiency**: B1

Students implement a complete database layer for Task API:
1. Database configuration with async engine
2. Task, Project, Worker models with relationships
3. CRUD operations with eager loading
4. Transaction handling for multi-step operations
5. Alembic migration setup

**Reference**: `/Users/mjs/Documents/code/mjunaidca/taskforce_agent1/apps/api/src/taskflow_api/`

**Assessment**: Working database layer passing all provided tests

**Ends with**: "Reflect on Your Skill" section + Chapter completion

---

## Content Constraints

### IN SCOPE
- SQLModel with async engine (NOT sync)
- PostgreSQL as production database
- SQLAlchemy 2.0+ async patterns
- asyncpg driver
- Alembic async migrations
- JSONB columns for flexible data
- Self-referential relationships
- FastAPI integration patterns

### OUT OF SCOPE
- Sync SQLAlchemy (async only in this chapter)
- Raw SQL queries (use SQLModel ORM)
- NoSQL databases (covered in Ch43 Vector DBs)
- Database administration (DBA topics)
- Advanced performance tuning
- Replication and sharding

## Images and Diagrams

| Lesson | Diagram | Description |
|--------|---------|-------------|
| L01 | `agent-data-flow.png` | Data flow from agent → API → Database |
| L03 | `model-relationships.png` | Task-Project-Worker ER diagram |
| L06 | `n-plus-one.png` | Visual of N+1 problem and solution |
| L07 | `transaction-flow.png` | Transaction commit/rollback flow |

## Assessment Strategy

### Per-Lesson
- "Reflect on Your Skill" section tests and improves student skill
- Code exercises with expected output

### Chapter Quiz
- 15 questions covering all lessons
- Focus on async patterns, N+1 prevention, transaction handling

### Capstone Assessment
- Working database layer for Task API
- Automated tests verify:
  - Models create correctly
  - CRUD operations work
  - Relationships load properly
  - Migrations run successfully

## Quality References

- **Expertise Skill**: `.claude/skills/building-with-sqlmodel-async/SKILL.md`
- **Reference Implementation**: `/Users/mjs/Documents/code/mjunaidca/taskforce_agent1/apps/api/src/taskflow_api/`
- **Lesson Quality Standard**: `apps/learn-app/docs/01-Introducing-AI-Driven-Development/01-agent-factory-paradigm/01-the-2025-inflection-point.md`

## Validation Requirements

All lessons must pass:
- `educational-validator`: Framework invisibility, evidence presence, structure compliance
- `validation-auditor`: Technical accuracy 30%, pedagogical effectiveness 25%, writing quality 20%
- `factual-verifier`: All statistics and claims verified
- `pedagogical-designer`: Layer progression L1→L2→L3→L4 validated
