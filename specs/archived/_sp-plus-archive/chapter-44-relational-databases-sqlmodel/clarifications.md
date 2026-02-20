# Clarifications for Chapter 44

## Resolved Questions

### 1. Technology Versions
- **SQLModel**: 0.0.22+ (latest stable with async support)
- **SQLAlchemy**: 2.0+ (required for modern async patterns)
- **asyncpg**: 0.29+ (PostgreSQL async driver)
- **PostgreSQL**: 15+ (for JSONB and modern features)
- **Alembic**: 1.13+ (async template support)

### 2. Scope Boundaries
**IN**: Async SQLModel, PostgreSQL, CRUD, relationships, N+1 prevention, transactions, Alembic
**OUT**: Sync patterns, raw SQL, NoSQL, DBA topics, replication/sharding

### 3. Prerequisite Assumptions
- Students have completed Ch40 (FastAPI fundamentals, basic SQLModel exposure)
- Students understand Python async/await (Part 5)
- Students have Docker for PostgreSQL container

### 4. Running Example Alignment
- Builds on Task API from Ch40
- Deepens database layer that was briefly introduced
- Uses same model names (Task, Project, Worker)

### 5. Chapter Position
- User specified "Chapter 44" explicitly
- This creates a new chapter for relational databases
- Fits in the "Data Layer" section of Part 6

## No Clarifications Needed

The user provided comprehensive context:
- Technology choices clearly specified (async only, PostgreSQL, asyncpg)
- Reference implementation path provided
- Lesson structure defined (L00-L09)
- Skill-First pattern specified with `relational-db-agent` as student skill name

## Spec Status: COMPLETE

No additional clarifications required. Proceeding to planning phase.
