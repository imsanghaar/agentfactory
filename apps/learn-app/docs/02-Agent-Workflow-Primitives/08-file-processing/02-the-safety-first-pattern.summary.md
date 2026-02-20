### Core Concept

The safety-first pattern establishes constraints before destructive operations. Create a backup, verify it's complete, then proceed with confidence. The paradox: the backup constraint doesn't limit you — it frees you to experiment without fear.

### Key Mental Models

- **Safety enables action**: The backup constraint doesn't limit you. It frees you to experiment without fear. The 2 minutes you spend on backup save the 20 minutes of anxiety that would otherwise paralyze every decision.
- **Verification before trust**: Never assume a backup worked. Always confirm completeness with source-to-destination comparison. A backup that fails silently is worse than no backup — it gives false confidence.
- **Agents should ask, not assume**: A well-designed agent clarifies ambiguous requests ("What counts as important?") before acting. That single question is the difference between a helpful tool and a dangerous one.
- **Backup failures are real**: Permissions errors, disk space limits, and partial copies happen. Good agents check preconditions and report errors, not just successes.

### Critical Patterns

- **"Before [operation], create a backup of [what matters]"**: This universal safety pattern applies to files, code, databases, and any irreversible change.
- **"Verify the backup is complete. Show me any errors"**: Always ask the agent to compare counts between source and backup and surface any failures.
- **Principle 6 (Constraints and Safety)**: The constraint of "backup first" enables fearless experimentation.
- **Principle 3 (Verification)**: The workflow follows backup → verify → then execute. The order is the whole point.
- **Universal safety mindset**: Files (backup before moving), code (commit before refactoring), databases (export before modifying), systems (snapshot before changing settings). The common thread: create a reversible state before any irreversible action.

### Common Mistakes

- Skipping verification: A backup that fails silently is worse than no backup because it gives false confidence.
- Not clarifying what "important" means: Letting the agent assume what to backup can miss critical files.
- Creating backups after changes: Starting work without safety limits your ability to recover from mistakes.
- Ignoring backup errors: A "mostly complete" backup with 2 failed files gives false confidence. Always check for errors in backup output.

### Connections

- **Builds on**: Lesson 1 (folder survey), understanding of General Agents from Part 1
- **Leads to**: Organization workflows (Lesson 3) where safety protects against categorization errors; Recovery (Lesson 5) where this backup becomes your active recovery tool
