---
sidebar_position: 3
title: "Creating Finance Skills"
description: "Apply the Skills concept from Chapter 3 to create finance-specific reusable intelligence. Design and build practical skills for variance analysis and transaction classification that encode your finance expertise."
keywords:
  [
    "finance skills",
    "variance-analyzer",
    "transaction-classifier",
    "reusable intelligence",
    "skill anatomy",
    "finance automation",
    "Digital FTE",
  ]
chapter: 7
lesson: 3
duration_minutes: 25

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration)"
layer_1_foundation: "Skills concept from Chapter 3 Lessons 5-7"
layer_2_collaboration: "Co-creating finance-specific skills with AI, refining skill anatomy through iteration, converging on domain-appropriate safety guardrails"
layer_3_intelligence: "Creating reusable finance intelligence components"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Applying Skills to Finance Domain"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can adapt the general Skills concept to create finance-specific skills that encode domain expertise"

  - name: "Designing Skill Anatomy for Finance"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can design a complete skill with persona, logic, context, and safety components tailored to finance workflows"

  - name: "Building Variance Analysis Skills"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can create a variance-analyzer skill with audit-ready explanations and materiality thresholds"

  - name: "Building Transaction Classification Skills"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can create a transaction-classifier skill with confidence levels and reasoning chains"

learning_objectives:
  - objective: "Apply the Skills concept from Chapter 3 to create finance-specific reusable intelligence"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Explanation connecting Chapter 3 Skills framework to finance domain application"
  - objective: "Design a skill with proper anatomy: persona, logic, context, and safety guardrails"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Creation of skill specification with all four anatomy components"
  - objective: "Build practical finance skills for variance analysis and transaction classification"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Implementation of at least one working finance skill with complete SKILL.md structure"

# Cognitive load tracking
cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (applying Ch5 skills to finance, skill anatomy with 4 components, finance skill patterns, variance-analyzer design, transaction-classifier design, skill composition, skills as Digital FTE components) - within A2-B1 limit"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Create a skill composition that chains variance-analyzer into a narrative-generator for automated board reporting; design skills for multi-currency consolidation"
  remedial_for_struggling: "Focus on one skill (variance-analyzer); copy the template structure and adapt for your company's specific thresholds before attempting custom design"

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
  - "Chapter 3, Lessons 5-7: Skills concept, Building Skills, Skill Factory Pattern"
  - "Chapter 7, Lesson 2: Finance Workspace Setup with CLAUDE.md"
---

# Creating Finance Skills

Your finance expertise is valuable. You know exactly how to analyze budget variances, classify transactions, and structure management reports. This knowledge took years to develop.

What if Claude could apply your expertise consistently, every time, without you having to explain your approach from scratch?

In Chapter 3, you learned that Skills are "reusable intelligence"—folders containing SKILL.md files that encode your expertise in a format Claude can activate automatically. You learned to create skills for blog planning, meeting notes, and code review.

Now you'll apply that same pattern to finance. By the end of this lesson, you'll have two working finance skills—`variance-analyzer` and `transaction-classifier`—that encode professional-grade financial reasoning you can use in your daily work.

---

## Building on Chapter 3: Skills for Finance

In Chapter 3, Lesson 5, you learned the core insight: **the bottleneck isn't AI intelligence—it's access to specialized expertise.** Claude is brilliant, but it doesn't know your company's variance thresholds, your chart of accounts, or your classification rules.

Skills bridge that gap.

| Chapter 3 Concept                                                | Finance Application                                                |
| ---------------------------------------------------------------- | ------------------------------------------------------------------ |
| Skills are folders with SKILL.md                                 | Finance skills live in `.claude/skills/variance-analyzer/SKILL.md` |
| Three-level loading (metadata → instructions → supporting files) | Keeps context efficient when you have many finance skills          |
| skill-creator generates skills                                   | You can use skill-creator for finance skills too                   |
| Skills complement MCP (expertise + connectivity)                 | Finance skills + accounting MCP servers = powerful automation      |
| Skills compound across organizations                             | Your variance analysis approach becomes team-wide standard         |

The structure is identical. The domain content is finance-specific.

---

## The Finance Skill Anatomy

In Chapter 3, you learned that skills have YAML frontmatter (name, description) and a markdown body (procedures, examples). For finance skills, we need to think about four key components:

### The Four Components

```
┌─────────────────────────────────────────────┐
│              FINANCE SKILL ANATOMY          │
├─────────────────────────────────────────────┤
│  PERSONA                                    │
│  Who is this skill? What expertise does it  │
│  embody? (Senior FP&A Analyst, Bookkeeper)  │
├─────────────────────────────────────────────┤
│  LOGIC                                      │
│  What decision-making process does it       │
│  follow? (Step-by-step reasoning chain)     │
├─────────────────────────────────────────────┤
│  CONTEXT                                    │
│  What information does it need? (Chart of   │
│  accounts, thresholds, policies)            │
├─────────────────────────────────────────────┤
│  SAFETY                                     │
│  What guardrails prevent errors? (Human     │
│  review triggers, never auto-post)          │
└─────────────────────────────────────────────┘
```

### Why These Four Matter

**Persona** defines the expertise level and communication style. A "senior FP&A analyst" persona produces different output than a "bookkeeper" persona—different depth, different assumptions about audience.

**Logic** makes reasoning explicit. Instead of hoping Claude figures out variance analysis, you specify: identify significance → categorize direction → trace root causes → explain for audit.

**Context** connects to your reality. The skill references your CLAUDE.md (chart of accounts, materiality thresholds, fiscal year) rather than generic assumptions.

**Safety** prevents costly mistakes. Finance has higher stakes than blog planning—incorrect journal entries cause real problems. Safety guardrails define what requires human review.

---

## Building the Variance Analyzer Skill

Variance analysis is the comparison of budgeted amounts to actual results. Every finance professional does this, and every one has slightly different approaches. This skill encodes a professional approach.

### The Complete Skill

Create `.claude/skills/variance-analyzer/SKILL.md`:

```markdown
---
name: "variance-analyzer"
description: "Analyze budget vs actual variances with audit-ready explanations. Identifies significant variances, categorizes as favorable/unfavorable, traces root causes, and provides reasoning for management review. Use when user asks about budget variances, over/under spending, or period comparison."
version: "1.0.0"
---

# Variance Analyzer Skill

## Persona

You are a senior FP&A analyst with 10+ years of experience in variance analysis. You are:

- Methodical and detail-oriented
- Always explain your reasoning
- Conservative in interpretations (flag uncertainty rather than assert)
- Focused on audit-ready documentation

You think in terms of: "What story does this variance tell? What action should management take?"

## When to Use This Skill

- User asks to analyze budget vs actual
- User mentions variances, over/under budget, or spending analysis
- User provides period comparison data
- User asks "why did we miss budget?" or similar

## Logic (Decision Process)

1. **Identify Significant Variances**
   - Flag variances > 5% AND > $10,000 (both thresholds must be met)
   - For smaller budgets, flag variances > 10% regardless of dollar amount
   - Consider cumulative significance (many small variances in same direction)

2. **Categorize Each Variance**
   - Favorable (F): Revenue higher than budget, or expense lower than budget
   - Unfavorable (U): Revenue lower than budget, or expense higher than budget
   - Note: What's "favorable" depends on the line item type

3. **Trace Root Causes**
   - Volume variance: More/fewer units than planned
   - Price variance: Different rate than budgeted
   - Mix variance: Different product/service mix than expected
   - Timing variance: Recognition in different period than budgeted
   - One-time variance: Unusual event not in original budget

4. **Generate Audit-Ready Explanation**
   - State the variance amount ($ and %)
   - Identify the root cause category
   - Explain the specific driver
   - Recommend action (investigate further, update forecast, no action needed)

## Context Requirements

- References chart of accounts from CLAUDE.md for proper categorization
- Applies materiality thresholds from your company's policies
- Considers seasonality when evaluating timing variances
- Checks for known business events (acquisitions, product launches) that explain variances

## Output Format

**Variance Analysis Summary**

| Line Item | Budget | Actual | Variance $ | Variance % | F/U | Significance     |
| --------- | ------ | ------ | ---------- | ---------- | --- | ---------------- |
| [item]    | [amt]  | [amt]  | [amt]      | [%]        | F/U | ✓ if significant |

**Detailed Analysis of Significant Variances**

For each significant variance:

**[Line Item Name]** — [Variance $] ([Variance %]) [F/U]

_Root Cause_: [Category: Volume/Price/Mix/Timing/One-time]

_Explanation_: [Specific driver in 2-3 sentences]

_Recommendation_: [Action item or "No action required"]

---

**Summary**

Total favorable variances: $X
Total unfavorable variances: $Y
Net position: [Over/Under] budget by $Z

## Safety Guardrails

- Always show calculation methodology (how you derived percentages)
- Flag assumptions explicitly ("Assuming fiscal year from CLAUDE.md...")
- Recommend human review for material variances (> $50,000)
- Never present estimates as facts—use language like "likely due to" or "appears to be"
- If data seems incomplete, state what's missing rather than guessing

## Example

**Input**: "Analyze this month's marketing spend vs budget"

**Output**:
```

**Variance Analysis Summary**

| Line Item   | Budget      | Actual      | Variance $ | Variance % | F/U   | Sig |
| ----------- | ----------- | ----------- | ---------- | ---------- | ----- | --- |
| Digital Ads | $45,000     | $52,300     | $7,300     | 16.2%      | U     | ✓   |
| Events      | $20,000     | $18,500     | ($1,500)   | (7.5%)     | F     |     |
| Content     | $15,000     | $14,200     | ($800)     | (5.3%)     | F     |     |
| **Total**   | **$80,000** | **$85,000** | **$5,000** | **6.3%**   | **U** | ✓   |

**Detailed Analysis**

**Digital Ads** — $7,300 (16.2%) Unfavorable

_Root Cause_: Volume variance

_Explanation_: Campaign for Q4 product launch was accelerated from December
to November based on Sales request. Additional spend covered expanded
audience targeting for holiday season. This spend was planned for next
period but pulled forward.

_Recommendation_: Update December forecast to reduce by offsetting amount.
Verify with Sales that campaign timing change was authorized.

---

**Summary**

Total favorable variances: $2,300
Total unfavorable variances: $7,300
Net position: Over budget by $5,000

The overage is primarily timing-related (Digital Ads pulled forward).
Recommend management review of campaign timing authorization.

```

```

### What Makes This Skill Effective

**Specific thresholds**: "> 5% AND > $10,000" is actionable. "Significant variances" is not.

**Reasoning chain**: The four-step logic (identify → categorize → trace → explain) produces consistent analysis.

**Audit-ready output**: The format with root cause categories and explicit recommendations matches what controllers expect.

**Built-in safety**: The guardrails prevent common errors (asserting facts without data, missing calculations).

---

## Building the Transaction Classifier Skill

Transaction classification is the process of categorizing financial transactions to the correct accounts. This happens hundreds of times per month in any business.

### The Complete Skill

Create `.claude/skills/transaction-classifier/SKILL.md`:

```markdown
---
name: "transaction-classifier"
description: "Classify transactions with contextual reasoning and confidence levels. Analyzes vendor name and description, matches to chart of accounts, considers historical patterns, and provides reasoning for audit trail. Use when user needs to categorize transactions, code expenses, or classify payments."
version: "1.0.0"
---

# Transaction Classifier Skill

## Persona

You are an experienced bookkeeper with industry knowledge. You are:

- Careful and thorough
- Ask clarifying questions when uncertain
- Provide reasoning for every classification
- Conservative—when in doubt, flag for human review

You think in terms of: "What account correctly reflects the economic substance of this transaction?"

## When to Use This Skill

- User asks to classify, categorize, or code a transaction
- User provides transaction details (vendor, amount, description)
- User asks "what account does this go to?"
- User mentions expense coding or GL classification

## Logic (Decision Process)

1. **Analyze Transaction Information**
   - Parse vendor name (company type, industry indicators)
   - Parse description (keywords: "subscription," "service," "equipment")
   - Note amount (affects capitalization decisions per CLAUDE.md threshold)

2. **Match to Chart of Accounts**
   - Reference chart of accounts from CLAUDE.md
   - Identify most likely account based on transaction nature
   - Consider if multiple accounts apply (split transactions)

3. **Consider Historical Patterns**
   - Same vendor in previous periods → likely same classification
   - Similar description → similar treatment
   - Flag if classification would differ from precedent

4. **Determine Confidence Level**
   - **High (90%+)**: Clear match to known account, common transaction type
   - **Medium (70-89%)**: Reasonable match but some ambiguity
   - **Low (below 70%)**: Multiple valid options, unusual transaction, or insufficient information

5. **Provide Reasoning Chain**
   - State the classification
   - Explain why this account is appropriate
   - Note any alternatives considered
   - Flag if human review recommended

## Context Requirements

- References chart of accounts from CLAUDE.md
- Uses accounting policies (capitalization threshold, prepaid treatment)
- Considers cost center structure if applicable
- Notes tax implications when relevant (sales tax, use tax)

## Output Format

**Transaction Classification**

| Field                   | Value                           |
| ----------------------- | ------------------------------- |
| Vendor                  | [name]                          |
| Amount                  | [amount]                        |
| Description             | [description]                   |
| **Recommended Account** | [account number] [account name] |
| **Confidence**          | [High/Medium/Low]               |
| **Cost Center**         | [if applicable]                 |

**Reasoning**

[2-4 sentences explaining why this classification is appropriate. Reference specific signals from vendor name, description, or amount that support this classification.]

**Alternatives Considered**

- [Alternative account]: [Why rejected]
- [Alternative account]: [Why less appropriate]

**Flags**

- [ ] Requires human review (if confidence < 80% or unusual)
- [ ] Tax implications (if sales/use tax relevant)
- [ ] Capitalization decision (if near threshold)

## Safety Guardrails

- Never auto-post to ledger—classification is a recommendation only
- Flag low-confidence classifications (< 80%) for human review
- Explain reasoning for audit trail (every classification needs justification)
- Escalate ambiguous transactions to human rather than guessing
- If vendor is new, recommend vendor master verification

## Example

**Input**: "Classify: Figma Inc, $180, 'Annual subscription - design tool'"

**Output**:
```

**Transaction Classification**

| Field                   | Value                             |
| ----------------------- | --------------------------------- |
| Vendor                  | Figma Inc                         |
| Amount                  | $180                              |
| Description             | Annual subscription - design tool |
| **Recommended Account** | 6300 Software Subscriptions       |
| **Confidence**          | High (95%)                        |
| **Cost Center**         | 300 (Engineering)                 |

**Reasoning**

Figma is a well-known design software company (SaaS). The description
explicitly states "subscription" which matches our Software Subscriptions
account. Amount ($180) is below our $2,500 capitalization threshold per
CLAUDE.md, so this is expensed rather than capitalized. Assigned to
Engineering cost center as design tools typically support product
development.

**Alternatives Considered**

- 6400 Professional Services: Rejected—Figma is a software product, not
  consulting/professional service
- 1550 Prepaid Expenses: Rejected—annual amount of $180 is immaterial for
  prepaid treatment; expense in period

**Flags**

- [ ] Requires human review
- [ ] Tax implications
- [ ] Capitalization decision

```

```

### What Makes This Skill Effective

**Confidence levels**: The 90%/70-89%/below 70% bands give users clear signals about reliability.

**Reasoning chain**: Every classification includes justification—essential for audit.

**Alternatives considered**: Showing what was rejected builds trust in the recommendation.

**Clear escalation**: Low confidence triggers human review, not guessing.

---

## Skill Composition: Combining Skills for Complex Workflows

Individual skills are powerful. Combined skills are transformational.

Consider this workflow for monthly variance reporting:

```
Budget vs Actual Data
        │
        ▼
┌───────────────────┐
│ variance-analyzer │ → Identifies significant variances
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│ narrative-generator│ → Converts analysis to management prose
└────────┬──────────┘
         │
         ▼
   Board Report Draft
```

When you compose skills:

1. **Output becomes input**: variance-analyzer's structured output feeds narrative-generator
2. **Context flows through**: Both skills reference the same CLAUDE.md
3. **Safety compounds**: Each skill's guardrails add protection

You don't need to build the orchestration manually. You can prompt:

```
Using variance-analyzer, analyze this month's results. Then use
narrative-generator to create the management summary for the board deck.
```

Claude activates each skill in sequence, passing outputs forward.

---

## Skills as Digital FTE Components

Remember the Agent Factory thesis from Chapter 1? Skills you create aren't just personal productivity tools—they're components of Digital FTEs you can package and sell.

Consider these paths:

| Your Skill             | Digital FTE Application                  |
| ---------------------- | ---------------------------------------- |
| variance-analyzer      | Financial reporting automation service   |
| transaction-classifier | Bookkeeping assistance product           |
| reconciliation-matcher | Bank rec automation for accounting firms |
| budget-forecaster      | FP&A advisory tool                       |

When you create a skill like `variance-analyzer`, you're not just saving yourself time. You're encoding expertise that:

1. Can be shared with your team (everyone uses your approach)
2. Can be versioned and improved (gets better over time)
3. Can be integrated into Custom Agents (Part 6 teaches this)
4. Can be monetized as part of a vertical AI solution

The variance-analyzer skill you build today could become the core of a financial reporting product you sell to other finance teams tomorrow.

This is what "Skills are intellectual property" means in practice.

---

## Creating Your First Finance Skill

Now apply what you've learned. Create a skill for a finance workflow you perform regularly.

**Step 1: Choose Your Workflow**

What finance task do you repeat frequently?

- Monthly close checklist
- Expense report review
- Cash flow forecasting
- Invoice verification
- Audit evidence gathering

**Step 2: Define the Four Components**

For your chosen workflow, specify:

- **Persona**: What expertise level and style?
- **Logic**: What step-by-step decision process?
- **Context**: What information from CLAUDE.md is needed?
- **Safety**: What requires human review? What should never be automatic?

**Step 3: Create the SKILL.md**

Using the variance-analyzer or transaction-classifier as templates, create your skill:

```bash
mkdir -p .claude/skills/your-skill-name
# Create SKILL.md with the four components
```

**Step 4: Test and Refine**

Try the skill with real scenarios. Note what works and what needs adjustment. Skills improve through use.

---

## Try With AI

Put your finance skill knowledge into practice through these collaborative exercises.

**Prompt 1: Design a Bank Reconciliation Skill**

```
Help me design a skill for monthly bank reconciliation. I need:

1. A PERSONA for someone doing reconciliation work—what expertise and style?
2. The LOGIC steps for reconciliation: matching transactions, identifying exceptions, resolving differences
3. What CONTEXT would this skill need from my CLAUDE.md?
4. What SAFETY guardrails should prevent errors in bank reconciliation?

Give me a complete skill specification I can use, following the format from variance-analyzer.
```

**What you're learning**: This prompt applies the skill anatomy to a new finance workflow. Notice how Claude structures the four components—persona drives communication style, logic provides the decision chain, context connects to your company's reality, and safety prevents costly mistakes. Compare the output to variance-analyzer to see the pattern consistency.

**Prompt 2: Create a Cash Flow Forecasting Skill**

```
Create a skill specification for analyzing cash flow trends and predicting potential shortfalls 30-60-90 days out.

Include:
1. PERSONA: Who is doing this analysis? What's their expertise level?
2. LOGIC: What's the step-by-step process for identifying cash flow risks?
3. CONTEXT: What company information does this skill need?
4. SAFETY: What requires human review? When should the skill flag risks?

The skill should produce actionable recommendations for treasury management.
```

**What you're learning**: Cash flow forecasting requires different logic than variance analysis—it's forward-looking rather than historical. Notice how the skill anatomy adapts to different time horizons and decision types while maintaining the same structural components.

**Prompt 3: Compose Skills for Board Reporting**

```
I have a variance-analyzer skill and want to create a narrative-generator skill. Together, these should automate our monthly board report preparation.

Help me:
1. Design the narrative-generator skill that takes variance-analyzer output as input
2. Show me how the workflow would chain: variance analysis → narrative generation
3. What integration points need to match for smooth handoff?
4. What should the combined output look like for a board presentation?

Show me the skill composition in action.
```

**What you're learning**: This prompt explores how individual skills compose into workflows. The key insight is that skill outputs need to be designed for consumption by other skills—structured data rather than prose, clear field names, consistent formats. When you design skills to compose, you multiply their value.

Note: When working with finance skills that access real company data, always test with sandbox data first. Review skill outputs before taking action. The safety guardrails in these skills are suggestions for human review, not automated controls—you remain responsible for financial decisions.
