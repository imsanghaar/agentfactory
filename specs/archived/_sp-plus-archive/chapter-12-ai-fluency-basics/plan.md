# Chapter 12 Implementation Plan

## Phase 1: Preparation

### Step 1.1: Create Chapter Directory Structure
- Create `12-ai-fluency-basics/` folder
- Remove old `11-prompt-engineering-for-aidd/` folder (after content extraction)
- Rename existing `12-context-engineering...` folder to backup

### Step 1.2: Extract Reusable Content
From old Ch11 (Prompt Engineering):
- L1: Jake Heller story, WHAT vs HOW, prompts as specifications
- L3: Iteration loop, bidirectional learning, convergence criteria

From old Ch12 (Context Engineering):
- L1: Context window concepts, token estimation, warning zones
- L2: Degradation symptoms, observable behaviors
- L3: Progressive loading strategy
- L4: Compression techniques
- L5: Context isolation
- L6: Memory file architecture
- L9: Capstone structure

## Phase 2: New Lessons (Create First)

### Step 2.1: L01 - What is AI Fluency?
**Priority**: HIGH (sets framework for entire chapter)

Content sources:
- Anthropic AI Fluency course curriculum
- 4D Framework definition
- Three modes of AI interaction

Key elements:
- Define AI Fluency vs prompt engineering
- Introduce Delegation, Description, Discernment, Diligence
- Connect to career value proposition

### Step 2.2: L06 - Description-Discernment Loop
**Priority**: HIGH (core conceptual lesson)

Content sources:
- Anthropic AI Fluency course
- Original synthesis from framework

Key elements:
- The iterative loop visualization
- Transition triggers between Description and Discernment
- Termination criteria

### Step 2.3: L09 - Diligence
**Priority**: HIGH (new content)

Content sources:
- Anthropic AI Fluency course (Diligence section)
- Responsible AI literature

Key elements:
- Creation, Transparency, Deployment framework
- Ethical considerations
- When NOT to use AI

## Phase 3: Adapted Lessons (Keep Core, Update Frame)

### Step 3.1: L02 - Delegation
Base: Old Ch11 L1

Adaptations:
- Add Delegation decision framework
- Add three interaction modes
- Add risk/reward matrix
- Keep Jake Heller story intact

### Step 3.2: L04 - Context Windows
Base: Old Ch12 L1

Adaptations:
- Update model context sizes (Claude 4.5, Gemini 2.5)
- Simplify observable behaviors section
- Keep token estimation rules
- Keep session note template

### Step 3.3: L10 - Capstone
Base: Old Ch12 L9

Adaptations:
- Reframe around 4D framework
- Update project requirements
- Align success criteria with new lessons

## Phase 4: Replaced Lessons

### Step 4.1: L03 - Description
**FULL REWRITE** (old L2 had unverified content)

New content:
- 6 prompting techniques (Anthropic)
- Product-Process-Performance framework
- Action verb taxonomy (keep from old)
- Intent → Constraints → Success (simplified)

Remove:
- "Zia Kaukab 8-Element Framework"

## Phase 5: Merged Lessons

### Step 5.1: L05 - Progressive Loading & Memory Files
Merge: Old Ch12 L3 + L6

Integration approach:
- L3 provides "when to load what"
- L6 provides "how to persist"
- Combine into unified "context management" lesson

### Step 5.2: L07 - Discernment
Merge: Old Ch11 L3 + Old Ch12 L2

Integration approach:
- L3 provides iteration methodology
- L2 provides degradation recognition
- Combine: "Iterative refinement WITH awareness of when it's failing"

### Step 5.3: L08 - Compression & Multi-Session
Merge: Old Ch12 L4 + L5

Integration approach:
- L4 provides compression techniques
- L5 provides isolation strategies
- Combine: "Managing context across time and tasks"

## Phase 6: Chapter Infrastructure

### Step 6.1: README.md
Create chapter overview with:
- 4D Framework introduction
- Lesson list with durations
- Prerequisites (Chapter 11: Markdown)
- Key insight statement

### Step 6.2: Quiz
Create `11_chapter_12_quiz.md` with:
- Questions covering all 4Ds
- Scenario-based questions
- At least 15 questions

## Phase 7: Validation

### Step 7.1: Educational Validator
Run on each lesson:
- Framework invisibility check
- Evidence presence check
- Structural compliance
- Proficiency alignment

### Step 7.2: Factual Verifier
Verify:
- Anthropic 6 techniques accuracy
- Claude model specifications
- Jake Heller citations
- Andrej Karpathy quote

### Step 7.3: Quality Comparison
Compare each lesson against reference:
`01-agent-factory-paradigm/01-digital-fte-revolution.md`

## Implementation Order

| Order | Lesson | Type | Dependencies |
|-------|--------|------|--------------|
| 1 | README.md | Infrastructure | None |
| 2 | L01 | NEW | None (foundation) |
| 3 | L02 | ADAPT | L01 (references 4D) |
| 4 | L03 | REPLACE | L02 (Description after Delegation) |
| 5 | L04 | KEEP | None |
| 6 | L05 | MERGE | L04 (context window knowledge) |
| 7 | L06 | NEW | L03 (Description concept) |
| 8 | L07 | MERGE | L06 (loop concept) |
| 9 | L08 | MERGE | L07 (refinement context) |
| 10 | L09 | NEW | All above (synthesis) |
| 11 | L10 | UPDATE | All above (capstone) |
| 12 | Quiz | Infrastructure | All lessons |

## Estimated Timeline

| Phase | Lessons | Estimated Time |
|-------|---------|----------------|
| Phase 1 | Preparation | 15 min |
| Phase 2 | L01, L06, L09 (NEW) | 2 hours |
| Phase 3 | L02, L04, L10 (ADAPT) | 1.5 hours |
| Phase 4 | L03 (REPLACE) | 45 min |
| Phase 5 | L05, L07, L08 (MERGE) | 2 hours |
| Phase 6 | README, Quiz | 45 min |
| Phase 7 | Validation | 1 hour |
| **Total** | | **~8 hours** |

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| New lessons lack depth | Use Anthropic AI Fluency course as primary source |
| Merged lessons are disjointed | Clear transition paragraphs, unified narrative |
| Old content doesn't fit 4D frame | Reframe explicitly around relevant D |
| Factual errors persist | Run factual-verifier on all lessons |
| Quality inconsistency | Compare each to reference lesson |
