### Core Concept
Sessions transform chatbots into relationships—automatically maintaining conversation history across multiple interactions so agents remember context without manual history management.

### Key Mental Models
- **Session = Notebook**: Automatically saves every exchange between user and agent
- **SQLiteSession vs AdvancedSQLiteSession**: Simple memory vs production analytics and branching
- **One Agent, Many Sessions**: Same agent instance serves multiple customers, each with their own persistent context

### Critical Patterns
- Basic session: `SQLiteSession(session_id, db_path="conversations.db")`
- Pass to runner: `Runner.run(agent, message, session=session)`
- Advanced tracking: `AdvancedSQLiteSession` with `store_run_usage(result)` for metrics
- Get history: `session.get_items(limit=3)` for recent messages
- Branching: `session.create_branch_from_turn(1)` to explore alternatives

### AI Collaboration Keys
- Use file-based sessions (`db_path`) for production persistence across restarts
- Track token usage with `get_session_usage()` to optimize costs

### Common Mistakes
- Using in-memory sessions in production (data lost on restart)
- Forgetting to pass `session=session` to `Runner.run()` (no memory)
- Not tracking usage metrics with `store_run_usage()` when you need cost optimization

### Connections
- **Builds on**: Guardrails and validation (Lesson 5)
- **Leads to**: Tracing and observability (Lesson 7)
