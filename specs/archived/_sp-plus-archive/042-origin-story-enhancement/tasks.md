# Tasks: Origin Story Lesson Enhancement

**Feature**: 042-origin-story-enhancement
**Created**: 2025-12-17
**Plan**: specs/042-origin-story-enhancement/plan.md

## Task Overview

| ID | Task | Status | Dependencies |
|----|------|--------|--------------|
| T1 | Extract preservable elements from existing lesson | pending | - |
| T2 | Write Section 1: The Uncomfortable Truth | pending | T1 |
| T3 | Write Section 2: What Actually Happened | pending | T1 |
| T4 | Write Section 3: The Dogfooding Explosion | pending | T1 |
| T5 | Write Section 4: The Paradigm Shift | pending | T1 |
| T6 | Write Section 5: Terminal Integration | pending | T1 |
| T7 | Write Section 6: The Self-Building Proof | pending | T1 |
| T8 | Write Section 7: Try With AI | pending | T1 |
| T9 | Assemble complete lesson file | pending | T2-T8 |
| T10 | Update summary file | pending | T9 |
| T11 | Run quality validation | pending | T9, T10 |
| T12 | Apply internal critique and fix issues | pending | T11 |

---

## Detailed Tasks

### T1: Extract Preservable Elements

**Description**: Read existing lesson and extract elements that must be preserved unchanged.

**Inputs**:
- `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`

**Outputs**:
- YAML frontmatter (exact copy)
- Image reference path
- Comparison table structure
- Try With AI prompt categories

**Acceptance Criteria**:
- [ ] Frontmatter extracted with all metadata intact
- [ ] Image path identified and documented
- [ ] Table column structure captured
- [ ] 4 Try With AI categories identified

---

### T2: Write Section 1 - The Uncomfortable Truth About AI Coding Tools

**Description**: Challenge the common belief that "AI makes coding faster" by exposing copy-paste friction.

**ONE IDEA**: Most AI coding tools create friction, not remove it

**Content Requirements**:
- Open with common belief
- Challenge with reality (copy-paste adds friction)
- Describe hidden costs (context switching)
- End with curiosity-opening question

**Constraints**:
- ~150 words
- No statistics (saved for later)
- No closure phrases
- Must create cognitive dissonance

**Acceptance Criteria**:
- [ ] Single idea: friction, not speed
- [ ] Ends with question or curiosity hook
- [ ] No "in conclusion" or similar phrases

---

### T3: Write Section 2 - What Actually Happened at Anthropic

**Description**: Reveal the origin through Boris Cherny's discovery of Product Overhang.

**ONE IDEA**: Boris Cherny discovered the Product Overhang

**Content Requirements**:
- Introduce Boris Cherny (founding engineer)
- Timeline: September 2024
- Describe experiment: Give Claude filesystem access
- Name insight: Product Overhang

**Facts to Include** (from source):
- Boris Cherny joined Anthropic September 2024
- Began prototyping with Claude 3.6
- Claude naturally explored codebases when given filesystem access

**Constraints**:
- ~200 words
- Cite source implicitly through paraphrase

**Acceptance Criteria**:
- [ ] Boris Cherny named with role
- [ ] September 2024 timeline stated
- [ ] Product Overhang concept explained
- [ ] Opens curiosity: What happened when others tried it?

---

### T4: Write Section 3 - The Dogfooding Explosion

**Description**: Show how internal adoption exceeded all expectations.

**ONE IDEA**: Internal adoption revealed something unexpected

**Content Requirements**:
- Challenge belief: "Developers resist new tools"
- November 2024 dogfooding launch
- Adoption curve: 20% → 50% → 80%+
- Productivity metrics: 5 PRs/day

**Facts to Include** (from source):
- November 2024: Dogfooding-ready version
- 20% of Engineering adopted day one
- 50% by day five
- 80%+ use daily by GA (May 2025)
- 5 PRs per engineer daily
- $500M+ annual run-rate

**Constraints**:
- ~200 words
- Use "as of mid-2025" for volatile metrics

**Acceptance Criteria**:
- [ ] November 2024 timeline stated
- [ ] Adoption percentages included
- [ ] 5 PRs/day metric included
- [ ] Opens curiosity: What made it spread?

---

### T5: Write Section 4 - The Paradigm Shift

**Description**: Explain the agentic vs passive distinction with enhanced comparison table.

**ONE IDEA**: The fundamental distinction that explains everything

**Content Requirements**:
- Define passive AI (Q&A without context)
- Define agentic AI (active collaboration)
- Enhanced comparison table
- Reference existing diagram

**Preserve from existing**:
- Table structure (7 rows)
- Image reference path

**Constraints**:
- ~250 words (including table)
- Keep existing image reference exactly

**Acceptance Criteria**:
- [ ] Table has 7 aspect rows
- [ ] Image reference preserved
- [ ] Consultant vs Pair Programmer metaphor
- [ ] Opens curiosity: Why terminal?

---

### T6: Write Section 5 - Terminal Integration

**Description**: Explain why terminal is essential, not just preference.

**ONE IDEA**: Terminal isn't preference, it's essential to the paradigm

**Content Requirements**:
- Address GUI preference objection
- 5 reasons terminal is essential
- Transparency builds trust

**Preserve/Enhance from existing**:
- 5 reasons structure
- Enhance descriptions with specificity

**Constraints**:
- ~200 words
- No new reasons (stick to 5)

**Acceptance Criteria**:
- [ ] 5 reasons present
- [ ] Objection addressed upfront
- [ ] Opens curiosity: What does this mean for work?

---

### T7: Write Section 6 - The Self-Building Proof

**Description**: Present the ~90% statistic as paradigm shift proof.

**ONE IDEA**: ~90% of Claude Code was written by Claude Code

**Content Requirements**:
- Challenge belief: "AI can't build complex systems"
- Present statistic: ~90% self-built
- Team/release context
- Connect to reader's future

**Facts to Include** (from source):
- ~90% of Claude Code written by itself
- Team grew from 2 to ~10 engineers
- 60-100 internal releases daily
- 1 external npm release daily

**Constraints**:
- ~150 words
- This is the climactic section

**Acceptance Criteria**:
- [ ] ~90% statistic stated
- [ ] Misconception challenged first
- [ ] Opens curiosity: What does this mean for you?

---

### T8: Write Section 7 - Try With AI

**Description**: Preserve structure, enhance prompts with factual context.

**ONE IDEA**: Convert understanding into capability

**Preserve from existing**:
- 4 prompt categories
- Active collaboration structure
- No meta-commentary

**Enhance**:
- Add factual references to prompts
- Embed safety note (not standalone)

**Constraints**:
- ~200 words
- Must end the lesson (no sections after)

**Acceptance Criteria**:
- [ ] 4 categories preserved
- [ ] Safety note embedded
- [ ] No "What's Next" or "Summary" after
- [ ] Prompts reference lesson facts

---

### T9: Assemble Complete Lesson File

**Description**: Combine all sections with preserved frontmatter.

**Structure**:
```
[YAML Frontmatter - preserved exactly]

# The Claude Code Origin Story and Paradigm Shift

[Section 1]
---
[Section 2]
---
[Section 3]
---
[Section 4 with table and image]
---
[Section 5]
---
[Section 6]
---
[Section 7 - Try With AI - FINAL SECTION]
```

**Acceptance Criteria**:
- [ ] Frontmatter preserved exactly
- [ ] All 7 sections present
- [ ] Section separators (---) between major sections
- [ ] Try With AI is final section
- [ ] ~1500-1800 words total

---

### T10: Update Summary File

**Description**: Add new mental models and key facts to summary.

**New Mental Models**:
1. Product Overhang
2. Friction Removal > Feature Addition
3. Self-Building Proof

**New Key Facts**:
- Timeline: Sept 2024 → Nov 2024 → May 2025
- Adoption: 20% → 50% → 80%+
- Productivity: 5 PRs/day
- Self-building: ~90%

**Acceptance Criteria**:
- [ ] 3 new mental models added
- [ ] Timeline facts added
- [ ] Metrics added
- [ ] Existing structure preserved

---

### T11: Run Quality Validation

**Description**: Execute all quality gate checks.

**Checks**:
```bash
# Zero closure phrases
grep -i "in conclusion\|to summarize\|overall\|in short" lesson.md

# Section count
grep "^## " lesson.md | wc -l

# Word count (~1500-1800)
wc -w lesson.md

# Image reference preserved
grep "pub-80f166e40b854371ac7b05053b435162" lesson.md
```

**Acceptance Criteria**:
- [ ] Zero closure phrases found
- [ ] 7-8 H2 sections
- [ ] 1500-1800 words
- [ ] Image reference present
- [ ] Frontmatter valid YAML

---

### T12: Apply Internal Critique

**Description**: Review for generic phrasing, shallow explanations, missed nuance.

**Critique Checklist**:
- [ ] Remove "very", "really", "important" modifiers
- [ ] Every claim has supporting evidence or reasoning
- [ ] Product Overhang nuance captured (not oversimplified)
- [ ] Each section ending creates forward momentum
- [ ] No "this is important" meta-commentary

**Acceptance Criteria**:
- [ ] All critique items addressed
- [ ] Final version ready for commit
