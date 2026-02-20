### Core Concept
Model Context Protocol (MCP) solves the integration explosion problem by standardizing how AI applications connect to external systems. One tool definition works across all MCP-compatible platforms—Claude, ChatGPT, Cursor—transforming O(n×m) custom integrations into O(n+m) standardized connections.

### Key Mental Models
- **USB-C for AI**: MCP is universal connectivity—one protocol works with any AI application and any external service
- **Host-Client-Server architecture**: Host (IDE/app) contains Client (connection manager) that talks to Server (tool provider) via JSON-RPC 2.0
- **Three primitives**: Tools (model-controlled actions), Resources (app-controlled data), Prompts (user-controlled templates)
- **Integration math**: 10 apps × 20 services = 200 custom integrations; with MCP = 30 components

### Critical Patterns
- JSON-RPC 2.0 format: `{"jsonrpc": "2.0", "id": 1, "method": "resources/list", "params": {}}`
- Tool schema unification: inputSchema works everywhere (vs OpenAI's `function.parameters`, Anthropic's `input_schema`, Google's `input`)
- Adoption timeline: Anthropic Nov 2024 → OpenAI Mar 2025 → AAIF Dec 2025

### AI Collaboration Keys
- Agent code doesn't change when adding MCP—just configure servers
- Community servers (GitHub, databases, search) provide instant capabilities
- Same server works across Claude Code, Cursor, VS Code

### Common Mistakes
- Building custom integrations when MCP servers already exist
- Confusing Host (where humans work) with Client (connection manager)
- Thinking MCP replaces SDKs—it sits beside them, handling tool routing

### Connections
- **Builds on**: SDK chapters (34-36) showed per-SDK tool patterns MCP standardizes
- **Leads to**: Transport Layers (Lesson 2)
