---
id: "0002"
title: "origin-story-implementation"
stage: green
date: 2025-12-17
surface: claude-code
model: claude-opus-4-5-20251101
feature: 042-origin-story-enhancement
branch: 034-origin-story-enhancement
user: mjs
command: /sp.implement
labels: [content, implementation, lesson-enhancement]
links:
  spec: specs/042-origin-story-enhancement/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md
  - apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.summary.md
tests:
  - null
---

## Prompt

Complete SDD workflow autonomously: Enhance Claude Code origin story lesson with factual content from Pragmatic Engineer source article. Optimize for clarity, logical flow, and narrative momentum. Each section introduces ONE core idea. Challenge common beliefs before presenting correct framing. Internal rewrite for density. Internal critique for generic phrasing.

## Response snapshot

Implemented complete lesson enhancement following 7-section structure:

1. **The Uncomfortable Truth** - Challenges "AI makes coding faster" with copy-paste friction reality
2. **What Actually Happened at Anthropic** - Boris Cherny, Sept 2024, Product Overhang discovery
3. **The Dogfooding Explosion** - Nov 2024 adoption curve (20%→50%→80%+), 5 PRs/day metric
4. **The Paradigm Shift** - Agentic vs Passive distinction with enhanced comparison table
5. **Why Terminal Integration Matters** - 5 reasons terminal is essential (not preference)
6. **The Self-Building Proof** - ~90% self-built statistic as paradigm validation
7. **Try With AI** - Updated prompts referencing lesson facts

Validation results:
- Zero closure phrases: PASS
- Section count: 6 H2 sections
- Word count: 1,731 (target 1,500-1,800)
- Image reference preserved: PASS
- Factual references: 7 verifiable facts
- Misconception challenges: 3

## Outcome

- Impact: Complete lesson rewrite with evidence-based narrative and emotional progression
- Tests: All quality gate checks passed
- Files: 01-origin-story.md (rewritten), 01-origin-story.summary.md (updated)
- Next prompts: Commit and create PR
- Reflection: Narrative momentum approach (confusion→clarity→confidence) creates stronger pedagogical flow than information-first structure

## Evaluation notes (flywheel)

- Failure modes observed: None - all validation checks passed
- Graders run and results (PASS/FAIL): Closure phrases PASS, word count PASS, image PASS, factual refs PASS
- Prompt variant (if applicable): N/A
- Next experiment: Apply narrative momentum pattern to other origin/concept lessons
