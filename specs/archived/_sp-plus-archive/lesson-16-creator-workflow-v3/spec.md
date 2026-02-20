# Lesson 16 Revision Spec: The Creator's Workflow v3.0

## Overview

**Current State**: Lesson 16 covers Boris's workflow from January 2026 thread plus official best practices.

**Change Request**: Incorporate February 2026 thread with new tips, particularly:

- Git worktrees (team preference)
- Claude-reviews-Claude pattern
- CLAUDE.md self-writing technique
- /techdebt slash command
- Learning mode configuration (/config output styles)
- HTML presentations for onboarding

## Sources Synthesized

| Source                                                                                      | Date        | Key Additions                                                                  |
| ------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------ |
| [Boris X thread #1](https://x.com/bcherny/status/2007179832300581177)                       | Jan 2026    | Original workflow: 15-20 sessions, CLAUDE.md, Plan Mode, Opus 4.5              |
| Boris X thread #2 (user-provided)                                                           | Feb 1, 2026 | Worktrees, Claude-reviews-Claude, self-writing rules, /techdebt, Learning mode |
| [Official Best Practices](https://code.claude.com/docs/en/best-practices)                   | Current     | Context window framing, verification, interview pattern                        |
| [Substack analysis](https://karozieminski.substack.com/p/boris-cherny-claude-code-workflow) | Jan 2026    | 9-point framework, philosophical shifts                                        |
| [InfoQ coverage](https://www.infoq.com/news/2026/01/claude-code-creator-workflow/)          | Jan 2026    | /commit-push-pr command, teleport, session abandonment                         |

## Content Structure (Revised)

### 1. Opening Hook (Keep)

- Boris thread went viral
- Features combine into production workflow

### 2. The Fundamental Constraint: Context Window (Keep, Enhance)

- Add: How each new tip manages context

### 3. Parallel Sessions with Git Worktrees (NEW SECTION)

- **What changed**: Original lesson mentioned "parallel sessions" generically
- **New content**:
  - Team prefers git worktrees over checkouts
  - Setup: `git worktree add ../feature-branch feature-branch`
  - Each worktree = isolated Claude session
  - Boris personally uses checkouts, team uses worktrees (both valid)
  - Practical: Start with 3 worktrees before scaling to 5+

### 4. Plan Mode First (Enhance)

- **Keep**: Core Plan Mode discipline
- **Add**: The "Claude Reviews Claude" Pattern
  - One Claude writes the plan
  - Spin up second Claude to review as "staff engineer"
  - Fresh context catches blind spots
  - Example prompt for reviewer

### 5. CLAUDE.md as Team Infrastructure (Enhance)

- **Keep**: Team CLAUDE.md, @.claude tagging
- **Add**: Self-Writing Technique
  - After correction: "Update your CLAUDE.md so you don't make that mistake again"
  - Why it works: Claude understands the context better than human description
  - Example flow with specific rule output

### 6. Skills and Commands for Workflow Automation (NEW SECTION)

- **Content**:
  - If you do something more than once a day → skill or command
  - /techdebt command: Find duplicated code at session end
  - /commit-push-pr: Pre-compute git status
  - Skills committed to git, reused across projects
  - Building a skill portfolio

### 7. Specialized Subagents (Keep, Enhance)

- **Keep**: code-simplifier, verify-app, build-validator
- **Add**: Investigation pattern for keeping context clean

### 8. Verification is Everything (Keep)

- Already well-covered

### 9. PostToolUse Hooks (Keep)

- Already well-covered

### 10. Permissions Management (Keep)

- Already well-covered

### 11. Model Selection (Keep)

- Already well-covered

### 12. Session Management (Enhance)

- **Keep**: /clear, /rewind, --continue, --resume
- **Add**: When to abandon (10-20% abandoned sessions is normal)

### 13. Learning Mode (NEW SECTION - FROM FEB THREAD)

- **Content**:
  - Enable "Explanatory" or "Learning" output style in /config
  - Claude explains the _why_ behind changes
  - Generate visual HTML presentations for onboarding
  - Example prompt for HTML presentation
  - Perfect for understanding unfamiliar codebases

### 14. Mapping Table (Update)

- Add new practices with sources

### 15. Common Failure Patterns (Keep)

- Already comprehensive

### 16. Operational Takeaways (Update)

- Revise to include new principles

### 17. Try With AI (Update)

- Add prompts for:
  - Setting up worktrees
  - Using Learning mode
  - Creating /techdebt command
  - Claude-reviews-Claude workflow

## New Sections Detail

### Git Worktrees Section

```markdown
## Setting Up Parallel Sessions with Git Worktrees

The January thread mentioned 15-20 sessions. The February update revealed _how_:

> "Spin up 3–5 git worktrees at once, each running its own Claude session in parallel.
> It's the single biggest productivity unlock, and the top tip from the team."
>
> — Boris Cherny, X (February 2026)

**What are worktrees?** Git worktrees let you have multiple working directories pointing
to the same repository. Each gets its own files, its own changes, and its own Claude session.

**Quick setup:**

\`\`\`bash

# Create worktrees for different workstreams

git worktree add ../auth-feature feature/auth
git worktree add ../bugfix-api bugfix/api-error
git worktree add ../experiment main

# Each worktree is a separate directory

cd ../auth-feature && claude # Session 1
cd ../bugfix-api && claude # Session 2 (new terminal)
cd ../experiment && claude # Session 3 (new terminal)
\`\`\`

**Why worktrees over branches?**

- Branches require switching (losing Claude context)
- Worktrees are parallel directories (isolated contexts)
- Changes don't conflict until you merge

**Boris's personal preference:** He uses multiple git checkouts instead of worktrees.
Both approaches work—worktrees are lighter-weight, checkouts are simpler mentally.

**Start small:** Begin with 3 worktrees before scaling to 5+. The cognitive overhead
of managing many sessions takes practice.
```

### Claude-Reviews-Claude Section

```markdown
## The Staff Engineer Review Pattern

From the February thread:

> "One person has one Claude write the plan, then they spin up a second Claude
> to review it as a staff engineer."
>
> — Boris Cherny, X (February 2026)

**The workflow:**

1. **Session A (Writer)**: Create the implementation plan
```

I need to add rate limiting to our API. Use Plan Mode.
Research our existing middleware patterns and create a detailed plan.

```

2. **Session B (Reviewer)**: Review with fresh eyes
```

You are a staff engineer reviewing this implementation plan.
Look for: edge cases, security issues, missing error handling,
architectural concerns, and things the author might have missed.

Here's the plan:
[paste plan from Session A]

```

3. **Session A**: Address feedback
```

Here's the review feedback: [Session B output].
Update the plan to address these issues.

```

**Why this works:**
- Fresh context catches blind spots
- Different "persona" surfaces different concerns
- Two-pass verification before any code is written
- Prevents sunk-cost fallacy (harder to catch flaws in your own plan)
```

### Self-Writing CLAUDE.md Section

````markdown
## Let Claude Write Its Own Rules

The most actionable tip from the February thread:

> "After every correction, end with: 'Update your CLAUDE.md so you don't make
> that mistake again.' Claude is eerily good at writing rules for itself."
>
> — Boris Cherny, X (February 2026)

**Example flow:**

1. Claude generates code with wrong import path:
   ```typescript
   import { auth } from "utils/auth"; // Wrong
   ```
````

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

**The compound effect:** Every correction makes Claude smarter. Over weeks,
your CLAUDE.md becomes a knowledge base that prevents entire categories of mistakes.

````

### /techdebt Command Section

```markdown
## Session Hygiene: The /techdebt Command

From the February thread:

> "Build a /techdebt slash command and run it at the end of every session
> to find and kill duplicated code."
>
> — Boris Cherny, X (February 2026)

**Create the command:**

\`\`\`markdown
# .claude/commands/techdebt.md

Find and report technical debt in files modified during this session:

1. Check git status to identify modified files
2. For each modified file, look for:
   - Duplicated code that could be extracted
   - Dead code (unreachable, unused)
   - TODO comments older than 1 week
   - Functions longer than 50 lines
   - Magic numbers without constants
3. Prioritize by impact (most duplicated → highest priority)
4. Suggest specific refactors with code examples

Output as a checklist I can work through.
\`\`\`

**The habit:** Before closing any session, run `/techdebt`. The context is fresh—
Claude knows exactly what you built and can spot cleanup opportunities you missed.

**Other session-end commands to consider:**
- `/commit-push-pr` — Pre-compute git status, create clean commits
- `/test-coverage` — Identify untested code paths
- `/security-check` — Scan for common vulnerabilities
````

### Learning Mode Section

```markdown
## Using Claude Code for Learning

From the February thread (tip #10):

> "Enable the 'Explanatory' or 'Learning' output style in /config to have
> Claude explain the _why_ behind its changes."
>
> — Boris Cherny, X (February 2026)

**Enable Learning Mode:**

Run `/config` and set the output style to "Explanatory" or "Learning".
Now Claude doesn't just make changes—it teaches you what it's doing and why.

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
- Common gotchas new developers encounter

Make it standalone (all CSS inline) so I can open it in a browser.

```

Claude creates an interactive HTML file you can share with teammates or
reference later. Perfect for:
- Onboarding new developers
- Documenting complex systems
- Creating training materials
- Understanding code you inherited
```

## Updated Mapping Table

```markdown
| Practice                    | Source           | Chapter Lesson | Your Takeaway                                                |
| --------------------------- | ---------------- | -------------- | ------------------------------------------------------------ |
| Context window constraint   | Official         | All            | The fundamental "why" behind every practice                  |
| Git worktrees (3-5)         | Boris Feb        | L01 + L09      | Isolate sessions for true parallelism                        |
| 15-20 parallel sessions     | Boris Jan        | L01 + L09      | Think of Claude as capacity to schedule                      |
| Claude-reviews-Claude       | Boris Feb        | L09            | Fresh context catches blind spots                            |
| Plan Mode first             | Boris + Official | L09            | Always plan before executing non-trivial tasks               |
| CLAUDE.md self-writing      | Boris Feb        | L05            | "Update your CLAUDE.md so you don't make that mistake again" |
| Team CLAUDE.md in git       | Boris Jan        | L05            | Every mistake becomes a rule; context evolves                |
| /techdebt at session end    | Boris Feb        | Commands       | Find and kill duplicated code regularly                      |
| Skills across projects      | Boris Feb        | L07-08         | Build a portable skill portfolio                             |
| Subagents for investigation | Official         | L09            | Keep main context clean; explore in isolation                |
| Specialized subagents       | Boris Jan        | L09            | Create subagents for repeated PR workflows                   |
| Verification loops          | Boris + Official | L10 + L13      | Give Claude tools to verify its own work                     |
| Learning output style       | Boris Feb        | /config        | Have Claude explain the _why_ behind changes                 |
| HTML presentations          | Boris Feb        | Learning       | Visual onboarding for unfamiliar code                        |
| PostToolUse formatting      | Boris Jan        | L13            | Automate the last 10% that causes CI failures                |
| /permissions over skip      | Boris Jan        | L13            | Pre-allow safe commands, share with team                     |
| /clear between tasks        | Official         | Session mgmt   | Reset context for fresh starts                               |
| /rewind for recovery        | Official         | Session mgmt   | Checkpoints are reversible—experiment freely                 |
| 10-20% session abandonment  | Boris Jan        | Session mgmt   | Some sessions fail—that's normal                             |
| Opus 4.5 choice             | Boris Jan        | L13            | Optimize for total iteration time, not speed                 |
```

## Updated Try With AI Section

```markdown
## Try With AI

**🔧 Set Up Git Worktrees:**

> "I want to try parallel Claude sessions with git worktrees. Help me:
>
> 1. Create 3 worktrees for my current project
> 2. Name them appropriately for [describe your current tasks]
> 3. Explain how to manage them without conflicts"

**What you're learning:** The mechanical setup that enables the parallelization
Boris calls "the single biggest productivity unlock."

**🔍 Enable Learning Mode:**

> "I want to understand code better as I work. Help me:
>
> 1. Configure Claude Code for 'Explanatory' output style
> 2. Show me the difference in output for a sample task
> 3. Create an HTML presentation explaining [a system in your codebase]"

**What you're learning:** How to use Claude Code for learning, not just doing—
the feature Boris says is perfect for onboarding and understanding unfamiliar code.

**📋 Create Your /techdebt Command:**

> "Help me create a /techdebt slash command for my project. I want it to:
>
> - Check files I modified today
> - Find duplicated code
> - Identify functions that are too long
> - Output a prioritized cleanup checklist"

**What you're learning:** Session hygiene habits that compound over time.
Running this daily prevents technical debt from accumulating.

**🎯 Try Claude-Reviews-Claude:**

> "I need to [describe a task]. Let's use the Claude-reviews-Claude pattern:
>
> 1. First, create a detailed implementation plan
> 2. Then I'll open a second session to review it as a staff engineer
> 3. Finally, we'll incorporate the feedback"

**What you're learning:** Two-pass verification that catches blind spots.
This is how Boris's team ensures plans are solid before execution.

**✍️ Practice Self-Writing Rules:**

> "I'm going to intentionally make a common mistake in my project. After you
> correct me, I'll ask you to update CLAUDE.md. Let's start—what's a common
> mistake developers make in [your tech stack]?"

**What you're learning:** The feedback loop that makes Claude smarter over time.
Each correction becomes a permanent rule.
```

## Success Criteria

1. **Completeness**: All 10 tips from Feb thread incorporated
2. **Practical**: Every new section has runnable commands/prompts
3. **Connected**: New content maps to existing chapter lessons
4. **Balanced**: New content doesn't overwhelm existing solid foundation
5. **Testable**: Try With AI prompts let students verify they understood

## Implementation Notes

- Keep existing solid sections (verification, hooks, permissions, model selection)
- Add new sections without bloating (target +2000 words, not +5000)
- Maintain voice: practical, expert-to-expert, no fluff
- Update metadata: version to 3.0.0, add refinement notes
