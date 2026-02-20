---
sidebar_position: 1
title: "What Is Context Engineering?"
description: "The discipline of controlling what your AI sees to produce consistent, high-quality output"
keywords:
  [
    "context engineering",
    "context window",
    "AI quality",
    "Digital FTE",
    "tokens",
    "context management",
    "context rot",
  ]
chapter: 4
lesson: 1
duration_minutes: 20

# HIDDEN SKILLS METADATA
skills:
  - name: "Define Context Engineering"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can articulate the definition of context engineering in one sentence"

  - name: "Distinguish Context from Prompts"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can explain why context (99.9%) matters more than prompts (0.1%)"

  - name: "Identify Context Rot Types"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can classify context degradation as poisoning, distraction, confusion, or clash"

learning_objectives:
  - objective: "Define context engineering using Anthropic's official framing"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can state the definition in their own words"

  - objective: "Explain why context engineering supersedes prompt engineering"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can articulate the token budget asymmetry"

  - objective: "Identify the four types of context rot in a working session"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Student can diagnose which rot type is affecting their work"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (token, context, context window, context engineering, context rot, four rot types) within A2 range"

differentiation:
  extension_for_advanced: "Explore transformer attention mechanisms and their relationship to context degradation"
  remedial_for_struggling: "Focus on the 5 definitions first before analyzing implications"

teaching_guide:
  lesson_type: "core"
  session_group: 1
  session_title: "Understanding Context Engineering"
  key_points:
    - "Context engineering is THE competitive moat for Digital FTEs — same model access means differentiation comes from context quality, not model choice"
    - "The 99.9% vs 0.1% split between context and prompts reframes everything students learned about prompt engineering — this is a paradigm shift"
    - "Four types of context rot (poisoning, distraction, confusion, clash) are diagnostic categories used throughout the rest of this chapter"
  misconceptions:
    - "Students think 'context' means 'the prompt I type' — emphasize context is everything the model sees BEFORE and ALONGSIDE the prompt"
    - "Students assume context rot means the AI is broken or getting dumber — it is the accumulated noise degrading signal quality"
    - "Students confuse context engineering with prompt engineering — context is 200K tokens of environment, prompts are 50-200 tokens of instruction"
  discussion_prompts:
    - "Have you ever had an AI session that started great but degraded over time? Which of the four rot types was likely at work?"
    - "If two competitors use the same AI model, what specifically makes one product worth $2,000/month and the other worthless?"
  teaching_tips:
    - "Open with the two-engineers scenario — ask students to guess the differentiator before revealing context quality"
    - "The prompts vs context table (0.1% vs 99.9%) is a strong whiteboard moment — draw the proportions visually"
    - "Have students run /context in Claude Code live during the lab — seeing their actual token consumption makes the concept concrete"
    - "Walk through each rot type with a live demo: start a session, change direction mid-conversation, then show how the AI references old information"
  assessment_quick_check:
    - "Define context engineering in one sentence without using the word 'prompt'"
    - "Name the four types of context rot and give one symptom of each"
    - "Why is optimizing prompts alone like 'polishing the doorknob while the house is on fire'?"
---

# What Is Context Engineering?

Two engineers build contract review agents. Same model. Same basic architecture. One sells for $2,000/month. The other can't give it away.

What's different?

**The answer: context quality.**

In Chapter 1, you learned that Digital FTEs are AI agents that work 24/7, delivering consistent results at a fraction of human cost. But here's the uncomfortable truth: those same AI models are available to everyone. Your competitors have access to Claude, GPT, and Gemini too. They can spin up the same frontier model in minutes.

The model isn't your moat. **Context engineering is.**

If you've used AI for real work, you've experienced the breakdown. Your AI followed instructions brilliantly for the first twenty minutes. Then it started ignoring conventions, repeating mistakes you already corrected, producing wildly different outputs for similar inputs. The AI didn't get dumber. Its context got corrupted.

This chapter teaches you the quality control discipline that separates sellable Digital FTEs from expensive toys.

## The Definition

Anthropic defines context engineering as:

> "The art and science of curating what will go into the limited context window from that constantly evolving universe of possible information."

The guiding principle: **find the smallest set of high-signal tokens that maximize the likelihood of some desired outcome.**

Your prompt is what you say. Your context is everything the AI already knows when you say it. Context engineering is controlling that "already knows" part.

## Five Terms You Need

| Term                    | Definition                                                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Token**               | The unit AI models use to measure text. Roughly 3/4 of a word. "Context engineering" = 2 tokens.                                            |
| **Context**             | Everything the model processes when generating a response: system prompts, instructions, conversation history, file contents, tool outputs. |
| **Context window**      | Maximum tokens the model can "see" at once (200,000 for Claude).                                                                            |
| **Context engineering** | The discipline of designing what goes into that window, where it's positioned, and when it loads.                                           |
| **Context rot**         | When accumulated conversation degrades output quality. Old errors and abandoned approaches compete with current instructions.               |

## Why Context Beats Prompts

"Prompt engineering" was the 2023 discipline. It has a ceiling.

|                  | Prompts       | Context           |
| ---------------- | ------------- | ----------------- |
| Token budget     | 50-200 tokens | 200,000+ tokens   |
| Your control     | What you type | What you engineer |
| Impact on output | 0.1%          | 99.9%             |

Your prompt is 0.1% of what the model processes. The other 99.9% is context. If you're optimizing prompts while ignoring context, you're polishing the doorknob while the house is on fire.

This matters for your Digital FTEs. A legal assistant Digital FTE with perfect prompts but corrupted context will hallucinate case citations. A sales Digital FTE with perfect prompts but bloated context will forget customer preferences mid-conversation. The context is what makes the difference between a $50/month chatbot and a $5,000/month professional assistant.

## The Four Types of Context Rot

Not all context degradation is equal. Recognizing the pattern helps you respond effectively.

### 1. Poisoning: Outdated Information Persists

You renamed something, changed a decision, or updated terminology. But 40 messages ago, you discussed the old version extensively. That discussion is still in context. Claude might reference the outdated information, creating confusion or errors.

**Symptom:** Claude uses terminology, patterns, or references that were correct earlier but aren't anymore.

### 2. Distraction: Irrelevant Content Dilutes Attention

You spent 20 messages on a tangent. Now you're working on something different. That tangent is still consuming attention budget—attention that could be allocated to your current constraints.

**Symptom:** Claude's responses feel less focused, miss details, or include tangential considerations.

### 3. Confusion: Similar Concepts Conflate

You're working with two similar things—maybe two services, two documents, or two processes. They have similar names or overlapping terminology. Claude starts conflating them—using the wrong one in the wrong context.

**Symptom:** Claude mixes up similar-sounding concepts, uses wrong terminology, or applies patterns from one domain to another.

### 4. Clash: Contradictory Instructions Compete

Early in the session, you said one thing. Later, you said something different. Both instructions are in context. Claude has to reconcile them and might choose wrong.

**Symptom:** Claude's decisions seem inconsistent, or it asks clarifying questions you thought you'd already answered.

## Automatic Context Management

Claude Code handles context automatically through a feature called autocompact. When your context window fills up, Claude Code summarizes the conversation, keeps key decisions, and forgets noise—without you doing anything.

Most of the time, this works well. Lesson 6 teaches when you need to manually intervene with `/compact` or `/clear` for situations where automatic management isn't enough.

## Lab: See Your Context

**Objective:** See what's consuming your context window right now.

### Task 1: Run the Context Command

In Claude Code, run:

```
/context
```

You'll see output showing:

- **System prompt**: Claude's base instructions (fixed cost)
- **MCP tools**: External integrations (each adds cost)
- **Memory files**: Your CLAUDE.md + rules (you control this)
- **Messages**: Conversation history (grows every turn)
- **Free space**: Remaining budget for actual work

**What to observe:** Much of your context is consumed before you type anything. That's baseline cost. Context engineering is managing these numbers so you have room for the work that matters.

### Task 2: Identify Potential Rot

Think about your current or most recent working session with Claude. Ask yourself:

- Did you change direction or rename anything mid-session? (Potential **poisoning**)
- Did you go on tangents unrelated to your current task? (Potential **distraction**)
- Are you working with similar-sounding concepts or files? (Potential **confusion**)
- Did you give different instructions at different times? (Potential **clash**)

If you identified any of these, you've diagnosed context rot. Later lessons teach how to treat each type.

## Try With AI

**Prompt 1: Context Inventory**

```
List everything currently in your context.
Estimate what percentage is:
(1) directly relevant to my next task,
(2) useful background,
(3) noise that dilutes attention.
```

**What you're learning:** Before you can engineer context, you need to see what's actually there. This prompt develops awareness of context state.

**Prompt 2: Rot Diagnosis**

```
Based on our conversation history, identify any signs of context rot:
- Poisoning (outdated information I've since changed)
- Distraction (tangents no longer relevant)
- Confusion (similar concepts that might be conflating)
- Clash (contradictory instructions I've given)

Be specific about what you find.
```

**What you're learning:** Diagnosis comes before treatment. This prompt helps you identify which rot type (if any) is affecting your current session, so you can apply the right fix.

**Safety note:** When running context diagnostics, you're examining the session state, not changing it. This is observational—safe to run at any time.
