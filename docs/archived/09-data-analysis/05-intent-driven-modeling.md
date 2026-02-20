---
title: "Intent-Driven Financial Modeling"
sidebar_position: 5
chapter: 7
lesson: 5
duration_minutes: 25

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration)"
layer_1_foundation: "Core financial modeling concepts (revenue, expenses, assumptions)"
layer_2_collaboration: "Co-creating financial models through natural language intent, iterative refinement with Claude acting as reasoning partner"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Intent-to-Model Translation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can express financial objectives in natural language and have Claude translate them into structured financial model specifications with explicit assumptions"

  - name: "Revenue Modeling with AI Assistance"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can collaborate with Claude to create revenue projections incorporating growth rates, seasonality, and customer segment analysis"

  - name: "Expense Forecasting Patterns"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can work with Claude to build expense models distinguishing fixed, variable, and step costs with appropriate triggers"

  - name: "Assumption Documentation for Audit Trails"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can generate explicit, traceable, and testable assumption documentation that supports financial model governance"

learning_objectives:
  - objective: "Translate business intent into financial model specifications using natural language prompts"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Demonstration of Claude translating conversational financial objectives into structured model specifications"
  - objective: "Generate revenue forecasts and expense models from conversational descriptions"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Creation of working financial models built through iterative natural language collaboration"
  - objective: "Document model assumptions in audit-ready format with explicit traceability"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Production of assumption documentation that lists each assumption, its source, validation method, and sensitivity impact"

# Cognitive load tracking
cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (intent-to-model translation, revenue modeling patterns, expense forecasting types, assumption documentation, model refactoring, sensitivity analysis basics, stakeholder narrative generation) - within B1 limit of 10"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Build multi-scenario models with Monte Carlo sensitivity analysis, create automated assumption validation workflows, generate board-ready narrative reports"
  remedial_for_struggling: "Focus on single revenue stream with linear growth, skip step costs, use simplified assumption templates"

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
  - "Chapter 7, Lesson 4: Connecting to Google Sheets via MCP"
  - "Chapter 7, Lesson 2: Finance Workspace Setup with CLAUDE.md"
---

# Intent-Driven Financial Modeling

What if you could describe what you want and Claude builds the model?

Traditional financial planning tools require you to know formulas, understand cell references, and translate your business thinking into spreadsheet mechanics. You think "conservative revenue scenario where we lose our largest customer," but you have to manually calculate the revenue impact, build the monthly projections, create the recovery assumptions, and wire everything together.

The technical barrier separates business insight from financial modeling capability.

Claude Code changes this equation. Instead of translating your thoughts into spreadsheet mechanics yourself, you express your financial objectives in natural language. Claude translates those intents into structured financial logic—assumptions documented, formulas generated, results calculated.

As the Agentic Financial Planning framework describes: "Users can express objectives in natural language: 'Model a conservative revenue scenario', 'Stress test margins under cost inflation', 'Explain the impact of churn on cash flow.' Claude translates these intents into structured financial logic."

This dramatically reduces the technical barrier to high-quality modeling. The expertise remains yours—the business judgment, the strategic context, the approval decisions. But the translation from intent to implementation becomes a conversation.

---

## From Intent to Model: The Core Pattern

Let's see what intent-driven modeling looks like in practice.

### The Scenario

Your CFO asks: "What happens to our cash position if we lose our largest customer in Q2, then recover half that revenue through new business by year-end?"

In traditional spreadsheet work, you would:
1. Calculate that your largest customer represents 20% of revenue
2. Determine when exactly the loss occurs
3. Build monthly projections showing the gap
4. Estimate recovery timeline and amounts
5. Update cash flow to reflect changed revenue
6. Create a summary explaining the scenario

With intent-driven modeling, you describe the scenario to Claude, and Claude reasons through each step—with you validating the logic at each point.

### The Conversation

**Your request:**

```
Model a conservative revenue scenario where we lose our largest customer
(20% of revenue) in Q2, then recover 50% of that lost revenue through
new business by Q4. Our current monthly revenue is $500,000.
```

**Claude's reasoning:**

```
Let me work through this scenario step by step.

Current State:
- Monthly revenue: $500,000
- Largest customer: $100,000/month (20% of $500K)

Scenario Timeline:
- Q1 (Jan-Mar): Full revenue of $500,000/month continues
- Q2 (Apr-Jun): Customer loss hits. Revenue drops to $400,000/month
- Q3 (Jul-Sep): New business development underway
- Q4 (Oct-Dec): Recovery of $50,000/month (50% of lost $100K)

Assumptions I'm Making:
1. Customer loss happens at start of Q2 (April 1)
2. Loss is immediate and complete (not gradual)
3. Recovery is linear through Q4 (phased in $16,667/month Oct, Nov, Dec)
4. No other revenue changes during this period

Should I adjust any of these assumptions before building the model?
```

Notice what happened. Claude didn't just produce numbers—it made its reasoning explicit. Each assumption is visible. You can challenge any of them.

**Your refinement:**

```
Good structure, but the recovery should be more realistic. New customers
don't appear instantly. Assume we close one new customer in October at
$20,000/month, another in November at $15,000, and a third in December
at $15,000. That gets us to $50,000 total new monthly revenue by December.
```

**Claude adapts:**

```
Updated recovery pattern—staggered new customer acquisition:

Monthly Revenue Projection:
| Month    | Base Revenue | Customer Loss | New Business | Total Revenue |
|----------|-------------|---------------|--------------|---------------|
| January  | $500,000    | $0            | $0           | $500,000      |
| February | $500,000    | $0            | $0           | $500,000      |
| March    | $500,000    | $0            | $0           | $500,000      |
| April    | $500,000    | -$100,000     | $0           | $400,000      |
| May      | $500,000    | -$100,000     | $0           | $400,000      |
| June     | $500,000    | -$100,000     | $0           | $400,000      |
| July     | $500,000    | -$100,000     | $0           | $400,000      |
| August   | $500,000    | -$100,000     | $0           | $400,000      |
| September| $500,000    | -$100,000     | $0           | $400,000      |
| October  | $500,000    | -$100,000     | +$20,000     | $420,000      |
| November | $500,000    | -$100,000     | +$35,000     | $435,000      |
| December | $500,000    | -$100,000     | +$50,000     | $450,000      |

Key Metrics:
- Total revenue impact: -$700,000 for the year
- Lowest point: $400,000/month (April-September)
- Recovery to: $450,000/month by December (90% of original)
- Cumulative new business by year-end: $105,000

Updated Assumptions:
1. Customer loss: April 1, immediate and complete
2. New Customer A: October close, $20,000/month
3. New Customer B: November close, $15,000/month
4. New Customer C: December close, $15,000/month
5. New business is incremental (doesn't replace other customers)

Ready to create this in your Google Sheets?
```

The conversation converged on a model neither of you had at the start. You provided the business reality (staggered customer acquisition). Claude structured it into quantified projections. Together, you built something better than either alone.

---

## Revenue Modeling Patterns

Intent-driven modeling works across common revenue scenarios. Here are patterns you'll use frequently.

### Pattern 1: Growth Rate Projection

**Your intent:**

```
Project revenue for 12 months starting at $100K, growing 10% month-over-month
for the first 6 months, then stabilizing at that level.
```

**Claude builds:**

```
Two-phase growth model:

Phase 1 (Months 1-6): 10% MoM compound growth
- Month 1: $100,000
- Month 2: $110,000 (×1.10)
- Month 3: $121,000
- Month 4: $133,100
- Month 5: $146,410
- Month 6: $161,051

Phase 2 (Months 7-12): Stabilized at Month 6 level
- Months 7-12: $161,051 each

Formula structure:
- Months 1-6: =B1*(1.10)^(ROW()-1)
- Months 7-12: =$B$6 (locked reference to Month 6 value)

Total annual revenue: $1,627,561
```

### Pattern 2: Seasonal Revenue

**Your intent:**

```
We're a retail business. Revenue peaks in November-December at 2x normal,
drops to 0.7x in January-February. Model this with $200K as our baseline.
```

**Claude builds:**

```
Seasonal adjustment model:

| Month     | Seasonality | Calculation         | Revenue   |
|-----------|-------------|---------------------|-----------|
| January   | 0.7x        | $200,000 × 0.7      | $140,000  |
| February  | 0.7x        | $200,000 × 0.7      | $140,000  |
| March     | 1.0x        | $200,000 × 1.0      | $200,000  |
| April     | 1.0x        | $200,000 × 1.0      | $200,000  |
| May       | 1.0x        | $200,000 × 1.0      | $200,000  |
| June      | 1.0x        | $200,000 × 1.0      | $200,000  |
| July      | 1.0x        | $200,000 × 1.0      | $200,000  |
| August    | 1.0x        | $200,000 × 1.0      | $200,000  |
| September | 1.0x        | $200,000 × 1.0      | $200,000  |
| October   | 1.2x        | $200,000 × 1.2      | $240,000  |
| November  | 2.0x        | $200,000 × 2.0      | $400,000  |
| December  | 2.0x        | $200,000 × 2.0      | $400,000  |

Annual total: $2,720,000
Average monthly: $226,667

Formula structure:
- Column B: Seasonality factor per month
- Column C: =Baseline*B2 (baseline in named cell)
```

### Pattern 3: Customer Segment Analysis

**Your intent:**

```
Break down revenue by customer tier. Enterprise customers ($50K+/year) are
30% of customers but 70% of revenue. SMB customers are 70% of count but
30% of revenue. Model total revenue of $1M annually.
```

**Claude builds:**

```
Segment concentration analysis:

| Segment    | % of Revenue | Annual Revenue | % of Customers | ARPU        |
|------------|--------------|----------------|----------------|-------------|
| Enterprise | 70%          | $700,000       | 30%            | $23,333/cust|
| SMB        | 30%          | $300,000       | 70%            | $4,286/cust |
| Total      | 100%         | $1,000,000     | 100%           | $10,000/cust|

If total customers = 100:
- Enterprise: 30 customers × $23,333 = $700,000
- SMB: 70 customers × $4,286 = $300,000

Risk insight: Losing one Enterprise customer = losing ~$23,333
             Losing one SMB customer = losing ~$4,286
             Enterprise concentration risk: 5.4x higher per customer
```

---

## Expense Forecasting Approaches

Revenue is only half the picture. Intent-driven modeling handles expense complexity too.

### Fixed Costs

**Your intent:**

```
Our office rent is $15,000/month. It increases 3% annually in July
when our lease renews.
```

**Claude builds:**

```
Fixed cost with annual escalation:

| Period        | Monthly Rent | Notes                    |
|---------------|--------------|--------------------------|
| Jan-Jun Y1    | $15,000      | Current rate             |
| Jul-Dec Y1    | $15,450      | +3% at lease renewal     |
| Jan-Jun Y2    | $15,450      | Same rate continues      |
| Jul-Dec Y2    | $15,914      | +3% at next renewal      |

Formula: =IF(MONTH(A2)>=7, BaseRent*(1.03)^(YEAR(A2)-StartYear),
             BaseRent*(1.03)^(YEAR(A2)-StartYear-1))
```

### Variable Costs

**Your intent:**

```
Our COGS is 35% of revenue. Marketing spend scales at 15% of revenue
but has a minimum of $20,000/month regardless of sales.
```

**Claude builds:**

```
Variable cost model:

Revenue assumption: See revenue projection
COGS: 35% of revenue (purely variable)
Marketing: MAX(15% of revenue, $20,000) (variable with floor)

| Month | Revenue   | COGS (35%) | Marketing           | Total Var |
|-------|-----------|------------|---------------------|-----------|
| Jan   | $100,000  | $35,000    | MAX($15K, $20K)=$20K| $55,000   |
| Feb   | $110,000  | $38,500    | MAX($16.5K,$20K)=$20K| $58,500  |
| ...   | ...       | ...        | ...                 | ...       |
| Jun   | $161,051  | $56,368    | MAX($24.2K,$20K)=$24,158| $80,526|

Marketing crosses the $20K floor when revenue exceeds $133,333.
```

### Step Costs

**Your intent:**

```
We hire engineers in batches. Currently 5 engineers at $12,000/month each.
We add 2 more when revenue hits $300K, and 3 more at $500K.
```

**Claude builds:**

```
Step cost model:

Trigger structure:
- Base: 5 engineers at $12,000/month = $60,000/month
- Trigger 1: At $300K revenue, add 2 engineers → $84,000/month
- Trigger 2: At $500K revenue, add 3 engineers → $120,000/month

| Revenue Range      | Engineer Count | Monthly Cost |
|--------------------|----------------|--------------|
| $0 - $299,999      | 5              | $60,000      |
| $300,000 - $499,999| 7              | $84,000      |
| $500,000+          | 10             | $120,000     |

Formula:
=IF(Revenue>=500000, 120000, IF(Revenue>=300000, 84000, 60000))

Critical insight: These are step increases, not gradual. Engineering cost
jumps 40% at the $300K threshold and another 43% at $500K. Budget planning
should anticipate these steps, not smooth them.
```

---

## Assumption Documentation

Every financial model rests on assumptions. Intent-driven modeling makes those assumptions explicit and traceable.

### The Assumption Registry Pattern

When Claude builds a model, ask it to generate an assumption registry:

**Your request:**

```
Create an assumption registry for the conservative revenue scenario model.
List each assumption, its source, how we would validate it, and what
happens if it's wrong by 20%.
```

**Claude generates:**

```
## Assumption Registry: Conservative Revenue Scenario

### Revenue Assumptions

| ID | Assumption | Value | Source | Validation Method | Sensitivity (±20%) |
|----|------------|-------|--------|-------------------|-------------------|
| R1 | Current monthly revenue | $500,000 | FY24 Q4 actuals | Compare to AR aging | ±$100K/month impact |
| R2 | Largest customer concentration | 20% of revenue | Customer analysis | AR by customer report | ±4% of revenue |
| R3 | Customer loss timing | April 1 | Contract review | Sales team confirmation | ±1 month shift |
| R4 | Loss is complete, not partial | 100% | Assumed worst case | Customer discussion | Upside if partial |

### Recovery Assumptions

| ID | Assumption | Value | Source | Validation Method | Sensitivity (±20%) |
|----|------------|-------|--------|-------------------|-------------------|
| V1 | New Customer A timing | October close | Pipeline review | Sales forecast | ±1 month delay risk |
| V2 | New Customer A value | $20,000/month | Proposal terms | Contract negotiation | ±$4,000/month |
| V3 | New Customer B timing | November close | Pipeline review | Sales forecast | ±1 month delay risk |
| V4 | New Customer B value | $15,000/month | Proposal terms | Contract negotiation | ±$3,000/month |
| V5 | New Customer C timing | December close | Pipeline review | Sales forecast | ±1 month delay risk |
| V6 | New Customer C value | $15,000/month | Proposal terms | Contract negotiation | ±$3,000/month |

### Implicit Assumptions (Made But Not Stated)

| ID | Assumption | Why It Matters | Validation Needed |
|----|------------|----------------|-------------------|
| I1 | No other customer churn | Model only shows largest customer impact | Review full customer risk |
| I2 | Collections timing unchanged | Cash flow assumes normal payment terms | Check if new customers have different terms |
| I3 | Pricing remains constant | No discounting to acquire new customers | Confirm deal terms maintain margins |

### Risk Summary

- **Total identified assumptions**: 13
- **High sensitivity (>10% model impact)**: R1, R2, V2
- **Validation required before presenting**: R3, V1-V6 (timing and values)
- **Board should know about**: I1-I3 (implicit assumptions)
```

This documentation transforms a spreadsheet model into an auditable financial analysis. Every number traces back to a source. Every judgment can be challenged.

---

## Model Refactoring with AI Assistance

Sometimes you inherit models others built—or models you built months ago and no longer remember. Intent-driven modeling helps untangle them.

**Your request:**

```
Review this revenue model and list every assumption, both explicit and
implicit. For each assumption, tell me what data I would need to validate
it and what happens if it's wrong.
```

Claude reads the model structure (via MCP from Lesson 4), traces the formula dependencies, and surfaces the embedded assumptions:

**Claude's analysis:**

```
Model Review: Revenue Forecast FY25

## Explicit Assumptions Found

| Location | Formula | Assumption | Risk if Wrong |
|----------|---------|------------|---------------|
| B2 | =B1*1.15 | 15% MoM growth | Each 1% variance compounds monthly |
| D2 | =C2*0.35 | 35% COGS ratio | Margin sensitivity to COGS changes |
| E2 | =MAX(C2*0.15, 20000) | Marketing floor of $20K | Below $133K revenue, marketing exceeds 15% |

## Implicit Assumptions (Not Stated)

1. **Growth is compound, not linear**: Formula =B1*1.15 creates exponential growth.
   - Month 12 value: $417,725 (not $250,000 that linear 15% would suggest)
   - Validation: Is your market really growing exponentially?

2. **No seasonality**: Every month uses same growth rate.
   - Risk: If Q4 is historically stronger, model understates Q4.
   - Validation: Compare to historical monthly patterns.

3. **No customer concentration**: Revenue modeled as aggregate, not by segment.
   - Risk: Losing a key customer isn't reflected until it happens.
   - Validation: Add customer segment breakdown.

4. **No capacity constraints**: Model assumes you can service unlimited growth.
   - Risk: At some point, growth requires hiring, which takes time.
   - Validation: What revenue level triggers capacity additions?

## Recommendations

1. Add seasonality factors (even if 1.0 for most months, making it explicit)
2. Break revenue into segments to model concentration risk
3. Add step-cost triggers for capacity planning
4. Document data sources for the 15% growth assumption

Want me to refactor the model to address these gaps?
```

---

## Sensitivity Analysis Introduction

Financial models are only as good as their assumptions. Sensitivity analysis shows how results change when assumptions change.

**Your request:**

```
For the conservative revenue scenario, show me what happens to annual
revenue if the customer loss timing shifts earlier or later by one month.
```

**Claude calculates:**

```
Sensitivity Analysis: Customer Loss Timing

Base case: Customer loss in April (Q2 start)

| Scenario | Loss Month | Revenue Impact | Difference from Base |
|----------|------------|----------------|----------------------|
| Earlier  | March      | -$800,000      | -$100,000 worse     |
| Base     | April      | -$700,000      | —                   |
| Later    | May        | -$600,000      | +$100,000 better    |

Key insight: Each month of timing shift = $100,000 annual impact.

If there's uncertainty about when the customer might leave, the range
of outcomes spans $200,000. This quantifies the value of accelerating
customer discussions to gain timing clarity.
```

This is how intent-driven modeling supports business decisions. Not just "here are the numbers," but "here's what the numbers mean and what you should do about them."

---

## Narrative Generation for Stakeholders

Numbers need stories. Intent-driven modeling generates both.

**Your request:**

```
Generate an executive summary of the conservative revenue scenario for
our board presentation. Focus on impact, risk, and mitigation.
```

**Claude generates:**

```
## Executive Summary: Customer Concentration Risk Scenario

### Situation
Our largest customer represents 20% of revenue ($100K monthly, $1.2M annually).
We've identified risk of losing this customer in Q2 based on [context].

### Impact Analysis
- **Immediate impact**: Revenue drops from $500K to $400K monthly in April
- **Sustained impact**: Six months at reduced revenue (April-September)
- **Annual revenue reduction**: $700K (11.7% of projected annual revenue)
- **Cash flow impact**: [Requires cash model integration]

### Recovery Plan
New business pipeline positions us to recover 50% of lost revenue by December:
- October: New Customer A ($20K/month)
- November: New Customer B ($15K/month)
- December: New Customer C ($15K/month)

By Q1 next year, monthly revenue reaches $450K (90% of original).

### Key Risks
1. **Timing risk**: If customer loss occurs earlier (March), impact increases $100K
2. **Pipeline risk**: New customers are projected, not committed
3. **Concentration risk**: Model does not address underlying concentration problem

### Recommended Actions
1. Accelerate customer discussions to gain timing certainty
2. Convert pipeline opportunities to signed contracts before Q2
3. Develop customer diversification strategy to reduce future concentration

### Assumptions (for audit trail)
[Link to full assumption registry]
```

The narrative connects numbers to decisions. Board members don't need to interpret spreadsheets—they receive a story that makes the model actionable.

---

## Try With AI

Put intent-driven modeling into practice with these collaborative exercises.

**Prompt 1: Revenue Scenario Model**

```
We're launching a new product line. Revenue will start at $10,000 in month 1,
grow 20% monthly for 6 months, then stabilize at that level. Create a 12-month
revenue model with all assumptions documented.

Show me:
1. Monthly revenue projections
2. The formula structure you'll use
3. An assumption registry for the model
4. What happens if growth is 15% instead of 20%
```

**What you're learning**: This prompt exercises the complete intent-to-model workflow. Notice how Claude structures the two-phase model (growth then stability), documents assumptions explicitly, and provides sensitivity analysis. Pay attention to whether Claude makes the growth phase length configurable or hardcodes it—good model design keeps key parameters adjustable.

**Prompt 2: Expense Model Refactoring**

```
Refactor my existing expense model to handle step costs. Currently it assumes
linear growth, but we hire in batches of 5 when revenue hits certain thresholds:
$500K, $1M, and $2M. Each batch costs $75,000/month (5 people at $15K each).

Show me:
1. The step function formula structure
2. How the expense line changes at each threshold
3. What this means for our margin at different revenue levels
```

**What you're learning**: This prompt demonstrates model refactoring—taking an existing linear model and adding complexity. The step cost pattern is common in finance but tricky to implement correctly. Notice how Claude structures the IF logic and whether it addresses the margin compression that happens when you cross a hiring threshold (costs jump immediately, but revenue growth is gradual).

**Prompt 3: Assumption Audit**

```
Review this revenue model and list every assumption, both explicit and implicit.
For each assumption, tell me what data I would need to validate it and what
happens if it's wrong by 20%.

[Paste your model structure or describe it]

Focus on:
1. Growth rate assumptions
2. Timing assumptions
3. Customer concentration assumptions
4. Anything the model assumes but doesn't state
```

**What you're learning**: This prompt practices assumption surfacing—the skill of finding hidden judgments in financial models. Claude will identify both explicit assumptions (the 15% in your formula) and implicit ones (no seasonality, no capacity constraints). This is where you teach Claude about your business context by confirming which implicit assumptions are valid and which need to be made explicit.

Note: When building financial models with Claude, always validate the formula logic before relying on results for decisions. Test with simple numbers where you can verify the math manually. Build trust in the modeling workflow incrementally, starting with non-critical analyses.
