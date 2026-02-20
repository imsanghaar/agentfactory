---
slug: /General-Agents-Foundations/general-agents/ralph-wiggum-loop
title: "Ralph Wiggum Loop: Autonomous Iteration Workflows"
sidebar_position: 17
chapter: 3
lesson: 17
duration_minutes: 15

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 2"
layer_progression: "L2 (AI Collaboration)"
layer_1_foundation: "N/A"
layer_2_collaboration: "AI suggests loop candidates based on workflow, Student evaluates fit against decision framework, convergence on appropriate automation scope"
layer_3_intelligence: "N/A (autonomous iteration pattern introduced here, formalized as intelligence layer in advanced content)"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Recognizing Autonomous Iteration Opportunities"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can analyze workflows to identify tasks with 10+ iterations and clear completion criteria, distinguishing good Ralph Loop candidates from poor fits"

  - name: "Installing and Configuring Claude Code Plugins"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Tool Proficiency"
    measurable_at_this_level: "Student can install Ralph Wiggum plugin from marketplace and verify installation with command-line tools"

  - name: "Designing Completion Criteria for Autonomous Systems"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Create"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can formulate objective, verifiable completion promises for autonomous iteration tasks"

  - name: "Implementing Safety Guardrails for AI Automation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Safety"
    measurable_at_this_level: "Student can set appropriate max-iterations limits, use version control checkpoints, and monitor cost/progress during autonomous loops"

  - name: "Understanding Stop Hook Architecture"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Understand"
    digcomp_area: "Technical Knowledge"
    measurable_at_this_level: "Student can explain how Stop hooks intercept Claude's exit to reinject continuation prompts and create autonomous iteration loops"

learning_objectives:
  - objective: "Identify workflows where manual iteration creates overhead (10+ iterations, clear success signals)"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Analysis of personal workflow to find Ralph Loop candidates using decision framework"

  - objective: "Install Ralph Wiggum plugin from marketplace"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successful plugin installation and command verification"

  - objective: "Design effective completion promises for autonomous tasks"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Creation of objective, specific, terminal completion criteria for a real task"

  - objective: "Configure safety parameters (max-iterations, version control, monitoring)"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Setting appropriate guardrails based on task complexity and cost tolerance"

  - objective: "Understand Stop hook mechanics at moderate technical depth"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Explanation of how Stop hooks enable autonomous iteration through prompt reinjection"

# Cognitive load tracking
cognitive_load:
  new_concepts: 8
  assessment: "8 concepts (autonomous iteration, Stop hook, completion promise, max-iterations, iteration-heavy workflows, cost management, Ralph Loop plugin, safety guardrails) - within B1 limit of 10 ✓"

# Differentiation guidance
differentiation:
  extension_for_advanced: "Create custom Stop hooks for project-specific workflows; design multi-stage Ralph Loops with conditional completion promises; implement cost tracking and reporting"
  remedial_for_struggling: "Start with simple single-command loops (e.g., linting) before complex multi-step tasks; use lower max-iterations (10-15) initially; focus on conceptual understanding before hands-on implementation"

# Generation metadata
generated_by: "Claude Sonnet 4.5"
source_spec: "Ralph Wiggum Loop lesson plan"
created: "2026-01-12"
last_modified: "2026-01-12"
git_author: "Claude Code"
workflow: "direct implementation"
version: "1.0.0"

teaching_guide:
  lesson_type: "core"
  session_group: 6
  session_title: "Autonomous Workflows, Creator Practices, and Exercises"
  key_points:
    - "Ralph Loop uses the Stop hook to intercept Claude's exit and reinject a continuation prompt — this is NOT a new concept but a specific application of hooks from Lesson 15"
    - "The completion promise is static and uses exact string matching — it cannot be changed mid-loop, which is why the embedded <promise> pattern is recommended for reliability"
    - "Max-iterations is the primary safety net, not the completion promise — students must always set a limit to prevent runaway cost"
    - "Good Ralph Loop candidates have 10+ expected iterations, objective verification (tests pass, build succeeds), and deterministic completion signals"
  misconceptions:
    - "Students think Ralph Loop is AI making decisions about when to stop — actually it is a mechanical string-match check on Claude's output against a static completion promise"
    - "Students assume any task benefits from autonomous iteration — tasks requiring human judgment, creative work, or multi-goal optimization are poor fits"
    - "Students underestimate cost: a 30-iteration loop can cost $30-60 in API credits, and overnight runs can exceed $100"
    - "Students believe they can modify the completion promise during a loop — it is set once at the initial /ralph-loop command and cannot be changed"
  discussion_prompts:
    - "Think of a task you did recently that required copying errors back to Claude multiple times. Would Ralph Loop have been appropriate? Apply the decision table criteria."
    - "What is the difference between automation that is safe to leave unattended and automation that requires periodic monitoring? Where does Ralph Loop fall?"
    - "If a loop is stuck repeating the same 3 errors, what does that tell you about the task design versus Claude's capability?"
  teaching_tips:
    - "Walk through the Stop hook flow diagram step by step — trace the linting example from '47 problems' to '0 problems' showing each intercept point"
    - "Have students write completion promises for 3 different scenarios BEFORE showing the examples — then compare their promises against the good/poor examples in the lesson"
    - "Emphasize the cost table early: show students that a complex 80-iteration refactor can cost $80-150 before they get excited about running overnight loops"
    - "Use the Decision Table (Good Fit vs Poor Fit) as a classification exercise: give students 5 tasks and have them categorize each with justification"
  assessment_quick_check:
    - "What two conditions cause a Ralph Loop to stop iterating?"
    - "Write a completion promise for 'fix all TypeScript errors in the project' — is yours objective, specific, and terminal?"
    - "Why is --max-iterations the primary safety net rather than the completion promise?"

# Legacy compatibility
prerequisites:
  - "Lessons 01-16: Complete Claude Code features (hooks, plugins, settings, subagents)"
  - "Understanding of event-driven automation from Lesson 15"
  - "Plugin installation from Lesson 16"
---

# Ralph Wiggum Loop: Autonomous Iteration Workflows

You're cleaning up code quality issues in a project you inherited. Your linter flags 47 problems. The workflow looks like this:

1. You ask Claude to fix the linting errors
2. Claude fixes 5 files
3. You run the linter: 32 problems remaining
4. You copy the error output and paste it back to Claude
5. Claude fixes 4 more files
6. You run the linter again: 18 problems remaining
7. You copy the new errors
8. Claude fixes them
9. You run the linter: 7 problems remaining
10. Repeat this cycle 6 more times

After 30 minutes, you're frustrated. Not because Claude can't fix the errors—it can. But because you've become a **manual feedback loop operator**, running commands, copying output, and waiting for Claude to respond.

**The question**: What if Claude could run the linter, see the errors, fix them, verify the fixes worked, and continue until all 47 problems are resolved—while you go get coffee?

**That's what Ralph Wiggum Loop solves.**

---

## The Iteration Fatigue Problem

**Manual iteration overhead** has three hidden costs:

1. **Waiting time**: You sit idle while Claude processes each response
2. **Context switching**: Each iteration breaks your flow as you check output, copy errors, paste back
3. **Error transcription**: Manually copying output introduces typos and missed details

**Common iteration-heavy workflows** where this pain appears:

- Framework upgrades (React v16→v19, Next.js 14→15)
- Test-driven refactoring (failing tests → fix → repeat)
- Build error resolution (compilation, linting, type checking)
- Deployment debugging (staging environment issues)
- Migration projects (database schema changes, API updates)

These aren't edge cases—they're everyday workflows. Every developer faces iteration-heavy tasks weekly.

### When Manual Iteration Becomes a Bottleneck

| Scenario            | Iteration Count   | Manual Cost           | Automation Value    |
| ------------------- | ----------------- | --------------------- | ------------------- |
| Simple bug fix      | 1-3 iterations    | Low (5-10 min)        | Not worth it        |
| Feature development | 5-10 iterations   | Medium (30-60 min)    | Maybe worth it      |
| Framework upgrade   | 15-50 iterations  | High (2-4 hours)      | Definitely worth it |
| Large refactor      | 20-100 iterations | Very high (4-8 hours) | Critical            |

**Rule of thumb**: If you expect more than 10 iterations, Ralph Loop saves time.

---

## What is Ralph Wiggum Loop?

**Definition**: Ralph Wiggum Loop is a Claude Code plugin that enables **autonomous iteration**—Claude Code runs a task, checks the result, identifies what needs fixing, makes corrections, and repeats until a completion condition is met, all without your intervention.

**Named after**: The Simpsons character Ralph Wiggum, known for cheerful persistence despite mistakes. The plugin embodies "try, fail, learn, repeat"—exactly what autonomous iteration requires.

### Architecture: How It Works

Ralph Loop uses the **Stop hook** (from Lesson 15) to intercept Claude Code's normal exit behavior:

1. **Normal flow**: You ask Claude to do something → Claude completes → Session ends
2. **Ralph Loop flow**: You ask Claude to do something → Claude completes → Stop hook triggers → Reinjects prompt asking "Did it work? If not, fix and continue" → Claude continues → Repeat until completion criteria met

**Key Components**:

| Component              | Purpose                                                    |
| ---------------------- | ---------------------------------------------------------- |
| **Stop Hook**          | Intercepts Claude's exit to reinject continuation prompts  |
| **Completion Promise** | Text that signals "we're done" (e.g., "All tests passing") |
| **Max Iterations**     | Safety limit preventing infinite loops                     |
| **Loop Prompt**        | Template asking Claude to verify results and continue      |

### Real-World Origin

Created by Geoffrey Huntley in summer 2025, formalized by Boris Cherny (Anthropic Head of Claude Code) in late 2025. Real production usage includes:

- 14-hour autonomous upgrade sessions
- React v16→v19 framework migrations
- Multi-repository refactoring campaigns
- Infrastructure-as-code deployments

**Why "plugin" not "built-in"**: Autonomous iteration carries cost and control risks. Making it a plugin ensures users opt in deliberately, not accidentally.

---

## How Stop Hooks Work

You learned about four hook events in Lesson 15:

- **PreToolUse**: Before Claude runs a tool
- **PostToolUse**: After Claude completes a tool
- **SessionStart**: When session begins
- **SessionEnd**: When session closes

**Stop Hook** is a special hook that fires when Claude is about to exit (stop working).

### Normal Claude Code Flow

```
User: "Fix the authentication bug"
  ↓
Claude: [reads code, analyzes, edits files, runs tests]
  ↓
Claude: "Bug fixed. Tests passing. I'm done."
  ↓
Session: [STOP - waiting for user input]
```

### Ralph Loop Flow with Stop Hook

```
User: "/ralph-loop 'Fix all linting errors' --max-iterations 20 --completion-promise '0 problems'"
  ↓
Claude: [runs linter, fixes first batch of errors]
  ↓
Claude: "Fixed 5 files. 32 problems remaining. I'm done."
  ↓
Stop Hook: [INTERCEPTS] "Wait—did you see '0 problems'? No? Then continue fixing."
  ↓
Claude: [reads errors, fixes more files, runs linter]
  ↓
Claude: "Fixed 4 more files. 18 problems remaining. I'm done."
  ↓
Stop Hook: [INTERCEPTS AGAIN] "Did you see '0 problems'? No? Continue."
  ↓
Claude: [continues fixing, runs linter]
  ↓
Claude: "All files fixed. 0 problems. I'm done."
  ↓
Stop Hook: [SEES COMPLETION PROMISE] "You're actually done now."
  ↓
Session: [STOP - task complete]
```

**The Pattern**: Stop hook acts as a **persistence layer**—it won't let Claude quit until success criteria are met.

### Technical Detail: How the Hook Reinjects Prompts

The Stop hook has access to:

- **Last output**: Claude's final response before attempting to stop
- **Iteration count**: How many loops have occurred
- **Completion promise**: The success signal to look for

When Stop hook fires, it:

1. Checks if `--completion-promise` text appears in Claude's output (using **exact string matching**)
2. If yes → Allow Claude to stop (task complete)
3. If no → Check if `iteration count < --max-iterations`
   - If yes → Inject prompt: "The task isn't complete yet. Review the output, identify what's wrong, fix it, and verify the result."
   - If no → Force stop with warning: "Max iterations reached. Stopping."

**Why This Works**: Claude Code is stateful—it remembers the conversation. Each reinjection adds context about what failed, creating a **self-correcting loop** where Claude learns from previous attempts.

### Critical Technical Detail: Completion Promise is Static

**The `--completion-promise` parameter is set once and cannot be changed during runtime.**

This means:

- ❌ You **cannot** add a completion promise after starting the loop
- ❌ You **cannot** modify it mid-loop (e.g., change from "DONE" to "COMPLETE")
- ❌ You **cannot** have multiple conditions (no "DONE OR SUCCESS")
- ✅ You **must** get it right at the initial `/ralph-loop` command

The Stop hook checks for the **same exact string** on every iteration using exact string matching—there's no dynamic adaptation or smart detection.

**Why `--max-iterations` is Your Primary Safety Net**: Since the completion promise uses fragile exact string matching and cannot be changed during runtime, always rely on `--max-iterations` as your main safety mechanism. The completion promise is a success signal, not a safety mechanism.

---

## Installing Ralph Wiggum Plugin

The Ralph Wiggum plugin is available through Claude Code plugin marketplaces. This lesson teaches the standard marketplace installation approach—no custom development required.

### Step 1: Add Marketplace

If you haven't already added the Anthropic plugins marketplace (from Lesson 16):

```bash
claude
/plugin marketplace add anthropics/claude-plugins-official
```

### Step 2: Install Ralph Wiggum

Use the interactive plugin UI:

```bash
/plugin
```

Select "ralph-wiggum" from the list and install.

**Alternative: Direct Install**

```bash
/plugin install ralph-loop@claude-plugins-official
```

### Verification

After installation, the `/ralph-loop` and `/cancel-ralph` commands become available.

Test by running:

```bash
/ralph-loop --help
```

You should see usage instructions with parameter options.

**Note**: Installation is one-time. The plugin persists across all future Claude Code sessions.

---

## Identifying Good Ralph Loop Use Cases

Not every task benefits from autonomous iteration. Here's how to decide:

### Decision Table: Ralph Loop Fit Analysis

| Criteria            | Good Fit                                          | Poor Fit                            |
| ------------------- | ------------------------------------------------- | ----------------------------------- |
| **Iteration Count** | 10+ expected iterations                           | 1-5 iterations                      |
| **Verification**    | Clear success signal (tests pass, build succeeds) | Subjective quality assessment       |
| **Scope**           | Single well-defined goal                          | Multiple independent goals          |
| **Failure Mode**    | Errors provide clear feedback                     | Silent failures or ambiguous errors |
| **Cost Tolerance**  | Budget allows $20-100 API spend                   | Cost-sensitive ($5 limit)           |
| **Supervision**     | Can check back in 30-60 min                       | Need immediate validation           |

### Good Use Cases

**1. Framework Upgrades**

- **Example**: "Upgrade Next.js from 14 to 15 and fix all breaking changes"
- **Completion promise**: `"npm run build successful"`
- **Why it works**: Build errors give clear feedback, completion is objective

**2. Test-Driven Refactoring**

- **Example**: "Refactor authentication module to use JWT tokens while keeping all tests passing"
- **Completion promise**: `"All 47 tests passing"`
- **Why it works**: Tests provide immediate verification

**3. Linting/Type Error Resolution**

- **Example**: "Fix all TypeScript errors in the project"
- **Completion promise**: `"tsc reports 0 errors"`
- **Why it works**: Compiler output is deterministic

**4. Deployment Debugging**

- **Example**: "Deploy to staging and resolve all errors until health check passes"
- **Completion promise**: `"Health check: 200 OK"`
- **Why it works**: HTTP status provides clear success signal

### Poor Use Cases

**1. Tasks Requiring Human Judgment**

- **Why**: Decisions involving strategy, aesthetics, business priorities, or ethical considerations need human input
- **Examples**: "Choose the best UI design", "Decide which features to prioritize", "Review if this messaging aligns with brand voice"
- **Better approach**: Manual collaboration where you provide the judgment

**2. Exploratory Research**

- **Why**: No clear completion criteria, open-ended discovery
- **Better approach**: Manual collaboration

**3. Creative Work** (writing, design, architecture decisions)

- **Why**: Quality is subjective, requires taste and context
- **Better approach**: Interactive feedback

**4. Multi-Goal Tasks** ("Fix bugs AND add features AND write docs")

- **Why**: Unclear which goal to prioritize, no single completion signal
- **Better approach**: Break into separate Ralph Loops

**5. Tasks Requiring External Input** (waiting for API keys, user decisions, third-party approvals)

- **Why**: Loop will stall waiting for something Claude can't provide
- **Better approach**: Complete setup manually first

**The Golden Rule**: Ralph Loop excels when success is **objective**, **verifiable**, and **deterministic**—measurable by tools, not human judgment.

---

## Hands-On: Your First Ralph Loop

### Step 1: Identify Your Iteration-Heavy Task

Think about your current project. What task would benefit from autonomous iteration?

**Prompts to help identify**:

- "What task have I done recently that required copying errors back to Claude multiple times?"
- "What framework or library am I planning to upgrade?"
- "What test suite keeps failing with different errors each run?"

**Examples by domain**:

| Domain          | Candidate Task                                              |
| --------------- | ----------------------------------------------------------- |
| Web Development | "Upgrade React dependencies and fix breaking changes"       |
| Data Science    | "Fix all pandas deprecation warnings in analysis notebooks" |
| DevOps          | "Debug Kubernetes deployment until all pods healthy"        |
| Mobile          | "Resolve all Xcode build warnings"                          |
| Backend         | "Migrate database schema and fix ORM compatibility"         |

### Step 2: Define Your Completion Promise

What text signals "we're done"?

**Good completion promises** are:

- **Objective**: Appear in command output, not subjective judgment
- **Specific**: Exact text string, not vague description
- **Terminal**: Only appear when truly complete

**Two approaches**:

**Approach 1: Use Natural Tool Output**

Rely on commands naturally producing completion signals:

| Task          | Completion Promise               |
| ------------- | -------------------------------- |
| Build fixes   | `"Build completed successfully"` |
| Test suite    | `"42 passed"` or `"0 failed"`    |
| Linting       | `"0 problems"`                   |
| Deployment    | `"deployment status: healthy"`   |
| Type checking | `"Found 0 errors"`               |

**Approach 2: Embed Output Promise in Prompt** (Recommended for reliability)

Explicitly instruct Claude to output a completion marker:

```bash
/ralph-loop "Standardise error handling in src/:
- Replace inline string errors with Error subclasses
- Add error tests where missing
- Keep public API unchanged
Output <promise>STANDARDISED</promise> when done." \
--max-iterations 15 \
--completion-promise "STANDARDISED"
```

**Why this works better**:

- You control the exact completion signal, not dependent on tool output format
- Claude explicitly knows what to output when complete
- More reliable across different tools and environments
- Clear contract: task instructions + explicit success marker
- Works reliably with static completion promises (set once at loop start)

**More examples with embedded promises**:

```bash
# Refactoring example
/ralph-loop "Refactor authentication module to use JWT:
- Replace session-based auth with JWT tokens
- Update all tests to pass
- Ensure no breaking changes to API
Output <promise>REFACTORED</promise> when complete." \
--max-iterations 20 \
--completion-promise "REFACTORED"

# Migration example
/ralph-loop "Migrate database schema:
- Run migration scripts
- Verify all tables updated
- Run test suite to confirm
Output <promise>MIGRATION_COMPLETE</promise> when done." \
--max-iterations 10 \
--completion-promise "MIGRATION_COMPLETE"
```

**Best Practice**: Use the embedded `<promise>` pattern for complex tasks where tool output might vary. Use natural tool output for simple, standard commands (linters, test runners).

### Step 3: Set Safety Guardrails

Determine `--max-iterations` based on task complexity:

| Task Complexity       | Suggested Max Iterations | Expected Cost |
| --------------------- | ------------------------ | ------------- |
| Simple (5-10 errors)  | 15-20                    | $10-20        |
| Medium (10-30 errors) | 30-40                    | $30-60        |
| Complex (50+ errors)  | 50-80                    | $80-150       |

**Conservative approach**: Start with 20 iterations. If the loop hits the limit without completing, you can restart with a higher limit—or break the task into smaller chunks.

### Step 4: Run Your First Loop

**Template with Embedded Promise** (Recommended):

```bash
/ralph-loop "TASK DESCRIPTION
- Specific requirement 1
- Specific requirement 2
- Verification step
Output <promise>COMPLETION_MARKER</promise> when done." \
--max-iterations LIMIT \
--completion-promise "COMPLETION_MARKER"
```

**Real example**:

```bash
/ralph-loop "Fix all ESLint errors in the project:
- Run ESLint on all files
- Fix each error
- Re-run ESLint to verify
Output <promise>LINTING_COMPLETE</promise> when all errors resolved." \
--max-iterations 20 \
--completion-promise "LINTING_COMPLETE"
```

**Alternative (using natural tool output)**:

```bash
/ralph-loop "Fix all ESLint errors in the project" --max-iterations 20 --completion-promise "0 problems"
```

### Step 5: Monitor Progress

Ralph Loop doesn't require constant attention, but checking periodically helps:

- **Every 15 minutes**: Quick glance at current iteration count
- **After 30 minutes**: Review what Claude has attempted
- **If loop seems stuck**: Use `/cancel-ralph` to stop and investigate

### Step 6: Review Results

When the loop completes (or hits max iterations):

1. **Check the completion criteria**: Did it actually succeed?
2. **Review the changes**: Use `git diff` to see what Claude modified
3. **Test manually**: Verify the result works as expected
4. **Analyze the iteration path**: What did Claude struggle with? (Informs future loops)

**Expected Outcome**: You've successfully run an autonomous iteration loop and seen how Claude self-corrects without manual feedback.

---

## Best Practices and Safety

### Safety First: Cost Management

Ralph Loop can consume significant API credits. Real-world examples:

- 14-hour upgrade session: ~$50-100 in API costs
- 30-iteration React migration: ~$30-40
- 80-iteration refactor: ~$80-150

**Cost Protection Rules**:

1. **Always set `--max-iterations`** - Never run without a limit
2. **Start conservative** - Use lower limits first, increase if needed
3. **Monitor spending** - Check Claude Code usage dashboard during long loops
4. **Use incremental approach** - Break large tasks into smaller loops
5. **Test on small scope first** - Run on one module before entire codebase

### Quality Best Practices

**1. Write Clear Task Descriptions**

- **Poor**: "Fix the app"
- **Good**: "Resolve all ESLint errors in src/ directory"

**2. Use Embedded Promise Pattern for Reliability**

Use the embedded `<promise>` pattern (detailed in Step 2) instead of relying on unpredictable tool output. This gives you full control over the completion signal and ensures Claude knows exactly what to output.

**3. Choose Unambiguous Completion Promises**

- **Poor**: "everything works"
- **Good**: "0 errors, 0 warnings" (natural output) or "TASK_COMPLETE" (embedded promise)

**4. Provide Context in CLAUDE.md**

Before running Ralph Loop, ensure CLAUDE.md includes:

- Project structure
- Testing commands
- Build commands
- Coding conventions

Better context → fewer wasted iterations

**5. Use Version Control**

Before starting a loop:

```bash
git checkout -b upgrade-react-19
git commit -am "Checkpoint before Ralph Loop"
```

If the loop goes wrong, you can revert straightforwardly.

**6. Review, Don't Blindly Accept**

Ralph Loop automates iteration, not judgment. Always review the final result before merging.

### When to Stop and Intervene

Cancel the loop (`/cancel-ralph`) if:

- Same error repeats 3+ times (Claude is stuck)
- Iteration count grows faster than progress
- Claude starts making unrelated changes
- External dependency issue (API key, network, permissions)

**The Philosophy**: Ralph Loop is a powerful tool, not autopilot. You remain responsible for the outcome.

---

## Common Questions

**Q: Can Ralph Loop run overnight while I sleep?**

Technically yes, but not recommended unless:

- Task is well-scoped and tested on smaller scope first
- You have cost monitoring alerts set up
- You're comfortable with potential $100+ API spend
- Version control allows easy rollback

Most users prefer checking in every 30-60 minutes.

**Q: What happens if I lose internet connection during a loop?**

The loop stops. Claude Code requires persistent connection. When you reconnect, you'll need to restart the loop, but Claude will see previous attempts in the conversation history.

**Q: Can I run multiple Ralph Loops in parallel?**

Yes, in separate Claude Code sessions (like Boris's parallel sessions pattern from Lesson 18). Each loop operates independently.

**Q: How do I know if Ralph Loop is actually making progress?**

Watch for:

- Iteration count increasing
- Different errors appearing (not same error repeating)
- Code changes in git diff
- Completion promise text getting closer (e.g., "12 errors" → "5 errors" → "0 errors")

**Q: Is Ralph Loop the same as GitHub Copilot Workspace or Cursor's Agent mode?**

Similar concept (autonomous iteration), different implementation:

- **Ralph Loop**: Uses Stop hooks to reinject prompts in Claude Code
- **Copilot Workspace**: Task-specific autonomous agent
- **Cursor's Agent mode**: Multi-file editing with autonomous planning

All solve iteration fatigue, but with different architectures.

**Q: Can I change the completion promise while the loop is running?**

No. As explained in "How Stop Hooks Work," the `--completion-promise` parameter is static—set once at loop start using exact string matching. You cannot modify it during runtime or use multiple completion conditions. This is why the embedded `<promise>` pattern (Step 2) is critical for reliability.

**Q: Can I use Ralph Loop without the plugin by manually reinjecting prompts?**

Yes, but extremely tedious. The plugin automates exactly what you'd do manually: check result, decide if done, prompt Claude to continue if not. Doing this 30 times manually defeats the purpose.

---

## Try With AI

Let's explore how to apply Ralph Loop to your specific workflow:

**🔍 Identify Your Loop Candidates:**

> "Analyze my current workflow [describe your typical tasks: web dev, data analysis, DevOps, etc.]. Which tasks would benefit most from autonomous iteration using Ralph Loop? For each candidate, suggest: (1) the task description, (2) appropriate completion promise, (3) estimated max-iterations, (4) potential risks or gotchas."

**What you're learning**: How to recognize automation opportunities in your own work, not generic examples.

---

**🎯 Design Safety Guardrails:**

> "I want to use Ralph Loop for [YOUR SPECIFIC TASK]. Help me design safety guardrails: (1) What's a reasonable --max-iterations limit? (2) What could go wrong and how do I detect it early? (3) What should I put in CLAUDE.md to give Claude the context it needs? (4) How do I test this on a small scope before running on the full codebase?"

**What you're learning**: Risk assessment and incremental validation—critical skills for production AI usage.

---

**🚀 Troubleshoot a Stuck Loop:**

> "I'm running a Ralph Loop to [YOUR TASK], but after 8 iterations, Claude keeps hitting the same error: [DESCRIBE ERROR]. The completion promise is '[YOUR PROMISE]'. Why might Claude be stuck? How can I help it get unstuck without canceling the loop and starting over?"

**What you're learning**: Debugging autonomous systems—recognizing when AI needs human intervention to break out of local optima.

---

## Why This Matters: Connection to Digital FTE Vision

**Workflow Impact**:

Ralph Loop demonstrates **autonomous execution**—one of the core capabilities of Digital FTEs. When you package skills, specs, and autonomous iteration into an agent, you create systems that:

- Start with a goal
- Work toward completion independently
- Self-correct when errors occur
- Signal when human judgment is needed

This is the pattern behind sellable AI agents:

- Customer provides goal ("Upgrade our application")
- Agent executes autonomously
- Customer pays for outcome, not hourly labor

**Paradigm Connection**:

You learned in Chapter 1 that AI shifts work from "executing" to "orchestrating." Ralph Loop embodies this:

- **You orchestrate**: Define goal, set guardrails, review results
- **Claude executes**: Iterates toward completion without hand-holding

**Real-World Context**:

The same pattern powers production AI employees:

- Autonomous sales agents that iterate through lead qualification
- Customer support agents that iterate toward issue resolution
- DevOps agents that iterate toward successful deployment

Mastering Ralph Loop teaches you the mechanics of autonomous iteration—essential for building and selling Digital FTEs.
