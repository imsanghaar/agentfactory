### Core Concept

The capstone tests not whether you know six workflows, but whether you know which one to reach for under pressure. Different scenarios require different workflow orders — urgency overrides the normal sequence, recurring problems need scripts not commands, and recovery starts with diagnosis not treatment.

### Key Mental Models

- **Triage under pressure**: Urgency changes workflow order. When someone is waiting, search first, organize later. When starting fresh, survey → backup → organize. When something broke, compare against backup first. When the problem recurs, ask for a script.
- **Toolkit over memory**: Every expert builds a personal prompt toolkit — proven patterns documented in `MY-PROMPT-TOOLKIT.md` for future reuse. The organized folders will get messy again; the templates are permanently useful.
- **Manual to automated bridge**: Your `rules.md` becomes the AI Employee's decision rules. Your verification patterns become its supervision methods. The gap between "I type a prompt" and "it runs automatically" is just a scheduler — same logic, same safety, same verification.
- **Command vocabulary**: You don't memorize syntax, but recognizing patterns (`ls`, `find`, `cp`, `mv`, `grep`, `diff`, `chmod`, pipes, `xargs`) helps you verify the agent is doing the right thing.

### Critical Patterns

- **Workflow selection**: Urgent search → go straight to search (Lesson 6). Fresh start → survey, backup, organize. Botched script → compare against backup first. Recurring problem → generate a reusable script.
- **"Help me create MY-PROMPT-TOOLKIT.md"**: Documents fill-in-the-blank templates for each workflow — the chapter's most important deliverable.
- **Seven Principles reflection**: Each lesson naturally surfaced principles — P1 (Bash) in survey, P6 (Safety) in backup, P5 (State) in rules, P4 (Decomposition) in testing, P2 (Code) in scripts, P3 (Verification) throughout.
- **The automation bridge**: Manual workflows map directly to automated code — `create_timestamped_backup()` is Lesson 2, `apply_rules()` is Lesson 3, `verify_all_files_accounted_for()` is Lesson 5. Automation removes you as the trigger; the rules, logic, and safety stay identical.

### Common Mistakes

- Treating each lesson as isolated: The power comes from combining all workflows systematically.
- Not documenting your toolkit: You'll re-discover patterns instead of building on past work.
- Using the same workflow order for every scenario: Urgency, fresh starts, and recovery all require different sequences.
- Missing the automation connection: Manual prompting today becomes automated decision rules later. Your rules.md, logs, and verification habits are exactly what AI Employees need.

### Connections

- **Builds on**: Lessons 1-6 (all workflows including error recovery), all Seven Principles from Part 1
- **Leads to**: AI Employees where manual prompting evolves into autonomous automation
