---
title: "Finance Workspace Setup with CLAUDE.md"
sidebar_position: 2
chapter: 7
lesson: 2
duration_minutes: 20

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L1 → L2 (Foundation transitioning to Collaboration)"
layer_1_foundation: "Applying CLAUDE.md knowledge from Chapter 3 to finance-specific context configuration"
layer_2_collaboration: "Co-creating finance CLAUDE.md with AI, refining accounting rules and governance policies through iteration"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Creating Finance-Specific CLAUDE.md Context"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can create a CLAUDE.md file that encodes company-specific accounting rules, chart of accounts structure, and fiscal context for finance workflows"

  - name: "Configuring Financial Data Safety Settings"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can configure appropriate permission settings with read-only defaults for financial data and identify what data categories require different safety levels"

  - name: "Organizing Finance Workspace Isolation"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can organize a finance workspace with proper isolation between sandbox and production environments"

learning_objectives:
  - objective: "Create a CLAUDE.md file that encodes company-specific accounting rules, chart of accounts, and fiscal context"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Creation of complete finance CLAUDE.md with all required sections (company profile, chart of accounts, accounting policies, governance rules)"
  - objective: "Configure appropriate permission settings for financial data safety with read-only defaults"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Demonstration of permission configuration that prevents unauthorized modifications to financial records"
  - objective: "Organize a finance workspace with proper isolation between sandbox and production environments"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Setup of directory structure that separates test data from live financial data"

# Cognitive load tracking
cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (CLAUDE.md as domain context, encoding accounting rules, fiscal year configuration, permission hierarchy, workspace isolation, data safety classification) - within A2 limit of 7"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Create multi-region CLAUDE.md configurations with different GAAP/IFRS standards, implement environment-specific permission matrices"
  remedial_for_struggling: "Focus on single company profile with basic chart of accounts, skip advanced permission configuration"

# Generation metadata
generated_by: "content-implementer"
source_spec: "prompt-based"
created: "2026-01-01"
last_modified: "2026-01-01"
git_author: "Claude Code"
workflow: "autonomous"
version: "1.0.0"

# Legacy compatibility (Docusaurus)
prerequisites:
  - "Chapter 3, Lesson 8: CLAUDE.md Context Files"
  - "Chapter 7, Lesson 1: Claude Code General Agent for Finance"
---

# Finance Workspace Setup with CLAUDE.md

Your company follows specific accounting rules. You use a particular chart of accounts. Your fiscal year might run July through June instead of calendar year. Your jurisdiction determines which tax regulations apply.

Claude Code knows none of this—unless you tell it.

In Chapter 3, Lesson 8, you learned to create CLAUDE.md files that provide persistent project context. You saw how a single markdown file eliminates the friction of re-explaining your tech stack, directory structure, and coding conventions every session.

Now you'll apply that same principle to finance—creating a CLAUDE.md that encodes your company's accounting reality so Claude Code reasons about your financial data correctly from the first prompt.

---

## Building on Chapter 3

In Chapter 3, you learned that CLAUDE.md contains six standard sections:

1. **Project Overview**: What does your project do?
2. **Technology Stack**: Languages, frameworks, dependencies
3. **Directory Structure**: Where files live
4. **Coding Conventions**: Style and patterns
5. **Key Commands**: Common operations
6. **Important Notes**: Gotchas and critical context

For finance, these sections transform:

| Chapter 3 Section   | Finance Equivalent                                              |
| ------------------- | --------------------------------------------------------------- |
| Project Overview    | Company Profile (fiscal year, jurisdiction, reporting currency) |
| Technology Stack    | Financial Systems (accounting software, integrations)           |
| Directory Structure | Data Organization (where financial files live)                  |
| Coding Conventions  | Accounting Policies (GAAP rules, recognition policies)          |
| Key Commands        | Common Workflows (reconciliation steps, close procedures)       |
| Important Notes     | Governance Rules (approval thresholds, audit requirements)      |

The structure is the same. The domain content is different.

---

## The Finance CLAUDE.md Template

Here's a complete CLAUDE.md template for finance work. This becomes Claude's understanding of your financial reality:

```markdown
# Finance Workspace Context

## Company Profile

- **Company Name**: [Your Company Name]
- **Fiscal Year**: July 1 - June 30
- **Reporting Currency**: USD
- **Functional Currency**: USD
- **Tax Jurisdiction**: US Federal + California
- **Accounting Standard**: US GAAP
- **Entity Type**: C-Corporation

## Chart of Accounts Structure

Our chart of accounts follows this numbering convention:

| Range     | Category             | Examples                                                          |
| --------- | -------------------- | ----------------------------------------------------------------- |
| 1000-1999 | Assets               | 1010 Cash, 1200 Accounts Receivable, 1500 Fixed Assets            |
| 2000-2999 | Liabilities          | 2010 Accounts Payable, 2100 Accrued Expenses, 2500 Long-term Debt |
| 3000-3999 | Equity               | 3010 Common Stock, 3500 Retained Earnings                         |
| 4000-4999 | Revenue              | 4010 Product Revenue, 4500 Service Revenue                        |
| 5000-5999 | Cost of Goods Sold   | 5010 Direct Materials, 5500 Direct Labor                          |
| 6000-6999 | Operating Expenses   | 6100 Salaries, 6200 Rent, 6500 Marketing                          |
| 7000-7999 | Other Income/Expense | 7010 Interest Income, 7500 Interest Expense                       |

## Accounting Policies

- **Revenue Recognition**: Point of delivery for products; over time for services based on milestones
- **Depreciation Method**: Straight-line over useful life
  - Computer Equipment: 3 years
  - Furniture: 7 years
  - Leasehold Improvements: Lesser of lease term or useful life
- **Inventory Method**: FIFO (First-In, First-Out)
- **Bad Debt Allowance**: 2% of receivables over 90 days
- **Capitalization Threshold**: Items over $2,500
- **Prepaid Amortization**: Straight-line over benefit period

## Cost Center Structure

- **100**: General & Administrative
- **200**: Sales & Marketing
- **300**: Engineering
- **400**: Customer Success
- **500**: Research & Development

## Governance Rules

- All AI suggestions require human approval before posting to ledger
- Never modify historical transactions without documented adjustment
- Flag any transaction > $10,000 for management review
- Flag any journal entry that affects retained earnings
- Month-end close requires explicit approval before finalizing
- All vendor changes require secondary verification

## Data Sensitivity Classification

- **Share with AI**: Trial balance exports, variance reports, budget templates
- **Verify before sharing**: Customer names, vendor payment details
- **Never share**: Bank account numbers, SSN/EIN, credit card data, passwords

## Key Workflows

- **Daily**: Bank reconciliation, AR aging review, AP queue processing
- **Weekly**: Cash flow forecast update, expense report processing
- **Monthly**: Close checklist, variance analysis, management reporting
- **Quarterly**: 941 payroll tax, sales tax filing, board deck preparation

## File Locations

- Working files: `finance/working/`
- Final reports: `finance/reports/[YYYY-MM]/`
- Templates: `finance/templates/`
- Archive: `finance/archive/`
- Test data (sandbox): `finance/sandbox/`
```

This CLAUDE.md gives Claude Code essential context:

- Your fiscal year determines period calculations
- Your chart of accounts determines transaction classification
- Your accounting policies determine treatment of specific scenarios
- Your governance rules determine what requires human approval

---

## Key Components Explained

### Company Profile

The company profile establishes foundational facts that affect every financial analysis:

```markdown
## Company Profile

- **Fiscal Year**: July 1 - June 30
- **Reporting Currency**: USD
- **Tax Jurisdiction**: US Federal + California
```

**Why this matters**: When Claude analyzes Q3 revenue, it needs to know whether Q3 means July-September (calendar year) or January-March (your fiscal year). When suggesting tax treatment, it needs to know which jurisdiction's rules apply.

### Chart of Accounts

The chart of accounts structure tells Claude how your company organizes financial data:

```markdown
| Range     | Category    |
| --------- | ----------- |
| 1000-1999 | Assets      |
| 2000-2999 | Liabilities |
```

**Why this matters**: When Claude suggests how to categorize a transaction, it should use account numbers that exist in your system. "Classify as Marketing Expense" is helpful. "Classify to account 6500" is more helpful.

### Accounting Policies

Accounting policies encode the rules that govern how transactions are recorded:

```markdown
## Accounting Policies

- **Revenue Recognition**: Point of delivery for products
- **Depreciation Method**: Straight-line over useful life
- **Capitalization Threshold**: Items over $2,500
```

**Why this matters**: Without this context, Claude might suggest capitalizing a $500 software subscription (wrong) or depreciating equipment using declining balance (not your policy). Your policies become Claude's policies.

### Governance Rules

Governance rules define what Claude should flag versus handle automatically:

```markdown
## Governance Rules

- All AI suggestions require human approval before posting
- Flag any transaction > $10,000 for management review
- Never modify historical transactions without documented adjustment
```

**Why this matters**: These rules prevent Claude from suggesting actions that violate your controls. Claude learns that recommending a post is fine; actually posting is not.

---

## Permission and Safety Configuration

Financial data requires careful handling. Configure Claude Code's permissions to match your risk tolerance.

### The Read-Only Default

For finance work, start with a conservative permission stance:

```bash
# When starting Claude Code for finance work
claude --permission-mode ask

# This ensures Claude asks before any write operation
```

The `ask` permission mode means Claude will:

- Read files freely (analyze your data)
- Request permission before writing anything
- Never modify files without explicit approval

This matches the AI-assisted, human-governed model from Lesson 1.

### Data Safety Classification

Your CLAUDE.md should include explicit guidance on data sensitivity:

```markdown
## Data Sensitivity Classification

- **Share with AI**: Trial balance exports, variance reports, budget templates
- **Verify before sharing**: Customer names, vendor payment details
- **Never share**: Bank account numbers, SSN/EIN, credit card data, passwords
```

**Think of it this way**: Claude Code operates within your file system. Anything in your project directory is potentially accessible. Structure your workspace so sensitive data isn't accidentally exposed.

### What Goes Where

| Data Type                | Location                           | AI Access   |
| ------------------------ | ---------------------------------- | ----------- |
| Working analysis         | `finance/working/`                 | Full access |
| Report drafts            | `finance/reports/`                 | Full access |
| Test data                | `finance/sandbox/`                 | Full access |
| Export files (sanitized) | `finance/exports/`                 | Full access |
| Credentials, API keys    | Outside project OR `.claudeignore` | No access   |
| Raw bank data            | Outside project OR `.claudeignore` | No access   |

---

## Workspace Isolation: Sandbox vs Production

Finance requires separating test work from real data. Your directory structure should enforce this:

```
finance-workspace/
├── CLAUDE.md                    # Your finance context file
├── sandbox/                     # Safe experimentation zone
│   ├── test-transactions.csv   # Fake data for testing
│   ├── sample-trial-balance.xlsx
│   └── practice-reconciliation/
├── working/                     # Current period work
│   ├── 2024-12/               # Monthly working files
│   │   ├── bank-rec.xlsx
│   │   └── variance-analysis.xlsx
│   └── templates/
├── reports/                     # Finalized outputs
│   └── 2024-12/
│       ├── financial-statements.pdf
│       └── management-report.xlsx
└── archive/                     # Historical data (read-only)
    └── 2024-Q3/
```

### The Sandbox Pattern

The `sandbox/` directory is your safe zone for:

- Testing Claude's suggestions before applying to real data
- Learning new workflows without risk
- Experimenting with different analysis approaches

**Rule**: Always test new Claude workflows in sandbox first.

### Working vs Archive

- **Working** (`working/`): Current period files you're actively modifying
- **Archive** (`archive/`): Closed periods you reference but don't change

Consider making archive directories read-only at the filesystem level. This adds a layer of protection beyond CLAUDE.md governance rules.

---

## Creating Your Finance CLAUDE.md

Now put this into practice. Here's the workflow:

### Step 1: Start with the Template

Copy the template from this lesson and save it as `CLAUDE.md` in your finance workspace root.

### Step 2: Customize Core Details

Update these sections with your actual information:

1. **Company Profile**: Your fiscal year, jurisdiction, currency
2. **Chart of Accounts**: Your actual account structure (even a simplified version helps)
3. **Accounting Policies**: Your key policies (start with revenue recognition and depreciation)
4. **Governance Rules**: Your approval thresholds and control requirements

### Step 3: Verify Context Loading

Start a new Claude Code session and test:

```bash
cd ~/finance-workspace
claude

# In Claude Code:
"What's our fiscal year end?"
```

If Claude answers correctly based on your CLAUDE.md—it loaded successfully.

### Step 4: Refine Through Use

Your first CLAUDE.md won't be perfect. As you work with Claude on finance tasks, you'll discover:

- Policies you forgot to include
- Governance rules that need clarification
- Account structures that need more detail

Update CLAUDE.md as you learn what context makes Claude's suggestions more accurate.

---

## Common Finance Context Patterns

Different finance roles need different CLAUDE.md emphasis:

### For Accounts Payable Focus

```markdown
## AP-Specific Context

- Invoice approval workflow: < $1,000 auto-approve, $1,000-$10,000 manager, > $10,000 director
- Preferred payment terms: Net 30 standard, Net 15 for early payment discount > 2%
- Duplicate detection: Flag invoices within 5% of same vendor in 30-day window
- Vendor master: Always verify new vendors against existing before creating duplicate
```

### For Financial Planning & Analysis

```markdown
## FP&A-Specific Context

- Budget calendar: Board presentation Q4 Week 2, department submissions Q3 Week 4
- Variance threshold: Investigate any line item > 10% or > $25,000 from budget
- Forecast updates: Monthly rolling 12-month, quarterly board deck
- Key metrics: ARR, CAC, LTV, Burn Rate, Runway (SaaS business)
```

### For Month-End Close

```markdown
## Close-Specific Context

- Close calendar: Soft close Day 3, Hard close Day 5, Reporting Day 8
- Critical reconciliations: Bank (daily), AR (Day 2), AP (Day 2), Prepaids (Day 3)
- Cutoff rules: Revenue through last day of month, expenses through Day 1 of next month
- Approval chain: Staff prepares → Senior reviews → Controller approves
```

---

## Try With AI

Put your finance CLAUDE.md knowledge into practice through these collaborative exercises.

**Prompt 1: Create Your Finance CLAUDE.md**

```
Help me create a CLAUDE.md for my finance workspace. My company details:
- We use calendar year (January-December fiscal year)
- We're a UK company following IFRS standards
- We're in the professional services industry
- Our chart of accounts uses 4-digit codes: 1xxx Assets, 2xxx Liabilities, 3xxx Equity, 4xxx Revenue, 5xxx Expenses

Create a complete CLAUDE.md with:
1. Company Profile section
2. Chart of Accounts structure
3. Key accounting policies for a services business
4. Governance rules with appropriate thresholds
5. Data sensitivity classification

Make it specific to a UK IFRS professional services company.
```

**What you're learning**: This prompt applies the template to your specific context. Notice how Claude adapts the structure—IFRS has different revenue recognition rules than US GAAP, UK has different tax considerations. Your CLAUDE.md should reflect your reality, not a generic template.

**Prompt 2: Review and Strengthen Your Context**

```
Review this CLAUDE.md I've drafted for my finance workspace:

[paste your CLAUDE.md here]

Identify:
1. What important accounting policies am I missing for a [your industry] company?
2. Are my governance rules appropriate, or too loose/strict?
3. What additional context would help you give better finance suggestions?
4. Any contradictions or ambiguities you notice?

Be specific about what to add or change.
```

**What you're learning**: This prompt demonstrates the Three Roles pattern from Chapter 3. Claude acts as Teacher (suggesting policies you missed), you act as Teacher (providing industry-specific constraints), and you converge together on a more complete CLAUDE.md.

**Prompt 3: Test Context Application**

```
Given my CLAUDE.md context [paste your file], help me classify this transaction:

Vendor: "CloudTech Solutions"
Amount: $15,000
Description: "Annual platform subscription - 12-month license plus implementation services"

Based on my accounting policies and governance rules:
1. How should this be categorized?
2. What accounts should be affected?
3. Does this trigger any governance reviews?
4. Should any portion be capitalized or deferred?

Walk me through your reasoning, referencing my specific policies.
```

**What you're learning**: This prompt validates that your CLAUDE.md is working. Claude should reference your specific chart of accounts, apply your capitalization threshold, and flag governance rules if triggered. If Claude gives generic advice instead of referencing your context, your CLAUDE.md may not be loading correctly—go back to the verification step.
