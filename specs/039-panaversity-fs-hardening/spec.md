# Feature Specification: PanaversityFS Production Hardening

**Feature Branch**: `039-panaversity-fs-hardening`
**Created**: 2025-12-04
**Status**: Draft
**Input**: Harden PanaversityFS storage implementation with PostgreSQL metadata journal, streaming archives, personalization overlays, and audit provenance
**Predecessor**: `specs/030-panaversity-fs/` (POC implementation)

## Executive Summary

PanaversityFS POC worked locally but failed in production with Cloudflare R2:
- **Archive timeouts**: 50MB+ books caused 502 errors (memory-bound reads)
- **No schema enforcement**: Agents created stray paths with no validation
- **Uncertain updates**: No way to distinguish file create vs update
- **Weak audit**: Read-modify-write failed under R2 latency; all operations logged as `agent_id="system"`
- **No personalization**: No mechanism for user-specific book variants

This specification hardens the storage layer with formally verifiable requirements (Alloy-style invariants) to move from POC to production.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Docusaurus Build Fetches Complete Book (Priority: P1)

A Docusaurus build pipeline needs to download an entire book's content reliably from PanaversityFS storage during CI/CD to generate the published website.

**Why this priority**: Without reliable book downloads, no content can be published. This is the core use case that failed in production (502 timeouts on 50MB+ books).

**Independent Test**: Can be tested by triggering a Docusaurus build with a 50MB book (300 lessons, 100 assets) and measuring completion time and memory usage. Delivers value immediately as the publishing pipeline becomes reliable.

**Acceptance Scenarios**:

1. **Given** a book with 500 files totaling 200MB exists in R2 storage, **When** hydration script calls `get_book_archive` with `scope=content`, **Then** archive downloads within 60 seconds with <64MB server memory usage
2. **Given** archive generation exceeds 60 seconds, **When** timeout triggers, **Then** system returns partial progress indicator with resumption token for retry
3. **Given** a single file is corrupted in R2, **When** archive generation encounters the file, **Then** it logs the error and continues with remaining files, including error manifest in response

---

### User Story 2 - Agent Updates Lesson with Conflict Detection (Priority: P1)

An AI agent updates a lesson file and needs certainty whether the operation was a create (new file) or update (existing file modified), with protection against concurrent overwrites.

**Why this priority**: Core CRUD reliability. Without knowing if operations succeed or conflict, agents cannot maintain content integrity. This was a major production confusion point.

**Independent Test**: Can be tested by calling `write_content` with and without `expected_hash`, verifying journal entries, and testing concurrent writes from two agents. Delivers value as agents gain confidence in their operations.

**Acceptance Scenarios**:

1. **Given** a lesson file exists with hash `abc123`, **When** agent calls `write_content` with `expected_hash=abc123` and new content, **Then** file updates, journal records new hash, and response indicates `mode: "updated"`
2. **Given** a lesson file exists with hash `abc123`, **When** agent calls `write_content` with `expected_hash=wrong456`, **Then** system rejects with `CONFLICT` error including current hash for retry
3. **Given** a path does not exist, **When** agent calls `write_content` without `expected_hash`, **Then** file creates, journal records hash, and response indicates `mode: "created"`
4. **Given** a path does not exist, **When** agent calls `write_content` WITH `expected_hash`, **Then** system rejects with `NOT_FOUND` error (can't update non-existent file)

---

### User Story 3 - System Administrator Queries Audit Trail (Priority: P2)

A developer or monitoring agent needs to trace all operations on a specific file to debug issues, with complete provenance including which agent made each change.

**Why this priority**: Observability is essential for production debugging but not required for basic content operations. Enables root cause analysis after core features work.

**Independent Test**: Can be tested by performing several operations, then querying audit log with filters, verifying returned entries have complete agent_id, prev_hash, and new_hash forming a traceable chain.

**Acceptance Scenarios**:

1. **Given** 10 operations occurred on `content/01-Part/01-Chapter/lesson.md`, **When** admin queries audit log filtered by path, **Then** system returns all 10 entries with `agent_id`, `prev_hash`, `new_hash`, and timestamp
2. **Given** audit entries for a file, **When** examining consecutive entries, **Then** `entry[n].new_hash == entry[n+1].prev_hash` (hash chain integrity)
3. **Given** an agent with ID `claude-lesson-writer-7` performs an operation, **When** audit log is queried, **Then** that specific agent_id appears (not "system")

---

### User Story 4 - Personalized Book for Individual User (Priority: P2)

A student has a personalized learning experience where certain lessons are modified specifically for them (e.g., translated, simplified, or extended) without affecting the shared base book.

**Why this priority**: Personalization is a key platform differentiator but not required for initial content management. Enables future adaptive learning without architectural rework.

**Independent Test**: Can be tested by creating a base lesson, then creating a user overlay, and verifying reads resolve to overlay when user context is provided, base otherwise.

**Acceptance Scenarios**:

1. **Given** base lesson exists at `books/python-book/content/01-Part/01-lesson.md`, **When** user `user-123` has overlay at `books/python-book/users/user-123/content/01-Part/01-lesson.md`, **Then** reading with `user_id=user-123` returns overlay content
2. **Given** user overlay exists for lesson, **When** reading with `user_id=user-456` (different user), **Then** system returns base lesson (no overlay for this user)
3. **Given** user overlay exists, **When** base lesson is updated, **Then** overlay remains unchanged (overlays are independent)
4. **Given** user overlay exists, **When** overlay is deleted, **Then** subsequent reads fall back to base lesson

---

### User Story 5 - Book Schema Validation on Write (Priority: P2)

Content paths must conform to the Docusaurus-aligned schema to ensure agents cannot create stray files that break the build or become orphaned.

**Why this priority**: Schema enforcement prevents the "no structure, no guidelines" problem observed in production. Without it, storage degrades over time.

**Independent Test**: Can be tested by attempting to write files with valid and invalid paths, verifying valid paths succeed and invalid paths are rejected with clear error messages.

**Acceptance Scenarios**:

1. **Given** path `content/01-Part-Name/01-Chapter/01-lesson.md`, **When** agent calls `write_content`, **Then** operation succeeds (matches schema)
2. **Given** path `lessons/random/file.md`, **When** agent calls `write_content`, **Then** operation fails with `SCHEMA_VIOLATION: Path must match content/{NN-Name}/{NN-Name}/{NN-lesson}.md`
3. **Given** path `content/01-Part/01-Chapter/lesson.summary.md`, **When** agent calls `write_content`, **Then** operation succeeds (summaries allowed)
4. **Given** path `content/../../../etc/passwd`, **When** agent calls `write_content`, **Then** operation fails with `INVALID_PATH: Path traversal not allowed`

---

### User Story 6 - Delta Build Detection (Priority: P3)

Docusaurus build pipeline needs to know which files changed since last build to enable incremental builds instead of full rebuilds.

**Why this priority**: Performance optimization that reduces CI/CD time but not required for basic functionality. Enables faster iteration cycles.

**Independent Test**: Can be tested by calling `plan_build` with a known manifest hash and verifying it returns only changed files.

**Acceptance Scenarios**:

1. **Given** previous build had manifest hash `manifest-abc`, **When** 3 files changed since then, **Then** `plan_build(target_hash=manifest-abc)` returns those 3 files only
2. **Given** no files changed since previous build, **When** `plan_build` is called with current manifest hash, **Then** system returns `status: "unchanged"` with empty file list
3. **Given** first build (no previous manifest), **When** `plan_build` is called without target_hash, **Then** system returns all files in book

---

### Edge Cases

- **Storage backend timeout during write**: What happens if R2 times out mid-write? System must not leave partial journal state; transaction rolls back atomically
- **Journal-storage desync**: What if journal says file exists but R2 doesn't have it? Health check detects desync, logs warning, triggers repair workflow
- **Concurrent overlay writes**: What if two processes write same user overlay simultaneously? Standard hash conflict detection applies to overlays
- **Archive of empty book**: What happens when archiving a book with no content? Return empty archive with metadata, not error
- **User with no overlays**: Reading with user_id but no overlays exist? All reads fall through to base (no special handling needed)
- **Schema validation vs migration**: What if existing files don't match new schema? Migration script, not runtime rejection, handles historical files

---

## Requirements *(mandatory)*

### Functional Requirements

**Metadata Journal (PostgreSQL/SQLite)**

- **FR-001**: System MUST maintain a file journal table with columns: `(book_id, path, user_id, sha256, last_written_at, storage_backend)` where `user_id` defaults to `"__base__"` for shared content
- **FR-002**: All `write_content` operations MUST record journal entry BEFORE returning success; if journal write fails, storage write MUST be rolled back
- **FR-003**: `write_content` with `expected_hash` parameter MUST reject if journal hash doesn't match, returning `CONFLICT` error with current hash
- **FR-004**: `write_content` without `expected_hash` on existing path MUST be rejected with `HASH_REQUIRED` error (no blind overwrites in production)
- **FR-005**: `write_content` without `expected_hash` on non-existent path MUST succeed as create operation
- **FR-006**: System MUST support PostgreSQL (asyncpg) in production and SQLite (aiosqlite) for local development, switchable via `DATABASE_URL` environment variable

**Schema Enforcement**

- **FR-007**: System MUST validate all content paths against regex: `content/{NN-Name}/{NN-Name}/{NN-name}(.summary)?.md` where `NN` is two digits
- **FR-008**: System MUST validate all asset paths against regex: `static/(img|slides|videos|audio)/{path}`
- **FR-009**: System MUST reject paths containing `..`, leading `/`, or null bytes with `INVALID_PATH` error
- **FR-010**: System MUST provide `validate_book_structure` tool that scans entire book and reports schema violations

**Archive Streaming**

- **FR-011**: `get_book_archive` MUST use chunked streaming with maximum 64MB memory buffer regardless of book size
- **FR-012**: `get_book_archive` MUST complete within 60 seconds for books up to 500 files / 200MB (SC-001)
- **FR-013**: `get_book_archive` MUST support `scope` parameter: `content` (markdown only), `assets` (static only), `all` (entire book)
- **FR-014**: If archive generation exceeds timeout, system MUST return partial result with error manifest listing failed files

**Personalization Overlays**

- **FR-015**: System MUST support user-specific content at namespace `books/{book}/users/{user_id}/content/...`
- **FR-016**: `read_content` with `user_id` parameter MUST check overlay first, fall back to base if overlay doesn't exist
- **FR-017**: `write_content` with `user_id` parameter MUST write to overlay namespace, not base
- **FR-018**: `delete_content` on overlay MUST only delete overlay, never affect base content
- **FR-019**: Overlay paths MUST mirror base paths exactly (same schema validation applies)

**Audit Provenance**

- **FR-020**: All operations MUST log audit entry with: `(id, timestamp, agent_id, operation, book_id, path, prev_hash, new_hash, user_id, status, error_message, execution_time_ms)`
- **FR-021**: `agent_id` MUST be provided by caller (extracted from auth token or MCP context); system MUST reject operations with missing agent_id
- **FR-022**: Audit entries for same `(book_id, path, user_id)` MUST maintain hash chain: `entry[n].new_hash == entry[n+1].prev_hash`
- **FR-023**: Audit log MUST be append-only via database INSERT (no read-modify-write pattern)
- **FR-024**: System MUST support audit queries filtered by: date range, agent_id, operation type, book_id, path pattern

**Docusaurus Contract**

- **FR-025**: System MUST provide `plan_build(book_id, target_manifest_hash?)` tool that returns files changed since target manifest
- **FR-026**: `plan_build` response MUST include: `{status: "unchanged"|"changed", files: [{path, current_hash, target_hash}], manifest_hash}`
- **FR-027**: Hydration script MUST be able to download only changed files using `plan_build` response

**Database Configuration**

- **FR-028**: System MUST connect to PostgreSQL when `DATABASE_URL` environment variable is set (format: `postgresql+asyncpg://user:pass@host/db`)
- **FR-029**: System MUST fall back to SQLite at `./panaversity_fs.db` when `DATABASE_URL` is not set
- **FR-030**: System MUST use SQLAlchemy 2.0 async with Alembic migrations for schema management
- **FR-031**: System MUST create tables automatically on first run if they don't exist

### Key Entities

- **FileJournal**: Tracks current state of every file `(book_id, path, user_id, sha256, last_written_at, storage_backend)`. Primary key is `(book_id, path, user_id)`. Used for conflict detection and delta builds.
- **AuditLog**: Append-only record of all operations `(id, timestamp, agent_id, operation, book_id, path, prev_hash, new_hash, user_id, status, ...)`. Maintains hash chain for provenance.
- **Book**: Logical container identified by `book_id`. Contains content (lessons, summaries) and assets (images, slides). May have user overlays.
- **Overlay**: User-specific variant of base content. Stored at `users/{user_id}/content/...` namespace. Falls through to base when not present.

### Agent Contract: Hash-Based Updates

**Agents MUST follow this protocol for write operations:**

```
IF file exists:
    1. Read current file to get file_hash from response
    2. Call write_content WITH expected_hash=<that hash>
    3. Handle CONFLICT → re-read, merge, retry

IF file does NOT exist:
    1. Call write_content WITHOUT expected_hash
    2. System creates file, returns new hash

FORBIDDEN:
    - write_content on existing file WITHOUT expected_hash → HASH_REQUIRED error
    - write_content WITH expected_hash on non-existent file → NOT_FOUND error
```

This explicit contract ensures agents always know whether they're creating or updating content, and concurrent writes are detected rather than silently overwritten.

### Manifest Hash Computation

**Definition**: A manifest hash uniquely identifies the state of a book's content at a point in time.

**Computation Algorithm**:
```python
def compute_manifest_hash(book_id: str, journal_entries: list[FileJournal]) -> str:
    """
    Compute deterministic manifest hash from FileJournal state.

    1. Filter: Only entries matching book_id with user_id="__base__"
    2. Sort: Lexicographically by path (stable ordering)
    3. Concatenate: "{path}:{sha256}\n" for each entry
    4. Hash: SHA256 of concatenated string
    """
    base_entries = [e for e in journal_entries
                    if e.book_id == book_id and e.user_id == "__base__"]
    base_entries.sort(key=lambda e: e.path)

    manifest_string = "\n".join(f"{e.path}:{e.sha256}" for e in base_entries)
    return hashlib.sha256(manifest_string.encode()).hexdigest()
```

**Properties**:
- **Deterministic**: Same journal state always produces same hash
- **Collision-resistant**: Different states produce different hashes
- **Excludes overlays**: Only base content contributes to manifest (overlays are per-user)

**Usage in `plan_build`**:
- Client stores `manifest_hash` after successful build
- Next build: calls `plan_build(book_id, target_manifest_hash=<stored>)`
- Server compares current manifest to target, returns delta

### Shared Path Validation

**Requirement**: Path validation logic MUST be centralized in a shared helper module to ensure consistent behavior across:
- Content write operations
- Overlay namespace resolution
- Schema validation tool
- Test fixtures

**Canonical Implementation Location**: `panaversity_fs/path_utils.py`

**Interface**:
```python
# Core validators (return ValidationResult with errors list)
def validate_content_path(path: str) -> ValidationResult
def validate_asset_path(path: str) -> ValidationResult
def validate_overlay_path(path: str, user_id: str) -> ValidationResult

# Pattern constants (compiled regexes for reuse)
CONTENT_PATH_PATTERN: re.Pattern  # content/{NN-Name}/{NN-Name}/{NN-name}(.summary)?.md
ASSET_PATH_PATTERN: re.Pattern    # static/(img|slides|videos|audio)/{path}
OVERLAY_PATH_PATTERN: re.Pattern  # users/{user_id}/content/...

# Path utilities
def extract_user_id_from_overlay(path: str) -> str | None
def convert_base_to_overlay(base_path: str, user_id: str) -> str
def convert_overlay_to_base(overlay_path: str) -> str
```

**Rationale**: Prevents divergent validation logic that could allow invalid paths through one code path while rejecting them in another.

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Books up to 500 files / 200MB archive within 60 seconds with <64MB server memory (R4 invariant)
- **SC-002**: All write operations record journal entry atomically; zero orphaned storage writes after any failure
- **SC-003**: Conflict detection accuracy is 100%; no silent overwrites when `expected_hash` mismatches
- **SC-004**: Audit hash chain integrity: for any file, consecutive audit entries satisfy `entry[n].new_hash == entry[n+1].prev_hash`
- **SC-005**: Schema validation rejects 100% of invalid paths; zero stray files created in production
- **SC-006**: Personalized reads return overlay content when present with <10ms additional latency vs base read
- **SC-007**: Delta build detection returns only changed files; full rebuild only required when explicitly requested
- **SC-008**: System operates identically on PostgreSQL (production) and SQLite (development) with same test suite passing
- **SC-009**: Agent operations are traceable: 100% of audit entries have actual agent_id (not "system")
- **SC-010**: R2 backend achieves 99.9% operation success rate with automatic retry on transient failures

### Instrumentation Requirements

**For measurable success criteria, implement instrumentation hooks BEFORE features:**

| Success Criteria | Required Metric | Hook Location |
|-----------------|-----------------|---------------|
| SC-001 | `archive_duration_ms`, `archive_memory_bytes` | `get_book_archive` entry/exit |
| SC-002 | `journal_write_success`, `storage_rollback_count` | `write_content` transaction wrapper |
| SC-004 | `audit_chain_valid`, `audit_chain_broken_count` | Health check periodic scan |
| SC-007 | `delta_files_count`, `full_rebuild_count` | `plan_build` response |

**Prometheus Metrics Format**:
```python
# Counters
panaversityfs_write_total{status="success|conflict|error", mode="create|update"}
panaversityfs_archive_total{scope="content|assets|all", status="success|timeout|error"}

# Histograms
panaversityfs_archive_duration_seconds{scope="content|assets|all"}
panaversityfs_write_duration_seconds{operation="journal|storage|total"}

# Gauges
panaversityfs_archive_memory_bytes
panaversityfs_journal_entries_total{book_id="*"}
```

**Implementation Order**: Plan must schedule instrumentation setup in early tasks so metrics are available for validation testing.

---

## Non-Goals *(explicit scope boundaries)*

- **Content versioning/rollback**: Audit trail provides history but not version control. No git-like branching, diffing, or rollback UI. External tools can use audit log for recovery.
- **Real-time collaboration**: No WebSocket presence, live cursors, or operational transformation. System assumes asynchronous agent workflows.
- **Multi-tenancy**: Single-tenant (Panaversity). No organization isolation, tenant-scoped registries, or billing separation.
- **AI-powered content generation**: PanaversityFS stores content; it does not generate summaries, translations, or adaptations. External agents perform intelligence operations.
- **Vector search**: No semantic/embedding search. Grep/glob pattern search is sufficient for current use cases.
- **Asset transformation**: No image resizing, video transcoding, or format conversion. Assets stored as-is.
- **CDN cache invalidation**: System generates CDN URLs; cache management is external (Cloudflare handles this automatically).

---

## Assumptions

- **PostgreSQL availability**: Production environment has managed PostgreSQL (Neon, Supabase, or RDS) accessible via `DATABASE_URL`
- **SQLAlchemy 2.0 maturity**: Async SQLAlchemy with asyncpg/aiosqlite is production-ready for our workload
- **Alembic migrations**: Schema changes will be managed through Alembic; no manual DDL in production
- **OpenDAL streaming**: OpenDAL Python bindings support chunked reads for R2 (verified in POC)
- **MCP context**: MCP protocol provides agent identification that can be extracted for audit logging
- **UTF-8 encoding**: All markdown content is UTF-8; other encodings are rejected
- **Idempotent deletes**: Deleting non-existent file returns success (no error, operation is no-op)

---

## Risks & Mitigations

**Risk 1: Journal-storage desync after partial failure**
- **Likelihood**: Low (atomic transactions)
- **Impact**: High (data integrity)
- **Mitigation**: Database transaction wraps both journal update and storage write. If either fails, both roll back. Health check periodically compares journal to storage and logs discrepancies.

**Risk 2: PostgreSQL connection pool exhaustion under load**
- **Likelihood**: Medium (many concurrent agents)
- **Impact**: Medium (degraded performance, not data loss)
- **Mitigation**: Configure appropriate pool size (default 5, max 20). Use connection timeout. Monitor pool metrics. Implement request queuing if needed.

**Risk 3: Schema migration breaks existing content**
- **Likelihood**: Low (Alembic tracks migrations)
- **Impact**: High (content inaccessible)
- **Mitigation**: Always create reversible migrations. Test migrations against production data snapshot. Never delete columns, only add nullable or deprecate.

**Risk 4: Overlay namespace collision**
- **Likelihood**: Low (user_id is unique)
- **Impact**: Medium (wrong content served)
- **Mitigation**: Validate user_id format (alphanumeric + hyphens, no special chars). Log all overlay operations for debugging.

---

## Formal Verification (Alloy-Style Invariants)

These invariants MUST hold at all times. Small-scope testing (3-5 instances) should verify each.

**Usage in Planning**: These Alloy snippets are concrete enough to:
1. Generate property-based tests (pytest + hypothesis)
2. Define database constraints (CHECK, TRIGGER)
3. Guide integration test assertions

---

### R1: Deterministic Book Schema

**Alloy Model**:
```alloy
sig Path {
  segments: seq String
}

sig ContentPath extends Path {}

pred validContentPath[p: ContentPath] {
  #p.segments = 4
  p.segments[0] = "content"
  p.segments[1].matches["[0-9]{2}-[A-Za-z-]+"]
  p.segments[2].matches["[0-9]{2}-[A-Za-z-]+"]
  p.segments[3].matches["[0-9]{2}-[a-z-]+(\\.summary)?\\.md"]
}

assert SchemaEnforced {
  all p: ContentPath | validContentPath[p]
}
check SchemaEnforced for 5
```

**Small-scope test**: 3 files with paths `["valid", "invalid-no-prefix", "traversal/../attack"]`
**Pytest assertion**: `assert all(validate_content_path(p).is_valid for p in valid_paths)`

---

### R2: Hash Journal Integrity

**Alloy Model**:
```alloy
sig FileJournal {
  book_id: String,
  path: String,
  user_id: String,
  sha256: String
}

sig Storage {
  files: path -> lone Bytes
}

pred journalStorageConsistent[j: FileJournal, s: Storage] {
  all entry: j | {
    let stored = s.files[entry.path] |
    some stored implies entry.sha256 = sha256(stored)
  }
}

assert JournalMatchesStorage {
  all j: FileJournal, s: Storage | journalStorageConsistent[j, s]
}
check JournalMatchesStorage for 5
```

**Small-scope test**: 5 files with sequence `[write, read, write, delete, write]`
**Pytest assertion**: `assert journal.get(path).sha256 == sha256(storage.read(path))`

---

### R3: Idempotent Delete

**Alloy Model**:
```alloy
pred deleteOperation[j, j': FileJournal, s, s': Storage, path: String] {
  -- Post-state: path removed from both journal and storage
  j' = j - {e: j | e.path = path}
  s'.files = s.files - (path -> Bytes)

  -- Idempotent: deleting non-existent is no-op
  (no {e: j | e.path = path}) implies (j' = j and s' = s)
}

assert DeleteIdempotent {
  all j: FileJournal, s: Storage, path: String |
    let j', s' = deleteOperation[j, s, path] |
    let j'', s'' = deleteOperation[j', s', path] |
    j' = j'' and s' = s''
}
check DeleteIdempotent for 3
```

**Small-scope test**: 3 files, call `delete(path)` twice on same path
**Pytest assertion**: `assert delete_content(path).status == "success"` (both times)

---

### R4: Archive Throughput Bound

**Alloy Model**:
```alloy
sig Book {
  files: set File,
  totalSize: Int
}

pred archiveCompletes[b: Book, timeout: Int] {
  #b.files <= 500 and b.totalSize <= 200_000_000 implies
    archiveTime[b] < timeout
}

assert ArchivePerformance {
  all b: Book | archiveCompletes[b, 60]
}
-- Note: Performance bounds verified empirically, not symbolically
```

**Small-scope test**: Synthetic book with exactly 500 files, 200MB total
**Pytest assertion**: `assert archive_duration_seconds < 60`

---

### R5: Overlay Exclusivity

**Alloy Model**:
```alloy
sig User {}
sig Lesson {
  base: Bytes,
  overlays: User -> lone Bytes
}

fun readContent[lesson: Lesson, user: User]: Bytes {
  user in lesson.overlays.User implies lesson.overlays[user]
  else lesson.base
}

assert OverlayOrBase {
  all l: Lesson, u: User |
    readContent[l, u] = l.overlays[u] or
    (no l.overlays[u] and readContent[l, u] = l.base)
}
check OverlayOrBase for 3 Lesson, 3 User
```

**Small-scope test**: 2 users, 2 lessons, overlay exists for user1/lesson1 only
**Pytest assertion**:
```python
assert read_content(lesson1, user1) == overlay_content
assert read_content(lesson1, user2) == base_content
assert read_content(lesson2, user1) == base_content
```

---

### R6: Audit Hash Chain

**Alloy Model**:
```alloy
sig AuditEntry {
  path: String,
  prev_hash: lone String,
  new_hash: String,
  timestamp: Int
}

pred hashChainValid[entries: seq AuditEntry] {
  all i: Int | i >= 0 and i < (#entries - 1) implies {
    let curr = entries[i], next = entries[i+1] |
    curr.new_hash = next.prev_hash
  }
}

assert AuditChainIntegrity {
  all path: String |
    let entries = {e: AuditEntry | e.path = path}.sortBy[timestamp] |
    hashChainValid[entries]
}
check AuditChainIntegrity for 5
```

**Small-scope test**: 4 consecutive operations on same path
**Pytest assertion**:
```python
entries = audit_log.query(path=path, order_by="timestamp")
for i in range(len(entries) - 1):
    assert entries[i].new_hash == entries[i+1].prev_hash
```

---

### R7: Agent Provenance

**Alloy Model**:
```alloy
sig AuditEntry {
  agent_id: String
}

pred validAgentId[entry: AuditEntry] {
  entry.agent_id != "system"
  entry.agent_id != ""
  some entry.agent_id
}

assert AllEntriesHaveAgent {
  all e: AuditEntry | validAgentId[e]
}
check AllEntriesHaveAgent for 10
```

**Small-scope test**: 5 operations from different agent contexts
**Pytest assertion**: `assert all(e.agent_id not in ["system", "", None] for e in audit_entries)`
**DB constraint**: `CHECK (agent_id IS NOT NULL AND agent_id != 'system' AND agent_id != '')`

---

## Dependencies

**Runtime Dependencies**:
- SQLAlchemy 2.0+ (async ORM)
- asyncpg (PostgreSQL async driver)
- aiosqlite (SQLite async driver)
- Alembic (migrations)
- OpenDAL (storage abstraction) - existing
- FastMCP (MCP server) - existing
- Pydantic 2.0+ (validation) - existing

**Infrastructure**:
- PostgreSQL 15+ (production) - Neon/Supabase/RDS
- Cloudflare R2 (object storage) - existing
- SQLite (local development) - built into Python

**Development Tools**:
- pytest-asyncio (async testing) - existing
- pytest-postgresql (integration tests with real PG)
