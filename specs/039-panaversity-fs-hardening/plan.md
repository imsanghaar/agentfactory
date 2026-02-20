# Implementation Plan: PanaversityFS Production Hardening

**Branch**: `039-panaversity-fs-hardening` | **Date**: 2025-12-04 | **Spec**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/storage/specs/039-panaversity-fs-hardening/spec.md`

**Input**: Harden PanaversityFS storage implementation with PostgreSQL metadata journal, streaming archives, personalization overlays, and audit provenance. Move from POC (local filesystem, JSONL audit) to production (PostgreSQL journal, streaming archives, overlays, delta builds) with formally verifiable guarantees.

---

## Summary

PanaversityFS POC worked locally but failed in production with Cloudflare R2:
- **Archive timeouts**: 50MB+ books caused 502 errors (memory-bound reads)
- **No schema enforcement**: Agents created stray paths with no validation
- **Uncertain updates**: No way to distinguish file create vs update
- **Weak audit**: Read-modify-write failed under R2 latency; all operations logged as `agent_id="system"`
- **No personalization**: No mechanism for user-specific book variants

This plan sequences hardening improvements with PostgreSQL metadata journal (asyncpg/aiosqlite), streaming archives with memory bounds, personalization overlays, hash-based conflict detection, and append-only audit with hash chain integrity. All requirements are backed by Alloy-style invariants (R1-R7) testable with small-scope property-based tests.

---

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**:
  - SQLAlchemy 2.0+ (async ORM)
  - asyncpg 0.29+ (PostgreSQL async driver)
  - aiosqlite 0.19+ (SQLite async driver)
  - Alembic 1.13+ (database migrations)
  - OpenDAL 0.46+ (storage abstraction - existing)
  - FastMCP 1.22+ (MCP server - existing)
  - Pydantic 2.12+ (validation - existing)
  - prometheus-client 0.19+ (metrics instrumentation)
  - hypothesis 6.92+ (property-based testing)

**Storage**:
  - **Metadata**: PostgreSQL 15+ (production via asyncpg) / SQLite (development via aiosqlite)
  - **Content/Assets**: Cloudflare R2 via OpenDAL (production) / Local filesystem (development)
  - **Schema Management**: Alembic migrations with automatic `alembic upgrade head` on startup

**Testing**: pytest 8.0+, pytest-asyncio 0.23+, pytest-postgresql 5.0+, hypothesis 6.92+

**Target Platform**: Google Cloud Run (Linux container) with Neon PostgreSQL (managed)

**Project Type**: Single Python package (`panaversity-fs`)

**Performance Goals**:
  - **SC-001**: 500 files / 200MB archive within 60s, <64MB memory (streaming ZIP)
  - **SC-002**: Zero orphaned storage writes after any failure (atomic journal + storage transaction)
  - **SC-006**: Overlay read adds <10ms latency vs base read (single journal query)

**Constraints**:
  - **Backwards Compatibility**: Existing MCP tool interfaces unchanged; journal integration is transparent to callers
  - **Fresh Start Deployment**: No legacy data migration required (POC had no production content)
  - **Small-Scope Verification**: All invariants (R1-R7) testable with 3-5 instances (Alloy-style)

**Scale/Scope**:
  - Books: 500 files, 200MB each
  - Users: 10k personalized overlays per book
  - Audit retention: 90 days (PostgreSQL), indefinite (cold storage)

---

## Project Structure

### Documentation (this feature)

```text
specs/039-panaversity-fs-hardening/
├── plan.md              # This file (/sp.plan command output)
├── spec.md              # Feature specification (complete)
├── checklists/          # Quality gates
└── tasks.md             # Phase 2 output (/sp.tasks command - will be created)
```

### Source Code (repository root)

```text
panaversity-fs/
├── src/panaversity_fs/
│   ├── __init__.py
│   ├── app.py                    # [EXISTING] FastMCP app
│   ├── config.py                 # [MODIFY] Add database_url, agent_id
│   ├── models.py                 # [MODIFY] Add overlay models, update inputs
│   ├── errors.py                 # [MODIFY] Add SchemaViolationError, HashRequiredError
│   ├── audit.py                  # [MODIFY] Refactor to append-only INSERT
│   ├── storage.py                # [EXISTING] OpenDAL abstraction (unchanged)
│   ├── storage_utils.py          # [EXISTING] SHA256 computation (unchanged)
│   ├── auth.py                   # [EXISTING] JWT auth (unchanged)
│   ├── server.py                 # [EXISTING] MCP server (unchanged)
│   ├── database/                 # [NEW] Database layer
│   │   ├── __init__.py
│   │   ├── models.py             # SQLAlchemy models (FileJournal, AuditLog)
│   │   ├── connection.py         # Session factory, engine setup
│   │   └── migrations/           # Alembic migrations
│   │       ├── env.py
│   │       ├── script.py.mako
│   │       └── versions/
│   │           └── 001_initial_schema.py
│   ├── path_utils.py             # [NEW] Centralized path validation
│   ├── metrics.py                # [NEW] Prometheus instrumentation
│   └── tools/
│       ├── __init__.py
│       ├── content.py            # [MODIFY] Journal integration, overlay support
│       ├── bulk.py               # [MODIFY] Streaming archives, delta build API
│       ├── assets.py             # [EXISTING] (unchanged)
│       ├── registry.py           # [EXISTING] (unchanged)
│       └── search.py             # [EXISTING] (unchanged)
│
├── tests/
│   ├── unit/
│   │   ├── test_path_utils.py            # [NEW] Regex validation
│   │   ├── test_journal.py               # [NEW] FileJournal CRUD
│   │   ├── test_audit_chain.py           # [NEW] Hash chain integrity
│   │   ├── test_manifest_hash.py         # [NEW] Deterministic computation
│   │   ├── test_overlay_resolution.py    # [NEW] Namespace merging
│   │   ├── test_metrics.py               # [NEW] Instrumentation
│   │   ├── test_content_tools.py         # [EXISTING] Update for journal
│   │   ├── test_auth.py                  # [EXISTING] (unchanged)
│   │   └── test_new_features.py          # [EXISTING] (unchanged)
│   ├── integration/
│   │   ├── test_journal_storage_atomic.py  # [NEW] Transaction integrity + fault injection (SC-002)
│   │   ├── test_conflict_detection.py      # [NEW] Concurrent write conflicts (SC-003)
│   │   ├── test_streaming_archive.py       # [NEW] Memory-bounded ZIP
│   │   ├── test_delta_build.py             # [NEW] Changed files detection
│   │   └── test_overlay_isolation.py       # [NEW] User overlay CRUD
│   ├── property/                           # [NEW] Property-based tests
│   │   ├── test_invariant_r1_schema.py     # Schema enforcement
│   │   ├── test_invariant_r2_journal.py    # Journal-storage consistency
│   │   ├── test_invariant_r3_delete.py     # Idempotent delete
│   │   ├── test_invariant_r5_overlay.py    # Overlay exclusivity
│   │   ├── test_invariant_r6_audit.py      # Hash chain integrity
│   │   └── test_invariant_r7_agent.py      # Agent provenance
│   └── performance/
│       ├── test_archive_throughput.py      # [NEW] SC-001 validation
│       └── test_overlay_latency.py         # [NEW] SC-006 validation
│
├── pyproject.toml                # [MODIFY] Add new dependencies
├── alembic.ini                   # [NEW] Alembic configuration
└── README.md                     # [MODIFY] Update with new features
```

**Structure Decision**: Single project layout (existing pattern). Database layer added as new module under `src/panaversity_fs/database/`. All existing tools refactored in-place for journal integration. Test structure expanded with `property/` and `performance/` directories.

---

## Component Architecture & Dependencies

### Tooling & Documentation Strategy

- Use the existing AI Toolkit helpers to pull authoritative references before implementing anything unfamiliar. In practice we will call the `context7` documentation tool to fetch SQLAlchemy, OpenDAL, and FastMCP docs instead of relying on stale knowledge.
- Prefer invoking the CLI (e.g., `alembic`, `pytest`, packaging scripts) to scaffold or mutate project assets rather than hand-editing generated files, so the command history doubles as provenance.
- When questions arise about Azure, storage backends, or library specifics, route through the prescribed best-practices tools first to ensure we stay aligned with internal guidance.

### Dependency Graph

```
Layer 1 (Foundations - No Dependencies)
├── database/           # SQLAlchemy models, session factory, Alembic migrations
├── path_utils.py       # Regex validators, path conversions
└── metrics.py          # Prometheus registry, decorators

Layer 2 (Journal Integration - Depends on Layer 1)
├── tools/content.py    # Refactored with journal CRUD, overlay support
└── audit.py            # Append-only audit with hash chain

Layer 3 (New Features - Depends on Layer 2)
├── tools/bulk.py       # Streaming archives, delta build API
└── overlay support     # Namespace resolution in content tools

Layer 4 (Validation - Depends on All Layers)
├── Integration tests
├── Property-based tests
└── Performance benchmarks
```

### Component Breakdown

#### 1. Database Layer (Foundation)
**Location**: `src/panaversity_fs/database/`

**Key Files**:
- `models.py`: SQLAlchemy models (FileJournal, AuditLog)
- `connection.py`: `async_sessionmaker`, engine configuration
- `migrations/versions/001_initial_schema.py`: Initial tables

**Purpose**: Provides metadata persistence for journal (file hashes, last_written_at) and audit (hash chain provenance).

**Key Entities**:
```python
class FileJournal(Base):
    # Tracks current state: (book_id, path, user_id) → sha256, last_written_at
    # Primary key: (book_id, path, user_id)
    # Supports conflict detection (FR-003) and delta builds (FR-026)

class AuditLog(Base):
    # Append-only history: (id, timestamp, agent_id, operation, prev_hash, new_hash)
    # Hash chain: entry[n].new_hash == entry[n+1].prev_hash (FR-022)
    # Database constraints: agent_id != 'system', agent_id != '' (FR-021)
```

**Dependencies**: None (foundation layer)

---

#### 2. Path Validation (Foundation)
**Location**: `src/panaversity_fs/path_utils.py`

**Purpose**: Centralized path validation to ensure consistent schema enforcement across content writes, overlay resolution, and validation tools.

**Key Functions**:
- `validate_content_path(path)`: Regex match against `content/{NN-Name}/{NN-Name}/{NN-name}(.summary)?.md`
- `validate_asset_path(path)`: Regex match against `static/(img|slides|videos|audio)/{path}`
- `validate_overlay_path(path, user_id)`: Extract and verify user_id from overlay path
- `convert_base_to_overlay(base_path, user_id)`: Transform base → overlay path
- `convert_overlay_to_base(overlay_path)`: Transform overlay → base path

**Dependencies**: None (foundation layer)

---

#### 3. Instrumentation (Foundation)
**Location**: `src/panaversity_fs/metrics.py`

**Purpose**: Prometheus metrics for success criteria validation (SC-001, SC-002, SC-006).

**Key Metrics**:
- Counters: `write_total{status, mode}`, `archive_total{scope, status}`
- Histograms: `archive_duration_seconds{scope}`, `write_duration_seconds{operation}`
- Gauges: `archive_memory_bytes`, `journal_entries_total{book_id}`

**Decorators**:
- `@instrument_write`: Tracks write duration, success/error counts
- `@instrument_archive(scope)`: Tracks archive duration, timeout/error rates

**Dependencies**: None (foundation layer)

---

#### 4. Journal Integration (Depends on Database + Path Validation)
**Location**: Refactor `tools/content.py`

**Key Changes**:
- **write_content**: Query journal for existing hash (FR-003), enforce expected_hash requirement on updates (FR-004), atomic journal + storage write (FR-002)
- **read_content**: Overlay resolution (FR-016) - check `users/{user_id}/content/...` first, fall back to base
- **delete_content**: Remove journal entry, idempotent (FR-018)

**Agent Contract** (Spec requirement):
```python
# Update existing file
current = await read_content(book_id, path)
await write_content(book_id, path, new_content, expected_hash=current.file_hash)

# Create new file
await write_content(book_id, path, content)  # No expected_hash

# FORBIDDEN
await write_content(book_id, path, content)  # Update without expected_hash → HashRequiredError
await write_content(book_id, path, content, expected_hash="...") # Create with hash → NotFoundError
```

**Dependencies**:
- Database layer (journal queries)
- Path validation (schema enforcement)
- Metrics (instrumentation)

---

#### 5. Audit Hardening (Depends on Database)
**Location**: Refactor `audit.py`

**Key Changes**:
- **Append-only INSERT**: No read-modify-write pattern (FR-023)
- **Hash chain**: `prev_hash` from previous operation on same `(book_id, path, user_id)` (FR-022)
- **Agent ID extraction**: From MCP context, NOT hardcoded as "system" (FR-021)
- **Database constraints**: `CHECK (agent_id != 'system' AND agent_id != '')`

**New Function**:
```python
def extract_agent_id_from_context() -> str:
    """Extract agent_id from MCP request metadata.

    Falls back to environment variable for development.
    Raises ValueError if agent_id not available.
    """
```

**Dependencies**:
- Database layer (AuditLog model)

---

#### 6. Streaming Archives (Depends on Database + Metrics)
**Location**: Refactor `tools/bulk.py`

**Key Changes**:
- **Memory-bounded ZIP**: Use `io.BytesIO` buffer with 64MB max (SC-001)
- **Timeout detection**: Return partial result with error manifest after 60s (FR-014)
- **Chunked reads**: Read files in chunks to avoid loading entire book into memory
- **Progress tracking**: Update `archive_memory` gauge throughout generation

**New Tool** (same file):
```python
@mcp.tool(name="plan_build")
async def plan_build(params: PlanBuildInput) -> str:
    """Compute delta between current manifest and target (FR-025, FR-026).

    Returns:
        - status: "unchanged" | "changed"
        - files: [{path, current_hash, target_hash}] (only changed files)
        - manifest_hash: Current manifest hash (deterministic)
    """
```

**Manifest Hash Computation** (Spec algorithm):
```python
def compute_manifest_hash(book_id: str, journal_entries: list[FileJournal]) -> str:
    # 1. Filter to base content only (user_id="__base__")
    # 2. Sort lexicographically by path
    # 3. Concatenate "{path}:{sha256}\n" for each entry
    # 4. SHA256 of concatenated string
```

**Dependencies**:
- Metrics (instrumentation, memory gauge)
- Database (journal queries for delta build)

---

#### 7. Overlay Support (Depends on Database + Path Validation)
**Location**: Integrated into `tools/content.py`

**Key Mechanisms**:
- **Namespace resolution**: `users/{user_id}/content/...` paths stored separately in journal
- **Read precedence**: Overlay → Base fallback (FR-016)
- **Write isolation**: Overlay writes don't affect base (FR-017)
- **Journal tracking**: Separate `(book_id, path, user_id)` primary key enables overlay isolation

**Dependencies**:
- Database layer (journal with user_id column)
- Path validation (overlay path regex, conversion helpers)

---

## Implementation Phases (Dependency-Ordered)

### Phase 1: Foundations (Parallel Execution)

**Duration**: 3-4 days
**Goal**: Establish database layer, path validation, and instrumentation without modifying existing tools

#### Task 1.1: Database Layer Setup
**Files**:
- Create `src/panaversity_fs/database/__init__.py`
- Create `src/panaversity_fs/database/models.py`
- Create `src/panaversity_fs/database/connection.py`
- Create `src/panaversity_fs/database/migrations/env.py`
- Create `src/panaversity_fs/database/migrations/versions/001_initial_schema.py`
- Update `src/panaversity_fs/config.py` (add `database_url` field)
- Update `pyproject.toml` (add SQLAlchemy, asyncpg, aiosqlite, alembic)

**Note**: Alembic is for **forward schema management** (future column additions, indexes), not data migration. Initial deployment is fresh start on empty database.

**Acceptance**:
- [ ] SQLAlchemy models defined with proper constraints (agent_id != 'system', user_id != '')
- [ ] Alembic migration creates tables on empty database (PostgreSQL and SQLite)
- [ ] `alembic upgrade head` runs successfully on fresh DB
- [ ] `get_session()` returns working async session
- [ ] Database constraints enforced by attempting to insert invalid data

**Tests**:
- `tests/unit/test_journal.py` - CRUD operations on FileJournal
- `tests/integration/test_database_backends.py` - Both PostgreSQL and SQLite work

---

#### Task 1.2: Path Validation Module
**Files**:
- Create `src/panaversity_fs/path_utils.py`
- Update `src/panaversity_fs/errors.py` (add SchemaViolationError, HashRequiredError)

**Acceptance**:
- [ ] Regex patterns compiled and exported
- [ ] `validate_content_path()` accepts valid paths, rejects invalid with clear errors
- [ ] `validate_asset_path()` enforces static/ structure
- [ ] `validate_overlay_path()` extracts user_id correctly, rejects mismatch
- [ ] Path conversion helpers work bidirectionally (base ↔ overlay)

**Tests**:
- `tests/unit/test_path_utils.py` - All validation functions with edge cases
- `tests/property/test_invariant_r1_schema.py` - Property-based schema validation

---

#### Task 1.3: Instrumentation Setup
**Files**:
- Create `src/panaversity_fs/metrics.py`
- Update `pyproject.toml` (add prometheus-client)

**Acceptance**:
- [ ] Prometheus registry created with all metrics defined
- [ ] Metrics defined (counters, histograms, gauges) per spec
- [ ] Decorators work (`@instrument_write`, `@instrument_archive`)
- [ ] Metrics can be exported via `generate_latest(registry)`

**Tests**:
- `tests/unit/test_metrics.py` - Decorator behavior, metric increments

---

### Phase 2: Core Refactoring (Sequential)

**Duration**: 5-6 days
**Goal**: Integrate journal into existing tools, harden audit trail

#### Task 2.1: Journal Integration for write_content
**Files**:
- Modify `src/panaversity_fs/tools/content.py` (write_content function)
- Modify `src/panaversity_fs/models.py` (add expected_hash to WriteContentInput)

**Acceptance**:
- [ ] `write_content` queries journal before write (FR-002)
- [ ] Conflict detection works (mismatched expected_hash → ConflictError with current hash)
- [ ] Hash required enforcement (existing file without expected_hash → HashRequiredError)
- [ ] Journal updated atomically with storage write (transaction wraps both)
- [ ] Success response includes `mode: "created"|"updated"` (FR-005)

**Tests**:
- `tests/integration/test_journal_storage_atomic.py` - Transaction integrity, rollback scenarios
- `tests/unit/test_content_tools.py` (update existing tests for new behavior)
- User Story 2 acceptance scenarios (all 4 scenarios)

---

#### Task 2.2: Journal Integration for read_content and delete_content
**Files**:
- Modify `src/panaversity_fs/tools/content.py` (read_content, delete_content)

**Acceptance**:
- [ ] `read_content` queries journal for metadata (optional optimization for future caching)
- [ ] `delete_content` removes journal entry (soft-delete: journal tracks deletion)
- [ ] Idempotent delete works (deleting non-existent returns success, no error)

**Tests**:
- `tests/property/test_invariant_r3_delete.py` - Idempotent delete property (double delete)
- Update existing content tool tests for delete behavior

---

#### Task 2.3: Audit Hardening
**Files**:
- Refactor `src/panaversity_fs/audit.py` (log_operation, query_audit_log)
- Modify all tool files to pass agent_id (extract from MCP context)

**Acceptance**:
- [ ] `log_operation` uses append-only INSERT (no read-modify-write, FR-023)
- [ ] Hash chain maintained (prev_hash from previous entry on same file, FR-022)
- [ ] Agent ID extraction from MCP context works (FR-021)
- [ ] Database constraint rejects agent_id='system' (enforced by CHECK constraint)
- [ ] Query filters work (agent_id, date range, path, operation, FR-024)

**Tests**:
- `tests/unit/test_audit_chain.py` - Hash chain integrity for consecutive operations
- `tests/property/test_invariant_r6_audit.py` - Property-based chain validation (3-5 operations)
- `tests/property/test_invariant_r7_agent.py` - No 'system' or empty agent_id
- User Story 3 acceptance scenarios (all 3 scenarios)

---

### Phase 3: New Features (Parallel Execution)

**Duration**: 4-5 days
**Goal**: Add streaming archives, overlay support, delta build API

#### Task 3.1: Streaming Archives
**Files**:
- Refactor `src/panaversity_fs/tools/bulk.py` (get_book_archive)

**Acceptance**:
- [ ] ZIP generation uses memory-bounded buffer (<64MB, SC-001)
- [ ] Timeout detection returns partial result with error manifest (FR-014)
- [ ] Archive completes within 60s for 500 files / 200MB (SC-001)
- [ ] Memory gauge tracked throughout operation (`archive_memory`)

**Tests**:
- `tests/integration/test_streaming_archive.py` - Real archive generation with filesystem/R2
- `tests/performance/test_archive_throughput.py` - SC-001 validation (synthetic 500-file book)
- User Story 1 acceptance scenarios (all 3 scenarios)

---

#### Task 3.2: Overlay Support
**Files**:
- Modify `src/panaversity_fs/tools/content.py` (read/write/delete with user_id parameter)
- Modify `src/panaversity_fs/models.py` (add user_id to ReadContentInput, WriteContentInput, DeleteContentInput)

**Acceptance**:
- [ ] Write with user_id creates overlay at `users/{user_id}/content/...` (FR-017)
- [ ] Read with user_id checks overlay first, falls back to base (FR-016)
- [ ] Delete with user_id removes overlay only, never affects base (FR-018)
- [ ] Overlay paths validated correctly (FR-019)
- [ ] Overlay reads add <10ms latency vs base read (SC-006)

**Tests**:
- `tests/integration/test_overlay_isolation.py` - CRUD operations on overlays
- `tests/property/test_invariant_r5_overlay.py` - Overlay exclusivity (2 users, 2 lessons)
- `tests/performance/test_overlay_latency.py` - SC-006 validation (overlay vs base read)
- User Story 4 acceptance scenarios (all 4 scenarios)

---

#### Task 3.3: Delta Build API
**Files**:
- Add `plan_build` tool to `src/panaversity_fs/tools/bulk.py`
- Add `PlanBuildInput` model to `src/panaversity_fs/models.py`

**Acceptance**:
- [ ] `compute_manifest_hash()` produces deterministic hash (spec algorithm)
- [ ] First build returns all files (no target_manifest_hash provided)
- [ ] Unchanged manifest returns `status: "unchanged"` with empty file list
- [ ] Changed manifest returns delta files (current_hash vs target_hash)

**Tests**:
- `tests/unit/test_manifest_hash.py` - Deterministic computation (same input → same hash)
- `tests/integration/test_delta_build.py` - Changed file detection across writes
- User Story 6 acceptance scenarios (all 3 scenarios)

---

### Phase 4: Validation (Sequential)

**Duration**: 3-4 days
**Goal**: Comprehensive testing across all layers

#### Task 4.1: Integration Tests
**Files**:
- All `tests/integration/test_*.py` files from Phase 2 and 3

**Acceptance**:
- [ ] All integration tests pass on both PostgreSQL and SQLite
- [ ] Journal-storage atomicity verified (transaction rollback scenarios)
- [ ] Overlay isolation verified (user-specific content doesn't leak)
- [ ] Streaming archives work end-to-end with real storage backends

---

#### Task 4.2: Performance Benchmarks
**Files**:
- `tests/performance/test_archive_throughput.py`
- `tests/performance/test_overlay_latency.py`

**Acceptance**:
- [ ] SC-001: 500 files / 200MB < 60s, <64MB memory (actual measurement logged)
- [ ] SC-006: Overlay read adds <10ms latency (actual measurement logged)
- [ ] Benchmark results logged and tracked for regression detection

---

#### Task 4.3: Property-Based Invariant Verification
**Files**:
- All `tests/property/test_invariant_*.py` files

**Acceptance**:
- [ ] R1: Schema enforcement (all valid paths match regex, all invalid rejected)
- [ ] R2: Journal-storage consistency (hashes match after writes)
- [ ] R3: Idempotent delete (double delete succeeds)
- [ ] R5: Overlay exclusivity (no base contamination, correct user resolution)
- [ ] R6: Audit chain integrity (consecutive hashes link, no breaks)
- [ ] R7: Agent provenance (no 'system' or empty agent_id in audit log)

**Tests** (using hypothesis for property-based testing):
```python
from hypothesis import given, strategies as st

@given(st.lists(st.text(min_size=1), min_size=3, max_size=5))
async def test_delete_idempotent(paths):
    """R3: Deleting same path twice always succeeds (small scope: 3-5 paths)."""
    for path in paths:
        result1 = await delete_content(book_id="test", path=path)
        result2 = await delete_content(book_id="test", path=path)
        assert result1["status"] == "success"
        assert result2["status"] == "success"
```

---

## Deployment Strategy: Fresh Start

### No Migration Required

**Context**: POC was prototype-only. No production data exists in R2 or JSONL audit logs that needs preservation. This is a clean-slate deployment.

**Approach**:
1. Deploy hardened system directly to production
2. `alembic upgrade head` creates fresh tables (FileJournal, AuditLog)
3. First content write populates journal from scratch
4. Audit trail starts clean with proper agent provenance

**Why This Works**:
- POC never held production content (test books only)
- JSONL audit was development debugging, not compliance record
- R2 bucket can be wiped or content re-synced from source (Git)
- No user overlays exist to preserve

**Rollback Plan** (if hardened system has issues):
- Feature flag `PANAVERSITYFS_JOURNAL_ENABLED=false` bypasses journal checks
- System degrades gracefully: writes succeed without conflict detection
- Re-enable journal once issues resolved, re-sync content hashes

---

## Test Strategy

### Unit Tests
**Coverage Target**: 80%+

| Component | Test File | Focus |
|-----------|-----------|-------|
| Path validation | `test_path_utils.py` | Regex matching, conversions, edge cases |
| Journal CRUD | `test_journal.py` | SQLAlchemy model operations |
| Manifest hash | `test_manifest_hash.py` | Deterministic computation |
| Metrics | `test_metrics.py` | Decorator behavior, counter/gauge increments |

---

### Integration Tests
**Coverage Target**: All cross-component interactions

| Component | Test File | Focus |
|-----------|-----------|-------|
| Journal + Storage | `test_journal_storage_atomic.py` | Transaction rollback, fault injection (SC-002) |
| Conflict detection | `test_conflict_detection.py` | Concurrent writes, stale hash rejection (SC-003) |
| Streaming archives | `test_streaming_archive.py` | Real ZIP generation with R2/filesystem |
| Delta build | `test_delta_build.py` | Changed file detection across writes |
| Overlay isolation | `test_overlay_isolation.py` | User-specific content CRUD |
| Audit chain | `test_audit_chain.py` | Hash chain integrity across operations |

---

### Property-Based Tests (Hypothesis)
**Coverage Target**: Logical invariants (R1-R3, R5-R7) via property-based testing

| Invariant | Test File | Strategy |
|-----------|-----------|----------|
| R1: Schema | `test_invariant_r1_schema.py` | Generate valid/invalid paths, verify 100% rejection of invalid |
| R2: Journal consistency | `test_invariant_r2_journal.py` | Write files, verify journal hashes match storage |
| R3: Idempotent delete | `test_invariant_r3_delete.py` | Delete paths multiple times, verify success always |
| R5: Overlay exclusivity | `test_invariant_r5_overlay.py` | Read with different users, verify correct content |
| R6: Audit chain | `test_invariant_r6_audit.py` | Perform operations, verify consecutive hashes link |
| R7: Agent provenance | `test_invariant_r7_agent.py` | Query audit log, verify no 'system' or empty |

**Note on R4 (Archive Throughput Bound)**: R4 is a **performance invariant**, not a logical property. It cannot be verified symbolically—only empirically. R4 is covered by `tests/performance/test_archive_throughput.py` (see Performance Tests section), not property-based testing.

**Small-Scope Testing Pattern** (3-5 instances per Alloy specification):
```python
@given(
    st.lists(
        st.fixed_dictionaries({
            'path': st.from_regex(CONTENT_PATH_PATTERN, fullmatch=True),
            'content': st.text(min_size=1, max_size=1000)
        }),
        min_size=3,
        max_size=5
    )
)
async def test_journal_storage_consistency(files):
    """R2: For small scope (3-5 files), journal always matches storage."""
    for file in files:
        await write_content(book_id="test", path=file['path'], content=file['content'])

    # Verify all journal entries match storage
    for file in files:
        journal_entry = await get_journal_entry("test", file['path'])
        storage_bytes = await storage.read(f"books/test/{file['path']}")
        storage_hash = compute_sha256(storage_bytes)

        assert journal_entry.sha256 == storage_hash
```

---

### Performance Tests
**Coverage Target**: Success criteria with performance bounds

| Success Criteria | Test File | Assertion |
|-----------------|-----------|-----------|
| SC-001 / R4 | `test_archive_throughput.py` | 500 files / 200MB < 60s, <64MB RAM |
| SC-006 | `test_overlay_latency.py` | Overlay read - base read < 10ms |

### Fault-Injection Tests
**Coverage Target**: Failure mode guarantees

| Success Criteria | Test File | Strategy |
|-----------------|-----------|----------|
| SC-002 | `test_journal_storage_atomic.py` | Inject storage failure mid-write, verify journal rolls back, no orphan in storage |
| SC-002 | `test_journal_storage_atomic.py` | Inject DB failure after storage write, verify storage write rolls back |
| SC-003 | `test_conflict_detection.py` | Concurrent writes with stale hash, verify exactly one succeeds, one gets CONFLICT |

---

## Deployment Checklist

### Pre-Deployment
- [ ] All Phase 4 tests passing (unit, integration, property, performance)
- [ ] Alembic migration creates schema correctly (`alembic upgrade head` on empty DB)
- [ ] Database credentials configured in Cloud Run secrets
- [ ] Prometheus metrics endpoint accessible (`/metrics`)
- [ ] Health check includes database connectivity status

### Deployment Steps
1. **Database Setup**:
   - Provision Neon PostgreSQL instance
   - Run `alembic upgrade head` to create tables
   - Verify schema with `alembic current`

2. **Application Deployment**:
   - Set `DATABASE_URL` environment variable in Cloud Run
   - Deploy new container image
   - Monitor startup logs for migration success

3. **Validation**:
   - Health check returns database: healthy
   - Write operation creates journal entry
   - Audit log populated with actual agent IDs (not "system")
   - Archive generation completes within timeout

### Post-Deployment Monitoring
- **Week 1**: Monitor journal-storage consistency via daily health checks
- **Week 2**: Analyze audit chain integrity (no broken prev_hash links)
- **Week 3**: Review performance metrics (archive duration, overlay latency)
- **Week 4**: Validate success criteria (SC-001 through SC-010)

---

## Risk Mitigation

### Risk 1: Journal-Storage Desync (High Impact)
**Mitigation**:
- Database transaction wraps both journal update and storage write
- Health check compares journal to storage daily
- Manual reconciliation script for detected desyncs

**Detection Script**:
```python
async def detect_journal_desync(book_id: str) -> list[str]:
    """Compare journal entries to actual storage."""
    orphans = []
    async with get_session() as session:
        entries = await session.execute(
            select(FileJournal).where(FileJournal.book_id == book_id)
        )
        for entry in entries.scalars():
            try:
                storage_bytes = await op.read(f"books/{book_id}/{entry.path}")
                storage_hash = compute_sha256(storage_bytes)
                if storage_hash != entry.sha256:
                    orphans.append(entry.path)
            except FileNotFoundError:
                orphans.append(entry.path)
    return orphans
```

---

### Risk 2: PostgreSQL Connection Pool Exhaustion (Medium Impact)
**Mitigation**:
- Configure max pool size: 20 connections
- Set connection timeout: 30 seconds
- Monitor pool usage via SQLAlchemy metrics
- Implement request queuing if needed

---

### Risk 3: Future Schema Changes Break Running System (Medium Impact)
**Mitigation**:
- Alembic used for forward schema management (new columns, indexes), not data migration
- All future migrations designed as additive (new nullable columns, new tables)
- Never delete columns in production (deprecate first, remove after confirmed unused)
- Note: Initial deployment is fresh start with no existing data to protect

---

## Timeline Summary

| Phase | Duration | Deliverables |
|-------|----------|--------------|
| **Phase 1: Foundations** | 3-4 days | Database layer, path validation, metrics |
| **Phase 2: Core Refactoring** | 5-6 days | Journal integration, audit hardening |
| **Phase 3: New Features** | 4-5 days | Streaming archives, overlays, delta build |
| **Phase 4: Validation** | 3-4 days | Integration tests, performance benchmarks, invariants |
| **Total** | **15-19 days** | Production-ready hardened system |

**Critical Path**: Phase 1 → Task 2.1 → Task 2.2 → Task 2.3 → Phase 4

**Parallelization Opportunities**:
- Phase 1 tasks (database, path validation, metrics) can run in parallel
- Phase 3 tasks (archives, overlays, delta build) can run in parallel after Phase 2

---

## Cross-Book Intelligence

### Patterns Reusable Across Platform

**Hash-Based Conflict Detection Pattern**:
- **What**: Journal tracks file hashes; writes verify expected_hash before update
- **Where Used**: PanaversityFS content operations
- **Reusable For**: Any multi-agent collaborative storage system
- **Generalization**: Replace FileJournal with EntityJournal(entity_type, entity_id, hash)

**Streaming Archive Pattern**:
- **What**: Memory-bounded ZIP generation with timeout and partial results
- **Where Used**: `get_book_archive` tool
- **Reusable For**: Bulk export in any content system (courses, projects, datasets)
- **Generalization**: StreamingArchiver(max_memory, timeout, error_handler)

**Overlay Namespace Pattern**:
- **What**: User-specific content stored at `users/{user_id}/{base_path}`, reads fall through to base
- **Where Used**: Personalized lesson variants
- **Reusable For**: Multi-tenant systems, A/B testing, staged rollouts
- **Generalization**: OverlayResolver(namespace_prefix, fallback_strategy)

**Append-Only Audit with Hash Chain**:
- **What**: AuditLog table with prev_hash/new_hash linking consecutive operations
- **Where Used**: File provenance tracking
- **Reusable For**: Any system requiring tamper-evident logs (financial, compliance)
- **Generalization**: HashChainAudit(entity_type, chain_field)

### Patterns Specific to This Service

**Docusaurus Book Schema**:
- **What**: Regex validation for `content/{NN-Name}/{NN-Name}/{NN-name}.md`
- **Where Used**: Path validation in write operations
- **Scope**: PanaversityFS only (coupled to Docusaurus structure)

**Manifest Hash for Incremental Builds**:
- **What**: Deterministic hash of all (path, sha256) pairs for delta detection
- **Where Used**: `plan_build` tool
- **Scope**: PanaversityFS only (optimizes Docusaurus CI/CD)

---

## Success Validation

### Acceptance Criteria Checklist

**User Story 1** (Book Archive - P1):
- [ ] 500 files / 200MB archives within 60s
- [ ] <64MB server memory usage during archive
- [ ] Timeout returns partial result with error manifest
- [ ] Corrupted file logged, archive continues

**User Story 2** (Write Conflict Detection - P1):
- [ ] Update with matching expected_hash succeeds, returns `mode: "updated"`
- [ ] Update with mismatched expected_hash returns CONFLICT error with current hash
- [ ] Create without expected_hash succeeds, returns `mode: "created"`
- [ ] Create with expected_hash returns NOT_FOUND error

**User Story 3** (Audit Trail - P2):
- [ ] Query returns all operations on path with agent_id, prev_hash, new_hash
- [ ] Consecutive entries satisfy `entry[n].new_hash == entry[n+1].prev_hash`
- [ ] Specific agent_id appears in audit log (not "system")

**User Story 4** (Personalized Content - P2):
- [ ] Read with user_id returns overlay when exists
- [ ] Read with different user_id returns base content
- [ ] Base update doesn't affect overlay
- [ ] Overlay delete falls back to base

**User Story 5** (Schema Validation - P2):
- [ ] Valid path succeeds
- [ ] Invalid path (no NN- prefix) fails with SCHEMA_VIOLATION
- [ ] Summary path (lesson.summary.md) succeeds
- [ ] Path traversal (../) fails with INVALID_PATH

**User Story 6** (Delta Build - P3):
- [ ] Changed files detected correctly
- [ ] Unchanged manifest returns `status: "unchanged"`
- [ ] First build returns all files

---

## Next Steps After Implementation

1. **Production Monitoring**:
   - Set up Prometheus scraping of `/metrics` endpoint
   - Create Grafana dashboards for journal size, audit chain integrity
   - Alert on journal-storage desync detection

2. **Documentation**:
   - Update API documentation with new parameters (expected_hash, user_id)
   - Document agent contract for hash-based updates
   - Create runbook for journal desync recovery

3. **Optimization Opportunities** (Post-MVP):
   - Implement true delta build (store manifest snapshots in database)
   - Add batch journal queries for bulk operations
   - Optimize overlay reads with journal caching

---

**End of Plan**
