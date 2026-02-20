### Core Concept
**Recurring operational patterns should become reusable intelligence — extract the deployment sequences you've repeated across multiple lessons into structured, portable skill files that an AI coding agent can execute without your supervision.** Every time you repeated a deployment sequence, you were executing tacit knowledge locked inside your head. Time to formalize it.

### Key Mental Models
- **Pattern Recognition Before Formalization**: Before writing a skill, identify what you repeat. User creation, permission setting, service writing, and health verification appear 3-6+ times across the chapter. That repetition signals a pattern.
- **Frequency + Complexity + Value Framework**: A pattern must recur 2+ times, involve 3+ steps, and save time or prevent errors to justify creation. Running `ls` 100 times doesn't make it a skill.
- **Persona + Questions + Principles Structure**: A skill file has three parts — Persona (expertise and mindset), Key Questions (what to know before acting, with defaults), and Principles (rules never violated).
- **Fresh-System Validation**: A skill that works on your server but fails on a clean system has hidden assumptions. Testing on fresh environments reveals missing dependencies.

### Critical Patterns
- **SKILL.md format**: YAML frontmatter with `name` and `description`, followed by markdown body with Persona, Key Questions (with defaults), and Principles sections.
- **Deploy-agent skill as reference implementation**: Combines user creation, directory setup, ownership assignment, service file generation, daemon-reload, enable, start, and health verification into a single orchestrated procedure.
- **Parameterized scripts**: The skill's implementation takes arguments (agent name, port, exec command) rather than hardcoded values, making it reusable across different agents and runtimes.
- **Encoding lessons as principles**: "Never run as root," "Always use Restart=on-failure," "Always set MemoryMax" — hard-won knowledge becomes machine-readable rules.

### Common Mistakes
- **Formalizing trivial operations**: Creating a skill for `ls` or single commands wastes effort. Apply the frequency + complexity + value filter first.
- **Hidden assumptions in scripts**: A deploy script that assumes Python is installed, the user exists, or a directory is present will fail on fresh systems. Test on clean environments.
- **Writing principles too vaguely**: "Be secure" is not a principle. "Never run agents as root — create a dedicated user with nologin shell" is actionable and specific.
