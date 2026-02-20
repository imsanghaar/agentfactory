### Core Concept
Long operations need continuous feedback. Without notifications, client UI freezes and users cancel. Progress notifications (quantified: "50% complete") and logging (qualitative: "Processing file...") keep clients informed during multi-second operations.

### Key Mental Models
- **Frozen UX problem**: 30-second operation with no feedback feels like crash
- **Progress semantics**: `report_progress(completed, total)` where completed = done count, not remaining
- **Severity levels**: info() = milestones, warning() = recoverable issues, error() = failures
- **Update frequency**: Every 5-10% or 1-2 seconds—not every 1%, not every 50%

### Critical Patterns
- Progress: `await context.report_progress(i + 1, total)` in loops
- Logging: `await context.info()`, `await context.warning()`, `await context.error()`
- Deterministic progress: Known total → use report_progress
- Indeterminate progress: Unknown total → use context.info() for checkpoints
- Multi-phase: Combine logging (phase transitions) with progress (within phases)

### AI Collaboration Keys
- Short operations (&lt;2 seconds): Skip notifications—overhead exceeds benefit
- Long operations: Report progress to prevent client timeout
- Error logging: Always log BEFORE raising exceptions

### Common Mistakes
- Using error() for expected conditions (use info() instead)
- Updating progress too frequently (floods client, degrades performance)
- Not logging before failure (can't debug production issues)

### Connections
- **Builds on**: Sampling — Servers Calling LLMs (Lesson 2)
- **Leads to**: Roots: File System Permissions (Lesson 4)
