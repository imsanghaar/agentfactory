### Core Concept

Effective organization with General Agents follows a collaborative design pattern. The agent proposes categories, you refine them, then the agent documents the rules for reuse. The best categorization systems aren't designed perfectly upfront — they're discovered through errors and corrections.

### Key Mental Models

- **Propose-refine-iterate**: The agent suggests categories based on your actual files. You adjust based on your needs. The agent adapts. You classify by function (CSV is a spreadsheet), the agent classifies by format (CSV is text). When you correct, the rules get smarter.
- **State persistence**: Rules get saved to `rules.md` with version tracking. The rules are the product — organized folders are just the output. Next month your folders will be outdated, but `rules.md` is reusable forever.
- **Test before scaling**: Always try on one file first. If the test works, proceed with confidence. If not, you caught the problem early.
- **Dry run before execution**: Ask the agent to show what it _would_ do without doing it. The single-file test checks the mechanism works; the dry run checks the decisions are right.
- **Two-layer categorization**: Extension-based rules are layer one. Content-based analysis (using `file` command to detect actual type) is layer two. When your "misc" bucket exceeds 20% of files, dig deeper.

### Critical Patterns

- **"Help me organize [folder]. Analyze what's there and suggest categories based on my actual files"**: This triggers collaborative rule design.
- **"Test on ONE file first"**: This single instruction prevents potential chaos by validating before batch operations.
- **"Show me what you'll do before doing it"**: Dry-run prompt that makes the agent's plan visible before it becomes irreversible (Principle 7: Observability).
- **"Document the rules so we can reuse them"**: Creates persistent state (Principle 5) that survives beyond this session.
- **Principle 4 (Decomposition)**: Small, reversible testing before scaling to hundreds of files.
- **Case-insensitive matching**: A common bug where `.PDF` files fall through to misc/ because rules only match `.pdf`. Always use case-insensitive extension matching.

### Common Mistakes

- Making up categories as you go instead of analyzing what you actually have: Your files may not fit predefined categories.
- Accepting a large misc/ bucket: If 49% of files are "miscellaneous," your categorization has a problem. Dig deeper with content analysis.
- Forgetting to document rules: Without `rules.md`, you'll re-decide categories every time your folder fills up.
- Testing on all files at once: One mistake miscategorizes everything. Test on one file first.
- Case-sensitive extension matching: `.PDF`, `.DOCX`, and `.TXT` files silently fall through to misc/.

### Connections

- **Builds on**: Lessons 1-2 (survey and safety), Principle 5 (Persisting State) from Part 1
- **Leads to**: Batch operations (Lesson 4) where rules become automated scripts
