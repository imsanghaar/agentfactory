### Core Concept
Skill-first learning creates a reusable `relational-db-agent` skill before learning SQLModel, transforming knowledge into an asset that generates production-quality async database code.

### Key Mental Models
- Skills over knowledge: Build assets that grow, not knowledge that fades
- Documentation-grounded: Fetch official docs first, never rely on memory
- Iterative improvement: Each lesson tests and improves the skill
- LEARNING-SPEC as contract: Define success criteria before building

### Critical Patterns
- Clone skills-lab fresh each chapter for clean state
- Write LEARNING-SPEC.md defining what skill should know
- Use `/fetching-library-docs` for official SQLModel patterns
- Use `/skill-creator` to generate SKILL.md with proper YAML frontmatter
- Test skill generates valid code with correct imports and `table=True`

### AI Collaboration Keys
- Use AI to verify skill structure (YAML frontmatter, "Use when" description)
- Test skill output by generating AsyncSession dependencies
- Identify gaps proactively before learning each topic

### Common Mistakes
- Building skill from memory instead of official documentation
- Skipping the LEARNING-SPEC clarity step
- Not testing skill output compiles without syntax errors

### Connections
- **Builds on**: Skill creation patterns from Chapter 39
- **Leads to**: L01 - Why agents need structured data
