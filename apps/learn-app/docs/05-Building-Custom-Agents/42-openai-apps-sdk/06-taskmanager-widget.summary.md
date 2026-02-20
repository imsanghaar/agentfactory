### Core Concept
`widgetState` persists UI state (selections, scroll position, filters) across widget reloads. `setWidgetState` saves, `widgetState` restores. Display modes: inline (default), pip (floating), fullscreen (expanded).

### Key Mental Models
- **UI state vs server data**: Server stores tasks; widgetState stores selections/preferences
- **Reload problem**: Every callTool replaces widget, losing unsaved UI state
- **Save before action**: Call setWidgetState before any operation that triggers reload
- **Display modes**: Control widget size/position via `openai.com/widgetDisplayMode`

### Critical Patterns
- Initialize: `const saved = window.openai?.widgetState; if (saved) state = {...state, ...saved}`
- Save: `window.openai?.setWidgetState?.(state)`
- Clean dangling IDs: Remove deleted task IDs from selections before saving
- Display mode: `_meta={"openai.com/widgetDisplayMode": "fullscreen"}`

### AI Collaboration Keys
- Prompt 1: Persist scroll position in widgetState
- Prompt 2: Add filter dropdown (All/Pending/Done) that persists
- Prompt 3: Create pip mode widget for quick status

### Common Mistakes
- Not saving state before callTool (selections lost on reload)
- Dangling IDs in selections (deleted tasks still in selectedIds)
- Merging saved state wrong (overwrites defaults instead of extending)

### Connections
- **Builds on**: Task Actions with callTool (Lesson 5)
- **Leads to**: React & Apps SDK UI (Lesson 7)
