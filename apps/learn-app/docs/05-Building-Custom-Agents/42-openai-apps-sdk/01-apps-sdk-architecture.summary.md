### Core Concept
Apps SDK puts your agents inside ChatGPT with 800M weekly active users. Three-layer architecture: ChatGPT UI (hosts everything), Widget iframe (your visual code), MCP Server (your backend). Distribution without building your own interface or user acquisition.

### Key Mental Models
- **Three layers**: ChatGPT UI → Widget iframe → MCP Server (security through isolation)
- **Distribution solved**: App Directory + AI-powered discovery replaces marketing
- **Dual channels**: `structuredContent` (model sees) + `_meta` (widget only)
- **Widget vs standard MCP**: MIME type `text/html+skybridge` triggers widget rendering

### Critical Patterns
- Data flow: User prompt → Model tool call → Server response → Widget render → Model narration
- `structuredContent`: Concise data for model narration (task counts, status)
- `_meta["openai.com/widget"]`: HTML with MIME type triggers iframe creation
- Bidirectional: `sendFollowUpMessage()` and `callTool()` from widget

### AI Collaboration Keys
- Prompt 1: Compare distribution strategies (standalone vs ChatGPT App)
- Prompt 2: Explain three-layer security separation
- Prompt 3: Differentiate Apps SDK from Agents SDK

### Common Mistakes
- Confusing Apps SDK with Agents SDK (visual widgets vs backend logic)
- Missing MIME type (widget won't render without `text/html+skybridge`)
- Putting large data in structuredContent (model tries to process it all)

### Connections
- **Builds on**: Custom MCP Servers (Chapter 38)
- **Leads to**: Your First Widget (Lesson 2)
