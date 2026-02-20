### Core Concept
Tools give agents the ability to **do** things; context gives tools the ability to **remember** what happened. Together they create agents that take real actions and build on their own previous actions.

### Key Mental Models
- **Tools = Actions, Context = Memory**: An agent without tools can only talk; an agent without context can only react, not build
- **Context flows forward**: Mutations persist across tool calls—the second tool call can see changes from the first
- **Pydantic = Validation**: Context models catch type errors early and enforce data integrity

### Critical Patterns
- Decorate tools with `@function_tool` and include type hints + docstrings
- Define context as Pydantic `BaseModel` with default values
- Access context in tools via `context: RunContextWrapper[YourContext]`
- Mutate via `context.context.field_name = value` (double `.context`)
- Pass context to runner: `Runner.run_sync(agent, "...", context=ctx)`

### Common Mistakes
- Using `context.field` instead of `context.context.field` (missing the `.context` access)
- Creating context but forgetting to pass it via `context=ctx` parameter
- Expecting context to be sent to the LLM (it's never sent—use tools to expose state to agents)

### Connections
- **Builds on**: Agent → Runner → Result pattern (Lesson 1)
- **Leads to**: Agents as tools and orchestration (Lesson 3)
