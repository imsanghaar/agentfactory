# claude-mem Architecture Reference

## Overview

claude-mem is a persistent memory system for Claude Code that automatically captures session activity, compresses it with AI, and injects relevant context into future sessions.

## Installation

```bash
> /plugin marketplace add thedotmack/claude-mem
> /plugin install claude-mem
# Restart Claude Code
```

## Requirements

- Node.js 18.0.0+
- Claude Code with plugin support
- Bun runtime (auto-installed)
- SQLite 3 (bundled)

## Architecture Components

### 1. Lifecycle Hooks (5 events)

| Hook | When Triggered | Purpose |
|------|---------------|---------|
| SessionStart | Session begins | Initialize memory context |
| UserPromptSubmit | User sends message | Capture user input patterns |
| PostToolUse | After tool execution | Record tool outcomes |
| Stop | Pause processing | Handle interrupts |
| SessionEnd | Session ends | Generate semantic summaries |

### 2. Worker Service

- **HTTP API**: Port 37777
- **Web Viewer UI**: http://localhost:37777
- **Purpose**: Serve memory queries, display observation browser

### 3. Storage Layer

**SQLite Database**:
- Sessions table
- Observations table
- Summaries table

**Chroma Vector DB**:
- Hybrid semantic + keyword search
- Embeddings for retrieval

### 4. mem-search Skill

Natural language query interface for memory retrieval.

## 3-Layer Token-Efficient Retrieval

The key innovation: progressive disclosure to minimize token usage.

### Layer 1: Search Index

```typescript
search(query="authentication bug", type="bugfix", limit=10)
```

- Returns compact results (~50-100 tokens/result)
- Contains observation IDs, timestamps, brief summaries
- Purpose: Filter to relevant observations

### Layer 2: Timeline Context

```typescript
timeline(observation_id=123, context_window=5)
```

- Returns chronological context around observation
- Shows sequence of events before/after
- Purpose: Understand observation in context

### Layer 3: Full Details

```typescript
get_observations(ids=[123, 456])
```

- Returns complete observation content (~500-1,000 tokens/result)
- Only fetched for filtered, relevant observations
- Purpose: Deep dive when needed

### Token Savings

Traditional approach: Fetch everything → 10,000+ tokens
3-Layer approach: Progressive filter → ~1,000 tokens

**Result**: ~10x token savings

## Privacy Controls

### Private Tags

```markdown
<private>
API_KEY=secret123
Database credentials here
Sensitive project information
</private>
```

Content inside `<private>` tags is:
- Excluded from long-term memory storage
- Not indexed for retrieval
- Not included in session summaries

### Fine-Grained Control

Users control what context gets injected:
- Query by type (bugfix, feature, conversation)
- Filter by date range
- Exclude specific observations

## Observation Types

| Type | Example | Storage Priority |
|------|---------|-----------------|
| bugfix | Error resolution | High |
| feature | New functionality | High |
| refactor | Code improvement | Medium |
| conversation | Discussion | Medium |
| exploration | Code browsing | Low |

## Web Viewer

Access at http://localhost:37777

Features:
- Browse all sessions
- View observations chronologically
- Search across history
- Export/import memory
- Delete observations

## Hook Implementation

### SessionStart Hook

```json
{
  "event": "session_start",
  "timestamp": "2025-01-20T10:00:00Z",
  "session_id": "sess_abc123",
  "project_path": "/path/to/project"
}
```

### UserPromptSubmit Hook

```json
{
  "event": "user_prompt_submit",
  "timestamp": "2025-01-20T10:01:00Z",
  "session_id": "sess_abc123",
  "prompt": "Fix the authentication bug",
  "context": {
    "current_file": "auth.py",
    "recent_files": ["config.py", "main.py"]
  }
}
```

### PostToolUse Hook

```json
{
  "event": "post_tool_use",
  "timestamp": "2025-01-20T10:02:00Z",
  "session_id": "sess_abc123",
  "tool": "Edit",
  "target": "auth.py",
  "result": "success",
  "changes_summary": "Added JWT validation"
}
```

### SessionEnd Hook

```json
{
  "event": "session_end",
  "timestamp": "2025-01-20T11:00:00Z",
  "session_id": "sess_abc123",
  "summary": "Fixed JWT authentication bug in auth.py",
  "observations_count": 15,
  "tools_used": ["Read", "Edit", "Bash"]
}
```

## Database Schema

### Sessions Table

```sql
CREATE TABLE sessions (
  id TEXT PRIMARY KEY,
  started_at DATETIME,
  ended_at DATETIME,
  project_path TEXT,
  summary TEXT,
  observation_count INTEGER
);
```

### Observations Table

```sql
CREATE TABLE observations (
  id INTEGER PRIMARY KEY,
  session_id TEXT,
  timestamp DATETIME,
  type TEXT,
  content TEXT,
  embedding BLOB,
  metadata JSON,
  FOREIGN KEY (session_id) REFERENCES sessions(id)
);
```

### Summaries Table

```sql
CREATE TABLE summaries (
  id INTEGER PRIMARY KEY,
  session_id TEXT,
  created_at DATETIME,
  summary TEXT,
  key_decisions TEXT,
  files_modified TEXT,
  FOREIGN KEY (session_id) REFERENCES sessions(id)
);
```

## Integration with Claude Code

claude-mem operates automatically:

1. **No manual intervention** - hooks capture activity silently
2. **Context injection** - relevant history injected at session start
3. **Progressive disclosure** - only fetch what's needed
4. **Privacy-aware** - respects `<private>` boundaries

## License

- Main project: AGPL-3.0
- ragtime/ directory: PolyForm Noncommercial License 1.0.0
