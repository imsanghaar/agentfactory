---
slug: /General-Agents-Foundations/general-agents/cowork-built-in-skills
title: "Built-in Skills: Documents, Spreadsheets, Presentations"
sidebar_position: 28
chapter: 3
lesson: 28
duration_minutes: 18
chapter_type: Practical
running_example_id: built-in-skills

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Understanding and using Cowork's built-in Skills for common document formats (docx, xlsx, pptx, pdf)"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Claude Cowork Built-in Skills"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can use Cowork's built-in document Skills for reading, editing, and creating docx, xlsx, pptx, and pdf files"

learning_objectives:
  - objective: "Use built-in Skills for Word document (docx) processing"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successful creation or modification of a Word document"
  - objective: "Use built-in Skills for Excel spreadsheet (xlsx) processing"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successful analysis or modification of a spreadsheet"
  - objective: "Use built-in Skills for PowerPoint (pptx) creation and editing"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successful creation or modification of a presentation"
  - objective: "Use built-in Skills for PDF text extraction and understanding"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successful extraction and use of content from PDF files"
  - objective: "Determine when to use built-in Skills vs. custom Skills"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Scenario-based selection of appropriate approach"

# Cognitive load tracking
cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (document Skills, format preservation, tracked changes, formula awareness, PDF extraction, Skill selection) - within A2 limit of 7 ✓"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Create custom Skills that extend or combine built-in document capabilities"
  remedial_for_struggling: "Focus on one document format at a time, starting with simple docx creation"

# Generation metadata
generated_by: "content-implementer v2.0.0"
created: "2025-01-22"
last_modified: "2025-01-22"
git_author: "Claude Code"
workflow: "manual"
version: "1.0.0"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 10
  session_title: "Practical Skills and the Code-vs-Cowork Decision"
  key_points:
    - "Built-in Skills (docx, xlsx, pptx, pdf) are pre-installed — students do not need to create or configure them"
    - "The Capability Matrix table is the key reference: pdf is read-only (no create/edit), tracked changes only work in docx, formulas only in xlsx"
    - "Built-in Skills handle format mechanics while custom Skills handle domain reasoning — combining both is where Cowork becomes most powerful"
    - "Each format has specific limitations students must know: macros not supported in docx, Power Query not preserved in xlsx, animations lost in pptx, password-protected pdfs unreadable"
  misconceptions:
    - "Students think built-in Skills can create PDFs — the pdf Skill is extraction-only (read), not creation"
    - "Students assume Claude can execute macros or VBA in Word documents — it cannot; macros are ignored"
    - "Students confuse built-in Skills with custom Skills — built-in handle file format operations, custom encode domain-specific reasoning"
  discussion_prompts:
    - "Which document format do you work with most often, and what is one repetitive task in that format that a built-in Skill could automate?"
    - "When would you combine a built-in Skill (like docx) with a custom Skill (like 'legal contract review'), and why is the combination more valuable than either alone?"
  teaching_tips:
    - "Project the Capability Matrix table and have students identify which cells would matter most for their daily work — this personalizes an abstract table"
    - "Run a live demo: create a simple docx or xlsx using a prompt from the lesson, then show the actual output to demonstrate format fidelity"
    - "Use the 'When to Use Built-in vs. Custom Skills' section as a sorting exercise — give students 5 scenarios and have them categorize each"
    - "Highlight the tracked changes feature in docx as a practical collaboration bridge — Claude edits with track changes so the human reviews changes, not rewrites"
  assessment_quick_check:
    - "Which built-in Skill is read-only and cannot create new files?"
    - "Name one limitation of the xlsx Skill when working with complex spreadsheets."
    - "Give an example of combining a built-in Skill with a custom Skill for a real task."

# Legacy compatibility (Docusaurus)
prerequisites:
  - "Completion of Lesson 27: Safety, Limitations, and What's Coming"
  - "Working Claude Cowork installation"
  - "Basic familiarity with Office documents"
---

# Built-in Skills: Documents, Spreadsheets, Presentations

Earlier in this chapter, you learned how to create custom Skills—encoded expertise that teaches Claude specific procedures. But Cowork also comes with **built-in Skills** for common document formats. These are pre-installed capabilities that work out of the box.

---

## What Built-in Skills Are

Built-in Skills are domain-specific capabilities Anthropic has developed and optimized:

| Skill    | File Types | What It Does                             |
| -------- | ---------- | ---------------------------------------- |
| **docx** | .docx      | Read, create, and edit Word documents    |
| **xlsx** | .xlsx      | Read, analyze, and modify spreadsheets   |
| **pptx** | .pptx      | Create and edit PowerPoint presentations |
| **pdf**  | .pdf       | Extract text and structure from PDFs     |

These Skills are pre-installed—you don't need to create or configure them. They're automatically available when working with these file types in Cowork.

---

## The docx Skill: Word Documents

**Capabilities:**

- Create new Word documents with proper formatting
- Edit existing documents while preserving structure
- Work with tracked changes
- Maintain styles, headers, footers, and page layouts
- Add tables, lists, and formatting

**Example prompt:**

> "Create a Word document called 'meeting-notes.docx' with:

- Title: 'Q1 Planning Meeting - January 15, 2026'
- Attendees section with placeholder names
- Agenda items: Budget Review, Timeline Discussion, Resource Allocation
- Action items table with columns: Task, Owner, Due Date
- Professional formatting with headers and bullet points"

**What Claude does:**

1. Creates the .docx file
2. Adds formatted content with proper document structure
3. Applies styles for headings, lists, and tables
4. Produces a file you can open directly in Word

**Advanced operations:**

> "Open 'proposal-draft.docx', find all instances of 'Q1 2026' and replace with 'Q2 2026'. Add a tracked changes comment explaining the update. Preserve all existing formatting."

**Tracked changes support:** When editing existing documents, Claude can use Word's tracked changes feature so you can review modifications before accepting them.

**Limitations:**

- Complex layouts (newsletters, brochures) may not preserve perfectly
- Macros and VBA are not executed or modified
- Very large documents (>100 pages) may have processing delays

---

## The xlsx Skill: Spreadsheets

**Capabilities:**

- Read spreadsheet data intelligently
- Analyze data and generate insights
- Add or modify rows and columns
- Create formulas that reference existing data
- Generate charts and visualizations
- Preserve formatting and existing formulas

**Example prompt:**

> "Read 'sales-data.xlsx'. Analyze the sales figures and:

- Calculate total sales by region
- Identify top 5 products by revenue
- Find month-over-month growth rate
- Add a new tab called 'Summary' with this analysis in a clean table
- Create a bar chart showing sales by region"

**What Claude does:**

1. Reads the spreadsheet data
2. Analyzes patterns and calculates metrics
3. Creates a new worksheet with the summary
4. Generates a chart based on the data
5. Updates the file while preserving original data

**Formula awareness:** Claude understands spreadsheet formulas and can:

- Explain what existing formulas do
- Create new formulas using appropriate functions
- Reference cells correctly when adding data
- Avoid breaking formula dependencies

**Best practices:**

- Always back up spreadsheets before bulk modifications
- Test formula changes on a small sample first
- Ask Claude to explain formulas you don't understand

**Limitations:**

- Very complex spreadsheets with thousands of formulas may be slow
- Custom functions and add-ins are not executed
- Power Query and Power Pivot operations may not preserve perfectly

---

## The pptx Skill: Presentations

**Capabilities:**

- Create presentation decks from outlines
- Add and arrange slides
- Format text, shapes, and images
- Apply consistent themes
- Add speaker notes

**Example prompt:**

> "Create a PowerPoint presentation called 'product-update.pptx' with:

- Title slide: 'Q1 Product Roadmap Update'
- Overview slide with key achievements
- 3 feature spotlight slides with bullet points
- Timeline slide showing Q2 plans
- Conclusion slide with next steps
- Use a professional design with consistent colors throughout"

**What Claude does:**

1. Creates the presentation file
2. Adds slides with proper layouts
3. Formats content consistently
4. Applies a theme with unified styling
5. Includes speaker notes for key points

**Working with existing presentations:**

> "Open 'deck-template.pptx'. Update the data slide with new figures from 'q1-results.xlsx'. Add two slides at the end summarizing key takeaways. Match the existing design style."

**Limitations:**

- Complex animations and transitions may not preserve
- Embedded videos and media may need manual re-linking
- Highly custom slide layouts may not replicate perfectly

---

## The pdf Skill: PDF Content

**Capabilities:**

- Extract text content from PDFs
- Identify document structure (headings, sections)
- Understand tables and data in PDFs
- Work with both text-based and scanned PDFs (OCR)

**Example prompt:**

> "Read 'contract-2024.pdf'. Extract and summarize:

- Key terms and obligations
- Payment schedule and amounts
- Important dates and deadlines
- Any unusual or concerning clauses
  Organize this into a structured summary document."

**What Claude does:**

1. Extracts text from the PDF
2. Identifies document structure and sections
3. Organizes key information logically
4. Creates a readable summary with proper formatting

**PDF limitations:**

- Images within PDFs are described, not analyzed visually
- Highly formatted layouts may lose some structure
- Password-protected PDFs cannot be read
- Some PDFs with complex formatting may have extraction errors

---

## When to Use Built-in vs. Custom Skills

**Use built-in Skills when:**

- Working with standard document formats
- You need format preservation
- The task involves reading/writing Office documents
- You want reliable, tested functionality

**Use custom Skills when:**

- You have domain-specific procedures
- You need consistent reasoning patterns
- Built-in capabilities don't cover your use case
- You want to encode expertise that applies across document types

**Example combination:**

- Built-in docx Skill for Word document creation
- Custom Skill for "legal contract review" reasoning
- Combined: Claude creates a properly formatted document AND applies legal analysis expertise

---

## Capability Matrix

| Task                    | docx    | xlsx | pptx    | pdf |
| ----------------------- | ------- | ---- | ------- | --- |
| **Read content**        | ✓       | ✓    | ✓       | ✓   |
| **Create new**          | ✓       | ✓    | ✓       | ✗   |
| **Edit existing**       | ✓       | ✓    | ✓       | ✗   |
| **Format preservation** | ✓       | ✓    | ✓       | N/A |
| **Formulas**            | N/A     | ✓    | N/A     | N/A |
| **Charts/visuals**      | Limited | ✓    | Limited | N/A |
| **Tracked changes**     | ✓       | N/A  | N/A     | N/A |

---

## Best Practices

**For documents (docx):**

- Use tracked changes when editing important documents
- Describe the desired structure clearly
- Specify formatting requirements explicitly

**For spreadsheets (xlsx):**

- Always back up before bulk operations
- Ask Claude to explain formulas before applying them
- Test on a small sample when modifying large datasets

**For presentations (pptx):**

- Provide an outline for better structure
- Specify design requirements (colors, fonts, themes)
- Review generated slides for consistency

**For PDFs:**

- Understand that extraction may have errors
- Verify important information against the original
- Use PDFs as reference, not as editable source

---

## Try With AI

\*\*🔍 Explore Built-in Skills:"

> "Choose a document format I work with regularly (Word, Excel, PowerPoint, or PDF). Create a simple example file and ask Claude to do something useful with it using the built-in Skill. What works well? What are the limitations?"

**What you're learning:** Hands-on capability assessment—understanding what built-in Skills can actually do by testing them. Direct experience is more valuable than reading documentation.

\*\*💡 Combine Built-in and Custom:"

> "Design a workflow that uses both a built-in Skill and a custom Skill. For example: Use the docx Skill to create a document, combined with a custom Skill for domain-specific content generation (like 'technical documentation' or 'marketing copy')."

**What you're learning:** Skill composition—understanding how to combine built-in capabilities with custom expertise. This combination is where Cowork becomes most powerful.

\*\*🏗️ Test Real-World Scenarios:"

> "Pick a real document I've worked with recently. How could Claude's built-in Skills have helped? Recreate a simplified version and test. What would have saved me time?"

**What you're learning:** Practical application—connecting Cowork's capabilities to your actual work. Identifying real opportunities to apply these Skills makes the learning concrete.

---

## What's Next

You've explored Cowork's interface, workflows, browser integration, connectors, and built-in Skills. The final lesson in this Cowork section brings everything together with a decision framework—helping you choose between Claude Code and Claude Cowork for any given task, and understanding when to use both together.
