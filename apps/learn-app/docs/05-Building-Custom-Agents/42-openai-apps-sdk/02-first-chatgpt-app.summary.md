### Core Concept
Build a ChatGPT App widget in under 50 lines. Three things make it work: MIME type `text/html+skybridge`, `_meta["openai.com/widget"]` key, and `EmbeddedResource` packaging. Development workflow: local server + ngrok + Developer Mode.

### Key Mental Models
- **Minimal viable widget**: FastMCP server returning HTML with magic MIME type
- **Development workflow**: Run server → ngrok tunnel → Register in ChatGPT → Test
- **ngrok endpoint**: `https://xyz.ngrok-free.app/mcp` (URL changes each restart)
- **See it work first**: Understand the flow before diving into details

### Critical Patterns
- MIME type: `MIME_TYPE = "text/html+skybridge"`
- Tool response: `_meta={"openai.com/widget": types.EmbeddedResource(...)}`
- Resource structure: `TextResourceContents(uri, mimeType, text)`
- SSE app: `app = mcp.sse_app()` for streaming events

### AI Collaboration Keys
- Prompt 1: Add a name parameter to personalize greeting
- Prompt 2: Customize widget styling with different gradients
- Prompt 3: Understand why custom MIME type is required

### Common Mistakes
- Wrong MIME type (widget shows "Loading..." forever)
- Missing `_meta` key (no widget, just text response)
- ngrok URL changed (delete app and re-register)
- Using JSON body instead of EmbeddedResource

### Connections
- **Builds on**: Apps SDK Architecture (Lesson 1)
- **Leads to**: Adding a Refresh Button (Lesson 3)
