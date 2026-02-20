### Core Concept
30-60% of tokens in typical CLAUDE.md files add no value—they consume attention budget without improving output. The 4-question audit framework distinguishes signal (what Claude needs) from noise (what wastes tokens), enabling a lean, effective CLAUDE.md under 60 lines.

### Key Mental Models
- **The Instruction Limit**: LLMs reliably follow ~150-200 instructions. Claude Code's system prompt uses ~50, leaving you ~100-150 before degradation. Every noisy instruction steals budget from valuable ones.
- **The 4-Question Filter**: For each line, ask: (1) Would Claude ask about this? (2) Could Claude infer it from existing materials? (3) Does this change frequently? (4) Is this a default convention Claude already knows?
- **Three-Zone Positioning**: Information in the first and last 10% of context gets high attention; the middle 80% gets ~30% less recall. Put critical rules at top, workflows at bottom, reference material in the middle.

### Critical Patterns
- Apply the audit framework systematically—classify each section as SIGNAL, NOISE, or PARTIAL
- Use progressive disclosure: move detailed content to `docs/*.md` files, reference with one line in CLAUDE.md
- Re-run comparison tests: measure quality before and after trimming to verify you didn't cut too much

### Common Mistakes
- Keeping "helpful" noise (context Claude can learn from reading files)—you're paying twice for stale duplicates
- Insufficient terseness: "Please always ensure you thoroughly review" → "Review" saves tokens, same meaning
- Not testing the result: audit without comparison testing is guesswork

### Connections
- **Builds on**: Context engineering definition and context rot (Lesson 1)
- **Leads to**: Context architecture with CLAUDE.md, Skills, Subagents, Hooks (Lesson 3)
