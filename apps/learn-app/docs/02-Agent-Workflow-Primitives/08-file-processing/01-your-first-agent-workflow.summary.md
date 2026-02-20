### Core Concept

Effective collaboration with General Agents starts with describing problems rather than solutions. You state what you want to understand, and let the agent figure out how to get there. The value isn't automation — it's the combination of your judgment with the agent's technical execution.

### Key Mental Models

- **Problem description over solution specification**: You describe outcomes, not procedures. The agent determines the technical approach.
- **Division of labor**: You describe the problem in language ("cluttered Downloads folder"). The agent chooses the solution in code (`ls`, `find`, `wc`, `du`). Neither can do the other's job — the value comes from combining human judgment with agent execution.
- **Observation over memorization**: Watch what the agent does to learn patterns without rote memorization of commands. Recognizing commands helps you verify the agent is doing the right thing.
- **Prompt patterns transfer**: The "help me understand" pattern works for files, data analysis, project planning, and any domain where you direct General Agents.
- **Know when you're faster**: If you can do it faster than you can describe it, just do it. Three files to move? Drag them. Three hundred to categorize? Agent territory.
- **Know when the agent is the wrong tool**: Browsing photos (you need to see thumbnails), network drives (latency and permissions differ), decisions that need human eyes (irreplaceable photos) — not every task belongs in a terminal.

### Critical Patterns

- **"Help me understand [problem], show me [what I need]"**: This universal prompt pattern triggers the agent to analyze and report findings.
- **Principle 1 (Bash is the Key)**: The agent combines basic Unix commands (`ls`, `find`, `wc`, `du`, `sort`) to extract exactly the information you need.
- **Principle 7 (Observability)**: The agent makes chaos visible through structured reports showing file counts, types, and space usage.
- **Command literacy**: You don't memorize commands, but recognizing patterns like `find ... | wc -l` ("find files, then count them") and common flags (`-l` for lines, `-h` for human-readable, `-r` for reverse) helps you verify agent behavior.

### Common Mistakes

- Specifying technical commands instead of describing the problem: "Run `find` and `du`" limits the agent to your approach.
- Skipping the observation phase: Missing how the agent works means you don't learn reusable patterns.
- Not defining what success looks like: Vague requests like "look at my files" produce unfocused responses.
- Using the agent when you're faster: Browsing photo thumbnails, moving 3 files, peeking at a file — some tasks don't need an agent.

### Connections

- **Builds on**: Part 1 (Chapters 1-5) understanding of General Agents and the Seven Principles
- **Leads to**: Safety-first patterns (Lesson 2), organization workflows (Lesson 3)
