### Core Concept
File checkpointing snapshots file state at execution checkpoints. Enable with `enable_file_checkpointing=True`, capture checkpoint UUIDs from UserMessage objects, and use `rewindFiles(checkpoint_id)` to recover from agent mistakes instantly.

### Key Mental Models
- **Resilience through reversibility**: Agents can be bold and exploratory because failure is instantly recoverable
- **Checkpoint = file state snapshot**: Each tool execution creates a new checkpoint UUID
- **Recovery pattern**: Detect error → rewindFiles(last_good_checkpoint) → try different approach

### Critical Patterns
- Enable checkpointing: `enable_file_checkpointing=True, extra_args={"replay-user-messages": None}`
- Capture UUIDs: `if isinstance(message, UserMessage) and message.uuid: checkpoint = message.uuid`
- Recover: `await client.rewind_files(checkpoint_id)`
- Multi-approach: Checkpoint baseline → try approach A → rewind → try approach B → compare

### AI Collaboration Keys
- Checkpoint BEFORE risky operations (major refactorings, architectural changes)
- Store checkpoint IDs semantically: `checkpoints["before_auth_refactor"] = uuid`
- Checkpoints persist across session boundaries—save both session_id and checkpoint_id

### Common Mistakes
- Missing `replay-user-messages` flag (can't access checkpoint UUIDs)
- Not capturing baseline checkpoint before risky operations
- Forgetting to save checkpoint IDs for long-running sessions

### Connections
- **Builds on**: Session Management (Lesson 7)
- **Leads to**: Subagents with Task Tool (Lesson 9)
