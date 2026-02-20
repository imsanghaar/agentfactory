---
sidebar_position: 3
chapter: 8
lesson: 3
layer: L2
title: "The Organization Workflow"
description: "Collaborate with Claude Code to design categorization rules, document them for reuse, and test on one file before scaling"
duration_minutes: 25
keywords:
  [
    "categorization",
    "rules",
    "organization",
    "file sorting",
    "iterative refinement",
    "state persistence",
  ]

skills:
  - name: "Collaborative Rule Design"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Work with AI to design categorization rules through iterative refinement"

  - name: "State Persistence"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Document rules in rules.md for future reuse"

  - name: "Single-File Testing"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Test categorization on one file before batch processing"

  - name: "Iterative Refinement"
    proficiency_level: "A2"
    category: "Soft"
    bloom_level: "Evaluate"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Refine AI suggestions based on personal requirements"

learning_objectives:
  - objective: "Collaborate with Claude Code to analyze files and propose categorization"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student engages in multi-turn conversation refining categories"

  - objective: "Refine AI-proposed categories based on personal needs"
    proficiency_level: "A2"
    bloom_level: "Evaluate"
    assessment_method: "Student modifies initial suggestion with custom categories"

  - objective: "Create rules.md documenting categorization logic"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Document exists with complete extension-to-directory mapping"

  - objective: "Test categorization on ONE file before batch processing"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student verifies single file moved correctly"

  - objective: "Execute batch organization with verification summary"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Student reviews summary and confirms results"

cognitive_load:
  new_concepts: 4
  concepts_list:
    - "Collaborative rule design (propose-refine-iterate pattern)"
    - "State persistence (rules.md for reusable logic)"
    - "Single-file testing (decomposition before scaling)"
    - "Batch execution with verification (trust but verify)"
  assessment: "4 concepts at A2 limit"

differentiation:
  extension_for_advanced: "Add project-based rules that override extension matching, and implement a conflict resolution strategy when files match multiple categories"
  remedial_for_struggling: "Focus on the basic extension-to-folder mapping and single-file test. Skip the misc deep-dive and content-based analysis for now."

teaching_guide:
  lesson_type: "core"
  session_group: 1
  session_title: "First Agent Workflow and Safety"
  key_points:
    - "The propose-refine-iterate pattern (agent proposes categories, student corrects based on domain knowledge) is the core collaboration model for all rule design"
    - "rules.md is more valuable than the organized folders — folders go stale, but documented logic is reusable forever"
    - "The 20% misc threshold is a concrete quality gate: if >20% of files are 'miscellaneous', the categorization system needs another layer"
    - "Single-file test + dry-run are two different verification steps: test checks the mechanism works, dry-run checks the decisions are right"
  misconceptions:
    - "Students think the agent's first suggestion is final — the CSV-as-text example shows why human correction of the agent's functional classification matters"
    - "Students confuse organized folders with a complete system — the folders are output, rules.md is the reusable product"
    - "Students may skip the single-file test because 'it worked in the conversation' — case-sensitivity bug shows why testing with real files catches hidden errors"
  discussion_prompts:
    - "The agent classified CSV as 'text' because it IS technically text. You corrected it to 'spreadsheet' because of how you USE it. When else does technical correctness differ from practical usefulness?"
    - "If nearly half your files end up in 'misc', is that a failure of the rules or a sign your files are genuinely diverse? How do you tell the difference?"
    - "Why is the dry-run step separate from the single-file test? What kind of error does each one catch?"
  teaching_tips:
    - "Start with the Q4-Budget-Draft.pdf ambiguity — ask students where THEY would file it before showing the lesson's approach"
    - "The case-sensitivity bug (30 missing files with uppercase extensions) is a powerful live demo — have students check whether their own system handles .PDF vs .pdf"
    - "Walk through the rules.md example on the board — students will create their own version in the checkpoint and need to understand the Layer 1 / Layer 2 structure"
    - "This is a natural session break point (noted in the lesson). Acknowledge this in class if doing multi-lesson workshops"
  assessment_quick_check:
    - "Ask students to list the 6-step organization pattern from memory: propose, refine, document, test one, dry-run, batch execute"
    - "Give a filename like 'meeting-recording-2026.mp4' and ask which category it goes to and why — tests rule application"
    - "Ask: 'What is more valuable — your organized folders or your rules.md? Why?' — tests understanding of state persistence"
---

# The Organization Workflow

Your Downloads has 487 files. Where does `Q4-Budget-Draft.pdf` go? Finance? Q4? Projects? Budget?

The answer reveals why categorization is harder than it looks. Every file belongs to multiple categories at once. A budget spreadsheet is a financial document AND a Q4 deliverable AND a project artifact. Any rule you pick will be wrong for some files.

That's the hard question this lesson tackles. Not "how do I move files into folders" — but how do you design rules that handle ambiguity? The answer: you don't design them alone. You design them in conversation with a General Agent, and the best categorization systems aren't designed perfectly upfront. They're discovered through errors and corrections.

---

## Prerequisites

This lesson builds on Lessons 1–2. You should have:

- Completed the survey workflow from Lesson 1 (you have `FILE-INVENTORY.md` with your actual file data)
- Created a backup from Lesson 2 (your important files are safely copied)

If you skipped ahead, go back and complete the checkpoints. The safety-first pattern protects you from mistakes, and you need real file data for this to be meaningful.

---

## The Conversation

Open Claude Code and start the collaboration:

**You:**

> Help me organize my Downloads folder. Let's create a categorization system that works for my files.

**Claude Code:**

> I can see you have 487 files in ~/Downloads. Based on the extensions, here's what I'd suggest:
>
> | Category  | File Types          | Count |
> | --------- | ------------------- | ----- |
> | Documents | pdf, doc, docx, txt | 127   |
> | Images    | jpg, png, gif       | 89    |
> | Code      | py, js, html, css   | 34    |
> | Misc      | everything else     | 237   |
>
> Does this categorization work for you, or would you like to adjust it?

**You:**

> That looks mostly right. But wait — where would .csv files go? Those are spreadsheets, not documents.

**Claude Code:**

> You're right. I had `.csv` grouped with documents since CSV is technically a text format. But functionally they're spreadsheets. Let me create a separate spreadsheet category.
>
> Updated categories:
>
> | Category     | File Types          | Count |
> | ------------ | ------------------- | ----- |
> | Documents    | pdf, doc, docx, txt | 98    |
> | Spreadsheets | xlsx, csv           | 29    |
> | Images       | jpg, png, gif       | 89    |
> | Code         | py, js, html, css   | 34    |
> | Misc         | everything else     | 237   |
>
> Should I document these rules in a rules.md file so we can reuse them later?

That correction matters. The agent classified by file format (CSV is text). You classified by function (CSV is a spreadsheet). You were right — because you know how you _use_ the files. The agent knows what they _are_. When you catch these mistakes and the agent adjusts, the rules get smarter.

**You:**

> Yes, create rules.md. Then test on ONE file first before doing all of them.

**Claude Code:**

> Created rules.md with the categorization logic and edge case handling.
>
> Now testing with a single file. Moving budget-2026.pdf to documents/...
>
> ```
> Moved: budget-2026.pdf → organized/documents/
> Verified: File exists in destination
> Verified: File no longer in source
> ```
>
> Test passed. Ready to proceed with the remaining 486 files?

**You:**

> Looks good. Now do the rest and show me a summary when done.

**Claude Code:**

> Organization complete. Here's the summary:
>
> | Category      | Files Moved |
> | ------------- | ----------- |
> | documents/    | 97          |
> | spreadsheets/ | 29          |
> | images/       | 89          |
> | code/         | 34          |
> | misc/         | 237         |
>
> **Total**: 486 files organized
>
> Updated ORGANIZER-LOG.md with the full activity history.
>
> Would you like me to show you any category in detail, or are we done?

Here's what happened to your folder structure:

```
BEFORE:
Downloads/
├── report.pdf
├── photo.jpg
├── budget.xlsx
├── script.py
└── mystery-file.bin

AFTER:
Downloads/
└── organized/
    ├── documents/
    │   └── report.pdf
    ├── images/
    │   └── photo.jpg
    ├── spreadsheets/
    │   └── budget.xlsx
    ├── code/
    │   └── script.py
    └── misc/
        └── mystery-file.bin
```

The transformation is visual. Flat chaos became categorized structure.

But don't celebrate yet. Look at that summary table again. **237 files in `misc/`.** That's 49% of your files dumped into an "everything else" bucket. If half your files are "miscellaneous," your categorization system has a problem.

This is the honest part most tutorials skip. Extension-based rules are a starting point, not a solution. Let's fix it.

---

## The Misc Problem: When Half Your Files Are "Everything Else"

**You:**

> 237 files in misc/ is way too many. Help me understand what's actually
> in there. Can you break down the misc/ folder by what these files
> actually ARE?

**Claude Code:**

> Let me analyze the misc/ folder by extension and content.
>
> ```
> .dmg/.exe installers:  43  (app installers, probably safe to delete)
> .zip archives:         38  (compressed folders, need to check contents)
> .mp4/.mov videos:      27  (screen recordings, downloaded videos)
> .eml/.msg emails:      19  (saved email messages)
> .json/.xml data:       15  (configuration and data export files)
> No extension:          12  (README files, scripts, unknown)
> Other (94 types):      83  (scattered: .sketch, .fig, .key, .psd...)
> ```
>
> The installers alone are 43 files. Want me to create subcategories
> for the obvious groups?

**You:**

> Yes. Create installers/, media/, and archives/ categories.
> Move the email files into documents/. For the rest, can you
> look INSIDE the files to figure out what they are?

**Claude Code:**

> I'll check the no-extension files and try to identify them by content.
>
> [Runs: file organized/misc/README]
> [Runs: file organized/misc/Makefile]
> [Runs: file organized/misc/data-export]
>
> Results:
> - 8 of the 12 no-extension files are actually text/code files
> - 3 are binary data files
> - 1 is a renamed PDF (someone saved it without .pdf extension)
>
> Moved 8 text files → code/
> Moved 1 mislabeled PDF → documents/
>
> Updated misc/ breakdown:
> ```
> Before: 237 files (49% of total)
> After:   86 files (18% of total)
> ```
>
> The remaining 86 files are genuinely miscellaneous — design files,
> one-off formats, and binary data. That's a reasonable misc/ bucket.

**The lesson:** Extension-based rules are layer one. Content-based analysis is layer two. When your "misc" bucket is too large, don't accept it — dig deeper. A good categorization system should have less than 20% of files uncategorized.

---

## When the Agent Gets It Wrong

Here's something the textbook version of this conversation doesn't show you. Sometimes the agent gets it wrong — and not in the polite, easy-to-fix way.

### Scenario: Silent Miscategorization

After the batch operation, you browse `organized/documents/` and count the files. 97. But your FILE-INVENTORY.md from Lesson 1 said you had 127 documents. Where are the other 30?

```
You: Wait — I should have 127 documents but there are only 97 in
documents/. Where are the missing 30?
```

```
Claude Code: Let me check...

[Runs: find organized/ -iname "*.doc" -o -iname "*.txt" | wc -l]
[Runs: find organized/misc/ -iname "*.doc" -o -iname "*.txt"]

Found the issue. 30 files have uppercase extensions (.PDF, .DOCX, .TXT)
and my rules only matched lowercase. These fell through to misc/.

- 22 files with .PDF → should be in documents/
- 5 files with .DOCX → should be in documents/
- 3 files with .TXT → should be in documents/

Moving them now and updating rules.md to use case-insensitive matching.
```

This is a real bug. Case-sensitive matching is one of the most common failures in file categorization, and the agent didn't catch it during the initial rule design. You caught it because you *verified the numbers*. This is Principle 3 in action — verification caught an error that looked like success.

### Scenario: The Agent Suggests a Category You Didn't Think Of

```
Claude Code: I notice 43 of your "misc" files are .dmg and .exe installers.
These are application installers that you probably don't need anymore
once the apps are installed. Would you like a separate "installers"
category? That would let you easily delete them to free up space.
```

The agent spotted a pattern you missed. This is the collaboration at work — neither you nor the agent alone would reach the best result.

**Why does `rules.md` matter more than the organized folders?** Next month your Downloads will fill up again. The folders will be outdated. But `rules.md` — the logic for _how_ to organize — is reusable forever. The rules are the product. The organized folders are just the output.

---

## The Pattern

Notice the structure of that conversation:

```
1. "Help me [goal]. Let's [approach]."
   → AI proposes initial solution

2. "That's good, but [refinement]."
   → You adjust based on your needs

3. "Document the rules so we can reuse them."
   → Logic becomes persistent state

4. "Test on ONE file first."
   → Small verification before scale

5. "Show me what you'll do before doing it."
   → Dry run — observability before action

6. "Now do the rest and show me a summary."
   → Batch execution with observability
```

This pattern works for any organization task. The specific categories change. Maybe you're organizing photos by date, or code files by project. But the workflow stays the same.

### The Dry-Run Habit

Step 5 deserves special attention. Before the agent moves hundreds of files, ask it to show you what it _would_ do:

```
Before you move everything, run this in dry-run mode — list exactly
what files you'll move and where, without actually doing it.
```

The agent will produce a plan like:

```
meeting-notes.docx     → organized/documents/
quarterly-data.xlsx    → organized/spreadsheets/
vacation-photo.jpg     → organized/images/
cleanup-script.py      → organized/code/
mystery-file.bin       → organized/misc/
... (481 more files)

No files moved yet. Want me to proceed?
```

A dry run makes the agent's intentions visible before they become irreversible. You can scan the list and catch problems — a file headed to the wrong folder, a naming conflict, something that should be skipped — while it's still just a plan on screen.

The single-file test (step 4) checks that the _mechanism_ works. The dry run (step 5) checks that the _decisions_ are right. Both matter.

---

## Your Workspace After This Lesson

Check what Claude Code created:

```bash
ls -la file-organizer/
```

**Output:**

```
drwxr-xr-x  backup/
-rw-r--r--  FILE-INVENTORY.md
-rw-r--r--  ORGANIZER-LOG.md
drwxr-xr-x  organized/
-rw-r--r--  rules.md
```

Examine the organized directory:

```bash
ls organized/
```

**Output:**

```
code  documents  images  misc  spreadsheets
```

Read your rules:

```bash
cat rules.md
```

**Output:**

```markdown
# File Organization Rules

## Layer 1: Extension-Based (case-insensitive)
| Extension                         | Destination    |
| --------------------------------- | -------------- |
| .pdf, .doc, .docx, .txt, .rtf     | documents/     |
| .xlsx, .csv, .ods                 | spreadsheets/  |
| .jpg, .png, .gif, .svg, .webp     | images/        |
| .mp4, .mov, .avi, .mkv            | media/         |
| .py, .js, .sh, .html, .css        | code/          |
| .dmg, .exe, .msi, .pkg            | installers/    |
| .zip, .tar, .gz, .rar             | archives/      |

## Layer 2: Content-Based (for no-extension and ambiguous files)
- Use `file` command to detect actual type
- Text/code files without extension → code/
- Mislabeled files (PDF saved without .pdf) → correct category
- Email exports (.eml, .msg) → documents/

## Edge Cases
- ALL extension matching is case-insensitive (.PDF = .pdf)
- Hidden files (starting with .) → skip
- Duplicate filename → append timestamp
- Filenames with spaces, parentheses, copy indicators → normalize before matching
- Misc/ target: less than 20% of total files

## History
- Version: 2.0
- Created: 2026-02-12
- Last applied: 2026-02-12
- Based on: FILE-INVENTORY.md analysis
- Changes: v1.0 initial rules; v1.1 case-insensitive matching;
  v2.0 added Layer 2 content analysis, installers/, media/, archives/
```

Your organization logic is now permanent. The next time your Downloads fills up, you have documented rules ready to apply.

---

## ✅ Checkpoint: Do This Now

Stop reading. Open Claude Code and organize your folder using the collaborative pattern.

Use this prompt:

```
Help me organize my [Downloads/Documents/Desktop] folder. Analyze what's
there and suggest categories based on MY actual files. Let me refine the
rules before we proceed. Document final rules in file-organizer/rules.md.
Test on ONE file first, then do the rest.
```

You should now have:

- `file-organizer/rules.md` with your categorization rules
- `file-organizer/organized/` with categorized subfolders
- Updated `file-organizer/ORGANIZER-LOG.md`

Review the organized folders. Did every file land in the right place? If not, tell the agent what went wrong and let it fix the rules.

Your folders are organized. Your rules are documented. But here's what you might be thinking: "I have to do this AGAIN next month when more files pile up." You're right. Typing the same prompts repeatedly is exactly the kind of tedious work agents should eliminate. What if this entire workflow became a single reusable script?

---

## 🔄 Session Management Note

You've now completed three lessons worth of work. If your Claude Code context is getting long, this is a natural point to start a fresh session.

**Why:** Remember the "Kitchen Sink Session" failure pattern from Chapter 6? Three lessons of exploration, backup, and organization creates a lot of context. Your rules and inventory are saved in files, so a fresh session can pick them up.

**How to reset cleanly:**

```
Commit our work so far with a message like "Complete file survey,
backup, and organization — Lessons 1-3"
```

Then start a new session for Lesson 4. Your `rules.md`, `FILE-INVENTORY.md`, and `ORGANIZER-LOG.md` carry your context forward — in files, not memory.

If your session still feels responsive, keep going. This is guidance, not a rule.

---

## Try With AI

**Rule Conflict Resolution:**

```
I have files that could belong to multiple categories. "project-budget-Q4.xlsx"
is both a spreadsheet AND a project document. Help me design rules that handle
these conflicts. What should take priority — file type or project membership?
```

**What you're learning:** Rule conflict resolution. Real categorization systems have ambiguity. You're learning to design rules that handle files that don't fit neatly into one category.

**Edge Case Discovery:**

```
What edge cases might break simple extension-based categorization?
Show me examples of files that could cause problems.
```

**What you're learning:** Defensive design. AI reveals tricky scenarios like `file.backup.pdf` (multiple dots), `README` (no extension), or `data.CSV` (case sensitivity).

**Rule Refinement:**

```
My rules.md categorizes by extension, but I have files from specific
projects that should stay together regardless of type. How can I add
project-based rules that take priority over extension rules?
```

**What you're learning:** Rule precedence. AI explains how to layer rules (check project name first, then fall back to extension), preparing you for more sophisticated automation.
