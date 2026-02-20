---
sidebar_position: 7
title: "Capstone: Tax Season Prep"
chapter: 9
lesson: 6
layer: L2
duration_minutes: 40
description: "Watch Claude Code orchestrate a complete tax preparation workflow, then understand how all Seven Principles came together"
keywords:
  [
    "capstone",
    "workflow orchestration",
    "tax preparation",
    "expense categorization",
    "spec-driven",
    "seven principles",
    "CSV processing",
  ]

skills:
  - name: "Orchestrating Multi-Step Workflows"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can direct Claude Code to execute a complete end-to-end workflow with verification"

  - name: "Principle Recognition"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Reflective Learning"
    measurable_at_this_level: "Student can identify which Seven Principles appear in a given workflow"

  - name: "Verification-First Approach"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Quality Assurance"
    measurable_at_this_level: "Student insists on test data verification before processing real data"

learning_objectives:
  - objective: "Direct Claude Code to orchestrate a complete tax prep workflow from CSVs to report"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Student successfully prompts agent to produce categorized totals with verification"

  - objective: "Identify Seven Principles in action during workflow execution"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student correctly maps at least 5 principles to specific workflow steps"

  - objective: "Apply verification-first pattern to ensure accuracy before processing real data"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student requests test data verification before running on actual bank statements"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (workflow orchestration, principle mapping, verification-first) - reduced load for synthesis"

differentiation:
  extension_for_advanced: "Add date filtering, multiple currencies, generate CSV output for accountant"
  remedial_for_struggling: "Follow the conversation pattern exactly. The workflow is already structured."

teaching_guide:
  lesson_type: "capstone"
  session_group: 3
  session_title: "Data Wrangling and Capstone"
  key_points:
    - "The verification-first orchestration pattern (test data → verify → real data) is the capstone's central contribution — it combines every lesson into one disciplined workflow"
    - "All Seven Principles appeared naturally in a single workflow — the mapping table makes this explicit and shows students how principles reinforce each other"
    - "The 'NEEDS REVIEW' section demonstrates that good automation flags ambiguity for human judgment rather than making silent decisions"
    - "The CSV merging technique (head -1 for header + tail -n +2 -q for data rows) is a practical Unix pattern students will reuse whenever combining structured files"
  misconceptions:
    - "Students think the capstone requires new skills — it actually requires orchestrating Lessons 1-5 in sequence, which is a different and harder challenge than learning each individually"
    - "Students may skip the verification step because they trust the categorizer from Lesson 5 — the capstone insists on verification with test data even for tools that worked before, because data changes"
    - "Students assume 'accountant-ready report' means perfect categorization — the NEEDS REVIEW section shows that flagging ambiguity is more professional than guessing"
  discussion_prompts:
    - "Why does the capstone insist on verification EVEN for the categorizer you already tested in Lesson 5? What could be different about the real data?"
    - "The report includes a NEEDS REVIEW section with 23 items. Is that a failure of the categorizer or a feature? Why?"
    - "Look at the before/after comparison table. Which capability do you think has the most impact outside of tax preparation?"
  teaching_tips:
    - "Let students attempt the capstone independently for 15-20 minutes before showing the reference implementation — struggling builds deeper understanding than following instructions"
    - "The Seven Principles mapping table is the chapter's culmination — walk through it and ask students to point to the specific moment in the workflow where each principle appeared"
    - "The reflection table (what it looked like vs what you actually learned) is a powerful closing tool — have students add their own row for what THEY learned that is not in the table"
    - "End by asking students to name one domain outside tax prep where the verification-first orchestration pattern would apply — this ensures transfer learning"
  assessment_quick_check:
    - "Ask students to describe the five steps of the capstone workflow from memory: test data, build categorizer, verify, process real files, flag ambiguous"
    - "Ask: 'Why does the workflow insist on verification BEFORE processing real files?' — tests understanding of verification-first as a principle, not just a step"
    - "Have students map at least 5 of the 7 principles to specific capstone steps from memory"
---

# Capstone: Tax Season Prep

Open Claude Code. Set a timer for 40 minutes. Your goal:

> **Point Claude Code at a folder of bank statement CSVs and produce a categorized tax report with verified totals.**

You have everything you need. You know how to build scripts that handle decimals (Lesson 1), verify them against known answers (Lesson 2), parse real CSV data (Lesson 3), make tools permanent (Lesson 4), and categorize with false-positive guards (Lesson 5). Now orchestrate all of it into one workflow.

:::tip Use Your Own Data
If you downloaded your bank statement CSV in Lesson 3, use that here. Create a folder `~/finances/2025/` and put your CSV files in it. Otherwise, ask Claude Code to generate test data. Real data makes this capstone real.
:::

## Your Mission

Build a workflow that:

1. Creates test data with known answers (you calculate expected totals by hand)
2. Builds a categorizer that handles Medical, Charitable, and Business expenses
3. Verifies totals match your hand calculations before touching real data
4. Processes all monthly CSVs into a single report
5. Flags ambiguous transactions for human review

**Start now.** Come back when you have a report — or when you're stuck.

Hint: Your opening prompt should tell Claude Code the full scope AND insist on verification first. Something like:

```
I have bank statement CSVs in ~/finances/2025/.
Help me categorize transactions (Medical, Charitable, Business),
calculate subtotals, and flag ambiguous items.

IMPORTANT: Verify with test data before processing real files.
```

---

<details>
<summary><strong>Reference Implementation</strong> — Done or stuck? Click to compare your approach.</summary>

## Reference Implementation

```
You: I have a folder ~/finances/2025/ with monthly bank statement CSVs
(january.csv through december.csv). Each has Date, Description, Amount.

Help me:
1. Categorize transactions: Medical, Charitable, Business
2. Calculate subtotals for each category
3. Flag anything ambiguous for human review
4. Generate a report for my accountant

IMPORTANT: First verify your approach with test data before touching real files.
I want to see it work on known data where I can check the math.
```

Watch what Claude Code does:

```
Claude Code: Smart approach - verify first with known data. Let me set up
a complete workflow.

STEP 1: CREATE TEST DATA WITH KNOWN ANSWERS
==========================================

[Creates: ~/finances/2025/test_january.csv]

Date,Description,Amount
01/05/2025,CVS PHARMACY #1234,-45.67
01/06/2025,DR MARTINEZ MEDICAL,-150.00
01/07/2025,WALGREENS #5678,-32.50
01/10/2025,AMERICAN RED CROSS,-100.00
01/15/2025,OFFICE DEPOT #901,-89.99
01/18/2025,STAPLES #123,-45.00
01/20/2025,DOCTORS WITHOUT BORDERS,-50.00
01/22/2025,DR PEPPER BOTTLING,-4.99
01/25/2025,CVSMITH CONSULTING,-200.00

Expected totals (calculated by hand):
- Medical: $228.17 (CVS + DR MARTINEZ + WALGREENS)
- Charitable: $150.00 (RED CROSS + DOCTORS WITHOUT BORDERS)
- Business: $134.99 (OFFICE DEPOT + STAPLES)
- NOT categorized: DR PEPPER ($4.99), CVSMITH ($200.00)

STEP 2: BUILD THE CATEGORIZER
=============================

[Creates: tax-prep.py with categories, false positive guards, and report generation]

STEP 3: VERIFY AGAINST TEST DATA
================================

[Runs: cat ~/finances/2025/test_january.csv | python tax-prep.py]

==================================================
2025 TAX CATEGORIZATION REPORT
==================================================

MEDICAL (Schedule A):
  CVS PHARMACY #1234 (1 txns)      $45.67
  DR MARTINEZ MEDICAL (1 txns)     $150.00
  WALGREENS #5678 (1 txns)         $32.50
  SUBTOTAL:                        $228.17

CHARITABLE (Schedule A):
  AMERICAN RED CROSS (1 txns)      $100.00
  DOCTORS WITHOUT BORDERS (1 txns) $50.00
  SUBTOTAL:                        $150.00

BUSINESS (if applicable):
  OFFICE DEPOT #901 (1 txns)       $89.99
  STAPLES #123 (1 txns)            $45.00
  SUBTOTAL:                        $134.99

==================================================
POTENTIAL DEDUCTIONS: $513.16
==================================================

NEEDS REVIEW:
  - "DR PEPPER BOTTLING" $4.99 - verify category
  - "CVSMITH CONSULTING" $200.00 - verify category

VERIFICATION:
✓ Medical: $228.17 (matches expected)
✓ Charitable: $150.00 (matches expected)
✓ Business: $134.99 (matches expected)
✓ DR PEPPER correctly flagged for review
✓ CVSMITH correctly flagged for review

All totals match hand-calculated values. Ready to process real files?
```

You verify the totals match your expectations. Then:

```
You: Verified. Now process all the real monthly files.
```

```
Claude Code: Processing all monthly CSVs...

STEP 4: COMBINE MONTHLY FILES
=============================

[Runs: head -1 ~/finances/2025/january.csv > all-2025.csv]
[Runs: tail -n +2 -q ~/finances/2025/*.csv >> all-2025.csv]

Combined 12 files, 1,247 transactions total.

STEP 5: GENERATE FINAL REPORT
=============================

[Runs: cat all-2025.csv | python tax-prep.py > tax-report-2025.txt]

==================================================
2025 TAX CATEGORIZATION REPORT
==================================================

MEDICAL (Schedule A):
  CVS PHARMACY (23 txns)           $456.70
  WALGREENS (15 txns)              $234.50
  Medical offices (8 txns)         $1,200.00
  SUBTOTAL:                        $1,891.20

CHARITABLE (Schedule A):
  RED CROSS (4 txns)               $400.00
  UNITED WAY (6 txns)              $600.00
  Other donations (8 txns)         $550.00
  SUBTOTAL:                        $1,550.00

BUSINESS (if applicable):
  Office supplies (18 txns)        $539.76
  Software subscriptions (9 txns)  $234.56
  SUBTOTAL:                        $774.32

==================================================
POTENTIAL DEDUCTIONS: $4,215.52
==================================================

NEEDS REVIEW (23 items):
  - "SQ *LOCALSTORE" $200.00 - verify category
  - "AMZN MKTP US" $89.00 - personal or business?
  [...]

Report saved to: tax-report-2025.txt

Would you like me to create a reusable script for next year?
```

In one conversation, a year of bank statements became an accountant-ready report.

</details>

## What Just Happened?

Let's trace how ALL Seven Principles appeared in that workflow.

| Principle                               | How It Appeared                                                  |
| --------------------------------------- | ---------------------------------------------------------------- |
| **P1: Bash is the Key**                 | `cat`, `head`, `tail`, pipes orchestrated all data flow          |
| **P2: Code as Universal Interface**     | Python script executed categorization - no hallucinated math     |
| **P3: Verification as Core Step**       | Test data with known totals BEFORE processing real files         |
| **P4: Small, Reversible Decomposition** | 5 clear steps, each testable independently                       |
| **P5: Persisting State in Files**       | Script saved to tax-prep.py, report saved to tax-report-2025.txt |
| **P6: Constraints and Safety**          | False positive guards prevented DR PEPPER → medical              |
| **P7: Observability**                   | "NEEDS REVIEW" section made ambiguous items visible              |

All seven principles appeared in a single workflow. This isn't coincidence. The principles are how agents work effectively with computing systems.

## The Agent's Toolkit: CSV Merging

The agent combined 12 CSVs without duplicating headers. Here's the technique:

```bash
# Get header from first file only
head -1 january.csv > combined.csv

# Append data (skip headers) from ALL files
tail -n +2 -q *.csv >> combined.csv
```

| Command      | What It Does                                |
| ------------ | ------------------------------------------- |
| `head -1`    | First line only (the header)                |
| `tail -n +2` | Everything from line 2 onward (skip header) |
| `-q`         | Quiet mode - no filename prefixes           |
| `>>`         | Append (don't overwrite)                    |

Result: One file with a single header row followed by all data rows.

## The Pattern: Verification-First Orchestration

Here's the capstone prompt pattern:

```
"Help me [complex multi-step goal].

IMPORTANT: First verify your approach with test data before touching
real files. I want to see it work on known data where I can check the math."
```

This pattern ensures:

1. **Test data is created first** - Known inputs with calculable outputs
2. **Logic is verified** - You check totals match before processing real data
3. **Real processing happens only after verification** - Trust is earned

The phrase "verify your approach with test data" triggers the agent to build a verification workflow, not just execute blindly.

### Pattern for Reusable Workflows

```
"Would you like me to create a reusable script for next year?"
```

When the agent offers this, say yes. The result is a script you can run annually:

```bash
./tax-prep.sh ~/finances/2026/
```

Same workflow, different year. No re-prompting needed.

## Try It Yourself

Direct Claude Code through the full workflow:

```
I have expense CSVs in ~/expenses/. Help me:
1. Categorize by type (supplies, travel, meals)
2. Generate monthly and yearly summaries
3. Flag transactions over $500 for receipt verification

Verify with test data first.
```

Watch how the agent:

1. Creates test data with known amounts
2. Builds categorization logic
3. Verifies totals match
4. Then processes real files

This is the verification-first pattern in action.

## The Victory

Step back and recognize what you accomplished in this chapter.

**Before Chapter 9:**

- Bash couldn't add decimals
- LLMs hallucinated calculations
- Manual spreadsheet work for expense categorization
- No systematic verification

**After Chapter 9:**

- Python scripts handle any calculation
- Verified against known test data
- Automated categorization with false-positive guards
- Reusable tools in your personal toolbox

You built your first Digital FTE component - a tool that does tedious work accurately, every time, without missing edge cases or hallucinating categories.

The same pattern applies to:

- Invoice processing
- Subscription tracking
- Budget analysis
- Any scenario where data needs categorization

You have the foundation.

## Reflection: What You're Actually Learning

This chapter taught you patterns, not just commands.

| What It Looked Like       | What You Actually Learned                       |
| ------------------------- | ----------------------------------------------- |
| Building sum.py           | How to direct agents to create reusable tools   |
| Testing with known data   | The verification-first pattern                  |
| CSV parsing with Python   | When to use specialized tools vs. simple ones   |
| Regex patterns            | How to specify precise matching with guardrails |
| Processing multiple files | How to orchestrate complex workflows            |

The specific tools (Python, regex, find/xargs) matter less than the patterns:

- Describe the problem, not the solution
- Verify before trusting
- Mention edge cases to get robust solutions
- Make tools permanent and reusable

These patterns transfer to any domain where you work with General Agents.

---

## Try With AI

### Prompt 1: Extend the Workflow

```
My tax-prep workflow works well. Now I want to add:
1. Filter by date range (only Q4 transactions: Oct-Dec)
2. Generate CSV output (for importing to Excel)
3. Email-ready summary (plain text I can paste)

Keep the verification-first approach.
```

**What you're learning:** Incremental extension. You have a working workflow and add features. The agent preserves the verification pattern while adding functionality.

### Prompt 2: Apply to Different Domain

```
I learned the tax-prep workflow pattern. Now apply it to a different
problem: I have server logs with timestamps and response codes.
Help me categorize by error type and generate a weekly report.

Same approach: verify with test data first, then process real logs.
```

**What you're learning:** Pattern transfer. The same workflow structure (test data → verify → process real) applies to completely different domains. You're learning to recognize when to apply patterns, not just execute them.

### Prompt 3: Build the Reusable Script

```
Convert my tax-prep workflow into a single bash script I can run
next year. It should:
1. Take a folder path as argument
2. Combine all CSVs in that folder
3. Run tax-prep.py and save the report
4. Print a summary to the terminal

Include comments explaining each step.
```

**What you're learning:** Packaging workflows. A conversation becomes a script. A script becomes a tool. A tool becomes part of your permanent toolkit. You're manufacturing Digital FTE components.
