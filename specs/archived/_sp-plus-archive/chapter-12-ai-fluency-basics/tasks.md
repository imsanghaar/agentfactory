# Chapter 12 Implementation Tasks

## Phase 1: Preparation

- [ ] **1.1** Create backup of old chapter folders
  ```bash
  mv 11-prompt-engineering-for-aidd 11-prompt-engineering-for-aidd.bak
  mv 12-context-engineering-for-ai-driven-development 12-context-engineering.bak
  ```

- [ ] **1.2** Create new chapter directory structure
  ```
  12-ai-fluency-basics/
  ```

- [ ] **1.3** Extract reusable content from old lessons
  - Old Ch11 L1: Jake Heller story, WHAT vs HOW
  - Old Ch11 L3: Iteration loop, bidirectional learning
  - Old Ch12 L1: Context window concepts, token estimation
  - Old Ch12 L2: Degradation symptoms
  - Old Ch12 L3+L6: Progressive loading + memory files
  - Old Ch12 L4+L5: Compression + isolation

## Phase 2: Infrastructure

- [ ] **2.1** Create `12-ai-fluency-basics/README.md`
  - Chapter overview
  - 4D Framework introduction
  - Lesson list with durations
  - Prerequisites
  - Key insight statement

## Phase 3: Implement Lessons

### NEW Lessons (Create from scratch)

- [ ] **3.1** Implement L01: What is AI Fluency?
  - Full YAML frontmatter
  - Compelling narrative opening
  - 4D Framework introduction
  - Three modes: Automation, Augmentation, Agency
  - 3 "Try With AI" prompts
  - Run educational-validator

- [ ] **3.2** Implement L06: Description-Discernment Loop
  - Full YAML frontmatter
  - Loop visualization description
  - Transition triggers
  - Termination criteria
  - 3 "Try With AI" prompts
  - Run educational-validator

- [ ] **3.3** Implement L09: Diligence
  - Full YAML frontmatter
  - Creation, Transparency, Deployment
  - Ethical considerations
  - When NOT to use AI
  - 3 "Try With AI" prompts
  - Run educational-validator

### ADAPT Lessons (Keep core, update frame)

- [ ] **3.4** Implement L02: Delegation
  - Base: Old Ch11 L1
  - Add Delegation decision framework
  - Add three interaction modes
  - Add risk/reward matrix
  - Keep Jake Heller story
  - Update YAML frontmatter
  - Run educational-validator

- [ ] **3.5** Implement L04: Context Windows
  - Base: Old Ch12 L1
  - Update model context sizes (Claude 4.5, Gemini 2.5)
  - Keep token estimation rules
  - Keep session note template
  - Update YAML frontmatter
  - Run educational-validator

- [ ] **3.6** Implement L10: Capstone
  - Base: Old Ch12 L9
  - Reframe around 4D framework
  - Update project requirements
  - Align success criteria
  - Run educational-validator

### REPLACE Lessons (Full rewrite)

- [ ] **3.7** Implement L03: Description (REPLACE)
  - 6 prompting techniques (Anthropic)
  - Product-Process-Performance framework
  - Action verb taxonomy
  - NO Zia Kaukab framework
  - Full YAML frontmatter
  - Run educational-validator

### MERGE Lessons

- [ ] **3.8** Implement L05: Progressive Loading & Memory Files
  - Merge Old Ch12 L3 + L6
  - Three-phase loading strategy
  - CLAUDE.md architecture
  - Full YAML frontmatter
  - Run educational-validator

- [ ] **3.9** Implement L07: Discernment
  - Merge Old Ch11 L3 + Ch12 L2
  - Iteration methodology
  - Degradation recognition
  - Full YAML frontmatter
  - Run educational-validator

- [ ] **3.10** Implement L08: Compression & Multi-Session
  - Merge Old Ch12 L4 + L5
  - Compression techniques
  - Context isolation
  - Full YAML frontmatter
  - Run educational-validator

## Phase 4: Quiz

- [ ] **4.1** Create chapter quiz
  - File: `11_chapter_12_quiz.md`
  - Questions covering all 4Ds
  - Scenario-based questions
  - At least 15 questions

## Phase 5: Validation

- [ ] **5.1** Run factual-verifier on all lessons
  - Verify Anthropic 6 techniques
  - Verify Claude model specifications
  - Verify Jake Heller citations
  - Verify Andrej Karpathy quote

- [ ] **5.2** Quality comparison
  - Compare each lesson to reference: `01-digital-fte-revolution.md`
  - Check narrative openings
  - Check "Try With AI" depth
  - Check YAML completeness

- [ ] **5.3** Final educational-validator pass
  - All lessons pass constitutional compliance
  - No framework exposure
  - Proper proficiency alignment

## Phase 6: Cleanup

- [ ] **6.1** Remove backup folders
  - Delete `11-prompt-engineering-for-aidd.bak`
  - Delete `12-context-engineering.bak`

- [ ] **6.2** Update Part 3 README.md
  - Change Chapter 12 description
  - Update lesson count
  - Add 4D Framework reference

- [ ] **6.3** Update chapter-index.md
  - Reflect new Chapter 12 structure

## Phase 7: Commit & Issues

- [ ] **7.1** Stage all changes
  ```bash
  git add apps/learn-app/docs/03-Markdown-Prompt-Context-Engineering/
  git add specs/chapter-12-ai-fluency-basics/
  ```

- [ ] **7.2** Create commit
  - Title: `feat(ch12): implement AI Fluency Basics - merge prompt & context chapters`
  - Body: List all changes

- [ ] **7.3** Update GitHub issues
  - Close tasks in #562 (Part 3 Restructuring)
  - Update progress in #560 (Epic)

---

## Progress Tracking

| Phase | Tasks | Completed |
|-------|-------|-----------|
| 1. Preparation | 3 | 0 |
| 2. Infrastructure | 1 | 0 |
| 3. Lessons | 10 | 0 |
| 4. Quiz | 1 | 0 |
| 5. Validation | 3 | 0 |
| 6. Cleanup | 3 | 0 |
| 7. Commit | 3 | 0 |
| **Total** | **24** | **0** |
