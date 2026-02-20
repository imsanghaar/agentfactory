### Core Concept
AI agents possess Five Powers (See, Hear, Reason, Act, Remember) that combine to enable autonomous orchestration, replacing navigation-based User Interfaces with conversation-based User Intent. These powers are delivered through a three-layer Modern AI Stack (Frontier Models, AI-First IDEs, Development Agents) connected by Model Context Protocol (MCP), which prevents vendor lock-in.

### Key Mental Models
- **UX to Intent Paradigm Shift**: Traditional software requires users to navigate interfaces (14 steps to book a hotel); agentic software lets users state intent conversationally (3 exchanges to achieve the same goal). The design challenge shifts from "make this interface intuitive" to "make this agent understand intent accurately."
- **Five Powers Framework**: See (visual understanding), Hear (audio processing), Reason (complex decision-making), Act (execute and orchestrate), Remember (maintain context and learn). Individually useful but limited; combined they create autonomous orchestration.
- **Three-Layer AI Stack**: Layer 1 (Frontier Models -- reasoning engines like Claude, GPT-5, Gemini), Layer 2 (AI-First IDEs -- development environments like Cursor, VS Code, Zed), Layer 3 (Development Agents -- autonomous workers like Claude Code). Layers are independent and composable.
- **MCP as USB for AI**: Model Context Protocol is a universal standard connecting agents to data/services without vendor lock-in. Write an MCP integration once, any compatible agent can use it.
- **Predictive to Generative to Agentic Evolution**: AI evolved from forecasting (Netflix recommendations) to creating (ChatGPT essays) to autonomous action (Claude Code editing, testing, committing). The agentic phase unlocked the Five Powers working together.

### Key Facts
- **Hotel booking comparison**: Traditional UX requires 14 manual steps; agentic UX reduces this to 3 conversational exchanges
- **2024 vs 2025 shift**: From tool silos (vendor bundles everything) to modular stack (pick your model, IDE, and agent independently)
- **Current Frontier Models**: Claude Opus 4.5 (Anthropic), GPT-5 (OpenAI), Gemini 2.5 (Google)
- **Current AI-First IDEs**: VS Code (Microsoft), Cursor (Anystic), Windsurf (Codeium), Zed (Zed Industries)
- **MCP benefit**: Before MCP, M models x N tools = M*N custom integrations. With MCP, M+N standardized connections

### Critical Patterns
- The Five Powers combine in sequences: Hear (request) -> Reason (analyze) -> Remember (recall preferences) -> Act (execute) -> See (read results) -> Reason (evaluate) -> Act (complete workflow) -> Remember (store for future)
- The spec-writing skill is now paramount: "When user clicks button X, do Y" becomes "When user expresses intent Z (in any phrasing), agent understands and acts appropriately"
- Competition drives innovation in modular stacks: when layers are independent, each layer improves separately and users benefit from best-of-breed selection
- Removing any single power from an agent significantly degrades its capability -- the powers are multiplicative, not additive

### Common Mistakes
- Thinking the Five Powers are just features when they are actually capabilities that must combine to enable autonomy (any single power alone is insufficient for orchestration)
- Confusing the shift from UX to Intent as eliminating the need for good design (the design challenge changes from visual hierarchy to intent modeling and context management)
- Assuming MCP eliminates all integration work (MCP standardizes the protocol, but you still need to build MCP servers for specific tools/services)
- Treating the AI stack layers as tightly coupled when the key innovation is their independence and composability (you can switch models without changing your IDE or agents)

### Connections
- **Builds on**: The orchestrator role (Lesson 2) and the OODA Loop that powers agent reasoning; the Two Paths Framework (Lesson 1) that distinguishes General from Custom Agents
- **Leads to**: AIFF Standards (Lesson 4) that govern MCP and other interoperability standards; the Digital FTE concept that combines all Five Powers via the three-layer stack for production use
