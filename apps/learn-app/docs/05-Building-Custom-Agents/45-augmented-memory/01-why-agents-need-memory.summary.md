### Core Concept
LLMs have no persistent memory by default; every session starts fresh due to finite context windows. Adding memory transforms agents from stateless chatbots into valuable AI assistants that build relationships over time.

### Key Mental Models
- Context window is a temporary buffer, not a memory system; it is ephemeral and lost between sessions
- Stateless agents process each request in isolation; stateful agents maintain context across interactions
- Memory creates switching costs and competitive advantage through personalization and improvement over time
- Valuable memories cluster around user preferences, interaction history, learned facts, and behavioral patterns

### Critical Patterns
- Context amnesia problem: large context windows (128k-200k tokens) are still insufficient due to cost, latency, and noise concerns
- User scoping with `user_id` to connect memories across sessions
- Memory categories: user identity/preferences, interaction history, learned facts, behavioral patterns
- Memory as competitive differentiator: retention effect, improvement effect, differentiation effect

### AI Collaboration Keys
- Use AI to design memory categories for specific agent use cases
- Have AI explore domain-specific memory requirements (legal, medical, financial have strict constraints)
- Practice comparing stateless vs stateful agent conversations to understand behavioral differences

### Common Mistakes
- Assuming large context windows eliminate the need for memory systems
- Storing everything without prioritization, leading to noise and storage costs
- Treating memory as just technical infrastructure rather than an experiential improvement for users

### Connections
- **Builds on**: Understanding of LLM context windows and basic agent concepts
- **Leads to**: Lesson 2 - Memory Architecture Patterns (five types of agent memory)
