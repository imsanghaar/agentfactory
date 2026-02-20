### Core Concept
Multi-agent pipelines fail from the dirty slate problem: each agent inherits accumulated context pollution from predecessors, leaving the final agent with attention budget consumed by irrelevant work-in-progress. The clean context pattern gives each subagent fresh, focused context—they return summaries, not full process.

### Key Mental Models
- **Dirty Slate Problem**: Agent A's 15 dead-end explorations + Agent B's analytical tangents = Agent C drowning in irrelevant tokens. The signal (final decisions) gets lost in noise (exploration scaffolding).
- **Clean Context Pattern**: Orchestrator delegates with fresh context to each subagent. Subagents return summaries only. Orchestrator synthesizes. Each agent uses full attention budget for its task.
- **Three Subagent Patterns**: Stateless (fresh context each call, strong isolation). Stateful (context transfers between agents for genuine dependencies). Shared (common memory layer for persistent state across long projects).

### Critical Patterns
- Orchestrator → [fresh context] → Subagent → [summary] → Orchestrator synthesis
- Parallel execution: independent research tasks can run simultaneously when contexts are isolated
- Context amnesia workarounds: preload Skills with domain knowledge, use master-clone architecture, or include critical context in delegation prompts
- Tool access control: give reviewers read-only access, writers get edit permissions, full access only for orchestrators

### Common Mistakes
- Linear pipeline handoffs: each agent passes full context, accumulating pollution—quality degrades as pipeline lengthens
- Not using orchestrator pattern: debugging polluted context is archaeology; isolated agents have clear accountability
- Forgetting context amnesia: subagents don't know your project without explicit knowledge injection

### Connections
- **Builds on**: Memory injection for evolving context (Lesson 8)
- **Leads to**: Complete context engineering playbook and decision frameworks (Lesson 10)
