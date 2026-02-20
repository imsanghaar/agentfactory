### Core Concept
Tools are model-controlled functions the AI decides when and how to invoke. Server broadcasts tools via `tools/list`; model discovers them, reasons about when to use each, and invokes via `tools/call`. Define once in MCP, use from any compatible client.

### Key Mental Models
- **Model-controlled**: AI autonomously decides tool invocation—you define what's available, model decides when to use
- **Discovery → Invocation**: `tools/list` returns all tools with schemas; `tools/call` executes specific tool with arguments
- **Universal schema**: JSON Schema inputSchema works across all MCP clients (vs SDK-specific formats)
- **Extensibility**: Add new tool on server → broadcast via tools/list → all clients gain capability

### Critical Patterns
- Naming: `[service]_[action]` pattern (e.g., `github_create_issue`, `database_query_users`)
- Schema structure: `{"name": "...", "description": "...", "inputSchema": {"type": "object", "properties": {...}, "required": [...]}}`
- Annotations: `readOnlyHint: true`, `destructiveHint: true`, `idempotentHint: true`
- FastMCP: `@mcp.tool()` decorator + Pydantic `Field()` for descriptions

### AI Collaboration Keys
- Good descriptions explain WHEN to use tool, not just what it does
- Schema validation prevents invalid arguments before execution
- Annotations help model reason about risks (destructive, read-only)

### Common Mistakes
- Vague tool names like `create_issue` (ambiguous service)
- Missing descriptions (model doesn't know when to use tool)
- Not marking destructive tools (model can't reason about risks)

### Connections
- **Builds on**: Transport Layers (Lesson 2)
- **Leads to**: Resources: The App-Controlled Primitive (Lesson 4)
