---
slug: /General-Agents-Foundations/general-agents/hello-world-basics
title: "Hello Claude: Your First Conversation"
sidebar_position: 4
chapter: 3
lesson: 4
duration_minutes: 7

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Opening Claude Code, natural language conversation, basic file creation, understanding Claude as a collaborator"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Claude Code First Contact"
    proficiency_level: "A1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Digital Engagement"
    measurable_at_this_level: "Student can open Claude Code, have a natural conversation, and create a simple file through natural language"

learning_objectives:
  - objective: "Start Claude Code and engage in natural conversation"
    proficiency_level: "A1"
    bloom_level: "Remember"
    assessment_method: "Successfully typing 'claude' and receiving a response"
  - objective: "Ask Claude exploratory questions about its capabilities"
    proficiency_level: "A1"
    bloom_level: "Understand"
    assessment_method: "Asking 'Where am I?' and 'What can you do?' and understanding responses"
  - objective: "Create a simple file by describing what you want"
    proficiency_level: "A1"
    bloom_level: "Apply"
    assessment_method: "Creating a markdown file with content using natural language"
  - objective: "Observe Claude's offer-and-approval workflow"
    proficiency_level: "A1"
    bloom_level: "Understand"
    assessment_method: "Noticing when Claude proposes actions and asks for approval"

# Cognitive load tracking
cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (Claude Code terminal, natural conversation, approval pattern) - well within A1 limit"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Try asking Claude to search the web for information and save it to a file"
  remedial_for_struggling: "Just focus on opening Claude and asking 'What can you do?' - that's success"

# Generation metadata
generated_by: "content-rewriter (04-hello-world-basics-beginner-focused)"
source_spec: "specs/04-hello-world-basics/spec.md"
created: "2026-01-16"
version: "2.0.0"

# Legacy compatibility
prerequisites:
  - "Lesson 02 or 03: Claude Code installed and authenticated"

# TEACHING GUIDE METADATA (visible to teacher role only)
teaching_guide:
  lesson_type: "hands-on"
  session_group: 2
  session_title: "First Conversations and Context Files"
  key_points:
    - "This is the 'aha moment' lesson — students go from reading about Claude Code to actually using it for the first time"
    - "The approval pattern (Enter to accept, Esc to reject) is introduced here and governs all future interactions"
    - "The Five Extension Tools preview table maps every future lesson — students should bookmark it as their roadmap"
    - "Natural language is the interface — students do not need to learn command syntax, just describe what they want"
  misconceptions:
    - "Students think they need special syntax or commands to talk to Claude — the whole point is natural language conversation"
    - "Students confuse 'approval workflow' with 'Claude being unsure' — Claude asks permission because of the security model, not uncertainty"
    - "Students think the Five Extension Tools table means they need to learn all five tools now — it is a preview, not a prerequisite"
  discussion_prompts:
    - "How does the approval pattern change your trust relationship with AI compared to tools that just execute without asking?"
    - "What was surprising about your first conversation with Claude Code compared to using ChatGPT or other AI tools?"
    - "Looking at the Five Extension Tools table, which tool do you think will be most useful for YOUR work and why?"
  teaching_tips:
    - "Have every student type 'claude' and get a response before moving on — do not proceed until 100% have a working session"
    - "The 'Where am I?' prompt is deliberately simple — use it to surface any remaining installation issues from Lessons 2-3"
    - "When demoing the AI news search example, reject the first proposal with Esc to show students that steering is safe and expected"
    - "Point at the Five Extension Tools table and say 'this is your chapter roadmap' — it reduces anxiety about upcoming complexity"
  assessment_quick_check:
    - "Ask students to describe what happened when they typed their first prompt — did Claude ask for approval before acting?"
    - "Have students press Esc on a proposed action and describe what happened next"
    - "Ask: What is the difference between Claude reading a file and Claude creating a file in terms of the approval workflow?"
---

# Hello Claude: Your First Conversation

You've installed Claude Code your General Agent. Now it's time to actually use it.

This lesson isn't about learning complex features. It's about having your first real conversation with Claude and realizing it's not intimidating—it's actually natural.

---

## The Setup: One Command

Open your terminal and type:

```bash
claude
```

That's it. You're now in Claude Code.

You'll see a prompt. It looks something like:

```
▗ ▗   ▖ ▖  Claude Code v2.1.9
           Haiku 4.5 · Claude Max
  ▘▘ ▝▝    ~/Documents/code/panaversity-official/tutorsgpt/mem
> _
```

This is where you talk to Claude. In natural language. No special syntax. No commands you need to memorize.

---

## Your First Questions: Orient Yourself

Let's start with the basics. Ask Claude where you are:

```
> Where am I right now??
```

Claude will tell you. Your current directory. Simple context.

Now ask what Claude can do:

```
> What can you do? What are my main options?
```

Claude will explain it naturally. Not a manual. Not technical jargon. Just what's possible.

**What you're learning:** Claude responds to natural language. You're not "commanding"—you're asking questions and conversing.

---

## Real-World Example: Search for News and Save It

Here's something useful. Let's find recent AI news and save it to a file.

Ask Claude:

```
> Search for the latest news about AI agents in 2026 and create a file called 'ai-news-2026.txt' with what you find
```

Watch what happens:

1. **Claude reads the web** for recent news
2. **Claude proposes a file** with formatted content
3. **You'll see a prompt asking:** `> Create file ai-news-2026.txt?`
4. **You press Enter** to approve

Done. You now have a file with actual, current information.

**What just happened:**

- You described what you wanted in plain English
- Claude figured out the steps (search, format, create file)
- Claude showed you what it was about to do
- You approved with one keypress

No clicking. No menu hunting. Just conversation.

---

## The Approval Pattern: You're Always in Control

Notice that Claude didn't just do things. **It asked first.**

This is the permission model. Every time Claude wants to:

- **Read** a file
- **Write** or create a file
- **Run** a command

It shows you exactly what it's about to do and waits for your approval.

Press `[Enter]` to approve. Press `[Esc]` to reject.

If you reject, you can ask Claude to try differently. That's steering.

**Why this matters:** You're never surprised. Claude can't accidentally delete your project or run something dangerous without your knowledge.

---

:::tip Ready to Practice?
Head to **Lesson 06: Practical Problem-Solving Exercises** for 27 hands-on exercises with complete walkthroughs. You'll organize messy files, analyze data, create documents, and build problem-solving skills — all with one-click exercise downloads and step-by-step guidance.
:::

---

## Next: Extending Claude (Preview)

Once you master basic conversations, you'll start asking more ambitious questions:

- _"How do I make Claude repeat this task every morning?"_
- _"How do I connect Claude to my Jira board so it can check for new tickets?"_
- _"How do I enforce my team's naming conventions automatically?"_
- _"How do I give Claude access to my company's database?"_

This is where Claude's extension tools come in. You don't need to understand them yet—just know they exist.

### The Five Extension Tools at a Glance

| If you need...                                          | Then use...   | Appears in...  |
| :------------------------------------------------------ | :------------ | :------------- |
| **Persistent context** for every Claude session         | **CLAUDE.md** | Lessons 5, 7   |
| **Repeated procedures** done your way                   | **Skill**     | Lessons 8-9    |
| **Delegation & focus** for complex workflows            | **Subagent**  | Lessons 11, 13 |
| **External systems & data** (APIs, databases, websites) | **MCP**       | Lessons 12-13  |
| **Automated quality gates & safety rules**              | **Hook**      | Lesson 15      |

**Here's the pattern:** You learn each tool individually (Lessons 5-15), then in Lesson 18, you'll see how an expert combines them in a production workflow—like a manager building a team, not a developer writing functions.

### Why This Matters Now

As you continue through the chapter, you'll recognize patterns:

- "I need Claude to always format code like this" → You'll think: _That's a CLAUDE.md use case_
- "I want Claude to research and write a report without interrupting me" → _That's a Subagent_
- "I need Claude to check GitHub for vulnerabilities before I commit" → _That's a Hook_

You're building a **mental model**. The tools are the same; the architecture is what separates amateur automation from professional systems.

---

## Try With AI

**Explore naturally:**

> "Ask Claude: 'What's in this directory?' Then ask: 'Tell me about my project structure.' Watch how Claude learns about your environment through conversation."

**Create something real:**

> "Ask Claude to search for recent breakthroughs in your field of interest and save them to a file. Use natural language—describe what you want, not how to do it."

**Test the approval workflow:**

> "Ask Claude to create a file, and when it asks for approval, press Esc to reject. Then ask it to do something different. Notice how Claude adapts without frustration."

**Next Up:** Now that you're comfortable conversing with Claude, let's teach Claude about YOUR preferences.
