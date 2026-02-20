---
title: "Five Powers and the Modern AI Stack"
chapter: 1
lesson: 4
duration_minutes: 30
sidebar_position: 4

# HIDDEN SKILLS METADATA
skills:
  - name: "Understanding the UX→Intent Paradigm Shift"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Literacy"
    measurable_at_this_level: "Student can explain the transition from navigation-based interfaces to conversation-based intent and identify which workflows benefit from agentic AI"

  - name: "Identifying the Five Powers of AI Agents"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Analyze"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can recognize and categorize agent capabilities (See, Hear, Reason, Act, Remember) in real systems and explain how they combine to enable autonomous orchestration"

  - name: "Understanding the Three-Layer AI Development Architecture"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Information Literacy"
    measurable_at_this_level: "Student can identify and explain the three layers of the modern AI stack: frontier models, AI-first IDEs, and development agents, plus the role of MCP as interoperability standard"

learning_objectives:
  - objective: "Understand the paradigm shift from User Interface (navigation-based) to User Intent (conversation-based) interaction"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Explanation comparing traditional UX workflows versus agentic intent-driven workflows with concrete examples"

  - objective: "Identify the Five Powers (See, Hear, Reason, Act, Remember) and explain how they combine to enable autonomous orchestration"
    proficiency_level: "A2"
    bloom_level: "Analyze"
    assessment_method: "Analysis of real agentic systems to categorize capabilities by the Five Powers framework"

  - objective: "Recognize the three layers of the modern AI stack and describe what each layer provides"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Classification of AI tools (models, IDEs, agents) into appropriate stack layers with explanation of their roles"

  - objective: "Understand how Model Context Protocol enables tool interoperability and prevents vendor lock-in"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Explanation of MCP as universal standard connecting agents to data/services, analogous to USB for computing"

# Cognitive load tracking
cognitive_load:
  new_concepts: 9
  assessment: "9 concepts (UX→Intent shift, Five Powers, Predictive→Generative→Agentic evolution, 3-layer stack, MCP) within A2 limit of 10 concepts. Framework-heavy but logically connected. ✓"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Analyze a complex agentic system (like Claude Code or customer service AI) to map all Five Powers and identify which powers are most critical for its use case; then research how MCP enables custom integrations for that system"
  remedial_for_struggling: "Focus on single concrete comparison: hotel booking via traditional website (14 steps) vs agentic AI (3 exchanges), then map each action in the agentic version to the Five Powers"

teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "Agent Capabilities and Standards"
  key_points:
    - "The Five Powers (See, Hear, Reason, Act, Remember) become a reusable analysis tool — students should be able to decompose any agentic system into these five capabilities"
    - "The hotel booking comparison (14 manual steps vs 3 exchanges) is the most concrete demonstration of UX→Intent — use it as the lesson's anchor example"
    - "MCP is the 'USB cable' and Skills are the 'App' — this analogy is critical for Lesson 5 where AAIF standards are covered in depth"
    - "The three-layer stack (Frontier Models → AI-First IDEs → Agent Skills) explains how the entire agentic ecosystem is composed"
  misconceptions:
    - "Students think Five Powers means the agent must have ALL five to be useful — many effective agents only use 2-3 powers (e.g., Claude Code primarily uses Reason + Act)"
    - "Students confuse 'Remember' with LLM memory — Remember is an application-level capability (stored preferences, history), not model memory (which is stateless per Lesson 2)"
    - "Students think MCP is a product — MCP is a protocol/standard (like HTTP), not a tool you download and install"
  discussion_prompts:
    - "Which of the Five Powers do you think is hardest to implement well — and which creates the most value when done right?"
    - "If you removed the 'Remember' power from the hotel booking agent, how would the experience change for a returning customer?"
    - "Why did the industry converge on MCP as a standard rather than letting each AI company build their own connector system?"
  teaching_tips:
    - "Start with the 14-step hotel booking — have students count the steps in a workflow they do regularly, then reimagine it as 2-3 intent exchanges"
    - "When teaching the Five Powers, map them onto Claude Code as a familiar reference: See (reads screenshots), Reason (OODA from Lesson 3), Act (writes files, runs tests), Remember (AGENTS.md)"
    - "The Predictive→Generative→Agentic evolution in Part 4 is a three-sentence summary worth repeating: Netflix predicts, ChatGPT generates, Claude Code acts"
    - "Emphasize that the 2024 vs 2026 comparison table (Tool Silos vs Modular Stack) shows how fast the industry moved — students are learning current-state, not history"
  assessment_quick_check:
    - "Have students name all Five Powers from memory and give one example for each"
    - "Ask: 'What is the difference between MCP and Agent Skills?' — expects the hands vs training analogy"
    - "Ask students to identify which layer of the AI stack their current tools belong to"

# Generation metadata
generated_by: "content-implementer v2.0.0 (Part 1 consolidation)"
source_spec: "Part 1 consolidation: 4 chapters (32 lessons) → 1 chapter (8 lessons)"
created: "2025-01-22"
git_author: "Claude Code"
workflow: "lesson consolidation (lessons 07 + 08 → 03)"
version: "1.0.0"

# Legacy compatibility (Docusaurus)
prerequisites:
  - "Understanding of basic AI concepts (from Lesson 1-2)"
  - "Familiarity with traditional software interfaces"
---

# Five Powers and the Modern AI Stack

Something fundamental is changing in how humans interact with software. For decades, we built interfaces—buttons, menus, forms—and trained users to navigate them. Success meant making interfaces "intuitive." But what if the interface disappeared entirely? What if users just stated what they wanted, and software figured out how to do it?

This transformation is possible because AI has evolved through three phases: **Predictive AI** (forecasting from data), **Generative AI** (creating content), and now **Agentic AI** (autonomous action). The agentic era combines five capabilities—the **Five Powers**—with a modular **three-layer stack** that makes composition possible. Understanding both the capabilities (what agents can do) and the architecture (how they're built) is essential for building effective AI systems.

This lesson unifies two foundational frameworks: the **Five Powers** that enable autonomous orchestration, and the **Modern AI Stack** that provides the technical foundation. Together, they explain both *why* the UX→Intent shift is happening now and *how* to build systems that leverage it.

---

## Part 1: From User Interface to User Intent

Traditional software interaction follows this model:

**User → Interface → Action**

- **Users navigate** through explicit interfaces (menus, buttons, forms)
- **Every action requires manual initiation** (click, type, submit)
- **Workflows are prescribed** (step 1 → step 2 → step 3)
- **Users must know WHERE to go and WHAT to click**
- **The interface is the bottleneck** between intent and execution

### Example: Booking a Hotel (Traditional UX)

Let's walk through what this looks like in practice:

1. Open travel website
2. Click "Hotels" in navigation menu
3. Enter destination city in search box
4. Select check-in date from calendar picker
5. Select check-out date from calendar picker
6. Click "Search" button
7. Review list of 50+ hotels
8. Click on preferred hotel
9. Select room type from dropdown
10. Click "Book Now"
11. Fill out guest information form (8 fields)
12. Fill out payment form (16 fields)
13. Click "Confirm Booking"
14. Wait for email confirmation

**Total: 14 manual steps**, each requiring the user to know exactly what to do next.

**The design challenge**: Make these 14 steps feel smooth. Reduce friction. Optimize button placement. Minimize form fields. A/B test checkout flow.

**This is "User Interface thinking"**: The user must navigate the interface the developers designed.

### The New Paradigm: User Intent

Now consider a fundamentally different model:

**User Intent → Agent → Orchestrated Actions**

- **Users state intent conversationally** ("I need a hotel in Chicago Tuesday night")
- **AI agents act autonomously** (search, compare, book, confirm)
- **Workflows are adaptive** (agent remembers preferences, anticipates needs)
- **Users describe WHAT they want; agents figure out HOW**
- **Conversation replaces navigation**

### Example: Booking a Hotel (Agentic UX)

The same goal, achieved differently:

**User**: "I need a hotel in Chicago next Tuesday night for a client meeting downtown."

**Agent**: "Found 3 options near downtown. Based on your preferences, I recommend the Hilton Garden Inn—quiet floor available, $189/night, free breakfast. Your usual king bed non-smoking room?"

**User**: "Yes, book it."

**Agent**: "Done. Confirmation sent to your email. Added to calendar. Uber scheduled for Tuesday 8am to O'Hare. Need anything else?"

**Total: 3 conversational exchanges** replacing 14 manual steps.

**What the agent did autonomously:**
- ✅ Remembered user preferences (quiet rooms, king bed, non-smoking)
- ✅ Inferred need for transportation (scheduled Uber without being asked)
- ✅ Integrated with calendar automatically
- ✅ Understood context (client meeting = business district location)

**This is "User Intent thinking"**: The user expresses goals; the agent orchestrates execution.

---

## Part 2: The Five Powers of AI Agents

Agentic AI can accomplish this transformation because it possesses five fundamental capabilities that, when combined, enable autonomous orchestration:

### 1. 👁️ See — Visual Understanding

**What it means:**
- Process images, screenshots, documents, videos
- Extract meaning from visual context
- Navigate interfaces by "seeing" them
- Understand diagrams and visual data

**Example:**
- Claude Code reading error screenshots to debug issues
- AI extracting data from invoices and receipts
- Agents clicking buttons by visually locating them on screen

### 2. 👂 Hear — Audio Processing

**What it means:**
- Understand spoken requests (voice interfaces)
- Transcribe and analyze conversations
- Detect sentiment and tone
- Process audio in real-time

**Example:**
- Voice assistants understanding natural speech
- Meeting transcription and summarization
- Customer service AI detecting frustration in tone

### 3. 🧠 Reason — Complex Decision-Making

**What it means:**
- Analyze tradeoffs and constraints
- Make context-aware decisions
- Chain multi-step reasoning (if X, then Y, then Z)
- Learn from outcomes

**Example:**
- Agent choosing optimal hotel based on price, location, and preferences
- AI debugging code by reasoning through error causes
- Financial agents evaluating investment opportunities

### 4. ⚡ Act — Execute and Orchestrate

**What it means:**
- Call APIs and use tools autonomously
- Perform actions across multiple systems
- Coordinate complex workflows
- Retry and adapt when things fail

**Example:**
- Claude Code writing files, running tests, committing to Git
- Travel agents booking flights and hotels
- E-commerce agents processing orders and tracking shipments

### 5. 💾 Remember — Maintain Context and Learn

**What it means:**
- Store user preferences and history
- Recall previous interactions
- Build domain knowledge over time
- Adapt behavior based on feedback

**Example:**
- Agent remembering you prefer quiet hotel rooms
- AI assistants referencing previous conversations
- Personal AI learning your communication style

### How the Five Powers Combine

**Individually**, each power is useful but limited.

**Combined**, they create something transformational: **autonomous orchestration**.

**Hotel booking example breakdown:**

1. **Hear**: User speaks request ("Find me a hotel in Chicago")
2. **Reason**: Analyzes requirements (location, timing, context)
3. **Remember**: Recalls user prefers quiet rooms, king beds, downtown proximity
4. **Act**: Searches hotels, compares options, filters by criteria
5. **See**: Reads hotel websites, reviews, location maps
6. **Reason**: Evaluates best option considering all factors
7. **Act**: Books room, schedules transportation, updates calendar
8. **Remember**: Stores this interaction to improve future bookings

**The result**: A multi-step workflow orchestrated autonomously, adapting to context and user needs.


---

## Part 3: The Modern AI Stack

The Five Powers explain *what* agents can do. The Modern AI Stack explains *how* they're built. By early 2026, we have moved from "Chatbots with tools" to **Protocol-Driven Autonomous Workers**.

### Layer 1: Frontier Models—The Reasoning Engines

* **Claude 4.5 / GPT-5.2 / Gemini 3:** The foundation. These models now feature "Native Agentic Reasoning," allowing them to pause, think, and call tools without needing a separate orchestration layer for simple tasks.

### Layer 2: AI-First IDEs—The Context Orchestrators

* **Cursor / Windsurf / VS Code:** These tools no longer just "see" your code; they act as the **Skill Host**. They are the environment where the models, tools, and local file systems meet.

### Layer 3: Agent Skills—The Autonomous Workers

This is the most significant change. Instead of "Custom Agents," we now build **Modular Skills**.

**What the Agent Skills Standard (`agentskills.io`) Provides:**

* **Progressive Disclosure:** An agent doesn't need to read 1,000 pages of documentation at once. It reads the "Skill Metadata" first (name and description). It only "loads" the full instructions and scripts when the task specifically requires them.
* **Skill Portability:** A "SQL Expert" skill you write for **Claude Code** works instantly in **Gemini CLI** or **OpenAI Codex**.
* **Procedural Knowledge:** Skills are stored as simple folders containing a `SKILL.md` file. They tell the agent *how* to do things (e.g., "Review this PR following the Google Style Guide").

**The 2026 Logic:**

* **MCP** = The "USB Cable" (Connects the agent to your Database/Slack/Jira).
* **Agent Skills** = The "App" (Teaches the agent *how* to use that connection to achieve a goal).


---

### Model Context Protocol (MCP): The Universal Connector

Everything in this stack is held together by **MCP**. In 2026, we have moved past the "plugin" era into the "protocol" era.

> **2026 Breakthrough: Bidirectional Sampling**
> A major update to MCP in late 2025 introduced **Sampling**. This allows an MCP Server (like your database) to actually "ask" the LLM a question. For example: A database server can now ask the model, *"I see this schema; should I optimize this specific index for the current query?"* before returning results.

| Feature | 2024 (Pre-MCP) | 2026 (Modern AI Stack) |
| --- | --- | --- |
| **Integration** | Custom API for every tool | Standardized MCP Connectors |
| **Vendor Lock-in** | High (stuck with one ecosystem) | Zero (swap GPT for Claude instantly) |
| **Data Access** | Static RAG / Manual Uploads | Real-time, governed system access |
| **Communication** | One-way (Model → Tool) | **Bidirectional** (Tool ↔ Model) |


---

## Part 4: The Evolution—Why Now?

Understanding where we are helps explain why the UX→Intent shift is happening now.

AI evolved through three phases:

### Phase 1: Predictive AI

**What it did**: Analyzed historical data to forecast outcomes

**Limitation**: Could only predict, not create or act

**Example**: Netflix recommending movies based on watch history

### Phase 2: Generative AI

**What it does**: Creates new content from patterns

**Limitation**: Generates when prompted, but doesn't take action

**Example**: ChatGPT writing essays, code, or creative content when you ask

### Phase 3: Agentic AI

**What it does**: Takes autonomous action to achieve goals

**Breakthrough**: AI shifts from tool to teammate—from responding to orchestrating

**Example**: Claude Code editing files, running tests, committing changes *without asking for each step*

**The key difference**: Earlier AI waited for commands. Agentic AI initiates, coordinates, and completes workflows autonomously.

This evolution unlocked the Five Powers working together, making the UX→Intent paradigm shift possible.

---

## Part 5: The 2024 vs 2026 Shift—From Silos to Composition

### 2024: Tool Silos (Monolithic)

* **Bundled Capabilities:** Each tool had its own "plugin" system. A "GPT Action" didn't work in Claude.
* **Heavy Context:** You had to paste massive instructions into your prompt every time to make the AI follow a specific workflow.
* **Vendor Lock-in:** Moving from one agent to another meant rewriting all your "Custom GPTs."

### 2026: Modular Stack (Composable)

* **Open Standards:** The industry has converged on **MCP** and **agentskills.io**.
* **On-Demand Expertise:** Agents "install" skills dynamically. You can say, *"Install the Stripe-Support skill,"* and your agent instantly knows the procedural steps for refunding a customer without you teaching it.
* **Cross-Platform Agency:** You own your skills. They live in your repo as `.md` files, making your agents independent of any single model provider.

---

## Part 6: Why This Shift Matters

The design challenge has shifted from **"How do we prompt this?"** to **"How do we author the skill?"**

### The Skill Shift

| 2024 Focus (Prompting Era) | 2026 Focus (Skill Era) |
| --- | --- |
| **Prompt Engineering:** Writing long, fragile "System Prompts." | **Skill Authoring:** Writing structured `SKILL.md` files with clear YAML metadata. |
| **Tool Integration:** Writing custom API wrappers for every project. | **Skill Discovery:** Ensuring agents can find the right "Skill" for the job. |
| **Manual Correction:** Telling the AI "no, do it this way" repeatedly. | **Constraint Engineering:** Defining rigid workflows within a Skill that the AI *must* follow. |

**The Skill that Matters Most: Skill Architecture.**

In 2026, high-level developers don't just write code; they write the **Skills** that allow agents to write the code.

* **Before:** You wrote a prompt: *"Please check the database for errors."*
* **Now:** You author a **Database-SRE Skill** that includes:
1. **Metadata:** "Use this when checking for Postgres performance bottlenecks."
2. **Logic:** A Python script that pulls logs via an MCP connector.
3. **Procedure:** A step-by-step markdown guide for how to interpret those logs.

**The result:** You aren't just giving an agent a task; you are giving it a **permanent capability.**

---

## Try With AI

Use your AI companion (Claude Code, ChatGPT, Gemini CLI) to explore these concepts:

### Exercise 1: Reimagine a Workflow as Agentic

**Prompt:**
```
I want to reimagine a manual workflow as agentic. Here's what I currently do [describe
a multi-step task you do regularly, like expense reporting, email management, project
planning, scheduling, research compilation, etc.].

Help me reimagine this as an agentic experience:
1. What would I say to an agent to express my intent?
2. What would the agent need to understand about my preferences?
3. What actions would it take autonomously?
4. Which of the Five Powers (See, Hear, Reason, Act, Remember) would it use for each action?
5. What would the agent need to remember for next time?

Let's discover together: What makes this agentic vs. just automated?
```

**What you're learning:** Intent modeling—thinking in goals and context rather than steps and clicks, plus mapping agentic capabilities to the Five Powers framework.

### Exercise 2: Identify the Five Powers in Real Systems

**Prompt:**
```
Let's analyze a real agentic system (like Claude Code, a travel booking agent, or
customer service AI). For the system we choose, help me identify concrete examples of
each power:

1. SEE: How does it process visual information?
2. HEAR: How does it understand natural language input?
3. REASON: What decisions does it make autonomously?
4. ACT: What actions can it take across systems?
5. REMEMBER: What context does it maintain?

Then let's discover: How do these five powers COMBINE to enable orchestration? What
would break if one power was missing?

Now map this system to the three-layer AI stack:
- Which frontier model powers it (Layer 1)?
- What environment does it run in (Layer 2)?
- Is it a general agent or a custom agent (Layer 3)?
```

**What you're learning:** System analysis—understanding how capabilities combine to create emergent behavior, and connecting capabilities to the technical infrastructure that enables them.

### Exercise 3: Map Your Current Tools to the Stack

**Prompt:**
```
I want to understand the modern AI stack better. Here's what I currently use:
- [IDE you use: VS Code, Cursor, etc.]
- [AI model: Claude, ChatGPT, Gemini, etc.]
- [Any agents or automation: GitHub Actions, custom scripts, etc.]

Help me map these to the three-layer stack:
- Layer 1: Which frontier models do I use?
- Layer 2: Which AI-first IDEs do I work in?
- Layer 3: Which development agents or automation tools do I use?

Then identify:
1. What gaps exist in my current stack?
2. Where could MCP help me connect tools that don't currently integrate?
3. If I wanted to switch models (e.g., Claude → GPT-5), what would I need to change?

Give me concrete recommendations for improving my stack composition.
```

**What you're learning:** Recognizing how real tools compose into the three-layer architecture, identifying which layers you already use, and understanding how modularity enables flexibility and prevents vendor lock-in.
