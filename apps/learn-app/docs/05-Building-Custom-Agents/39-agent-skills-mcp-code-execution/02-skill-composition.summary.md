### Core Concept
Skills don't formally depend on each other—Claude orchestrates them at runtime. Skill descriptions are your API contract; good descriptions enable composition. Design complementary skills with compatible output→input interfaces.

### Key Mental Models
- **Claude as orchestrator**: Reads descriptions, matches capabilities to tasks, invokes in sequence
- **Description = contract**: Vague description → skill selection fails; clear description → composition works
- **Output→Input flow**: Skill A produces JSON, Skill B expects JSON—compatible by design
- **No formal dependencies**: Skills remain independent and portable

### Critical Patterns
- Description structure: What it does + When to use + What it returns
- Composition patterns: Output→Input flow, Shared domain knowledge, Progressive refinement
- Bundled resources: Duplicate for portability; centralize only when you control deployment
- Error handling: Claude decides retry/skip/halt/adapt based on task requirements

### AI Collaboration Keys
- Write descriptions that answer: "When should this skill activate?"
- Design interfaces that match—don't rely on Claude to transform data
- Multi-skill workflows emerge from clear descriptions, not formal chaining

### Common Mistakes
- Too vague descriptions ("helps with various tasks")
- Overlapping descriptions (Claude can't distinguish which to use)
- Incompatible interfaces (Skill A outputs XML, Skill B expects JSON)

### Connections
- **Builds on**: Advanced Skill Patterns (Lesson 1)
- **Leads to**: Anatomy of MCP-Wrapping Skills (Lesson 3)
