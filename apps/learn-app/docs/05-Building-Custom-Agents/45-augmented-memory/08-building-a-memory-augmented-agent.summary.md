### Core Concept
A complete memory-augmented agent combines OpenAI Agents SDK with Mem0, using `@function_tool` decorators to expose memory operations. The agent remembers users across sessions and provides personalized task management assistance.

### Key Mental Models
- Memory tools are first-class agent capabilities: recall, store, list, forget
- Agent instructions guide natural memory usage in conversation
- User scoping ensures every operation includes `user_id` parameter
- Multi-session testing verifies memory survives application restarts

### Critical Patterns
- Memory tools: `recall_memories(query, user_id)`, `store_memory(content, user_id, category)`, `list_user_memories(user_id)`, `forget_memory(memory_text, user_id)`
- Agent instructions: "At conversation START: Always recall relevant memories about the user"
- Conversation loop: initial context retrieval -> interactive chat -> session-end storage
- Test pattern: store in Session 1, retrieve in new Session 2 with fresh agent instance
- Architecture layers: OpenAI Agents SDK -> Memory Tools -> Mem0 SDK -> Storage (SQLite + Qdrant)

### AI Collaboration Keys
- Use AI to add memory summarization when context grows large
- Have AI implement entity extraction for structured memory linking
- Practice building confidence scoring that considers similarity, recency, frequency, and user feedback

### Common Mistakes
- Not including initial context retrieval at session start
- Forgetting session-end storage for important conversation insights
- Testing only with same agent instance, not verifying true persistence across restarts

### Connections
- **Builds on**: Lesson 7 - Memory-Augmented Agent Patterns (production patterns)
- **Leads to**: Lesson 9 - Memory for Claude Code (experiencing memory as a user)
