### Core Concept
Transform API endpoints into agent tools: wrap CRUD functions with `@function_tool`, create Agent with tools list, expose via `/agent/chat` endpoint. Natural language requests become API operations. Agent decides WHEN to call tools based on user intent.

### Key Mental Models
- **APIs to Functions to Tools**: Endpoint logic extracted to functions, wrapped as tools, given to agent
- **Docstrings are descriptions**: Tool docstring becomes what agent sees to decide usage
- **Return strings**: Tools return human-readable strings, not complex objects
- **Session-independent**: Tool functions manage own database session, not tied to HTTP request

### Critical Patterns
- Tool wrapper: `@function_tool` decorator on function with docstring
- Agent creation: `Agent(name="...", instructions="...", tools=[...])`
- Non-streaming: `result = await Runner.run(agent, message)` returns `result.final_output`
- Streaming: `Runner.run_streamed()` with `async for event in result.stream_events()`
- SSE endpoint: `EventSourceResponse(agent_stream_generator(message))`

### AI Collaboration Keys
- Prompt 1: User context in tools—pass current user to tools for multi-user systems
- Prompt 2: Error handling—return error strings vs raise exceptions
- Prompt 3: Multiple agents—specialized agents with handoffs

### Common Mistakes
- Missing docstrings on tools (agent doesn't know what tool does)
- Returning SQLModel objects (not JSON-serializable)
- Not handling None/missing resources (crashes on missing task)
- Tools assuming HTTP request context exists

### Connections
- **Builds on**: Streaming with SSE (Lesson 13)
- **Leads to**: Capstone: Agent-Powered Task Service (Lesson 15)
