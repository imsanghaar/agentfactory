### Core Concept
Building a Dapr skill before learning Dapr ensures you own a production-ready knowledge asset from day one, grounded in official documentation rather than memory-based assumptions.

### Key Mental Models
- **Skill-First Learning**: Create the skill before learning the content; the chapter teaches you what your skill already knows
- **Documentation-Grounded Knowledge**: Skills built from Context7/official docs are more reliable than AI memory
- **Fresh Clone Pattern**: Always start from a clean skills-lab to avoid state assumptions
- **Ownership Over Consumption**: You graduate owning sellable skills, not just knowledge

### Critical Patterns
- Clone skills-lab fresh at chapter start
- Use Context7 skill to fetch official Dapr documentation
- Create skill with natural language prompt specifying use case
- Skill appears at `.claude/skills/dapr-sidecar/`

### AI Collaboration Keys
- Use "skill creator skill" to bootstrap new skills
- Specify real use case (microservices communication, state management)
- Let Claude ask clarifying questions to refine the skill

### Common Mistakes
- Skipping the fresh clone and carrying over state from previous work
- Building skills from memory instead of official docs
- Not specifying a concrete use case for the skill

### Connections
- **Builds on**: Claude Code skills infrastructure from earlier chapters
- **Leads to**: Lesson 1 - Sidecar Pattern fundamentals
