---
sidebar_position: 6
chapter: 8
lesson: 6
layer: L2
title: "Search & Discovery Workflow"
description: "Direct Claude Code to find files by description rather than memorizing search commands. Because you know what you're looking for, not where it is"
duration_minutes: 25
keywords:
  [
    "file search",
    "content search",
    "descriptive search",
    "grep",
    "find",
    "search refinement",
  ]

skills:
  - name: "Descriptive File Search"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can describe files to find by characteristics rather than exact names"

  - name: "Search Refinement Direction"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can narrow search results through conversational refinement"

  - name: "Pattern Recognition Request"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can ask agent to find similar files based on discovered examples"

learning_objectives:
  - objective: "Direct Claude Code to find files by description instead of filename"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student locates a file by describing its content or purpose"

  - objective: "Refine search results through conversation"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student narrows from many candidates to the target file"

  - objective: "Request discovery of similar files"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student asks agent to find related files based on a found example"

  - objective: "Observe combined bash tools in agent workflow"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student identifies how agent combines find, grep, and pipes"

cognitive_load:
  new_concepts: 3
  concepts_list:
    - "Descriptive search (describing what, not how)"
    - "Search refinement (narrowing through conversation)"
    - "Pattern-based discovery (find similar files)"
  assessment: "3 concepts within A2 limit of 5"

differentiation:
  extension_for_advanced: "Ask Claude Code to create a search report showing all tax-related documents from the past 3 years, organized by year"
  remedial_for_struggling: "Start with a simple search: 'Find any PDF files in my Documents folder.' Then gradually add constraints like date or content."

teaching_guide:
  lesson_type: "core"
  session_group: 3
  session_title: "Search, Synthesis, and Capstone"
  key_points:
    - "The inversion from 'search by location' to 'search by description' is the core mindset shift — students know WHAT they want, agents know HOW to find it"
    - "Three search layers build progressively: filename metadata → content inside files (pdftotext + grep) → pattern-based discovery of similar files"
    - "Conversational refinement ('from Chase, not Fidelity') is a transferable skill that applies to databases, research tasks, and any AI-directed search"
    - "The chapter progression table (Lessons 1-6) shows how each lesson added a new capability — use this to show students how far they have come"
  misconceptions:
    - "Students think searching means knowing the exact filename — the entire lesson demonstrates that describing characteristics (type, date, content, source) is more powerful"
    - "Students may not realize content search (pdftotext) is fundamentally different from filename search — looking inside files accesses information invisible to folder browsing"
    - "Students assume broad searches are always better — the session protection tip shows why saving results to a file prevents conversation flooding"
  discussion_prompts:
    - "When was the last time you spent 20 minutes looking for a file? How would you describe it to an agent instead of clicking through folders?"
    - "The agent searched INSIDE PDFs to find invoices with generic filenames like 'document.pdf'. What other situations have important information trapped inside files with unhelpful names?"
    - "Descriptive search works for files, databases, and research. What makes 'describe what you need' a universal skill across different domains?"
  teaching_tips:
    - "Start with the lost tax document scenario — it is universally relatable and immediately motivates why location-based search fails"
    - "The traditional vs agent-directed search comparison table is excellent for the board — have students add their own examples to each column"
    - "Demo the content search (finding invoices inside generically-named PDFs) live — the moment students see information extracted from file contents, the capability becomes real"
    - "Connect the 'find similar files' pattern to real research workflows — this is how professionals discover related documents they did not know existed"
  assessment_quick_check:
    - "Give students a scenario: 'You need a contract you signed last year but cannot remember the filename.' Ask them to write the search prompt they would give the agent"
    - "Ask: 'What is the difference between searching by filename and searching by content? When do you need each?' — tests understanding of the three search layers"
    - "Ask students to name the six patterns from this chapter in order — tests synthesis of the full chapter arc"
---

# Search & Discovery Workflow

You downloaded it. You know you did. It was a PDF, something about taxes, from your bank. It's been 20 minutes of clicking through folders. Downloads? Not there. Documents? Nothing. Desktop? You're starting to wonder if you imagined it.

This is the most common file problem in existence, and you've been solving it wrong your whole life. You've been searching by _where_ you put things. "Was it in the Finance folder or the 2023 folder?" But you don't remember where you put it. You remember _what_ it was: a tax document, about dividends, from Chase.

That's the inversion this lesson teaches. Stop searching by location. Start searching by description. You know WHAT you're looking for. The agent knows HOW to find it. That's the ideal split.

---

## The Conversation

Open Claude Code. Describe the problem.

```
You: I'm looking for a tax document from 2023. It was a PDF, something
about dividends or 1099. I think I downloaded it from my bank. Can you
help me find it?
```

Watch what Claude Code does.

```
Claude Code: I'll search for that tax document. Let me check common
locations for downloaded PDFs related to taxes.

[Runs: find ~/Downloads ~/Documents -name "*.pdf" -newer "2023-01-01"
  ! -newer "2024-01-01" 2>/dev/null]
[Runs: find ~/Downloads ~/Documents -iname "*1099*" -o -iname "*tax*"
  -o -iname "*dividend*" 2>/dev/null]

I found several candidates:

| File                           | Location            | Modified   |
|--------------------------------|---------------------|------------|
| 1099-DIV-2023-Fidelity.pdf     | ~/Downloads         | 2023-02-14 |
| 1099-INT-2023-Chase.pdf        | ~/Downloads         | 2023-01-28 |
| Tax-Summary-2023.pdf           | ~/Documents/Taxes   | 2023-04-12 |
| dividend-statement-Q4-2023.pdf | ~/Downloads         | 2023-10-15 |
| W2-2023-Employer.pdf           | ~/Documents/Taxes   | 2023-02-01 |

The most likely match for "dividends or 1099" is:
  ~/Downloads/1099-DIV-2023-Fidelity.pdf

Is this the one you're looking for?
```

That's a lot of results. Let's narrow it down.

```
You: It was from my bank, not Fidelity. I think it was Chase or
Bank of America.
```

```
Claude Code: Let me narrow the search to bank-related documents.

[Runs: find ~/Downloads ~/Documents -iname "*chase*" -o
  -iname "*bofa*" -o -iname "*bankofamerica*" 2>/dev/null |
  xargs grep -l -i "1099\|dividend" 2>/dev/null]

Found these bank-related tax documents:

| File                          | Location    | Content Match       |
|-------------------------------|-------------|---------------------|
| 1099-INT-2023-Chase.pdf       | ~/Downloads | Contains "1099-INT" |
| Chase-Tax-Statements-2023.pdf | ~/Documents | Contains "dividend" |

The Chase 1099-INT document looks like your best match.
Want me to open it so you can verify?
```

That's the one.

```
You: That's it! Actually, can you find all my Chase tax documents?
I want to see what else I have from them.
```

```
Claude Code: I'll find all Chase-related tax documents.

[Runs: find ~ -iname "*chase*" -type f \( -iname "*.pdf" -o
  -iname "*.PDF" \) 2>/dev/null]
[Runs: grep -r -l -i "chase.*1099\|chase.*tax\|chase.*statement"
  ~/Documents ~/Downloads 2>/dev/null]

Here's everything I found from Chase:

TAX DOCUMENTS:
  ~/Downloads/1099-INT-2023-Chase.pdf         (2023)
  ~/Downloads/1099-INT-2022-Chase.pdf         (2022)
  ~/Documents/Taxes/Chase-Year-End-2023.pdf   (2023)
  ~/Documents/Taxes/Chase-Year-End-2022.pdf   (2022)

OTHER CHASE FILES:
  ~/Downloads/Chase-Statement-Dec-2023.pdf    (statement)
  ~/Downloads/Chase-Statement-Nov-2023.pdf    (statement)

You have 4 tax documents and 2 regular statements from Chase.
Would you like me to organize these into a Chase-Taxes folder?
```

You went from "I can't find that tax document" to "here's everything from Chase" in three exchanges.

---

## The Invisible Skill

You're learning something you might not realize. "Descriptive search" — describing what you're looking for instead of knowing where it is — is a transferable skill that goes far beyond files. Every database query, every research task, every time you ask an AI to find information in a large corpus, you're doing the same thing: describing what you need and letting a system figure out how to find it.

The agent used `find`, `grep`, and `xargs` behind the scenes. You didn't need to know those commands. But notice the skill you _did_ use: you described the file in progressively more specific terms. "Tax document from 2023" → "about dividends" → "from Chase, not Fidelity." Each refinement narrowed the search. That's the skill — not bash syntax, but the ability to describe what you need in terms a search can use.

| Traditional Search         | Agent-Directed Search                    |
| -------------------------- | ---------------------------------------- |
| Type exact filename        | Describe what you're looking for         |
| One folder at a time       | Search multiple locations simultaneously |
| Match filename only        | Match content inside files               |
| Get list, you filter       | Agent filters and explains why           |
| You refine with new search | Agent refines through conversation       |

---

## The Level-Up: Searching Inside Files

Everything above searched by *filename*. But what about files whose names tell you nothing?

Your Downloads folder has 40 PDFs named `document.pdf`, `download.pdf`, `file(1).pdf`. The filename is useless. The information you need is *inside* the file.

```
You: I have a bunch of PDFs with generic names. One of them is an
invoice from December for more than $500. Can you search INSIDE
the PDFs to find it?
```

```
Claude Code: I'll search the content of your PDF files.

[Runs: find ~/Downloads -name "*.pdf" -newer "2025-12-01"
  ! -newer "2026-01-01" -exec pdftotext {} - 2>/dev/null \;
  | grep -l -i "invoice"]

Actually, let me take a better approach — I'll check each PDF
individually so I can tell you which file matches.

[Runs: for f in ~/Downloads/*.pdf; do
  if pdftotext "$f" - 2>/dev/null | grep -qi "invoice"; then
    echo "$f: $(pdftotext "$f" - 2>/dev/null | grep -i 'total\|amount\|$'
      | head -3)"
  fi
done]

Found 6 PDFs containing "invoice":

| File                | Key Content                    |
|---------------------|--------------------------------|
| download(3).pdf     | Invoice #4521, Total: $847.00  |
| document.pdf        | Invoice #3892, Total: $125.50  |
| file(1).pdf         | Invoice #4103, Total: $2,340   |
| scan_20251215.pdf   | Invoice #4287, Total: $599.99  |
| unnamed.pdf         | Invoice #3901, Total: $89.00   |
| receipt_dec.pdf     | Invoice #4455, Total: $312.00  |

The ones over $500 are: download(3).pdf ($847), file(1).pdf ($2,340),
and scan_20251215.pdf ($599.99).

Want me to rename these with meaningful names based on their content?
```

This is the jump from searching by *metadata* (filename, date, size) to searching by *content* (what's actually in the file). The agent used `pdftotext` to read inside the PDFs, then `grep` to find matches. You couldn't do this by browsing folders — the filenames told you nothing.

**The progression through this chapter:**
- Lesson 1: See your files (metadata)
- Lesson 3: Organize by extension (surface attributes)
- Lesson 6: Search by content (deep attributes)

Each level gives you access to information the previous level couldn't reach.

---

## The Pattern

Here's what made this work:

```
"Find files that match [description] from [time period]"
```

This pattern tells the agent:

1. What characteristics to look for (description)
2. When the file was created or modified (time period)
3. That you don't know the exact location

The agent will search broadly and then narrow based on your criteria.

The second key pattern:

```
"Find all similar files to this one"
```

Once you find one example, this request triggers a pattern-based search. The agent identifies characteristics of the found file and looks for others that match.

Together, these patterns turn "I can't find it" into "here's everything related."

---

## Why Description Beats Commands

Consider the mental load difference:

| Approach       | What You Need to Know            |
| -------------- | -------------------------------- |
| Manual `find`  | Exact syntax, flags, regex       |
| Manual `grep`  | Pattern matching, file piping    |
| Combined tools | How to chain commands with xargs |
| Agent-directed | What you're looking for          |

The agent knows `find -iname "*pattern*" -newer "date"`. The agent knows `grep -l -i "content"`. You know "it was a tax document from 2023 about dividends."

Your knowledge is valuable. The agent's command syntax knowledge is mechanical. The combination is powerful.

### Protecting Your Session From Too Many Results

One thing to watch for: broad searches can return thousands of results. If you ask the agent to search your entire home directory, the output might flood the conversation and degrade the agent's performance. When you expect many results, ask the agent to save them:

```
Save the full list to search-results.txt and just show me the first 10 matches.
```

This keeps your session clean and creates a persistent record you can reference later.

---

## The Key Requests

Remember these phrases for search tasks:

| What You Want       | What to Say                                        |
| ------------------- | -------------------------------------------------- |
| Find by description | "Find files that match [description]"              |
| Add time constraint | "...from [time period]"                            |
| Search inside files | "...that contain [text]"                           |
| Find similar files  | "Find all similar files to this one"               |
| See search process  | "Show me where you're searching and what you find" |
| Narrow results      | "It was specifically from [source/context]"        |

You're not learning `find -mtime -30 -name "*.pdf" | xargs grep -l "pattern"`. You're learning how to describe what you need.

---

## What You're Building

By now in this chapter, you've learned:

| Lesson                    | Pattern                            |
| ------------------------- | ---------------------------------- |
| 1. First Workflow         | "Help me understand"               |
| 2. Safety First           | "Back up before changing"          |
| 3. Categorize with Rules  | "Write rules first"                |
| 4. Batch Operations       | "Show me first, create a script"   |
| 5. Error Recovery         | "Restore from backup, compare"     |
| **6. Search & Discovery** | **"Find files that match [desc]"** |

Each pattern expands your capability. You understand your files. You protect them with backups. You document your rules. You automate repetitive tasks. You recover from mistakes. Now you find anything by describing it.

You now have six distinct workflows. Survey, backup, organize, batch, recover, search. Each powerful on its own. But the real skill isn't knowing each workflow — it's knowing which one to reach for when your files are on fire and your boss is on the phone.

---

## Try With AI: Extended Practice

**Prompt 1: Multi-Criteria Search**

```
I need to find a document that meets multiple criteria:
- It's a PDF
- It contains the word "invoice" somewhere in the file
- It's from 2025
- The amount was over $500 (if you can search for that)

Show me your search strategy before running it.
```

**What you're practicing:** Complex search specification. You're asking the agent to combine multiple filters — file type, content, date, and even numeric values. Watch how it approaches an ambitious search request.

**Prompt 2: Search Report Generation**

```
Create a report of all tax-related documents I have, organized by year.
Include the filename, location, file size, and which year it's from.
Save the report so I can reference it later.
```

**What you're practicing:** Turning search into documentation. This request combines search (finding tax documents) with state persistence (saving a report). You're applying Principle 5 to search results.

**Prompt 3: Semantic Duplicate Detection**

```
I think I have duplicate files with DIFFERENT names — the same document saved
as "Budget Final.xlsx" and "budget_v2_final.xlsx". Can you find files that
might be duplicates based on file SIZE and CONTENT similarity, not just name?
```

**What you're practicing:** Semantic deduplication. Finding duplicates that look different on the surface. This asks the agent to go beyond simple name matching and use file characteristics to identify copies that were renamed, versioned, or saved under different names.
