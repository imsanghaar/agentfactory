### Core Concept
Production memory-augmented agents combine four patterns: pre-prompt injection (always-on context), dynamic retrieval (on-demand context), conflict resolution (handling contradictions), and testing strategies (verifying behavior).

### Key Mental Models
- Pre-prompt injection is simple but may waste tokens on irrelevant context
- Dynamic retrieval is more efficient but requires agent decision-making
- Conflicts fall into three types: temporal (newer wins), ambiguous (ask user), partial (gather context)
- Testing memory agents requires verifying behavior, not just storage operations

### Critical Patterns
- Pre-prompt: `build_system_prompt()` retrieves and injects memories before user message
- Dynamic: `@function_tool` for `recall_memory` and `store_memory` that agent calls during conversation
- Conflict detection: LLM-based analysis to identify contradictions between memories
- Conflict resolution: `handle_temporal_conflict()`, `handle_ambiguous_conflict()`, `handle_partial_conflict()`
- Test categories: storage correctness, retrieval relevance, conflict detection, multi-session persistence

### AI Collaboration Keys
- Use AI to design memory injection strategy allocation (pre-prompt vs dynamic budget)
- Have AI implement conflict resolution with context-aware decisions
- Practice building comprehensive test suites for memory-augmented behavior

### Common Mistakes
- Using only pre-prompt injection when dynamic would be more token-efficient
- Assuming all contradictions should resolve to "newer wins" without considering context
- Testing only storage operations, not end-to-end personalization behavior

### Connections
- **Builds on**: Lesson 6 - Implementing Memory with Mem0 (SDK operations)
- **Leads to**: Lesson 8 - Building a Memory-Augmented Agent (complete implementation)
