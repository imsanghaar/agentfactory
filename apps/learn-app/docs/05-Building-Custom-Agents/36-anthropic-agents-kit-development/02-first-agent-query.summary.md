### Core Concept
The `query()` function is an async generator that streams messages as the agent executes. Configure with `ClaudeAgentOptions` to control tools, permissions, and execution limits.

### Key Mental Models
- **Async generator pattern**: `async for message in query(...)` streams agent execution
- **Three message types**: assistant (reasoning), tool_use (execution), result (final answer)
- **ClaudeAgentOptions**: allowed_tools, permission_mode, max_turns, cwd

### Critical Patterns
- Basic query: `async for message in query(prompt=..., options=ClaudeAgentOptions(...))`
- Extract result: `if message.type == "result": print(message.result)`
- Permission modes: default (prompts), acceptEdits (auto-approve files), bypassPermissions (full auto)
- Tool restriction: `allowed_tools=["Read", "Glob", "Grep"]` for read-only agents

### AI Collaboration Keys
- Start conservative with tools: deny-all, then allowlist necessary
- Use max_turns to prevent runaway agents

### Common Mistakes
- Forgetting async/await pattern
- Granting all tools when agent only needs read access
- No max_turns limit (infinite loop risk)

### Connections
- **Builds on**: SDK Architecture (Lesson 1)
- **Leads to**: Built-in Tools Deep Dive (Lesson 3)
