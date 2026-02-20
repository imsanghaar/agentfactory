# Feature Specification: Origin Story Lesson Enhancement

**Feature Branch**: `042-origin-story-enhancement`
**Created**: 2025-12-17
**Status**: Draft
**Input**: Enhance Claude Code origin story lesson with factual content from Pragmatic Engineer source article, optimized for clarity, logical flow, and narrative momentum.

## Context & Problem Statement

The current lesson `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md` makes narrative claims without factual substantiation:

- "Within weeks, Claude Code wasn't just being used—it was transforming how developers worked" (no data)
- "The team expected a niche audience" (no source)
- Timeline and key people completely absent

**Source of truth**: Pragmatic Engineer article "How Claude Code is Built" contains verified facts:
- Timeline: Sept 2024 prototype → Nov 2024 dogfooding → May 2025 GA
- Key people: Boris Cherny (founder), Sid Bidasaria (subagents), Cat Wu (PM)
- Metrics: 80%+ daily usage, 5 PRs/day, $500M+ run-rate
- Product Overhang Discovery: Claude already had capability, just needed filesystem access
- ~90% self-built statistic

**Problem**: Current lesson tells a vague "origin story" without the actual origin story.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Reader Understands the Paradigm Shift Through Evidence (Priority: P1)

A developer reads the lesson expecting to understand WHY Claude Code matters. They start skeptical ("isn't this just another AI tool?"). By the end, they understand the paradigm shift through concrete evidence, not marketing claims.

**Why this priority**: Without evidence-based narrative, the lesson fails its core purpose.

**Independent Test**: Reader can cite 3 specific facts (timeline, metrics, design philosophy) that substantiate the paradigm shift claim.

**Acceptance Scenarios**:

1. **Given** a reader skeptical of AI hype, **When** they read the timeline section, **Then** they understand the actual development progression (Sept 2024 → May 2025)
2. **Given** a reader unfamiliar with Claude Code, **When** they encounter the Product Overhang insight, **Then** they grasp the technical discovery (capability existed, product unlocked it)
3. **Given** a reader comparing AI tools, **When** they see adoption metrics, **Then** they have concrete data to evaluate (80%+ usage, 5 PRs/day)

---

### User Story 2 - Reader Experiences Narrative Momentum (Priority: P2)

A developer progresses through the lesson with increasing clarity and confidence. Each section introduces ONE core idea. Confusion resolves progressively. Curiosity builds rather than closes.

**Why this priority**: Pedagogical effectiveness requires emotional progression from skepticism → clarity → momentum.

**Independent Test**: Reader can identify which single idea each section introduced, and where their understanding shifted.

**Acceptance Scenarios**:

1. **Given** a reader at section N, **When** they encounter section N+1, **Then** only ONE new core idea appears (additional ideas deferred)
2. **Given** a reader finishing a section, **When** they read the section ending, **Then** curiosity opens rather than closes (no summarizing phrases)
3. **Given** a reader at the end, **When** they reflect on their journey, **Then** they recognize progression from confusion → clarity → confidence

---

### User Story 3 - Reader Challenges Preconceptions (Priority: P2)

A developer arrives with common misconceptions about Claude Code ("just ChatGPT in terminal", "replaces programmers", "only for CLI enthusiasts"). The lesson explicitly challenges these beliefs before presenting correct framing.

**Why this priority**: Misconception correction is more effective than information delivery.

**Independent Test**: Reader can name 2 misconceptions they held that the lesson corrected.

**Acceptance Scenarios**:

1. **Given** a reader believing "Claude Code is ChatGPT in terminal", **When** they read the paradigm shift section, **Then** they understand agentic vs passive distinction
2. **Given** a reader believing "AI replaces developers", **When** they read the friction removal insight, **Then** they understand AI handles friction, humans handle creativity
3. **Given** a reader believing "terminal = harder", **When** they read terminal integration section, **Then** they understand terminal removes context-switching friction

---

### User Story 4 - Lesson Passes Factual Accuracy Standards (Priority: P1)

All claims in the lesson have verifiable sources. No hallucinated statistics. Timeline, people, and metrics traceable to Pragmatic Engineer article.

**Why this priority**: Constitutional Principle 3 (Factual Accuracy) is mandatory.

**Independent Test**: Every factual claim can be traced to source article or official documentation.

**Acceptance Scenarios**:

1. **Given** a factual claim (e.g., "80%+ daily usage"), **When** traced, **Then** source article confirms it
2. **Given** a timeline date (e.g., "November 2024 dogfooding"), **When** verified, **Then** source article confirms it
3. **Given** a named person (e.g., "Boris Cherny"), **When** verified, **Then** role matches source article

---

### Edge Cases

- What if reader skips to middle sections? Each section should be comprehensible with minimal back-reference.
- What if Pragmatic Engineer article becomes inaccessible? Core facts should be paraphrased, not just linked.
- What if metrics change over time? Use "as of [date]" framing for volatile statistics.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Lesson MUST include concrete timeline (Sept 2024 prototype → Nov 2024 dogfooding → May 2025 GA)
- **FR-002**: Lesson MUST name key people with roles (Boris Cherny - founding engineer, Sid Bidasaria - subagents, Cat Wu - PM)
- **FR-003**: Lesson MUST include adoption metrics with source attribution (80%+ daily usage, 5 PRs/day, $500M+ run-rate)
- **FR-004**: Lesson MUST explain Product Overhang Discovery (capability existed, product unlocked it through filesystem access)
- **FR-005**: Lesson MUST include self-building statistic (~90% written by Claude Code itself) as paradigm shift evidence
- **FR-006**: Lesson MUST challenge common misconceptions explicitly before presenting correct framing
- **FR-007**: Each section MUST introduce only ONE core idea (additional ideas deferred to later sections)
- **FR-008**: Section endings MUST open curiosity, not close it (no "in conclusion", "to summarize", "overall", "in short")
- **FR-009**: Lesson MUST NOT use summarizing phrases that close curiosity
- **FR-010**: Lesson MUST maintain emotional progression: confusion → clarity → confidence → momentum
- **FR-011**: All factual claims MUST be traceable to Pragmatic Engineer source or official documentation
- **FR-012**: Lesson MUST update `.summary.md` companion file with key facts and mental models
- **FR-013**: Lesson structure MUST preserve existing pedagogical layer metadata (Layer 1, A2 proficiency)

### Narrative Structure Requirements

- **NR-001**: Before presenting correct framing, explicitly challenge the most common belief about the topic
- **NR-002**: After writing each section, apply internal rewrite to: remove redundancy, increase conceptual density, preserve length and tone
- **NR-003**: Before finalizing, apply internal critique for: generic phrasing, shallow explanations, missed nuance - fix all issues
- **NR-004**: Assume reader starts confused and skeptical; design for progressive resolution
- **NR-005**: Each section ending should create forward momentum, not closure

### Content Structure (Proposed Outline)

**Section 1: The Uncomfortable Truth About AI Coding Tools**
- ONE IDEA: Most AI coding tools create friction, not remove it
- CHALLENGE: "AI makes coding faster" → Actually, copy-paste workflow is slower than no AI
- Opens curiosity: What would friction-free AI look like?

**Section 2: What Actually Happened at Anthropic (September 2024)**
- ONE IDEA: Boris Cherny's prototype discovery - Product Overhang
- FACTS: Timeline, key person, the insight (Claude already had capability, just needed filesystem access)
- Opens curiosity: What happened when they let others try it?

**Section 3: The Dogfooding Explosion (November 2024)**
- ONE IDEA: Internal adoption revealed something unexpected
- FACTS: 20% day 1, 50% day 5, 80%+ daily by GA
- CHALLENGE: "Developers resist new tools" → Actually, they adopted faster than anticipated
- Opens curiosity: What made it spread so fast?

**Section 4: The Paradigm Shift - Agentic vs Passive**
- ONE IDEA: The fundamental distinction that explains everything
- Comparison table (enhanced from current lesson)
- Diagram reference (existing image)
- Opens curiosity: Why does terminal integration matter so much?

**Section 5: Terminal Integration - The Hidden Leverage**
- ONE IDEA: Terminal isn't preference, it's essential to the paradigm
- 5 reasons (from current lesson, enhanced)
- Opens curiosity: What does this mean for how you work?

**Section 6: The Self-Building Proof**
- ONE IDEA: ~90% of Claude Code was written by Claude Code
- CHALLENGE: "AI can't build complex systems" → This IS the paradigm shift proof
- Opens curiosity: What does this mean for your future as a developer?

**Section 7: Try With AI**
- Active collaboration prompts (preserved from current lesson)
- Safety note embedded

### Key Entities

- **Lesson File**: `01-origin-story.md` - primary content, ~200-250 lines post-enhancement
- **Summary File**: `01-origin-story.summary.md` - key concepts, mental models, patterns
- **Frontmatter Metadata**: Preserved Layer 1, A2 proficiency, skills, learning objectives

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Every factual claim (dates, names, metrics) can be traced to source article - 100% traceability
- **SC-002**: Reader can identify the ONE core idea introduced in each section - tested via section headings mapping to single concepts
- **SC-003**: Zero summarizing closure phrases ("in conclusion", "to summarize", "overall", "in short") in section endings
- **SC-004**: At least 3 explicit misconception challenges included (framed as "Many believe X → Actually Y")
- **SC-005**: Lesson passes constitutional validation (Principle 3: Factual Accuracy, Principle 7: Minimal Sufficient Content)
- **SC-006**: Summary file updated with: Product Overhang concept, self-building statistic, adoption metrics
- **SC-007**: Internal critique checklist completed with zero unresolved issues for: generic phrasing, shallow explanations, missed nuance

## Assumptions

- Source article (Pragmatic Engineer "How Claude Code is Built") remains accessible and accurate
- Existing lesson structure (frontmatter, image references, Try With AI section) should be preserved
- Target audience remains A2 proficiency (beginners with basic AI and terminal understanding)
- Lesson duration target remains ~10 minutes reading time

## Non-Goals

- **NOT teaching Claude Code commands or usage** - that's Lesson 2+
- **NOT comparing Claude Code to competitors** (Copilot, Cursor) - mentioned in extension, not core content
- **NOT explaining technical architecture** (TypeScript, React Ink, Bun) - too technical for A2
- **NOT providing installation instructions** - separate lesson
- **NOT updating other lessons in Chapter 5** - scope limited to Lesson 1

## Dependencies

- Existing lesson file: `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`
- Existing summary file: `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.summary.md`
- Source article: https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built
- Constitution v6.0.1 (factual accuracy, minimal content principles)
