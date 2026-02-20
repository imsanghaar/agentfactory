### Core Concept

A verification-first workflow tests the entire pipeline with known data before processing real files. The capstone challenge: point Claude Code at a folder of bank statement CSVs and produce a categorized tax report with verified totals in 40 minutes. All Seven Principles converge naturally — Bash orchestrates, Python executes, test data verifies, small steps decompose, files persist, guards constrain, and review sections observe.

### Key Mental Models

- **Verification-first orchestration**: Create test data with hand-calculated totals, verify the pipeline matches, then process real data. Trust is earned through proof, not assumption.
- **Seven Principles convergence**: Each principle appears naturally in a well-structured workflow — this isn't a checklist to force, but a pattern that emerges from good practice.
- **Patterns over tools**: The specific tools (Python, regex, find/xargs) matter less than the transferable patterns: describe problems, verify before trusting, mention edge cases, make tools permanent.

### Critical Patterns

- **The verification-first prompt**: "IMPORTANT: First verify your approach with test data before touching real files." This phrase triggers the agent to build a test-first workflow.
- **CSV merging without duplicate headers**: `head -1 first.csv > combined.csv` then `tail -n +2 -q *.csv >> combined.csv` creates one file with a single header row.
- **Ambiguous transaction flagging**: Items that don't match any category or match multiple categories get flagged for human review rather than silently dropped or miscategorized.

### Common Mistakes

- Processing real data before verifying with test data — if the categorization logic is wrong, you won't know until you've already generated an incorrect report
- Not flagging ambiguous items — silently skipping uncategorized transactions means potential deductions are lost
- Treating the workflow as a one-time conversation — converting it into a reusable script (`./tax-prep.sh ~/finances/2026/`) means next year requires zero re-prompting

### Connections

- **Builds on**: All previous lessons — broken math (L1), testing loop (L2), CSV parsing (L3), permanent toolkit (L4), data wrangling (L5)
- **Leads to**: Practice exercises (Lesson 7) and more complex data workflows in later chapters
