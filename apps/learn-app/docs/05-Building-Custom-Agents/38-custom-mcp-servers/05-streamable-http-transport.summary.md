### Core Concept
stdio is local-only; remote MCP needs HTTP. StreamableHTTP uses dual-connection pattern: POST for client→server requests, GET/SSE for server→client streaming. Session IDs bind connections together.

### Key Mental Models
- **HTTP asymmetry**: Client→Server easy (POST), Server→Client hard (HTTP has no native push)
- **SSE solution**: Server-Sent Events enable server-initiated messages without polling
- **Dual connections**: POST /messages for requests, GET /sse/{sessionId} for streaming responses
- **Session lifecycle**: Initialize → Acknowledge → Stream → Communicate → Cleanup

### Critical Patterns
- Session flow: POST /initialize → get mcp-session-id header → POST /notifications/initialized → GET /sse?session_id=X
- FastMCP config: `StreamableHTTP(host="0.0.0.0", port=8000, session_timeout=300, enable_tool_sse=True)`
- Primary SSE: General notifications, tool results, errors
- Tool-specific SSE: Per-tool sampling requests and progress
- Always include sessionId in POST request bodies

### AI Collaboration Keys
- Session ID binds HTTP connections—critical for multi-client scenarios
- Without session ID routing, requests from different clients collide
- StreamableHTTP transforms HTTP into bidirectional MCP communication

### Common Mistakes
- Forgetting to include sessionId in POST requests
- Not configuring session timeouts (stale sessions leak resources)
- Assuming stdio works for remote deployment (it doesn't)

### Connections
- **Builds on**: Roots: File System Permissions (Lesson 4)
- **Leads to**: Stateful vs Stateless Servers (Lesson 6)
