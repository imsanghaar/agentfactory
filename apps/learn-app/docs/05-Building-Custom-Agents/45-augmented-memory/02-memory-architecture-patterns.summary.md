### Core Concept
Effective agent memory is a system of specialized memory types inspired by cognitive science, each serving a different purpose. The two-tier architecture (in-context vs out-of-context) mirrors how the brain handles in-focus versus background information.

### Key Mental Models
- Five memory types map to human cognition: conversation (short-term), working (task-scoped), episodic (events), semantic (facts), long-term (persistent)
- Core memory (always visible) is small but high-value; external memory (retrieved on-demand) is large but query-dependent
- Self-editing memory: agents actively maintain their own memory rather than relying on external systems
- Memory types differ in persistence, scope, update patterns, and query use cases

### Critical Patterns
- Conversation memory: sliding window of recent turns, volatile per session
- Working memory: task-scoped context with goals, progress, and intermediate state
- Episodic memory: time-stamped records of specific events with context and outcomes
- Semantic memory: entity-focused knowledge graph with relationships (people, projects, concepts)
- Two-tier Letta/MemGPT pattern: persona block + human block (in-context) vs archival memory + conversation history (external)

### AI Collaboration Keys
- Use AI to map the five memory types to specific domain requirements (coding assistant, task manager, CRM)
- Have AI design episodic memory schemas with appropriate metadata and timestamps
- Explore semantic memory as knowledge graphs with entities and relationships

### Common Mistakes
- Treating all memory types the same without considering persistence and scope differences
- Putting too much in core memory (token-expensive) or too little (loses essential context)
- Ignoring the self-editing pattern where agents should update their own memory blocks

### Connections
- **Builds on**: Lesson 1 - Why Agents Need Memory (stateless vs stateful fundamentals)
- **Leads to**: Lesson 3 - What to Remember and What to Forget (prioritization and forgetting)
