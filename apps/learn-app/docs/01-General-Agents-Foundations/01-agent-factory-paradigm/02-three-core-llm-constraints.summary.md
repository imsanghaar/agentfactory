### Core Concept

LLMs operate under three fundamental constraints—statelessness, probabilistic outputs, and limited context—that aren't bugs to fix but design parameters that shape every AI-native methodology. Understanding these constraints transforms you from fighting the technology to designing workflows that work with it.

### Key Mental Models

- **Expert with Amnesia**: Each session starts fresh; you must brief the model from scratch every time with all relevant context
- **Constraints → Methodology**: Each constraint directly creates its solution—statelessness creates AGENTS.md, probabilistic outputs create validation phases, limited context creates specification-first thinking
- **Specify, Validate, Iterate**: The natural workflow when outputs vary—define requirements precisely, validate what you receive, expect 1-2 refinement cycles

### Critical Patterns

- Persist context in files (AGENTS.md, SPEC.md) so it survives across sessions
- Use specifications to constrain the "space of valid outputs" rather than hoping for identical results
- Curate context quality over quantity—noise dilutes relevance within limited windows
- Reset long conversations by summarizing progress and starting fresh with only relevant context

### Common Mistakes

- Expecting the model to "remember" past sessions or preferences (it cannot—applications re-send history each time)
- Assuming identical prompts produce identical code (probabilistic sampling means variation is normal, not a bug)
- Stuffing entire codebases into context instead of selectively including relevant files

### Connections

- **Builds on**: The 2025 inflection point and why AI capabilities now demand new methodologies
- **Leads to**: The Orchestrator Mindset and specific techniques (SDD, MCP, TDD) that address each constraint
