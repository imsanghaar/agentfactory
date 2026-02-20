### Core Concept
Complete TaskManager combining all patterns: architecture, widgets, interactivity, data channels, callTool, state persistence. Production requires: permanent URL, database, OAuth, security metadata (widgetCSP, widgetDomain, visibility).

### Key Mental Models
- **Architecture trace**: Prompt → Model tool call → Server → Widget render → Model narration
- **Debugging checklist**: Server → ngrok → App registered → URL correct → Tool discovered → Widget delivered
- **Production vs development**: ngrok→permanent URL, memory→database, none→OAuth
- **Security metadata**: widgetCSP for external domains, visibility for private tools

### Critical Patterns
- Debugging order: Check MIME type, widgetAccessible annotation, optional chaining
- widgetCSP: `{"connect-src": ["https://api.yourdomain.com"], "img-src": [...]}`
- Private tools: `annotations={"openai/visibility": "private"}` (widget-only)
- widgetDomain: Enables fullscreen and API allowlisting

### AI Collaboration Keys
- Prompt 1: Add task categories with colored badges
- Prompt 2: Debug three common widget bugs
- Prompt 3: Design ChatGPT App for your domain

### Common Mistakes
- Wrong MIME type (widget stuck on Loading)
- Missing widgetAccessible (callTool fails silently)
- No optional chaining (crashes outside ChatGPT)
- Cache issues (delete app and re-register with new ngrok URL)

### Connections
- **Builds on**: All Lessons 1-7 patterns composed
- **Leads to**: Chapter 43 (Vector Databases & RAG) / Production deployment
