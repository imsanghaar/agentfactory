### Core Concept
MCP (Model Context Protocol) lets agents connect to remote tool ecosystems via a standard protocol. Instead of hardcoding integrations, agents discover and use tools from MCP servers automatically through `mcp_servers=[server]`.

### Key Mental Models
- **Integration becomes configuration**: Custom code → Standard protocol. Connect once, use all tools
- **Compose tool ecosystems**: Multiple MCP servers contribute tools that agents intelligently select
- **Async lifecycle management**: `async with MCPServerStreamableHttp(...) as server` handles connection/cleanup

### Critical Patterns
- Connect to MCP: `async with MCPServerStreamableHttp(name, url, headers) as server`
- Add to agent: `Agent(mcp_servers=[server1, server2])`
- Context7 documentation: `resolve-library-id` → `get-library-docs` for current API references
- Authentication via headers: `headers={"Authorization": f"Bearer {token}"}`

### AI Collaboration Keys
- Let agents discover tools naturally—don't hardcode "call this first, then that"
- Use Context7 to ground agent responses in current documentation, not stale training data

### Common Mistakes
- Forgetting to use `async with` for connection lifecycle (connection leaks)
- Not explaining available tools in agent instructions (agent doesn't know capabilities)
- Using MCP for internal logic (it's for external integrations—use custom tools for internal)

### Connections
- **Builds on**: Tracing and observability (Lesson 7)
- **Leads to**: RAG with FileSearchTool (Lesson 9)
