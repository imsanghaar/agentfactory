### Core Concept
`callTool` talks directly to server without conversation turn—silent updates for toggling/deleting. `widgetAccessible: true` annotation required. Pattern: `callTool` to mutate, then `sendFollowUpMessage` to refresh.

### Key Mental Models
- **callTool vs sendFollowUpMessage**: Direct server (silent) vs conversation (model sees)
- **widgetAccessible security**: Only annotated tools callable from widgets
- **Mutation pattern**: callTool → action happens → refresh via sendFollowUpMessage
- **Use case split**: sendFollowUpMessage for adding; callTool for toggling/deleting

### Critical Patterns
- Tool annotation: `@mcp.tool(annotations={"openai/widgetAccessible": True})`
- Widget call: `await window.openai?.callTool?.('complete_task', { task_id: taskId })`
- Refresh after mutation: `callTool()` then `sendFollowUpMessage({ prompt: "Show tasks" })`
- Parameter name match: `task_id` in Python = `task_id` in JavaScript

### AI Collaboration Keys
- Prompt 1: Add "Add Task" input field with sendFollowUpMessage
- Prompt 2: Add confirmation dialog before delete
- Prompt 3: Handle callTool errors gracefully

### Common Mistakes
- Missing `widgetAccessible: True` (callTool silently fails)
- Parameter name mismatch (`taskId` vs `task_id`)
- Not refreshing after callTool (widget shows stale data)

### Connections
- **Builds on**: Displaying Tasks (Lesson 4)
- **Leads to**: State Persistence and Display Modes (Lesson 6)
