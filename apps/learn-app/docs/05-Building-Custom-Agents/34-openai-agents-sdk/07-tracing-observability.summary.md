### Core Concept
Observability transforms agents from black boxes into transparent systems. RunHooks capture lifecycle events (agent start/end, tool calls), while tracing correlates multi-agent workflows into causal chains viewable in OpenAI Platform.

### Key Mental Models
- **Three Levels of Visibility**: Lifecycle events (what happened) → Execution context (tokens, cost) → Causal chains (how agents relate)
- **Hooks = Events, Traces = Correlation**: RunHooks fire on events; traces connect multiple agent runs into one story
- **Cost Attribution**: Connect token usage to specific agents and tools to understand where money goes

### Critical Patterns
- Implement `RunHooks` with `on_agent_start`, `on_agent_end`, `on_tool_start`, `on_tool_end`
- Access usage via `context.usage.total_tokens`, `input_tokens`, `output_tokens`
- Create traces: `with trace("workflow_name", group_id=trace_id)`
- Add spans: `with custom_span("phase_name")` for structured phases
- Generate IDs: `trace_id = gen_trace_id()` for correlation

### AI Collaboration Keys
- Use traces to see exactly what the agent decided and why—invaluable for debugging
- Track cost per agent to identify expensive operations worth optimizing

### Common Mistakes
- Only tracking agent-level events without tool granularity (missing where time is spent)
- Forgetting to pass `hooks=hooks` to `Runner.run()`
- Not using `group_id` to correlate multi-agent workflows

### Connections
- **Builds on**: Sessions and conversation memory (Lesson 6)
- **Leads to**: MCP integration (Lesson 8)
