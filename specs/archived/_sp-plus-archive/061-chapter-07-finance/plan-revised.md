# Chapter 7: Claude Code for Finance Professionals - REVISED Implementation Plan

**Revision Reason**: Original plan missed critical Chapter 5 building blocks (Skills, MCP Servers, Subagents, Digital FTE concept). This revision properly builds on Chapter 5 concepts.

**Source Documents**:
- `docs/Agentic_Financial_Planning.pdf` - Claude Code as "Financial Reasoning Engine", three-layer architecture, multi-agent patterns
- `docs/Claude_Xero_AI_Native_Accounting.pdf` - "AI-assisted, human-governed" model, reasoning vs rules

---

## Key Terminology from Source Documents

| Term | Definition | Source |
|------|------------|--------|
| **Financial Reasoning Engine** | Claude Code interprets intent and reasons over financial data | Agentic_Financial_Planning |
| **Intent-Driven Modeling** | Express objectives in natural language, Claude translates to financial logic | Agentic_Financial_Planning |
| **Three-Layer Architecture** | Intelligence (Claude) + Logic (Sheets) + Interface (Users) | Agentic_Financial_Planning |
| **AI-assisted, human-governed** | Claude reasons and suggests, humans verify and approve | Claude_Xero |
| **Reasoning Engine vs Rules Engine** | Claude reasons contextually; traditional automation executes predefined logic | Claude_Xero |

---

## Chapter 5 Concepts Applied to Finance

| Chapter 5 Concept | Chapter 7 Application |
|-------------------|----------------------|
| **General Agent** | Claude Code as Financial Reasoning Engine |
| **Skills** | Finance-specific skills (variance-analyzer, transaction-classifier, reconciliation-assistant) |
| **MCP Servers** | Google Sheets MCP for spreadsheet integration, conceptual Xero/QuickBooks MCP |
| **Subagents** | Financial Modeler, Scenario Analyst, Risk Assessor, Validator, Narrative Generator |
| **CLAUDE.md** | Encoding accounting rules, chart of accounts, fiscal policies as context |
| **Digital FTE** | Finance Digital FTE that handles end-to-end finance workflows |

---

## Revised Lesson Structure

### Lesson 1: Claude Code General Agent for Finance
**Slug**: `01-general-agent-finance`
**Layer**: L1 (Foundation)
**Proficiency**: A2
**Duration**: 15 min

**Core Message**: Claude Code is not just a tool—it's a **General Agent** that can reason about finance. From Chapter 5, you learned Claude Code is a General Agent. Now apply that to finance as a **Financial Reasoning Engine**.

**Key Concepts** (5):
1. General Agent applied to finance domain
2. Financial Reasoning Engine (from source doc)
3. Reasoning vs Rules - Claude reasons contextually, traditional automation executes rules
4. Intent-driven systems - express goals in natural language
5. "AI-assisted, human-governed" operating model

**Chapter 5 Prerequisites**:
- General Agent concept (Ch5 L1)
- OODA reasoning loop (Ch5 L1)

**Source Material**: Agentic_Financial_Planning §1-4, Claude_Xero §1-3

**Try With AI**:
1. "I need to understand why our Q3 expenses exceeded budget. Reason through the possible causes step-by-step." (Demonstrates reasoning vs calculation)
2. "Classify this transaction: 'AWS Invoice $2,340 - Monthly cloud services'. Explain your reasoning." (Shows contextual reasoning)
3. "Compare how a rules-based system vs your reasoning approach would handle: 'Client paid invoice #1234 but amount differs by $50.'" (Contrasts paradigms)

---

### Lesson 2: Finance Workspace Setup with CLAUDE.md
**Slug**: `02-finance-workspace-setup`
**Layer**: L1→L2
**Proficiency**: A2
**Duration**: 20 min

**Core Message**: From Chapter 5, you learned CLAUDE.md provides persistent context. In finance, this means encoding your **chart of accounts, fiscal year, accounting policies, and compliance rules** so Claude understands your domain.

**Key Concepts** (6):
1. CLAUDE.md as domain context (from Ch5)
2. Encoding accounting rules as AI context
3. Chart of accounts structure
4. Fiscal year and reporting periods
5. Permission hierarchy (read-only by default)
6. Data safety classification

**Chapter 5 Prerequisites**:
- CLAUDE.md context files (Ch5 L8)
- Permission settings (Ch5 L12)

**CLAUDE.md Example for Finance**:
```markdown
# Finance Workspace Context

## Company Profile
- Fiscal Year: July 1 - June 30
- Reporting Currency: USD
- Tax Jurisdiction: US Federal + California

## Chart of Accounts
- 1000-1999: Assets
- 2000-2999: Liabilities
- 3000-3999: Equity
- 4000-4999: Revenue
- 5000-6999: Expenses

## Accounting Policies
- Revenue recognition: Point of delivery
- Depreciation: Straight-line over useful life
- Inventory: FIFO method

## Governance Rules
- All AI suggestions require human approval before posting
- Never modify historical transactions
- Flag any transaction > $10,000 for review
```

**Try With AI**:
1. "Help me create a CLAUDE.md for my finance workspace. My company uses calendar year, we're in the UK, and follow IFRS standards."
2. "Review this CLAUDE.md and suggest what accounting policies I should add for a SaaS company."
3. "Given my CLAUDE.md context, classify this transaction: 'Received $50,000 from CustomerCo for annual subscription starting next month.'"

---

### Lesson 3: Creating Finance Skills
**Slug**: `03-finance-skills`
**Layer**: L2
**Proficiency**: A2→B1
**Duration**: 25 min

**Core Message**: From Chapter 5, you learned Skills are **reusable intelligence**. Finance professionals should create finance-specific skills that encode their expertise and can be reused across workflows.

**Key Concepts** (7):
1. Skills as reusable intelligence (from Ch5)
2. Skill anatomy (persona, logic, context, safety)
3. Finance skill patterns
4. Building a `variance-analyzer` skill
5. Building a `transaction-classifier` skill
6. Skill composition for complex workflows
7. Skills as sellable Digital FTE components

**Chapter 5 Prerequisites**:
- Agent Skills (Ch5 L9)
- Skill Factory Pattern (Ch5 L10)
- skill-creator tool (Ch5 L10)

**Example Finance Skills**:

**variance-analyzer skill**:
```yaml
name: variance-analyzer
description: Analyzes budget vs actual variances with audit-ready explanations

persona: Senior FP&A Analyst with 10+ years experience
logic: |
  1. Identify significant variances (>5% or >$10K)
  2. Categorize as favorable/unfavorable
  3. Trace to root causes
  4. Generate audit-ready explanation
safety: |
  - Always show calculation methodology
  - Flag assumptions explicitly
  - Recommend human review for material variances
```

**transaction-classifier skill**:
```yaml
name: transaction-classifier
description: Classifies transactions with contextual reasoning

persona: Experienced bookkeeper with industry knowledge
logic: |
  1. Analyze vendor name and description
  2. Match to chart of accounts
  3. Consider historical patterns
  4. Provide confidence level and reasoning
safety: |
  - Never auto-post to ledger
  - Flag low-confidence classifications
  - Explain reasoning for audit trail
```

**Try With AI**:
1. "Help me design a skill for monthly reconciliation. What persona, logic, and safety rules should it have?"
2. "Create a skill specification for analyzing cash flow trends and predicting shortfalls."
3. "I have a variance-analyzer skill. How would I compose it with a narrative-generator skill for board reports?"

---

### Lesson 4: Connecting to Google Sheets via MCP
**Slug**: `04-sheets-mcp-integration`
**Layer**: L2
**Proficiency**: B1
**Duration**: 25 min

**Core Message**: From Chapter 5, you learned MCP servers connect Claude Code to external systems. For finance, **Google Sheets MCP** implements the three-layer architecture: Claude reasons, Sheets computes.

**Key Concepts** (6):
1. MCP servers for external access (from Ch5)
2. Google Sheets MCP server setup
3. Three-layer architecture implementation
4. Claude as Intelligence layer
5. Sheets as Execution layer (deterministic computation)
6. Formula generation from intent

**Chapter 5 Prerequisites**:
- MCP servers (Ch5 L6-7)
- External integration patterns (Ch5 L6)

**Architecture Diagram**:
```
User Intent ("Model revenue growth at 15% MoM")
         ↓
    Claude Code (Reasoning)
    - Interprets intent
    - Designs model structure
    - Generates formulas
         ↓
    Google Sheets MCP
    - Creates/modifies cells
    - Executes formulas
    - Returns results
         ↓
    Claude Code (Analysis)
    - Interprets results
    - Generates narratives
    - Suggests refinements
```

**Try With AI**:
1. "Using the Google Sheets MCP, create a 12-month revenue projection in my Financial Model sheet. Start with $100K in January, grow 15% monthly."
2. "Read my Q3 actuals from the Budget sheet and compare to plan. Explain the top 3 variances."
3. "Generate a SUMIFS formula for calculating total expenses by department for the current fiscal year."

---

### Lesson 5: Intent-Driven Financial Modeling
**Slug**: `05-intent-driven-modeling`
**Layer**: L2
**Proficiency**: B1
**Duration**: 25 min

**Core Message**: Traditional modeling requires building formulas manually. With Claude Code as a **Financial Reasoning Engine**, you express intent in natural language and Claude generates the model.

**Key Concepts** (7):
1. Intent-to-model translation
2. Revenue modeling patterns
3. Expense forecasting (fixed, variable, step)
4. Assumption documentation
5. Model refactoring with AI
6. Sensitivity analysis
7. Narrative generation for stakeholders

**Source Material**: Agentic_Financial_Planning §4

**Example Intent-Driven Workflow**:
```
Human: "Model a conservative revenue scenario where we lose our largest
        customer (20% of revenue) in Q2, then recover 50% through
        new business by Q4."

Claude: [Reasons through the scenario]
        - Current revenue: $500K/month
        - Largest customer: $100K/month (20%)
        - Q2 loss: -$100K/month starting April
        - Recovery: +$50K/month by December

        [Generates model specification]
        - Creates monthly projection
        - Documents all assumptions
        - Builds formulas in Sheets via MCP
        - Produces executive summary
```

**Try With AI**:
1. "We're launching a new product. Revenue starts at $10K in month 1, grows 20% monthly for 6 months, then stabilizes. Create a 12-month model."
2. "Refactor my existing expense model to handle step costs when we hire. Currently it assumes linear growth."
3. "Review this revenue model and list every assumption. For each, tell me what data I need to validate it."

---

### Lesson 6: AI-Native Accounting Workflows
**Slug**: `06-ai-native-accounting`
**Layer**: L2
**Proficiency**: B1
**Duration**: 25 min

**Core Message**: Apply the **"AI-assisted, human-governed"** model to accounting. Claude reasons about transactions; humans approve before posting.

**Key Concepts** (7):
1. Reasoning-based transaction classification
2. Reconciliation with anomaly detection
3. Journal entry generation with explanations
4. Audit trail documentation
5. Invoice/receipt processing
6. Explanation vs execution separation
7. Ledger integrity (AI suggests, never posts)

**Source Material**: Claude_Xero §5

**Separation of Responsibilities**:
| Component | Responsibility |
|-----------|---------------|
| Claude Code | Reasoning, interpretation, classification |
| Accounting System | Recording, validation, compliance |
| Human | Approval, oversight, exceptions |

**Try With AI**:
1. "Here are 10 transactions from our bank feed. Classify each with reasoning so I can verify before posting: [list transactions]"
2. "Bank shows $45,230, ledger shows $44,890. Walk me through a systematic approach to find the $340 difference."
3. "Generate a journal entry for: Customer paid $5,000 deposit - $3,000 is prepaid service, $2,000 is equipment sale. Include audit explanation."

---

### Lesson 7: Connecting to Accounting Platforms
**Slug**: `07-accounting-platform-mcp`
**Layer**: L2
**Proficiency**: B1
**Duration**: 20 min

**Core Message**: Just as Google Sheets connects via MCP, accounting platforms (Xero, QuickBooks) can connect via MCP servers, enabling Claude to reason about your actual financial data.

**Key Concepts** (5):
1. Accounting platform MCP patterns (conceptual)
2. Read-only access by default
3. Platform-agnostic workflow design
4. API-first architecture
5. Safe integration patterns

**Important Caveat**: This lesson is conceptual. Actual MCP server implementation for Xero/QuickBooks may require technical setup beyond this course's scope. Focus is on the pattern.

**Platform-Agnostic Pattern**:
```
                    ┌──────────────────┐
                    │   Claude Code    │
                    │ (Reasoning Layer)│
                    └────────┬─────────┘
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
    ┌──────▼─────┐    ┌──────▼─────┐    ┌──────▼─────┐
    │ Sheets MCP │    │  Xero MCP  │    │   QB MCP   │
    └──────┬─────┘    └──────┬─────┘    └──────┬─────┘
           │                 │                 │
    ┌──────▼─────┐    ┌──────▼─────┐    ┌──────▼─────┐
    │   Google   │    │    Xero    │    │ QuickBooks │
    │   Sheets   │    │  Ledger    │    │   Online   │
    └────────────┘    └────────────┘    └────────────┘
```

**Try With AI**:
1. "Design a workflow for processing invoices that works whether I use Xero, QuickBooks, or just Google Sheets."
2. "What safeguards should a Xero MCP server have to ensure Claude can't accidentally modify the ledger?"
3. "If I had read-only access to my accounting system via MCP, what analysis could Claude perform?"

---

### Lesson 8: Finance Subagents
**Slug**: `08-finance-subagents`
**Layer**: L3
**Proficiency**: B1
**Duration**: 25 min

**Core Message**: From Chapter 5, you learned about Subagents. The source documents describe **multiple specialized agents working simultaneously**: Financial Modeler, Scenario Analyst, Risk Assessor, Validator, Narrative Generator.

**Key Concepts** (6):
1. Subagents from Chapter 5 applied to finance
2. Agent specialization (focused expertise)
3. Finance subagent roles (from source docs)
4. Orchestration patterns (sequential, parallel)
5. Month-end close as multi-agent workflow
6. When multi-agent adds value vs complexity

**Chapter 5 Prerequisites**:
- Subagent orchestration (Ch5 L5)
- Explore agent and Plan mode (Ch5 L5)

**Finance Subagent Roles** (from Agentic_Financial_Planning):

| Subagent | Role |
|----------|------|
| **Financial Modeler** | Builds and refactors financial models |
| **Scenario Analyst** | Creates and compares multiple scenarios |
| **Risk Assessor** | Identifies risks and stress tests |
| **Validator** | Checks model integrity and assumptions |
| **Narrative Generator** | Creates stakeholder-ready explanations |

**Example: Month-End Close Orchestration**:
```
User: "Run month-end close for October"

Orchestrator delegates to:
  1. Validator → Verify all transactions posted
  2. Financial Modeler → Update forecasts with actuals
  3. Scenario Analyst → Compare to plan scenarios
  4. Risk Assessor → Flag unusual items
  5. Narrative Generator → Create CFO summary

All report back → Orchestrator compiles final package
```

**Try With AI**:
1. "Design a subagent for variance analysis. What should its specialty be? What tools does it need?"
2. "Our month-end involves: data validation, variance analysis, forecast updates, and board reporting. Map this to specialized subagents."
3. "When should I use one general Claude conversation vs multiple specialized subagents? Help me decide for my quarterly reporting."

---

### Lesson 9: Governance, Compliance, and Safety
**Slug**: `09-governance-compliance`
**Layer**: L2
**Proficiency**: B1
**Duration**: 20 min

**Core Message**: Finance demands strict governance. Claude Code must be **AI-assisted, human-governed**. This lesson codifies what Claude should and should NOT do.

**Key Concepts** (7):
1. Human-in-the-loop governance patterns
2. Approval workflow design
3. Audit trail requirements
4. Read-only vs write access principles
5. What Claude should NEVER do
6. Compliance boundaries
7. AI limitations acknowledgment

**Source Material**: Claude_Xero §7

**What Claude Should NEVER Do** (from source doc):
- Post transactions autonomously
- Override accounting controls
- Make tax decisions without review
- Replace human approval

**Required Safeguards**:
- Human-in-the-loop approvals
- Read-only access by default
- Logged reasoning outputs
- Versioned changes
- Role-based permissions

**Governance Skill Pattern**:
```yaml
name: finance-governance-checker
description: Validates workflows against governance requirements

checks:
  - Human approval checkpoint exists
  - No autonomous ledger modifications
  - Reasoning is logged for audit
  - Material items flagged for review
  - Tax implications require human sign-off
```

**Try With AI**:
1. "Design approval workflow for AI-assisted journal entries. Where must humans review? What should they check?"
2. "Create an audit trail template for documenting AI-assisted decisions. What must be captured?"
3. "Review this workflow: 'Claude classifies transactions, then auto-posts to ledger.' What governance violations exist?"

---

### Lesson 10: Capstone - Building Your Finance Digital FTE
**Slug**: `10-capstone-finance-digital-fte`
**Layer**: L4
**Proficiency**: B1
**Duration**: 30 min

**Core Message**: Combine everything—Skills, MCP connections, Subagents, Governance—into a complete **Finance Digital FTE** that handles end-to-end workflows.

**Key Concepts** (6):
1. Digital FTE concept (from Ch5)
2. Composing Skills + MCP + Subagents
3. Workflow specification structure
4. Recurring workflow automation
5. Stakeholder output requirements
6. Production deployment considerations

**Digital FTE Components**:
```
Finance Digital FTE
├── Skills (Reusable Intelligence)
│   ├── variance-analyzer
│   ├── transaction-classifier
│   ├── reconciliation-assistant
│   └── narrative-generator
│
├── MCP Connections (External Systems)
│   ├── Google Sheets MCP
│   └── Accounting Platform MCP (conceptual)
│
├── Subagents (Specialized Roles)
│   ├── Financial Modeler
│   ├── Scenario Analyst
│   ├── Risk Assessor
│   └── Validator
│
└── Governance (Safety Rails)
    ├── Human-in-the-loop checkpoints
    ├── Audit logging
    └── Access controls
```

**Capstone Project Options**:
1. **Monthly Financial Health Checkup** - Automated variance analysis, metrics review, executive summary
2. **Accounts Receivable Aging Workflow** - Customer analysis, collection priority, risk assessment
3. **Budget vs Actual Reporting** - Variance identification, explanation generation, action recommendations
4. **Cash Flow Forecasting** - Rolling forecast, scenario analysis, liquidity alerts

**Capstone Deliverables**:
1. CLAUDE.md with domain context
2. 2-3 Finance Skills
3. MCP integration design
4. Subagent orchestration plan
5. Governance checklist
6. Workflow specification document

**Try With AI**:
1. "Help me design a Finance Digital FTE for monthly close. What Skills, MCP connections, and Subagents do I need?"
2. "Review my capstone specification. Does it have all components? What's missing for production use?"
3. "I want to sell my Finance Digital FTE to other finance teams. What makes it valuable? How would I package it?"

---

## Validation Checklist

### Chapter 5 Integration
- [ ] General Agent concept referenced in L1
- [ ] Skills concept applied in L3
- [ ] MCP servers applied in L4, L7
- [ ] Subagents applied in L8
- [ ] CLAUDE.md applied in L2
- [ ] Digital FTE concept in L10

### Source Document Terminology
- [ ] "Financial Reasoning Engine" used
- [ ] "Intent-driven" modeling explained
- [ ] "AI-assisted, human-governed" pattern emphasized
- [ ] "Reasoning vs rules" distinction made
- [ ] Three-layer architecture from docs
- [ ] Multi-agent roles from Agentic_Financial_Planning

### Cognitive Load
- [ ] A2 lessons: 5-6 concepts
- [ ] B1 lessons: 6-7 concepts
- [ ] No programming required

---

**Plan Status**: REVISED - Ready for implementation with corrected Chapter 5 integration
