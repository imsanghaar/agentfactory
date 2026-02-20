### Core Concept
Context is dependency-injected, not passed as parameter. FastMCP automatically provides Context with logging (info/warning/error), progress reporting (report_progress), and session access. Server lifecycle uses on_startup/on_shutdown for resource management.

### Key Mental Models
- **Dependency injection**: Context is special parameter after `*` separator—NOT in tool schema
- **Per-request isolation**: Each tool invocation gets its own Context; concurrent tools don't interfere
- **Lifecycle guarantees**: on_startup runs BEFORE accepting connections; on_shutdown runs at server stop
- **Restaurant kitchen analogy**: Chefs focus on cooking (domain logic), restaurant provides tools/timers (Context)

### Critical Patterns
- Context injection: `async def tool(query: str, *, context: Context)`
- Logging levels: `await context.info()`, `await context.warning()`, `await context.error()`
- Progress: `await context.report_progress(completed, total)`
- Session access: `context.session.session_id`
- Lifecycle: `@mcp.on_startup` and `@mcp.on_shutdown` decorators

### AI Collaboration Keys
- Context provides logging, progress, session—all automatically wired
- Log BEFORE and AFTER significant operations for debugging
- Progress prevents client timeout on long operations

### Common Mistakes
- Passing Context as explicit parameter (should be after `*` separator)
- Forgetting Context is per-request, not global
- Not using lifecycle handlers for resource initialization/cleanup

### Connections
- **Builds on**: Build Your MCP Server Skill (Lesson 0)
- **Leads to**: Sampling — Servers Calling LLMs (Lesson 2)
