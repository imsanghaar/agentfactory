---
sidebar_position: 14
title: "When Your Employee Codes"
description: "Discover the inversion pattern: your AI Employee orchestrates Claude Code to write actual software, demonstrating the Agent Factory thesis -- agents that build agents"
keywords:
  [
    coding agent,
    agent orchestration,
    sub-agents,
    claude code,
    openclaw coding,
    agent factory thesis,
    PTY mode,
    multi-agent,
    self-building agents,
    delegation chain,
  ]
chapter: 13
lesson: 14
duration_minutes: 30

# HIDDEN SKILLS METADATA
skills:
  - name: "Agent Orchestration Comprehension"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can explain how a Custom Agent orchestrates a General Agent, identifying the chain of delegation from user to AI Employee to coding agent"

  - name: "Multi-Agent Architecture Understanding"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can describe the sub-agent pattern (main agent, orchestrator, worker) and explain why PTY mode, workdir isolation, and background process monitoring exist"

learning_objectives:
  - objective: "Explain the inversion pattern: Custom Agent orchestrating General Agent"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student can draw the delegation chain (User -> Telegram -> OpenClaw -> Claude Code -> code changes -> results back to user) and explain what makes this different from direct coding"

  - objective: "Describe how the coding-agent skill uses PTY mode, workdir isolation, and background processes to safely delegate coding work"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student can explain why PTY mode is required, why workdir isolation matters, and how background process monitoring prevents runaway agents"

  - objective: "Articulate why 'agents that build agents' represents the Agent Factory thesis"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Student can connect the OpenClaw -> Claude Code pattern to the broader thesis that General Agents create Custom Agents, and Custom Agents orchestrate General Agents in return"

cognitive_load:
  new_concepts: 3
  assessment: "3 new concepts (agent-to-agent delegation, the coding-agent skill pattern, the self-building recursive loop). High conceptual density but built on 6 prior lessons of foundation."

differentiation:
  extension_for_advanced: "Explore OpenClaw's sub-agent documentation. Design a multi-agent workflow where OpenClaw spawns 3 parallel Claude Code instances to fix 3 different issues simultaneously using git worktrees."
  remedial_for_struggling: "Focus on the delegation chain diagram. Trace one message from your phone through OpenClaw to Claude Code and back. Write down each step."

teaching_guide:
  lesson_type: "core"
  session_group: 5
  session_title: "Agent-to-Agent Orchestration"
  key_points:
    - "The inversion pattern is the chapter's thesis made visible: a Custom Agent (your AI Employee) orchestrating a General Agent (Claude Code) to write actual software"
    - "Three safety mechanisms make agent-to-agent delegation reliable: PTY mode (interactive terminal), workdir isolation (filesystem sandbox), background mode (non-blocking execution)"
    - "The self-building recursive loop (General Agent builds Custom Agent, Custom Agent orchestrates General Agent) means your AI Employee can improve itself"
    - "This lesson bridges Chapter 13 (build your employee) to the broader Agent Factory thesis from Chapter 1 — agents that build agents"
  misconceptions:
    - "Students think the AI Employee writes code itself — it delegates to Claude Code, a specialized coding agent; the Employee is the manager, not the developer"
    - "Students confuse PTY mode with a safety feature — PTY mode is a COMPATIBILITY requirement; without it, interactive coding agents hang or produce broken output"
    - "Students assume the self-building pattern is theoretical — OpenClaw literally uses Claude Code to modify its own source code, and this is documented in the lesson"
    - "Students think parallel coding requires special infrastructure — PM2 from L10 plus git worktrees is sufficient for running multiple Claude Code instances"
  discussion_prompts:
    - "The lesson shows a 10-step delegation chain from your phone to code changes. At which step does the most value get added, and why?"
    - "The self-building pattern means your AI Employee can extend its own capabilities. What safeguards would you want before allowing an AI to modify its own code?"
    - "Compare the two approaches: LLM generating code in chat vs Claude Code working on the filesystem. When would the simpler chat approach actually be better?"
  teaching_tips:
    - "The delegation chain diagram (10 steps from phone to code) is the lesson's centerpiece — walk through it step by step, mapping each to the 6 universal patterns"
    - "If students have Claude Code installed, the live demo ('Build me a snake game in Python') is dramatically more convincing than reading about it"
    - "The comparison table (without vs with coding-agent skill) is the best 'aha moment' — the difference between copy-paste coding and autonomous development"
    - "End by connecting to Chapter 13: students will build their own AI Employee, and that employee can use Claude Code to extend itself — the seed that grows"
  assessment_quick_check:
    - "Draw the delegation chain from your phone to code changes — how many AI agents are involved and what role does each play?"
    - "Name the three safety mechanisms for agent-to-agent delegation and explain what each prevents"
    - "Explain the self-building loop in one sentence: how does a Custom Agent use a General Agent to improve itself?"
---

# When Your Employee Codes

In Lesson 06, you crystallized the 6 universal agent patterns and assessed what OpenClaw proved and what it didn't. You can now evaluate any agent framework in minutes. But the lesson ended with a promise: there is still one more thing to see in OpenClaw -- the most surprising pattern of all.

Here it is. If you have Claude Code installed on your machine, send this message to your Telegram bot: "Build me a REST API for tracking my reading list."

Something unexpected happens. Your AI Employee does not attempt to write code directly through the LLM. It does not paste Python into a chat message and hope for the best. Instead, it launches Claude Code -- a fully autonomous coding agent -- in a background terminal, pointed at a project directory, with a pseudo-terminal for proper interactive control. Your phone becomes a remote control for a developer-grade coding tool.

This is the inversion. Your AI Employee (a Custom Agent you configured) is commanding Claude Code (a General Agent that can build anything). You built the custom agent. The custom agent now orchestrates the general agent. This is not a feature bolted onto OpenClaw as an afterthought. This is the Agent Factory thesis made visible: agents that build agents.

:::tip Hands-On vs Read-Along Path

This lesson's demo requires a coding agent (Claude Code, Codex CLI, or similar) installed on your machine. OpenClaw's bundled `coding-agent` skill detects available coding tools automatically.

**Hands-on path** (recommended): Install Claude Code first:

```bash
npm install -g @anthropic-ai/claude-code
```

Then send the coding request to your bot. You will see the full delegation chain in action.

**Read-along path**: If you do not have a coding agent installed or prefer not to install one now, this lesson is fully understandable by reading the walkthrough and diagrams below. The architectural patterns are the same whether you observe them live or trace them on paper. You will use Claude Code directly in Chapter 13 regardless.

:::

## The Message That Changes Everything

Walk through what happens when you type "Build me a snake game in Python" on Telegram. Every step maps to a pattern you already know:

1. **Message arrives at Gateway** (Orchestration pattern from L04)
2. **Gateway routes to your agent session** (State Isolation pattern from L04)
3. **Agent recognizes this as a coding task** -- the LLM reads the request and determines that it requires writing files, not just generating text
4. **Agent activates the coding-agent skill** (Capability Packaging pattern from L05)
5. **Skill launches Claude Code in background** with PTY mode enabled
6. **Claude Code works autonomously** in a sandboxed directory -- reading files, writing code, running tests, fixing errors
7. **Progress is monitored** via process polling
8. **Claude Code signals completion** by triggering a notification back to OpenClaw
9. **OpenClaw delivers the result** back through the Gateway to Telegram
10. **You receive the finished code on your phone**

The delegation chain:

```
You -> Phone -> Telegram -> OpenClaw Gateway -> coding-agent skill
  -> Claude Code (background PTY) -> code changes -> results
    -> OpenClaw -> Telegram -> Phone -> You
```

Count the AI agents in that chain. There are two. Your AI Employee (OpenClaw) delegated work to another AI agent (Claude Code). This is agent-to-agent orchestration -- and it happened because you sent a text message from your phone.

## How the Coding-Agent Skill Works

The coding-agent skill is a standard SKILL.md file -- the same format you learned to create in Lesson 05. But its instructions tell the agent how to launch and manage external coding tools. It supports multiple coding agents:

| Coding Agent        | Command                    | Strengths                                                               |
| ------------------- | -------------------------- | ----------------------------------------------------------------------- |
| **Claude Code**     | `claude 'Your task'`       | Anthropic's terminal coding agent, strong at complex multi-file changes |
| **Codex CLI**       | `codex exec 'Your task'`   | OpenAI's coding agent, requires git repo                                |
| **OpenCode**        | `opencode run 'Your task'` | Open-source alternative                                                 |
| **Pi Coding Agent** | `pi 'Your task'`           | Lightweight, supports multiple providers                                |

The skill does not simply run a command and wait. It manages three critical safety mechanisms that make agent-to-agent delegation reliable.

### PTY Mode: Why Interactive Terminals Matter

Coding agents are interactive terminal applications, not simple scripts. They display progress bars, colored output, interactive prompts, and real-time status updates. Without a pseudo-terminal (PTY), the output breaks, colors disappear, or the agent hangs waiting for terminal input that never arrives.

The skill enforces PTY mode for every coding agent invocation:

```
bash pty:true workdir:~/project command:"claude 'Build a snake game in Python'"
```

**Output:**

```
OpenClaw -> Launching Claude Code with PTY...
Session started. Claude Code is working on: Build a snake game in Python
```

The `pty:true` flag allocates a virtual terminal, giving the coding agent a proper interactive environment. Skip this flag and the agent stalls silently -- one of the most common mistakes when first integrating coding agents.

### Workdir Isolation: Containing the Blast Radius

The `workdir` parameter restricts the coding agent to a specific directory. Claude Code only sees files in that directory and its subdirectories. It cannot wander into your personal files, read your SSH keys, or modify unrelated projects.

```
workdir:~/projects/snake-game
```

This is the same State Isolation pattern from L04, applied at the filesystem level instead of the session level. Each coding task gets its own sandbox. If the coding agent makes a mess, the mess stays contained.

### Background Mode: Long Tasks Without Blocking

Short tasks (fix a typo, add a function) complete in seconds. But building a REST API or refactoring a module might take minutes. Background mode prevents the coding agent from blocking your conversation:

```
bash pty:true background:true workdir:~/project command:"claude 'Build REST API'"
```

**Output:**

```
Session started in background. ID: session_abc123
Use /status session_abc123 to check progress.
```

The skill returns a session ID immediately. You can continue chatting with your AI Employee about other tasks while the coding agent works. When you want an update:

- `process action:log sessionId:abc123` -- read the coding agent's terminal output
- `process action:poll sessionId:abc123` -- check if it's still running or finished

When the coding agent finishes, it triggers an OpenClaw notification:

```
openclaw system event --text "Done: Built REST API with 4 endpoints, all tests passing"
```

Your phone buzzes with the result. No polling required.

## The Delegation Chain: Why This Changes Everything

Compare two approaches to the same request -- "Build me a REST API for my reading list":

**Without the coding-agent skill:**

```
You -> OpenClaw -> LLM generates code in chat -> you copy-paste
  -> you fix errors manually -> you run tests yourself
```

The LLM produces code in a chat window. It cannot see your file system. It cannot run the code. It cannot read error messages. It cannot iterate. You become the integration layer between the LLM's output and the actual computer.

**With the coding-agent skill:**

```
You -> OpenClaw -> coding-agent skill -> Claude Code
  -> reads files, writes code, runs tests, fixes errors, iterates
    -> delivers working result
```

Claude Code has access to the file system. It creates files, runs them, reads error messages, and fixes issues autonomously. It operates like a developer sitting at a terminal -- not like a chatbot pasting code into a message.

This is delegation, not generation. OpenClaw does not try to be a coding expert. It recognizes the task type and routes it to a specialist. This is the same management pattern humans use: a good manager does not do every task personally -- they identify the right person for the job and delegate.

## The Self-Building Pattern

Here is where the architecture becomes recursive.

OpenClaw's own development uses this exact pattern. The OpenClaw repository contains a file called CLAUDE.md (a symlink to AGENTS.md) -- a configuration file that tells Claude Code how to work on the OpenClaw codebase itself.

Follow this chain:

1. You send a message to OpenClaw: "Fix issue #78 in the OpenClaw repo"
2. OpenClaw activates the coding-agent skill
3. The skill launches Claude Code pointed at the OpenClaw source code
4. Claude Code reads AGENTS.md (which is the CLAUDE.md configuration)
5. Claude Code uses those instructions to understand the codebase -- its conventions, test patterns, architecture
6. Claude Code fixes the issue, runs tests, commits, and pushes
7. OpenClaw reports the result back to you on Telegram

The Custom Agent (OpenClaw) is using the General Agent (Claude Code) to modify its own source code. Peter Steinberger, OpenClaw's creator, described this on X with a line that captures the entire architecture: "The Claw gotta orchestrate itself."

It was not a joke. It is the architecture. The AI Employee you configured is using a coding agent to improve itself.

## Parallel Coding at Scale

A single coding agent handles one task at a time. But OpenClaw can spawn multiple coding agents simultaneously, turning your phone into a command center for parallel development work.

**Practical scenarios:**

- **Parallel issue fixing**: Create git worktrees for each issue, launch separate Claude Code instances in each worktree
- **Batch code review**: One coding agent per pull request, all analyzing code in parallel
- **Multi-file refactoring**: Split a large refactoring into independent modules, assign one agent per module

OpenClaw manages concurrency through sub-agent configuration:

| Setting                 | Default | Purpose                                                                               |
| ----------------------- | ------- | ------------------------------------------------------------------------------------- |
| **maxSpawnDepth**       | 2       | An orchestrator sub-agent can spawn its own workers (main -> orchestrator -> workers) |
| **maxChildrenPerAgent** | 5       | Caps how many active child processes one session can manage                           |
| **maxConcurrent**       | 8       | Global limit on parallel coding agents                                                |

The depth limit prevents infinite recursion. The concurrency limit prevents your machine from running out of memory. Results flow back up the chain: workers report to orchestrator, orchestrator reports to main agent, main agent reports to you.

This is not theoretical. OpenClaw users run parallel coding agents from their phone to fix multiple issues, review multiple PRs, and build multiple features simultaneously.

## The Agent Factory Thesis, Demonstrated

Recall the thesis from Chapter 1: General Agents build Custom Agents. Custom Agents solve domain problems.

OpenClaw completes the second half of the loop:

```
General Agent (Claude Code)
    | builds
    v
Custom Agent (OpenClaw with your skills)
    | orchestrates
    v
General Agent (Claude Code)
    | extends
    v
Custom Agent (now with new capabilities)
    | orchestrates again...
    v
```

Each cycle through this loop:

1. The **General Agent** builds or improves the Custom Agent
2. The **Custom Agent** orchestrates the General Agent for new work
3. The General Agent's work makes the **Custom Agent more capable**
4. The more capable Custom Agent can orchestrate **more sophisticated work**

This is a self-improving system. The boundary between "using" an AI Employee and "developing" one disappears. Your AI Employee is simultaneously your tool and your development partner.

## What This Means for Chapter 13

In Chapter 13, you build your own AI Employee using Claude Code. Now you understand something the previous six lessons only hinted at:

You will not just build an AI Employee. You will build an AI Employee that can use Claude Code to extend itself. The specification you write is not a static blueprint. It is a seed that grows -- because the thing you build can command the same tools you used to build it.

The 6 universal patterns are your architectural foundation. The coding-agent skill is your bridge from understanding to building. And the self-improvement loop means your first version is never your last.

## Try With AI

### Prompt 1: Delegation Chain Analysis

```
Walk me through the complete chain of events when I send this message
to my OpenClaw bot on Telegram: "Build a Python script that monitors
my Downloads folder and organizes files by type."

Trace every step: from my phone, through the Gateway, to the coding
agent skill, to Claude Code, and back to my phone. For each step,
identify which of the 6 universal agent patterns (orchestration,
I/O adapters, state isolation, capability packaging, externalized
memory, autonomous invocation) is being used.
```

**What you're learning:** Seeing the 6 universal patterns in action during a real agent-to-agent delegation. This connects abstract architecture (Lesson 04) to concrete behavior, reinforcing that the patterns are not just categories -- they are active mechanisms you can trace through real systems.

### Prompt 2: Self-Improvement Design

```
Design a scenario where an AI Employee uses Claude Code to improve
itself. Start with a basic AI Employee that only handles email
summarization. Show me a 5-step evolution where:

1. The employee identifies a limitation in its own capabilities
2. It uses Claude Code to build a new skill for that limitation
3. It tests the new skill in its own workspace
4. It integrates the skill into its active skill set
5. It can now handle something it could not handle before

For each step, explain: what triggers it, what the coding agent does,
and what changes in the employee's capabilities afterward.
```

**What you're learning:** Self-improving systems design. This is the recursive loop at the heart of the Agent Factory thesis: agents that build better versions of themselves. Understanding this loop prepares you to design your Chapter 13 AI Employee as an evolving system rather than a static tool.

### Prompt 3: Your Domain Application

```
I work in [YOUR DOMAIN]. Design an agent-to-agent workflow where:

1. An AI Employee (Custom Agent) manages my daily tasks via messaging
2. When it encounters a task that requires code, it delegates to
   Claude Code (General Agent)
3. Claude Code builds the solution
4. The AI Employee integrates and delivers the result

Be specific about: what domain tasks trigger coding delegation, what
Claude Code builds, and how the results flow back to me on my phone.
```

**What you're learning:** Applying the agent orchestration pattern to your own work. The value of agent-to-agent delegation depends entirely on YOUR context -- what tasks you face, what tools you need built, and how results should reach you. This prompt bridges abstract architecture to personal design decisions for Chapter 13.
