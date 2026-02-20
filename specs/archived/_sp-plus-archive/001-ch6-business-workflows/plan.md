# Implementation Plan: Chapter 6 - Building a Complete Email Assistant

**Created**: 2026-01-01
**Source Spec**: specs/001-ch6-business-workflows/spec.md
**Chapter Path**: apps/learn-app/docs/02-AI-Tool-Landscape/06-business-workflow-and-social-media/
**Part**: 2 - AI Tool Landscape
**Proficiency Level**: A2-B1 (Elementary to Intermediate) - Progressive skill building
**Total Lessons**: 7 (6 content + 1 quiz)
**Revision Note**: Complete rewrite to align with spec revision (Skills + Subagents + MCP)

---

## I. Chapter Type Classification

**Type**: Technical/Code-Focused (Hands-On Skill Building)

**Recognition signals**:
- Focus on building skills (4 skills), subagents (3 agents), and MCP integration
- Learning objectives use "apply/create/implement" verbs
- Code examples required for skill YAML, agent definitions, orchestration logic
- Deliverables are working artifacts (skills, agents, configurations)

**Structure**: Sequential lessons with progressive complexity
- Lessons 1-3: Individual skills (building blocks)
- Lesson 4: Custom subagents (specialized workers)
- Lesson 5: MCP integration (external connectivity)
- Lesson 6: Orchestration (capstone integration)
- Lesson 7: Quiz (validation)

---

## II. Concept Density Analysis

### Core Concepts Identified (from spec)

**Skills Domain** (7 concepts):
1. SKILL.md file format (YAML frontmatter, markdown body)
2. Skill directory structure (.claude/skills/[name]/SKILL.md)
3. Tone specification in references/
4. Template design with variable substitution
5. Template library organization
6. Thread summarization patterns
7. Extraction targets (decisions, action items, questions)

**Subagents Domain** (6 concepts):
1. Agent definition format (.claude/agents/[name].md)
2. Single-line description requirement
3. Task tool for delegation
4. Priority classification logic
5. Response suggestion patterns
6. Follow-up tracking with deadlines

**MCP Domain** (4 concepts):
1. Gmail MCP server tools (19 available)
2. SMTP vs OAuth authentication
3. Safety protocols (draft-first)
4. MCP configuration (.mcp.json or claude mcp add)

**Orchestration Domain** (5 concepts):
1. Master skill pattern
2. Delegation logic (when to use which component)
3. Workflow sequencing (Triage -> Suggest -> Draft -> Send)
4. Error handling and graceful degradation
5. Component composition

**Total Core Concepts**: 22 concepts across 7 lessons

### Justified Lesson Count

**Proficiency Tier**: A2-B1 (Part 2, Tool Landscape)
- A2 lessons (L1-L3): Max 5-7 concepts
- B1 lessons (L4-L6): Max 7-10 concepts

**Concept Distribution**:
| Lesson | New Concepts | Proficiency | Validation |
|--------|--------------|-------------|------------|
| L1: Email Drafter Skill | 5 (project setup, SKILL.md format, directory structure, tone spec, skill invocation) | A2 | 5 <= 7 |
| L2: Email Templates Skill | 5 (template design, variable substitution, template library, template selection, references dir) | A2 | 5 <= 7 |
| L3: Email Summarizer Skill | 5 (thread parsing, extraction targets, output formatting, combining skills, skill chaining) | A2 | 5 <= 7 |
| L4: Custom Subagents | 7 (agent format, single-line desc, Task tool, inbox-triager, response-suggester, follow-up-tracker, skills vs subagents decision) | B1 | 7 <= 10 |
| L5: Gmail MCP Integration | 6 (Gmail MCP tools, SMTP auth, OAuth auth, testing MCP, safety protocols, MCP + skills integration) | B1 | 6 <= 10 |
| L6: Orchestration Capstone | 8 (master skill pattern, delegation logic, workflow sequencing, error handling, graceful degradation, component composition, end-to-end testing, spec-first orchestration) | B1 | 8 <= 10 |

**All lessons within cognitive load limits.**

---

## III. Pedagogical Layer Progression

### Layer Mapping

| Lesson | Layer | Justification |
|--------|-------|---------------|
| L1: Email Drafter | L1->L2 | Manual setup first (L1), then AI collaboration for tone refinement (L2) |
| L2: Email Templates | L2->L3 | AI collaboration for template design (L2), create reusable skill (L3) |
| L3: Email Summarizer | L2->L3 | AI collaboration for extraction patterns (L2), create reusable skill (L3) |
| L4: Custom Subagents | L3 | Intelligence Design - creating reusable agent components |
| L5: Gmail MCP | L2 + Setup | Technical setup + AI collaboration for testing |
| L6: Orchestration | L4 | Spec-Driven Capstone - compose all components |

### Layer Validation Checklist

- [x] L1: No AI-first in Lesson 1 (manual project setup first)
- [x] L2-L3: Three Roles demonstrations planned for AI collaboration sections
- [x] L4-L5: Reusable artifacts created (agents, MCP config)
- [x] L6: Spec-first pattern for orchestration design
- [x] Progression: L1->L2->L3->L4 without skipping

---

## IV. Success Evals (from Spec)

| ID | Criterion | Measurement | Lessons |
|----|-----------|-------------|---------|
| SC-001 | 4+ working skills created | All skills invocable via `/name` | L1-L3, L6 |
| SC-002 | 3+ working subagents created | Subagents execute via Task tool | L4 |
| SC-003 | Gmail MCP connection works | Can list labels, search emails | L5 |
| SC-004 | Orchestrator coordinates all components | End-to-end workflow executes | L6 |
| SC-005 | System handles edge cases | Graceful error handling | L6 |
| SC-006 | 90% quiz pass rate | Quiz analytics | L7 |
| SC-007 | Skills vs subagents decision mastery | Can articulate decision criteria | L4 |
| SC-008 | System extensibility | Demonstrate adding new template | L2, L6 |

---

## V. Lesson Sequence

### Lesson 1: Project Setup & Email Drafter Skill (30 min)

**File**: `01-project-setup-email-drafter.md`
**Layer**: L1 (Manual Foundation) -> L2 (AI Collaboration)
**Proficiency**: A2
**Bloom's Level**: Apply
**Duration**: 30 minutes

#### Learning Objectives

1. **Set up** the Email Assistant project directory structure with `.claude/skills/` and `.claude/agents/` folders (A2, Apply)
   - Assessment: Student creates correct directory structure
2. **Create** an email-drafter SKILL.md with proper YAML frontmatter (name, description fields) (A2, Apply)
   - Assessment: Skill file passes format validation
3. **Define** tone guidelines in references/tone-guidelines.md for consistent email voice (A2, Apply)
   - Assessment: Tone guidelines include formality, warmth, and length specifications
4. **Invoke** the email-drafter skill to draft a professional email (A2, Apply)
   - Assessment: Generated email matches tone specifications
5. **Refine** skill output through AI collaboration with iterative feedback (A2, Apply)
   - Assessment: Student demonstrates refinement cycle with improved output

#### Concepts Covered

| Concept | How Taught | Evidence |
|---------|-----------|----------|
| Project structure | Manual setup commands | Directory tree verification |
| SKILL.md format | Template with YAML frontmatter | File content inspection |
| Directory structure | `.claude/skills/[name]/SKILL.md` | Correct path creation |
| Tone specification | References file creation | Guidelines document |
| Skill invocation | `/email-drafter` command | Working invocation |

#### Deliverables (Exact File Paths)

```
skills-lab/
├── .claude/
│   └── skills/
│       └── email-drafter/
│           ├── SKILL.md
│           └── references/
│               └── tone-guidelines.md
└── CLAUDE.md
```

#### Code Examples Needed

1. **SKILL.md Template** (email-drafter):
```yaml
---
name: email-drafter
description: This skill should be used when drafting professional emails. Use when the user needs to compose cold outreach, follow-ups, meeting requests, or any professional correspondence. Follows tone guidelines for consistent voice.
---

# Email Drafter

## Overview

Draft professional emails that match your personal tone and communication style.

## When to Use This Skill

- Composing cold outreach emails
- Writing follow-up messages
- Drafting meeting requests
- Any professional email correspondence

## How It Works

1. Read tone guidelines from references/tone-guidelines.md
2. Understand the email context and purpose
3. Draft email matching tone specifications
4. Suggest subject line options

## References

- `references/tone-guidelines.md` - Your personal tone and style preferences
```

2. **Tone Guidelines Template**:
```markdown
# Tone Guidelines

## Formality Level
- **Default**: Professional but approachable
- **First contact**: More formal
- **Follow-ups**: Slightly more casual once relationship established

## Warmth
- Include genuine interest in recipient's work
- Personalize with specific references
- Avoid generic flattery

## Length
- Cold outreach: 3-5 short paragraphs
- Follow-ups: 2-3 paragraphs
- Quick responses: 1-2 paragraphs

## Signature Style
[Your preferred signature format]
```

#### Three Roles Demonstration (L2 Section)

**AI as Teacher**:
- Student: "Help me draft a cold outreach email to a potential client"
- AI suggests: "Based on your tone guidelines, I recommend opening with a specific observation about their recent work. Here's a structure:
  1. Personalized hook (reference their recent project/post)
  2. Value proposition in their context
  3. Soft call-to-action"
- Student learns: Structured approach to cold outreach they hadn't considered

**AI as Student**:
- AI drafts email with default professional tone
- Student: "This sounds too formal for my brand. I'm more conversational."
- AI adapts: "I see - let me adjust. I'll use contractions, shorter sentences, and a more relaxed opening. Does 'Hey [Name], I've been following your work on...' feel more like your voice?"
- AI learns: Student's specific voice preferences

**AI as Co-Worker**:
- Iteration 1: AI draft -> Student: "Good structure, but the CTA is too aggressive"
- Iteration 2: AI refines CTA -> Student: "Better, but add mention of mutual connection"
- Iteration 3: Converged email incorporating both AI's structure and student's voice/context
- Neither had the final version initially - emerged through collaboration

#### Try With AI Exercises (3)

**Exercise 1: First Skill Creation**
```
Create the email-drafter skill structure:
1. Create directory: .claude/skills/email-drafter/
2. Create SKILL.md with proper YAML frontmatter
3. Create references/tone-guidelines.md with your preferences
4. Test by invoking: /email-drafter "Draft a cold outreach to [name] about [topic]"
```
**What you're learning**: How Claude Code discovers and loads skills from the .claude/skills/ directory. The YAML frontmatter provides metadata; the markdown body provides instructions.

**Exercise 2: Tone Refinement Loop**
```
Refine your tone guidelines through iteration:
1. Draft email with current guidelines
2. Identify what doesn't match your voice
3. Update tone-guidelines.md with specific adjustments
4. Re-draft and compare
5. Repeat until email sounds like you
```
**What you're learning**: Skills improve through iteration. The references/ directory acts as persistent memory that Claude loads on each invocation.

**Exercise 3: Professional Scenario**
```
Test your skill on a real scenario:
/email-drafter "Write a follow-up email to [person] who hasn't responded to my proposal about [project] sent 5 days ago"
```
**What you're learning**: How context (person, project, time elapsed) influences email structure and tone. Good skills handle varied inputs gracefully.

---

### Lesson 2: Email Templates Skill (25 min)

**File**: `02-email-templates-skill.md`
**Layer**: L2 (AI Collaboration) -> L3 (Intelligence Design)
**Proficiency**: A2
**Bloom's Level**: Apply
**Duration**: 25 minutes

#### Learning Objectives

1. **Design** email templates with placeholder variables for reusable content (A2, Apply)
   - Assessment: Template includes proper placeholders like `{{recipient_name}}`
2. **Create** the email-templates SKILL.md with template selection logic (A2, Apply)
   - Assessment: Skill can select appropriate template based on use case
3. **Build** a template library with cold-outreach, follow-up, and meeting-request templates (A2, Apply)
   - Assessment: Three functional templates in templates/ directory
4. **Implement** variable substitution patterns that work with Claude (A2, Apply)
   - Assessment: Variables correctly replaced in output
5. **Combine** templates skill with email-drafter for enhanced drafting (A2, Apply)
   - Assessment: Skills work together seamlessly

#### Concepts Covered

| Concept | How Taught | Evidence |
|---------|-----------|----------|
| Template design | Pattern with placeholders | Template file structure |
| Variable substitution | `{{variable}}` syntax | Working substitution |
| Template library | templates/ directory organization | Multiple template files |
| Template selection | Match-case logic in skill | Correct template chosen |
| Skill combination | Chaining skills together | Drafter uses templates |

#### Deliverables (Exact File Paths)

```
.claude/skills/
└── email-templates/
    ├── SKILL.md
    └── templates/
        ├── cold-outreach.md
        ├── follow-up.md
        └── meeting-request.md
```

#### Code Examples Needed

1. **Email Templates SKILL.md**:
```yaml
---
name: email-templates
description: This skill should be used when composing emails from templates. Use when the user needs a structured email for common scenarios like cold outreach, follow-ups, or meeting requests. Provides consistent structure with customizable variables.
---

# Email Templates

## Overview

Apply structured email templates with variable substitution for consistent, professional communication.

## When to Use This Skill

- Cold outreach to new contacts
- Follow-up emails after meetings or proposals
- Meeting request emails
- Any recurring email pattern

## Template Selection Logic

| Scenario | Template |
|----------|----------|
| First contact with potential client/partner | cold-outreach.md |
| No response after initial contact | follow-up.md |
| Scheduling a meeting | meeting-request.md |

## Variables

All templates use `{{variable_name}}` syntax:
- `{{recipient_name}}` - Person's name
- `{{company}}` - Their company
- `{{topic}}` - Subject matter
- `{{your_name}}` - Your name
- `{{your_company}}` - Your company
- `{{date}}` - Proposed date (for meetings)
- `{{duration}}` - Meeting length
```

2. **Cold Outreach Template** (`templates/cold-outreach.md`):
```markdown
# Cold Outreach Template

## Subject Options
- "Quick question about {{topic}}"
- "{{your_company}} + {{company}} collaboration?"
- "Idea for {{company}}"

## Body

Hi {{recipient_name}},

I noticed [specific observation about their work/company]. [Why this resonated with you or relates to your work].

At {{your_company}}, we [brief value proposition relevant to their context]. [One specific way this could benefit them].

Would you be open to a brief conversation about {{topic}}? I'd love to hear your perspective on [related question that shows genuine interest].

Best,
{{your_name}}
```

3. **Follow-Up Template** (`templates/follow-up.md`):
```markdown
# Follow-Up Template

## Subject Options
- "Following up on {{topic}}"
- "Quick follow-up"
- "Circling back on {{topic}}"

## Body

Hi {{recipient_name}},

I wanted to follow up on my previous message about {{topic}}. I understand you're busy, so I'll keep this brief.

[One-sentence reminder of the value proposition or question].

Would [specific day/time] or [alternative day/time] work for a quick chat? Happy to work around your schedule.

Best,
{{your_name}}
```

#### Three Roles Demonstration (L2 Section)

**AI as Teacher**:
- Student: "How should I structure email templates for reuse?"
- AI suggests: "I recommend separating structure from content:
  1. Use `{{variables}}` for all personalized elements
  2. Keep opening/closing formulas consistent
  3. Create subject line OPTIONS not a single subject
  4. Add usage notes for each template"
- Student learns: Template design patterns for maximum reusability

**AI as Student**:
- AI creates template with generic placeholders
- Student: "I need industry-specific placeholders - I work in SaaS sales"
- AI adapts: "Adding SaaS-specific variables:
  - `{{their_product}}` - Their software product
  - `{{integration_type}}` - How you'd integrate
  - `{{pain_point}}` - Common problem you solve"
- AI learns: Domain-specific customization requirements

**AI as Co-Worker**:
- Iteration 1: Template too long -> Student: "Trim to 3 paragraphs max"
- Iteration 2: Variables too complex -> Student: "Simplify to essentials only"
- Iteration 3: Converged template with right balance of structure and flexibility

#### Try With AI Exercises (3)

**Exercise 1: Template Creation**
```
Create the email-templates skill with three templates:
1. Build skill directory structure
2. Create cold-outreach.md with {{variables}}
3. Create follow-up.md and meeting-request.md
4. Test: /email-templates "Use cold-outreach for [person] at [company] about [topic]"
```
**What you're learning**: Templates separate structure from content. Variables make templates reusable across hundreds of similar emails.

**Exercise 2: Template Customization**
```
Customize templates for your industry:
1. Identify 3-5 industry-specific variables you need
2. Add them to your templates
3. Test with a real scenario from your work
4. Refine based on output quality
```
**What you're learning**: Generic templates become powerful when customized for your domain. The skill becomes YOUR competitive advantage.

**Exercise 3: Template Library Expansion**
```
Add a new template type:
1. Choose a recurring email you send (e.g., project-update, thank-you, introduction)
2. Create the template file in templates/
3. Add the scenario to SKILL.md selection logic
4. Test the new template
```
**What you're learning**: Skill extensibility. Your skill library grows as you identify patterns in your work.

---

### Lesson 3: Email Summarizer Skill (25 min)

**File**: `03-email-summarizer-skill.md`
**Layer**: L2 (AI Collaboration) -> L3 (Intelligence Design)
**Proficiency**: A2
**Bloom's Level**: Apply
**Duration**: 25 minutes

#### Learning Objectives

1. **Design** extraction patterns for email thread analysis (decisions, action items, questions) (A2, Apply)
   - Assessment: Extraction patterns document in references/
2. **Create** the email-summarizer SKILL.md for thread summarization (A2, Apply)
   - Assessment: Skill correctly identifies extraction targets
3. **Implement** output formatting for different use cases (brief summary, detailed analysis, action list) (A2, Apply)
   - Assessment: Multiple output formats available
4. **Parse** email thread structure identifying sender, timestamps, and content boundaries (A2, Apply)
   - Assessment: Correct thread parsing in multi-email chains
5. **Combine** summarizer output with email-drafter for response generation (A2, Apply)
   - Assessment: Summarizer informs drafter for contextual responses

#### Concepts Covered

| Concept | How Taught | Evidence |
|---------|-----------|----------|
| Thread parsing | Pattern recognition in email chains | Correct sender/content extraction |
| Extraction targets | Decisions, action items, questions | Categorized output |
| Output formatting | Multiple format options | Format selection working |
| Skill chaining | Summarizer -> Drafter flow | Integrated response generation |
| Reference patterns | extraction-patterns.md | Pattern file creation |

#### Deliverables (Exact File Paths)

```
.claude/skills/
└── email-summarizer/
    ├── SKILL.md
    └── references/
        └── extraction-patterns.md
```

#### Code Examples Needed

1. **Email Summarizer SKILL.md**:
```yaml
---
name: email-summarizer
description: This skill should be used when analyzing email threads. Use when the user needs to summarize long conversations, extract action items, identify decisions made, or find open questions. Helps prepare informed responses.
---

# Email Summarizer

## Overview

Analyze and summarize email threads, extracting key information for quick understanding and response preparation.

## When to Use This Skill

- Summarizing long email threads before responding
- Extracting action items from meeting follow-ups
- Identifying decisions made across multiple messages
- Finding open questions that need answers
- Preparing to delegate email responses

## Extraction Targets

| Target | Description | Output Format |
|--------|-------------|---------------|
| Decisions | Agreements, choices made | Bullet list with who decided, what, when |
| Action Items | Tasks assigned or mentioned | Task, owner, deadline (if stated) |
| Open Questions | Unanswered questions | Question, who asked, context |
| Key Points | Main topics discussed | Brief summary of each topic |
| Tone/Urgency | Overall thread sentiment | Urgency level (low/medium/high) |

## Output Formats

### Brief Summary (default)
- 2-3 sentence overview
- Top 3 action items
- Urgency level

### Detailed Analysis
- Full extraction of all targets
- Timeline of the conversation
- Relationship dynamics noted

### Action List Only
- Just the action items
- Owners and deadlines
- Suggested priority order

## References

See `references/extraction-patterns.md` for detailed extraction logic.
```

2. **Extraction Patterns Reference**:
```markdown
# Email Thread Extraction Patterns

## Decision Indicators
Look for phrases signaling decisions:
- "Let's go with..."
- "We've decided to..."
- "I'll approve..."
- "The plan is to..."
- "We agreed that..."

## Action Item Indicators
Look for phrases signaling tasks:
- "Can you..." / "Could you..."
- "Please [verb]..."
- "I'll [verb]..."
- "ACTION:" or "TODO:"
- "By [date]..."
- "Next steps:"

## Question Indicators
Look for:
- Question marks (?)
- "What do you think about..."
- "Should we..."
- "Have you considered..."
- Unanswered questions from previous messages

## Urgency Indicators
- **High**: "URGENT", "ASAP", "immediately", deadline within 24h
- **Medium**: "this week", "soon", "when you can"
- **Low**: "whenever", "no rush", "FYI"
```

#### Three Roles Demonstration (L2 Section)

**AI as Teacher**:
- Student provides long email thread
- AI suggests: "I notice several patterns in this thread:
  1. There's an implicit action item in paragraph 3 (no 'please' but clearly a request)
  2. The question in email 2 was never answered
  3. There's a soft deadline hidden in 'before the quarterly review'
  Let me show you how to spot these patterns..."
- Student learns: Email analysis beyond obvious keywords

**AI as Student**:
- AI extracts action items
- Student: "You missed the action item about the budget - in my company 'loop in finance' always means I need to send them the spreadsheet"
- AI adapts: "I see - 'loop in' in your context means active action, not just CC'ing. I'll treat that pattern as an action item going forward."
- AI learns: Organization-specific language patterns

**AI as Co-Worker**:
- Iteration 1: Summary too detailed -> Student: "I just need the 3 most critical items"
- Iteration 2: Priorities unclear -> AI: "Should I rank by deadline or by sender seniority?"
- Iteration 3: Converged format matching student's decision-making needs

#### Try With AI Exercises (3)

**Exercise 1: Create the Summarizer Skill**
```
Build the email-summarizer skill:
1. Create skill directory structure
2. Write SKILL.md with extraction targets
3. Create references/extraction-patterns.md
4. Test with a sample email thread (copy-paste or describe)
```
**What you're learning**: Skills can process complex unstructured input (email threads) and produce structured output (categorized extractions).

**Exercise 2: Multi-Format Output**
```
Test different output formats on the same thread:
1. /email-summarizer "Brief summary of this thread: [paste thread]"
2. /email-summarizer "Detailed analysis of this thread: [paste thread]"
3. /email-summarizer "Just action items from: [paste thread]"
Compare which format serves which purpose.
```
**What you're learning**: Skills should offer multiple output modes. Different contexts need different levels of detail.

**Exercise 3: Skill Chaining**
```
Chain summarizer with drafter for informed responses:
1. Summarize a thread that needs a response
2. Use the summary to inform your response strategy
3. Invoke email-drafter with context from the summary
4. Observe how the summary improves response quality
```
**What you're learning**: Skills compound in value when chained. The summarizer's output becomes input for better drafting.

---

### Lesson 4: Creating Custom Subagents (35 min)

**File**: `04-creating-custom-subagents.md`
**Layer**: L3 (Intelligence Design)
**Proficiency**: B1
**Bloom's Level**: Apply/Analyze
**Duration**: 35 minutes

#### Learning Objectives

1. **Explain** the difference between skills and subagents with decision criteria (B1, Analyze)
   - Assessment: Can articulate when to use each
2. **Create** the inbox-triager subagent definition with priority classification logic (B1, Apply)
   - Assessment: Working agent file with correct format
3. **Create** the response-suggester subagent that proposes reply options (B1, Apply)
   - Assessment: Agent generates 2-3 response variations
4. **Create** the follow-up-tracker subagent for deadline management (B1, Apply)
   - Assessment: Agent identifies follow-up needs with dates
5. **Delegate** tasks to subagents using the Task tool (B1, Apply)
   - Assessment: Successful Task tool invocations
6. **Debug** common subagent format issues (single-line description, tool access) (B1, Analyze)
   - Assessment: Can fix format errors independently

#### Concepts Covered

| Concept | How Taught | Evidence |
|---------|-----------|----------|
| Agent definition format | Template and validation | Correct .md file format |
| Single-line description | Requirement with examples | No multi-line descriptions |
| Task tool usage | Delegation examples | Working delegation |
| Skills vs Subagents | Decision framework table | Can choose correctly |
| Inbox classification | Priority logic | Urgent/Important/Normal/Low |
| Response suggestions | Tone variations | Multiple response options |
| Deadline tracking | Date extraction | Follow-up schedule |

#### Skills vs Subagents Decision Framework

| Characteristic | Use a Skill | Use a Subagent |
|----------------|------------|----------------|
| **Stateless** | Yes - each invocation is independent | No - needs to remember context across calls |
| **Single-step** | Yes - one prompt, one output | No - requires multi-step reasoning |
| **User-invoked** | Yes - user types `/skill-name` | Sometimes - often orchestrator-invoked |
| **Template-based** | Often - fills in patterns | Rarely - generates novel approaches |
| **Tool access** | Limited to skill's scope | Full access to specified tools |
| **Autonomous** | No - responds to specific request | Yes - can make decisions and iterate |

**Examples**:
- **Skill**: `/email-drafter` - One request -> one email
- **Subagent**: `inbox-triager` - Analyze batch of emails, classify each, may need to re-check

#### Deliverables (Exact File Paths)

```
.claude/agents/
├── inbox-triager.md
├── response-suggester.md
└── follow-up-tracker.md
```

#### Code Examples Needed

1. **Inbox Triager Agent**:
```yaml
---
name: inbox-triager
description: Classifies email metadata into priority levels (Urgent/Important/Normal/Low) with reasoning. Use for batch inbox processing.
model: claude-sonnet-4-20250514
tools: Read, Grep
---

# Inbox Triager Agent

## Purpose

Analyze email metadata (sender, subject, snippets) and classify into priority levels for efficient inbox processing.

## Priority Classification

| Level | Criteria | Examples |
|-------|----------|----------|
| **Urgent** | Deadline within 24h, VIP sender, explicit urgency markers | Boss's email about today's meeting, "URGENT" in subject |
| **Important** | Requires action this week, key stakeholder, project-critical | Client questions, team blockers, approval requests |
| **Normal** | Standard business communication, can wait 2-3 days | Regular updates, FYI emails, non-critical requests |
| **Low** | Newsletters, automated notifications, optional reads | Marketing emails, system notifications, CC'd threads |

## Input Format

Provide email metadata as:
- From: [sender]
- Subject: [subject line]
- Snippet: [first 100 characters of body]
- Received: [timestamp]

## Output Format

For each email:
- Priority: [Urgent|Important|Normal|Low]
- Reasoning: [Brief explanation of classification]
- Suggested Action: [Respond today | Review this week | Read when free | Archive]
```

2. **Response Suggester Agent**:
```yaml
---
name: response-suggester
description: Generates 2-3 response options for emails with different tones (concise/detailed, formal/friendly). Use when deciding how to reply.
model: claude-sonnet-4-20250514
tools: Read
---

# Response Suggester Agent

## Purpose

Analyze an email requiring response and generate 2-3 reply options with different approaches.

## Response Variations

| Variation | Tone | Length | Use When |
|-----------|------|--------|----------|
| **Concise** | Professional | 2-3 sentences | Busy, straightforward answer |
| **Detailed** | Thorough | 3-5 paragraphs | Complex topic, important relationship |
| **Friendly** | Warm | 3-4 sentences | Peer, established relationship |

## Output Format

For each email provide:
- Option 1: Concise - [Response text] - Best for: [When to use]
- Option 2: Detailed - [Response text] - Best for: [When to use]
- Option 3: Friendly - [Response text] - Best for: [When to use]
- Recommendation: Option [X] because [reasoning]
```

3. **Follow-Up Tracker Agent**:
```yaml
---
name: follow-up-tracker
description: Identifies sent emails needing follow-up by analyzing implicit/explicit deadlines and response expectations. Outputs follow-up schedule.
model: claude-sonnet-4-20250514
tools: Read, Grep
---

# Follow-Up Tracker Agent

## Purpose

Analyze sent emails to identify which need follow-up, when, and with what approach.

## Follow-Up Triggers

| Trigger | Detection | Suggested Follow-Up |
|---------|-----------|-------------------|
| **Explicit deadline** | "By Friday", "Before the 15th" | Follow-up 1 day after deadline if no response |
| **Question asked** | Direct question requiring answer | Follow-up after 3 business days |
| **Request made** | "Can you...", "Please..." | Follow-up after 5 business days |
| **Proposal sent** | Pricing, proposal, offer | Follow-up after 1 week |
| **Introduction made** | Connected two people | Follow-up after 2 weeks to check outcome |

## Output Format

Categorize by urgency:
- Overdue: [Email subject] to [recipient] - Sent [date], expected by [date], Action: [specific follow-up]
- Due This Week: [Email subject] to [recipient] - Sent [date], follow up by [date], Action: [specific follow-up]
- Coming Up: [Email subject] to [recipient] - Sent [date], follow up by [date], Action: [specific follow-up]
```

#### Try With AI Exercises (3)

**Exercise 1: Create Inbox Triager**
```
Build the inbox-triager agent:
1. Create .claude/agents/inbox-triager.md
2. Include YAML frontmatter (name, description - single line!, model, tools)
3. Add priority classification logic
4. Test with Task tool: "Triage these emails: [list 5 email subjects/senders]"
```
**What you're learning**: Subagents have different format from skills. The single-line description is CRITICAL - multi-line breaks parsing.

**Exercise 2: Create Response Suggester**
```
Build the response-suggester agent:
1. Create agent file with proper format
2. Define 3 response variation styles
3. Test: "Suggest responses for: [paste an email needing reply]"
4. Evaluate which suggestion you'd actually use
```
**What you're learning**: Agents can generate options for human decision-making. The recommendation at the end adds value beyond just listing options.

**Exercise 3: Skills vs Subagents Analysis**
```
For each scenario, decide: Skill or Subagent?
1. Drafting a single thank-you email
2. Processing 50 new emails for priority
3. Generating meeting agenda from thread
4. Tracking which proposals need follow-up
5. Converting email to task list

Explain your reasoning for each.
```
**What you're learning**: The decision framework becomes intuitive with practice. Most single-step, template-based tasks = Skills. Multi-step, decision-heavy tasks = Subagents.

---

### Lesson 5: Gmail MCP Integration (30 min)

**File**: `05-gmail-mcp-integration.md`
**Layer**: L2 (AI Collaboration) + Technical Setup
**Proficiency**: B1
**Bloom's Level**: Apply
**Duration**: 30 minutes

#### Learning Objectives

1. **Describe** the Gmail MCP server capabilities (19 tools for email operations) (B1, Understand)
   - Assessment: Can list key tools and their purposes
2. **Configure** SMTP authentication for Gmail MCP (2-minute setup) (B1, Apply)
   - Assessment: Successful connection test
3. **Configure** OAuth authentication for Gmail MCP (10-minute setup) (B1, Apply)
   - Assessment: Successful OAuth flow completion
4. **Test** Gmail MCP tools (list labels, search emails, create drafts) (B1, Apply)
   - Assessment: Successful tool invocations
5. **Apply** safety protocols for email operations (draft-first pattern) (B1, Apply)
   - Assessment: Demonstrates draft-first workflow before sending
6. **Integrate** MCP tools with previously created skills (B1, Apply)
   - Assessment: Skill can trigger MCP operations

#### Concepts Covered

| Concept | How Taught | Evidence |
|---------|-----------|----------|
| Gmail MCP tools | Tool catalog with examples | Tool invocation working |
| SMTP authentication | Step-by-step with app passwords | Connection successful |
| OAuth authentication | Step-by-step with Google console | OAuth flow complete |
| Safety protocols | Draft-first pattern | Demonstrates safe workflow |
| MCP + Skills integration | Skill triggers MCP tool | End-to-end flow working |
| Sensitive data handling | Best practices | Proper credential management |

#### Gmail MCP Tool Catalog

| Tool | Purpose | Example Use |
|------|---------|-------------|
| `list_labels` | Get all Gmail labels | Verify connection, understand organization |
| `search_emails` | Search inbox with Gmail query syntax | Find emails from specific sender/topic |
| `read_email` | Get full email content by ID | Read email for summarization |
| `draft_email` | Create email draft | Safe pre-send review |
| `send_email` | Send email directly | After draft approval |
| `reply_to_email` | Reply to existing thread | Maintain conversation thread |
| `create_label` | Create new label | Organize inbox |
| `modify_labels` | Add/remove labels from email | Auto-categorization |
| `trash_email` | Move to trash | Clean up processed emails |

#### Code Examples Needed

1. **SMTP Configuration** (2-minute setup):
```bash
# Step 1: Generate Gmail App Password
# Go to: Google Account > Security > 2-Step Verification > App Passwords
# Generate password for "Mail" on "Other (Custom name)" = "Claude Code"

# Step 2: Add Gmail MCP server
claude mcp add gmail --scope user -- npx mcp-remote \
  https://deep-red-marten.fastmcp.app/mcp \
  --header "X-Gmail-Email: your-email@gmail.com" \
  --header "X-Gmail-Password: your-app-password"

# Step 3: Verify connection
# In Claude Code: "List my Gmail labels"
```

2. **OAuth Configuration** (10-minute setup):
```markdown
## OAuth Setup Steps

### 1. Google Cloud Console Setup
1. Go to console.cloud.google.com
2. Create new project or select existing
3. Enable Gmail API
4. Configure OAuth consent screen (External, Testing)
5. Create OAuth 2.0 Client ID (Desktop app)
6. Download credentials.json

### 2. Configure MCP with OAuth
claude mcp add gmail-oauth --scope user -- npx @anthropic/mcp-gmail \
  --credentials-path /path/to/credentials.json

### 3. First-Run Authorization
# Claude Code will open browser for Google sign-in
# Authorize access to Gmail
# Token stored for future sessions
```

3. **Safety Protocol - Draft-First Pattern**:
```markdown
## Draft-First Protocol for Email Operations

NEVER send emails directly. Always:

1. **Draft First**: Use `draft_email` to create draft
2. **Review**: Claude shows draft for human review
3. **Approve**: Human confirms or requests changes
4. **Send**: Only after approval, use `send_email` or send from Gmail UI

### Why This Matters
- Prevents accidental sends of unreviewed content
- Allows human oversight of AI-generated emails
- Creates audit trail of human approval
- Respects principle: AI assists, human decides
```

#### Three Roles Demonstration (L2 Section)

**AI as Teacher**:
- Student: "How do I search for emails effectively with MCP?"
- AI explains: "Gmail has a powerful query syntax. I can teach you patterns:
  - `from:name@company.com` - From specific sender
  - `is:unread` - Unread emails only
  - `after:2024/12/01` - After specific date
  - `has:attachment` - With attachments
  - Combine: `from:boss@company.com is:unread after:2024/12/01`"
- Student learns: Gmail query syntax through MCP

**AI as Student**:
- AI suggests searching "all emails from clients"
- Student: "That's too broad. My clients are tagged with the 'Client-Active' label"
- AI adapts: "Using label filter: `label:Client-Active is:unread`. I'll remember this label is your client indicator."
- AI learns: Student's organization system

**AI as Co-Worker**:
- Iteration 1: Draft email via MCP -> Student: "Subject too long"
- Iteration 2: AI shortens subject -> Student: "Good, now create draft"
- Iteration 3: Draft created, reviewed, student approves -> Send

#### Try With AI Exercises (3)

**Exercise 1: Gmail MCP Connection**
```
Connect Claude Code to your Gmail:
1. Choose authentication method (SMTP is faster, OAuth is more secure)
2. Follow setup steps for your choice
3. Test: "List my Gmail labels"
4. Verify you see your labels in the output
```
**What you're learning**: MCP servers connect Claude to external services. Authentication is the bridge between AI capability and real-world access.

**Exercise 2: Safe Email Operations**
```
Practice the draft-first pattern:
1. "Draft an email to test@example.com with subject 'Test' and body 'This is a test'"
2. Review the draft (DO NOT send - this is practice)
3. "Delete that draft"
4. Reflect: Why is draft-first important for AI email operations?
```
**What you're learning**: Safety protocols prevent mistakes. AI-generated content should always have human review before external action.

**Exercise 3: MCP + Skills Integration**
```
Combine Gmail MCP with your skills:
1. Use email-summarizer to analyze a thread from your inbox
2. Use email-drafter to compose a response
3. Use Gmail MCP to create the draft
4. Review the full workflow from analysis to draft creation
```
**What you're learning**: Skills (expertise) + MCP (connectivity) = powerful workflows. Each piece does what it does best.

#### Note: Gmail Account Fallback

**If student doesn't have Gmail**:
- Can still complete L1-L4 and L6 (skills, subagents, orchestration)
- L5 becomes conceptual with demo videos/screenshots
- Alternative: Use simulated MCP responses for practice

---

### Lesson 6: Orchestrating the Complete System (40 min)

**File**: `06-orchestrating-complete-system.md`
**Layer**: L4 (Spec-Driven Capstone)
**Proficiency**: B1
**Bloom's Level**: Create
**Duration**: 40 minutes

#### Learning Objectives

1. **Write** a specification for the email-assistant orchestrator skill (B1, Create)
   - Assessment: Spec includes intent, constraints, success criteria
2. **Design** delegation logic determining when to use which component (B1, Analyze)
   - Assessment: Clear decision tree for component selection
3. **Implement** the orchestrator skill combining skills, subagents, and MCP (B1, Create)
   - Assessment: Working master skill in .claude/skills/email-assistant/
4. **Create** the complete workflow: Triage -> Suggest -> Draft -> Send (B1, Create)
   - Assessment: End-to-end workflow execution
5. **Handle** errors gracefully when components fail (B1, Apply)
   - Assessment: Graceful degradation demonstrated
6. **Test** the complete system with realistic scenarios (B1, Evaluate)
   - Assessment: Multiple test cases pass

#### Concepts Covered

| Concept | How Taught | Evidence |
|---------|-----------|----------|
| Master skill pattern | Orchestrator SKILL.md | Working orchestrator |
| Delegation logic | Decision tree in skill | Correct component selection |
| Workflow sequencing | Triage->Suggest->Draft->Send | End-to-end execution |
| Error handling | Try/fallback patterns | Graceful degradation |
| Component composition | Skills+Agents+MCP | All components integrated |
| Spec-first design | Write spec before implementation | Spec matches final skill |

#### Specification Template for Orchestrator

```markdown
# Email Assistant Orchestrator Specification

## Intent

Create a master skill that coordinates all email-related components (skills, subagents, MCP) to provide comprehensive inbox management through a single entry point.

## Constraints

- Must work offline (skills/subagents) when MCP is unavailable
- Must apply draft-first safety protocol for all sends
- Must preserve user choice (never send without approval)
- Must handle component failures gracefully
- Should complete common tasks in < 30 seconds

## Success Criteria

| ID | Criterion | Validation |
|----|-----------|------------|
| SC-01 | Invoked with `/email-assistant` | Skill loads correctly |
| SC-02 | Can triage batch of emails | inbox-triager executes |
| SC-03 | Can suggest responses | response-suggester provides options |
| SC-04 | Can draft responses | email-drafter + templates work |
| SC-05 | Can create Gmail drafts | MCP draft_email succeeds |
| SC-06 | Handles MCP unavailability | Graceful offline mode message |
| SC-07 | Applies draft-first for sends | Never auto-sends |
```

#### Deliverables (Exact File Paths)

```
skills-lab/
├── .claude/
│   ├── skills/
│   │   ├── email-drafter/
│   │   │   ├── SKILL.md
│   │   │   └── references/tone-guidelines.md
│   │   ├── email-templates/
│   │   │   ├── SKILL.md
│   │   │   └── templates/
│   │   │       ├── cold-outreach.md
│   │   │       ├── follow-up.md
│   │   │       └── meeting-request.md
│   │   ├── email-summarizer/
│   │   │   ├── SKILL.md
│   │   │   └── references/extraction-patterns.md
│   │   └── email-assistant/         # Orchestrator
│   │       ├── SKILL.md
│   │       └── references/
│   │           └── orchestration-logic.md
│   └── agents/
│       ├── inbox-triager.md
│       ├── response-suggester.md
│       └── follow-up-tracker.md
├── CLAUDE.md
└── .mcp.json                        # Gmail MCP config
```

#### Code Examples Needed

1. **Email Assistant Orchestrator SKILL.md**:
```yaml
---
name: email-assistant
description: This skill should be used for comprehensive email management. Use when the user wants to manage their inbox, process emails, draft responses, or track follow-ups. Orchestrates all email-related skills, subagents, and Gmail MCP.
---

# Email Assistant - Master Orchestrator

## Overview

Your complete Email Digital FTE. Combines specialized skills, intelligent subagents, and Gmail connectivity for end-to-end email management.

## Capabilities

| Command | Components Used | Result |
|---------|-----------------|--------|
| "Manage my inbox" | inbox-triager + Gmail MCP | Prioritized email list |
| "Help me respond to this email" | summarizer + response-suggester + drafter | Response options with drafts |
| "Draft a cold outreach to [person]" | templates + drafter | Professional email ready to send |
| "What needs follow-up?" | follow-up-tracker | Follow-up schedule |
| "Send email to [person] about [topic]" | drafter + Gmail MCP | Draft created for review |

## Delegation Logic

See `references/orchestration-logic.md` for detailed decision tree.

### Quick Reference

- IF needs_batch_processing: Use inbox-triager subagent
- ELIF needs_response_options: Use response-suggester subagent
- ELIF needs_follow_up_analysis: Use follow-up-tracker subagent
- ELIF needs_thread_summary: Use email-summarizer skill
- ELIF needs_template: Use email-templates skill
- ELIF needs_draft: Use email-drafter skill
- ELIF needs_gmail_operation: Use Gmail MCP (with draft-first for sends)

## Error Handling

| Failure | Detection | Fallback |
|---------|-----------|----------|
| Gmail MCP unavailable | Connection timeout | "Gmail offline. I can still draft locally." |
| Subagent fails | Error response | Retry once, then skill-only approach |
| Template not found | No matching template | "Using email-drafter for custom draft." |

## Safety Protocols

- NEVER send emails automatically
- ALWAYS create drafts for review first
- ALWAYS confirm before any Gmail modification
```

2. **Orchestration Logic Reference**:
```markdown
# Orchestration Logic

## Request Classification

When user invokes /email-assistant with a request:

### Intent Classification

| Intent Pattern | Primary Component | Supporting Components |
|----------------|-------------------|----------------------|
| "Manage inbox", "Process emails" | inbox-triager | Gmail MCP (list) |
| "Respond to", "Reply to" | response-suggester | summarizer, drafter |
| "Draft", "Write", "Compose" | email-drafter | templates (if pattern matches) |
| "Summarize", "Analyze thread" | email-summarizer | - |
| "Follow-up", "What's pending" | follow-up-tracker | Gmail MCP (search sent) |
| "Send", "Email [person]" | drafter + Gmail MCP | templates |

### Component Availability Check

Before invoking Gmail MCP:
1. Try list_labels() as connection test
2. If timeout or error: Set gmail_available = false
3. Notify user: "Gmail offline - working locally"

### Workflow Sequencing

Full inbox processing:
1. Triage: inbox-triager classifies emails
2. Prioritize: User selects which to address
3. Analyze: email-summarizer extracts key info
4. Suggest: response-suggester provides options
5. Draft: email-drafter composes response
6. Create Draft: Gmail MCP creates draft
7. Review: User reviews in Gmail
8. Send: User approves -> email sent
```

#### Three Roles Demonstration (L4 Section)

**AI as Teacher**:
- Student: "How do I design the orchestration logic?"
- AI explains: "Think of the orchestrator as a dispatcher:
  1. Receive request
  2. Classify intent (what does the user want?)
  3. Select components (which skills/agents/MCP?)
  4. Execute in sequence (each output feeds the next)
  5. Handle failures (graceful degradation)
  The key insight: orchestrators don't DO the work - they delegate and coordinate."
- Student learns: Orchestration design patterns

**AI as Student**:
- AI creates orchestrator with fixed workflow
- Student: "I want to skip triage sometimes and go straight to drafting"
- AI adapts: "Adding intent classification: If request clearly specifies drafting -> skip triage. Making workflow flexible."
- AI learns: User workflow preferences

**AI as Co-Worker**:
- Iteration 1: Orchestrator -> Student: "Error handling too aggressive, retries slow things down"
- Iteration 2: AI adjusts retry logic -> Student: "Better, but need clearer offline messaging"
- Iteration 3: Converged on balanced error handling with clear user communication

#### Try With AI Exercises (3)

**Exercise 1: Write the Specification**
```
Before implementing, write the spec:
1. Define intent: What does the email-assistant orchestrator do?
2. Define constraints: What rules must it follow?
3. Define success criteria: How do we know it works?
4. List all components it will orchestrate
```
**What you're learning**: Spec-first development. The specification becomes the contract for implementation.

**Exercise 2: Implement the Orchestrator**
```
Build the email-assistant skill:
1. Create .claude/skills/email-assistant/SKILL.md
2. Add references/orchestration-logic.md with decision tree
3. Test: /email-assistant "Manage my inbox"
4. Test: /email-assistant "Help me respond to [email]"
5. Test: /email-assistant "Draft a cold outreach to [person]"
```
**What you're learning**: Master skills coordinate specialized components. The whole is greater than the sum of parts.

**Exercise 3: End-to-End Test**
```
Full workflow test:
1. "Triage my last 10 emails" (inbox-triager + Gmail MCP)
2. Select an email that needs response
3. "Suggest responses for this email" (summarizer + response-suggester)
4. Choose the best option, request draft
5. Review the Gmail draft created
6. Reflect: How many minutes did this save compared to manual?
```
**What you're learning**: Digital FTEs compound productivity. This workflow that took hours manually now takes minutes.

---

### Lesson 7: Chapter Quiz (15 min)

**File**: `07-chapter-quiz.md`
**Duration**: 15 minutes

#### Quiz Structure

**Total Questions**: 15
**Pass Threshold**: 60% (9/15 correct)
**Time Limit**: 15 minutes

#### Question Categories

| Category | Questions | Coverage |
|----------|-----------|----------|
| Skills Format & Creation | 4 | SKILL.md format, directory structure, when to create |
| Subagents | 4 | Agent format, Task tool, skills vs subagents |
| MCP Integration | 3 | Authentication, tools, safety protocols |
| Orchestration | 4 | Component composition, workflow design, error handling |

#### Sample Questions

**Skills Category**:
1. What is the correct directory structure for a skill named "email-drafter"?
   - A) .claude/skills/email-drafter.md
   - B) .claude/skills/email-drafter/SKILL.md (correct)
   - C) .claude/agents/email-drafter.md
   - D) skills/email-drafter/index.md

2. Which YAML fields are required in a SKILL.md frontmatter?
   - A) name, description, version
   - B) name, description (correct)
   - C) name, description, tools
   - D) name, model, skills

**Subagents Category**:
3. What tool is used to delegate tasks to subagents?
   - A) Agent tool
   - B) Task tool (correct)
   - C) Delegate tool
   - D) Run tool

4. When should you use a subagent instead of a skill?
   - A) For single-step, template-based tasks
   - B) For multi-step, autonomous decision-making tasks (correct)
   - C) For faster execution
   - D) For smaller context usage

**MCP Category**:
5. What safety protocol should ALWAYS be applied before sending emails via MCP?
   - A) Password confirmation
   - B) Two-factor authentication
   - C) Draft-first pattern (correct)
   - D) Admin approval

**Orchestration Category**:
6. What happens when Gmail MCP is unavailable in a well-designed orchestrator?
   - A) The entire system fails
   - B) Skills and subagents still work, only Gmail operations are affected (correct)
   - C) The orchestrator retries indefinitely
   - D) The user is locked out

---

## VI. Final System Architecture

```
                        ┌─────────────────────────────────────┐
                        │      /email-assistant               │
                        │      (Master Orchestrator)          │
                        └─────────────────┬───────────────────┘
                                          │
              ┌───────────────────────────┼───────────────────────────┐
              │                           │                           │
              ▼                           ▼                           ▼
    ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
    │     SKILLS      │         │   SUBAGENTS     │         │       MCP       │
    │   (Expertise)   │         │   (Workers)     │         │ (Connectivity)  │
    └────────┬────────┘         └────────┬────────┘         └────────┬────────┘
             │                           │                           │
    ┌────────┼────────┐         ┌────────┼────────┐                  │
    │        │        │         │        │        │                  │
    ▼        ▼        ▼         ▼        ▼        ▼                  ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐    ┌─────────┐
│Drafter│ │Templ- │ │Summa- │ │Inbox  │ │Respon-│ │Follow-│    │  Gmail  │
│       │ │ates   │ │rizer  │ │Triager│ │se     │ │up     │    │   MCP   │
│       │ │       │ │       │ │       │ │Sugg.  │ │Tracker│    │(19tools)│
└───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘    └─────────┘
```

---

## VII. Summary Tables

### Lessons by Layer

| Layer | Lessons | Count |
|-------|---------|-------|
| L1->L2 | 1 | 1 |
| L2->L3 | 2, 3 | 2 |
| L3 | 4 | 1 |
| L2 + Setup | 5 | 1 |
| L4 (Capstone) | 6 | 1 |
| Quiz | 7 | 1 |

### Lessons by Bloom's Level

| Bloom's Level | Lessons | Count |
|---------------|---------|-------|
| Apply | 1, 2, 3, 4, 5 | 5 |
| Analyze | 4, 6 | 2 |
| Create | 6 | 1 |
| Evaluate | 6 | 1 |

### Duration Summary

| Lesson | Duration |
|--------|----------|
| L1: Project Setup & Email Drafter | 30 min |
| L2: Email Templates Skill | 25 min |
| L3: Email Summarizer Skill | 25 min |
| L4: Creating Custom Subagents | 35 min |
| L5: Gmail MCP Integration | 30 min |
| L6: Orchestrating Complete System | 40 min |
| L7: Chapter Quiz | 15 min |
| **Total** | **200 min (~3.3 hours)** |

---

## VIII. Dependency Graph

```
Lesson 1: Project Setup & Email Drafter
    └── Lesson 2: Email Templates
        └── Lesson 3: Email Summarizer
            └── Lesson 4: Custom Subagents
                └── Lesson 5: Gmail MCP Integration
                    └── Lesson 6: Orchestration Capstone
                        └── Lesson 7: Quiz

Prerequisites from Chapter 5:
- Skills Architecture (L5)
- Creating Skills (L6-L7)
- MCP Fundamentals (L9)
- Compiling MCP to Skills (L10)
- Subagents & Orchestration (L11)
```

---

## IX. Implementation Checklist

For each lesson, implementer must:

- [ ] Include full YAML frontmatter (sidebar_position, title, description, keywords, skills, learning_objectives, cognitive_load, differentiation)
- [ ] Write compelling narrative opening (2-3 paragraphs before first section)
- [ ] Match pedagogical layer requirements (L1 = manual first, L2 = Three Roles, L3 = artifact creation, L4 = spec-first)
- [ ] Create 3 "Try With AI" prompts with learning explanations
- [ ] Include code examples with proper formatting (YAML, Markdown, Bash)
- [ ] Include comparison tables where appropriate
- [ ] Verify all skill/agent formats match canonical sources
- [ ] Test all code examples before inclusion
- [ ] Ensure cognitive load within A2/B1 limits (5-7 / 7-10 concepts)
- [ ] Include Three Roles demonstrations in L2+ lessons (invisible framework)

---

## X. Canonical Format Verification

Before implementation, verify taught formats match these canonical sources:

| Pattern | Canonical Source | Key Format Elements |
|---------|------------------|---------------------|
| **Skills** | `.claude/skills/session-intelligence-harvester/SKILL.md` | Directory structure, YAML with `name`, `description` |
| **Subagents** | `.claude/agents/content-implementer.md` | Single .md file, YAML with `name`, `description`, `model`, `skills`, single-line description |
| **MCP Config** | `.mcp.json` or `claude mcp add` commands | Server registration format |

**Critical**: Single-line description requirement for agents. Multi-line descriptions break tool parsing.

---

## XI. Validation Checklist

### Chapter-Level Validation
- [x] Chapter type identified (Technical/Skill Creation)
- [x] Concept density analysis documented (22 concepts across 7 lessons)
- [x] Lesson count justified by spec (7 lessons as specified)
- [x] All 8 evals from spec covered by lessons
- [x] All lessons map to at least one eval

### Stage Progression Validation
- [x] L1: Manual foundation before AI collaboration
- [x] L2-L3: Three Roles demonstrations planned
- [x] L4: Reusable artifacts created (subagents)
- [x] L5: MCP technical setup with AI collaboration
- [x] L6: Spec-first capstone orchestration
- [x] Progression follows L1->L2->L3->L4 without skipping

### Cognitive Load Validation
- [x] L1-L3: <= 7 concepts (A2 limit)
- [x] L4-L6: <= 10 concepts (B1 limit)
- [x] All lessons within proficiency tier limits

### Three Roles Validation (L2+ Lessons)
- [x] Each lesson demonstrates AI as Teacher (suggests patterns)
- [x] Each lesson demonstrates AI as Student (adapts to feedback)
- [x] Each lesson demonstrates AI as Co-Worker (convergence loop)

### Canonical Format Validation
- [x] Skills follow canonical SKILL.md format
- [x] Subagents follow canonical agent format
- [x] Single-line descriptions enforced
- [x] MCP configuration matches canonical patterns

---

## XII. Digital FTE Contribution

**How This Chapter Contributes to Agent Factory**:

By chapter end, students own a complete **Email Digital FTE**:

| Component | Type | Business Value |
|-----------|------|----------------|
| `/email-drafter` | Skill | Draft emails 10x faster |
| `/email-templates` | Skill | Consistent professional messaging |
| `/email-summarizer` | Skill | Process inbox in minutes |
| `inbox-triager` | Subagent | Automated priority classification |
| `response-suggester` | Subagent | Quick reply recommendations |
| `follow-up-tracker` | Subagent | Never miss a deadline |
| Gmail MCP | Connectivity | Real email operations |
| `/email-assistant` | Orchestrator | Complete system coordination |

**Combined Value**: A productizable "Email Assistant Digital FTE" that could be offered as a service to professionals, small businesses, or executives who manage high email volumes.

---

**Plan Version**: 2.0.0
**Status**: Ready for Implementation
**Next Step**: Execute `/sp.tasks` to generate tasks.md from this plan
