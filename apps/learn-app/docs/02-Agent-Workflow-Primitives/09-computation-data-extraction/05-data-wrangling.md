---
sidebar_position: 6
title: "Data Wrangling"
chapter: 9
lesson: 5
layer: L2
duration_minutes: 30
description: "Watch Claude Code categorize bank transactions with regex patterns and false-positive guards, then process multiple files"
keywords:
  [
    "regex",
    "regular expressions",
    "re module",
    "find",
    "xargs",
    "data extraction",
    "pattern matching",
    "tax categorization",
  ]

skills:
  - name: "Directing Pattern-Based Categorization"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Data Processing"
    measurable_at_this_level: "Student can direct Claude Code to build a categorizer with edge case handling"

  - name: "Understanding Regex Patterns"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Pattern Recognition"
    measurable_at_this_level: "Student can explain why word boundaries prevent false matches"

  - name: "Batch File Processing"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Automation"
    measurable_at_this_level: "Student uses find and xargs to process multiple files"

learning_objectives:
  - objective: "Direct Claude Code to build a transaction categorizer with false-positive guards"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student prompts agent to create tax-categorize.py that handles edge cases"

  - objective: "Explain how regex word boundaries prevent false matches"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can explain why \\bCVS\\b matches 'CVS PHARMACY' but not 'CVSMITH'"

  - objective: "Use find and xargs to batch process multiple CSV files"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student executes: find . -name '*.csv' | xargs cat | python tax-categorize.py"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (categorization logic, false positives, regex word boundaries, false positive guards, batch processing) within A2 limit"

differentiation:
  extension_for_advanced: "Handle case sensitivity, regex anchors for precision, more complex patterns"
  remedial_for_struggling: "Focus on the conversation - use pre-built keyword lists, don't modify patterns yourself"

teaching_guide:
  lesson_type: "core"
  session_group: 3
  session_title: "Data Wrangling and Capstone"
  key_points:
    - "The Dr. Pepper false positive is the chapter's signature teaching moment — simple keyword matching ('DR' in description) silently inflates tax deductions, which is fraud by algorithm"
    - "Regex word boundaries (\\b) solve partial matching: \\bCVS\\b matches 'CVS PHARMACY' but not 'CVSMITH' — this single concept prevents an entire category of false positives"
    - "FALSE_POSITIVES checked BEFORE categories demonstrates that execution order matters — guards must run first or the match happens before the guard can block it"
    - "The find | xargs cat | python pipeline chains three Unix tools to process 12 months of bank statements in one command — the composability from Lesson 1 scales to real workflows"
  misconceptions:
    - "Students think the first categorizer output 'looks right' — the false positives (Dr. Pepper, CVSMITH) are deliberately plausible enough to miss on casual inspection"
    - "Students confuse regex word boundaries with exact string matching — \\bCVS\\b still matches 'CVS PHARMACY' and 'CVS/STORE' because the boundary is at word edges, not string edges"
    - "Students may think false positives are edge cases they can ignore — on tax returns, a $204.99 inflation from Dr. Pepper and CVSMITH is a concrete financial error"
  discussion_prompts:
    - "The first version of the categorizer 'looked right' until you scanned the medical list carefully. How do you decide when to trust output and when to inspect it line by line?"
    - "Why are FALSE_POSITIVES checked before categories rather than after? What would happen if you checked them in the opposite order?"
    - "The Dr. Pepper problem only shows up in bank data where merchant names are messy. What other domains have similar 'looks like X but is actually Y' matching problems?"
  teaching_tips:
    - "Let students see the FIRST output (with false positives) and ask them to find the bugs BEFORE revealing them — this builds the inspection habit"
    - "Draw the regex word boundary concept on the board with 'CVSMITH' and show where \\b does and does not trigger — visual learners need to see the boundary positions"
    - "The batch processing pipeline (find | xargs cat | python) is worth walking through step by step — each pipe adds one capability"
    - "The iterative loop (build → test → find false positives → fix) is the lesson's workflow pattern — emphasize that no one designs perfect categorization rules on the first try"
  assessment_quick_check:
    - "Ask: 'Why does matching DR in a transaction description catch both doctor visits and Dr. Pepper?' — tests understanding of substring vs word boundary matching"
    - "Give students the pattern \\bCVS\\b and ask which of these it matches: 'CVS PHARMACY', 'CVSMITH', 'MY CVS RECEIPT', 'MCVS' — tests regex boundary understanding"
    - "Ask students to explain the three stages of the batch pipeline: find, xargs cat, python script — tests understanding of Unix composability"
---

# Data Wrangling

In Lesson 4, you built a permanent toolkit of reusable scripts. Now you'll put one of those tools to work on a real problem: tax categorization.

sum-expenses gives you totals. But tax season needs CATEGORIES -- medical, charitable, business. Your accountant doesn't want "Total: $4,215.52." They want:

- Medical expenses: $1,891.20
- Charitable donations: $1,550.00
- Business supplies: $774.32

The challenge: bank statements use chaotic merchant names. CVS, Walgreens, and "PHARMACY #1234" are all medical. "DR MARTINEZ MEDICAL" is a doctor visit. But "DR PEPPER SNAPPLE" is soda, not a medical expense.

Let's watch Claude Code build a categorizer -- and discover why the first attempt breaks.

## The Conversation

Open Claude Code and describe your categorization challenge:

```
You: Help me categorize my bank transactions for taxes. I need to identify:
- Medical: CVS, Walgreens, pharmacy, doctor visits
- Charitable: donations, Red Cross, United Way
- Business: Office Depot, Staples, subscriptions
```

Notice what you DIDN'T say: you didn't warn about false positives. Let's see what happens.

```
Claude Code: I'll build a categorizer using keyword matching.

[Creates: tax-categorize.py]

#!/usr/bin/env python3
import sys
import csv

CATEGORIES = {
    'medical': ['CVS', 'WALGREENS', 'PHARMACY', 'DR', 'MEDICAL'],
    'charitable': ['DONATION', 'RED CROSS', 'UNITED WAY'],
    'business': ['OFFICE DEPOT', 'STAPLES', 'SUBSCRIPTION'],
}

def categorize(description):
    desc_upper = description.upper()
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in desc_upper:
                return category
    return None

# Process CSV from stdin
reader = csv.DictReader(sys.stdin)
totals = {}
for row in reader:
    cat = categorize(row['Description'])
    if cat:
        amount = abs(float(row['Amount'].replace('$', '')))
        totals.setdefault(cat, 0)
        totals[cat] += amount
        print(f"{cat.upper()}: {row['Description']}: ${amount:.2f}")

print("\n--- TOTALS ---")
for cat, total in totals.items():
    print(f"{cat.title()}: ${total:.2f}")

[Runs: cat test_bank.csv | python tax-categorize.py]

MEDICAL: CVS/PHARMACY #1234: $45.67
MEDICAL: WALGREENS #5678: $23.45
MEDICAL: DR MARTINEZ MEDICAL: $150.00
MEDICAL: DR PEPPER SNAPPLE: $4.99
CHARITABLE: UNITED WAY: $100.00
MEDICAL: CVSMITH CONSULTING: $200.00
BUSINESS: OFFICE DEPOT #901: $89.50

--- TOTALS ---
Medical: $424.11
Charitable: $100.00
Business: $89.50
```

At first glance, that looks right. Medical, charitable, business — all categorized. The totals look reasonable. You almost move on.

Then you scan the medical list one more time. Wait.

## The Bug

**Dr. Pepper is not a doctor.**

```
MEDICAL: DR PEPPER SNAPPLE: $4.99      <-- Soda, not a doctor
MEDICAL: CVSMITH CONSULTING: $200.00   <-- A consultant, not CVS pharmacy
```

There it is. The keyword "DR" appears in "DR PEPPER," so the categorizer flags it as medical. "CVS" appears inside "CVSMITH," so a consulting fee gets counted as a pharmacy visit.

This is what simple keyword matching does. `if 'CVS' in desc_upper` matches ANYTHING containing those three letters in sequence — CVS Pharmacy, CVSMITH, MCVS, whatever. And `if 'DR' in desc_upper` matches every doctor AND every Dr. Pepper.

Your medical total is inflated by $204.99. On a tax return, that's a problem.

## The Fix

Now you know what's wrong. Tell the agent:

```
You: The categorizer has false positives. "DR PEPPER" is showing up as
medical, and "CVSMITH" is matching as CVS. Can you fix these?
```

```
Claude Code: Good catch. The problem is simple keyword matching.
I need two fixes: word boundaries so "CVS" only matches the
standalone word, and false positive guards for things like Dr. Pepper.

[Updates: tax-categorize.py]

import re

CATEGORIES = {
    'medical': [r'\bCVS\b', r'\bWALGREENS\b', r'\bPHARMACY\b', r'\bMEDICAL\b'],
    'charitable': [r'\bDONATION\b', r'\bRED CROSS\b', r'\bUNITED WAY\b'],
    'business': [r'\bOFFICE DEPOT\b', r'\bSTAPLES\b', r'\bSUBSCRIPTION\b'],
}

FALSE_POSITIVES = [r'\bDR\.?\s*PEPPER\b', r'\bCVSMITH\b']

def categorize(description):
    desc_upper = description.upper()
    for fp_pattern in FALSE_POSITIVES:
        if re.search(fp_pattern, desc_upper, re.IGNORECASE):
            return None
    for category, patterns in CATEGORIES.items():
        for pattern in patterns:
            if re.search(pattern, desc_upper, re.IGNORECASE):
                return category
    return None
```

Look at what the agent changed -- and WHY each fix solves a specific false positive.

**`\bCVS\b` fixes CVSMITH.** The `\b` is a word boundary -- it marks where a word starts or ends. So `\bCVS\b` matches "CVS PHARMACY" (CVS is a complete word) but NOT "CVSMITH" (CVS is part of a longer word). Without boundaries, `CVS` matches any string containing those letters.

**`FALSE_POSITIVES` checked first fixes Dr. Pepper.** The pattern `\bDR\.?\s*PEPPER\b` matches "DR PEPPER" and "DR. PEPPER" (the `\.?` makes the period optional). Because false positives are checked BEFORE categories, Dr. Pepper gets excluded before "DR" can trigger a medical match. Order matters -- guards run first.

**`\b(AMZN|AMAZON)\b` shows the pattern generalizes.** If you later need to match Amazon transactions, the same word boundary technique catches "AMZN" and "AMAZON" without matching "AMAZONIA" or "CAMZN."

Let's verify the fix:

```
[Runs: cat test_bank.csv | python tax-categorize.py]

MEDICAL: CVS/PHARMACY #1234: $45.67
MEDICAL: WALGREENS #5678: $23.45
MEDICAL: DR MARTINEZ MEDICAL: $150.00
CHARITABLE: UNITED WAY: $100.00
BUSINESS: OFFICE DEPOT #901: $89.50

--- TOTALS ---
Medical: $219.12
Charitable: $100.00
Business: $89.50
```

Dr. Pepper and CVSMITH are gone. DR MARTINEZ MEDICAL still matches because it contains "MEDICAL" as a standalone word. The totals are now correct.

**Checkpoint:** Run the categorizer on YOUR bank data from Lesson 3. How many transactions does it categorize? How many false positives do you spot?

## Processing Multiple Files

You have 12 months of bank statements. Processing them one by one would be tedious.

```
You: I have a folder with 12 months of bank statements (january.csv through
december.csv). Process them all at once.
```

```
Claude Code: I'll use find and xargs to batch process all CSV files.

[Runs: find statements/ -name "*.csv" | xargs cat | python tax-categorize.py]

Processing 12 files...
Total transactions: 1,247

MEDICAL (Schedule A):
  CVS PHARMACY (23 txns)      $456.70
  WALGREENS (15 txns)         $234.50
  Doctor visits (8 txns)      $1,200.00
  SUBTOTAL:                   $1,891.20

CHARITABLE (Schedule A):
  Donations (12 txns)         $1,550.00

BUSINESS:
  Office supplies (18 txns)   $539.76
  Subscriptions (9 txns)      $234.56
  SUBTOTAL:                   $774.32

All 12 months processed in one command.
```

**How the pipeline works:**

```bash
find statements/ -name "*.csv" | xargs cat | python tax-categorize.py
```

1. `find` locates all CSV files in the statements folder
2. `xargs cat` reads them all and combines the output
3. `tax-categorize.py` categorizes and sums everything

One command processes an entire year of transactions.

## The Pattern

Two prompt patterns emerged in this lesson:

**Categorization:** `"Categorize [data] by [criteria]."`

Start simple -- let the agent build a first version. Then test it and look for false positives yourself. When you find them, tell the agent: `"[X] is showing up as [Y]. Fix it."` This iterative loop produces better results than trying to anticipate every edge case upfront.

**Batch processing:** `"I have [multiple files matching pattern]. Process them all at once."`

This signals you want file discovery with `find`, batch execution with `xargs`, and aggregated results.

You can categorize transactions and process multiple files. But you've been doing this piece by piece — summing here, categorizing there, batch processing over here. In the capstone, you'll orchestrate everything into a single workflow: point Claude Code at a folder of bank statements and get an accountant-ready tax report. One conversation. One command. A full year of data.

---

## Try With AI

### Prompt 1: Design a Merchant Pattern

```
I need to match all Amazon transactions in my bank statement.
They appear as: AMZN MKTP US, AMAZON.COM, AMAZON PRIME

Write a regex pattern that matches all these but does NOT match:
- AMAZONIA TRAVEL
- CAMZN AUTO PARTS

Explain why word boundaries matter here.
```

**What you're learning:** Regex design with precision. The agent shows how `\b(AMZN|AMAZON)\b` catches variations while excluding false positives. You understand the WHY, not just the pattern.

### Prompt 2: Handle a New False Positive

```
My tax-categorize.py marks "AMAZON RIVER CRUISE" as a purchase
from Amazon.com. It's actually a travel expense.

How do I add this to the false positive guards? Show me the pattern
that excludes travel-related Amazon mentions.
```

**What you're learning:** Iterative refinement. As you discover new false positives, you update the guards. The agent shows how to add patterns without breaking existing categorization.

### Prompt 3: Extend Categories

```
Help me add these categories to tax-categorize.py:
- home_office: Home Depot, Lowes, Ikea (but NOT "IKEA RESTAURANT")
- subscriptions: Netflix, Spotify, Hulu, Apple.com

What false positives might I need to guard against?
```

**What you're learning:** Proactive edge case thinking. The agent suggests guards you might not have considered -- like distinguishing IKEA furniture from IKEA food court. You're learning to anticipate problems before they happen.
