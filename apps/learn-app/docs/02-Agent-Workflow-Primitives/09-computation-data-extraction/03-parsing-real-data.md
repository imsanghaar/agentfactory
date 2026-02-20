---
sidebar_position: 4
title: "Parsing Real Data"
chapter: 9
lesson: 3
layer: L2
duration_minutes: 25
description: "Direct Claude Code to build a CSV parser that handles the traps hiding in real bank statements"
keywords:
  [
    "CSV",
    "awk",
    "csv module",
    "structured data",
    "bank statement",
    "parsing",
    "data extraction",
  ]

# HIDDEN SKILLS METADATA
skills:
  - name: "Directing CSV Processing"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Data Processing"
    measurable_at_this_level: "Student can direct Claude Code to build a CSV parser that handles real-world edge cases"

  - name: "Understanding CSV Parsing Traps"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can explain why awk/cut fail on quoted CSV fields"

  - name: "Adapting Scripts to Personal Data"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Data Processing"
    measurable_at_this_level: "Student can modify a script to match their specific CSV column layout"

learning_objectives:
  - objective: "Direct Claude Code to build a CSV parser for bank statements"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student prompts agent to create sum-expenses.py that handles quoted fields"

  - objective: "Explain why simple delimiter-based tools fail on real CSV"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student identifies that quoted fields with commas break awk/cut"

  - objective: "Adapt a CSV parsing script to handle a specific bank format"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student modifies column references to match their bank's CSV layout"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (CSV quoting complexity, awk limitation, csv module) within A2 limit of 5"

differentiation:
  extension_for_advanced: "Add command-line column selection, explore csv.DictReader for named columns"
  remedial_for_struggling: "Focus on the conversation - watch how the agent recognizes and solves the CSV trap"

teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "Real Data and Permanent Tools"
  key_points:
    - "The CSV quoting trap (commas inside quoted fields breaking awk) is the canonical example of 'clean test data behaves, real data cheats'"
    - "The collaboration pattern is the lesson's real teaching: student discovers the failure (awk on AMAZON, INC.), agent provides the solution (csv module) — neither could solve it alone"
    - "Mentioning the edge case in your prompt ('some merchant names have commas') steers the agent to robust solutions instead of naive ones"
    - "The awk-vs-csv decision table is a practical tool: if data comes from outside your control, always use a proper CSV parser"
  misconceptions:
    - "Students think awk is always wrong for CSV — it works fine for tab-separated data and CSVs you control, only failing on external data with quoted fields"
    - "Students may not realize the bug is intermittent — awk works on rows without commas in fields and fails silently on rows with them, making it the worst kind of bug"
    - "Students assume Python's csv module is overkill for simple data — but the edge cases it handles (escaped quotes, different line endings) justify it for any external CSV"
  discussion_prompts:
    - "The awk command returned 'INC.' instead of an error. Why is a wrong value more dangerous than a crash for financial data?"
    - "You discovered the awk failure before asking the agent. How did bringing a specific failure example change the quality of the agent's response?"
    - "The lesson says 'if the CSV came from outside your control, use a proper CSV parser.' Why does the source of the data matter more than its apparent simplicity?"
  teaching_tips:
    - "Have students run the awk command on the AMAZON, INC. line themselves — seeing 'INC.' appear instead of '-89.50' is the lesson's central shock moment"
    - "Walk through the awk field-splitting diagram (4 fields instead of 3) on the board — visual learners need to see how the comma inside quotes creates a phantom field"
    - "The privacy note about bank CSVs is important — remind students they can remove account numbers before processing, or use the provided test data"
    - "Connect to Lesson 2's zero-trust philosophy: even this csv-module script should be verified with known-answer test data before running on real bank statements"
  assessment_quick_check:
    - "Give students the line '2024-01-07,\"AMAZON, INC.\",-89.50' and ask: what does 'awk -F, \"{print $3}\"' return and why?"
    - "Ask: 'When should you use awk and when should you use Python csv module?' — tests understanding of the decision table"
    - "Ask students to write a prompt that would steer the agent toward a robust CSV solution instead of a naive awk approach"
---

# Parsing Real Data

You download your bank statement, point sum-expenses at it, and get a number. It looks reasonable. You almost move on. Then something nags at you — that Amazon order was $89.50, but you can't find it in the output. You scroll through the CSV and spot the problem: `"AMAZON, INC."` — a comma hiding inside quotes. Your script just silently split that merchant name in half and summed the wrong column.

This is the wall that every real-world data task hits. Clean test data behaves. Real data cheats.

:::warning Checkpoint: Use YOUR Bank Data
Download your actual bank statement as CSV. Most banks offer this under "Download Transactions" or "Export" in online banking.

If your bank doesn't offer CSV export, use the test data below instead.

**Privacy note:** Your bank CSV may contain account numbers. Before processing, you can remove sensitive columns. The scripts only need the Description and Amount columns.
:::

## The Problem

Here's what a bank statement CSV looks like:

```csv
Date,Description,Amount
2024-01-02,Coffee Shop,-5.50
2024-01-03,Grocery Store,-127.43
2024-01-07,"AMAZON, INC.",-89.50
```

You need to sum the Amount column. The third column. Simple, right?

Look at line 4 carefully. The description is `"AMAZON, INC."` -- it contains a comma INSIDE the quoted field. If you split on commas, you'll get the wrong column.

## Try the Obvious Approach First

Before asking Claude Code for help, try the obvious solution yourself. The Amount is the third column. awk splits on commas. This should work:

```bash
echo '2024-01-07,"AMAZON, INC.",-89.50' | awk -F',' '{print $3}'
```

**Output:**

```
 INC."
```

That's garbage. Not `-89.50`. Not even close. awk split on EVERY comma, including the one inside the quoted field. It saw four fields:

1. `2024-01-07`
2. `"AMAZON`
3. ` INC."`
4. `-89.50`

Field 3 is ` INC."` — not the amount you wanted. And the worst part? No error. No warning. Just a wrong value that looks plausible enough to miss.

Now try the rows WITHOUT quotes:

```bash
echo '2024-01-02,Coffee Shop,-5.50' | awk -F',' '{print $3}'
```

**Output:**

```
-5.50
```

That works. The trap only triggers on quoted fields — the rows where merchant names contain commas. Some rows work, some silently fail. This is the worst kind of bug.

## The Conversation

Now bring this problem to Claude Code. Show it what you found:

```
You: I have a bank statement CSV. I tried using awk to get the Amount
column but it breaks on rows like: 2024-01-07,"AMAZON, INC.",-89.50
The comma inside the quotes throws off the column count. How do I
sum the Amount column correctly?
```

Watch what happens:

```
Claude Code: That's the classic CSV quoting trap. awk treats every
comma as a delimiter, even inside quotes. I'll use Python's csv
module which understands quoting rules.

[Creates: sum-expenses.py]

#!/usr/bin/env python3
# sum-expenses.py - Sum the Amount column from bank statement CSV
import sys
import csv

total = 0
reader = csv.reader(sys.stdin)
next(reader)  # Skip header row

for row in reader:
    amount_str = row[2]  # Amount is 3rd column (index 2)
    amount = float(amount_str.replace('$', '').replace(',', ''))
    total += abs(amount)

print(f"Total: ${total:.2f}")

[Creates: test_bank.csv]
Date,Description,Amount
2024-01-02,Coffee Shop,-5.50
2024-01-03,Grocery Store,-127.43
2024-01-07,"AMAZON, INC.",-89.50

[Runs: cat test_bank.csv | python sum-expenses.py]

Total: $222.43
```

Notice the collaboration. YOU discovered the awk failure by running it yourself. You brought that specific failure to the agent, which told it exactly what problem to solve. The agent knew about Python's csv module — something you might not have found on your own. You taught the agent about your data. The agent taught you about the right tool.

**Python's csv module understands quoting rules.** It knows that commas inside quotes don't count as separators. The module handles:

- Quoted fields with commas inside
- Escaped quotes within quoted fields
- Different line ending styles
- Edge cases you haven't thought of yet

## When to Use Which

| Data Type | Use awk | Use csv module |
|-----------|---------|----------------|
| Log files with consistent delimiters | Yes | |
| Tab-separated data | Yes | |
| Data you control (no embedded delimiters) | Yes | |
| Bank exports | | Yes |
| Downloaded datasets | | Yes |
| Any external CSV | | Yes |

Rule of thumb: If the CSV came from outside your control, use a proper CSV parser.

## The Pattern

Here's the pattern for handling structured data:

```
"I have [structured data type]. Process [specific column/field].
Be careful - [edge case that could break naive parsing]."
```

Mentioning the edge case helps the agent choose robust solutions. Compare:

| Prompt | Agent's Likely Response |
|--------|------------------------|
| "Sum the third column of this CSV" | Might use awk (faster, simpler) |
| "Sum the Amount column. Some merchant names have commas" | Uses csv module (handles edge cases) |

The second prompt gives context that guides the agent to the right tool. You're teaching the agent about your data -- and the agent is teaching you which tools handle that data correctly.

You have a script that handles real bank data — commas in quotes, dollar signs, the works. But right now it's stuck in whatever folder you built it in. Next month when you download a fresh bank statement into `~/finances/`, you'll have to remember the exact path to this script. If you have to remember where a tool lives, it's not a tool yet. (And once it IS a tool, you'll still need to teach it the difference between a pharmacy and a Dr. Pepper. That's coming.)

---

## Try With AI

### Prompt 1: Understand the CSV Trap

```
Show me what happens when I try to parse "AMAZON, INC.",-89.50 with awk.
Why does it give the wrong result? What does Python's csv module do differently?
```

**What you're learning:** Deep understanding of the failure mode. The agent demonstrates the problem step by step, so you understand why csv modules exist -- not just that you should use them.

### Prompt 2: Extend the Parser

```
My sum-expenses.py works well. Can you modify it to:
1. Accept a column number as an argument (so I can sum any column)
2. Handle empty lines gracefully
3. Show how many transactions were processed

Keep the stdin pattern so it still works with pipes.
```

**What you're learning:** Iterative improvement. You have working code and clear requirements. The agent extends functionality while preserving the composable pattern.

### Prompt 3: Adapt to Your Bank Format

```
My bank's CSV has different column names than the example. The amount
column is called 'Debit' instead of 'Amount' and there's a separate
'Credit' column. How do I modify sum-expenses.py to handle my specific
bank format?
```

**What you're learning:** Adapting scripts to YOUR data. Every bank exports differently. The agent helps you customize the tool for your specific situation.
