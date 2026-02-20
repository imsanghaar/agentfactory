### Core Concept

Boris Cherny's (Claude Code creator) workflow demonstrates how chapter concepts combine into production-grade practice. While Boris works in software development, the techniques apply universally: parallel sessions ("the single biggest productivity unlock"), Claude-reviews-Claude for plan validation, self-writing CLAUDE.md rules, and Learning Mode for understanding new material. One person operating like a small team.

### Key Mental Models

- **Context is the Constraint**: Every technique traces back to managing the context window. Parallel sessions, subagents for investigation, `/clear` between tasks, Plan Mode—all prevent context pollution
- **Capacity Scheduling**: Run 15-20 concurrent Claude sessions across terminal and browser. Claude isn't a single tool you interact with—it's capacity you schedule like a team of assistants
- **Plan First, Execute Later**: Always enter Plan Mode for non-trivial tasks. Iterate on the plan until it's solid, then switch to auto-accept for execution. Planning alignment prevents wasted iterations
- **Verification-First Quality**: Give Claude ways to verify its own work (browser testing, MCP tools, hooks). This feedback loop 2-3x quality of final results. You don't trust AI output—you instrument it
- **Self-Evolving Documentation**: After corrections, say "Update your CLAUDE.md so you don't make that mistake again." Every mistake becomes a rule. Team shares and evolves CLAUDE.md through code review, creating institutional memory that compounds
- **Claude-Reviews-Claude**: One Claude writes the plan, second Claude reviews critically. Fresh context catches blind spots the writer missed

### Critical Patterns

- **Parallel sessions with worktrees**: Git worktrees (or separate checkouts) with shell aliases (`za`, `zb`, `zc`) to hop between them; dedicated "analysis" worktree for logs/queries
- **Session-end review**: Build a skill in `.claude/skills/name/SKILL.md`, run at end of every session to capture insights
- **Re-plan when stuck**: The moment something goes sideways, switch back to Plan Mode—don't push through confusion
- **Autonomous problem solving**: Give Claude the problem, not the solution—paste a thread and say "fix" or "resolve this"
- **Challenge prompts**: "Grill me on this", "Poke holes in this plan", "Knowing everything you know now, scrap this and create the elegant solution"
- **Learning Mode**: `/config` → "Explanatory" output style—Claude explains the _why_ behind changes
- **Visual learning**: Generate HTML presentations and ASCII diagrams for unfamiliar material
- **Voice dictation**: Speak 3x faster than typing (fn x2 on macOS)—more detail = better output
- **Conversational research**: Query your data sources (databases, documents, connected tools) through natural language
- Use Opus 4.5 with thinking—"wrong fast answer" costs more time than "right slow answer"
- Create specialized subagents; append "use subagents" to throw more compute at problems
- Add PostToolUse hooks for consistent formatting or checks
- Use `/permissions` to pre-allow safe commands rather than `--dangerously-skip-permissions`
- 10-20% session abandonment is normal—sometimes fresh is faster than recovery

### Common Mistakes

- Running single overloaded sessions instead of parallel ones
- Skipping Plan Mode because "this seems simple"—Boris uses it for every non-trivial task
- Pushing through when stuck instead of re-planning
- Writing CLAUDE.md rules yourself instead of letting Claude self-write after corrections
- Micromanaging problem-solving instead of letting Claude investigate autonomously
- Hoping output is correct instead of building verification infrastructure
- Not using Learning Mode when onboarding to unfamiliar material

### Connections

- **Synthesizes**: All Chapter 3 lessons—Origin Story (agency), CLAUDE.md (context), Skills (expertise), MCP (tools), Subagents (delegation), Hooks (automation), Settings (configuration)
- **Demonstrates**: Real-world workflow at Anthropic production scale
- **Leads to**: Part 3 (Spec-Driven Development), Part 6 (Custom Agent SDKs), Part 7 (Digital FTE Deployment)
- **Digital FTE Link**: Each capability maps to productizable agent components—skills become assets, CLAUDE.md becomes team memory, subagents become orchestration patterns
