### Core Concept
React + `@openai/apps-sdk-ui` for complex widgets. `useOpenAiGlobal` hook subscribes to `window.openai` values reactively. `useWidgetState` hook manages persistent state. Pre-built components match ChatGPT's design system.

### Key Mental Models
- **React for complexity**: Declarative rendering, centralized state, automatic cleanup
- **useOpenAiGlobal**: Subscribes to window.openai values; re-renders on changes
- **useWidgetState**: Hydrates from widgetState, syncs back on every update
- **apps-sdk-ui**: Button, Badge, TextLink matching ChatGPT design tokens

### Critical Patterns
- Hook usage: `const toolOutput = useOpenAiGlobal("toolOutput")`
- Persistent state: `const [state, setState] = useWidgetState(() => ({ selectedIds: [] }))`
- Component: `<Button variant="primary" onClick={handleClick}>Add</Button>`
- Bundle: esbuild → single `widget.js` file embedded in HTML

### AI Collaboration Keys
- Prompt 1: Add dark mode support using theme from useOpenAiGlobal
- Prompt 2: Create custom hook for task actions (complete, delete, add, refresh)
- Prompt 3: Add display mode toggle button

### Common Mistakes
- Not using useSyncExternalStore for window.openai (stale values)
- Forgetting to sync state back via setWidgetState
- External stylesheets (must inline CSS or bundle with esbuild)

### Connections
- **Builds on**: State Persistence and Display Modes (Lesson 6)
- **Leads to**: Complete TaskManager Capstone (Lesson 8)
