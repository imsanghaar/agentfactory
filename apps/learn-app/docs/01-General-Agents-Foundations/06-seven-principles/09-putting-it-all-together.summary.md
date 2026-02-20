### Core Concept

The Seven Principles aren't a checklist—they're an integrated system where each principle reinforces the others. Mastery means knowing which principles to emphasize for different situations and orchestrating them into smooth workflows. This is the Director's Mindset: you orchestrate outcomes, not type prompts.

### Key Mental Models

- **From Typist to Director**: Typists type prompts and hope. Directors invoke principles explicitly, verify continuously, and course-correct proactively. The shift is from reactive to orchestrating.
- **Project Health Score (0-7)**: Score your setup: +1 each for CLAUDE.md, git repo, test suite, permission config, ADRs, Skills, Hooks. 0-2 = Cowboy Coder, 3-4 = Collaborator, 5-6 = Architect, 7 = Master Director.
- **Principle Prioritization by Task**: Different tasks emphasize different principles—debugging (P1, P3, P7), refactoring (P2, P4, P5), new features (all), exploration (P1, P7).
- **Skill Stacking**: Principles build on each other. P1 (Bash) enables P3 (Verification via tests). P4 (Decomposition) enables P6 (Safety via git). Master the dependencies.

### Key Facts

- **Integration payoff**: Individual principles provide incremental improvement; combined principles provide multiplicative improvement
- **Time to mastery**: Principles become automatic after 2-3 weeks of conscious practice
- **Director's advantage**: Directors complete tasks in 20% of the time typists spend, with higher quality

### Critical Patterns

- **Template 1b (When Fix Fails)**: "That didn't work. Let's revert to the last working state and try a different approach. What other options do we have?"
- **The Director's Tip**: Invoke principles explicitly in prompts: "Using Principle 4, break this into atomic steps with commits after each."
- **Workflow Selection**: Match workflow to task type—Quick Fix (P3+P4), Feature Dev (all), Refactoring (P2+P4+P5)
- **Health Score Check**: Before major work, audit your setup against the 0-7 scale
- Three complete workflows: debugging (investigation + verification), new feature (all principles), refactoring (decomposition + safety)

### Common Mistakes

- Treating principles as checklist (they're interconnected, not independent)
- Applying same workflow to all tasks (different situations need different principle emphasis)
- Forgetting to invoke principles explicitly (Claude responds better when principles are named)
- Skipping the health score audit (low scores predict session failures)
- Staying in typist mode (hoping prompts work instead of directing outcomes)
- Not having a recovery path (Template 1b should be automatic when fixes fail)

### Connections

- **Synthesizes**: All seven principles into integrated workflows
- **Enables**: The Director's Mindset—confident, proactive AI collaboration
- **Foundation for**: Part 2's applied workflows, where principles become automatic
