### Core Concept
CLAUDE.md, Skills, Subagents, and Hooks are four distinct context management tools—each loads differently and costs differently. Proper architecture distributes information across them to reduce baseline context load by 10x or more.

### Key Mental Models
- **Four Loading Patterns**: CLAUDE.md loads at session start (every request). Skills load descriptions at start but full content only when invoked. Subagents use isolated context (zero main session cost). Hooks run externally (zero context cost).
- **Information-to-Tool Mapping**: Always needed + stable → CLAUDE.md. Sometimes needed + stable → Skill. Needs fresh analysis → Subagent. Must happen deterministically every time → Hook.
- **Cost Calculation**: A 500-line CLAUDE.md = ~7,300 tokens every request. Proper architecture (50-line CLAUDE.md + 3 Skills) = ~550 tokens baseline. 13x reduction means more room for actual work.

### Critical Patterns
- Keep CLAUDE.md under 60 lines with always-on context; move domain workflows to Skills
- Delegate research-heavy tasks to Subagents—your main context only receives summaries, not raw data
- Use Hooks for deterministic validation (linting, formatting)—no LLM overhead for tasks that don't require reasoning

### Common Mistakes
- Everything in CLAUDE.md: 300+ line files cause attention dilution and ignored instructions
- Never using Subagents: all file reads accumulate in main context, filling it quickly
- Unclear skill descriptions: Claude won't invoke skills correctly if it doesn't know when to use them
- Forgetting Hooks exist: using Claude for checks that don't require reasoning wastes LLM calls

### Connections
- **Builds on**: Signal vs Noise audit and lean CLAUDE.md (Lesson 2)
- **Leads to**: Task system for persistent state management (Lesson 4)
