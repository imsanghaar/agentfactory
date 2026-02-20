### Core Concept
Building an agent-evals skill using the Skill-First approach means creating the skill structure immediately from official documentation, then learning concepts by improving that skill throughout the chapter.

### Key Mental Models
- Skill-First inverts traditional learning: build the container first, then fill it with knowledge through practice
- Andrew Ng's insight: disciplined evaluation processes predict success with agentic workflows
- Evals test reasoning quality (probabilistic scores), not code correctness (PASS/FAIL)
- LEARNING-SPEC.md defines your learning contract with measurable success criteria

### Critical Patterns
- Clone skills-lab fresh for each chapter to prevent state pollution
- Write LEARNING-SPEC.md before any skill building (intent, success criteria, questions to answer)
- Create SKILL.md with valid YAML frontmatter (`name`, `description` fields only)
- Start with skeleton sections marked TODO - lessons fill them in
- Skill structure: Core Thesis, When to Activate, Key Concepts (to be developed)

### AI Collaboration Keys
- Use AI to validate your LEARNING-SPEC for measurable success criteria
- Ask AI to expand "When to Activate" triggers you might overlook
- Connect abstract eval concepts to your specific domain with AI help

### Common Mistakes
- Learning concepts first and building skill later (inverts the Skill-First approach)
- Skipping the LEARNING-SPEC (losing the learning contract and success criteria)
- Starting with synthetic test cases instead of real production data

### Connections
- **Builds on**: Chapter 46 (API development), general agent-building skills
- **Leads to**: Lesson 01 (Evals Are Exams for Reasoning)
