---
sidebar_position: 9
title: "Putting It All Together: Workflows in Practice"
chapter: 6
lesson: 9
duration_minutes: 35
description: "Synthesis lesson showing how all seven principles combine in real-world agentic workflows"
keywords:
  [
    "workflow",
    "synthesis",
    "practical",
    "real-world",
    "integration",
    "end-to-end",
  ]

# HIDDEN SKILLS METADATA
skills:
  - name: "Integrated Workflow Design"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Computational Thinking"
    measurable_at_this_level: "Student can design workflows that integrate all seven principles appropriately for specific tasks"

  - name: "Principle Selection and Application"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can analyze a task and determine which principles are most critical and how to apply them"

  - name: "Workflow Optimization"
    proficiency_level: "B2"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "Critical Thinking"
    measurable_at_this_level: "Student can evaluate and optimize existing workflows by applying the seven principles"

learning_objectives:
  - objective: "Integrate all seven principles into a cohesive workflow for real-world tasks"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Student designs a complete workflow that demonstrates appropriate application of all principles"

  - objective: "Evaluate which principles are most critical for specific types of tasks"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Student can analyze different task types and prioritize principles based on task characteristics"

  - objective: "Apply the seven principles to improve existing workflows"
    proficiency_level: "B2"
    bloom_level: "Evaluate"
    assessment_method: "Student identifies weaknesses in current workflows and proposes principle-based improvements"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (workflow integration, principle prioritization, task type analysis, workflow optimization, pattern recognition) within B1-B2 limit of 7 ✓"

differentiation:
  extension_for_advanced: "Design a comprehensive workflow framework for a specific domain (e.g., web development, data science) that codifies principle application patterns."
  remedial_for_struggling: "Focus on one complete example walkthrough, then practice with similar tasks. Emphasize the practical application over theoretical understanding."

teaching_guide:
  lesson_type: "core"
  session_group: 4
  session_title: "Synthesis and Practice"
  key_points:
    - "The Director's Loop mindset shift: students move from typing code to directing an agent that investigates, proposes, implements, and verifies"
    - "Different task types prioritize different principles: debugging emphasizes P1/P3/P7, refactoring emphasizes P2/P4/P5, new features need all seven"
    - "Three reusable workflow templates (Quick Fix, Feature Development, Refactoring) provide ready-to-use patterns students can adapt"
    - "The meta-principle: general agents are most effective when they leverage computing fundamentals (files, shells, code, version control) rather than fighting them"
  misconceptions:
    - "Students may think every task needs all seven principles equally, when principle prioritization based on task type is the key skill"
    - "Some students treat the workflow templates as rigid scripts rather than adaptable frameworks to customize for their context"
    - "The self-assessment checklist can feel like busywork unless students connect low scores to actual frustrating sessions they have experienced"
  discussion_prompts:
    - "Which of the seven principles do you think you already apply naturally? Which do you consistently neglect? Why?"
    - "The lesson says 'You are no longer the typist, you are the director.' What changes about your daily work if you fully adopt this mindset?"
    - "When Template 1b shows what to do when verification fails, how does that connect to the Correction Loop failure pattern from Lesson 8?"
  teaching_tips:
    - "Walk through one complete workflow example end-to-end, explicitly naming each principle as it is applied, before discussing the theory"
    - "Have students score themselves on the 7-point self-assessment, then pair up to discuss their gaps and strategies for improvement"
    - "Use the Principle Selection Guide table as a classroom activity: give students task scenarios and have them identify the top 2-3 principles"
    - "The Director's Tip (explicitly invoking principles in prompts) is a power technique worth demonstrating live with a real Claude Code session"
  assessment_quick_check:
    - "For a quick bug fix, which 2-3 principles are most critical and why?"
    - "Describe the Director's Loop: what is the human's role versus the AI agent's role?"
    - "What is the meta-principle that underlies all seven principles?"
---

# Putting It All Together: Workflows in Practice

You've learned the seven principles of general agent problem solving:

1. **Bash is the Key** - Terminal access enables agentic capability
2. **Code as Universal Interface** - Code provides precision in communication
3. **Verification as Core Step** - Continuous testing ensures reliability
4. **Small, Reversible Decomposition** - Breaking problems into manageable steps
5. **Persisting State in Files** - Context files maintain shared understanding
6. **Constraints and Safety** - Guardrails enable confident collaboration
7. **Observability** - Visibility enables debugging and trust

Knowing the principles is one thing. Applying them together in real workflows is another. This lesson shows how the principles combine in practice, with concrete examples you can adapt to your own work.

## Your New Role: From Typist to Director

Here's the mindset shift: **You're no longer the one typing code. You're the director managing an agent.**

Think of the AI as a junior developer with infinite energy but no institutional knowledge. It will work tirelessly, but it needs:

- Clear direction (what to do)
- Context (why and how)
- Guardrails (what NOT to do)
- Verification (did it work?)

Your job is no longer typing—it's directing, reviewing, and approving. The seven principles are your management framework.

```
                    THE DIRECTOR'S LOOP

         YOU (Director)              AI (Agent)
        ┌───────────┐              ┌───────────┐
        │  Intent   │──── P2 ────►│ Investigate│
        │  & Context│   (Code)    │ & Propose  │
        │           │◄── P7 ─────│            │
        │  Review   │ (Observe)   │  Implement │
        │  & Approve│──── P6 ────►│  & Verify  │
        └─────┬─────┘ (Safety)    └─────┬──────┘
              │                         │
              │        P3 (Verify)      │
              └─────── P4 (Small) ──────┘
                       P5 (Persist)

    P1 (Bash) underlies every AI action
```

## The Integration Challenge: Principles in Combination

Real workflows rarely involve a single principle in isolation. They require multiple principles working together:

| Task                       | Key Principles | Why These Principles Matter                                                                      |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------------ |
| **Debug production issue** | 1, 3, 7        | Terminal access to investigate, verification of fixes, observability to understand what happened |
| **Refactor large module**  | 2, 4, 5        | Code as specification, small reversible steps, context persistence for patterns                  |
| **Add new feature**        | All principles | Complete workflow needs all aspects                                                              |
| **Set up new project**     | 1, 5, 6        | Terminal for setup, context files, safety for new environment                                    |
| **Optimize performance**   | 1, 3, 7        | Terminal for profiling, verification of improvements, observability to find bottlenecks          |

## Workflow 1: Debugging a Production Issue

### Scenario

You get a report: "Users are seeing 'Invalid token' errors when logging in."

### Applying the Principles

**Principle 1: Bash is the Key**

```bash
# AI can investigate directly
tail -f /var/log/app.log              # Real-time logs
grep "Invalid token" /var/log/app.log # Find related errors
ps aux | grep node                    # Check running processes
```

**Principle 7: Observability**

```bash
# Trace through the system
# AI reads logs to understand the sequence:
# 14:32:15 - Login request from user@example.com
# 14:32:16 - Token generated: eyJhbGc...
# 14:32:17 - Token validation: FAIL
# 14:32:17 - Error: Invalid token
```

**Principle 3: Verification as Core Step**

```bash
# AI proposes fix, then verifies
# "I see the issue: Token validation uses wrong secret"
# AI reads .env file
# AI confirms: TOKEN_SECRET mismatch
# AI proposes: Fix secret in .env
# You verify: Is this the correct secret?
# AI tests: Login with test credentials
```

**Principle 4: Small, Reversible Decomposition**

```bash
# Fix in one step, verify, then move on
Step 1: Update .env with correct secret
Step 2: Restart application
Step 3: Verify login works
Step 4: Monitor logs for recurrence
```

**Principle 6: Constraints and Safety**

```bash
# AI doesn't automatically modify production .env
# Requires your confirmation
# You: "Show me the diff before applying"
# AI shows: -TOKEN_SECRET=old +TOKEN_SECRET=new
# You approve, AI applies change
```

### Complete Workflow

```
You: "Users getting 'Invalid token' errors. Help debug."

AI: "Let me investigate.
[Reads logs]
I see: Token validation failing for all logins.
[Checks .env]
Found: TOKEN_SECRET doesn't match what's encoded in tokens.
[Checks token generation code]
Confirmed: app.js uses TOKEN_SECRET from .env, but .env has wrong value.

Proposed fix:
1. Update .env with correct TOKEN_SECRET
2. Restart application
3. Test login
4. Monitor logs

Shall I proceed?"

You: "Show me the diff first."

AI: [Shows .env diff]

You: "Approved."

AI: [Applies change]
[Restarts app]
[Tests login]
✓ Login working
[Monitoring logs]
✓ No new errors

Fixed. Summary: TOKEN_SECRET mismatch caused validation failures.
Corrected secret, restarted, verified login working."
```

## Workflow 2: Implementing a New Feature

### Scenario

You need to add: "Users can reset their password via email."

### Applying the Principles

**Principle 5: Persisting State in Files**

```markdown
# First, update CLAUDE.md with new context

## Current Work

### In Progress

- Password reset feature: email token generation, reset endpoint, UI

### Requirements

- Token expires in 1 hour
- Single-use tokens
- Email sent via SendGrid
```

**Principle 2: Code as Universal Interface**

```typescript
// Write specification as code (test)
test("password reset flow", async () => {
  // Request reset
  const response1 = await requestReset("user@example.com");
  expect(response1.success).toBe(true);

  // Get token from email (mock)
  const token = await getLastEmailToken();

  // Use token to reset
  const response2 = await resetPassword(token, "newPassword123");
  expect(response2.success).toBe(true);

  // Login with new password
  const response3 = await login("user@example.com", "newPassword123");
  expect(response3.success).toBe(true);
});
```

**Principle 4: Small, Reversible Decomposition**

```
Break into 8 steps:
1. Add password reset token to database schema
2. Create token generation utility
3. Create password reset email template
4. Add POST /auth/reset-request endpoint
5. Add POST /auth/reset-confirm endpoint
6. Add password reset UI
7. Add tests
8. Integrate with SendGrid
```

**Principle 3: Verification as Core Step**

```bash
# After each step:
npm test                     # Run tests
git diff                     # Review changes
npm run build               # Verify build
```

**Principle 1: Bash is the Key**

```bash
# AI executes each step
# Step 1: Modify schema
npx prisma migrate dev --name add-reset-tokens

# Step 2: Create utility
# [AI writes src/utils/token-generator.ts]

# Step 3: Create email template
# [AI writes emails/reset-password.html]

# Continue through all steps...
```

**Principle 6: Constraints and Safety**

```bash
# Safety checkpoints:
- Database migration: Show SQL before applying
- Email sending: Use sandbox API key first
- UI changes: Review before committing
```

**Principle 7: Observability**

```
AI provides progress updates:
"Step 3 complete: Created email template
Files: +emails/reset-password.html
Next: Add reset-request endpoint
Continue?"
```

### Complete Workflow Timeline

| Time | Step                                    | Principle(s) Applied  |
| ---- | --------------------------------------- | --------------------- |
| 0:00 | Write test specification                | 2 (Code as Interface) |
| 0:05 | Update CLAUDE.md with context           | 5 (Persist State)     |
| 0:10 | Break into 8 steps                      | 4 (Decomposition)     |
| 0:15 | Step 1: Database migration + verify     | 1, 3, 6               |
| 0:20 | Step 2: Token utility + verify          | 1, 3, 6               |
| 0:25 | Step 3: Email template + verify         | 1, 3, 6               |
| 0:30 | Step 4: Reset-request endpoint + verify | 1, 3, 6, 7            |
| 0:35 | Steps 5-8: Remaining work               | 1, 3, 6, 7            |
| 0:50 | Full test suite + integration tests     | 3 (Verification)      |
| 0:55 | Review all changes with git diff        | 7 (Observability)     |
| 1:00 | Commit if satisfied                     | 4 (Reversible)        |

## Workflow 3: Refactoring a Large Module

### Scenario

Refactor `src/auth/auth.js` (500 lines) into smaller, testable modules.

### Applying the Principles

**Principle 5: Persisting State in Files**

```markdown
# Document before starting

## Refactoring Plan: src/auth/auth.js

Current issues:

- 500-line file, hard to understand
- Mixed concerns: validation, storage, tokens
- No tests

Target structure:
src/auth/
├── validation.js # Input validation
├── storage.js # Database operations
├── tokens.js # Token generation/validation
├── auth.js # Orchestration (small)
└── **tests**/
├── validation.test.js
├── storage.test.js
└── tokens.test.js
```

**Principle 4: Small, Reversible Decomposition**

```
Step 1: Extract validation logic (reversible via git)
Step 2: Extract storage logic (reversible via git)
Step 3: Extract token logic (reversible via git)
Step 4: Write tests for extracted modules
Step 5: Update auth.js to use new modules
Step 6: Add integration tests
Step 7: Remove old auth.js code
Step 8: Full test suite
```

**Principle 2: Code as Universal Interface**

```javascript
// Before: Show current code
// After: Show refactored code
// AI proposes diff, you review
```

**Principle 3: Verification as Core Step**

```bash
# After each extraction:
npm test                      # Ensure tests still pass
npm run lint                  # Ensure code quality
npm run build                 # Ensure build succeeds
```

**Principle 1: Bash is the Key**

```bash
# AI executes refactor steps
git checkout -b refactor/auth-extraction
# [Performs extractions]
git diff --stat               # Show summary
```

**Principle 6: Constraints and Safety**

```bash
# Work on feature branch
# Commit after each successful step
# Easy rollback if needed
```

**Principle 7: Observability**

```
AI provides progress:
"Extracted validation (87 lines)
Created: src/auth/validation.js
Modified: src/auth/auth.js (-87 lines)
Tests: PASS
Commit? [y/n]"
```

## Principle Selection Guide: Which Principles When?

Not all principles are equally important for every task. Use this guide to prioritize:

| Task Type             | Most Critical Principles | Why                                               |
| --------------------- | ------------------------ | ------------------------------------------------- |
| **Quick bug fix**     | 1, 3, 7                  | Fast investigation, verify fix, see what happened |
| **New feature**       | All                      | Complete workflow needs all aspects               |
| **Refactoring**       | 2, 4, 5                  | Code precision, small steps, context persistence  |
| **Debugging**         | 1, 3, 7                  | Terminal access, verification, visibility         |
| **Learning codebase** | 1, 7, 5                  | Read files, observe patterns, understand context  |
| **Setup/install**     | 1, 5, 6                  | Terminal commands, state files, safety in new env |
| **Performance work**  | 1, 3, 7                  | Profiling (terminal), verification, observability |

## Workflow Templates: Ready-to-Use Patterns

### Template 1: Quick Fix Pattern

```
1. Describe problem to AI
2. AI reads files to understand (Principle 1, 7)
3. AI proposes solution as code diff (Principle 2)
4. You review and approve (Principle 6)
5. AI applies change (Principle 1)
6. AI verifies with tests (Principle 3)
7. AI shows summary (Principle 7)
8. You commit if satisfied (Principle 4)
```

### Template 1b: When the Fix Fails

What happens when step 6 (verification) fails? Don't panic—follow this recovery path:

```
6. AI verifies with tests → TESTS FAIL
   ↓
6b. AI identifies WHY it failed (Principle 7: Observability)
    "Tests fail because: [specific reason]"
   ↓
6c. AI reverts the change (Principle 4: Reversibility)
    git checkout -- . OR git reset --hard HEAD
   ↓
6d. AI proposes NEW approach based on what it learned
    "The first approach failed because X. Let me try Y instead."
   ↓
6e. Return to step 3 with new approach
```

**Key insight**: Failure is information. The failed attempt tells you what DOESN'T work, narrowing down what will. Revert cleanly, learn from the failure, try again.

### Template 2: Feature Development Pattern

```
1. Write test/specification (Principle 2)
2. Update CLAUDE.md with context (Principle 5)
3. Break feature into steps (Principle 4)
4. For each step:
   a. AI implements (Principle 1)
   b. AI verifies (Principle 3)
   c. AI shows progress (Principle 7)
   d. You approve (Principle 6)
5. Full integration tests (Principle 3)
6. Review all changes (Principle 7)
7. Commit (Principle 4)
```

### Template 3: Refactoring Pattern

```
1. Document current state (Principle 5)
2. Plan refactoring steps (Principle 4)
3. Create feature branch (Principle 6)
4. For each extraction:
   a. AI extracts code (Principle 2)
   b. AI verifies tests pass (Principle 3)
   c. AI shows what changed (Principle 7)
   d. Commit if good (Principle 4)
5. Integration tests (Principle 3)
6. Merge to main when ready (Principle 6)
```

## Evaluating Your Workflow: A Self-Assessment

Use this checklist to evaluate how well you're applying the principles:

### Terminal Access (Principle 1)

- [ ] AI can read project files directly
- [ ] AI can run commands (tests, builds, etc.)
- [ ] You're not copying/pasting code manually
- [ ] AI uses terminal for investigation, not just code generation

### Code as Interface (Principle 2)

- [ ] You provide specifications as code/tests, not vague descriptions
- [ ] You review AI-generated code as the primary feedback mechanism
- [ ] You use concrete examples to clarify requirements
- [ ] You iterate through code changes, not natural language debate

### Verification (Principle 3)

- [ ] You verify after every significant change
- [ ] Tests run automatically or with AI assistance
- [ ] You never accept code without testing
- [ ] You have appropriate verification depth for risk level

### Decomposition (Principle 4)

- [ ] You break tasks into small steps
- [ ] Each step can be independently tested
- [ ] Each commit is atomic and reversible
- [ ] You iterate rather than batch

### State Persistence (Principle 5)

- [ ] You maintain CLAUDE.md or similar context file
- [ ] Project conventions are documented
- [ ] Current work is tracked
- [ ] Decisions are documented (ADRs)

### Safety (Principle 6)

- [ ] Destructive operations require approval
- [ ] You work in sandbox/feature branches
- [ ] You have appropriate permission model
- [ ] You can easily rollback changes

### Observability (Principle 7)

- [ ] You can see what AI is doing
- [ ] You understand AI's rationale for changes
- [ ] You review activity logs when debugging
- [ ] AI provides progress updates

### Your Project Health Score

Count how many principles you're actively applying (1 point per principle with at least 2 checkboxes marked):

| Score   | Level           | What It Means                                                                                 |
| ------- | --------------- | --------------------------------------------------------------------------------------------- |
| **0-2** | Cowboy Coder    | High risk. You're flying blind. Start with Principles 3 (Verification) and 7 (Observability). |
| **3-4** | Collaborator    | Good progress. You're working WITH the AI, not just using it. Focus on the gaps.              |
| **5-6** | Agent Architect | Professional grade. You're managing AI effectively. Fine-tune for efficiency.                 |
| **7**   | Master Director | Full integration. You've internalized the principles. Now optimize and teach others.          |

**Where to start if you're at 0-2**: Begin with just two principles—Verification (always test) and Observability (always see what AI did). These two alone prevent most disasters.

## Why This Integration Matters

The principles are powerful individually. Together, they're transformative:

- **Terminal + Code + Verification**: AI can investigate, implement, and test autonomously
- **Decomposition + Safety + Observability**: Small, safe, visible steps
- **State Persistence**: Context accumulates across sessions

When you apply all principles together, you move from "using AI" to "collaborating with an intelligent agent." The workflow becomes:

1. You provide intent and direction
2. AI investigates and proposes solutions
3. You review and redirect
4. AI implements and verifies
5. You approve and integrate

This is the Agent Factory paradigm in action.

## The Meta-Principle

All seven principles derive from one meta-principle:

**General agents are most effective when they leverage computing fundamentals rather than fighting against them.**

File systems, shells, code execution, version control—these aren't limitations to work around. They're the foundations that enable reliable, debuggable, powerful agent workflows.

Claude Code makes this explicit through the terminal interface. Cowork makes it accessible through a GUI. But underneath, they're running on the same principles—the same Claude Agent SDK, the same reasoning engine, the same fundamental approach to problem-solving through computing primitives.

## Choosing Your Interface Based on Principles

Both interfaces support all seven principles. Choose based on your task characteristics:

| If you need...          | Claude Code                   | Claude Cowork                  |
| ----------------------- | ----------------------------- | ------------------------------ |
| Maximum observability   | Best choice (raw terminal)    | Good (three-panel layout)      |
| Minimal friction        | Good                          | Best choice (GUI)              |
| Custom constraints      | Best choice (hooks, settings) | Limited (built-in only)        |
| Built-in safety prompts | Manual configuration          | Best choice (native dialogs)   |
| Git-based reversibility | Native                        | Requires setup                 |
| Document workflows      | Requires Skills/tools         | Best choice (built-in Skills)  |
| Programmatic precision  | Best choice (code/scripts)    | Good (structured prompts)      |
| Non-technical users     | Requires terminal comfort     | Best choice (familiar desktop) |

The choice isn't "which is better"—it's "which fits this task." Many workflows benefit from using both: Claude Code for implementation, Cowork for documentation and review.

## The Director's Tip: Invoke Principles Explicitly

Here's a power move: **tell the AI which principle to use**.

Instead of vague instructions like "refactor this code," try:

```
"Refactor this using Principle 4—break it into 3 small steps.
After each step, show me what changed and wait for my approval
before continuing."
```

Or for a bug fix:

```
"Debug this using Principles 1, 3, and 7. Use the terminal to
investigate, verify your fix with tests, and show me the logs
so I can see what happened."
```

**Why this works**: You're giving the AI a framework, not just a task. It knows HOW you want it to work, not just WHAT you want done. This puts you firmly in the director's seat.

## Try With AI

### Prompt 1: Full Workflow Practice

```
I want to practice applying all seven principles together.

Here's a task I want to accomplish: [describe a real task you're working on]

Help me design a complete workflow:
1. Which principles are most critical for this task?
2. What steps should I take, in what order?
3. How will each principle be applied in each step?
4. What should I verify at each checkpoint?

Then, let's actually execute this workflow together, with you explaining which principle we're applying at each step and why.
```

**What you're learning**: How to integrate all seven principles into a cohesive workflow. You're experiencing how the principles work together to make AI collaboration more effective.

### Prompt 2: Workflow Optimization

```
I want to improve my current AI workflow.

Here's how I currently work with AI:
[Describe your current approach—what you do, how you interact, what tools you use]

Analyze this workflow against the seven principles:
1. Which principles am I applying well?
2. Which principles am I missing or underutilizing?
3. What's the impact of these gaps?
4. What specific changes should I make?

Help me create an improved workflow that applies all principles appropriately.
```

**What you're learning**: How to evaluate and optimize your existing workflows using the seven principles as a framework. You're learning to identify gaps and implement improvements.

### Prompt 3: Scenario-Based Practice

```
I want to practice principle selection for different scenarios.

Give me 5 different scenarios (e.g., debugging, refactoring, new feature, learning codebase, setup).

For each scenario:
1. Which 2-3 principles are MOST critical?
2. Why these specifically?
3. What would go wrong if I ignored them?
4. What's a minimal workflow that covers the essentials?

After reviewing all scenarios, help me identify patterns:
- Are some principles always important?
- Does principle priority depend on task type?
- What's a good default approach if I'm unsure?
```

**What you're learning**: How to select and prioritize principles based on task characteristics. You're developing judgment about which principles matter most in different contexts.

---

## Next Steps

These seven principles form the foundation for effective problem-solving with General Agents. In Part 2 and beyond, you'll apply these principles to increasingly sophisticated workflows:

- **Complex file processing** (Principles 1, 4, 5)
- **Data analysis and reporting** (Principles 2, 3, 7)
- **Multi-step research projects** (Principles 4, 5, 6)
- **Automated document generation** (Principles 2, 3, 4)
- **Browser-based automation** (Principles 3, 6, 7)
- **Building Custom Agents** (All principles at scale)

Each workflow will demonstrate how the principles combine in practice, using whichever interface—Claude Code or Cowork—best fits the task. The principles don't change; only their application deepens.
