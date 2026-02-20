### Core Concept
ToolContext provides tool-level state access (read/write during execution), while SessionService provides session-level persistence (how conversations survive across API calls). Together they enable agents that remember context across conversations.

### Key Mental Models
- **ToolContext = state gateway**: Tools read/write session state via `tool_context.state`
- **SessionService = storage backend**: InMemory (dev) → Firestore (prod) → VertexAI (enterprise)
- **State flows bidirectionally**: Initial state → tool reads → tool modifies → updated state persists

### Critical Patterns
- Read state: `tool_context.state.get("key", default)`
- Write state: `tool_context.state["key"] = value`
- Dev setup: `Runner(agent=agent, session_service=InMemorySessionService())`
- Prod setup: `FirestoreSessionService(project="my-project", database="(default)")`

### AI Collaboration Keys
- Use InMemory for local testing, Firestore for production persistence
- Design state schema upfront: preferences, history, progress tracking

### Common Mistakes
- Using InMemory in production (state lost on restart)
- Not passing session_id to runner (can't correlate conversations)
- Expecting state to persist without SessionService configuration

### Connections
- **Builds on**: Custom Function Tools (Lesson 2)
- **Leads to**: Coordinator Patterns (Lesson 4)
