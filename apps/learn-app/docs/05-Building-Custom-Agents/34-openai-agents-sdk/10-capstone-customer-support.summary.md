### Core Concept
A production Digital FTE composes all chapter patterns: multi-agent routing (triage → specialists), context persistence across agents, guardrails for safety, sessions for memory, tracing for observability, MCP for external docs, and RAG for knowledge bases.

### Key Mental Models
- **Specialist composition**: Triage routes to focused experts (FAQ, Booking, Escalation)—each excellent at one job
- **Context flows across boundaries**: Single Pydantic model accumulates state as conversation moves between agents
- **Safety layering**: Input guardrails (abuse, PII) + Output guardrails + Escalation = defense in depth

### Critical Patterns
- Design context model with all fields agents need: `AirlineAgentContext`
- Implement handoffs with `on_handoff` callbacks for context injection
- Combine MCP (external docs) + RAG (internal policies) for comprehensive knowledge
- Track full conversation with `trace()` and `group_id` correlation
- Use `SQLiteSession` for persistent multi-turn memory

### AI Collaboration Keys
- Let triage decide routing based on instructions—don't hardcode decision trees
- Build specialist agents that hand back to triage when out of scope

### Common Mistakes
- Building one mega-agent instead of specialists (confusion, low accuracy)
- Not testing guardrails against real attack patterns
- Skipping escalation path (some issues genuinely need humans)

### Connections
- **Builds on**: All Lessons 1-9 (SDK, tools, context, agents-as-tools, handoffs, guardrails, sessions, tracing, MCP, RAG)
- **Leads to**: Chapter 35 Google ADK or production deployment
