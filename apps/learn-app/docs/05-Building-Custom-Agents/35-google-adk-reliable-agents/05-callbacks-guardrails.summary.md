### Core Concept
Callbacks hook into agent lifecycle to enforce safety, validate data, and enhance responses. Return None to allow, return dict to block/override. Six callback types provide granular control at agent, model, and tool execution points.

### Key Mental Models
- **before = gatekeeping**: Validate, filter, or block before execution
- **after = enhancement**: Transform, log, or augment after execution
- **Return None = proceed**: Allow normal execution
- **Return value = override**: Skip execution, use your value instead

### Critical Patterns
- Domain filtering: `if "site:blocked.com" in query: return {"error": "blocked"}`
- Source transparency: Extract URLs, store in `tool_context.state['process_log']`
- Rate limiting: Track `tool_context.state['search_count']` and block at limit
- Caching: Check cache before tool, store result after tool

### AI Collaboration Keys
- Document callback behavior in agent instructions so agent understands its constraints
- Combine multiple callbacks: filtering + rate limiting + transparency

### Common Mistakes
- Letting callback exceptions crash agent (wrap in try-except)
- Multiple concerns in one callback (keep focused)
- Not updating agent instructions to explain callback constraints

### Connections
- **Builds on**: Coordinator Patterns (Lesson 4)
- **Leads to**: Multi-Agent Orchestration (Lesson 6)
