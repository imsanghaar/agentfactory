# PanaversityFS Production Hardening - Implementation Prompt

**Feature**: `039-panaversity-fs-hardening`
**Working Directory**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/panaversity-fs`
**Artifacts**: `specs/039-panaversity-fs-hardening/` (spec.md, plan.md, tasks.md)

---

## Executive Summary

Harden PanaversityFS from POC to production with:
- PostgreSQL metadata journal (asyncpg/aiosqlite)
- Streaming archives with 64MB memory cap
- Hash-based conflict detection
- Personalization overlays
- Append-only audit with hash chain integrity

**MVP Scope**: Phase 1 (Setup) + Phase 2 (Foundational) + Phase 3 (US1: Archives) + Phase 4 (US2: Conflict Detection)

---

## Behavioral Guardrails

<default_to_action>
Implement changes directly. Don't suggest—execute. Read files before editing. Use CLI tools for scaffolding. Commit after logical task groups.
</default_to_action>

<cli_first_principle>
ALWAYS prefer CLI commands over manual file creation:

| Action | USE THIS | NOT THIS |
|--------|----------|----------|
| Add dependencies | `uv add sqlalchemy asyncpg` | Manually edit pyproject.toml |
| Init Alembic | `alembic init <path>` | Manually create env.py |
| Create migration | `alembic revision --autogenerate -m "msg"` | Manually create version file |
| Verify install | `uv pip list \| grep <pkg>` | Assume it worked |
</cli_first_principle>

<documentation_lookup_principle>
BEFORE implementing any library integration, fetch official docs via Context7:

```
# Required lookups for this feature:
mcp__context7__resolve-library-id("sqlalchemy")     → async patterns
mcp__context7__resolve-library-id("alembic")        → async migrations
mcp__context7__resolve-library-id("prometheus-client") → metrics/decorators
mcp__context7__resolve-library-id("hypothesis")     → property testing
mcp__context7__resolve-library-id("pydantic")       → settings patterns
```

When task says `**Doc**: Fetch X docs via Context7`, you MUST call Context7 before implementing.
</documentation_lookup_principle>

<investigate_before_acting>
Never speculate about existing code. Before modifying any file:
1. Read the file first
2. Understand existing patterns
3. Follow existing conventions (naming, imports, error handling)
</investigate_before_acting>

---

## Project Context

**Existing Structure**:
```
panaversity-fs/
├── src/panaversity_fs/
│   ├── __init__.py
│   ├── app.py              # FastMCP app
│   ├── audit.py            # Current audit (JSONL-based, needs refactor)
│   ├── auth.py             # JWT auth (unchanged)
│   ├── config.py           # Pydantic settings (add database_url)
│   ├── errors.py           # Exceptions (add new error types)
│   ├── models.py           # Pydantic models (add new fields)
│   ├── server.py           # MCP server (unchanged)
│   ├── storage.py          # OpenDAL abstraction (unchanged)
│   ├── storage_utils.py    # SHA256 computation (unchanged)
│   └── tools/
│       ├── assets.py       # Asset operations
│       ├── bulk.py         # Archive generation (refactor for streaming)
│       ├── content.py      # CRUD operations (add journal integration)
│       ├── registry.py     # Tool registry
│       └── search.py       # Search operations
├── tests/
│   └── unit/               # Existing tests
├── pyproject.toml          # Add new dependencies
└── alembic.ini             # NEW: Alembic config
```

**New Directories to Create**:
```
src/panaversity_fs/
├── database/               # NEW
│   ├── __init__.py
│   ├── models.py           # SQLAlchemy models
│   ├── connection.py       # Async session factory
│   └── migrations/         # Alembic (via `alembic init`)
├── path_utils.py           # NEW: Path validation
└── metrics.py              # NEW: Prometheus instrumentation

tests/
├── integration/            # NEW
├── property/               # NEW
└── performance/            # NEW
```

---

## Phase 1: Setup (T001-T004)

### T001: Add Dependencies

```bash
cd /Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/panaversity-fs
uv add sqlalchemy asyncpg aiosqlite alembic prometheus-client hypothesis
```

**Verify**:
```bash
uv pip list | grep -E "sqlalchemy|asyncpg|aiosqlite|alembic|prometheus|hypothesis"
```

**Expected**: All 6 packages listed with versions.

---

### T002: Initialize Alembic

**Step 1**: Fetch Alembic docs for async configuration
```
Context7: alembic → topic: "async migrations"
```

**Step 2**: Run Alembic init
```bash
cd /Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/panaversity-fs
alembic init src/panaversity_fs/database/migrations
```

**Step 3**: Configure `alembic.ini` (created at project root)
- Set `script_location = src/panaversity_fs/database/migrations`
- Set `sqlalchemy.url` to use env var: `driver://user:pass@localhost/dbname` (placeholder, overridden in env.py)

**Verify**:
```bash
ls src/panaversity_fs/database/migrations/
# Should show: env.py, script.py.mako, versions/, README
```

---

### T003: Create Database Module Init

**File**: `src/panaversity_fs/database/__init__.py`

```python
"""Database layer for PanaversityFS metadata journal and audit log."""

from .models import FileJournal, AuditLog, Base
from .connection import get_session, get_engine, init_db

__all__ = [
    "FileJournal",
    "AuditLog",
    "Base",
    "get_session",
    "get_engine",
    "init_db",
]
```

---

### T004: Add database_url to Config

**Step 1**: Fetch Pydantic docs
```
Context7: pydantic → topic: "BaseSettings environment variables"
```

**Step 2**: Edit `src/panaversity_fs/config.py`

Add field to `Config` class:
```python
# Database Configuration
# PostgreSQL: postgresql+asyncpg://user:pass@host/db
# SQLite: sqlite+aiosqlite:///./panaversity_fs.db
database_url: str | None = None  # Falls back to SQLite if not set

@property
def effective_database_url(self) -> str:
    """Get database URL, defaulting to SQLite for development."""
    return self.database_url or "sqlite+aiosqlite:///./panaversity_fs.db"
```

---

## Phase 2: Foundational (T005-T017)

### T005: SQLAlchemy Models

**Step 1**: Fetch SQLAlchemy docs
```
Context7: sqlalchemy → topic: "async DeclarativeBase Mapped"
```

**File**: `src/panaversity_fs/database/models.py`

```python
"""SQLAlchemy models for PanaversityFS metadata."""

from datetime import datetime
from typing import Optional
from sqlalchemy import String, DateTime, Text, Index, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """Base class for all models."""
    pass


class FileJournal(Base):
    """Tracks current state of every file for conflict detection and delta builds.

    Primary key: (book_id, path, user_id)
    Invariant R2: sha256 matches actual storage content
    """
    __tablename__ = "file_journal"

    book_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    path: Mapped[str] = mapped_column(String(1024), primary_key=True)
    user_id: Mapped[str] = mapped_column(String(255), primary_key=True, default="__base__")
    sha256: Mapped[str] = mapped_column(String(64), nullable=False)
    last_written_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    storage_backend: Mapped[str] = mapped_column(String(50), default="s3")

    __table_args__ = (
        Index("ix_file_journal_book_path", "book_id", "path"),
    )


class AuditLog(Base):
    """Append-only audit trail with hash chain integrity.

    Invariant R6: entry[n].new_hash == entry[n+1].prev_hash
    Invariant R7: agent_id != 'system' and agent_id != ''
    """
    __tablename__ = "audit_log"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, index=True)
    agent_id: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    operation: Mapped[str] = mapped_column(String(50), nullable=False)  # create, update, delete, read
    book_id: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    path: Mapped[str] = mapped_column(String(1024), nullable=False)
    user_id: Mapped[str] = mapped_column(String(255), default="__base__")
    prev_hash: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    new_hash: Mapped[Optional[str]] = mapped_column(String(64), nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="success")
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    execution_time_ms: Mapped[Optional[int]] = mapped_column(nullable=True)

    __table_args__ = (
        CheckConstraint("agent_id != 'system'", name="ck_agent_not_system"),
        CheckConstraint("agent_id != ''", name="ck_agent_not_empty"),
        Index("ix_audit_book_path_user", "book_id", "path", "user_id"),
    )
```

---

### T006: Connection Factory

**Step 1**: Fetch SQLAlchemy docs
```
Context7: sqlalchemy → topic: "create_async_engine async_sessionmaker"
```

**File**: `src/panaversity_fs/database/connection.py`

```python
"""Async database connection management."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
    AsyncEngine,
)

from ..config import get_config
from .models import Base


_engine: AsyncEngine | None = None
_session_factory: async_sessionmaker[AsyncSession] | None = None


def get_engine() -> AsyncEngine:
    """Get or create the async engine singleton."""
    global _engine
    if _engine is None:
        config = get_config()
        _engine = create_async_engine(
            config.effective_database_url,
            echo=config.log_level == "DEBUG",
            pool_pre_ping=True,
        )
    return _engine


def get_session_factory() -> async_sessionmaker[AsyncSession]:
    """Get or create the session factory singleton."""
    global _session_factory
    if _session_factory is None:
        _session_factory = async_sessionmaker(
            get_engine(),
            class_=AsyncSession,
            expire_on_commit=False,
        )
    return _session_factory


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Get an async database session with automatic cleanup."""
    factory = get_session_factory()
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


async def init_db() -> None:
    """Initialize database tables (for development/testing)."""
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
```

---

### T007: Configure Alembic env.py for Async

**Step 1**: Fetch Alembic docs
```
Context7: alembic → topic: "async run_migrations_online"
```

**Edit**: `src/panaversity_fs/database/migrations/env.py`

Key changes:
1. Import async engine from connection.py
2. Use `run_sync` for migrations
3. Load config from panaversity_fs.config

```python
# Add to env.py after alembic init generates it:
import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

# Import your models for autogenerate
from panaversity_fs.database.models import Base
from panaversity_fs.config import get_config

# ... existing config setup ...

def get_url():
    return get_config().effective_database_url

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=Base.metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=Base.metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations() -> None:
    """Run migrations in 'online' mode with async engine."""
    configuration = config.get_section(config.config_ini_section) or {}
    configuration["sqlalchemy.url"] = get_url()

    connectable = async_engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    asyncio.run(run_async_migrations())

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

---

### T008: Generate Initial Migration

```bash
cd /Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/panaversity-fs
alembic revision --autogenerate -m "initial FileJournal and AuditLog schema"
```

**Post-generation**: Review the migration file in `versions/`. Verify CHECK constraints are present:
- `ck_agent_not_system`
- `ck_agent_not_empty`

If missing, add manually:
```python
op.create_check_constraint('ck_agent_not_system', 'audit_log', "agent_id != 'system'")
op.create_check_constraint('ck_agent_not_empty', 'audit_log', "agent_id != ''")
```

**Verify**:
```bash
alembic upgrade head
alembic current
```

---

### T009-T017: Continue with remaining foundational tasks...

(Path validation, metrics, tests - follow same pattern)

---

## Spec References

**Key Functional Requirements**:
- **FR-002**: Journal entry BEFORE storage write (atomic transaction)
- **FR-003**: Conflict detection via expected_hash
- **FR-004**: Hash required for updates (no blind overwrites)
- **FR-005**: Response includes `mode: "created"|"updated"`
- **FR-007**: Content path regex: `content/{NN-Name}/{NN-Name}/{NN-name}(.summary)?.md`
- **FR-014**: Timeout returns partial result with error manifest
- **FR-021**: Agent ID from MCP context (never "system")
- **FR-022**: Hash chain: `entry[n].new_hash == entry[n+1].prev_hash`

**Success Criteria**:
- **SC-001/R4**: 500 files/200MB < 60s, <64MB memory
- **SC-002**: Zero orphaned storage writes (atomic rollback)
- **SC-003**: 100% conflict detection accuracy
- **SC-006**: Overlay read adds <10ms latency

**Invariants** (property-based tests):
- **R1**: Schema enforcement (all paths match regex)
- **R2**: Journal-storage consistency (hashes match)
- **R3**: Idempotent delete (double delete succeeds)
- **R5**: Overlay exclusivity (correct user resolution)
- **R6**: Audit chain integrity (consecutive hashes link)
- **R7**: Agent provenance (no 'system' or empty)

---

## Execution Pattern

For each task:

1. **Read task from tasks.md** - Get exact requirements
2. **Fetch docs if `**Doc**` present** - Use Context7
3. **Read existing files** - Understand current patterns
4. **Implement** - Follow existing conventions
5. **Verify** - Run specified verification command
6. **Commit** - After logical task group

```bash
# Example commit pattern
git add src/panaversity_fs/database/
git commit -m "feat(039): add database layer with FileJournal and AuditLog models (T005-T008)"
```

---

## Start Command

Begin implementation with Phase 1, Task T001:

```bash
cd /Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/panaversity-fs
uv add sqlalchemy asyncpg aiosqlite alembic prometheus-client hypothesis
```

Then proceed sequentially through tasks, fetching Context7 docs where indicated.
