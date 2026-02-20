### Core Concept
MCP debugging requires systematic diagnosis across three failure layers: server startup, tool discovery, and tool execution. The MCP Inspector is the primary tool—connect, list tools, test invocations, verify error messages before production deployment.

### Key Mental Models
- **Three failure layers**: Startup (process won't launch), Discovery (tools don't appear), Execution (calls fail)
- **stdio vs HTTP debugging**: stdio needs stderr logging (stdout = protocol); HTTP needs network inspection
- **Inspector workflow**: Start → Connect → List Tools → Test → Verify error messages
- **Decision tree**: Server starts? → Tools appear? → Calls succeed? → Results correct?

### Critical Patterns
- Inspector launch: `mcp dev your_server.py` (Python) or `npx @modelcontextprotocol/inspector server.js` (Node)
- stdio logging: `logging.basicConfig(stream=sys.stderr)` (NEVER stdout)
- JSON-RPC errors: `{"error": {"code": -32602, "message": "Invalid params"}}`
- Common errors: Connection refused, Tool not found, Invalid arguments, Authentication failed

### AI Collaboration Keys
- Inspector isolates MCP server from client—test tools before integration
- Raw JSON-RPC responses reveal protocol-level issues
- Error code -32602 = parameter validation; -32600 = invalid request

### Common Mistakes
- Logging to stdout in stdio servers (breaks protocol stream)
- Not setting environment variables before running Inspector
- Skipping Inspector workflow and debugging in production

### Connections
- **Builds on**: Using Community MCP Servers (Lesson 7)
- **Leads to**: Chapter Quiz (Lesson 9)
