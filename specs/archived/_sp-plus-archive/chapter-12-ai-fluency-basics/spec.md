# Chapter 12: AI Fluency Basics - Prompt & Context Engineering

## Overview

**Part**: 3 (Markdown & Context Engineering)
**Position**: Chapter 12 (after Markdown chapter)
**Proficiency Level**: A2-B1
**Duration**: 6-8 hours total

This chapter merges the former "Prompt Engineering for AIDD" (old Chapter 11) and "Context Engineering for AI-Driven Development" (old Chapter 12) into a unified chapter based on **Anthropic's AI Fluency Framework** with the 4Ds: Delegation, Description, Discernment, and Diligence.

## Rationale for Merge

1. **Industry Shift**: Andrej Karpathy notes that "prompt engineering" is now a subset of "context engineering"
2. **Framework Alignment**: Anthropic's 4D framework unifies prompting and context management
3. **Content Overlap**: Many lessons had redundant concepts (iteration, refinement, validation)
4. **Quality Issues**: Old Ch11 L2 contained unverifiable "Zia Kaukab 8-Element Framework"
5. **Template Obsolescence**: Old Ch11 L6-L8 (templates) are now obsolete with modern models

## Authoritative Sources

| Source | Content |
|--------|---------|
| **Anthropic AI Fluency Course** | 4D Framework, 6 prompting techniques, Description-Discernment loop |
| **Anthropic Context Engineering Guide** | Compaction, structured note-taking, sub-agent architectures |
| **Claude 4.x Documentation** | Literal instruction following, context awareness, multi-window |
| **Jake Heller (Casetext)** | 60%→97% iteration methodology |
| **Andrej Karpathy** | "Context engineering" shift |

## Chapter Structure (10 Lessons)

### Lesson 1: What is AI Fluency? The 4D Framework (NEW)
**Duration**: 25 min | **Proficiency**: A2 | **Concepts**: 5

**Source**: NEW content based on Anthropic AI Fluency course

**Learning Objectives**:
- Define AI Fluency as a measurable professional skill
- Identify the 4Ds: Delegation, Description, Discernment, Diligence
- Distinguish AI Fluency from "prompt engineering"
- Explain how 4Ds build on each other

**Key Content**:
- AI Fluency as career differentiator
- Three modes: Automation, Augmentation, Agency
- 4D Framework overview
- How this chapter is structured around 4Ds

**Try With AI**:
1. Ask Claude to explain the 4D framework
2. Identify which D applies to a given scenario
3. Compare AI Fluency to traditional "prompt engineering"

---

### Lesson 2: Delegation - Deciding What AI Should Do
**Duration**: 30 min | **Proficiency**: A2 | **Concepts**: 6

**Source**: Adapted from old Ch11 L1 + Anthropic Delegation concepts

**Content Disposition**: ADAPT existing lesson

**Learning Objectives**:
- Apply the Delegation decision framework (Can AI help? Should AI help?)
- Identify tasks suitable for AI collaboration vs. human-only tasks
- Recognize the three interaction modes (Automation, Augmentation, Agency)
- Evaluate tasks using risk/reward framework

**Key Content**:
- Jake Heller's "prompts as specifications" insight (keep from old L1)
- Delegation decision tree
- Task categories by interaction mode
- Risk assessment for AI delegation

**From Old L1 to Keep**:
- Jake Heller 60%→97% story
- WHAT vs HOW distinction
- "Prompts are specifications" framing

**From Old L1 to Remove**:
- None - this lesson was high quality

**New Content to Add**:
- Delegation decision framework from Anthropic
- Three modes of AI interaction
- Risk/reward evaluation matrix

---

### Lesson 3: Description - Prompt Structure & Clarity (REWRITE)
**Duration**: 35 min | **Proficiency**: A2 | **Concepts**: 6

**Source**: REPLACE old Ch11 L2 (had unverifiable Zia Kaukab framework)

**Content Disposition**: REPLACE with verified content

**Learning Objectives**:
- Apply the 6 prompting techniques from Anthropic
- Structure prompts using Product-Process-Performance framework
- Use action verbs for clear intent
- Identify what makes descriptions effective

**Key Content**:
- **6 Prompting Techniques** (Anthropic):
  1. Give context
  2. Show examples
  3. Specify constraints
  4. Break into steps
  5. Ask AI to think first
  6. Define role/tone
- Description sub-components: Product, Process, Performance
- Intent → Constraints → Success Criteria (keep, but simplified)
- Action verb taxonomy (CREATE, DEBUG, REFACTOR, etc.)

**Removed**:
- ❌ "Zia Kaukab 8-Element Framework" (unverifiable)
- ❌ Overly complex prompt anatomy

**Why Rewrite**:
Previous lesson cited "Zia Kaukab's prompting research at Google" which could not be verified. Replace with documented Anthropic 6 techniques.

---

### Lesson 4: Context Windows & Token Economics
**Duration**: 40 min | **Proficiency**: A2 | **Concepts**: 4

**Source**: Old Ch12 L1 (keep most)

**Content Disposition**: KEEP with minor updates

**Learning Objectives**:
- Explain context windows as AI working memory
- Estimate token usage for text content
- Create session notes for manual tracking
- Identify utilization warning zones (green/yellow/red)

**Key Content** (from old L1):
- Context window as working memory analogy
- Token estimation rules (1 word ≈ 1-1.2 tokens)
- Session note template
- Warning thresholds (0-70% green, 70-85% yellow, 85-100% red)

**Updates**:
- Update Claude model context sizes (Claude Sonnet 4.5: 200K standard, 1M extended)
- Add Gemini 2.5 comparison (2M tokens)
- Simplify observable behaviors section

---

### Lesson 5: Progressive Loading & Memory Files (MERGE)
**Duration**: 40 min | **Proficiency**: B1 | **Concepts**: 6

**Source**: Merge old Ch12 L3 (Progressive Loading) + L6 (Memory Files)

**Content Disposition**: MERGE two lessons

**Learning Objectives**:
- Apply three-phase loading strategy (Foundation → Current → On-Demand)
- Design CLAUDE.md memory files for project persistence
- Create architecture.md and decisions.md for multi-session work
- Evaluate when to use memory files vs. session context

**Key Content**:
- Progressive loading phases (from L3)
- Foundation files: What AI always needs
- Current focus: Active working files
- On-demand: Load when referenced
- Memory file architecture (from L6):
  - CLAUDE.md for project rules
  - architecture.md for system design
  - decisions.md for rationale tracking

**Why Merge**: Both lessons address "what goes into context" - loading strategy and persistent memory are complementary.

---

### Lesson 6: The Description-Discernment Loop (NEW)
**Duration**: 35 min | **Proficiency**: B1 | **Concepts**: 5

**Source**: NEW based on Anthropic AI Fluency course

**Learning Objectives**:
- Apply the Description-Discernment iterative loop
- Identify when to apply Description vs. Discernment
- Recognize loop patterns in real workflows
- Design prompts that enable effective loops

**Key Content**:
- The core loop: Describe → Generate → Evaluate → Refine
- When Description fails: triggers for Discernment
- When Discernment fails: triggers for Description revision
- Loop termination criteria (convergence, diminishing returns)
- Real example: Writing a specification through the loop

**Try With AI**:
1. Execute a 5-iteration loop on a real task
2. Identify which phase (Description or Discernment) is active
3. Track quality improvement across iterations

---

### Lesson 7: Discernment - Iterative Refinement (MERGE)
**Duration**: 45 min | **Proficiency**: B1 | **Concepts**: 7

**Source**: Merge old Ch11 L3 (Iterative Refinement) + old Ch12 L2 (Degradation Symptoms)

**Content Disposition**: MERGE two lessons

**Learning Objectives**:
- Apply discernment through Product, Process, and Performance evaluation
- Recognize context degradation symptoms (forgetting, repetition, vagueness)
- Execute multi-iteration refinement sessions
- Know when to restart vs. continue a session

**Key Content**:
- Discernment sub-components: Product, Process, Performance
- From old Ch11 L3:
  - Jake Heller's 60%→97% methodology
  - Iteration loop pattern
  - Bidirectional learning (AI teaches you, you teach AI)
  - Convergence criteria
- From old Ch12 L2:
  - Context degradation symptoms
  - Observable behaviors (yellow/red zone)
  - Session restart triggers

**Why Merge**: Iterative refinement IS discernment. Degradation symptoms inform when discernment fails.

---

### Lesson 8: Compression & Multi-Session Workflows (MERGE)
**Duration**: 40 min | **Proficiency**: B1 | **Concepts**: 6

**Source**: Merge old Ch12 L4 (Compression) + L5 (Context Isolation)

**Content Disposition**: MERGE two lessons

**Learning Objectives**:
- Apply compression strategies (checkpoint summaries, session handoff)
- Design multi-session workflows for complex projects
- Use context isolation for parallel tasks
- Create effective session restart documents

**Key Content**:
- From old Ch12 L4:
  - Checkpoint summaries
  - Session restart protocol
  - Compression techniques
- From old Ch12 L5:
  - Context isolation for parallel tasks
  - Separate sessions for unrelated work
  - Multi-window workflows

---

### Lesson 9: Diligence - Responsible AI Collaboration (NEW)
**Duration**: 30 min | **Proficiency**: B1 | **Concepts**: 5

**Source**: NEW based on Anthropic AI Fluency course

**Learning Objectives**:
- Apply the three Diligence areas: Creation, Transparency, Deployment
- Evaluate AI outputs for accuracy, bias, and appropriateness
- Document AI assistance transparently
- Identify ethical considerations in AI collaboration

**Key Content**:
- Diligence in Creation: Fact-checking, source verification, quality gates
- Diligence in Transparency: Attribution, disclosure, documentation
- Diligence in Deployment: Impact assessment, monitoring, feedback loops
- Responsible AI collaboration principles
- When NOT to use AI (high-stakes decisions, ethical concerns)

**Try With AI**:
1. Ask Claude about its limitations for a specific task
2. Create an AI disclosure statement for a project
3. Design a fact-checking workflow for AI-generated content

---

### Lesson 10: Capstone - AI Fluency in Practice
**Duration**: 60 min | **Proficiency**: B1 | **Concepts**: Synthesis

**Source**: Adapted from old Ch12 L9 (Capstone)

**Content Disposition**: UPDATE capstone project

**Learning Objectives**:
- Apply all 4Ds in a complete workflow
- Create a specification document using the Description-Discernment loop
- Design a multi-session project workflow
- Demonstrate AI Fluency through documented collaboration

**Project**:
Write a complete specification for a context-aware development tool that orchestrates:
- Delegation decisions (what AI should do)
- Description patterns (how to communicate intent)
- Discernment loops (how to evaluate and refine)
- Diligence practices (how to be responsible)

**Success Criteria**:
- Specification document 500+ words
- Clear 4D alignment for each section
- Memory files designed
- Multi-session workflow planned
- Diligence considerations documented

---

## Content Disposition Summary

| Lesson | Source | Status |
|--------|--------|--------|
| L1 | NEW | Create from Anthropic AI Fluency |
| L2 | Old Ch11 L1 | ADAPT (add Delegation framework) |
| L3 | Old Ch11 L2 | REPLACE (remove unverified framework) |
| L4 | Old Ch12 L1 | KEEP (update model sizes) |
| L5 | Old Ch12 L3+L6 | MERGE |
| L6 | NEW | Create from Anthropic loop concept |
| L7 | Old Ch11 L3 + Ch12 L2 | MERGE |
| L8 | Old Ch12 L4+L5 | MERGE |
| L9 | NEW | Create from Anthropic Diligence |
| L10 | Old Ch12 L9 | UPDATE (4D alignment) |

## Deleted Content

| Old Lesson | Reason |
|------------|--------|
| Ch11 L4: Specification-First Prompting | Redundant with L2/L3 |
| Ch11 L5: Question-Driven Development | Integrated into L6/L7 |
| Ch11 L6: Reusable Prompt Templates | Obsolete with modern models |
| Ch11 L7: Template Selection Criteria | Obsolete with modern models |
| Ch11 L8: Capstone - Template Library | Obsolete with modern models |
| Ch12 L7: Tool Selection Framework | Out of scope (moved to tooling chapters) |
| Ch12 L8: Hands-On Debugging | Integrated into L7 |

## Quality Gates

Before implementation:
- [ ] All 6 Anthropic prompting techniques cited correctly
- [ ] 4D Framework presented accurately per Anthropic course
- [ ] No unverifiable frameworks (Zia Kaukab removed)
- [ ] Jake Heller citations verified
- [ ] Claude 4.x model capabilities updated

During implementation:
- [ ] Each lesson has full YAML frontmatter
- [ ] Each lesson has 3 "Try With AI" prompts
- [ ] Each lesson has compelling narrative opening
- [ ] All statistics verified via WebSearch
- [ ] Educational-validator passes

## File Structure

```
12-ai-fluency-basics/
├── README.md
├── 01-what-is-ai-fluency.md
├── 02-delegation.md
├── 03-description-prompt-structure.md
├── 04-context-windows-token-economics.md
├── 05-progressive-loading-memory-files.md
├── 06-description-discernment-loop.md
├── 07-discernment-iterative-refinement.md
├── 08-compression-multi-session.md
├── 09-diligence-responsible-ai.md
├── 10-capstone-ai-fluency-practice.md
└── 11_chapter_12_quiz.md
```

## GitHub Issue References

- Epic: #560 (Restructure Parts 2-3)
- Part 3 Restructuring: #562

## Next Steps

1. **Clarify**: Confirm 4D framework alignment with user
2. **Plan**: Create implementation plan with lesson-by-lesson tasks
3. **Tasks**: Generate tasks.md with checkboxes
4. **Implement**: Use content-implementer subagent for each lesson
5. **Validate**: Run educational-validator on each lesson
6. **Commit**: Stage changes and update GitHub issues
