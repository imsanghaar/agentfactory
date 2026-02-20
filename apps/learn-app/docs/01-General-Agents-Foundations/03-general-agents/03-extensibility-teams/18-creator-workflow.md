---
slug: /General-Agents-Foundations/general-agents/creator-workflow
title: "The Creator's Workflow: Claude Code Best Practices"
sidebar_position: 18
chapter: 3
lesson: 18
duration_minutes: 22
estimated_time: "22 mins"
chapter_type: Hybrid
running_example_id: boris-workflow

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration) - Synthesis of all concepts through real-world expert workflow"
layer_1_foundation: "N/A (all foundations established in L01-L17)"
layer_2_collaboration: "Analyzing expert workflow patterns, comparing to personal practice, identifying gaps and improvements"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA (Institutional Integration Layer)
skills:
  - name: "Synthesizing Claude Code Workflow Patterns"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can analyze an expert workflow, map techniques to concepts learned in chapter, and identify patterns to adopt in their own practice"
  - name: "Parallel Session Management"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can set up git worktrees and manage multiple Claude sessions"
  - name: "Self-Evolving Documentation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can use the CLAUDE.md self-writing technique to capture corrections"

learning_objectives:
  - objective: "Set up parallel Claude sessions using git worktrees"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Creating 3 worktrees and running concurrent sessions"
  - objective: "Apply the Claude-reviews-Claude pattern for plan validation"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Using two sessions to write and review an implementation plan"
  - objective: "Implement the CLAUDE.md self-writing technique"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Using the correction-to-rule pattern after a mistake"
  - objective: "Create session hygiene skills (/techdebt)"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Building and using a /techdebt skill"
  - objective: "Configure Claude Code for learning and generate HTML presentations"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Enabling learning output style and generating visual documentation"

# Cognitive load tracking
cognitive_load:
  new_concepts: 5
  assessment: "5 new concepts (parallel sessions, Claude-reviews-Claude, CLAUDE.md self-writing, session hygiene skills, learning mode) - synthesis lesson with actionable techniques from creator's workflow"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Implement full 5-worktree workflow; create custom verification subagents; build skill portfolio across projects"
  remedial_for_struggling: "Start with single worktree; focus on self-writing CLAUDE.md technique first; implement one new practice at a time"

# Generation metadata
generated_by: "Claude Opus 4.5"
source_spec: "Boris Cherny workflow lesson - v3.0 incorporating Claude Code team practices"
created: "2026-01-08"
last_modified: "2026-02-02"
git_author: "Claude Code"
workflow: "direct implementation"
version: "3.3.0"
refinement_notes: "v3.3.0 - Domain-neutral tables for all new sections (problem solving, prompting, workspace, research). v3.2.0 - Complete February 2026 thread coverage. v3.1.0 - Unified skill architecture. v3.0.0 - Initial Claude Code team practices."

teaching_guide:
  lesson_type: "supplementary"
  session_group: 6
  session_title: "Autonomous Workflows, Creator Practices, and Exercises"
  key_points:
    - "Context window degradation is the unifying constraint behind ALL best practices — parallel sessions, /clear, subagents for investigation, and Plan Mode all manage this one resource"
    - "The CLAUDE.md self-writing technique ('Update your CLAUDE.md so you don't make that mistake again') turns every correction into permanent institutional memory"
    - "Claude-reviews-Claude uses a fresh session (Session B) to review the plan from Session A — the fresh context catches blind spots the cluttered writer session missed"
    - "Boris's '15-20 sessions' is expert-level; students should start with 2-3 parallel sessions and scale up as they build the habit"
  misconceptions:
    - "Students think they need 15+ parallel sessions like Boris to be productive — the lesson explicitly says start with 2-3; the principle is parallelism, not volume"
    - "Students confuse Plan Mode (aligning understanding before execution) with being cautious — Boris uses Plan Mode for EVERY non-trivial task, not just when unsure"
    - "Students assume the self-writing CLAUDE.md technique only works for code projects — it applies equally to knowledge work, writing conventions, and domain-specific rules"
    - "Students think 'use Opus 4.5 with thinking for everything' means faster models are always worse — the insight is about total task time including corrections, not per-response speed"
  discussion_prompts:
    - "Boris says 10-20% of his sessions are abandoned. How does that change your attitude toward starting fresh versus pushing through a confused session?"
    - "What is one correction you have given Claude in the past week that could have been captured as a CLAUDE.md rule? Write the rule now."
    - "Which practice from this lesson would have the highest impact on YOUR current workflow if you adopted it tomorrow?"
  teaching_tips:
    - "Open with the context window constraint table — it provides the 'why' for every technique and prevents students from seeing practices as disconnected tips"
    - "Have students try the Claude-reviews-Claude pattern live in class: Session A writes a plan, Session B reviews it as a staff engineer, then compare the improvement"
    - "The 'Mapping the Complete Workflow' table at the end is an excellent review tool — have students match each practice to the lesson where they learned the underlying concept"
    - "Encourage students to create their first /session-review skill before leaving class — it takes 5 minutes and establishes the session hygiene habit immediately"
  assessment_quick_check:
    - "Name the single constraint that unifies all Claude Code best practices discussed in this lesson"
    - "What is the exact phrase Boris recommends saying to Claude after every correction?"
    - "In the Claude-reviews-Claude pattern, why does Session B catch things Session A missed?"

# Legacy compatibility (Docusaurus)
prerequisites:
  - "Lessons 01-17: Complete Claude Code features"
  - "Understanding of CLAUDE.md, MCP, skills, subagents, hooks, and settings"
---

# The Creator's Workflow: Claude Code Best Practices

Boris Cherny, creator and head of Claude Code at Anthropic, has shared detailed insights into how he and his team use the tool in production. While Boris works primarily in software development, the practices his team has refined reveal universal patterns that transform Claude Code from a capable assistant into a force multiplier—regardless of your domain.

What makes these practices valuable isn't exotic techniques. It's seeing how the features you've learned in this chapter combine into a production workflow that lets one person operate like a small team.

This lesson maps the Claude Code team's workflow to everything you've learned—and connects it to the [official Claude Code best practices](https://code.claude.com/docs/en/best-practices)—showing you what expert-level usage looks like in practice. Where techniques are developer-specific, we'll note the equivalent approach for knowledge workers.

---

## The Fundamental Constraint: Context Window

Before diving into specific techniques, understand the principle that unifies all Claude Code best practices:

> **Claude's context window fills up fast, and performance degrades as it fills.**

The context window holds your entire conversation: every message, every file Claude reads, every command output. A single research session or complex task can consume tens of thousands of tokens. As context fills, Claude may start "forgetting" earlier instructions or making more mistakes.

**Why this matters:**

| Practice                    | How It Manages Context                                         |
| --------------------------- | -------------------------------------------------------------- |
| Parallel sessions           | Each session = isolated context window                         |
| Claude-reviews-Claude       | Fresh reviewer context catches what cluttered writer missed    |
| Plan Mode first             | Aligns understanding upfront, reducing correction iterations   |
| Subagents for investigation | Explores in separate context, reports back summaries           |
| `/clear` between tasks      | Resets context for fresh starts                                |
| CLAUDE.md self-writing      | Encodes learning once, prevents re-explanation across sessions |
| Session-end review          | Captures insights while context is fresh, before clearing      |

Every practice in this lesson connects back to this constraint. When you understand context as the fundamental resource, the "why" behind each technique becomes clear.

---

## Setting Up Parallel Sessions

Boris maintains 15-20 concurrent sessions in his workflow. The key insight from the Claude Code team: running multiple isolated sessions is the single biggest productivity unlock.

> "It's the single biggest productivity unlock, and the top tip from the team."
>
> — Boris Cherny

:::info The Core Principle
Boris runs many sessions because he manages a massive software product. **You do not need this many.** Start with 2-3. The principle is about _parallel workstreams_—like having multiple assistants working different problems simultaneously.
:::

**How to run parallel sessions:**

| If you're a...       | Approach                                                                                     |
| -------------------- | -------------------------------------------------------------------------------------------- |
| **Developer**        | Use git worktrees or separate checkouts—each directory gets its own Claude session           |
| **Knowledge worker** | Open multiple browser tabs on claude.ai/code, or use Claude Desktop with separate workspaces |
| **Anyone**           | Simply open multiple terminal windows in different project folders                           |

**For developers using git worktrees:**

```bash
# Create worktrees for different workstreams
git worktree add ../auth-feature feature/auth
git worktree add ../bugfix-api bugfix/api-error
git worktree add ../experiment main

# Each worktree is a separate directory
cd ../auth-feature && claude   # Session 1
cd ../bugfix-api && claude     # Session 2 (new terminal)
cd ../experiment && claude     # Session 3 (new terminal)
```

**Why parallel directories work better than switching:**

- **Switching contexts loses Claude's memory** — when you change projects, Claude loses the conversation
- **Parallel directories = parallel contexts** — each session maintains its own conversation history
- **Work doesn't conflict** — until you explicitly combine results

**Pro tips from the team:**

- Set up shell aliases (`za`, `zb`, `zc`) to hop between worktrees in one keystroke
- Keep a dedicated "analysis" worktree for reading logs and running queries—no code changes
- Use `/statusline` to always show context usage and current git branch in your status bar
- Color-code and name your terminal tabs—one tab per task/worktree

**Start small:** Begin with 3 parallel sessions before scaling. The cognitive overhead of managing many sessions takes practice.

**Connection to Chapter Concepts:**

- **Lesson 01 (Origin Story)**: The agentic paradigm means Claude works autonomously. Parallel sessions multiply this agency.
- **Lesson 11 (Subagents)**: Each session is like a subagent with a specific task—research in one, drafting in another, review in a third.

---

## Plan Mode First (Always)

Boris activates Plan Mode (Shift+Tab twice) for every non-trivial task. He iterates back and forth with Claude until the plan is solid, then switches to auto-accept mode for execution.

> "A good plan is really important!"
>
> — Boris Cherny

**The Pattern:**

1. Start with a goal (e.g., "Add authentication to this project")
2. Enter Plan Mode
3. Discuss and refine until the plan makes sense
4. Switch to auto-accept mode
5. Claude typically one-shots the execution

**Why this works**: When you spend time on planning, you align Claude's understanding with your intent. The investment in planning pays off through faster, more accurate execution. No wasted iterations fixing misunderstandings.

**When things go sideways**: The moment something goes wrong, switch back to Plan Mode and re-plan. Don't keep pushing through a confused execution. Some team members also explicitly tell Claude to enter Plan Mode for verification steps—not just for the initial build.

### The Claude-Reviews-Claude Pattern

A powerful technique from the Claude Code team involves using separate sessions for writing and reviewing:

> "One person has one Claude write the plan, then they spin up a second Claude to review it as a staff engineer."
>
> — Boris Cherny

**The workflow:**

**Session A (Writer)**: Create the implementation plan

```
I need to add rate limiting to our API. Use Plan Mode.
Research our existing middleware patterns and create a detailed plan.
```

**Session B (Reviewer)**: Review with fresh eyes

```
You are a staff engineer reviewing this implementation plan.
Look for: edge cases, security issues, missing error handling,
architectural concerns, and things the author might have missed.

Here's the plan:
[paste plan from Session A]
```

**Session A**: Address feedback

```
Here's the review feedback: [Session B output].
Update the plan to address these issues.
```

**Why this works:**

- Fresh context catches blind spots (Session B hasn't seen the exploration that led to the plan)
- Different "persona" surfaces different concerns
- Two-pass verification before any code is written
- Prevents sunk-cost fallacy (it's harder to catch flaws in your own plan)

**Connection to Chapter Concepts:**

- **Lesson 11 (Subagents)**: Plan is a built-in subagent that researches your codebase. The reviewer is effectively another subagent with a different role.

---

## CLAUDE.md as Team Infrastructure

Boris's team maintains a shared CLAUDE.md file checked into git. The entire team contributes multiple times per week.

The key practice: **when Claude makes a mistake, document it immediately**.

> "Anytime we see Claude do something incorrectly we add it to the CLAUDE.md, so Claude knows not to do it next time."
>
> — Boris Cherny

They also use GitHub's `@.claude` tagging feature during code reviews—when a reviewer sees Claude could have done better, they update CLAUDE.md as part of the review process.

### Let Claude Write Its Own Rules

One of the most actionable techniques from the Claude Code team:

> "After every correction, end with: 'Update your CLAUDE.md so you don't make that mistake again.' Claude is eerily good at writing rules for itself."
>
> — Boris Cherny

**Example flow:**

1. Claude generates code with wrong import path:

   ```typescript
   import { auth } from "utils/auth"; // Wrong
   ```

2. You correct:

   ```
   That import should be from '@/utils/auth' not 'utils/auth'.
   We use path aliases in this project.
   ```

3. **Add the magic phrase:**

   ```
   Update your CLAUDE.md so you don't make that mistake again.
   ```

4. Claude adds to CLAUDE.md:

   ```markdown
   ## Import Paths

   - Always use the @/ path alias for imports
   - Example: `import { auth } from '@/utils/auth'`
   - Never use relative paths like 'utils/auth'
   ```

**Why Claude writes better rules than you:**

- Claude understands the exact context of what went wrong
- It knows which variations of the mistake to prevent
- The rule is immediately testable (Claude follows what it wrote)

**The compound effect:** Every correction makes Claude smarter. Over weeks, your CLAUDE.md becomes a knowledge base that prevents entire categories of mistakes.

**Notes directory pattern:** One engineer tells Claude to maintain a notes directory for every task/project, updated after every PR. They then point CLAUDE.md at it. This creates project-specific context that accumulates over time.

**Connection to Chapter Concepts:**

- **Lesson 05 (CLAUDE.md)**: You learned to create project context. Boris shows how it evolves into self-improving institutional memory.

---

## Skills for Workflow Automation

The Claude Code team applies a simple but powerful heuristic:

> "If you do something more than once a day, turn it into a skill."
>
> — Boris Cherny

:::tip Skill Architecture
Every skill can be **user-invoked** (you type `/skill-name`) or **agent-invoked** (Claude uses it automatically). Use `disable-model-invocation: true` to restrict a skill to manual invocation only.
:::

### Session-End Review Skills

Boris recommends building a skill you run at the end of every session—while the context is still fresh:

> "Build a skill and run it at the end of every session."

**For developers (`/techdebt`):**

```markdown
# .claude/skills/techdebt/SKILL.md

---

name: techdebt
description: Review session for technical debt
disable-model-invocation: true

---

Review files modified during this session for:

- Duplicated code that could be extracted
- Dead code or unused functions
- TODO comments that need attention
- Overly complex functions

Output as a prioritized checklist.
```

**For knowledge workers (`/session-review`):**

```markdown
# .claude/skills/session-review/SKILL.md

---

name: session-review
description: Summarize session decisions and follow-ups
disable-model-invocation: true

---

Review what we accomplished this session:

1. Summarize key decisions made
2. List any open questions or uncertainties
3. Identify follow-up tasks
4. Note any insights worth capturing in CLAUDE.md

Output as a brief session summary I can save.
```

**The habit:** Before closing any session, run your review skill. The context is fresh—Claude remembers exactly what you discussed and can spot things you might have missed.

### Building Your Skill Portfolio

> "Create your own skills and commit them to git. Reuse across every project."

**Pattern:**

1. Any workflow you do more than once a day → create a skill
2. Store project-agnostic skills in `~/.claude/skills/` (user-level)
3. Or maintain a `skills-library` repo you clone into each project

**Example skills (adapt to your domain):**

| Skill             | Developer Use                                     | Knowledge Worker Use                        |
| ----------------- | ------------------------------------------------- | ------------------------------------------- |
| `/commit`         | Pre-compute git status, create clean commits      | Save and organize completed work            |
| `/simplify`       | Clean up code after implementation                | Condense verbose drafts                     |
| `/verify`         | Run comprehensive test suite                      | Cross-check facts and consistency           |
| `/session-review` | Find technical debt at session end                | Summarize decisions and follow-ups          |
| `/context-dump`   | Sync 7 days of GitHub, Slack, CI into one context | Sync meetings, docs, tasks into one context |

**Advanced pattern**: Build analytics-engineer-style agents that write dbt models, review code, and test changes in dev. These become reusable assets that any team member can invoke.

**Connection to Chapter Concepts:**

- **Lessons 08-09 (Skills)**: You learned the unified skill architecture. Boris shows the discipline of building a portable skill portfolio.

---

## Specialized Subagents for Common Workflows

Boris uses custom subagents for his most common workflows:

| Subagent          | Purpose                                              |
| ----------------- | ---------------------------------------------------- |
| `code-simplifier` | Cleans up code after Claude completes implementation |
| `verify-app`      | Detailed end-to-end testing instructions             |
| `build-validator` | Validates builds before merging                      |
| `code-architect`  | Architecture review for complex changes              |

> "I think of subagents as automating the most common workflows that I do for most PRs."
>
> — Boris Cherny

**The Investigation Pattern**: Beyond PR workflows, subagents keep your main context clean. When Claude researches a codebase, it reads many files—all consuming your context. Instead:

```
Use subagents to investigate how our authentication system handles
token refresh, and whether we have any existing OAuth utilities.
```

The subagent explores in its own context window, reads relevant files, and reports back with findings—all without cluttering your main conversation.

**Throw more compute at problems**: Append "use subagents" to any request where you want Claude to parallelize the work. Claude will spin up multiple subagents to tackle different aspects simultaneously.

**Advanced: Route permissions to Opus 4.5 via hook**: Some team members route permission requests through an Opus 4.5 hook that scans for attacks and auto-approves safe operations—letting Claude work more autonomously while maintaining security.

**Connection to Chapter Concepts:**

- **Lesson 11 (Subagents)**: You learned to create subagents with `/agents`. Boris shows what a mature subagent ecosystem looks like.

---

## Verification is Everything

This might be the most important insight from Boris's workflow:

> "Probably the most important thing to get great results out of Claude Code: give Claude a way to verify its work. If Claude has that feedback loop, it will 2-3x the quality of the final result."
>
> — Boris Cherny

**How he implements this:**

- Claude uses the Claude Chrome extension to test UI changes directly
- Opens a browser, tests the interface, iterates until the code works and UX feels good
- Domain-specific verification ranges from simple (running bash commands) to complex (browser or phone simulator testing)

**The Philosophy**: You don't trust AI output—you instrument it. Give Claude tools to check its own work, and quality improves dramatically.

**Connection to Chapter Concepts:**

- **Lesson 12 (MCP Integration)**: MCP tools can include verification capabilities—testing endpoints, validating outputs, checking UI state
- **Lesson 15 (Hooks)**: Hooks can trigger automated verification after Claude makes changes

---

## PostToolUse Hooks for Formatting

Boris's team uses a simple but effective hook:

```json
{
  "PostToolUse": {
    "matcher": "Write|Edit",
    "command": "bun run format || true"
  }
}
```

This runs the formatter after every file write or edit. Claude generates well-formatted code 90% of the time, and the hook handles the remaining 10% to prevent CI formatting failures.

**Connection to Chapter Concepts:**

- **Lesson 15 (Hooks)**: You learned the PostToolUse pattern. This is a production example that prevents a common frustration.

---

## Permissions, Not Skip Permissions

Boris explicitly avoids `--dangerously-skip-permissions`. Instead, he uses `/permissions` to pre-allow commands that are safe in his environment:

- `bun run build:*`
- `bun run test:*`
- `bun run typecheck:*`

These permissions are checked into `.claude/settings.json` and shared with the entire team.

**Why this matters**: Skip permissions trades safety for convenience. Pre-allowed permissions give you the convenience while maintaining the safety boundary—Claude still asks before running unknown commands.

**Connection to Chapter Concepts:**

- **Lesson 14 (Settings Hierarchy)**: Team-shared settings in `.claude/settings.json` ensure consistency across team members.

---

## Autonomous Problem Solving

The Claude Code team has developed patterns for letting Claude solve problems independently:

**The core pattern**: Give Claude the problem, not the solution. It often finds better approaches when it has freedom to investigate.

| If you're a...       | Example                                                                                  |
| -------------------- | ---------------------------------------------------------------------------------------- |
| **Developer**        | Paste a Slack bug thread and say "fix." Or: "Go fix the failing CI tests."               |
| **Knowledge worker** | Paste a confusing email thread and say "draft a response that resolves this."            |
| **Researcher**       | "Here are my notes from 5 sources. Find the contradictions and synthesize the truth."    |
| **Manager**          | "Here's feedback from 3 stakeholders. Create a plan that addresses everyone's concerns." |

**Don't micromanage**: Instead of prescribing exact steps, describe the outcome you want. Claude often finds better solutions than you would have specified.

**Connect to your data**: Enable MCP integrations (Slack, Google Drive, Notion) so Claude can pull context directly. Zero context switching—Claude reads the source material, investigates, and produces the solution.

---

## Level Up Your Prompting

Beyond the basics, the Claude Code team uses specific prompting techniques that work across domains:

**Challenge Claude to verify your work**:

| Domain         | Challenge Prompt                                                           |
| -------------- | -------------------------------------------------------------------------- |
| **Developer**  | "Grill me on these changes and don't merge until I pass your test."        |
| **Writer**     | "Challenge every claim in this draft. What's unsupported? What's unclear?" |
| **Strategist** | "Poke holes in this plan. What am I missing? What could go wrong?"         |
| **Analyst**    | "Prove to me this conclusion is correct. Show me the logic chain."         |

**Escape mediocre solutions**: After a mediocre result, say: "Knowing everything you know now, scrap this and create the elegant solution." This prompt leverages Claude's accumulated context to find better approaches it wouldn't have seen initially.

**Reduce ambiguity**: Write detailed briefs before handing work off. The more specific you are about constraints, audience, and success criteria, the better the output. Vague requests produce vague results.

---

## Workspace & Environment Setup

The Claude Code team has refined their environment for optimal Claude usage. These principles apply whether you're in a terminal or browser:

**Status visibility**: Use `/statusline` to always show context usage. Know at a glance how much context you've consumed—this helps you decide when to `/clear` or start fresh.

**Visual organization**:

| If you're a...       | Organization Approach                                                          |
| -------------------- | ------------------------------------------------------------------------------ |
| **Developer**        | Color-code terminal tabs (tmux), one tab per worktree. Team recommends Ghostty |
| **Knowledge worker** | Color-code browser tabs or windows, one per project/client                     |
| **Anyone**           | Name your sessions descriptively (`/rename`) so you can find them later        |

**Voice dictation**: Use voice input (hit fn twice on macOS, or use your platform's dictation). You speak 3x faster than you type, and your prompts get way more detailed as a result. More detail = better output. This works in any Claude interface.

---

## Research & Data Analysis

Claude Code can become your research and analysis interface—you describe what you want to know, Claude figures out how to get it:

| If you're a...       | How Claude helps                                                         |
| -------------------- | ------------------------------------------------------------------------ |
| **Developer**        | Query databases via CLI (BigQuery, Postgres)—no SQL needed               |
| **Analyst**          | Pull metrics, generate reports, create visualizations from raw data      |
| **Researcher**       | Search across documents, synthesize findings, identify patterns          |
| **Knowledge worker** | Query your connected tools (Google Drive, Notion, Slack) for information |

> "Personally, I haven't written a line of SQL in 6+ months."
>
> — Boris Cherny

**The pattern**: If there's a way to access your data (CLI, MCP, API, or even files), Claude can query it for you. Build a skill that knows how to access your data sources, and analytics becomes conversational.

---

## Model Selection: Opus 4.5 with Thinking

> "I use Opus 4.5 with thinking for everything. It's the best coding model I've ever used, and even though it's bigger & slower than Sonnet, since you have to steer it less and it's better at tool use, it is almost always faster than using a smaller model in the end."
>
> — Boris Cherny

**The Counterintuitive Insight**: A "wrong fast answer" costs more time than a "right slow answer." Opus 4.5 requires less correction and iteration, making total task completion faster despite slower per-response times.

---

## Session Management: Course-Correct and Recover

The official best practices emphasize aggressive session management. Claude Code's conversations are persistent and reversible—use this to your advantage.

**Course-Correct Early:**

- **`Esc`**: Stop Claude mid-action. Context is preserved, so you can redirect.
- **`Esc + Esc` or `/rewind`**: Opens the rewind menu to restore previous conversation and code state.
- **`/clear`**: Reset context between unrelated tasks. Long sessions with irrelevant context reduce performance.

**Resume Conversations:**

```bash
claude --continue    # Resume the most recent conversation
claude --resume      # Select from recent conversations
```

Use `/rename` to give sessions descriptive names (`"oauth-migration"`, `"debugging-memory-leak"`) so you can find them later. Treat sessions like branches—different workstreams can have separate, persistent contexts.

**When to Clear**: If you've corrected Claude more than twice on the same issue, the context is cluttered with failed approaches. Run `/clear` and start fresh with a more specific prompt that incorporates what you learned.

**When to Abandon**: Boris notes that 10-20% of his sessions are abandoned when they hit unexpected scenarios. This is normal. Sometimes starting fresh is faster than recovering a confused session.

---

## Using Claude Code for Learning

The Claude Code team recommends a specific configuration for anyone who wants to learn as they work:

> "Enable the 'Explanatory' or 'Learning' output style in /config to have Claude explain the _why_ behind its changes."
>
> — Boris Cherny

**Enable Learning Mode:**

Run `/config` and set the output style to "Explanatory" or "Learning". Now Claude doesn't just make changes—it teaches you what it's doing and why.

**Before (default mode):**

```
I'll update the authentication middleware to use JWT.
[makes changes]
Done.
```

**After (learning mode):**

```
I'll update the authentication middleware to use JWT.

WHY: The current session-based auth doesn't scale across multiple servers
because sessions are stored in memory. JWTs are stateless—the token itself
contains the user info, signed cryptographically.

HOW: I'm adding a verifyJWT middleware that:
1. Extracts the token from the Authorization header
2. Verifies the signature using our secret key
3. Attaches the decoded user to req.user

[makes changes with inline explanations]
```

**Generate Visual HTML Presentations:**

For onboarding or understanding unfamiliar code:

```
Generate a visual HTML presentation explaining the authentication system
in this codebase. Include:
- Diagrams showing the login → token → refresh flow
- Code snippets for key functions
- Common gotchas newcomers encounter

Make it standalone (all CSS inline) so I can open it in a browser.
```

Claude creates an interactive HTML file you can share with teammates or reference later. Perfect for:

- Onboarding new team members
- Documenting complex processes or systems
- Creating training materials
- Understanding work you inherited from others

**ASCII diagrams for quick understanding**: Ask Claude to draw ASCII diagrams of new protocols and codebases. Sometimes a quick text diagram is faster than generating HTML—great for understanding data flows, state machines, or API relationships.

**Spaced-repetition learning skill**: Build a skill where you explain your understanding, Claude asks follow-up questions to fill gaps, and stores the result. This creates active recall practice that deepens learning over time.

---

## Mapping the Complete Workflow

Here's how these techniques map to what you've learned:

| Practice                    | Source      | Chapter Lesson | Your Takeaway                                                |
| --------------------------- | ----------- | -------------- | ------------------------------------------------------------ |
| Context window constraint   | Official    | All            | The fundamental "why" behind every practice                  |
| Parallel sessions (3-5)     | Team        | L01 + L11      | Isolate sessions for true parallelism                        |
| Workspace shortcuts         | Team        | Workspace      | Quick switching between workstreams (aliases, tabs)          |
| Claude-reviews-Claude       | Team        | L11            | Fresh context catches blind spots                            |
| Plan Mode first             | Team + Docs | L11            | Always plan before executing non-trivial tasks               |
| Re-plan when stuck          | Team        | L11            | Switch back to Plan Mode when things go sideways             |
| CLAUDE.md self-writing      | Team        | L05            | "Update your CLAUDE.md so you don't make that mistake again" |
| Notes directory pattern     | Team        | L05            | Maintain task notes, point CLAUDE.md at them                 |
| Session-end review          | Team        | L08-09         | Capture insights while context is fresh                      |
| Skills across projects      | Team        | L08-09         | Build a portable skill portfolio                             |
| Context dump skill          | Team        | L08-09         | Sync communications/docs into one context                    |
| Subagents for investigation | Official    | L11            | Keep main context clean; explore in isolation                |
| "use subagents" directive   | Team        | L11            | Append to throw more compute at problems                     |
| Autonomous problem solving  | Team        | MCP + L11      | Give Claude the problem, not the solution                    |
| Challenge prompts           | Team        | Prompting      | "Grill me" and "Poke holes in this plan"                     |
| Elegant solution prompt     | Team        | Prompting      | "Knowing everything you know now, scrap and redo"            |
| Verification loops          | Team + Docs | L12 + L15      | Give Claude tools to verify its own work                     |
| Learning output style       | Team        | /config        | Have Claude explain the _why_ behind changes                 |
| Visual presentations        | Team        | Learning       | HTML onboarding for unfamiliar material                      |
| ASCII diagrams              | Team        | Learning       | Quick text diagrams for flows and relationships              |
| Voice dictation             | Team        | Workspace      | Speak 3x faster than typing—more detail = better output      |
| `/statusline` config        | Team        | Workspace      | Always show context usage at a glance                        |
| Conversational research     | Team        | MCP            | Query data sources through natural language                  |
| PostToolUse hooks           | Team        | L15            | Automate consistent formatting or checks                     |
| `/permissions` over skip    | Team        | L14            | Pre-allow safe operations, share with team                   |
| `/clear` between tasks      | Official    | Session mgmt   | Reset context for fresh starts                               |
| `/rewind` for recovery      | Official    | Session mgmt   | Checkpoints are reversible—experiment freely                 |
| 10-20% session abandonment  | Team        | Session mgmt   | Some sessions fail—that's normal                             |
| Opus 4.5 choice             | Team        | L14            | Optimize for total iteration time, not speed                 |

---

## Common Failure Patterns (What to Avoid)

The official documentation catalogs failure patterns observed across many users. Recognizing these early saves time:

| Pattern                      | Symptom                                                                    | Fix                                                                    |
| ---------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Kitchen sink session**     | Started with one task, asked unrelated questions, now context is cluttered | `/clear` between unrelated tasks                                       |
| **Correction spiral**        | Corrected Claude twice, still wrong, correcting again                      | After 2 failed corrections, `/clear` and rewrite the initial prompt    |
| **Over-specified CLAUDE.md** | Claude ignores instructions; important rules get lost                      | Ruthlessly prune. If Claude already does it correctly, delete the rule |
| **Trust-then-verify gap**    | Plausible-looking output that doesn't handle edge cases                    | Always provide verification methods                                    |
| **Infinite exploration**     | Asked Claude to "investigate" without scoping; context fills with reads    | Scope investigations narrowly or use subagents                         |

**Meta-pattern**: Most failures stem from context pollution—either too much irrelevant information, or failed approaches cluttering the conversation. When in doubt, start fresh.

---

## Operational Takeaways

Looking at Boris's workflow and the official best practices, five principles emerge:

**1. Context is the Constraint**

Every technique traces back to managing the context window. Worktrees, subagents for investigation, `/clear` between tasks, Plan Mode—all prevent context pollution. Internalize this and the "why" behind every practice becomes clear.

**2. Parallelization Over Optimization**

Multiple simple sessions outperform one overloaded session. Don't try to make one conversation do everything—distribute work across parallel Claude instances using worktrees.

**3. Plan Mode Discipline**

Planning isn't training wheels. It's the foundation. Boris uses it for every non-trivial task, not just when he's unsure. The investment in alignment pays off in execution quality.

**4. Self-Evolving Documentation**

CLAUDE.md isn't static. It grows with every correction. The magic phrase—"Update your CLAUDE.md so you don't make that mistake again"—turns every mistake into institutional memory.

**5. Verification Infrastructure**

Quality comes from feedback loops, not hope. Give Claude ways to check its work—through MCP tools, hooks, subagents, or browser automation. Verification creates the iteration loop that produces excellent results.

---

## Try With AI

Apply what you've learned from the creator's workflow:

**🔧 Set Up Parallel Sessions:**

```
I want to try running parallel Claude sessions. Help me understand:
1. How to set up 3 separate sessions for different workstreams
2. How to name/organize them based on [describe your current tasks]
3. Best practices for managing multiple sessions without confusion
```

**What you're learning:** The setup that enables the parallelization Boris calls "the single biggest productivity unlock."

**🎯 Try Claude-Reviews-Claude:**

```
I need to [describe a task]. Let's use the Claude-reviews-Claude pattern:
1. First, create a detailed plan for this work
2. Then I'll open a second session to review it critically
3. Finally, we'll incorporate the feedback
```

**What you're learning:** Two-pass verification that catches blind spots. This is how the Claude Code team ensures plans are solid before execution.

**✍️ Practice Self-Writing Rules:**

```
I'm going to intentionally make a common mistake in my work. After you
correct me, I'll ask you to update CLAUDE.md. Let's start—what's a common
mistake people make when working on [your domain]?
```

**What you're learning:** The feedback loop that makes Claude smarter over time. Each correction becomes a permanent rule.

**📋 Create Your Session-End Review Skill:**

```
Help me create a session-end review skill for my work. I want it to:
- Summarize what we accomplished
- Identify any open questions
- List follow-up tasks
- Note insights worth capturing in CLAUDE.md

Create it in .claude/skills/session-review/SKILL.md with disable-model-invocation: true
so I invoke it manually at the end of each session.
```

**What you're learning:** Session hygiene habits that compound over time. Running this before closing any session captures value that would otherwise be lost.

**🔍 Enable Learning Mode:**

```
I want to understand things better as I work. Help me:
1. Configure Claude Code for 'Explanatory' output style
2. Show me the difference in output for a sample task
3. Create an HTML presentation explaining [a topic you're learning]
```

**What you're learning:** How to use Claude Code for learning, not just doing—perfect for onboarding and understanding unfamiliar material.

**🔍 Analyze Your Current Practice:**

```
Compare my current Claude Code workflow to the best practices in this lesson.
I've been using [describe your typical usage pattern]. What's the biggest gap?
Which technique would have the most impact if I adopted it?
```

**What you're learning:** Self-assessment against expert practice—identifying your highest-leverage improvement opportunity.
