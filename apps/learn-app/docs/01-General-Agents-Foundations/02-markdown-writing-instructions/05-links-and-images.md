---
title: "Links and Images"
description: "Adding hyperlinks and images to markdown documents for richer communication"
sidebar_label: "Links and Images"
sidebar_position: 5
chapter: 2
lesson: 5
duration_minutes: 35
proficiency: "A2"
concepts: 3

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
# Not visible to students; enables competency assessment and differentiation
skills:
  - name: "Creating Links"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can create working links to documentation and other resources in markdown"

  - name: "Adding Images"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can add images to markdown documents for README screenshots, diagrams, and logos"

  - name: "Using Text Emphasis"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Content Creation"
    measurable_at_this_level: "Student can use bold and italic formatting for emphasis in specifications"

learning_objectives:
  - objective: "Create working hyperlinks to documentation and external resources"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Exercise includes at least one valid link that renders correctly"

  - objective: "Add images to markdown documents for visual communication (screenshots, diagrams, logos)"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Exercise includes at least one properly formatted image"

  - objective: "Apply bold and italic formatting to emphasize key terms and requirements"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Exercise uses emphasis formatting appropriately for critical terms"

cognitive_load:
  new_concepts: 3
  assessment: "3 new concepts: (1) link syntax, (2) image syntax, (3) emphasis syntax. Well within A2 limit of 7."
  mitigation_strategy: "Image syntax mirrors link syntax (just adds !). Emphasis uses simple asterisk patterns (*italic*, **bold**)."

differentiation:
  extension_for_advanced: "Research URL encoding for special characters in links; explore relative vs absolute image paths; learn strikethrough (~~text~~)"
  remedial_for_struggling: "Practice link syntax with provided URLs before finding own; use placeholder image services to avoid path issues"

teaching_guide:
  lesson_type: "core"
  session_group: 3
  session_title: "Links, Images & Complete Specifications"
  key_points:
    - "Link [text](url) and image ![alt text](url) syntax differ by only the ! prefix — teach as a pair so students leverage pattern recognition"
    - "Descriptive link text matters for AI: '[Python documentation](...)' provides context, '[click here](...)' provides none — AI cannot infer destination from vague text"
    - "Bold (**must**) vs italic (*recommended*) signals requirement priority to AI — this semantic distinction directly affects implementation decisions"
    - "This lesson completes the Task Tracker spec started in Lesson 2 — celebrate the achievement of building a full specification"
  misconceptions:
    - "Students write 'click here' as link text — AI agents and screen readers cannot infer the destination from generic text"
    - "Students forget the ! prefix for images, accidentally creating a link instead of an embedded image — 'show it here' (!) vs 'take me there' (no !)"
    - "Students overuse bold emphasis making everything stand out equally — bold loses its signaling power when every other word is bold"
  discussion_prompts:
    - "If you were an AI reading a spec and saw **must** vs *recommended*, how would you prioritize your implementation work differently?"
    - "Why is descriptive alt text important even though modern AI can 'see' images? Think about how specs are processed as plain text files in coding workflows."
  teaching_tips:
    - "Teach link and image syntax back-to-back — the ! prefix is the only difference, and students learn both faster when presented as a pair"
    - "Use the 'Common Image Mistakes' section as a live error-spotting exercise before revealing the answers"
    - "End with the 'Your First Complete Specification' section as a genuine celebration — students built a real spec across 4 lessons"
    - "Connect the full chapter arc: Lesson 1 explained WHY markdown matters, Lessons 2-5 taught HOW — the finished Task Tracker spec is proof they can write specifications for AI"
  assessment_quick_check:
    - "Ask students to write the syntax for a link and an image from memory, then identify the single-character difference"
    - "Give students a sentence with **bold** and *italic* terms and ask which are hard requirements vs recommendations"
---

# Links and Images

## Connecting Documents to the World

You've learned how to structure documents with headings, organize information with lists, and show code with fenced blocks. Now you'll learn the final elements that make your markdown documents truly useful: **links** to connect to external resources, **images** to show what things look like, and **emphasis** to highlight critical information.

These are the final syntax elements you need for writing effective markdown files like READMEs, CLAUDE.md instructions, and project documentation.

---

## Concept 1: Links - Connecting to Resources

A document doesn't exist in isolation. You often need to reference **external documentation**, **examples**, or **standards**. Links solve this problem.

### Why Links Matter

When you write "Use Python's requests library," the reader might not know:
- What is the requests library?
- Where do I find it?
- How do I use it?

But if you write "[Use Python's **requests** library](https://requests.readthedocs.io/)," the reader can click through to complete documentation instantly.

### The Syntax

Markdown links follow a simple pattern:

```text
[link text](url)
```

- **link text** = what the reader sees and clicks
- **url** = where the link goes

**What you type:**

```text
Read the [Python documentation](https://docs.python.org/) for help.
```

**What it renders as:**

Read the [Python documentation](https://docs.python.org/) for help.

### Common Mistake: Spaces in URLs Break Links

Beginner mistake:

```markdown
[Wrong link](https://docs.python.org/3/ reference guide)
```

This **won't work** because the space breaks the URL. Either:
1. Use a URL without spaces (recommended):
```markdown
[Python reference](https://docs.python.org/3/reference/)
```

2. Or use URL encoding (replace space with `%20`):
```markdown
[reference guide](https://docs.python.org/3/reference%20guide)
```

For documentation, **always stick with option 1** – find clean URLs without spaces.

### Common Mistake: Vague Link Text

Never use "click here" or "link" as your link text:

**Wrong:**
```markdown
For more information, [click here](https://docs.python.org/).
See the [link](https://requests.readthedocs.io/) for details.
```

**Correct:**
```markdown
See the [Python documentation](https://docs.python.org/) for more information.
The [requests library documentation](https://requests.readthedocs.io/) has examples.
```

**Why this matters for AI**: AI agents use link text to understand what the destination provides *without* following the link. `[Python documentation](...)` tells AI it's a language reference. `[click here](...)` provides zero context—AI must guess or follow the link (which it often can't do).

:::info[Expert Insight]
Links in specifications serve as **context anchors** for AI agents. When you link to library documentation, you're telling the AI: "This is the authoritative source for how this works." Some AI tools can fetch linked URLs to understand APIs better. Even when they can't, the link text provides semantic context—`[requests library](...)` tells the AI you're using the Python requests package, not just making generic "requests."
:::

---

## Example 1: Links to Documentation

Here's how to add helpful links to a README:

```markdown
# Weather App

## Required Libraries
- [Python requests library](https://requests.readthedocs.io/) - for making API calls
- [OpenWeatherMap API](https://openweathermap.org/api) - free weather data source

## Data Format
Data should be formatted as JSON. See the [JSON specification](https://www.json.org/) for details.

## Testing
Verify your app works like the examples in the [OpenWeatherMap docs](https://openweathermap.org/current).
```

Now readers can click through and see:
- How to use the requests library
- Where to get weather data
- What JSON looks like
- What sample outputs should look like

Instead of describing resources, you're pointing directly to them — readers get answers in one click.

:::tip[Pro-Tip: Reference-Style Links]
For documents with many links, markdown supports reference-style links that keep your text clean:

```text
Read the [Python docs][python] and [requests library][requests] documentation.

[python]: https://docs.python.org/
[requests]: https://requests.readthedocs.io/
```

The link definitions go at the bottom of your document. This is optional but useful for long documents.
:::

#### AI Colearning Prompt

> **Explore with your AI**: "I'm writing a README for a project that uses three external libraries. Can you show me how to format a 'Dependencies' section with links to each library's documentation? Use real library URLs."

---

## Concept 2: Images - Showing What Things Look Like

Sometimes words aren't enough. You need to **show** what something looks like. That's where images come in.

### Why Images Matter in Documentation

Images help readers understand:
- **What the UI looks like** - Screenshots show expected interface
- **How data flows** - Diagrams explain system architecture
- **Project branding** - Logos make READMEs professional

### The Syntax (Very Similar to Links!)

Markdown images use almost the same syntax as links, with one difference — an exclamation mark `!` at the start:

```text
![alt text](image-url)
```

- **alt text** = description of the image (shown if image doesn't load, read by screen readers)
- **image-url** = where the image is located (web URL or local file path)

**What you type:**

```text
![Python logo](https://www.python.org/static/community_logos/python-logo.png)
```

**What it renders as:**

![Python logo](https://www.python.org/static/community_logos/python-logo.png)

### Where Images Come From

**Option 1: Online images** (easiest for beginners)
Use a direct image URL from the web:

```markdown
![Example screenshot](https://example.com/screenshot.png)
```

**Option 2: Local images in your project**
Put images in a folder (like `images/` or `assets/`) and reference them with a relative path:

```markdown
![App screenshot](./images/screenshot.png)
```

**For beginners**: Start with online image URLs. Later you can add local images to your projects.

:::info[Expert Insight]
**Important for AI-native development**: Modern AI models are multimodal—they CAN see images when given visual access. However, when AI reads your markdown files as text (common in coding workflows), it only sees the `![alt text](url)` syntax, not the actual image. Descriptive alt text serves two purposes: (1) accessibility for screen readers, and (2) providing context when AI processes your spec as a text file. Instead of `![screenshot](app.png)`, write `![Task list showing 3 pending items with checkboxes](app.png)`.
:::

---

## Example 2: README with Images

Here's how images make READMEs more professional:

```markdown
# Weather Dashboard

![Weather Dashboard Screenshot](https://via.placeholder.com/800x400.png?text=Weather+Dashboard)

## Features
- **Display** current temperature and conditions
- **Show** 7-day forecast
- **Save** favorite locations

## Architecture

![System diagram](https://via.placeholder.com/600x200.png?text=User+→+API+→+Database)
```

A screenshot replaces a paragraph of description, and a diagram can explain architecture faster than any list.

### Common Image Mistakes

**Mistake 1: Forgetting the `!` at the start**

```markdown
[Missing exclamation](image.png)
```

This creates a *link* to the image, not an embedded image. Always use `![...]` for images.

:::tip[Quick Rule: Link vs Image]
- `[text](url)` = **Take me there** (clickable link)
- `![text](url)` = **Show it here** (embedded image)

The `!` means "display this content inline" rather than "navigate to this location."
:::

**Mistake 2: Broken image paths**

```markdown
![Screenshot](./images/screenshot.png)
```

If `screenshot.png` doesn't exist at that path, the image won't show. Check your paths!

**Mistake 3: Too many large images**

Don't embed 20 screenshots in one README. Use images strategically:
- 1 logo/banner at the top
- 1-2 key screenshots showing the app
- Diagrams only when words aren't enough

#### Practice Exercise

> **Ask your AI**: "I'm writing a README for a task management app. I want to show what the main interface looks like and a simple architecture diagram. Suggest what images I should include and help me write descriptive alt text for accessibility."

---

## Concept 3: Text Emphasis - Highlighting What Matters

Sometimes you need to draw attention to specific words or phrases within your text. Markdown provides two levels of emphasis: **bold** for strong emphasis and *italic* for lighter emphasis.

### The Syntax

**Bold** uses double asterisks or double underscores:

**What you type:**

```text
This requirement is **critical** for security.
This requirement is __critical__ for security.
```

**What it renders as:**

This requirement is **critical** for security.

**Italic** uses single asterisks or single underscores:

**What you type:**

```text
See the *optional* configuration section.
See the _optional_ configuration section.
```

**What it renders as:**

See the *optional* configuration section.

**Combined** (bold italic) uses triple asterisks:

**What you type:**

```text
***Never*** store passwords in plain text.
```

**What it renders as:**

***Never*** store passwords in plain text.

### When to Use Each

| Emphasis | Syntax | Use For |
|----------|--------|---------|
| **Bold** | `**text**` | Critical requirements, warnings, key terms |
| *Italic* | `*text*` | Optional items, definitions, slight emphasis |
| ***Both*** | `***text***` | Absolute requirements, security warnings |

### Example: Emphasis in Specifications

```markdown
## Security Requirements

- User passwords **must** be hashed before storage
- API keys should *never* be committed to version control
- All endpoints **require** authentication
- Rate limiting is *recommended* but optional for internal APIs

***Critical***: The database connection string contains credentials
and must be stored in environment variables, not in code.
```

:::info[Expert Insight]
Emphasis helps AI understand priority. When AI sees "**must**" vs "*recommended*", it can distinguish between hard requirements and nice-to-haves. Use bold for requirements that would cause implementation failure if missed, and italic for optional enhancements. This semantic distinction helps AI make appropriate trade-off decisions during implementation.
:::

### Common Emphasis Mistakes

**Mistake 1: Overusing bold**

If everything is bold, nothing stands out. Reserve bold for truly critical items.

**Mistake 2: Inconsistent emphasis for placeholders**

Don't use italic alone to indicate placeholders like *database_name*. Instead, use inline code with angle brackets: `<database_name>`. This is clearer for both humans and AI.

**Mistake 3: Using emphasis instead of structure**

If you're bolding entire sentences to make them stand out, consider using a heading or callout box instead. Emphasis is for words within sentences, not for creating document structure.

---

## Try With AI

Test your understanding of links and images by building a real README section.

### Setup

Use any AI assistant you have access to — ChatGPT, Claude, Gemini, or another tool.

**Prompt 1 (Links Practice):**

```
I'm writing a README for a Python weather app that uses the requests library
and the OpenWeatherMap API. Write me a "Getting Started" section that includes
links to the relevant documentation. Use proper markdown link syntax.
```

**Expected Outcome:**

Your AI will generate a section with properly formatted `[text](url)` links:

- Links pointing to real documentation pages (requests, OpenWeatherMap)
- Descriptive link text (not "click here")
- Clean URLs without spaces

---

**Prompt 2 (Images Practice):**

```
Now add an "Architecture" section to my weather app README. Include a placeholder
image showing the data flow (user → app → API → response). Use proper markdown
image syntax with descriptive alt text.
```

**Expected Outcome:**

Your AI will create an image reference using `![alt text](url)` syntax:

- The `!` prefix that distinguishes images from links
- Descriptive alt text explaining what the diagram shows
- A placeholder URL or reference to a local image path

---

**Prompt 3 (Combined Practice):**

```
Review this README section I wrote and suggest improvements to my links and images:

## Resources
- Python docs: https://docs.python.org
- API info at openweathermap.org

Screenshot:
[app screenshot](screenshot.png)

What markdown syntax errors did I make? Fix them for me.
```

**Expected Outcome:**

Your AI should catch at least three errors:

- Bare URLs without proper link syntax (`https://docs.python.org` needs `[text](url)` format)
- Missing `!` on the image (creates a link instead of an embedded image)
- Vague alt text that doesn't describe the image content

---

## Practice Exercise: Task Tracker App (Part 4 - Links & Images)

**Continuing from Lesson 4**: Open your Task Tracker App specification. You'll now **add links and images** to complete your first full specification.

### Your Task for Lesson 5

Add links and images to finalize your Task Tracker App specification:

**Part 1: Add Resource Links**

Add a "Resources" or "Documentation" section with helpful links:

`````text
## Resources

- [Python Official Documentation](https://docs.python.org/) - Language reference
- [Python File I/O Tutorial](https://docs.python.org/3/tutorial/inputoutput.html) - For saving tasks to file
`````

**Part 2: Add a Placeholder Image (Online URL)**

Add a screenshot placeholder showing what your app's interface looks like:

`````text
## Screenshot

![Task Tracker main menu showing 5 options: Add Task, View Tasks, Mark Complete, Delete Task, and Exit](https://via.placeholder.com/600x300.png?text=Task+Tracker+Menu)
`````

**Part 3: Try a Relative Path (Local Image)**

In AI-native development, AI agents often create images (diagrams, charts) and save them locally. Practice referencing a local image:

1. Create an `images/` folder in your project
2. Add any image file (or create an empty placeholder)
3. Reference it with a relative path:

`````text
## Architecture Diagram

![Data flow diagram showing user input going to Task class then to file storage](./images/architecture.png)
`````

This prepares you for when AI generates diagrams and saves them to your project folder.

:::tip[Pro-Tip: Descriptive Alt Text]
Write alt text that describes what the image SHOWS, not just what it IS. "Task Tracker menu" is vague. "Task Tracker main menu showing 5 options" tells the reader (and AI) exactly what to expect.
:::

### Validation Checklist

Check your completed specification:

1. Has at least one working link to external documentation
2. Links use proper syntax: `[text](url)` with no spaces in URL
3. Link text is descriptive (not "click here" or "link")
4. Has at least one image with descriptive alt text
5. Image uses proper syntax: `![alt text](url)` with `!` at the start
6. Alt text describes what the image shows, not just what it is
7. (Bonus) Includes a relative path image reference like `./images/diagram.png`

---

## Common Mistakes to Avoid

### Mistake 1: Using "Click Here" as Link Text

**Wrong:**
```text
For more info, [click here](https://docs.python.org/).
```

**Correct:**
```text
See the [Python documentation](https://docs.python.org/) for more info.
```

Descriptive link text tells both humans and AI what the destination provides — without needing to follow the link.

### Mistake 2: Forgetting the `!` for Images

**Wrong (creates a link, not an embedded image):**
```text
[App screenshot](screenshot.png)
```

**Correct (embeds the image):**
```text
![App screenshot showing main menu](screenshot.png)
```

Remember: `[text](url)` = **take me there**. `![text](url)` = **show it here**.

### Mistake 3: Overusing Bold Emphasis

**Wrong (everything bold = nothing stands out):**
```text
**All** **users** **must** **log** **in** **before** **accessing** **data**.
```

**Correct (bold only the critical word):**
```text
All users **must** log in before accessing data.
```

Reserve bold for truly critical terms. If everything is emphasized, nothing is.

### Mistake 4: Vague Alt Text on Images

**Wrong:**
```text
![screenshot](app.png)
```

**Correct:**
```text
![Task list showing 3 pending items with checkboxes and due dates](app.png)
```

Alt text should describe what the image **shows**, not just what it **is**. This helps both screen readers and AI agents processing your spec as text.

---

## Why This Matters for AI

When you use links, images, and emphasis correctly in specifications, AI agents can:

1. **Follow documentation links** - Some AI tools fetch linked pages for additional context
2. **Understand resource relationships** - Link text tells AI what each resource provides
3. **Parse alt text for image context** - When reading markdown as text, AI relies on alt text for image understanding
4. **Generate appropriate placeholders** - When AI creates documentation, it follows your link/image patterns
5. **Distinguish priority levels** - Bold (**must**) vs italic (*recommended*) helps AI decide what to implement first vs what is optional

Together, these elements transform a basic specification into a rich brief — one that gives AI context, examples, and clear priorities to work from.

:::info[Expert Insight]
Links, images, and emphasis each add a different dimension to your specifications. Links provide **context anchors** — connecting your spec to authoritative sources that AI can reference. Images provide **visual contracts** — showing what the result should look like. Emphasis provides **priority signals** — telling AI which requirements are non-negotiable and which are nice-to-have. Together, these elements transform a basic specification into a comprehensive brief that guides AI toward accurate, well-prioritized implementations.
:::

:::note[How AI Processes Images]
Modern AI models are multimodal and can view images directly when given visual access. However, in text-based workflows (like reading spec files), AI sees only the alt text and filename. Write descriptive alt text that works for both scenarios—it helps accessibility AND provides context regardless of how your document is processed.
:::

---

## Bonus: Additional Markdown Elements

Before we wrap up, here are additional markdown elements you'll encounter in real projects.

### Tables — Comparing Options

Tables are useful when you need to compare features, list configurations, or show structured data:

```text
| Feature        | Free Plan | Pro Plan |
|----------------|-----------|----------|
| Task limit     | 10        | Unlimited|
| Collaboration  | No        | Yes      |
| Export to PDF   | No        | Yes      |
```

**What it renders as:**

| Feature        | Free Plan | Pro Plan |
|----------------|-----------|----------|
| Task limit     | 10        | Unlimited|
| Collaboration  | No        | Yes      |
| Export to PDF   | No        | Yes      |

**Key rules**: Use `|` to separate columns and `---` to create the header row. Alignment is optional — the columns don't need to line up perfectly in your source file.

### Task Lists — Tracking Progress

Task lists add checkboxes to track what's done. This is a GitHub Flavored Markdown (GFM) extension:

```text
- [x] Set up project structure
- [x] Create main menu
- [ ] Add task creation feature
- [ ] Add task deletion feature
```

**What it renders as:**

- [x] Set up project structure
- [x] Create main menu
- [ ] Add task creation feature
- [ ] Add task deletion feature

**Syntax**: `- [x]` for checked, `- [ ]` for unchecked. These render as interactive checkboxes on GitHub.

### Escaping Special Characters

Sometimes you want to display characters like `*`, `#`, or `[` as literal text instead of markdown formatting. Use a backslash `\` to escape them:

![Markdown escape sequences diagram showing how backslash prevents special characters from being interpreted as formatting: \*not italic\* renders as literal asterisks, \# not a header shows the hash symbol, and \[link\](url) displays bracket syntax instead of creating a link.](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/images/part-3/chapter-10/escape-sequences-backslashes.png)

**Common characters to escape:**
- `\*` → literal asterisk (instead of italic/bold)
- `\#` → literal hash (instead of heading)
- `\[` and `\]` → literal brackets (instead of link)
- `\\` → literal backslash

### How Newlines Work

Markdown handles line breaks differently than you might expect:

![Comparison diagram showing single newline vs double newline behavior: a single Enter key joins lines into one paragraph, while pressing Enter twice (double newline) creates separate paragraphs in the rendered output.](https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/images/part-3/chapter-10/newline-escaping-markdown-blocks.png)

**Key rule:** A single newline doesn't create a new paragraph. You need a **blank line** (double newline) to separate paragraphs.

```text
Line one.
Line two.
```
Renders as: "Line one. Line two." (same paragraph)

```text
Line one.

Line two.
```
Renders as two separate paragraphs.

---

## Your First Complete Specification

**Congratulations!** You've now built a complete specification across Lessons 2-5.

Your Task Tracker App specification now has everything an AI agent needs to understand and implement your project:

- **Clear structure** (headings)
- **Organized requirements** (lists)
- **Concrete examples** (code blocks)
- **Supporting resources** (links)
- **Visual context** (images)

### Check Your Work

Compare your specification against this reference. Don't worry if yours isn't identical — the important thing is that it has the right structure and elements.

<details>
<summary><strong>Reference: Complete Task Tracker Specification (click to expand)</strong></summary>

````text
# Task Tracker App

## Problem

People forget daily tasks and lose track of what they've completed.
A simple command-line tracker lets users manage tasks without
complicated software.

## Features

### Add Tasks
- Create tasks with title and description
- Set optional due dates
- Assign priority levels (high, medium, low)

### View Tasks
- Display all tasks with status
- Filter by priority or due date
- Show completed and pending separately

### Mark Complete
- Mark tasks as done
- Track completion timestamps
- Move completed tasks to archive

### Delete Tasks
- Remove tasks permanently
- Confirm before deleting to prevent accidents

## Expected Output

When the user runs `python tracker.py`, they should see:

```text
Task Tracker Menu
1. Add Task
2. View Tasks
3. Mark Complete
4. Delete Task
5. Exit

Choose an option: _
```

When viewing tasks, the display looks like:

```text
Your Tasks:
1. Buy groceries [Pending] - Due: 2025-11-08
2. Call dentist [Pending] - Due: 2025-11-07
3. Submit report [Complete] - Done: 2025-11-06
```

When the task list is empty:

```text
Your Tasks:
No tasks yet. Use option 1 to add a task.
```

## Installation

1. Install Python 3.9 or higher from python.org
2. Download the task tracker files from GitHub
3. Navigate to the project folder: `cd task-tracker`
4. Run the program: `python tracker.py`

## Resources

- [Python Official Documentation](https://docs.python.org/) - Language reference
- [Python File I/O Tutorial](https://docs.python.org/3/tutorial/inputoutput.html) - For saving tasks to file

## Screenshot

![Task Tracker main menu showing 5 options: Add Task, View Tasks, Mark Complete, Delete Task, and Exit](https://via.placeholder.com/600x300.png?text=Task+Tracker+Menu)

## Architecture Diagram

![Data flow diagram showing user input going to Task class then to file storage](./images/architecture.png)
````

**What to check in your version:**
- One `#` title, four `##` sections, four `###` feature headings
- Features use bullet lists (unordered — order doesn't matter)
- Installation uses numbered list (ordered — sequence matters)
- Expected output uses fenced code blocks with `text` tag
- At least one link with descriptive text (not "click here")
- At least one image with descriptive alt text (not just "screenshot")

</details>

### What's Next?

In the **Chapter Quiz**, you'll test your markdown knowledge. Then in **Chapter 3**, you'll use these markdown skills to write real specifications for AI agents — turning structured documents into working software.
