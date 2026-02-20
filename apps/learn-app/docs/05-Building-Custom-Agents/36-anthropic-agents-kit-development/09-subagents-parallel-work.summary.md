### Core Concept
Subagents decompose complex workflows into specialized agents that work in parallel. Define AgentDefinition with description, prompt, tools, and model. Orchestrator invokes via Task tool. Pattern: Decompose → Specialize → Parallelize → Synthesize.

### Key Mental Models
- **Context isolation**: Each subagent gets focused expertise without competing for context window
- **Tool restriction per subagent**: Security reviewer gets Read/Grep, performance analyst gets Bash
- **Model selection**: Sonnet for complex reasoning, Haiku for straightforward analysis

### Critical Patterns
- Subagent definition: `AgentDefinition(description=..., prompt=..., tools=[...], model="haiku")`
- Orchestrator requires Task tool: `allowed_tools=["Read", "Grep", "Task"]`
- Parallel execution: All subagents work simultaneously, total time = longest single task
- Result synthesis: Orchestrator collects and combines subagent outputs

### AI Collaboration Keys
- Start with 2-3 specialists, add more only when needed
- Design subagent prompts with structured output formats for easy synthesis
- Specialization tradeoff: more specialists = more coordination complexity

### Common Mistakes
- Creating too many subagents (overhead exceeds benefit)
- Using subagents when tasks are sequential (breaks parallelism)
- Forgetting to include Task tool in orchestrator's allowed_tools

### Connections
- **Builds on**: File Checkpointing (Lesson 8)
- **Leads to**: Lifecycle Hooks (Lesson 10)
