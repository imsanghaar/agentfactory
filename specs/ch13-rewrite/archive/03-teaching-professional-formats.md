---
sidebar_position: 3
title: "Teaching Professional Formats"
sidebar_label: "L03: Professional Formats"
description: "Build a reusable email-templates skill with variable substitution, template libraries, and intelligent selection logic for consistent professional communication."
series: "email"
series_position: 2
keywords:
  - email templates
  - Claude Code skills
  - variable substitution
  - cold outreach
  - follow-up emails
  - meeting requests
  - professional communication
  - SKILL.md
chapter: 10
lesson: 3
duration_minutes: 25

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2 to Layer 3"
layer_progression: "L2 (AI Collaboration) transitioning to L3 (Intelligence Design)"
layer_1_foundation: "Understanding template design principles, variable syntax, folder structure"
layer_2_collaboration: "Working with AI to refine templates, test substitution, improve tone"
layer_3_intelligence: "Creating the email-templates skill as reusable intelligence"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Email Template Design"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can design email templates with appropriate placeholders for variable substitution"
  - name: "Skill Creation"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Programming"
    measurable_at_this_level: "Student can create a SKILL.md file with proper YAML frontmatter and workflow instructions"
  - name: "Template Library Organization"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information and Data Literacy"
    measurable_at_this_level: "Student can organize templates into logical categories with clear naming conventions"
  - name: "Variable Substitution Patterns"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can implement {{variable_name}} syntax and understand substitution workflow"
  - name: "Template Selection Logic"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can define when-to-use criteria for different email templates"

learning_objectives:
  - objective: "Design email templates with variable placeholders that enable personalization without manual rewriting"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Create cold-outreach template with at least 5 variable placeholders"
  - objective: "Create an email-templates skill with proper SKILL.md structure following Claude Code conventions"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Produce working SKILL.md with YAML frontmatter and workflow instructions"
  - objective: "Build a template library with three distinct email types: cold-outreach, follow-up, and meeting-request"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Create three template files with consistent structure and clear purpose"
  - objective: "Implement variable substitution patterns using {{variable_name}} syntax"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Successfully substitute variables in templates to produce personalized emails"
  - objective: "Apply template selection logic based on email context and recipient relationship"
    proficiency_level: "A2"
    bloom_level: "Apply"
    assessment_method: "Correctly identify which template applies for given scenarios"

# Cognitive load tracking
cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (template design principles, variable syntax, template library organization, selection logic, references directory) - within A2 limit of 5-7 concepts"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Create additional templates for specific domains (sales, recruiting, investor outreach) with conditional logic"
  remedial_for_struggling: "Focus on single cold-outreach template first before expanding to full library"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 1
  session_title: "Template Libraries and Variable Substitution"
  key_points:
    - "Templates encode expertise as reusable intelligence — updating one template improves ALL future emails, unlike one-off prompting which starts fresh each time"
    - "The {{variable_name}} syntax is the first formal pattern language students learn — it bridges the gap between static text and programmable output"
    - "Anti-patterns are as valuable as patterns — the cold-outreach anti-patterns table prevents the most common email mistakes (generic openers, multiple CTAs)"
    - "Template selection logic teaches intent recognition — Claude must map natural language ('haven't heard back') to the correct template (follow-up)"
  misconceptions:
    - "Students think templates make emails sound robotic — the variable substitution and tone guidance sections show how templates ENABLE personalization at scale"
    - "Students confuse the email-templates skill with the email-drafter skill from L02 — drafter is freeform composition, templates are structured formats with variables"
    - "Students expect templates to handle every email type — the lesson explicitly scopes to three types and shows how to extend, not replace"
    - "Students skip anti-patterns sections thinking they are optional — anti-patterns prevent the most common quality regressions"
  discussion_prompts:
    - "The lesson shows 80 minutes vs 10 minutes for 20 emails. What recurring communication in YOUR work has similar multiplicative savings potential?"
    - "Why does the follow-up template require 'new value' instead of just 'checking in'? How does this constraint improve response rates?"
    - "The meeting request template includes a time-boxed agenda. Why does showing preparation upfront increase the chance of getting a meeting?"
  teaching_tips:
    - "Have students fill the cold-outreach template with REAL data from their domain — abstract examples do not build muscle memory"
    - "The follow-up timing guidelines table (5-7 days, 10-14 days, 21 days) is worth discussing as a strategy, not just a template feature"
    - "Demo template selection live: read three different email requests aloud and have students identify which template applies before Claude does"
    - "Emphasize that templates/ uses Level 3 loading — files are only loaded when the skill needs them, not on every invocation"
  assessment_quick_check:
    - "Name the three template types and one scenario where each applies"
    - "What is the difference between the email-drafter skill (L02) and the email-templates skill (this lesson)?"
    - "Fill the {{variables}} in the cold-outreach template with data from your own domain"

# Generation metadata
generated_by: "content-implementer (autonomous execution)"
created: "2026-01-01"
last_modified: "2026-01-01"
version: "1.0.0"
---

# Teaching Professional Formats

You've written the same cold outreach email a hundred times. Each time, you customize the recipient's name, personalize the hook, adjust the value proposition. It takes 10 minutes to get it right. Multiply that across dozens of prospects, and you've spent hours on what should take seconds.

The problem isn't that you lack an AI assistant. Claude can write emails. The problem is that Claude doesn't know YOUR patterns—the specific structure that works for your industry, the tone that matches your brand, the follow-up sequences that actually get responses.

This lesson changes that. You'll build an **email-templates skill** that encodes your email expertise into reusable intelligence. Instead of explaining your preferences every time, you'll invoke a skill that already knows your cold outreach structure, your follow-up timing philosophy, and your meeting request format.

---

## Why Template Skills Beat One-Off Prompting

Compare two approaches to sending 20 personalized outreach emails:

| Approach | Time per Email | Consistency | Improvement |
|----------|----------------|-------------|-------------|
| **Manual prompting** | 3-5 minutes (explaining format each time) | Variable (depends on prompt quality) | None (starts fresh each time) |
| **Template skill** | 30 seconds (fill variables, send) | High (same structure every time) | Compounds (refine template once, all emails improve) |

The math is clear: 20 emails at 4 minutes each = 80 minutes. With templates: 20 emails at 30 seconds = 10 minutes. That's 70 minutes saved—per batch.

But time savings miss the bigger point. **Templates encode your expertise as reusable intelligence.** When you discover that a particular subject line format doubles your response rate, you update one template. Every future email benefits.

---

## Template Design Principles

Effective email templates share three characteristics:

**1. Clear Placeholders**

Variables identify what changes between emails. Use `{{variable_name}}` syntax for consistency:

```
Good:  {{recipient_name}}, {{company}}, {{hook}}
Bad:   [NAME], {company}, <insert hook here>
```

The double-brace syntax `{{...}}` is unambiguous. Claude recognizes it immediately. Your templates become self-documenting.

**2. Structured Sections**

Each template needs:
- **Purpose**: When to use this template
- **Variables**: What information is required
- **Template**: The actual email structure
- **Example**: A filled-out version showing the pattern

Structure enables automation. When Claude sees a complete template, it can:
- Prompt you for missing variables
- Substitute values correctly
- Validate the result makes sense

**3. Anti-Patterns**

Templates should prevent common mistakes, not just provide structure:

```markdown
## Anti-Patterns
- Generic openers ("I hope this finds you well")
- Wall of text (4-5 short paragraphs max)
- Multiple CTAs (one clear ask only)
- Obvious template feel
```

Documenting what NOT to do is as valuable as documenting what to do. It prevents regression when you're rushing.

---

## The Email Templates Skill Structure

Your skill will follow Claude Code's standard structure:

```
.claude/skills/
└── email-templates/
    ├── SKILL.md                 # Main skill instructions
    └── templates/               # Template library
        ├── cold-outreach.md     # First contact
        ├── follow-up.md         # Re-engagement
        └── meeting-request.md   # Scheduling calls
```

**Why this structure works:**

- **SKILL.md** loads on-demand when Claude activates the skill (Level 2 loading)
- **templates/** directory contains supporting files accessed when needed (Level 3 loading)
- Each template is a separate file for easy editing and version control

---

## Building the SKILL.md

The SKILL.md file is the entry point. It tells Claude:
- What this skill does
- When to activate it
- How to use the templates

Here's the complete SKILL.md for your email-templates skill:

```markdown
---
name: email-templates
description: This skill provides reusable email templates with variable substitution. Use when the user needs to send recurring email types like cold outreach, follow-ups, or meeting requests. Automatically selects appropriate template and fills variables.
---

# Email Templates

## Overview

Reusable email templates with variable substitution for consistent, efficient communication.

## When to Use This Skill

Activate this skill when user needs to:
- Send cold outreach to new contacts
- Follow up on unanswered emails
- Request meetings or calls
- Draft any recurring email type

## Available Templates

### 1. Cold Outreach (`templates/cold-outreach.md`)

For first contact with new connections. Focuses on:
- Personalized hook (why reaching out to THEM)
- Brief credibility (proof you're worth hearing)
- Clear value proposition (what's in it for them)
- Low-friction CTA (easy next step)

### 2. Follow-Up (`templates/follow-up.md`)

For re-engaging after no response. Focuses on:
- Non-accusatory reference to previous message
- New value addition (not just "checking in")
- Easier response options

### 3. Meeting Request (`templates/meeting-request.md`)

For scheduling calls or meetings. Focuses on:
- Clear context (why meeting makes sense)
- Specific agenda (what you'll discuss)
- Multiple time options (respect their calendar)

## Variable Syntax

Templates use `{{variable_name}}` syntax:

| Variable | Description |
|----------|-------------|
| `{{recipient_name}}` | First name of recipient |
| `{{company}}` | Recipient's company name |
| `{{topic}}` | Email subject matter |
| `{{sender_name}}` | Your name |

Additional template-specific variables are documented in each template file.

## Workflow

1. **Identify email type** from user request
2. **Load appropriate template** from templates/ directory
3. **Gather variable values** from context or ask user
4. **Substitute variables** into template
5. **Apply tone adjustments** if user has preferences
6. **Present filled template** for review and refinement

## Integration Notes

This skill works well with:
- Gmail MCP for direct sending
- Calendar tools for meeting request coordination
- CRM data for personalization
```

**What makes this effective:**

- **Clear activation triggers**: "when user needs to send recurring email types"
- **Template overview**: Quick reference for what's available
- **Variable documentation**: Consistent substitution patterns
- **Workflow steps**: Claude knows the process to follow

---

## Creating the Cold Outreach Template

The cold outreach template is your highest-impact email type. First impressions matter. Here's the complete template:

```markdown
# Cold Outreach Template

## Purpose

First contact with someone who doesn't know you. The goal is to earn a response, not close a deal.

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{recipient_name}}` | First name | "Sarah" |
| `{{hook}}` | Why reaching out to THEM specifically | "Your Kubernetes talk at KubeCon" |
| `{{hook_subject}}` | Subject line hook | "Your Kubernetes talk - question from a practitioner" |
| `{{credibility}}` | Brief proof you're worth hearing | "I've helped 200+ developers adopt similar patterns" |
| `{{value_prop}}` | What's in it for them | "Include your approach as a case study" |
| `{{cta}}` | Low-friction next step | "15-minute call next week" |
| `{{sender_name}}` | Your name | "Alex" |

## Template

Subject: {{hook_subject}}

Hi {{recipient_name}},

{{hook}}

{{credibility}}

{{value_prop}}

{{cta}}

Best,
{{sender_name}}

## Example Filled

**Subject:** Your Kubernetes talk - question from a practitioner

Hi Sarah,

I saw your talk on scaling microservices at KubeCon. Your approach to service mesh configuration solved a problem I've been wrestling with for weeks.

I'm building a course on cloud-native development and have helped 200+ developers adopt similar patterns.

Would a 15-minute call work next week to discuss including your approach as a case study?

Best,
Alex

## Anti-Patterns

These patterns reduce response rates:

| Pattern | Problem | Instead |
|---------|---------|---------|
| "I hope this finds you well" | Generic, wastes space | Jump to personalized hook |
| Long paragraphs | Overwhelming on mobile | Keep to 2-3 sentences per paragraph |
| Multiple asks | Confuses priority | One clear CTA only |
| "I'm sure you're busy" | Apologetic, low status | Confident, value-first framing |
| Obvious template feel | Breaks trust | Genuine personalization in hook |

## Tone Guidance

- **Confident but not arrogant**: You have value to offer
- **Specific but not overwhelming**: One clear point
- **Personal but not creepy**: Reference public information only
- **Short but not abrupt**: 4-5 sentences total
```

**Key design choices:**

- **Variable table with examples**: Claude knows exactly what to ask for
- **Complete example**: Shows the pattern in action
- **Anti-patterns table**: Prevents common mistakes
- **Tone guidance**: Maintains voice consistency

---

## Creating the Follow-Up Template

Follow-ups fail when they sound desperate or accusatory. The key is adding value while making response easier:

```markdown
# Follow-Up Template

## Purpose

Re-engage after no response without being pushy. Adds value instead of just "checking in."

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{recipient_name}}` | First name | "Marcus" |
| `{{original_topic}}` | What first email was about | "Partnership opportunity" |
| `{{new_value}}` | Additional value or context | "Your v2.0 release makes this more relevant" |
| `{{easier_option}}` | Lower-friction alternative | "3-minute Loom video instead of call" |
| `{{sender_name}}` | Your name | "Alex" |

## Template

Subject: Re: {{original_topic}} - one more thought

Hi {{recipient_name}},

Wanted to circle back on my message about {{original_topic}}.

{{new_value}}

{{easier_option}}

Best,
{{sender_name}}

## Example Filled

**Subject:** Re: Partnership opportunity - one more thought

Hi Marcus,

Wanted to circle back on my message about the documentation partnership from last week.

Since then, I noticed your team released v2.0—congratulations! This actually makes the collaboration even more relevant since the new API patterns match what I'm documenting.

Would it be easier to start with a quick async exchange? I could send over our proposed integration in a 3-minute Loom video instead of scheduling a call.

Best,
Alex

## Timing Guidelines

Strategic timing increases response rates:

| Follow-up | Timing | Approach |
|-----------|--------|----------|
| First | 5-7 business days | Add new value, maintain confidence |
| Second | 10-14 days after first | Offer easier response option |
| Final | 21 days | Give explicit permission to say no |

## Anti-Patterns

| Pattern | Problem | Instead |
|---------|---------|---------|
| "Just checking in" | No value, annoys recipient | Add new information or context |
| "Did you see my email?" | Accusatory tone | Assume they're busy, add value |
| "I'll keep this brief" | Draws attention to length | Just be brief, don't announce it |
| Exact same message | Shows no effort | Reference something new |
```

**Why this works:**

- **New value requirement**: Forces you to earn the follow-up
- **Easier option**: Reduces friction for busy recipients
- **Timing guidelines**: Strategic spacing without harassment
- **Permission to say no**: Final follow-up preserves relationship

---

## Creating the Meeting Request Template

Meeting requests fail when they lack context or make scheduling hard. The template solves both:

```markdown
# Meeting Request Template

## Purpose

Schedule time efficiently by demonstrating value upfront. The recipient should know exactly why meeting is worth their time.

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{recipient_name}}` | First name | "Priya" |
| `{{context}}` | Why meeting makes sense | "Based on our Slack thread about rate limiting" |
| `{{topic}}` | Meeting subject | "API integration" |
| `{{duration}}` | Time commitment | "30 min" |
| `{{agenda_items}}` | Specific topics (bulleted) | Review limits, discuss patterns, agree on solution |
| `{{time_options}}` | 3 specific time slots | Tuesday 2 PM, Wednesday 10 AM, Thursday 3 PM |
| `{{sender_name}}` | Your name | "Alex" |

## Template

Subject: {{duration}} sync on {{topic}} - {{number}} time options

Hi {{recipient_name}},

{{context}}

Proposed agenda ({{duration}}):
{{agenda_items}}

Would any of these work?
{{time_options}}

{{sender_name}}

## Example Filled

**Subject:** 30-min sync on API integration - 3 time options

Hi Priya,

Based on our Slack thread about the rate limiting issue, I think we'd resolve this faster in a quick call.

Proposed agenda (30 min):
- Review current rate limits (5 min)
- Discuss your usage patterns (10 min)
- Agree on solution approach (15 min)

Would any of these work?
- Tuesday 2-2:30 PM EST
- Wednesday 10-10:30 AM EST
- Thursday 3-3:30 PM EST

Alex

## Best Practices

| Practice | Why It Works |
|----------|--------------|
| Include specific agenda | Shows you've prepared, respects their time |
| Offer 3 time options minimum | Increases chance of fit |
| State duration clearly | Sets expectations, shows respect |
| Include time zone | Prevents confusion, especially remote |
| Time-boxed agenda items | Demonstrates efficiency |

## Anti-Patterns

| Pattern | Problem | Instead |
|---------|---------|---------|
| "Let's hop on a call" | Vague, no agenda | Specific purpose with agenda |
| "When are you free?" | Puts burden on them | Offer specific times |
| "Quick sync" (no time) | Unclear commitment | State exact duration |
| Back-to-back requests | Assumes first time works | Offer alternatives upfront |
```

---

## Template Selection Logic

Your SKILL.md defines when to use each template. But Claude needs to recognize intent from natural language:

**Cold Outreach indicators:**
- "I want to reach out to..."
- "First time contacting..."
- "Introduce myself to..."
- "Initial outreach to..."

**Follow-Up indicators:**
- "Haven't heard back from..."
- "Follow up on my previous..."
- "Circle back with..."
- "Re-engage with..."

**Meeting Request indicators:**
- "Schedule a call with..."
- "Set up a meeting..."
- "Find time to discuss..."
- "Book time with..."

Add these patterns to your SKILL.md's "When to Use" section to improve activation accuracy.

---

## Testing Your Skill

Create the skill structure and test with Claude:

**Step 1: Create the directory structure**

```bash
mkdir -p .claude/skills/email-templates/templates
```

**Step 2: Create SKILL.md and template files**

Copy the content from this lesson into:
- `.claude/skills/email-templates/SKILL.md`
- `.claude/skills/email-templates/templates/cold-outreach.md`
- `.claude/skills/email-templates/templates/follow-up.md`
- `.claude/skills/email-templates/templates/meeting-request.md`

**Step 3: Test activation**

Ask Claude:

```
"I need to reach out to Sarah Chen at DataFlow Inc. She gave a great talk
on data pipelines at the recent conference. I want to explore a potential
partnership for our developer education content."
```

**Expected behavior:**
1. Claude recognizes this as cold outreach
2. Loads the cold-outreach template
3. Identifies variables: `{{recipient_name}}` = Sarah, `{{company}}` = DataFlow Inc
4. Asks for remaining variables or infers from context
5. Produces filled template for review

**Step 4: Refine through iteration**

Claude's first attempt may not match your voice perfectly. This is where AI collaboration shines:

**You**: "This sounds too formal. I want it warmer, more conversational."

**Claude adapts**: Revises tone while maintaining structure.

**You**: "The CTA is too aggressive. Soften it."

**Claude refines**: Adjusts call-to-action while keeping it clear.

Each refinement teaches you something about your preferences. Update the template's tone guidance based on what you learn.

---

## Extending Your Template Library

The three core templates handle most professional email needs. But you can extend for your domain:

| Domain | Additional Templates |
|--------|---------------------|
| **Sales** | Demo request, pricing follow-up, contract renewal |
| **Recruiting** | Candidate outreach, interview scheduling, offer letter |
| **Investor Relations** | Intro request, update email, pitch deck follow-up |
| **Customer Success** | Onboarding check-in, renewal reminder, upsell intro |

Each new template follows the same structure:
1. Purpose
2. Variables table
3. Template
4. Example filled
5. Anti-patterns
6. Tone guidance

The pattern is the reusable intelligence. Templates are just instantiations.

---

## What You Built

You now have a production-ready email templates skill:

| Component | Purpose |
|-----------|---------|
| **SKILL.md** | Entry point with activation triggers and workflow |
| **cold-outreach.md** | First contact template with personalization |
| **follow-up.md** | Re-engagement template with value-add approach |
| **meeting-request.md** | Scheduling template with agenda and options |

This skill represents **Layer 3 intelligence**—tacit knowledge (your email patterns) transformed into explicit, reusable assets. Every email you send using these templates reinforces the pattern. Every refinement improves all future emails.

---

## Try With AI

**Create Your Cold Outreach Template:**

```
"Help me create a cold outreach email template for [your specific use case].
I typically reach out to [target audience] about [your offering]. My usual
structure is [describe your current approach]. What variables should we
define, and what anti-patterns should I avoid?"
```

**What you're learning:** How to translate your intuitive email patterns into explicit template structure. Notice how Claude asks clarifying questions—that's the variable identification process.

**Test Variable Substitution:**

```
"Using the cold outreach template structure, create an email for:
- Recipient: [name] at [company]
- Hook: [something specific about them]
- My credibility: [your relevant experience]
- Value prop: [what you're offering]
- CTA: [your ask]

Show me the filled template and explain which variables you substituted."
```

**What you're learning:** The mechanical process of variable substitution. This is what your skill automates—Claude gathers variables and produces consistent output.

**Refine Tone Through Iteration:**

```
"This template sounds too [formal/casual/aggressive/passive]. I want my
emails to sound more [your desired tone]. Revise the template and
update the tone guidance section to reflect this preference."
```

**What you're learning:** How bidirectional refinement works. You're teaching Claude your preferences; Claude is suggesting improvements you hadn't considered. The result is better than either starting point.

**Remember:** Always review AI-generated emails before sending. Templates provide structure; your judgment provides appropriateness for each specific recipient and context.
