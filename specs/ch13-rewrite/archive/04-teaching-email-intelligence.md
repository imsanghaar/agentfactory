---
sidebar_position: 4
title: "Teaching Email Intelligence"
sidebar_label: "L04: Email Intelligence"
description: "Build an email-summarizer skill that parses email threads, extracts decisions, action items, and open questions. Your employee learns to understand what matters."
series: "email"
series_position: 3
keywords:
  - email summarization
  - thread parsing
  - action items
  - Claude Code skills
  - email processing
  - decision extraction
  - skill chaining
  - professional communication
chapter: 10
lesson: 4
duration_minutes: 25

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2 to Layer 3"
layer_progression: "L2 (AI Collaboration) transitioning to L3 (Intelligence Design)"
layer_1_foundation: "Understanding thread structure, extraction patterns, output formatting"
layer_2_collaboration: "Using AI to identify extraction targets, refine output formats, iterate on summarization quality"
layer_3_intelligence: "Creating the email-summarizer skill with skill chaining capability"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Thread Parsing"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Information and Data Literacy"
    measurable_at_this_level: "Student can identify message boundaries and sender attribution in email threads"
  - name: "Information Extraction"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Information and Data Literacy"
    measurable_at_this_level: "Student can extract decisions, action items, and open questions from unstructured text"
  - name: "Output Format Design"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can design output formats appropriate for different use cases"
  - name: "Skill Chaining"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can connect skill outputs to skill inputs for workflow automation"
  - name: "Skill Reference Files"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can create reference files that enhance skill capabilities"

learning_objectives:
  - objective: "Parse email thread structures to identify message boundaries and sender attribution"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successfully identify 3+ messages and their senders in a sample thread"
  - objective: "Create an email-summarizer SKILL.md for thread analysis with proper activation triggers"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "SKILL.md contains YAML frontmatter, extraction workflow, and output format specifications"
  - objective: "Extract decisions, action items, and open questions from email threads"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Accurately categorize 5+ items from a sample thread into correct extraction targets"
  - objective: "Format summary output for different use cases (executive summary vs detailed breakdown)"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Produce two different output formats from the same thread input"
  - objective: "Chain summarizer with drafter skill for automated response generation"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Demonstrate understanding of how summarizer output feeds drafter input"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (thread parsing, extraction targets, output formats, skill chaining, reference patterns) - within A2 limit of 5-7 concepts"

differentiation:
  extension_for_advanced: "Add sentiment analysis to detect thread urgency and stakeholder tensions"
  remedial_for_struggling: "Focus on extracting action items only before expanding to full extraction targets"

teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "Email Intelligence and Skill Chaining"
  key_points:
    - "Only 25% of thread content is actionable — the extraction targets (Decisions, Action Items, Open Questions) are the DAQ pattern students will reuse in every analysis skill"
    - "Three output formats (Executive Summary, Detailed Breakdown, Response Context) teach that same data serves different purposes — format follows function"
    - "Skill chaining (/email-summarizer → /email-drafter) is the first workflow automation pattern — it previews the orchestration layer built in L05-L07"
    - "Extraction patterns in references/ demonstrate that pattern libraries improve over time — students add patterns as they encounter new email styles"
  misconceptions:
    - "Students think the summarizer replaces reading the thread — it extracts actionable items but may miss nuance, especially sarcasm or political subtext"
    - "Students confuse suggestions with action items — the 'Common Extraction Mistakes' section explicitly distinguishes 'We could consider X' from 'Marcus, please do X by Friday'"
    - "Students expect perfect extraction on first try — the skill improves as the extraction-patterns.md reference file grows with new patterns"
    - "Students think skill chaining requires special configuration — it is just invoking one skill after another, using the first skill's output as context"
  discussion_prompts:
    - "The lesson says only 25% of a 15-message thread is actionable. Think of a recent long email thread — what percentage was actually useful for your response?"
    - "The four 'Common Extraction Mistakes' show increasingly subtle errors. Which mistake would be hardest for a human to catch, and why?"
    - "When would you choose the Executive Summary format over the Response Context format? What drives that decision?"
  teaching_tips:
    - "Use a REAL email thread (anonymized) for the live demo — sample threads do not trigger the same recognition as authentic workplace communication"
    - "Walk through the four extraction mistakes sequentially — each builds on the previous one's subtlety, from 'missing implied decisions' to 'ignoring chronology'"
    - "Demo skill chaining live: invoke /email-summarizer, then immediately invoke /email-drafter using the summary as context — students see the workflow in action"
    - "The extraction-patterns.md reference file is a good teaching moment for how L3 intelligence accumulates — start small, add patterns as you encounter them"
  assessment_quick_check:
    - "Name the three extraction targets (DAQ) and give one signal pattern for each"
    - "Given a thread excerpt, identify whether 'We could consider Vendor B' is a decision or a suggestion"
    - "Explain in one sentence how skill chaining works between the summarizer and drafter"

# Generation metadata
generated_by: "content-implementer v1.0.0"
created: "2026-01-01"
version: "1.0.0"
---

# Teaching Email Intelligence

Your inbox shows 47 unread messages. Buried in that count is a 23-message thread about the Q4 budget that you need to respond to before 3 PM. But you can't just read the latest message—critical context is scattered across replies from five different stakeholders over two weeks. Someone made a decision about headcount. Someone assigned you an action item. Someone asked a question that's still unanswered.

You could spend 20 minutes re-reading the entire thread. Or you could invoke a skill that does it in seconds.

This lesson builds an **email-summarizer skill** that transforms long email threads into actionable intelligence: decisions made, tasks assigned, questions pending. More importantly, you'll learn how skills chain together—how the summarizer's output becomes the drafter's input, creating an automated read-to-respond workflow.

---

## The Information Extraction Challenge

Long email threads bury critical information in conversational noise. Consider a typical 15-message thread:

| Message Type | Percentage | Value |
|--------------|------------|-------|
| Greetings and sign-offs | 25% | Zero |
| Context repetition | 20% | Low (already known) |
| Discussion and exploration | 30% | Medium (background) |
| Decisions and action items | 15% | High (actionable) |
| Open questions | 10% | Critical (blocks progress) |

Only 25% of thread content matters for your response. The email-summarizer skill extracts that 25% while discarding the rest.

**Why this matters beyond time savings:**

- **Accuracy**: Manual scanning misses items. Systematic extraction catches everything.
- **Consistency**: Same extraction pattern every time, not dependent on your attention span.
- **Handoff**: Clear summary enables delegation. Anyone can pick up the thread.
- **Memory**: Summaries become searchable records of decisions made.

---

## Understanding Thread Structure

Before extracting information, you need to understand how email threads are structured. Different email clients format threads differently, but common patterns exist.

**Thread Markers to Recognize:**

```
On Mon, Jan 15, 2024 at 2:30 PM Sarah Chen <sarah@company.com> wrote:
```

```
From: Marcus Thompson <marcus@company.com>
Sent: Tuesday, January 16, 2024 9:15 AM
To: Team <team@company.com>
Subject: Re: Q4 Budget Discussion
```

```
---------- Forwarded message ---------
From: Finance Team <finance@company.com>
Date: Wed, Jan 17, 2024 at 11:00 AM
```

**What to Extract from Structure:**

| Element | What It Tells You |
|---------|-------------------|
| Sender name | Who said what |
| Timestamp | When (chronological reconstruction) |
| Subject changes | Topic pivots or forwards |
| Reply depth | Conversation branches |
| CC additions | Stakeholder expansion |

**Message Boundary Detection:**

Threads nest replies inside replies. The skill needs to identify where one message ends and another begins. Key signals:

- Timestamp patterns (`On [date], [name] wrote:`)
- Quote markers (`>` at line start)
- Horizontal rules or separator lines
- Header blocks (From/To/Subject/Date)

---

## Extraction Targets: What to Pull from Threads

Your skill needs to extract three categories of information, each requiring different recognition patterns.

### 1. Decisions Made

Explicit agreements or conclusions that close discussion:

**Signal Patterns:**
- "We've decided to..."
- "Let's go with..."
- "Agreed—we'll..."
- "Final decision:"
- "Approved by..."
- "Confirmed:"
- "Sign-off received"

**What to Capture:**
- The decision itself
- Who made or approved it
- When it was made
- Any conditions attached

**Example Extraction:**

```
Thread excerpt:
"After reviewing the proposals, let's go with Vendor B for the
cloud migration. Sarah approved the budget yesterday."

Extracted:
DECISION: Select Vendor B for cloud migration
WHO: Team decision, budget approved by Sarah
WHEN: [date of message]
CONDITIONS: None stated
```

### 2. Action Items

Tasks assigned to specific people with ownership:

**Signal Patterns:**
- "Can you please..."
- "[Name] will..."
- "I'll take care of..."
- "Action item:"
- "TODO:"
- "Next step:"
- "By [date], we need..."
- "Your action:"

**What to Capture:**
- The task description
- Who is responsible (owner)
- Due date (if stated)
- Dependencies (if mentioned)

**Example Extraction:**

```
Thread excerpt:
"Marcus, can you pull the usage metrics from Q3?
We need them before Friday's meeting."

Extracted:
ACTION: Pull Q3 usage metrics
OWNER: Marcus
DUE: Before Friday meeting
DEPENDENCY: Needed for Friday discussion
```

### 3. Open Questions

Unresolved items waiting for response:

**Signal Patterns:**
- Lines ending with `?`
- "What do you think about..."
- "Need input on..."
- "Waiting for..."
- "TBD:"
- "Open question:"
- "Has anyone..."
- "Can someone clarify..."

**What to Capture:**
- The question itself
- Who asked it
- Who should answer (if specified)
- How long it's been open

**Example Extraction:**

```
Thread excerpt (from 3 days ago):
"Does the new pricing apply to existing customers,
or just new signups? Need to know before we update the FAQ."

Extracted:
QUESTION: New pricing scope (existing vs new customers)
ASKED BY: [sender]
ANSWER NEEDED FROM: [not specified - likely product/sales]
OPEN FOR: 3 days
BLOCKS: FAQ update
```

---

## The Email Summarizer Skill Structure

Your skill follows the same pattern as email-drafter and email-templates:

```
.claude/skills/
└── email-summarizer/
    ├── SKILL.md                    # Main skill instructions
    └── references/
        └── extraction-patterns.md  # Pattern recognition library
```

---

## Building the SKILL.md

Here's the complete SKILL.md for your email-summarizer skill. Create this at `.claude/skills/email-summarizer/SKILL.md`:

```yaml
---
name: email-summarizer
description: This skill summarizes email threads and extracts key information. Use when the user has a long email thread to understand, needs to identify action items, or wants context before replying. Extracts decisions made, action items, and open questions.
---

# Email Summarizer

## Overview

Transform long email threads into actionable summaries with extracted decisions, action items, and context.

## When to Use This Skill

- Email thread has 5+ messages
- Need to quickly understand thread state
- Preparing to reply to a thread
- Extracting action items from discussions
- Creating meeting notes from email exchanges
- Briefing someone on thread status

## Extraction Targets

### 1. Decisions Made

Explicit agreements or conclusions:
- Who decided what
- When it was decided
- Any conditions attached

### 2. Action Items

Tasks assigned to specific people:
- WHO is responsible
- WHAT they need to do
- WHEN it's due (if stated)

### 3. Open Questions

Unresolved items needing response:
- Questions asked but not answered
- Items waiting for input
- Blockers mentioned

### 4. Key Context

Background for response:
- Current state of discussion
- Positions of key stakeholders
- Recent developments

## Output Formats

### Executive Summary (Default)

Quick overview for busy professionals:
- 3-5 sentence summary
- Top 3 action items
- Immediate next step

### Detailed Breakdown

For complex threads:
- Decision log with timestamps
- Full action item list with owners
- Open questions with context
- Stakeholder positions

### Response Context

When preparing to reply:
- What the thread is asking of you
- Your pending action items
- Key points to address

## Workflow

1. Parse thread structure (identify messages and senders)
2. Identify participants and their roles
3. Extract decisions chronologically
4. Extract action items with ownership
5. Identify open questions
6. Format based on user need
7. Offer to chain with /email-drafter for response

## Integration with Other Skills

- Chains with `/email-drafter` for response generation
- Uses tone from `email-drafter/references/tone-guidelines.md`
- Can feed `/email-templates` for structured replies
```

**Key design elements:**

- **Clear activation triggers**: "5+ messages", "action items", "preparing to reply"
- **Three extraction targets**: Decisions, actions, questions (DAQ pattern)
- **Multiple output formats**: Different needs require different summaries
- **Skill chaining**: Explicit integration with drafter and templates

---

## Creating the Extraction Patterns Reference

The extraction patterns file gives Claude a recognition library. Create this at `.claude/skills/email-summarizer/references/extraction-patterns.md`:

```markdown
# Extraction Patterns for Email Analysis

## Decision Signals

Look for these patterns indicating a decision:
- "We've decided to..."
- "Let's go with..."
- "Agreed - we'll..."
- "Final decision:"
- "Confirmed:"
- "Approved by..."
- "Sign-off received"
- "Moving forward with..."
- "After discussion, we'll..."
- "Consensus is..."

## Action Item Signals

Patterns indicating tasks:
- "Can you please..."
- "I'll take care of..."
- "[Name] will..."
- "Action item:"
- "TODO:"
- "Next step:"
- "By [date], we need..."
- "Your action:"
- "Please send..."
- "Make sure to..."
- "Don't forget to..."

## Question Patterns

Unresolved items:
- Lines ending with "?"
- "What do you think about..."
- "Need input on..."
- "Waiting for..."
- "TBD:"
- "Open question:"
- "Has anyone..."
- "Can someone clarify..."
- "Does anyone know..."
- "Should we..."

## Thread Structure Markers

Identify message boundaries:
- "On [date], [name] wrote:"
- "From: / To: / Subject:"
- "---------- Forwarded message"
- "Begin forwarded message:"
- Timestamp patterns (various formats)
- Quote markers (> at line start)
- Horizontal separator lines

## Participant Roles

Identify key players:
- **Original sender** (initiator) - started the thread
- **Decision makers** (approvers) - can authorize
- **Subject matter experts** (info providers) - provide data
- **Blockers** (waiting on input) - thread stalls on them
- **FYI recipients** (CC'd) - informed but not active

## Urgency Indicators

Signals requiring immediate attention:
- "URGENT:" or "ASAP"
- "EOD" or "End of day"
- "Before [meeting/deadline]"
- "Blocking [something]"
- Exclamation marks (multiple)
- ALL CAPS sections
- "Critical" or "Priority"

## De-Prioritization Signals

Safe to defer:
- "When you get a chance..."
- "No rush, but..."
- "Low priority"
- "FYI only"
- "For your awareness"
```

**Why pattern libraries work:**

- **Consistency**: Same patterns recognized every time
- **Coverage**: Captures variations you might miss
- **Improvement**: Add patterns as you encounter new ones
- **Transfer**: Patterns work across domains, not just email

---

## Output Format Examples

Different situations require different summary formats. Here's how each works:

### Executive Summary Format

For quick decisions about whether to engage deeply:

```
## Thread Summary: Q4 Budget Discussion

**Status**: Active discussion, awaiting final approval

**Key Points** (3):
1. Vendor B selected for cloud migration (approved by Sarah, Jan 15)
2. Headcount frozen at current levels for Q4
3. Marketing budget reduced 15% per CFO guidance

**Your Action Items**:
- Pull Q3 usage metrics before Friday
- Review revised timeline from Marcus

**Immediate Next Step**: Respond to open question about contractor budget
```

### Detailed Breakdown Format

For complex threads requiring full context:

```
## Thread Analysis: Q4 Budget Discussion
**Messages**: 23 | **Participants**: 5 | **Duration**: 12 days

### Decisions Log

| Date | Decision | Decided By | Conditions |
|------|----------|------------|------------|
| Jan 15 | Vendor B for migration | Sarah (budget), Team (technical) | Subject to contract review |
| Jan 18 | Headcount freeze | CFO directive | Through Q4 only |
| Jan 22 | Marketing -15% | CFO + CMO | Reallocate to digital |

### Action Items

| Task | Owner | Due | Status |
|------|-------|-----|--------|
| Q3 metrics | Marcus | Friday | Pending |
| Timeline revision | Marcus | Next week | In progress |
| Contract review | Legal | Jan 30 | Not started |
| FAQ update | You | After pricing clarity | Blocked |

### Open Questions

1. **Contractor budget scope** (Jan 20, asked by PM)
   - Does freeze apply to existing contractors?
   - No response yet (3 days open)
   - Blocks: Resource planning

2. **New pricing for existing customers** (Jan 19, asked by Sales)
   - Grandfather existing or apply to all?
   - Blocks: FAQ update, customer comms

### Stakeholder Positions

- **CFO**: Focused on cost reduction, firm on headcount
- **CMO**: Accepted marketing cut, pushing for digital reallocation
- **PM**: Concerned about timeline with frozen resources
- **Sales**: Waiting on pricing clarity for customer communication
```

### Response Context Format

When you're about to reply:

```
## Response Context: Q4 Budget Thread

**What the thread is asking of you**:
1. Pull Q3 usage metrics (explicit request from Marcus)
2. Clarify contractor budget question (you're likely the right person)
3. Confirm timeline feasibility with reduced resources

**Your pending action items**:
- Q3 metrics: Due Friday (2 days)
- FAQ update: Blocked on pricing question

**Key points to address in your reply**:
- Confirm you'll deliver metrics by Friday
- Provide contractor budget guidance (or defer to CFO)
- Flag timeline risk if resources stay frozen

**Tone note**: CFO is in thread—be concise, data-focused
```

---

## Skill Chaining: Summarizer to Drafter

The real power emerges when skills work together. Your email-summarizer produces context that your email-drafter consumes:

**The Chain:**

```
[Long Thread] → /email-summarizer → [Context] → /email-drafter → [Reply Draft]
```

**How It Works:**

1. Invoke summarizer on the thread
2. Summarizer extracts action items, decisions, questions
3. Ask to draft a response
4. Drafter uses summary as context
5. Draft addresses extracted items with your tone

**Example Flow:**

```
User: Summarize this thread and then help me respond.

[Claude invokes /email-summarizer]

Summary:
- Decision: Vendor B selected
- Action for you: Provide Q3 metrics by Friday
- Open question: Contractor budget (needs your input)

[Claude recognizes response intent, invokes /email-drafter]

Using your summary, here's a draft response:

Hi team,

Quick updates on the open items:

**Q3 Metrics**: I'll have these ready by Thursday EOD,
giving us a day buffer before Friday's meeting.

**Contractor Budget**: For existing contractors, I recommend
we honor current agreements through Q4. New contractor
requests should route through the approval exception process.

Let me know if you need anything else before Friday.

Best,
[Your name]
```

**Why chaining matters:**

- **Context preservation**: Summary context flows into draft
- **Efficiency**: Single workflow, not separate prompts
- **Consistency**: Same tone guidelines apply
- **Completeness**: Draft addresses all extracted items

---

## Testing Your Skill

Let's verify the skill works correctly.

**Step 1: Create the directory structure**

```bash
mkdir -p .claude/skills/email-summarizer/references
```

**Output:**
```
(no output - directories created silently)
```

**Step 2: Verify your structure**

```bash
find .claude/skills -type d | sort
```

**Output:**
```
.claude/skills
.claude/skills/email-drafter
.claude/skills/email-drafter/references
.claude/skills/email-summarizer
.claude/skills/email-summarizer/references
.claude/skills/email-templates
.claude/skills/email-templates/templates
```

**Step 3: Create the files**

Copy the SKILL.md content to `.claude/skills/email-summarizer/SKILL.md` and the extraction patterns to `.claude/skills/email-summarizer/references/extraction-patterns.md`.

**Step 4: Test with a sample thread**

Provide Claude with a multi-message email thread and invoke the skill:

```
/email-summarizer

[Paste your email thread here]

Give me an executive summary and list my action items.
```

**Expected Behavior:**

1. Claude recognizes thread parsing is needed
2. Identifies message boundaries and senders
3. Extracts decisions, actions, questions
4. Formats as executive summary
5. Highlights your specific action items

---

## Common Extraction Mistakes

When building extraction logic, these patterns cause problems:

**Mistake 1: Missing implied decisions**

```
Thread: "I don't hear any objections, so we'll proceed with Plan A."

WRONG: No decision extracted (no explicit "decided" word)
RIGHT: Decision extracted (consensus by silence)
```

**Mistake 2: Confusing suggestions with action items**

```
Thread: "We could also consider reaching out to Partner X."

WRONG: Action item - reach out to Partner X
RIGHT: Suggestion only (no ownership, no commitment)
```

**Mistake 3: Missing conditional action items**

```
Thread: "If the budget clears, Sarah will start procurement."

WRONG: Action item - Sarah starts procurement
RIGHT: Conditional action - Sarah starts IF budget clears
```

**Mistake 4: Ignoring thread chronology**

```
Early message: "Let's use Vendor A"
Later message: "After review, switching to Vendor B"

WRONG: Decision - use Vendor A
RIGHT: Decision - use Vendor B (supersedes earlier)
```

---

## Extending the Skill

Once the basic skill works, consider these enhancements:

| Extension | Value | Complexity |
|-----------|-------|------------|
| Sentiment detection | Identify tension or urgency | Medium |
| Stakeholder mapping | Auto-identify roles | Low |
| Timeline extraction | Build project timeline from thread | Medium |
| Commitment tracking | Match promises to follow-through | High |

**Sentiment example addition to SKILL.md:**

```markdown
## Sentiment Indicators

### Urgency Signals
- Multiple exclamation marks
- "URGENT", "ASAP", "Critical"
- Short response times (< 1 hour between messages)

### Tension Signals
- Defensive language ("As I mentioned...")
- Escalation (new executives added to CC)
- Formal tone shift (first names → full names)
```

---

## Try With AI

**Setup:** Open Claude Code in the `email-assistant` directory with the email-summarizer skill installed.

**Prompt 1: Basic Thread Extraction**

```
/email-summarizer

Here's a thread I need to understand quickly:

[Paste a real or sample email thread with 5+ messages
that contains at least one decision, one action item,
and one open question]

Give me the executive summary format.
```

**What you're learning:** This tests the core extraction workflow. Review the output: Did Claude correctly identify message boundaries? Are the extraction targets (decisions, actions, questions) accurate? Did anything get missed or miscategorized?

**Prompt 2: Response Context Generation**

```
Now give me the response context format for that same thread.
I need to understand what the thread is asking of ME specifically
and what I should address in my reply.
```

**What you're learning:** This tests output format flexibility. The same thread should produce different summaries for different purposes. Compare the executive summary to the response context—same source data, different focus.

**Prompt 3: Chain to Email Drafter**

```
Based on that summary, help me draft a response.
Use /email-drafter to compose a reply that addresses
all the action items assigned to me and answers
the open questions I can answer.
```

**What you're learning:** This demonstrates skill chaining. The summarizer's output becomes the drafter's context. Notice how the draft addresses the specific items extracted from the summary. This is workflow automation—multiple skills coordinating automatically.

**Safety Note:** When summarizing threads containing sensitive information, be mindful of what you share with AI systems. Summarization is powerful but should be used appropriately for the content's sensitivity level.
