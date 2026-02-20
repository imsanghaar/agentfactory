### Core Concept

Real-world CSV data has commas inside quoted fields (like `"AMAZON, INC."`) that break simple tools like awk — silently producing wrong results with no error. Python's `csv` module understands quoting rules and handles these edge cases correctly. When data comes from outside your control, always use a proper CSV parser.

### Key Mental Models

- **The CSV parsing trap**: `awk -F','` splits on EVERY comma, including ones inside quotes. A field like `"AMAZON, INC."` becomes two broken fields. The worst part: some rows work fine, so the bug hides in plain sight.
- **Right tool for the job**: awk works for data you control (log files, tab-separated). For any CSV from an external source (bank exports, downloaded datasets), use Python's csv module.
- **Discovery-driven debugging**: Try the obvious approach first (awk), see it fail yourself, then bring that specific failure to Claude Code. You teach the agent about the problem; the agent teaches you about the right tool.

### Critical Patterns

- Try the naive approach yourself first — run `awk` on a quoted CSV row and see it break before asking for help
- Prompt pattern: "I tried [approach] but it breaks on [specific case]. How do I handle this correctly?"
- `csv.reader(sys.stdin)` handles quoted fields, escaped quotes, and different line endings automatically
- Mentioning edge cases in your prompt guides the agent to choose robust tools over simple ones

### Common Mistakes

- Splitting CSV on commas with awk or cut — this silently produces wrong results on any field containing a comma
- Not mentioning known data quirks in your prompt — "sum the third column" might get awk; "sum the Amount column, some merchants have commas" gets csv module
- Forgetting that `next(reader)` skips the header row — without it, the header line gets processed as data

### Connections

- **Builds on**: sum.py (Lesson 1) and verification (Lesson 2)
- **Leads to**: Making scripts permanent (Lesson 4) — if you have to remember where a tool lives, it's not a tool yet
