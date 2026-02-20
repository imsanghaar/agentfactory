# Output Format Examples and Specifications

This document provides detailed format specifications and examples for DOCX, Markdown, and PDF outputs.

---

## DOCX Format (Printable - Recommended)

### Structure

```
[Header Section]
Title: Agent Factory Fundamentals: Building Digital Full-Time Equivalents (FTEs)
Exam Code: L1: P1-AGFF
90 Questions | 120 Minutes

[Questions Section]
1) The 'Agent Factory Thesis' primarily reframes the AI business opportunity as:
A. Manufacturing digital employees rather than selling traditional software
B. Shipping UI features rather than codifying organizational expertise
C. Selling token bundles rather than selling recurring subscriptions
D. Optimizing chat workflows rather than deploying autonomous systems

2) Which of the following best describes the core value proposition?
A. Reducing software licenses by 50%
B. Replacing human expertise with commodity AI
C. Codifying expert knowledge into autonomous, repeatable systems
D. Increasing chat interface sophistication

[...Continue through Q90...]

---

[Answer Key Section]
Reference this section after completing the quiz to check your answers.

1-A, 2-C, 3-B, 4-A, 5-B, 6-B, 7-B, 8-B, 9-A, 10-D
11-A, 12-A, 13-A, 14-C, 15-C, 16-A, 17-B, 18-D, 19-C, 20-C
21-B, 22-C, 23-A, 24-D, 25-B, 26-C, 27-A, 28-B, 29-C, 30-A
[...grouped by 10 for easy scanning...]

---

[Explanations Section]
Q1 - Correct Answer: A
Source: Agent Factory Fundamentals

The Agent Factory Thesis posits that instead of selling software licenses,
companies can manufacture digital full-time equivalents (FTEs)...

---

Q2 - Correct Answer: C
Source: Agent Manufacturing Principles

Manufacturing agents transforms domain expertise into codified systems...

---
[...Continue for all questions...]
```

### Formatting Rules

- **Font**: Professional serif (Calibri 11pt) or sans-serif
- **Question numbering**: 1), 2), 3)... (parenthesis after number)
- **Options**: Each on separate line: A., B., C., D. (period after letter)
- **Spacing**: Single-space options, blank line between questions
- **Answer Key**: Grouped by 10 for readability, 10 answers per line
- **Explanations**: Separate section after answer key, full paragraph per question

---

## Markdown Format (Version Control Friendly)

### Structure

```markdown
# Agent Factory Fundamentals Assessment

**Source Code:** P1-AGFF
**Questions:** 90
**Duration:** 120 minutes
**Content Type:** Conceptual
**Difficulty Tier:** T2 (Intermediate)

---

## Questions

**Q1.** The 'Agent Factory Thesis' primarily reframes the AI business opportunity as:

**A.** Manufacturing digital employees rather than selling traditional software

**B.** Shipping UI features rather than codifying organizational expertise

**C.** Selling token bundles rather than selling recurring subscriptions

**D.** Optimizing chat workflows rather than deploying autonomous systems

---

**Q2.** Which of the following best describes the core value proposition?

**A.** Reducing software licenses by 50%

**B.** Replacing human expertise with commodity AI

**C.** Codifying expert knowledge into autonomous, repeatable systems

**D.** Increasing chat interface sophistication

---

[Continue for all questions...]

## Answer Key

| Q#  | Answer | Source Section                 | Bloom Level | Question Type          | Difficulty |
| --- | ------ | ------------------------------ | ----------- | ---------------------- | ---------- |
| 1   | A      | Agent Factory Fundamentals     | Understand  | Conceptual Distinction | Medium     |
| 2   | C      | Agent Manufacturing Principles | Understand  | Specification Design   | Medium     |
| 3   | B      | Core Principles                | Apply       | Decision Matrix        | Medium     |
| ... | ...    | ...                            | ...         | ...                    | ...        |

## Explanations

### Q1

**Correct Answer: A**

The Agent Factory Thesis posits that instead of selling software licenses,
companies can manufacture digital full-time equivalents (FTEs)—AI agents that
codify domain expertise and perform specific professional tasks.

**Source:** Agent Factory Fundamentals (Section: Business Model Reframing)
**Why other options are wrong:**

- B: This describes UI shipping, not the core reframing
- C: Token bundles are a pricing mechanism, not the thesis
- D: Chat workflows are a feature, not the business model

---

### Q2

**Correct Answer: C**

Manufacturing agents transforms domain expertise into codified, repeatable systems
that can operate autonomously within defined constraints.

**Source:** Agent Manufacturing Principles
**Why other options are wrong:**

- A: Software economics remain, only licensing model changes
- B: Expertise is preserved, not replaced
- D: Interface sophistication is irrelevant to value proposition

---

[Continue for all questions...]
```

### Formatting Rules

- **Metadata**: YAML-style key-value pairs at top
- **Questions**: Bold "Q#." format with full question text
- **Options**: Lettered A-D with bold and period: **A.**, **B.**, **C.**, **D.** (prevents pandoc list interpretation)
- **Answer Key Table**: Includes source section, Bloom level, question type, difficulty
- **Explanations**: Section per question with correct answer highlighted, rationale, and why other options are wrong

---

## PDF Format (Read-Only Distribution)

- Generated from Markdown format
- Converted via Markdown → DOCX → PDF pipeline
- Optimized for printing and student distribution
- Preserves all formatting, tables, and structure from Markdown

---

## Key Differences

| Aspect            | DOCX                        | Markdown                  | PDF                       |
| ----------------- | --------------------------- | ------------------------- | ------------------------- |
| **Best For**      | Printing, formal assessment | Version control, editing  | Final delivery, read-only |
| **Editability**   | MS Word required            | Text editor, easy diff    | Not editable              |
| **Metadata**      | Embedded in document        | YAML frontmatter          | Embedded in PDF           |
| **Answer Key**    | Compact, 10 per line        | Table format with details | Same as source format     |
| **Distribution**  | Email, hard copy            | Git, web publishing       | Email, LMS upload         |
| **Accessibility** | Screen reader compatible    | Plain text, accessible    | PDF accessibility varies  |

---

## Quality Specifications for All Formats

- **Question clarity**: Each question standalone, no ambiguity
- **Option parity**: All 4 options within 0.8x-1.2x of mean word count (length parity). Target 12-18 words per option.
- **Specificity balance**: All options at similar detail level
- **Source references**: Every question maps to lesson section
- **Bloom alignment**: Distribution matches content type (25% Analyze, 25% Remember/Understand, etc.)
- **No consecutive patterns**: Max 3 consecutive same-letter answers
- **Position distribution**: 25% A, 25% B, 25% C, 25% D (±5% acceptable)
