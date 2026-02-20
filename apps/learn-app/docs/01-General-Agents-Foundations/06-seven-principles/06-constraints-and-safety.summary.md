### Core Concept

Constraints enable autonomy—thoughtful safety measures and guardrails are what allow you to give AI systems meaningful power without risking damage. The paradox: when you trust the safety model, you give agents more autonomy. Without constraints, you'd never let them do meaningful work.

### Key Mental Models

- **The Safety Mantra**: "If it's in git, it's recoverable." Uncommitted changes? `git checkout` restores them. Bad commit? `git reset` removes it. Already pushed? `git revert` creates an undo commit. Git is your safety net.
- **The Soft Sandbox**: Before risky work, `git checkout -b experiment`. Work freely. If it fails, `git checkout main && git branch -D experiment`. Zero damage, full learning.
- **Trust Gradualism**: Phase 1 (observation) → Phase 2 (supervised) → Phase 3 (selective autonomy) → Phase 4 (calibrated autonomy). Build trust through evidence, not hope.
- **Safety Hierarchy (Defense in Depth)**: Five layers from Technical Constraints through Permission Controls, Environment Isolation, Process Controls, to Human Verification.

### Key Facts

- **Destructive operations**: `rm -rf`, `git reset --hard`, `git push --force`, `DROP TABLE`, `sudo`
- **Safe sandbox strategies**: Git branches (simplest), Docker containers, staging environments, separate credentials
- **Trust signals**: Error rate, correction ease, pattern adherence, risk awareness

### Critical Patterns

- **Pre-session checklist**: Correct directory? Correct branch? Uncommitted work backed up?
- **The Safety Hook**: Add to prompts: "Before any destructive operation, tell me what you're about to do and wait for approval."
- **Guardrail Template**: "You have permission to [specific actions]. You must ask before [risky actions]. You must never [forbidden actions]."
- **Emergency Cheat Sheet**: Stop (`Ctrl+C`) → Assess (`git status`) → Revert (`git checkout .`) → Review (what constraint would have prevented this?)

### Common Mistakes

- Zero to full autonomy overnight (trust should be graduated through phases)
- No rollback plan before starting (always know how to revert)
- Same permission level for all tasks (prototype vs production need different safety)
- Thinking safety means restricting to uselessness (constraints should be targeted, not blanket)
- Forgetting git branch as sandbox (the simplest isolation mechanism, always available)

### Connections

- **Builds on**: Principle 5 (State Persistence)—safety rules encoded in CLAUDE.md become persistent and automatic
- **Leads to**: Principle 7 (Observability)—constraints only effective if you can see when they're triggered
- **Synergy with P4**: Git commits are both decomposition units AND reversibility mechanisms
