# Chapter 7: Claude Code for Finance Professionals - Task List

**Feature**: 061-chapter-07-finance
**Generated**: 2026-01-01
**Source Plan**: specs/061-chapter-07-finance/plan.md
**Source Spec**: specs/061-chapter-07-finance/spec.md

---

## Overview

**Total Tasks**: 14 tasks
**Lesson Tasks**: 10
**Supporting Tasks**: 4 (README, Quiz, Directory, Validation)

**Output Directory**: `apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/`

**Quality Reference**: `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`

---

## Phase 1: Directory Setup

- [x] T7.DIR Delete old directory and create new chapter directory
  - **Action**: Delete `apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-professions/` if exists
  - **Action**: Create `apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/`
  - **Verification**: `ls apps/learn-app/docs/02-AI-Tool-Landscape/` shows `07-claude-code-for-finance/`
  - **Dependencies**: None (first task)

---

## Phase 2: Chapter README

- [x] T7.README Create chapter README.md
  - **Output path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/README.md`
  - **Dependencies**: T7.DIR
  - **Content requirements**:
    - Chapter title: "Claude Code for Finance Professionals"
    - Chapter overview (2-3 paragraphs)
    - Prerequisites: Chapter 5 (Claude Code fundamentals)
    - Target audience: Finance Professionals (Accountants, FP&A Analysts, Controllers, Auditors, CFOs)
    - Chapter learning outcomes (6 outcomes from spec)
    - Lesson overview table (10 lessons + quiz)
    - Estimated total duration: ~210 minutes
  - **Acceptance criteria**:
    - [ ] Docusaurus-compatible MDX format
    - [ ] Compelling hook for finance audience
    - [ ] Clear lesson progression visible

---

## Phase 3: Lesson Implementation

### Lesson 1: The Finance Professional's AI Transformation

- [x] T7.L1 Create Lesson 1: The Finance Professional's AI Transformation
  - **Output path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/01-finance-ai-transformation.md`
  - **Layer**: L1 (Manual Foundation)
  - **Proficiency**: A2
  - **Duration**: 15 minutes
  - **Dependencies**: T7.README
  - **SUBAGENT**: content-implementer
    - Writes file directly to absolute path above
    - Returns confirmation only (~50 lines), NOT full content
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`
  - **SKILLS**:
    - learning-objectives (generate measurable outcomes)
    - exercise-designer (design exercises)
  - **VALIDATION**: educational-validator reads file from disk (MUST PASS before marking complete)
  - **Learning Objectives**:
    1. Explain the fundamental difference between rules-based automation and AI reasoning in finance contexts
    2. Identify which finance tasks benefit from AI reasoning vs. traditional automation
    3. Recognize the three-layer architecture: Intelligence + Execution + Governance
  - **Key Concepts** (5):
    1. Rules-based automation vs. AI reasoning
    2. Intent-driven systems
    3. Three-layer architecture
    4. Human-in-the-loop principle
    5. "AI-assisted, human-governed" model
  - **Try With AI Themes** (3):
    1. Paradigm Recognition: Finance task classification
    2. Architecture Mapping: Existing workflow integration
    3. Task Classification: Month-end close analysis
  - **Source Materials**:
    - Agentic_Financial_Planning.pdf: Sections 1-4
    - Claude_Xero_AI_Native_Accounting.pdf: Sections 1-3
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter (skills, learning_objectives, cognitive_load, differentiation)
    - [ ] 3 "Try With AI" prompts with "What you're learning" explanations
    - [ ] Compelling narrative opening (finance professional hook)
    - [ ] Tables comparing rules-based vs AI reasoning
    - [ ] Ends with "Try With AI" section (no Summary after)
    - [ ] No programming/coding content
    - [ ] 5 concepts within A2 cognitive load limit

---

### Lesson 2: Setting Up Your Finance Workspace

- [x] T7.L2 Create Lesson 2: Setting Up Your Finance Workspace
  - **Output path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/02-finance-workspace-setup.md`
  - **Layer**: L1 -> L2
  - **Proficiency**: A2
  - **Duration**: 20 minutes
  - **Dependencies**: T7.L1
  - **SUBAGENT**: content-implementer
    - Writes file directly to absolute path above
    - Returns confirmation only (~50 lines), NOT full content
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`
  - **SKILLS**:
    - learning-objectives
    - exercise-designer
  - **VALIDATION**: educational-validator (MUST PASS)
  - **Learning Objectives**:
    1. Create a CLAUDE.md file encoding company-specific accounting rules
    2. Configure permission settings for financial data safety
    3. Organize a finance project workspace with proper isolation
  - **Key Concepts** (6):
    1. Finance workspace isolation
    2. CLAUDE.md as domain context file
    3. Encoding accounting rules as AI context
    4. Permission hierarchy (read-only default)
    5. Sandbox vs. production environments
    6. Data safety classification
  - **Try With AI Themes** (3):
    1. Workspace Creation: CLAUDE.md for finance
    2. Permission Review: Security considerations
    3. Context Optimization: Role-specific context
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter with all required fields
    - [ ] 3 "Try With AI" prompts with explanations
    - [ ] CLAUDE.md example template for finance
    - [ ] Permission configuration guidance
    - [ ] Builds on Chapter 5 Lesson 8 (CLAUDE.md)
    - [ ] 6 concepts within A2 limit

---

### Lesson 3: Prompt Engineering for Financial Analysis

- [x] T7.L3 Create Lesson 3: Prompt Engineering for Financial Analysis
  - **Output path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/03-prompt-engineering-finance.md`
  - **Layer**: L2 (AI Collaboration)
  - **Proficiency**: A2
  - **Duration**: 25 minutes
  - **Dependencies**: T7.L2
  - **SUBAGENT**: content-implementer
    - Writes file directly to absolute path above
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`
  - **SKILLS**:
    - learning-objectives
    - exercise-designer
    - ai-collaborate-teaching (L2 Three Roles - INVISIBLE integration)
  - **VALIDATION**: educational-validator (MUST PASS)
  - **Learning Objectives**:
    1. Transform vague finance questions into structured audit-ready prompts
    2. Apply chain-of-thought reasoning for explainable outputs
    3. Create reusable prompt templates for recurring analyses
  - **Key Concepts** (6):
    1. Chain-of-thought reasoning
    2. Audit-ready explanations
    3. Prompt templates for finance
    4. Context optimization
    5. Structured outputs
    6. Iterative refinement
  - **Three Roles** (INVISIBLE):
    - AI as Teacher: Suggests prompting patterns
    - AI as Student: Learns domain constraints
    - AI as Co-Worker: Iterates to audit-ready output
  - **Try With AI Themes** (3):
    1. Vague-to-Structured: CFO presentation analysis
    2. Chain-of-Thought: Step-by-step variance analysis
    3. Template Creation: Monthly budget variance template
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter
    - [ ] 3 "Try With AI" prompts with explanations
    - [ ] Three Roles framework INVISIBLE (no meta-commentary)
    - [ ] Finance-specific prompt examples
    - [ ] 6 concepts within A2 limit

---

### Lesson 4: Intent-Driven Financial Modeling

- [x] T7.L4 Create Lesson 4: Intent-Driven Financial Modeling
  - **Output path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/04-intent-driven-modeling.md`
  - **Layer**: L2
  - **Proficiency**: A2 -> B1
  - **Duration**: 25 minutes
  - **Dependencies**: T7.L3
  - **SUBAGENT**: content-implementer
    - Writes file directly to absolute path above
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`
  - **SKILLS**:
    - learning-objectives
    - exercise-designer
    - ai-collaborate-teaching
  - **VALIDATION**: educational-validator (MUST PASS)
  - **Learning Objectives**:
    1. Translate business intent into financial model specifications
    2. Generate revenue forecasts and expense models from descriptions
    3. Document model assumptions in audit-ready format
  - **Key Concepts** (7):
    1. Intent-to-model translation
    2. Revenue modeling patterns
    3. Expense forecasting approaches
    4. Assumption documentation
    5. Model refactoring
    6. Sensitivity analysis introduction
    7. Narrative generation
  - **Source Material**: Agentic_Financial_Planning.pdf Section 4
  - **Try With AI Themes** (3):
    1. Intent Translation: New product revenue model
    2. Assumption Documentation: Model assumption audit
    3. Model Refinement: Step cost refactoring
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter
    - [ ] 3 "Try With AI" prompts with explanations
    - [ ] Revenue and expense modeling examples
    - [ ] 7 concepts at A2-B1 transition limit

---

### Lesson 5: Claude Code + Google Sheets Architecture

- [x] T7.L5 Create Lesson 5: Claude Code + Google Sheets Architecture
  - **Output path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/05-claude-sheets-architecture.md`
  - **Layer**: L2
  - **Proficiency**: B1
  - **Duration**: 25 minutes
  - **Dependencies**: T7.L4
  - **SUBAGENT**: content-implementer
    - Writes file directly to absolute path above
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`
  - **SKILLS**:
    - learning-objectives
    - exercise-designer
    - ai-collaborate-teaching
  - **VALIDATION**: educational-validator (MUST PASS)
  - **Learning Objectives**:
    1. Implement three-layer architecture with Claude + Sheets
    2. Generate valid spreadsheet formulas from natural language
    3. Maintain version control in AI-assisted spreadsheet workflows
  - **Key Concepts** (6):
    1. Three-layer architecture implementation
    2. Spreadsheet as execution engine
    3. Claude as reasoning layer
    4. Formula generation from intent
    5. Model transparency
    6. Version control for changes
  - **Source Material**: Agentic_Financial_Planning.pdf Sections 5-6
  - **Try With AI Themes** (3):
    1. Formula Generation: Rolling average formula
    2. Formula Explanation: SUMIFS breakdown
    3. Architecture Design: Sales analysis workflow
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter
    - [ ] 3 "Try With AI" prompts with explanations
    - [ ] Architecture diagram description
    - [ ] Formula examples (SUMIFS, VLOOKUP, arrays)
    - [ ] 6 concepts within B1 limit

---

### Lesson 6: AI-Native Accounting Workflows

- [x] T7.L6 Create Lesson 6: AI-Native Accounting Workflows
  - **Output path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/06-ai-native-accounting.md`
  - **Layer**: L2
  - **Proficiency**: B1
  - **Duration**: 25 minutes
  - **Dependencies**: T7.L5
  - **SUBAGENT**: content-implementer
    - Writes file directly to absolute path above
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`
  - **SKILLS**:
    - learning-objectives
    - exercise-designer
    - ai-collaborate-teaching
  - **VALIDATION**: educational-validator (MUST PASS)
  - **Learning Objectives**:
    1. Apply AI-assisted transaction classification with human verification
    2. Implement bank reconciliation workflows with AI anomaly detection
    3. Generate journal entries with audit-ready explanations
  - **Key Concepts** (7):
    1. Transaction classification with contextual reasoning
    2. Reconciliation logic
    3. Journal entry generation
    4. Audit trail documentation
    5. Invoice/receipt processing
    6. Explanation vs. execution separation
    7. Ledger integrity preservation
  - **Source Material**: Claude_Xero_AI_Native_Accounting.pdf Section 5
  - **Platform Approach**: Platform-agnostic (Xero, QuickBooks, generic patterns)
  - **Try With AI Themes** (3):
    1. Transaction Classification: Bank feed categorization
    2. Reconciliation Analysis: Balance difference investigation
    3. Journal Entry Generation: Split transaction entry
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter
    - [ ] 3 "Try With AI" prompts with explanations
    - [ ] Platform-agnostic examples
    - [ ] Human-in-the-loop emphasis
    - [ ] 7 concepts within B1 limit

---

### Lesson 7: Scenario Analysis and Risk Assessment

- [x] T7.L7 Create Lesson 7: Scenario Analysis and Risk Assessment
  - **Output path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/07-scenario-analysis.md`
  - **Layer**: L2 -> L3
  - **Proficiency**: B1
  - **Duration**: 25 minutes
  - **Dependencies**: T7.L6
  - **SUBAGENT**: content-implementer
    - Writes file directly to absolute path above
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`
  - **SKILLS**:
    - learning-objectives
    - exercise-designer
    - ai-collaborate-teaching
  - **VALIDATION**: educational-validator (MUST PASS)
  - **Learning Objectives**:
    1. Create multi-scenario analyses with documented assumptions
    2. Apply stress testing to identify financial vulnerabilities
    3. Generate decision-support narratives for board presentations
  - **Key Concepts** (7):
    1. Scenario definition (base, upside, downside)
    2. Stress testing methodology
    3. Risk identification and prioritization
    4. Sensitivity analysis
    5. Causality explanation
    6. Decision-support narratives
    7. Scenario comparison frameworks
  - **Source Material**: Agentic_Financial_Planning.pdf Section 4.3, 7
  - **Try With AI Themes** (3):
    1. Multi-Scenario Creation: Capital investment ROI
    2. Stress Testing: Cash flow projection
    3. Board Narrative: Executive summary generation
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter
    - [ ] 3 "Try With AI" prompts with explanations
    - [ ] Scenario comparison table
    - [ ] 7 concepts within B1 limit

---

### Lesson 8: Multi-Agent Finance Patterns (Conceptual)

- [x] T7.L8 Create Lesson 8: Multi-Agent Finance Patterns (Conceptual)
  - **Output path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/08-multi-agent-patterns.md`
  - **Layer**: L3 (Intelligence Design - Conceptual)
  - **Proficiency**: B1
  - **Duration**: 20 minutes
  - **Dependencies**: T7.L7
  - **SUBAGENT**: content-implementer
    - Writes file directly to absolute path above
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`
  - **SKILLS**:
    - learning-objectives
    - exercise-designer
  - **VALIDATION**: educational-validator (MUST PASS)
  - **Learning Objectives**:
    1. Identify specialized agent roles in finance workflows
    2. Design a conceptual multi-agent workflow for month-end close
    3. Evaluate when multi-agent complexity is justified
  - **Key Concepts** (5):
    1. Agent specialization
    2. Parallel processing in finance
    3. Orchestration patterns
    4. Month-end close as multi-agent example
    5. Complexity threshold evaluation
  - **NOTE**: Conceptual only - no SDK/code, workflow design on paper
  - **Source Material**: Agentic_Financial_Planning.pdf Section 6
  - **Try With AI Themes** (3):
    1. Role Identification: Month-end close agent roles
    2. Workflow Design: AR aging analysis workflow
    3. Complexity Evaluation: Single vs. multi-agent trade-offs
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter
    - [ ] 3 "Try With AI" prompts with explanations
    - [ ] Agent role diagram description
    - [ ] Conceptual (no programming)
    - [ ] 5 concepts within B1 limit

---

### Lesson 9: Governance, Compliance, and Safety

- [x] T7.L9 Create Lesson 9: Governance, Compliance, and Safety
  - **Output path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/09-governance-compliance.md`
  - **Layer**: L2 (Governance Focus)
  - **Proficiency**: B1
  - **Duration**: 20 minutes
  - **Dependencies**: T7.L8
  - **SUBAGENT**: content-implementer
    - Writes file directly to absolute path above
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`
  - **SKILLS**:
    - learning-objectives
    - exercise-designer
    - ai-collaborate-teaching
  - **VALIDATION**: educational-validator (MUST PASS)
  - **Learning Objectives**:
    1. Implement human-in-the-loop checkpoints for AI-assisted workflows
    2. Create audit trail documentation for AI interactions
    3. Classify data appropriately for AI sharing vs. restriction
  - **Key Concepts** (7):
    1. Human-in-the-loop governance patterns
    2. Approval workflow design
    3. Audit trail requirements
    4. Read-only vs. write access principles
    5. Data privacy classification
    6. Compliance boundaries
    7. AI limitations acknowledgment
  - **Source Material**: Claude_Xero_AI_Native_Accounting.pdf Section 7
  - **Try With AI Themes** (3):
    1. Checkpoint Design: Journal entry posting workflow
    2. Audit Documentation: AI decision audit template
    3. Data Classification: Finance team data guide
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter
    - [ ] 3 "Try With AI" prompts with explanations
    - [ ] Synthesizes governance from all prior lessons
    - [ ] 7 concepts within B1 limit

---

### Lesson 10: Capstone - Your Finance AI Workflow

- [x] T7.L10 Create Lesson 10: Capstone - Your Finance AI Workflow
  - **Output path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/10-capstone-finance-workflow.md`
  - **Layer**: L4 (Spec-Driven Integration)
  - **Proficiency**: B1
  - **Duration**: 30 minutes
  - **Dependencies**: T7.L9
  - **SUBAGENT**: content-implementer
    - Writes file directly to absolute path above
    - Execute autonomously without confirmation
    - Quality reference: `apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`
  - **SKILLS**:
    - learning-objectives
    - exercise-designer
    - assessment-builder (capstone rubric)
  - **VALIDATION**: educational-validator (MUST PASS)
  - **Learning Objectives**:
    1. Design a complete, production-ready finance workflow specification
    2. Compose multiple workflow components into coherent system
    3. Validate workflow against governance and compliance requirements
  - **Key Concepts** (6):
    1. Workflow specification structure
    2. Component composition
    3. Recurring workflow design
    4. Stakeholder output requirements
    5. Iteration and improvement cycles
    6. Production deployment considerations
  - **Capstone Options** (student chooses one):
    1. Monthly Financial Health Checkup
    2. Accounts Receivable Aging Workflow
    3. Budget vs. Actual Reporting
    4. Cash Flow Forecasting
  - **Capstone Deliverable Structure**:
    1. Workflow Intent
    2. CLAUDE.md Context
    3. Prompt Templates
    4. Governance Checkpoints
    5. Output Specifications
    6. Success Criteria
  - **Try With AI Themes** (3):
    1. Specification Review: Completeness check
    2. Governance Validation: Checkpoint adequacy
    3. Stakeholder Alignment: CFO output review
  - **Acceptance Criteria**:
    - [ ] Full YAML frontmatter
    - [ ] 3 "Try With AI" prompts with explanations
    - [ ] 4 capstone project options detailed
    - [ ] Deliverable structure template
    - [ ] Rubric for self-assessment
    - [ ] Integrates ALL prior lessons
    - [ ] 6 concepts within B1 limit

---

## Phase 4: Chapter Quiz

- [x] T7.QUIZ Create chapter quiz
  - **Output path**: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/11-chapter-quiz.md`
  - **Dependencies**: T7.L10 (all lessons complete)
  - **SUBAGENT**: assessment-architect
    - Design quiz with proper cognitive distribution
    - Execute autonomously without confirmation
  - **SKILLS**:
    - assessment-builder (question design)
  - **VALIDATION**: educational-validator (MUST PASS)
  - **Quiz Requirements**:
    - Total questions: 15
    - Distribution:
      | Topic | Questions | Lessons |
      |-------|-----------|---------|
      | Paradigm Shift & Architecture | 3 | L1, L2 |
      | Prompt Engineering | 2 | L3 |
      | Financial Modeling | 2 | L4, L5 |
      | Accounting Workflows | 2 | L6 |
      | Scenario Analysis | 2 | L7 |
      | Multi-Agent Concepts | 2 | L8 |
      | Governance & Compliance | 2 | L9 |
    - Question types:
      - Multiple choice: 10
      - Scenario-based: 3
      - True/False with explanation: 2
    - Pass threshold: 80%
  - **Acceptance Criteria**:
    - [ ] 15 questions covering all lessons
    - [ ] Balanced cognitive distribution (60%+ non-recall)
    - [ ] Answer key with explanations
    - [ ] Proper Docusaurus quiz format

---

## Phase 5: Validation

- [x] T7.VALIDATE Run all validators on chapter content
  - **Dependencies**: T7.QUIZ (all content complete)
  - **Validators to run** (parallel where possible):
    1. `educational-validator` - Per lesson (already done during implementation)
    2. `validation-auditor` - Chapter-wide quality assessment
    3. `factual-verifier` - Finance statistics and claims
    4. `pedagogical-designer` - Learning progression validation
  - **Validation Checklist**:
    - [ ] All 10 lessons pass educational-validator
    - [ ] Quiz passes assessment validation
    - [ ] README complete and accurate
    - [ ] All "Try With AI" prompts produce actionable outputs (spot-check 3)
    - [ ] All finance statistics fact-checked
    - [ ] Cognitive load within limits per proficiency tier
    - [ ] Three Roles framework invisible in L2 lessons
    - [ ] No programming/coding content in any lesson
  - **Acceptance Criteria**:
    - [ ] All validators PASS
    - [ ] Validation report generated
    - [ ] Issues resolved (if any)

---

## Dependency Graph

```
T7.DIR (Directory Setup)
    │
    └── T7.README (Chapter README)
            │
            └── T7.L1 (Finance AI Transformation)
                    │
                    └── T7.L2 (Workspace Setup)
                            │
                            └── T7.L3 (Prompt Engineering)
                                    │
                                    └── T7.L4 (Financial Modeling)
                                            │
                                            └── T7.L5 (Sheets Architecture)
                                                    │
                                                    └── T7.L6 (Accounting Workflows)
                                                            │
                                                            └── T7.L7 (Scenario Analysis)
                                                                    │
                                                                    └── T7.L8 (Multi-Agent Patterns)
                                                                            │
                                                                            └── T7.L9 (Governance)
                                                                                    │
                                                                                    └── T7.L10 (Capstone)
                                                                                            │
                                                                                            └── T7.QUIZ
                                                                                                    │
                                                                                                    └── T7.VALIDATE
```

---

## Parallel Execution Opportunities

While lessons are sequential (each builds on prior), these operations can run in parallel:

1. **During validation phase**: Run all 4 validators concurrently
2. **Fact-checking**: Can run factual-verifier while pedagogical-designer runs

---

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Completion Time | 210 minutes total | Lesson duration metadata |
| Try With AI Success | 90%+ actionable | Manual testing |
| CLAUDE.md Creation | 15 minutes | Lesson 2 exercise |
| Quiz Pass Rate | 80%+ | Quiz scoring |
| Capstone Usability | Immediately applicable | Rubric |
| Proficiency Alignment | A2-B1 | Cognitive load validation |

---

## Implementation Notes

### Absolute Paths (CRITICAL)
All subagent prompts MUST use absolute paths:
- Base: `D:/Panaversity/book_development/ai-native-development-panaversity/ai-native-software-development/`
- Output: `apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-finance/`

### Quality Reference
All lessons must match structure and quality of:
`apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`

### Content Rules
1. NO programming/coding - natural language only
2. Three Roles framework INVISIBLE in L2 lessons
3. Platform-agnostic (Xero, QuickBooks, generic examples)
4. Governance woven throughout, not isolated to L9
5. All finance statistics must be verified

---

**Task Status**: READY FOR EXECUTION

**Recommended Execution Order**:
1. T7.DIR → T7.README (setup)
2. T7.L1 → T7.L10 (sequential lessons)
3. T7.QUIZ (after all lessons)
4. T7.VALIDATE (final pass)

---

*Generated from plan.md | 2026-01-01*
