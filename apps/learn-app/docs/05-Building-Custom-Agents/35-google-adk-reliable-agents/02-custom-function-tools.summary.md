### Core Concept
Google ADK auto-wraps Python functions as tools when they have type hints and docstrings. No decorators needed—just a function with types and documentation becomes an agent capability.

### Key Mental Models
- **Type hints = Tool schema**: ADK generates the schema Gemini needs from your type annotations
- **Docstring = Tool discovery**: Becomes the tool's description; helps agent decide when to use it
- **Graceful degradation**: Return error dicts instead of raising exceptions—agent continues working

### Critical Patterns
- Function pattern: `def tool(param: type) -> return_type:` with complete docstring
- Wrap for agent: `Tool.from_function(my_tool)`
- Add to agent: `Agent(tools=[Tool.from_function(fn1), google_search])`
- Error handling: try-catch around each operation, return structured error responses

### AI Collaboration Keys
- Tools should be focused: one tool fetches data, another analyzes—don't combine
- Agent naturally chains tools: search → parse results → enrich with financial data

### Common Mistakes
- Missing type hints (ADK cannot generate tool schema)
- Raising exceptions instead of returning error dicts (agent crashes)
- Inconsistent return types (sometimes dict, sometimes string)
- Overly complex logic in single tool (should split into focused tools)

### Connections
- **Builds on**: Agent basics (Lesson 1)
- **Leads to**: Session State & Memory (Lesson 3)
