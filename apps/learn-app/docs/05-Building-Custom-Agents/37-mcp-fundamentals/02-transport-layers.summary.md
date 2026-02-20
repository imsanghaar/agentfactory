### Core Concept
MCP's transport agnosticism means your server code doesn't change when switching from local development (stdio) to production deployment (HTTP). JSON-RPC messages are identical whether traveling through subprocess streams or HTTP requests—only configuration changes.

### Key Mental Models
- **Transport independence**: Protocol (JSON-RPC) is separate from delivery mechanism (stdio/HTTP)
- **stdio = local**: Subprocess communication via stdin/stdout for single-client desktop scenarios
- **Streamable HTTP = remote**: HTTP POST for cloud/multi-client; stateless (JSON) or stateful (SSE for streaming)
- **Stream discipline**: Messages → stdout, Logs → stderr (violating this corrupts the protocol)

### Critical Patterns
- stdio config: `"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem"]`
- Log redirection: `print("message", file=sys.stderr)` not `print("message")`
- HTTP modes: Stateless for serverless/horizontal scaling; Stateful SSE for progress updates
- Latency: stdio &lt;1ms (local IPC); HTTP 10-100ms (network)

### AI Collaboration Keys
- Development → stdio (simple, automatic subprocess); Production → HTTP (scalable, multi-client)
- Same tool implementation works with both transports
- Switch transport via configuration, not code changes

### Common Mistakes
- Logging to stdout in stdio servers (breaks JSON-RPC protocol stream)
- Using stateful HTTP when stateless would scale better
- Forgetting HTTP requires authentication (stdio assumes trusted localhost)

### Connections
- **Builds on**: MCP Architecture Overview (Lesson 1)
- **Leads to**: Tools: The Model-Controlled Primitive (Lesson 3)
