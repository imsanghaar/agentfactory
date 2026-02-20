### Core Concept

Recovery confidence matters more than mistake avoidance. You deliberately practice breaking things and restoring from backup so that when real mistakes happen, you know exactly what to do.

### Key Mental Models

- **Deliberate practice over fear**: Break something on purpose in a safe environment. Recovery becomes muscle memory, not panic.
- **Backup as undo button**: Your Lesson 2 backup isn't just insurance — it's an active tool you use when things go wrong.
- **Compare before restoring**: Always check what's different between current state and backup before restoring. Don't blindly overwrite.
- **Agent is ephemeral, code is eternal**: Asking the agent to recover files works once. A recovery script works forever — same steps, same result, no agent needed.

### Critical Patterns

- **"Compare the current state against my backup"**: Triggers the agent to run `diff` and show exactly what changed.
- **"Restore [specific files] from backup"**: Targeted recovery is safer than restoring everything.
- **Principle 3 (Verification)**: After every recovery, verify the restored files are correct.
- **Principle 2 (Code as Universal Interface)**: If you're asking the agent to do the same recovery twice, ask it to write a script instead. Trade a conversation for a tool.
- **Principle 6 (Constraints and Safety)**: The backup created in Lesson 2 enables fearless experimentation here.

### Common Mistakes

- Panicking and restoring everything: Targeted recovery preserves intentional changes while fixing mistakes.
- Not verifying after restoration: A restored file might be an older version than you expected.
- Skipping the comparison step: You need to understand what went wrong before fixing it.

### Connections

- **Builds on**: Lesson 2 (safety-first backup), Lesson 3 (organized files to practice with)
- **Leads to**: Search workflows (Lesson 6) and capstone toolkit (Lesson 7) with recovery confidence
