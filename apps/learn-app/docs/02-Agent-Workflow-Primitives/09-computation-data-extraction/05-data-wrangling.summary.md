### Core Concept

Dr. Pepper is not a doctor. Simple keyword matching produces false positives that corrupt your data. Regex word boundaries (`\b`) match whole words only, and false-positive guard lists checked before categories prevent known bad matches. The workflow: build a naive version, discover it's wrong, then fix with precision.

### Key Mental Models

- **Iterate, don't anticipate**: Build a first version, run it, and find false positives yourself. Then fix them. This produces better results than trying to anticipate every edge case upfront.
- **Word boundaries as precision**: `\bCVS\b` matches "CVS PHARMACY" but not "CVSMITH." The `\b` marks word edges, turning broad matches into precise ones.
- **Guards-run-first ordering**: False positive patterns are checked BEFORE category patterns. Order matters — Dr. Pepper gets excluded before "DR" can trigger a medical match.

### Critical Patterns

- Categorization prompt: "Categorize [data] by [criteria]." Start simple, then fix false positives with: "[X] is showing up as [Y]. Fix it."
- Regex word boundaries: `r'\bKEYWORD\b'` for standalone word matching
- Batch processing: `find folder/ -name "*.csv" | xargs cat | python script.py` processes multiple files in one command

### Common Mistakes

- Trusting the first version of a categorizer without scanning the output for false positives — Dr. Pepper as "medical" inflates your tax deductions by $204.99
- Using `if 'CVS' in text` instead of `re.search(r'\bCVS\b', text)` — substring matching catches partial words like CVSMITH
- Processing files one at a time when `find | xargs` handles the batch automatically

### Connections

- **Builds on**: CSV parsing (Lesson 3) and permanent tools (Lesson 4)
- **Leads to**: Full tax preparation capstone (Lesson 6) — one conversation, one command, a full year of data
