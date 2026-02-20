### Core Concept
Custom tools extend agent capabilities into specialized domains. Use @tool decorator with async functions, create servers with create_sdk_mcp_server, register in allowed_tools using mcp__<server>__<toolname> convention.

### Key Mental Models
- **Tools as security boundary**: Invalid input is your responsibility to handle
- **@tool decorator anatomy**: name, description, input schema (type hints)
- **MCP response format**: `{"content": [{"type": "text", "text": "..."}], "isError": True/False}`

### Critical Patterns
- Define tool: `@tool("get_stock_price", "Get current price", {"symbol": str})`
- Input validation layers: schema validation → format validation → resource limits → execution
- Error handling: Return `isError: True` with actionable message, never raise exceptions
- Tool granularity: Neither god-tool (too coarse) nor over-fragmented (too fine)

### AI Collaboration Keys
- Create custom tools when accessing external systems, requiring auth, or calling frequently
- Keep secrets server-side in tools, never expose to agent
- Design tools as if called by untrusted code—validate strictly

### Common Mistakes
- Using Bash for API calls instead of custom tools (exposes credentials)
- Creating god-tools with operation parameter instead of focused tools
- Forgetting isError flag (agent assumes success on failure)

### Connections
- **Builds on**: Lifecycle Hooks (Lesson 10)
- **Leads to**: ClaudeSDKClient and Streaming (Lesson 12)
