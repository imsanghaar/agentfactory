### Core Concept
Sessions are persistent conversation contexts. Capture `session_id` from init messages, resume later with full context preserved. Session forking creates independent branches for parallel exploration—explore approach A and B simultaneously while keeping the original at a checkpoint.

### Key Mental Models
- **Session lifecycle**: Init (new session_id) → Resume (context restored) → Fork (parallel branches)
- **Forking power**: Instead of choosing blindly, fork the session and explore multiple paths
- **Digital FTE continuity**: Sessions let agents work across days/weeks, accumulating expertise

### Critical Patterns
- Capture session_id: `if message.subtype == 'init': session_id = message.session_id`
- Resume session: `ClaudeAgentOptions(resume=session_id)`
- Fork pattern: Create `fork_a = session_id + "_fork_indexing"`, resume with fork ID
- Long-running agent: Store session_id to file, reload on restart

### AI Collaboration Keys
- Use forking for A/B testing approaches before committing
- Store critical decisions in database, session for conversation context
- Session handoff: Transfer session_id to specialist agent with different system_prompt

### Common Mistakes
- Not capturing session_id from init messages
- Storing sensitive data in sessions instead of encrypted databases
- Forgetting to save session_id for long-running agents (lost on crash)

### Connections
- **Builds on**: Custom Slash Commands (Lesson 6)
- **Leads to**: File Checkpointing (Lesson 8)
