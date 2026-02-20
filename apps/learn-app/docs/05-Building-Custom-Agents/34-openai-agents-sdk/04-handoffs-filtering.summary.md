### Core Concept
Handoffs transfer control between agents—the specialist takes over completely. Message filtering cleans up conversation history before handoff so the specialist only sees relevant context.

### Key Mental Models
- **Triage → Specialist**: Triage doesn't solve problems—it routes to experts who take full responsibility
- **Filtering = Focus**: Remove tool calls and old messages so specialists don't get distracted by noise
- **on_handoff = Just-in-time injection**: Data that only exists at handoff time (flight number, session info) gets injected right before transfer

### Critical Patterns
- Register handoffs: `Agent(handoffs=[specialist_agent])`
- Use `handoff()` for callbacks: `handoff(agent, on_handoff=inject_data)`
- Access filter data: `HandoffInputData(input_history, pre_handoff_items, new_items)`
- Use utilities: `handoff_filters.remove_all_tools(data)` for common filtering

### AI Collaboration Keys
- Let the agent decide when to handoff based on instructions—don't manually trigger transfers
- Use `handoff_description` so the triage agent understands what the specialist does

### Common Mistakes
- Confusing handoffs (transfer control) with agents-as-tools (manager retains control)
- Not filtering tool calls, causing specialist confusion from irrelevant history
- Forgetting to inject runtime data with on_handoff when specialist needs session-specific context

### Connections
- **Builds on**: Agents as tools and orchestration (Lesson 3)
- **Leads to**: Guardrails and validation (Lesson 5)
