---
sidebar_position: 7
title: "Bronze Capstone: Your First Working Employee"
sidebar_label: "L07: Bronze Capstone"
description: "Build the email-assistant master skill that orchestrates skills, subagents, and MCP into a complete Triage-to-Send workflow. Your employee is ready for work."
series: "email"
series_position: 6
keywords:
  - master skill
  - orchestration
  - skill composition
  - subagent coordination
  - MCP integration
  - graceful degradation
  - Email Digital FTE
  - Claude Code
  - workflow automation
chapter: 10
lesson: 7
duration_minutes: 40

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 4"
layer_progression: "L4 (Spec-Driven Capstone)"
layer_1_foundation: "N/A (capstone builds on lessons 1-5)"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "Design master skill orchestrating all chapter components into Digital FTE"

# HIDDEN SKILLS METADATA
skills:
  - name: "Master Skill Design"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can design orchestrator skill that coordinates multiple component skills and subagents"
  - name: "Delegation Logic"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can determine when to use skills vs subagents vs MCP based on task characteristics"
  - name: "Workflow Sequencing"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can sequence workflow steps correctly (triage before suggest, draft before send)"
  - name: "Error Handling"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can implement error handling that provides clear feedback and recovery options"
  - name: "Graceful Degradation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can design systems that continue functioning when components are unavailable"
  - name: "Component Composition"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can compose skills, subagents, and MCP into cohesive workflow"
  - name: "End-to-End Testing"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can test complete workflows with verification at each step"
  - name: "Spec-First Orchestration"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can write specifications that define orchestration behavior before implementation"

learning_objectives:
  - objective: "Design master skill orchestration patterns that coordinate multiple component skills"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Create email-assistant SKILL.md with workflow modes and component references"
  - objective: "Create the email-assistant master skill that coordinates email-drafter, email-templates, email-summarizer, and subagents"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Produce working master skill that invokes component skills appropriately"
  - objective: "Implement delegation logic determining when to use skills versus subagents versus MCP"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Correctly identify component type for given task scenarios"
  - objective: "Build complete workflow from Triage through Suggest, Draft, to Send"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Demonstrate end-to-end workflow execution in correct sequence"
  - objective: "Handle errors and implement graceful degradation when MCP is unavailable"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "System continues functioning with skills-only when Gmail MCP offline"
  - objective: "Test the complete Email Digital FTE system end-to-end"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Execute all four workflow modes and verify correct component activation"

cognitive_load:
  new_concepts: 8
  assessment: "8 concepts (master skill, delegation logic, workflow sequencing, error handling, graceful degradation, component composition, end-to-end testing, spec-first orchestration) - at upper limit for B1, appropriate for capstone synthesis"

differentiation:
  extension_for_advanced: "Add conditional workflow branching based on email priority level; implement feedback loop that improves triage accuracy over time"
  remedial_for_struggling: "Focus on basic two-component orchestration (email-drafter + email-templates) before adding subagents and MCP"

teaching_guide:
  lesson_type: "capstone"
  session_group: 3
  session_title: "Bronze Capstone - Email Digital FTE"
  key_points:
    - "A master skill does not do work itself — it interprets intent, selects workflow, coordinates components, manages state, and handles failures"
    - "The delegation decision tree (content→skill, classification→subagent, external→MCP) is the core orchestration pattern that applies to any domain beyond email"
    - "Graceful degradation means the system continues functioning when components fail — skills work without MCP, subagents work with pasted data"
    - "Four workflow modes (Inbox Management, Composition, Thread Response, Follow-Up Check) show that one entry point can serve multiple user intents"
  misconceptions:
    - "Students think the master skill replaces the component skills — it orchestrates them, each component still does its own work"
    - "Students expect the orchestrator to always use ALL components — each workflow mode uses only the relevant subset"
    - "Students think graceful degradation means 'nothing works' — it means reduced but still functional capability with clear user communication"
    - "Students try to put all logic in the master SKILL.md — the orchestration-logic.md reference file separates coordination rules from the skill definition"
  discussion_prompts:
    - "The master skill has 4 workflow modes. If you could only keep 2, which would you choose for YOUR work and why?"
    - "Graceful degradation provides email content for clipboard when Gmail MCP is offline. What other fallback strategies could you design?"
    - "The delegation decision tree applies beyond email. Map it to a domain you know — what would skills, subagents, and MCP handle in customer support? Content creation?"
  teaching_tips:
    - "Have students draw the component architecture diagram from memory before revealing it — this tests whether they understand the system they have been building"
    - "Test graceful degradation FIRST (Test 5) before testing normal operation — it validates the most important engineering principle and gives students confidence"
    - "The delegation logic decision tree is the best whiteboard exercise — walk through 3-4 user requests and trace which components activate"
    - "Celebrate this milestone explicitly — students have built a complete Digital FTE from scratch across 7 lessons"
  assessment_quick_check:
    - "Name the 4 workflow modes and give one trigger phrase for each"
    - "What happens when you invoke /email-assistant and Gmail MCP is offline? Walk through the graceful degradation path."
    - "Draw the delegation decision tree: content→skill, classification→subagent, external→MCP"

# Generation metadata
generated_by: "content-implementer (autonomous execution)"
created: "2026-01-01"
version: "1.0.0"
---

# Bronze Capstone: Your First Working Employee

You've built the pieces: four skills for email composition, three subagents for email processing, and MCP integration for real email operations. Each component works independently. But individually, they're just tools sitting in folders.

The business professional you're building for doesn't want to think about which skill to invoke or which subagent to activate. They want to say "Help me with email" and have the system figure out whether to triage, draft, follow-up, or send. They want a single entry point that orchestrates everything.

This is the difference between a collection of tools and a **Digital FTE**. A Digital FTE doesn't require the user to be the coordinator. It owns the workflow end-to-end, making decisions about what to do next, handling errors gracefully, and continuing to function even when some components are unavailable.

In this capstone lesson, you'll build the `/email-assistant` master skill that transforms your collection of components into a complete Email Digital FTE.

---

## The Architecture You've Built

Before orchestrating, let's see what you have:

```
Email Assistant System
├── Skills (4 Components - Content Generation)
│   ├── /email-drafter        → Compose with tone specification
│   ├── /email-templates      → Variable substitution, 3 templates
│   ├── /email-summarizer     → Thread parsing, action extraction
│   └── /email-assistant      → MASTER ORCHESTRATOR (this lesson)
│
├── Subagents (3 Workers - Processing & Analysis)
│   ├── inbox-triager         → Priority classification (urgent/respond/defer/archive)
│   ├── response-suggester    → Generate contextual reply options
│   └── follow-up-tracker     → Monitor pending responses and deadlines
│
├── MCP Integration (External Operations)
│   └── Gmail MCP Server      → 19 tools: read, send, search, label, archive
│
└── Orchestration Flow
    └── Triage → Suggest → Draft → Send
```

Each component has a specific role:

| Component Type   | Purpose                                 | Examples                                 |
| ---------------- | --------------------------------------- | ---------------------------------------- |
| **Skills**       | Provide expertise and templates         | Email tone, template structures          |
| **Subagents**    | Autonomous reasoning and classification | Priority decisions, response suggestions |
| **MCP**          | External system operations              | Gmail read/send/search                   |
| **Orchestrator** | Workflow coordination                   | Deciding what to invoke when             |

---

## The Master Skill Pattern

A master skill differs from component skills in one critical way: **it doesn't do work itself**. Instead, it:

1. **Interprets user intent** — What does "help me with email" actually mean?
2. **Selects appropriate workflow** — Which mode should we activate?
3. **Coordinates components** — Which skills/subagents/MCP tools to invoke?
4. **Manages state** — What happened, what's next, what needs follow-up?
5. **Handles failures** — What if Gmail MCP is down? What if a subagent fails?

This is **specification-driven orchestration**. The master skill is essentially a specification that defines how components interact.

---

## Creating the Master Skill Directory

First, set up the orchestrator skill structure:

```bash
mkdir -p .claude/skills/email-assistant/references
```

**Output:**

```
(no output - directory created silently)
```

Your complete project structure should now look like this:

```
email-assistant/
├── .claude/
│   ├── skills/
│   │   ├── email-drafter/
│   │   │   ├── SKILL.md
│   │   │   └── references/
│   │   │       └── tone-guidelines.md
│   │   ├── email-templates/
│   │   │   ├── SKILL.md
│   │   │   └── templates/
│   │   │       ├── cold-outreach.md
│   │   │       ├── follow-up.md
│   │   │       └── meeting-request.md
│   │   ├── email-summarizer/
│   │   │   ├── SKILL.md
│   │   │   └── references/
│   │   │       └── extraction-patterns.md
│   │   └── email-assistant/          # MASTER ORCHESTRATOR
│   │       ├── SKILL.md
│   │       └── references/
│   │           └── orchestration-logic.md
│   └── agents/
│       ├── inbox-triager.md
│       ├── response-suggester.md
│       └── follow-up-tracker.md
├── CLAUDE.md
└── .mcp.json                          # Gmail MCP config (optional)
```

---

## Building the Master SKILL.md

The master skill is your most complex SKILL.md. It needs to:

- Reference all component skills and subagents
- Define multiple workflow modes
- Include delegation logic
- Handle graceful degradation

Create `.claude/skills/email-assistant/SKILL.md`:

```yaml
---
name: email-assistant
description: Master orchestrator for email workflow automation. Coordinates email-drafter, email-templates, email-summarizer skills with inbox-triager, response-suggester, follow-up-tracker subagents, and Gmail MCP for end-to-end email management.
---

# Email Assistant

## Overview

Your complete Email Digital FTE — orchestrating skills, subagents, and MCP for automated email workflow management. This is the single entry point for all email operations.

## Components Orchestrated

### Skills (Content Generation)

| Skill | Purpose | When to Invoke |
|-------|---------|----------------|
| `/email-drafter` | Professional email composition | User needs custom email with tone control |
| `/email-templates` | Template-based messaging | User needs standard email type (outreach, follow-up, meeting) |
| `/email-summarizer` | Thread analysis | User needs to understand long threads quickly |

### Subagents (Processing & Analysis)

| Subagent | Purpose | When to Invoke |
|----------|---------|----------------|
| `inbox-triager` | Priority classification | User wants inbox organized by importance |
| `response-suggester` | Quick reply options | User needs response ideas for specific email |
| `follow-up-tracker` | Deadline management | User wants to know what needs attention |

### MCP (External Operations)

| Tool Category | Purpose | When to Invoke |
|---------------|---------|----------------|
| Gmail MCP: search_emails | Fetch emails by query | Need real email data |
| Gmail MCP: draft_email | Create Gmail draft | Ready to save draft for review |
| Gmail MCP: send_email | Send email | User confirms send action |

## Workflow Modes

### Mode 1: Inbox Management

**Trigger:** "Help me manage my inbox" or "Triage my email"

**Workflow sequence:**
1. Fetch unread emails (Gmail MCP: search_emails with query "is:unread")
2. Classify by priority (inbox-triager subagent)
3. Summarize important threads (email-summarizer skill)
4. Suggest responses for urgent items (response-suggester subagent)
5. Draft replies for approved suggestions (email-drafter + email-templates skills)
6. Create as Gmail drafts (Gmail MCP: draft_email)

**State after completion:**
- Inbox categorized by priority
- Important threads summarized
- Draft responses ready for review

### Mode 2: Email Composition

**Trigger:** "Write an email to [person] about [topic]"

**Workflow sequence:**
1. Identify email type (cold outreach, follow-up, meeting request, or custom)
2. Select template if applicable (email-templates skill)
3. Draft email with personalization (email-drafter skill)
4. Apply tone guidelines
5. Create draft or send based on user preference (Gmail MCP)

**Decision logic:**
- If email type matches template → Use email-templates first, then email-drafter for personalization
- If email type is custom → Use email-drafter directly
- If user specifies "urgent" or "formal" → Apply appropriate tone modifier

### Mode 3: Thread Response

**Trigger:** "Help me respond to this thread" or "Reply to [email]"

**Workflow sequence:**
1. Fetch thread content (Gmail MCP: get_thread)
2. Summarize thread and extract key points (email-summarizer skill)
3. Identify required action items
4. Generate response options (response-suggester subagent)
5. Draft chosen response (email-drafter skill)
6. Create draft for review (Gmail MCP: draft_email)

**Output:**
- Thread summary with action items
- 3 response options with tone labels
- Draft of user-selected option

### Mode 4: Follow-Up Check

**Trigger:** "What emails need follow-up?" or "Check my pending responses"

**Workflow sequence:**
1. Fetch sent emails from past 7-14 days (Gmail MCP: search_emails)
2. Analyze for awaiting responses (follow-up-tracker subagent)
3. Identify items past response deadline
4. Generate follow-up drafts (email-templates: follow-up template)
5. Create drafts for review (Gmail MCP: draft_email)

**Output:**
- List of emails awaiting response with wait time
- Flagged items past expected response window
- Ready-to-send follow-up drafts

## Delegation Logic

When should you use each component type?

| Task Characteristic | Component Type | Reasoning |
|---------------------|----------------|-----------|
| Content generation with known patterns | **Skills** | Predictable output, consistent application |
| Classification requiring judgment | **Subagents** | Autonomous reasoning, context evaluation |
| External data or actions | **MCP** | System integration, real operations |
| Multi-step coordination | **Orchestrator** | Workflow sequencing, state management |

**Decision tree for component selection:**

Is task about creating content?
├── Yes → Does a template exist?
│   ├── Yes → email-templates skill
│   └── No → email-drafter skill
└── No → Is task about classification/analysis?
    ├── Yes → Use appropriate subagent
    │   ├── Priority classification → inbox-triager
    │   ├── Response suggestions → response-suggester
    │   └── Deadline tracking → follow-up-tracker
    └── No → Is task about external operations?
        ├── Yes → Gmail MCP tools
        └── No → Orchestrator handles directly

## Graceful Degradation

Systems fail. Gmail API goes down. Authentication expires. Network drops. The Email Assistant must continue functioning with reduced capability rather than failing completely.

### If Gmail MCP Unavailable

When Gmail MCP cannot connect:

1. **Skills still work fully**
   - email-drafter produces emails
   - email-templates applies patterns
   - email-summarizer analyzes provided text

2. **Subagents work with provided data**
   - If user pastes email content, subagents can analyze it
   - Cannot fetch new emails automatically

3. **Output changes**
   - Instead of creating Gmail draft → Copy email to clipboard
   - Instead of sending → Provide formatted email for manual paste
   - Clear notification: "Gmail MCP offline. Email copied to clipboard for manual sending."

### If Specific Skill Missing

When a component skill is unavailable:

- Fall back to email-drafter for all composition tasks
- Note which specialized skill would have helped
- Continue workflow with reduced specialization

## Error Handling

1. **MCP connection failed**: Continue with local skills, notify user of reduced capability
2. **Email not found**: Report clearly, suggest alternative search terms
3. **Draft creation failed**: Provide email content for manual use
4. **Authentication expired**: Guide user through re-authentication steps

## Usage Examples

| User Says | Mode Selected | Components Used |
|-----------|---------------|-----------------|
| "Help me with email" | Mode selection menu | (offers all modes) |
| "Triage my inbox" | Mode 1: Inbox Management | Gmail MCP + inbox-triager + email-summarizer |
| "Write a cold outreach" | Mode 2: Composition | email-templates + email-drafter + Gmail MCP |
| "Respond to this thread" | Mode 3: Thread Response | email-summarizer + response-suggester + email-drafter |
| "Check my follow-ups" | Mode 4: Follow-Up Check | Gmail MCP + follow-up-tracker + email-templates |
```

---

## Creating the Orchestration Logic Reference

The master skill references an orchestration-logic.md file that provides detailed decision frameworks. Create `.claude/skills/email-assistant/references/orchestration-logic.md`:

```markdown
# Orchestration Logic for Email Assistant

## Component Selection Matrix

| User Request Pattern         | Primary Component  | Supporting Components       |
| ---------------------------- | ------------------ | --------------------------- |
| "Write an email"             | email-drafter      | email-templates, Gmail MCP  |
| "Use the follow-up template" | email-templates    | email-drafter, Gmail MCP    |
| "Summarize this thread"      | email-summarizer   | -                           |
| "Triage my inbox"            | inbox-triager      | email-summarizer, Gmail MCP |
| "Suggest a response"         | response-suggester | email-drafter               |
| "What needs follow-up?"      | follow-up-tracker  | email-templates, Gmail MCP  |
| "Help me manage email"       | ORCHESTRATOR       | ALL components              |

## Workflow Sequencing

### Sequential Dependencies

Tasks that must complete before the next can begin:

1. **Triage BEFORE Suggest** — Need priority context before generating response options
2. **Summarize BEFORE Respond** — Need thread context before drafting reply
3. **Draft BEFORE Send** — Need email content before sending

### Parallel Opportunities

Tasks that can run simultaneously:

- Triage multiple email batches in parallel
- Draft multiple responses while user reviews first
- Track follow-ups while composing new emails

## State Management

### Session State

Information maintained during active session:

- Current inbox snapshot (from last triage)
- Active drafts pending review
- Follow-up queue with deadlines

### Persistent State

Information stored in skill references:

- Tone guidelines (in email-drafter/references/)
- Templates (in email-templates/templates/)
- Priority contact list (in inbox-triager configuration)

## Offline Mode Workflow

When Gmail MCP is unavailable:

1. **Skill invocation works normally** — All content generation functions
2. **Subagent analysis works with provided data** — User can paste email content
3. **Output format changes**:
   - Email content copied to clipboard
   - Manual instructions provided
   - User notified of offline status

## Quality Gates

Before any email is sent:

1. Tone matches guidelines
2. Template variables fully substituted (no {{placeholders}} remaining)
3. Recipient address verified
4. Draft reviewed if importance level high
5. User confirmed send action explicitly
```

---

## Understanding Delegation Logic

The delegation logic determines which component handles each task. This is the intelligence at the heart of orchestration.

**Skills vs Subagents vs MCP — When to Use Each:**

| Characteristic            | Use Skill             | Use Subagent               | Use MCP                   |
| ------------------------- | --------------------- | -------------------------- | ------------------------- |
| **Decision Points**       | 2-4                   | 5+                         | N/A                       |
| **Output Predictability** | High (template-based) | Variable (reasoning-based) | Deterministic (API-based) |
| **Processing Type**       | Content generation    | Classification/analysis    | External operations       |
| **Example**               | Draft email with tone | Classify priority level    | Fetch from Gmail          |

**The key insight:** Skills provide guidance. Subagents provide reasoning. MCP provides integration. The orchestrator provides coordination.

---

## Testing the Complete System

Let's walk through testing each workflow mode to verify the orchestration works correctly.

### Test 1: Inbox Management Mode

```
/email-assistant

I want to triage my inbox. Show me what needs attention.
```

**Expected behavior:**

1. Gmail MCP fetches unread emails (or skill asks for email content if offline)
2. inbox-triager classifies each email (urgent/respond/defer/archive)
3. email-summarizer provides summaries of important threads
4. response-suggester generates quick reply options for urgent items
5. User selects which suggestions to draft
6. email-drafter/email-templates create draft responses

**Verification points:**

- Are emails correctly categorized by priority?
- Do summaries capture key information?
- Are response suggestions contextually appropriate?

### Test 2: Email Composition Mode

```
/email-assistant

Write a follow-up email to Sarah Chen about the data partnership we discussed at the conference last week.
```

**Expected behavior:**

1. Orchestrator recognizes this as Mode 2 (composition) with follow-up type
2. email-templates skill provides follow-up template structure
3. email-drafter applies tone guidelines and personalizes content
4. Gmail MCP creates draft (or provides clipboard content if offline)

**Verification points:**

- Did orchestrator select the correct workflow mode?
- Was the follow-up template applied?
- Does the draft match your tone guidelines?

### Test 3: Thread Response Mode

```
/email-assistant

Here's a thread I need to respond to:

[Paste email thread content]

Help me craft a response.
```

**Expected behavior:**

1. email-summarizer extracts key points and action items
2. response-suggester generates 3 response options with different tones
3. User selects preferred approach
4. email-drafter creates full response based on selection

**Verification points:**

- Are all action items extracted from the thread?
- Do the 3 response options offer meaningfully different approaches?
- Does the final draft address all required points?

### Test 4: Follow-Up Check Mode

```
/email-assistant

What emails need follow-up? Check my sent folder.
```

**Expected behavior:**

1. Gmail MCP searches sent emails from past 7-14 days
2. follow-up-tracker analyzes for awaiting responses
3. Items past expected response window are flagged
4. email-templates generates follow-up drafts for flagged items

**Verification points:**

- Is the lookback period appropriate (7-14 days)?
- Are awaited responses correctly identified?
- Do follow-up drafts add new value (not just "checking in")?

---

## Testing Graceful Degradation

The most important test is verifying the system continues working when components fail.

### Test 5: Gmail MCP Offline

Temporarily disable Gmail MCP (rename or remove `.mcp.json`), then:

```
/email-assistant

Write a cold outreach email to Marcus Rodriguez, CEO of DataFlow Inc. I want to propose a partnership around developer education content.
```

**Expected behavior:**

1. Orchestrator detects Gmail MCP is unavailable
2. Skills (email-templates, email-drafter) work normally
3. Instead of creating Gmail draft, email content is provided for clipboard
4. Clear message: "Gmail MCP offline. Here's your email for manual sending."

**Verification points:**

- Does the skill workflow complete successfully?
- Is the degradation clearly communicated?
- Is the email content complete and usable?

---

## What You've Built

With the email-assistant master skill, you now have:

| Component           | Count | Purpose                                                           |
| ------------------- | ----- | ----------------------------------------------------------------- |
| **Skills**          | 4     | email-drafter, email-templates, email-summarizer, email-assistant |
| **Subagents**       | 3     | inbox-triager, response-suggester, follow-up-tracker              |
| **MCP Integration** | 1     | Gmail MCP with 19 tools                                           |
| **Workflow Modes**  | 4     | Inbox management, composition, thread response, follow-up check   |

This is a **Digital FTE** — a complete system that can:

- Understand user intent from natural language
- Select appropriate workflows automatically
- Coordinate multiple components seamlessly
- Handle failures gracefully
- Continue functioning in degraded mode

The pattern you've learned applies far beyond email. Customer support, document processing, data analysis, content creation — any domain where multiple AI capabilities need coordination can use this same orchestration pattern.

---

## Try With AI

**Prompt 1: Full Inbox Management Workflow**

```
/email-assistant

I'm behind on email after a week of travel. Help me triage my inbox and identify the 5 most urgent items that need responses today. For each urgent item, suggest a quick response I can send.
```

**What you're learning:** This tests the complete Mode 1 workflow. Watch how the orchestrator coordinates Gmail MCP (or asks for content if offline), inbox-triager for prioritization, email-summarizer for context, and response-suggester for quick replies. Notice which components activate in which sequence.

**Prompt 2: Orchestrator Decision-Making**

```
/email-assistant

I need to:
1. Write a meeting request to schedule a call with the engineering team
2. Follow up on a proposal I sent last week to a potential client
3. Respond to a thread about project timeline concerns

Handle all three tasks, explaining which components you're using for each.
```

**What you're learning:** This tests delegation logic across multiple task types. The orchestrator should use email-templates for the meeting request, email-templates (follow-up) for the proposal follow-up, and the thread response workflow (summarizer + suggester + drafter) for the timeline concerns. Compare the components used for each task.

**Prompt 3: Graceful Degradation in Action**

```
/email-assistant

Assume Gmail MCP is offline. I still need to:
- Draft a cold outreach email to introduce myself to a conference speaker I admired
- Create a follow-up for a job application I submitted 10 days ago

Show me how you'd handle these without Gmail integration, and what the user experience looks like.
```

**What you're learning:** This tests graceful degradation. With MCP offline, skills should still work fully. You should receive complete email content with instructions for manual sending. Evaluate: Is the degradation clear? Is the output still useful? What's the difference in user experience compared to full functionality?

**Always review AI-generated emails before sending.** The Email Assistant provides drafts, not final approved content. You remain responsible for accuracy, appropriateness, and timing of all communications.
