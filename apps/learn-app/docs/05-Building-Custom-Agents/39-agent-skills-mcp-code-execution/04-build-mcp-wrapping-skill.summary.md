### Core Concept
Specification first, implementation second. Write spec answering: What MCP? What decisions? How measure success? What if failure? Then collaborate with AI iteratively—discover patterns, refine with domain constraints, test, iterate until robust.

### Key Mental Models
- **Spec-first development**: 4 questions (MCP server, intelligent decisions, success metrics, failure recovery)
- **Collaborative iteration**: AI suggests pattern → you test → discover constraints → AI refines → repeat
- **Token efficiency target**: 30%+ reduction through intentional filtering
- **Persona translates spec**: Persona = "who makes decisions"; Questions = "how to decide"

### Critical Patterns
- MCP client init: StdIOClient with command, args, timeout; context manager for cleanup
- Token counting: tiktoken before/after filtering; calculate savings percentage
- Filtering logic: detect_experience_level → extract_candidates → score_relevance → top N
- Error handling: specific exceptions → retry with backoff → fallback → escalate

### AI Collaboration Keys
- Round 1: Generic pattern; Round 2: Domain constraints; Round 3: Edge cases; Round 4: Working solution
- Implementation emerges from iteration, not predefined steps
- Each round addresses specific limitations discovered through testing

### Common Mistakes
- Skipping specification (leads to rework)
- Accepting generic solution without domain refinement
- Not testing filtering against real-world data

### Connections
- **Builds on**: Anatomy of MCP-Wrapping Skills (Lesson 3)
- **Leads to**: Script Execution Fundamentals (Lesson 5)
