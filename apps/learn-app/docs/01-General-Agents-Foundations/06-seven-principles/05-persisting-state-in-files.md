---
sidebar_position: 5
title: "Principle 5: Persisting State in Files"
chapter: 6
lesson: 5
duration_minutes: 25
description: "Why file-based state management is the key to effective AI collaboration and reproducible workflows"
keywords: ["state persistence", "files", "context", "CLAUDE.md", "memory", "reproducibility"]

# HIDDEN SKILLS METADATA
skills:
  - name: "State Persistence Design"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "Digital Competence"
    measurable_at_this_level: "Student can explain why state must be persisted in files for AI collaboration and identify what state should be persisted"

  - name: "Context File Management"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Information Management"
    measurable_at_this_level: "Student can create and maintain context files (CLAUDE.md, .cursorrules, etc.) that improve AI collaboration"

  - name: "Reproducible Workflow Design"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can design workflows where all important state is persisted in files, enabling reproducibility and knowledge transfer"

learning_objectives:
  - objective: "Explain why file-based state persistence is essential for AI collaboration"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student can describe what information is lost without state persistence and how file-based persistence solves this problem"

  - objective: "Create and maintain context files that capture project-specific knowledge for AI"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student creates a CLAUDE.md or similar context file that includes relevant project conventions, patterns, and constraints"

  - objective: "Design reproducible workflows where all important state is persisted"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Student structures their work so that another person (or AI) can understand the full context from persisted files alone"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (state persistence, context files, memory limits, reproducibility, knowledge transfer, file as interface) within A2-B1 limit of 7 ✓"

differentiation:
  extension_for_advanced: "Design a comprehensive context file system for a complex project, including architecture diagrams, decision records, and automated context generation from project structure."
  remedial_for_struggling: "Focus on practical examples: show a project without context files (and the resulting repetitive explanations) versus the same project with well-maintained context files."

teaching_guide:
  lesson_type: "core"
  session_group: 2
  session_title: "Workflow Principles"
  key_points:
    - "AI is stateless between sessions — CLAUDE.md is the 'handshake' that gives every session the same project knowledge automatically"
    - "The ROI table (10 min re-explaining x 20 sessions = 3+ hours wasted vs 20 min writing CLAUDE.md once) makes the economic case concrete"
    - "State hierarchy (ephemeral → session → project → permanent) helps students decide WHAT to persist and WHERE"
    - "ADRs capture the 'why' behind decisions — six months later, neither you nor the AI will remember why you chose PostgreSQL without one"
  misconceptions:
    - "Students think CLAUDE.md is just a README — it's specifically formatted for AI consumption with conventions, patterns, and constraints that override generic AI behavior"
    - "Students try to put everything in CLAUDE.md — the 200-line golden rule prevents context overload; link to separate files for domain-specific context"
    - "Students persist ephemeral state like 'currently debugging login bug' — this clutter makes the file less useful; only persist state that survives across sessions"
  discussion_prompts:
    - "How many times this week did you re-explain something to an AI that you could have written in a context file once?"
    - "If you left your project for six months and came back, what decisions would you struggle to remember — and how would ADRs help?"
  teaching_tips:
    - "The 'without persistence vs with persistence' ASCII diagram is the best visual — draw the contrast between knowledge lost vs knowledge accumulated"
    - "Have students create a real CLAUDE.md for their current project during class — the exercise is immediately practical"
    - "The session journal pattern (AI writes its own notes) is a powerful advanced technique — demo it live if time allows"
    - "Emphasize that context files must be updated IN THE SAME COMMIT as code changes — tie it back to Principle 4 (atomic changes)"
  assessment_quick_check:
    - "Name the four levels of the state hierarchy and give an example of what belongs at each level"
    - "What goes in a CLAUDE.md file vs what should NOT go in one?"
    - "Why are Architecture Decision Records valuable for AI collaboration specifically?"
---

# Principle 5: Persisting State in Files

You've had this conversation: "As I mentioned earlier, we use TypeScript with strict mode, we prefix interfaces with 'I', we don't use any, and our API follows REST conventions." You find yourself repeating the same context every time you start a new conversation with AI. Each new session forgets everything from previous sessions. You waste time re-establishing context that never changes.

The solution is simple but powerful: **persist state in files**.

When you store project knowledge, decisions, and context in files within your repository, AI systems can read them directly. You stop repeating yourself. Context becomes cumulative rather than reset each session. New team members (or future you) can understand decisions without hunting through git history.

This lesson explores what to persist, how to structure it, and why file-based persistence is the secret to effective AI collaboration.

## The Memory Problem: Why AI Context Doesn't Persist

### AI Systems Are Stateless

Here's the fundamental limitation: **AI systems have no persistent memory between sessions**.

Each conversation starts fresh:
- Session 1: You explain your project conventions
- Session 2: You explain them again
- Session 3: You explain them a third time

The AI doesn't remember your previous conversations. It doesn't learn about your project over time. Each session is a blank slate.

### Why This Matters

Without persistent state, you face:
- **Repetitive context sharing**: Re-explaining the same things
- **Lost knowledge**: Decisions disappear with closed chats
- **Inconsistency**: Different sessions might get different context
- **Onboarding friction**: New team members start from zero
- **Future confusion**: You forget why you made a decision

| Approach | Time per Session | Over 20 Sessions |
|----------|------------------|------------------|
| Re-explain context each time | ~10 minutes | 3+ hours wasted |
| Write CLAUDE.md once | 0 seconds (auto-read) | 3+ hours saved |

The 20 minutes you spend writing a context file pays for itself after just two sessions. That's the laziness that pays off.

### The Solution: Files as Persistent Memory

Files in your repository are the one thing AI systems can read and that persists across sessions:

```
Repository Structure:
├── src/
├── tests/
├── CLAUDE.md          ← Project conventions for AI
├── docs/
│   └── decisions/     ← Why we made choices
└── .cursorrules       ← AI coding guidelines
```

Every AI session reads these files. Context is shared automatically. Knowledge accumulates.

## What to Persist: The State Hierarchy

Not all state is equal. Some changes constantly (current task status), some rarely changes (architecture decisions), some never changes (project language).

### State Types and Persistence Strategy

| State Type | Change Frequency | Persistence Strategy | Examples |
|------------|------------------|---------------------|----------|
| **Ephemeral** | Every session | Don't persist | Current task, what you're debugging right now |
| **Session** | Within session | Task files, TODO comments | "Working on auth bug," "Need to refactor X" |
| **Project** | Weekly/Monthly | CLAUDE.md, docs | Coding conventions, architecture patterns |
| **Permanent** | Rarely | Architecture Decision Records | Why we chose PostgreSQL, why we use Redux |

### What NOT to Persist

- **Current session context**: "We just discussed the login bug" → This isn't useful tomorrow
- **Transient opinions**: "I think we should rewrite in Rust" → Unless decided, don't document
- **Outdated information**: Update or remove, don't let it rot
- **Sensitive data**: API keys, secrets, passwords → Use environment variables

```
WITHOUT PERSISTENCE               WITH PERSISTENCE

Session 1: "We use TypeScript"    Session 1: Write CLAUDE.md
Session 2: "We use TypeScript"    Session 2: ← reads CLAUDE.md (auto)
Session 3: "We use TypeScript"    Session 3: ← reads CLAUDE.md (auto)
   ...repeats forever                ...never repeat again

        ┌─────────┐                   ┌─────────┐
        │ Session │──► lost           │ Session │──► CLAUDE.md
        └─────────┘                   └────┬────┘      │
        ┌─────────┐                   ┌────┴────┐      │
        │ Session │──► lost           │ Session │◄─────┘
        └─────────┘                   └─────────┘
```

## Context Files: CLAUDE.md and Friends

The most direct way to persist state for AI collaboration is through context files that AI systems automatically read.

### CLAUDE.md: Project Context for AI

Claude Code automatically reads `CLAUDE.md` in your project root. This is the perfect place to capture project-specific knowledge:

```markdown
# Project Context

## Project Overview
This is a customer support dashboard for Acme Inc.

## Tech Stack
- Frontend: React with TypeScript
- Backend: Node.js with Express
- Database: PostgreSQL
- Auth: JWT tokens

## Coding Conventions
- Use functional components with hooks
- Prefix interfaces with 'I' (IUser, IAuthResponse)
- No 'any' types—use 'unknown' if truly unknown
- Async functions must handle errors explicitly

## File Structure
src/
├── components/     # React components
├── services/       # API calls
├── utils/          # Shared utilities
└── types/          # TypeScript types

## Important Patterns
- API calls go through services/, not from components
- All errors are logged and user-friendly messages shown
- Components receive data via props, no global state except auth

## Current Work
- Refactoring authentication to use refresh tokens
- Next: Add password reset flow
```

Every Claude Code session reads this automatically. No more repeating conventions.

> **The Handshake**: When Claude Code sees CLAUDE.md, it doesn't just read it—it treats your project-specific conventions as context that takes precedence over generic patterns. Think of it as a handshake between you and the AI: "These are MY rules for THIS project."

### Other Context Files

Different AI tools read different files:

| File | Tool | Purpose |
|------|------|---------|
| `CLAUDE.md` | Claude Code | Project context for Anthropic Claude |
| `.cursorrules` | Cursor | Coding rules and patterns |
| `README.md` | All tools | General project documentation |
| `.aider.conf.yml` | Aider | AI coding assistant configuration |
| `docs/adr/` | All tools | Architecture Decision Records |

## Architecture Decision Records: Why We Made Choices

One of the most valuable things to persist: **why you made technical decisions**.

Six months later, you won't remember why you chose PostgreSQL over MongoDB. A new developer won't know why you used Redux instead of Context API. These decisions deserve persistent documentation.

### ADR Template

```markdown
# ADR-001: Choose PostgreSQL as Primary Database

## Status
Accepted

## Context
We need a database for customer data. Requirements:
- ACID transactions for payment processing
- Complex relationships between customers, orders, products
- SQL expertise available on team

## Decision
Use PostgreSQL as the primary database.

## Consequences
Positive:
- ACID guarantees for payments
- Mature tooling and monitoring
- Team has PostgreSQL experience

Negative:
- Vertical scaling limitations (mitigate with read replicas)
- More complex schema management than NoSQL

## Alternatives Considered
- MongoDB: Rejected due to ACID requirements
- MySQL: Rejected due to team's PostgreSQL preference

## Date
2024-03-15
```

### Why ADRs Matter

When someone (or AI) asks "Why did we use PostgreSQL?", you don't need to remember. The ADR explains the decision, alternatives considered, and tradeoffs.

This is especially valuable for AI: when suggesting changes, AI can read ADRs and respect previous decisions rather than re-opening settled debates.

## Reproducibility: The Ultimate Goal

The highest form of state persistence: **someone (or some AI) can understand your entire project from the files alone**.

### What Makes a Project Reproducible?

**Complete Context**:
- CLAUDE.md explains conventions and current work
- README.md explains how to run the project
- ADRs explain why key decisions were made
- Code comments explain tricky logic
- Tests document expected behavior

**Self-Documenting Structure**:
```
acme-dashboard/
├── CLAUDE.md              # "This is a customer dashboard..."
├── README.md              # "To start: npm install && npm start"
├── docs/
│   ├── adr/              # "Why PostgreSQL? Why Redux?"
│   ├── architecture.md   # "How components interact"
│   └── api.md            # "API endpoint documentation"
├── src/
│   ├── components/       # Organized by feature
│   ├── services/         # API abstraction layer
│   └── types/            # TypeScript definitions
└── tests/                # Document behavior
```

Someone opening this project for the first time can:
1. Read CLAUDE.md to understand what it is and how to work on it
2. Read README.md to run it
3. Read ADRs to understand key decisions
4. Read code to understand implementation
5. Read tests to understand expected behavior

AI can do the same—giving it complete context without you explaining anything.

## Practical State Persistence Patterns

### Pattern 1: Convention Documentation

Capture coding conventions in context files:

```markdown
## Naming Conventions
- Files: kebab-case (user-service.ts)
- Components: PascalCase (UserProfile.tsx)
- Functions: camelCase (getUserById)
- Constants: UPPER_SNAKE_CASE (API_BASE_URL)

## Import Order
1. React imports
2. Third-party imports
3. Internal imports (grouped: types, components, services, utils)
4. CSS imports
```

AI follows these automatically. Code stays consistent.

### Pattern 2: Work-in-Progress Tracking

Document current work to help future sessions:

```markdown
## Current Work (2025-01-22)
### In Progress
- Refactoring auth to use refresh tokens

### Completed Recently
- Added email verification (2025-01-20)
- Fixed pagination bug (2025-01-18)

### Next Up
- Add password reset flow
- Implement rate limiting on API
```

When you return to a project after a break, you know exactly where you left off.

### Pattern 3: Known Issues and Gotchas

Document things that trip people up:

```markdown
## Known Issues
- API rate limits: 100 req/min, use exponential backoff
- Test database: Must run `docker-compose up -d db` first
- Hot reload: Doesn't work for environmental variables, restart server
```

AI can warn about these when suggesting changes.

### Pattern 4: The Session Journal

Here's a powerful pattern: ask the AI to maintain a `scratchpad.md` or `session-notes.md` file where it records its own reasoning.

```markdown
## Session Notes (2025-01-22)

### What I figured out
- The auth bug was caused by token expiry not being checked
- Fixed by adding middleware in src/auth/validate.ts

### Where I left off
- Implemented fix, tests passing
- Still need to handle refresh token edge case

### Questions for next session
- Should refresh tokens have the same expiry policy?
- Consider adding rate limiting to token refresh endpoint
```

**The insight**: Documentation is for *others*. Persisting state is for *the loop*. When the AI writes down its thought process, the next session picks up mid-thought instead of starting from scratch.

## The Anti-Pattern: When Persistence Goes Wrong

### Anti-Pattern 1: Outdated Context

```markdown
## Tech Stack
React, Redux, PostgreSQL
```

But you migrated to MongoDB six months ago.

**Fix**: Treat context files like code—update them in the *same commit* as your code changes. Renamed a function? Update CLAUDE.md in that commit. Changed the tech stack? Update the context file before merging. This ties directly to Principle 4 (Atomic Changes): one logical change, one commit, documentation included.

### Anti-Pattern 2: Over-Documenting Trivia

```markdown
## We use semicolons
## We use 2-space indentation
## We use double quotes for strings
```

These are formatting conventions—let your linter handle them. Context files should capture meaningful decisions, not trivia.

### Anti-Pattern 3: Scattered Knowledge

Some decisions in Slack, some in email, some in tickets, some in people's heads.

**Fix**: If it's a decision, write an ADR. If it's a convention, add to CLAUDE.md. If it's not in git, it doesn't exist.

### Anti-Pattern 4: Context Overload

Pasting entire library documentation, full API references, or every possible convention into CLAUDE.md.

**The problem**: AI has a limited context window. Stuffing too much in means the AI might miss the important parts—or run out of room for your actual conversation.

**Golden Rule**: Keep context files dense but concise. Link to external docs instead of pasting them. Summarize the parts you actually use. If your CLAUDE.md is longer than 200 lines, ask yourself what can be moved to separate files that AI reads only when relevant.

## Working with AI: Guiding Context Reading

AI systems can be guided to read specific context:

```markdown
# When working on authentication:
Read: CLAUDE.md, docs/adr/003-auth-decision.md, src/auth/README.md

# When working on database:
Read: CLAUDE.md, docs/adr/001-database-choice.md, docs/schema.md

# When adding new features:
Read: CLAUDE.md first, then the relevant feature directory
```

This focuses AI's attention on relevant context rather than reading everything.

## Why This Principle Matters: Compounding Knowledge

Without state persistence:
- Each session starts from zero
- Knowledge doesn't accumulate
- Onboarding is expensive
- Decisions are forgotten

With state persistence:
- Each session builds on previous ones
- Knowledge compounds over time
- Onboarding is self-service
- Decisions are preserved

The difference is dramatic. With good state persistence, your AI collaboration gets better over time. Each session benefits from all previous documentation. You're not starting fresh—you're continuing an ongoing conversation.

## This Principle in Both Interfaces

Files are the durable layer that both General Agents share. The specific file types differ, but the principle is universal.

| Pattern | Claude Code | Claude Cowork |
|---------|-------------|---------------|
| **Context file** | CLAUDE.md (explicit, you create it) | Could use CLAUDE.md if working in folder with one |
| **Progress tracking** | Request explicit progress.md files | Progress visible in right panel during session |
| **Artifacts** | All outputs are files in filesystem | Artifacts panel shows generated files |
| **Session persistence** | Files persist, chat history doesn't | Same—files are the durable layer |
| **Handoff** | Document approach in files for next session | Save outputs for future reference |

**In Cowork**: Ask Cowork to maintain a `progress.md` file tracking what's been completed. Create a `context.md` file before starting complex projects. These files serve the same purpose as CLAUDE.md—they persist knowledge that would otherwise be lost between sessions.

**Non-coder tip**: Start every Cowork session with: *"Before answering any questions, please read 'project_brief.docx' in my files."* This simple prompt gives Cowork the same "memory" that CLAUDE.md gives Claude Code. The principle is universal—only the file format changes.

**The meta-insight**: Both interfaces are stateless. The AI doesn't remember you. But files do. The more you invest in persistent context files, the smarter every future session becomes—regardless of which interface you use.

## Try With AI

### Prompt 1: Context File Creation

```
I want to create a CLAUDE.md file for my project.

Here's what I can tell you about my project:
- [Project description]
- [Tech stack]
- [Coding conventions I follow]
- [File structure]
- [Any patterns or important decisions]

Help me create a comprehensive CLAUDE.md that will help AI work effectively on this project.

After creating it, help me understand:
- What did I include that's most valuable?
- What did I miss that should be added?
- How will this file improve my AI collaboration going forward?
```

**What you're learning**: How to capture project-specific knowledge in a format that AI systems can use. You're learning to identify what context matters and how to structure it for maximum impact.

### Prompt 2: ADR Writing Practice

```
I want to practice writing Architecture Decision Records.

Help me write an ADR for a decision I made recently:

[Describe a technical decision you made—choice of database, framework, library, or approach]

For this ADR:
1. What was the context/problem?
2. What decision did I make?
3. What are the consequences (positive and negative)?
4. What alternatives did I consider?
5. Why did I choose this over the alternatives?

Write the ADR in proper format, then help me understand how this document would be valuable to:
- Future me (6 months from now)
- A new team member
- An AI assistant working on this project
```

**What you're learning**: How to document technical decisions in a way that preserves the "why" behind choices. You're learning to create knowledge assets that compound in value over time.

### Prompt 3: Reproducibility Audit

```
I want to audit my project for reproducibility.

Help me assess: If a new developer (or AI) joined my project today, could they understand everything from the files alone?

Check for:
1. Project overview: Is there a clear description of what this project is?
2. Getting started: Can someone run the project from README instructions?
3. Conventions: Are coding patterns documented?
4. Decisions: Are key technical choices explained with ADRs?
5. Architecture: Is the system structure documented?
6. Current work: Is it clear what's being worked on now?

For each area, tell me:
- What's currently in place?
- What's missing or inadequate?
- What specific file should I create or update to improve this?

Then, help me create the missing pieces one by one.
```

**What you're learning**: How to design a project for maximum reproducibility. You're learning to create a self-documenting codebase where knowledge persists and compounds—making collaboration with humans and AI more effective.

### Safety Note

Never persist sensitive data (API keys, passwords, tokens, personal information) in context files like CLAUDE.md. These files are committed to version control and visible to anyone with repository access. Use environment variables (`.env` files in `.gitignore`) for secrets. If you accidentally commit a secret, rotate it immediately—removing it from git history is not enough.
