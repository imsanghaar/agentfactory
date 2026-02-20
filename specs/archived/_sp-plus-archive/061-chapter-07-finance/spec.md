# Feature Specification: Chapter 7 - Claude Code for Finance Professionals

**Feature Branch**: `061-chapter-07-finance`
**Created**: 2026-01-01
**Status**: Draft
**Input**: Create Chapter 7: Claude Code for Finance Professionals - 10 lessons for finance professionals covering AI-native financial planning, accounting workflows, and governance

---

## Executive Summary

Transform the skeleton Chapter 7 "Claude Code for Professions" into a focused **"Claude Code for Finance Professionals"** chapter. This chapter applies Claude Code skills (from Chapter 5) to finance-specific workflows for non-technical finance professionals.

**Key Decision**: Finance-only focus (not generic professions) allows depth over breadth and addresses a high-demand professional audience.

---

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Claude Code fundamentals (Chapter 5): installation, authentication, CLAUDE.md context files, basic skills, MCP concepts
- Natural language interaction with AI agents
- Basic understanding of what AI can and cannot do
- No programming knowledge required

**What this chapter must explain from scratch**:
- Finance-specific terminology for AI workflows (intent-driven modeling, reconciliation automation)
- Three-layer architecture (AI reasoning + spreadsheet execution + human governance)
- Human-in-the-loop governance patterns specific to financial compliance
- Multi-agent orchestration concepts (conceptual only, not SDK-level)

---

## Chapter Metadata

| Attribute | Value |
|-----------|-------|
| **Chapter Title** | Claude Code for Finance Professionals |
| **Part** | 2 (AI Tool Landscape) |
| **Position** | 07 |
| **Directory** | `07-claude-code-for-finance` |
| **Target Audience** | Accountants, FP&A Analysts, Financial Controllers, Auditors, CFOs |
| **Prerequisites** | Chapter 5 (Claude Code fundamentals) |
| **Proficiency Range** | A2 - B1 |
| **Lesson Count** | 10 lessons + quiz |
| **Total Duration** | ~210 minutes |

---

## Source Materials

| Source | Primary Use |
|--------|-------------|
| `docs/Agentic_Financial_Planning.pdf` | Lessons 1, 4, 5, 7, 8 - Financial modeling, scenarios, multi-agent patterns |
| `docs/Claude_Xero_AI_Native_Accounting.pdf` | Lessons 1, 6, 9 - Accounting workflows, governance, compliance |
| `docs/Annex-1_Learning_Outcomes_revised.pdf` | Learning objectives, assessment methods, curriculum structure |

---

## User Scenarios & Testing

### User Story 1 - Finance Professional Learns AI Transformation Mindset (Priority: P1)

A finance professional (accountant, analyst, controller) with no technical background wants to understand how Claude Code can transform their daily work. They need to grasp the paradigm shift from rule-based automation to reasoning-based AI assistance.

**Why this priority**: Foundation understanding is required before any practical application. Without understanding the "AI-Assisted, Human-Governed" model, finance professionals may either over-trust or under-utilize AI.

**Independent Test**: Student can explain the difference between traditional automation (rules-based) and AI agents (reasoning-based), and identify which finance tasks benefit from each approach.

**Acceptance Scenarios**:

1. **Given** a finance professional completing Lesson 1, **When** they encounter a new finance task, **Then** they can correctly classify whether it's suitable for AI assistance vs traditional automation
2. **Given** understanding of the three-layer architecture, **When** explaining to colleagues, **Then** they can articulate why AI reasons while spreadsheets compute and humans approve
3. **Given** exposure to governance concepts, **When** asked about AI safety in finance, **Then** they can explain human-in-the-loop requirements

---

### User Story 2 - Finance Professional Configures Domain-Specific Workspace (Priority: P1)

A finance professional needs to set up Claude Code for their specific finance context, including company-specific accounting rules, chart of accounts, and fiscal year settings.

**Why this priority**: Without proper configuration, AI suggestions will be generic rather than context-aware. This is foundational for all subsequent lessons.

**Independent Test**: Student creates a CLAUDE.md file that encodes their company's fiscal year, chart of accounts structure, and key accounting policies.

**Acceptance Scenarios**:

1. **Given** a new finance project folder, **When** student creates CLAUDE.md following lesson guidance, **Then** Claude Code provides company-specific suggestions
2. **Given** understanding of permission settings, **When** working with financial data, **Then** student configures read-only access by default
3. **Given** completed workspace setup, **When** asking Claude about their chart of accounts, **Then** Claude responds with company-specific categories

---

### User Story 3 - Finance Professional Applies Prompt Engineering to Financial Analysis (Priority: P1)

A finance professional needs to craft effective prompts that produce audit-ready, explainable financial analysis outputs.

**Why this priority**: Prompt quality directly determines output quality. Finance-specific prompting patterns differ from general use due to compliance and auditability requirements.

**Independent Test**: Student transforms a vague finance question into a structured prompt that produces traceable, audit-ready analysis.

**Acceptance Scenarios**:

1. **Given** a vague question like "why did expenses increase", **When** applying prompt engineering techniques, **Then** output includes specific data references, calculation steps, and audit trail
2. **Given** need for recurring analysis, **When** creating a prompt template, **Then** template can be reused monthly with different data
3. **Given** chain-of-thought prompting knowledge, **When** requesting complex analysis, **Then** Claude shows reasoning steps that stakeholders can verify

---

### User Story 4 - Finance Professional Builds Intent-Driven Financial Models (Priority: P2)

A finance professional wants to create financial models using natural language instead of complex spreadsheet formulas.

**Why this priority**: This is the core value proposition of AI-native financial planning - translating business intent into analytical outputs without formula expertise.

**Independent Test**: Student specifies a revenue forecast in natural language and receives a structured model specification that can be executed.

**Acceptance Scenarios**:

1. **Given** a business scenario description, **When** using intent-driven prompting, **Then** Claude produces a model specification with clear assumptions
2. **Given** need for scenario comparison, **When** requesting variations, **Then** Claude generates comparable scenarios with documented differences
3. **Given** an existing model, **When** asking for refinement, **Then** Claude suggests improvements while preserving model integrity

---

### User Story 5 - Finance Professional Integrates Claude Code with Spreadsheets (Priority: P2)

A finance professional needs to use Claude Code alongside Google Sheets/Excel for computation while using AI for reasoning.

**Why this priority**: Spreadsheets remain the primary execution environment for finance. Understanding the separation of intelligence (Claude) and computation (Sheets) is essential.

**Independent Test**: Student describes a workflow where Claude reasons about financial questions and Sheets computes the answers.

**Acceptance Scenarios**:

1. **Given** a financial question, **When** Claude generates formulas, **Then** formulas are valid and can be pasted directly into spreadsheet
2. **Given** complex Excel formulas, **When** asking Claude to explain them, **Then** Claude provides plain-English explanations with examples
3. **Given** need for new analysis, **When** collaborating with Claude, **Then** student maintains version control of spreadsheet changes

---

### User Story 6 - Finance Professional Automates Accounting Workflows (Priority: P2)

A finance professional wants to use AI assistance for transaction classification, reconciliation, and journal entry generation.

**Why this priority**: These are high-volume, repetitive tasks where AI reasoning can reduce errors while maintaining human oversight.

**Independent Test**: Student walks through a reconciliation workflow showing where AI assists and where human validates.

**Acceptance Scenarios**:

1. **Given** unclassified transactions, **When** using AI classification prompts, **Then** Claude suggests categories with reasoning that human can verify
2. **Given** a bank reconciliation discrepancy, **When** asking Claude for analysis, **Then** Claude identifies potential causes and proposes resolution steps
3. **Given** need for journal entry, **When** describing the scenario, **Then** Claude generates entry with debit/credit, accounts, and compliance notes

---

### User Story 7 - Finance Professional Conducts Scenario Analysis (Priority: P3)

A finance professional needs to perform stress testing and risk assessment using AI-assisted scenario generation.

**Why this priority**: Scenario analysis is a higher-order application combining multiple skills learned earlier.

**Independent Test**: Student creates a three-scenario analysis (optimistic, realistic, pessimistic) for a business decision.

**Acceptance Scenarios**:

1. **Given** a business investment decision, **When** requesting scenario analysis, **Then** Claude generates comparable scenarios with clear assumptions
2. **Given** need for stress testing, **When** applying specific parameters, **Then** Claude shows sensitivity to key variables
3. **Given** completed analysis, **When** generating narrative, **Then** output is suitable for board presentation

---

### User Story 8 - Finance Professional Understands Multi-Agent Patterns (Priority: P3)

A finance professional wants to understand how multiple specialized AI agents could coordinate on complex finance workflows.

**Why this priority**: Conceptual understanding of multi-agent patterns prepares students for potential future implementations without requiring technical SDK knowledge.

**Independent Test**: Student designs a conceptual multi-agent workflow for month-end close (no code, just specification).

**Acceptance Scenarios**:

1. **Given** a complex finance workflow like month-end close, **When** thinking about agent specialization, **Then** student can identify distinct agent roles
2. **Given** understanding of agent coordination, **When** asked about handoffs, **Then** student can describe how agents would pass work
3. **Given** single-agent vs multi-agent options, **When** evaluating a task, **Then** student can determine when complexity justifies multiple agents

---

### User Story 9 - Finance Professional Implements Governance and Compliance (Priority: P1)

A finance professional must ensure AI-assisted workflows maintain compliance, audit trails, and appropriate human oversight.

**Why this priority**: Finance is a regulated domain. Governance is non-negotiable and must be woven throughout all AI usage.

**Independent Test**: Student creates a governance checklist for AI-assisted financial workflows that addresses audit, compliance, and approval requirements.

**Acceptance Scenarios**:

1. **Given** an AI-assisted workflow, **When** auditor asks about controls, **Then** student can demonstrate human-in-the-loop checkpoints
2. **Given** data sensitivity concerns, **When** classifying information, **Then** student correctly identifies what's safe to share with AI
3. **Given** need for audit documentation, **When** using AI assistance, **Then** all AI interactions are logged with reasoning visible

---

### User Story 10 - Finance Professional Completes Capstone Integration (Priority: P2)

A finance professional designs a complete finance workflow specification that integrates all chapter concepts.

**Why this priority**: Integration demonstrates mastery and creates a practical asset the student can use immediately.

**Independent Test**: Student produces a complete workflow specification for a recurring finance task (e.g., monthly financial health checkup).

**Acceptance Scenarios**:

1. **Given** all chapter concepts, **When** designing end-to-end workflow, **Then** specification includes all necessary components
2. **Given** the workflow specification, **When** executing it monthly, **Then** workflow produces consistent, audit-ready outputs
3. **Given** stakeholder review needs, **When** presenting the workflow, **Then** student can explain each component and its governance

---

### Edge Cases

- What happens when AI suggests a classification that violates company policy?
- How does the system handle sensitive financial data that shouldn't be shared with external AI?
- What if AI-generated formulas contain errors that aren't caught before use?
- How should multi-agent handoffs handle failures or disagreements?
- What's the appropriate response when AI suggests actions that require human judgment (materiality decisions, tax interpretations)?

---

## Requirements

### Functional Requirements

- **FR-001**: Chapter MUST include 10 complete lessons following the pedagogical layer progression L1 - L2 - L3 - L4
- **FR-002**: Each lesson MUST include full YAML frontmatter with pedagogical metadata (skills, learning_objectives, cognitive_load, differentiation)
- **FR-003**: Each lesson MUST include at least 3 "Try With AI" prompts with learning explanations
- **FR-004**: Lessons MUST maintain cognitive load limits: 5-7 new concepts per lesson (A2-B1 proficiency)
- **FR-005**: Chapter MUST include a comprehensive quiz covering key concepts from all lessons
- **FR-006**: All content MUST be platform-agnostic, showing examples from Xero, QuickBooks, and generic patterns
- **FR-007**: All statistical claims and financial facts MUST be verified via authoritative sources
- **FR-008**: Chapter MUST build on Chapter 5 (Claude Code fundamentals) without re-teaching basics
- **FR-009**: Governance and compliance considerations MUST be woven throughout, not isolated to one lesson
- **FR-010**: No coding or programming MUST be required - all interactions are natural language
- **FR-011**: Directory MUST be renamed from `07-claude-code-for-professions` to `07-claude-code-for-finance`

### Key Entities

- **Finance Professional**: Target learner - accountant, analyst, controller, auditor, or CFO with domain expertise but no technical background
- **Claude Code**: The General Agent tool used for AI-assisted finance workflows
- **CLAUDE.md**: Context file that encodes company-specific accounting rules and policies
- **Three-Layer Architecture**: Intelligence (Claude) + Execution (Spreadsheet) + Governance (Human)
- **Multi-Agent Pattern**: Conceptual architecture with specialized agents (Modeler, Analyst, Validator, Narrator)

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: Finance professionals with no coding experience can complete all 10 lessons within the estimated 210 minutes total duration
- **SC-002**: 90% of "Try With AI" prompts produce actionable outputs when copied directly into Claude Code
- **SC-003**: Students can create a working CLAUDE.md file for their finance context within 15 minutes of completing Lesson 2
- **SC-004**: Quiz pass rate of 80% or higher demonstrates concept mastery across all lesson topics
- **SC-005**: Capstone workflow specifications are immediately usable in student's actual work environment
- **SC-006**: All content passes educational-validator, validation-auditor, factual-verifier, and pedagogical-designer checks
- **SC-007**: Students report increased confidence in AI-assisted finance workflows after chapter completion (qualitative survey)
- **SC-008**: Chapter content aligns with Part 2 proficiency expectations (A2-B1) as defined in chapter-index.md

---

## Lesson Structure Summary

| # | Title | Layer | Proficiency | Duration | Key Concepts |
|---|-------|-------|-------------|----------|--------------|
| 1 | The Finance Professional's AI Transformation | L1 | A2 | 15 min | Intent-driven systems, AI reasoning vs rules, human-in-the-loop, separation of concerns, paradigm shift |
| 2 | Setting Up Your Finance Workspace | L1-L2 | A2 | 20 min | Finance workspace isolation, CLAUDE.md domain context, accounting rules as context, permission hierarchy, data safety, sandbox vs production |
| 3 | Prompt Engineering for Financial Analysis | L2 | A2 | 25 min | Chain-of-thought reasoning, audit-ready explanations, prompt templates, context optimization, structured outputs, iterative refinement |
| 4 | Intent-Driven Financial Modeling | L2 | A2-B1 | 25 min | Intent-to-model translation, revenue modeling, expense forecasting, assumption documentation, sensitivity analysis, model refactoring, narrative generation |
| 5 | Claude Code + Google Sheets Architecture | L2 | B1 | 25 min | Three-layer architecture, spreadsheet as execution engine, Claude as reasoning layer, formula generation, model transparency, version control |
| 6 | AI-Native Accounting Workflows | L2 | B1 | 25 min | Transaction classification, reconciliation logic, journal entry generation, audit trail documentation, invoice processing, explanation vs execution, ledger integrity |
| 7 | Scenario Analysis and Risk Assessment | L2-L3 | B1 | 25 min | Scenario definition, stress testing, risk identification, sensitivity analysis, causality explanation, decision-support narratives |
| 8 | Multi-Agent Finance Patterns (Conceptual) | L3 | B1 | 20 min | Agent specialization, parallel processing, orchestration, month-end close workflow, when to use multi-agent |
| 9 | Governance, Compliance, and Safety | L2 | B1 | 20 min | Human-in-the-loop governance, approval workflows, audit trails, read-only vs write access, data privacy, compliance boundaries, AI limitations |
| 10 | Capstone - Your Finance AI Workflow | L4 | B1 | 30 min | Integration of all concepts into production-ready workflow specification |

---

## Non-Goals (Explicitly Out of Scope)

- **No coding/programming**: Natural language interaction only
- **No SDK development**: That's Part 6 content
- **No MCP server setup**: Too technical for audience
- **No specific software integration setup** (Xero/QuickBooks configuration): Conceptual patterns only
- **No tax/legal advice**: Finance workflow patterns only, not professional financial advice
- **No enterprise deployment**: Focus on individual professional use

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Finance terminology inaccuracy | Use WebSearch for verification; invoke factual-verifier |
| Cognitive overload for non-technical users | Strict 5-7 concept limit per lesson; review by pedagogical-designer |
| Chapter 5 prerequisite assumptions | Cross-reference Chapter 5 content explicitly |
| Generic AI advice instead of finance-specific | Ground all examples in PDF source material |
| Platform-specific content becoming outdated | Use platform-agnostic patterns with multiple examples |

---

## Implementation Notes

### Directory Change
The existing `apps/learn-app/docs/02-AI-Tool-Landscape/07-claude-code-for-professions/` directory must be deleted and replaced with `07-claude-code-for-finance/`.

### Quality Reference
All lessons should match the structure and quality of:
`apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/01-origin-story.md`

### Validation Requirements
Before commit, all content must pass:
- `educational-validator` (per lesson)
- `validation-auditor` (chapter-wide)
- `factual-verifier` (chapter-wide)
- `pedagogical-designer` (chapter-wide)
