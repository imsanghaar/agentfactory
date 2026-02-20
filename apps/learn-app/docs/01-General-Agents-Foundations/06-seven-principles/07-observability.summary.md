### Core Concept

You cannot debug what you cannot see. Observability—visibility into what the AI is doing, why it's doing it, and what happened—transforms AI from an unpredictable black box into a debuggable system. Without it, you're guessing; with it, you're engineering.

### Key Mental Models

- **Three Pillars of Observability**: What happened (Action), Why it happened (Rationale), What resulted (Result). All three needed for full debugging capability.
- **Scan for Verbs**: When reading logs, ignore timestamps. Look for verbs: READ, EDIT, TEST, FAIL, COMPLETE. Red flag: EDIT without TEST after it.
- **Real-Time vs Post-Mortem**: Real-time catches problems as they happen (progress bars, streaming). Post-mortem reconstructs what went wrong (logs, history). Both essential.
- **The 2-Minute Audit**: After significant work, spend 2 minutes reviewing what Claude did. Check the activity log. Verify changes match intent. Make this automatic.
- **Rationalization Warning**: Claude will confidently explain its reasoning even when that reasoning is flawed. Don't mistake eloquent explanation for correct action.

### Key Facts

- **Synergy with Principle 3**: Observability IS verification for AI behavior. You verify code with tests; you verify AI with logs.
- **Log locations**: Claude Code (`~/.claude/logs/`), git history (`git log --oneline`), checkpoint history (`/rewind`)
- **jq for filtering**: `cat session.log | jq 'select(.level == "error")'` to quickly find problems

### Critical Patterns

- **The Verb Scan**: Skim logs looking only for action verbs, not details. EDIT without TEST = problem.
- **jq Error Query**: `cat session.log | jq 'select(.level == "error")'` to filter for problems
- **Progress Reporting Prompt**: "After each step, report: what you did, what changed, what's next"
- **Post-Session Review**: Before closing, check activity log for unexpected actions
- Three workflow patterns: Explain Before Executing, Checkpoint After Major Steps, Summary After Completion

### Common Mistakes

- Trusting eloquent explanations (Claude rationalizes confidently even when wrong)
- Ignoring logs until something breaks (proactive review catches problems early)
- Only checking final output (intermediate steps often reveal issues)
- No systematic review habit (the 2-minute audit should be automatic)
- Confusing verbosity with observability (long explanations ≠ visible actions)
- Silent failures: AI says "Done!" but something actually failed

### Connections

- **Builds on**: Principle 6 (Constraints)—observability validates that safety constraints are working
- **Leads to**: Lesson 9 (Putting It Together)—observability enables the Director's Mindset by making AI actions transparent
- **Synergy with P3**: Observability for AI behavior is equivalent to verification for code
