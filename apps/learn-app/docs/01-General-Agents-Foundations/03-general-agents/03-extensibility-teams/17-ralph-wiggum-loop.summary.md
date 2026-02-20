### Core Concept

Ralph Wiggum Loop is a Claude Code plugin that enables autonomous iteration—Claude runs a task, checks results, identifies problems, fixes them, and repeats until completion criteria are met, eliminating manual feedback loop overhead. Always use with safety guardrails.

### Key Mental Models

- **Autonomous Execution**: Claude operates independently through multiple iterations without requiring you to manually copy errors, paste feedback, and wait—the Stop hook intercepts exits and reinjects continuation prompts
- **Objective Completion**: Success must be verifiable through clear signals (tests passing, linter showing "0 problems", build succeeding)—not subjective quality judgment
- **Cost-Aware Automation**: Long loops can consume $50-100+ in API credits; always set `--max-iterations` and use version control checkpoints

### Critical Patterns

- Install from marketplace: `/plugin marketplace add anthropics/claude-plugins-official` then `/plugin install ralph-loop@claude-plugins-official`
- **Embedded promise pattern (recommended)**: Explicitly instruct Claude to output completion marker
  ```bash
  /ralph-loop "Task description:
  - Requirement 1
  - Requirement 2
  Output <promise>DONE</promise> when complete." \
  --max-iterations 20 \
  --completion-promise "DONE"
  ```
- Alternative (natural output): `/ralph-loop "Fix all ESLint errors" --max-iterations 20 --completion-promise "0 problems"`
- Emergency exit: `/cancel-ralph` if loop gets stuck on same error 3+ times
- **Golden rule**: Use when success is objective, verifiable, deterministic—measurable by tools, NOT human judgment
- Decision criteria: 10+ iterations expected AND clear completion signal AND no human judgment required

### Common Mistakes

- Running loops without `--max-iterations`—can burn through budget on impossible tasks
- Vague completion promises ("everything works") instead of objective signals—use embedded `<promise>` pattern
- **Using for tasks requiring human judgment**—strategy, aesthetics, priorities need human input, not autonomous loops
- Relying on unpredictable tool output instead of embedded promise pattern for completion signals
- Using for multi-goal tasks ("fix bugs AND add features")—break into separate loops instead
- Not using version control checkpoints—makes rollback difficult if loop produces unwanted changes
- Blindly accepting results—always review the final output before merging

### Connections

- **Builds on**: Hooks (Lesson 15) for Stop hook mechanics, Plugins (Lesson 16) for marketplace installation
- **Leads to**: Digital FTE autonomous execution patterns (Part 6-7), advanced custom hook creation (Part 5)
