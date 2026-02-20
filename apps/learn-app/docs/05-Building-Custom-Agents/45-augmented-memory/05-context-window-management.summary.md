### Core Concept
Context windows are finite and expensive; effective management through injection strategies, hierarchical summarization, and retrieve-vs-summarize decisions maximizes value from limited token budgets.

### Key Mental Models
- Context allocation is zero-sum: system prompt, tools, history, memories, and response all compete for tokens
- "Lost in the middle" problem: LLMs attend less to information in the middle of long contexts
- Hierarchical summarization compresses memories over time: events -> daily -> weekly -> monthly summaries
- Retrieve vs summarize is a decision based on query type: specific questions need full retrieval, pattern questions need summaries

### Critical Patterns
- Pre-prompt injection: memories before user message, good for background context
- Mid-prompt injection: memories after user message but before response, for query-specific context
- Dynamic injection: agent calls memory tools during reasoning to discover needed context
- Summarization chains: time-triggered compression with `summarize_tier()` function for each level
- Decision framework: recent events and specific dates need full retrieval; patterns and trends need summaries

### AI Collaboration Keys
- Use AI to design compression strategies within fixed token budgets
- Have AI create 4-tier summarization hierarchies with clear preservation rules
- Practice retrieve-vs-summarize decisions on concrete query examples

### Common Mistakes
- Allocating too much budget to memories, leaving insufficient space for conversation and response
- Placing important memories in the middle of context where they get less attention
- Summarizing too aggressively without preserving key details needed for specific queries

### Connections
- **Builds on**: Lesson 4 - Memory Retrieval Strategies (getting memories before managing context)
- **Leads to**: Lesson 6 - Implementing Memory with Mem0 (practical implementation)
