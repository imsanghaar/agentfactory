---
sidebar_position: 5
title: "Hiring Specialists"
sidebar_label: "L05: Hiring Specialists"
description: "Build three specialized email processing subagents for inbox triaging, response suggestion, and follow-up tracking. Your employee hires its own team."
series: "email"
series_position: 5
keywords:
  - Claude Code subagents
  - inbox triage
  - email automation
  - agent definition
  - Task tool
  - autonomous reasoning
  - response suggestion
  - follow-up tracking
chapter: 10
lesson: 5
duration_minutes: 35

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 3"
layer_progression: "L3 (Intelligence Design) - Creating reusable autonomous components"
layer_1_foundation: "Understanding agent definition format, single-line description requirement"
layer_2_collaboration: "Testing agents with Task tool, refining classification logic"
layer_3_intelligence: "Creating three subagents that encode email processing expertise"
layer_4_capstone: "N/A (orchestration comes in Lesson 6)"

# HIDDEN SKILLS METADATA
skills:
  - name: "Subagent Architecture Understanding"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can explain how subagents differ from skills and when to use each"
  - name: "Agent Definition Format"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can create valid agent definition files with proper YAML frontmatter"
  - name: "Classification Logic Design"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can design priority classification systems with clear criteria"
  - name: "Task Tool Delegation"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can invoke subagents using the Task tool for autonomous processing"
  - name: "Response Generation Patterns"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Communication and Collaboration"
    measurable_at_this_level: "Student can design response suggestion systems with multiple tone options"
  - name: "Deadline Tracking Logic"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can implement follow-up tracking with implicit and explicit deadline detection"
  - name: "Skills vs Subagents Decision Framework"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can correctly choose between skill and subagent for a given automation task"

learning_objectives:
  - objective: "Explain how subagent architecture differs from skills and when autonomous reasoning justifies subagent creation"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student correctly identifies subagent vs skill use cases in scenarios"
  - objective: "Create agent definition files with proper YAML frontmatter including single-line description"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Agent definition file passes validation with required fields"
  - objective: "Build an inbox-triager subagent that classifies emails into Urgent/Important/Normal/Low priorities"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Subagent correctly classifies sample emails with reasoning"
  - objective: "Build a response-suggester subagent that generates 2-3 response options with different tones"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Subagent produces distinct response options matching specified tones"
  - objective: "Build a follow-up-tracker subagent that identifies sent emails needing follow-up with deadlines"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Subagent detects implicit and explicit deadlines in email threads"
  - objective: "Apply the skills vs subagents decision framework to correctly choose the right component type"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student justifies component choice using decision framework criteria"

cognitive_load:
  new_concepts: 7
  assessment: "7 concepts (agent definition format, single-line description, Task tool, inbox-triager logic, response-suggester logic, follow-up-tracker logic, skills vs subagents framework) - at upper B1 limit of 7-10 concepts, appropriate for stepping up from A2"

differentiation:
  extension_for_advanced: "Add conditional logic for VIP contact lists, integrate with calendar for meeting-related emails, create priority overrides based on project context"
  remedial_for_struggling: "Focus on inbox-triager first before building additional subagents; use the provided examples as templates rather than building from scratch"

teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "Subagent Architecture"
  key_points:
    - "Skills tell Claude HOW to do something, subagents tell Claude WHAT to do after analyzing a situation — this is the core architectural distinction students must internalize"
    - "The 2-4 vs 5+ decision points threshold is the practical rule for choosing skills vs subagents — inbox triage requires 5+ contextual factors"
    - "Single-line YAML description is a hard technical requirement — multi-line breaks Claude Code's parser, and this is the most common agent creation error"
    - "Three subagents demonstrate three reasoning patterns: classification (triager), generation with options (suggester), temporal tracking (follow-up tracker)"
  misconceptions:
    - "Students think subagents are 'better' than skills — they serve different purposes; a template substitution task should NEVER be a subagent"
    - "Students confuse the single-line description requirement with a content limit — the line can be very long (up to 1024 chars), it just cannot use YAML multiline syntax"
    - "Students think subagents run automatically — they are invoked via the Task tool or by Claude Code's own reasoning, not by external triggers (that comes in L08 with Watchers)"
    - "Students expect the follow-up tracker to monitor Gmail in real-time — it analyzes sent emails on demand, not continuously (continuous monitoring is Silver tier)"
  discussion_prompts:
    - "The inbox-triager checks sender, subject, deadlines, recipient field, and action indicators. Which factor would YOU weight most heavily in your own inbox, and why?"
    - "The response-suggester always provides 3 options (brief, detailed, alternative). In what scenario would the 'alternative' option (defer/redirect) be the best choice?"
    - "Using the skills vs subagents decision framework, classify these tasks: formatting a report, deciding which bugs to fix first, generating a weekly summary"
  teaching_tips:
    - "Start with the skills vs subagents comparison table — students who do not grasp this distinction will misuse both patterns in every subsequent lesson"
    - "The inbox-triager's 5-step classification logic is the lesson's best whiteboard moment — walk through each step with a real email example"
    - "Have students create the inbox-triager FIRST and test it before building the other two — early success builds confidence for the more complex agents"
    - "The CC'd email from CFO in the test examples (marked Normal despite senior sender) is a great discussion point about why multi-factor reasoning beats simple rules"
  assessment_quick_check:
    - "When should you use a skill vs a subagent? Give one example of each."
    - "What happens if you use multi-line YAML in an agent description? (Parser breaks)"
    - "Classify this email as Urgent/Important/Normal/Low and explain your reasoning: From CEO, CC'd to 15 people, subject 'FY24 Planning Update'"

# Generation metadata
generated_by: "content-implementer v1.0.0"
created: "2026-01-01"
version: "1.0.0"
---

# Hiring Specialists

Your inbox receives 80 emails before lunch. Client requests mixed with newsletters. Urgent deadline reminders buried under automated notifications. Meeting follow-ups you've forgotten to send. Every day starts with the same mental labor: What matters? What can wait? What have I forgotten?

Skills helped you draft consistent emails. Templates gave you reusable structures. But drafting isn't the bottleneck—**triage is**. The cognitive load of deciding which emails demand immediate attention, which need thoughtful responses, and which sent messages are overdue for follow-up. These decisions require reasoning, not just following instructions.

This lesson introduces **subagents**—autonomous components that reason through complex decisions on your behalf. You'll build three subagents that transform inbox chaos into structured action: one that prioritizes incoming messages, one that suggests response options, and one that tracks what you've sent and when to follow up. By the end, your Email Assistant will not just write emails—it will help you **think** about them.

---

## Skills vs Subagents: The Core Distinction

You've built skills that guide consistent execution. Skills are like recipe cards: follow the steps, get predictable results. But what happens when the "recipe" depends on analyzing the situation first?

| Characteristic | Skills | Subagents |
|----------------|--------|-----------|
| **Primary function** | Guidance for consistent execution | Autonomous reasoning and classification |
| **Decision points** | 2-4 (simple branching) | 5+ (complex analysis) |
| **Output type** | Predictable format | Context-dependent conclusions |
| **User interaction** | User triggers directly with `/skill-name` | System delegates via Task tool |
| **Best for** | Templates, tone guidelines, formatting | Classification, prioritization, analysis |

**The key insight**: Skills tell Claude *how* to do something. Subagents tell Claude *what* to do after analyzing a situation.

Consider prioritizing an email. A skill might say "Urgent emails come from the CEO." But that's a single rule. Real prioritization requires analyzing:
- Who sent it?
- What's the subject about?
- Is there a deadline mentioned?
- Am I in the TO: or CC: field?
- Does the thread reference a project I'm leading?

That's 5+ decision points requiring contextual analysis. That's a subagent.

---

## Agent Definition Format

Subagents live in `.claude/agents/` as individual markdown files. The format is strict—Claude Code parses these files to understand agent capabilities.

**Directory structure:**

```
.claude/agents/
├── inbox-triager.md
├── response-suggester.md
└── follow-up-tracker.md
```

**Critical: Single-line description requirement**

The YAML frontmatter has a strict format. Multi-line descriptions break Claude Code's parser:

```yaml
# WRONG - Multi-line breaks parsing
---
name: inbox-triager
description: |
  This agent classifies emails by priority.
  It analyzes sender, subject, and content.
model: sonnet
---

# CORRECT - Single line (can be long)
---
name: inbox-triager
description: Classifies emails by priority (Urgent/Important/Normal/Low) based on sender, subject, and content signals. Use when triaging inbox or batch-processing emails.
model: sonnet
tools: Read, Grep
---
```

**Required YAML fields:**

| Field | Purpose | Format |
|-------|---------|--------|
| `name` | Agent identifier (used in Task tool) | lowercase-with-hyphens |
| `description` | When to use this agent (activation trigger) | Single line, max 1024 chars |
| `model` | Which model to use | `sonnet`, `opus`, `haiku` |
| `tools` | Comma-separated tool access | `Read, Grep, Glob, Edit` |

**Output:**

When you create a valid agent file:

```bash
cat .claude/agents/inbox-triager.md
```

```
---
name: inbox-triager
description: Classifies emails by priority...
model: sonnet
tools: Read, Grep
---

# Inbox Triager
...
```

---

## Building the Inbox Triager Subagent

The inbox triager analyzes incoming emails and classifies them into four priority levels. This isn't a simple keyword match—it requires reasoning about context.

Create `.claude/agents/inbox-triager.md`:

```markdown
---
name: inbox-triager
description: Classifies emails by priority (Urgent/Important/Normal/Low) based on sender, subject, and content signals. Use when triaging inbox or batch-processing emails.
model: sonnet
tools: Read, Grep
---

# Inbox Triager

## Purpose

Classify incoming emails into priority categories for efficient inbox management.

## Priority Levels

### Urgent (respond within hours)

**Signals:**
- From: Direct manager, C-level executives, key clients
- Subject contains: "URGENT", "ASAP", "deadline today", "escalation"
- Explicit same-day deadlines in body
- You are the sole recipient (TO:, not CC:)

**Action:** Immediate attention required

### Important (respond within 24 hours)

**Signals:**
- From: Team members, project stakeholders, active clients
- Subject contains: Decision needed, blocker mentioned, meeting-related
- References active projects you own
- Request requires your specific input

**Action:** Handle during focused work time

### Normal (respond within 2-3 days)

**Signals:**
- From: Cross-functional teams, vendors, extended network
- FYI or status update content
- Routine requests without urgency
- Multiple recipients (your input is one of many)

**Action:** Batch process during email time

### Low (respond when convenient)

**Signals:**
- From: Newsletters, automated systems, mass distribution
- No action required, purely informational
- Can be archived for reference
- Unsubscribe candidate

**Action:** Archive or process weekly

## Classification Logic

When analyzing an email, follow this sequence:

1. **Check sender against priority contacts**
   - Direct reports → minimum Important
   - Manager/executives → minimum Important, often Urgent
   - Key clients (by domain or name) → minimum Important

2. **Scan subject for urgency signals**
   - Explicit urgency words → elevate priority
   - Project names you own → minimum Important
   - Meeting or deadline references → evaluate timeline

3. **Analyze body for deadlines**
   - Today/tomorrow → Urgent
   - This week → Important
   - No deadline mentioned → Normal or Low

4. **Check recipient field**
   - TO: (sole recipient) → elevate priority
   - TO: (one of few) → maintain priority
   - CC: (copied for awareness) → lower priority

5. **Look for action indicators**
   - Questions directed at you → elevate priority
   - "FYI" or "No action needed" → lower priority
   - Approval requests → minimum Important

## Output Format

Present results in a scannable table:

| Priority | From | Subject | Reason |
|----------|------|---------|--------|
| Urgent | boss@company.com | Q4 Numbers - Need by 3pm | Explicit deadline, direct manager |
| Important | pm@team.com | Sprint blocker | Blocker mentioned, project stakeholder |
| Normal | vendor@ext.com | Invoice attached | Routine, no deadline |
| Low | news@industry.com | Weekly digest | Newsletter, FYI only |

## Context Awareness

- Consider time of day when evaluating "end of day" deadlines
- Account for time zones in deadline interpretation
- Note recurring senders who always mark things urgent (calibrate)
- Flag emails that seem important but sender is unknown (ask user)

## Integration

Works with `/email-summarizer` to provide context for important emails.
Feeds into `/response-suggester` for prioritized response generation.
```

**What makes this effective:**

- **Clear priority levels** with specific signals (not vague categories)
- **Decision sequence** that mirrors human reasoning
- **Output format** that's scannable at a glance
- **Context awareness** for edge cases

---

## Building the Response Suggester Subagent

Once you know which emails matter, you need to respond efficiently. The response suggester generates quick reply options with varying tones and approaches.

Create `.claude/agents/response-suggester.md`:

```markdown
---
name: response-suggester
description: Suggests 2-3 quick response options for emails with different tones (brief/detailed, formal/casual). Use when user needs help crafting replies efficiently.
model: sonnet
tools: Read
---

# Response Suggester

## Purpose

Generate quick response options to speed up email replies while maintaining quality and appropriate tone.

## Response Types

### Quick Acknowledgment

For FYI emails or simple confirmations:

> - "Thanks for the update!"
> - "Got it, will review."
> - "Noted - I'll circle back if questions."

### Acceptance/Confirmation

For meeting requests, proposals, approvals:

> - "Works for me. See you then."
> - "Approved - please proceed."
> - "Confirmed for [date/time]."

### Deferral

When you need time to respond properly:

> - "Let me review and get back to you by [date]."
> - "Good question - need to check with [person] first."
> - "Can we discuss this in our 1:1?"

### Clarification Request

When more information is needed:

> - "Quick clarification - did you mean X or Y?"
> - "Before I proceed, can you confirm [detail]?"
> - "What's the deadline for this?"

### Decline/Redirect

When the request isn't for you:

> - "I'm not the right person for this - try [name]."
> - "Unfortunately I can't commit to this timeline."
> - "This isn't something I can prioritize right now."

## Output Format

For each email, provide exactly 3 options:

**Option 1 (Brief):** 1-2 sentences, quick response for time efficiency

**Option 2 (Detailed):** Full response with context and explanation

**Option 3 (Alternative):** Different approach (defer, clarify, redirect, etc.)

## Tone Matching

Before generating responses, analyze:

1. **Sender's formality level**
   - Formal greeting → mirror formality
   - Casual tone → can be conversational
   - New contact → err toward professional

2. **Thread conventions**
   - Match length of previous exchanges
   - Follow established tone patterns
   - Maintain consistency within thread

3. **User's voice**
   - Reference tone guidelines from /email-drafter skill if available
   - Maintain signature style (Best/Thanks/Cheers)
   - Preserve personal touches user typically uses

## Urgency Handling

Adjust response suggestions based on email priority:

| Priority | Response Approach |
|----------|------------------|
| Urgent | Lead with action/answer, details optional |
| Important | Complete response with next steps |
| Normal | Standard professional response |
| Low | Quick acknowledgment sufficient |

## Context Analysis

Before suggesting responses, identify:

- What is being asked? (Question, request, FYI)
- What action is expected? (Reply, approval, information)
- What constraints exist? (Deadline, dependencies)
- What's the relationship? (Manager, peer, client, vendor)

## Quality Checks

Each suggested response must:

- Answer the core question or address the request
- Match appropriate formality level
- Include clear next step if action is needed
- Respect user's established voice patterns
- Be complete enough to send as-is (with minor personalization)

## Integration

Uses `/email-drafter` tone guidelines for voice consistency.
Receives priority context from `inbox-triager` agent.
Outputs can be sent directly via Gmail MCP.
```

**Key design decisions:**

- **Three distinct options** give choice without overwhelming
- **Tone matching** ensures responses fit the context
- **Ready-to-send quality** means minimal editing needed

---

## Building the Follow-Up Tracker Subagent

The emails you send need tracking too. The follow-up tracker identifies which sent messages need attention and when.

Create `.claude/agents/follow-up-tracker.md`:

```markdown
---
name: follow-up-tracker
description: Tracks sent emails that need follow-up by analyzing implicit and explicit deadlines. Identifies which emails need follow-up and when. Use for inbox zero maintenance.
model: sonnet
tools: Read, Grep
---

# Follow-Up Tracker

## Purpose

Ensure no sent emails fall through the cracks by tracking expected response times and alerting when follow-up is needed.

## Deadline Detection

### Explicit Deadlines

Direct mentions of dates or times:

- "Please respond by Friday"
- "Need this by EOD"
- "Deadline: March 15"
- "Before our meeting on Tuesday"

### Implicit Deadlines

Context-based urgency without explicit dates:

| Email Type | Implicit Deadline |
|------------|-------------------|
| Meeting-related | Before meeting date |
| Proposal sent | 5-7 business days |
| First outreach | 7 days |
| Second follow-up | 14 days from first |
| Urgent request | 24-48 hours |
| Partnership inquiry | 10-14 days |

### No Follow-Up Needed

Recognize when tracking isn't required:

- FYI or informational emails
- Emails explicitly marked "no reply needed"
- Thank you or closing messages
- Automated notifications
- Emails where you're CC'd

## Follow-Up Schedule

Recommended timing based on email type:

| Email Type | First Follow-Up | Second Follow-Up | Final |
|------------|----------------|------------------|-------|
| Cold outreach | Day 7 | Day 14 | Day 21 |
| Warm intro | Day 5 | Day 10 | Day 15 |
| Proposal | Day 5 | Day 10 | Day 14 |
| Meeting request | Day 3 | Day 7 | Day 10 |
| Urgent request | Day 2 | Day 4 | Day 7 |
| Internal team | Day 3 | Day 7 | - |

## Tracking Logic

When analyzing sent emails:

1. **Identify email type** from subject and content
2. **Extract explicit deadlines** if present
3. **Calculate implicit deadline** based on email type
4. **Check for responses** in inbox
5. **Determine follow-up status**:
   - Overdue (past deadline, no response)
   - Due today (deadline is today)
   - Due soon (within 2 days)
   - On track (before deadline)
   - Resolved (response received)

## Output Format

Present tracking status in actionable format:

| Email | Sent | Follow-Up Due | Status |
|-------|------|---------------|--------|
| Partnership proposal to Marcus | Dec 20 | Dec 27 | ⚠️ Due today |
| Meeting request to Sarah | Dec 23 | Dec 28 | ⏰ Due in 1 day |
| Cold outreach to Alex | Dec 15 | Dec 22 | ❌ Overdue (5 days) |
| Quarterly update to team | Dec 24 | - | ✅ No follow-up needed |

## Actions

For each tracked email, suggest:

- **Overdue**: Generate follow-up email using /email-templates
- **Due today**: Prioritize in today's task list
- **Due soon**: Schedule for upcoming follow-up
- **Resolved**: Mark as closed, remove from tracking

## Response Detection

Identify when email has been answered:

- Direct reply in inbox (same thread)
- Response from any recipient (not just TO:)
- Meeting scheduled (for meeting requests)
- Action taken (for approval requests)

Mark as "Closed - [response type]" when detected.

## Weekly Summary

Generate weekly overview:

> **Follow-Up Summary (Week of Dec 22)**
>
> Overdue (need immediate attention): 2
> Due this week: 5
> On track: 8
> Closed this week: 12
>
> **Top priority follow-ups:**
> 1. Partnership proposal to Marcus (overdue 5 days)
> 2. Meeting request to Sarah (due tomorrow)

## Integration

Uses Gmail MCP to scan sent folder and inbox.
Triggers `/email-templates follow-up` for follow-up drafting.
Works with `inbox-triager` to correlate sent/received.
```

**Design rationale:**

- **Implicit deadline detection** handles the common case (no explicit deadline stated)
- **Status symbols** (⚠️ ❌ ⏰ ✅) enable quick scanning
- **Action suggestions** turn tracking into doing

---

## The Decision Framework: Skills vs Subagents

With three subagents built, you can now apply a clear decision framework for future automation:

| Use SKILL when... | Use SUBAGENT when... |
|-------------------|----------------------|
| Task is content generation | Task requires reasoning/classification |
| Output format is predictable | Output depends on analysis |
| User triggers directly (`/skill`) | System triggers automatically |
| Reusable template applies | Custom logic for each case |
| 2-4 decision points | 5+ decision points |
| Same steps every time | Steps vary by context |

**Practical examples:**

| Task | Component | Reasoning |
|------|-----------|-----------|
| Draft email with consistent tone | Skill | Predictable format, user-triggered |
| Prioritize 50 inbox emails | Subagent | Analysis required, context-dependent output |
| Apply follow-up template | Skill | Template substitution, predictable steps |
| Decide which emails need follow-up | Subagent | Deadline detection requires reasoning |
| Format meeting notes | Skill | Structure is consistent |
| Classify customer support tickets | Subagent | Category depends on content analysis |

---

## Testing Your Subagents

With all three agents created, test them using the Task tool:

**Test inbox-triager:**

```
Use the inbox-triager agent to classify these emails:

1. From: ceo@company.com
   Subject: Board meeting prep - need numbers by 2pm
   Body: Please send Q4 projections before board meeting.

2. From: newsletter@techsite.com
   Subject: This week in AI
   Body: Top stories from the AI world...

3. From: teammate@company.com
   Subject: Sprint planning question
   Body: Can you clarify the priority for the API feature?
```

**Expected output:**

```
| Priority | From | Subject | Reason |
|----------|------|---------|--------|
| Urgent | ceo@company.com | Board meeting prep | C-level sender, explicit 2pm deadline |
| Low | newsletter@techsite.com | This week in AI | Newsletter, FYI only |
| Important | teammate@company.com | Sprint planning question | Team member, project-related question |
```

**Test response-suggester:**

```
Use the response-suggester agent for this email:

From: client@bigcorp.com
Subject: Contract renewal timeline
Body: We need to finalize the renewal by end of month. Can you
confirm your team's capacity for the expanded scope?
```

**Expected output:**

```
**Option 1 (Brief):**
Thanks for reaching out. Yes, we can handle the expanded scope.
I'll send capacity details by Thursday.

**Option 2 (Detailed):**
Thanks for the renewal discussion. We've reviewed the expanded scope
and can confirm capacity. Our team can absorb the additional work
starting Q1. I'll prepare a detailed capacity breakdown by Thursday
for your review before month-end signing.

**Option 3 (Alternative - Clarification):**
Before I confirm capacity, could you share the specific scope
additions you're considering? That will help me give you an
accurate timeline for the expanded engagement.
```

---

## Your Complete Agent Architecture

You now have three specialized subagents:

```
.claude/agents/
├── inbox-triager.md      → Prioritizes incoming emails (5+ decision points)
├── response-suggester.md → Generates reply options (tone analysis)
└── follow-up-tracker.md  → Tracks sent email deadlines (implicit + explicit)
```

Combined with your skills from previous lessons:

```
.claude/skills/
├── email-drafter/        → Consistent email voice
├── email-templates/      → Reusable email structures
└── email-summarizer/     → Thread parsing and action extraction
```

This architecture separates concerns:
- **Skills** handle consistent execution (templates, formatting, tone)
- **Subagents** handle reasoning (classification, prioritization, deadline detection)

The orchestration layer (Lesson 6) will combine these into a complete workflow.

---

## Try With AI

**Setup:** Ensure you have all three agent files created in `.claude/agents/`

**Prompt 1: Test Priority Classification**

```
I have 5 unread emails. Use the inbox-triager agent to classify them:

1. From: direct-manager@company.com
   Subject: Quick question about Friday's presentation
   Body: Do you have the latest revenue slides?

2. From: random-recruiter@linkedin.com
   Subject: Exciting opportunity!
   Body: Your profile caught my attention...

3. From: key-client@bigcorp.com
   Subject: URGENT - Production issue
   Body: Our API integration is returning errors. Need immediate help.

4. From: teammate@company.com
   Subject: Coffee chat next week?
   Body: Haven't caught up in a while. Free Tuesday?

5. From: cfo@company.com (CC: you and 12 others)
   Subject: FY24 Planning Update
   Body: Attached is the latest planning document for review.
```

**What you're learning:** The inbox-triager applies multi-factor analysis. Notice how it weighs sender importance against content urgency. The CC'd email from CFO is NOT urgent despite the senior sender—being CC'd lowers priority.

**Prompt 2: Compare Response Approaches**

```
Use the response-suggester for this challenging email:

From: frustrated-client@company.com
Subject: RE: Delayed deliverable
Body: This is the third time the deadline has slipped. I need to
understand what's happening and when we can realistically expect
delivery. My leadership is asking questions.

Generate 3 response options that balance empathy with professionalism.
```

**What you're learning:** The response-suggester adapts to emotional context. Each option should address the frustration while providing actionable information. Compare the brief vs detailed approaches—which fits your communication style?

**Prompt 3: Design Your Own Classification Logic**

```
I want to add a new classification to my inbox-triager: "Delegate"
for emails that should be forwarded to someone else on my team.

Help me define:
1. What signals indicate an email should be delegated?
2. What information should the output include for delegation?
3. How does this interact with the existing priority levels?

Update my inbox-triager agent definition with this new category.
```

**What you're learning:** Subagent design is iterative. You're extending the classification logic based on your actual workflow. This is Layer 3 in action—transforming tacit knowledge (you know which emails to delegate) into explicit, reusable intelligence.

**Safety Note:** Subagents can process emails quickly, but always review their classifications before taking action. Priority systems should augment your judgment, not replace it. An email misclassified as "Low" priority could contain something important that the automated analysis missed.
