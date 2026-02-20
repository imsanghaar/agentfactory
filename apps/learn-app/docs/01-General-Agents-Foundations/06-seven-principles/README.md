---
sidebar_position: 6
title: "Chapter 6: The Seven Principles of General Agent Problem Solving"
slides:
  source: "https://pub-80f166e40b854371ac7b05053b435162.r2.dev/books/ai-native-dev/static/slides/part-1/chapter-06/agent-director-strategy.pdf"
  title: "Agent Director Strategy"
  height: 700
---

# Chapter 6: The Seven Principles of General Agent Problem Solving

You've learned the tools—Claude Code, CLAUDE.md, Skills, Subagents. You've learned context engineering. But here's what separates productive sessions from frustrating ones: **workflow discipline**.

Two people use Claude Code for the same task. One finishes in 20 minutes with clean commits. The other spends an hour in correction loops, ends up with a polluted context, and starts over. Same AI. Same capabilities. What's different?

**The answer: principles.**

This chapter teaches the **Seven Principles of General Agent Problem Solving**—the operational patterns that make AI collaboration reliable rather than random. These aren't abstract theories; they're the habits that turn Claude from a novelty into a production tool.

## From Chaos to System

Early Claude Code users discover a frustrating pattern: sometimes it works brilliantly, sometimes it fails mysteriously. The difference isn't luck—it's whether you're following principles that align with how AI agents actually work.

The Seven Principles emerged from analyzing thousands of successful and failed AI sessions. They answer questions like: Why does Claude sometimes go in circles? Why do long sessions degrade? Why do some prompts work and others don't?

Each principle addresses a specific failure mode:
- **Bash is the Key** — Why Claude can do things, not just say things
- **Code as Universal Interface** — Why precise requests get precise results
- **Verification as Core Step** — Why "looks right" isn't good enough
- **Small, Reversible Decomposition** — Why big changes create big problems
- **Persisting State in Files** — Why Claude forgets (and how to fix it)
- **Constraints and Safety** — Why guardrails enable autonomy
- **Observability** — Why you need to see what Claude is doing

## Prerequisites

This chapter builds directly on:

- **Chapter 3** — You learned Claude Code's core capabilities: CLAUDE.md for persistent memory (Lesson 5), Skills (Lesson 7-8), and Subagent orchestration (Lesson 9)
- **Chapter 4** — You learned context engineering: why context quality determines agent reliability, and the Tasks system for persistent state
- **Chapter 5** — You learned Spec-Driven Development: the four-phase workflow that structures AI collaboration

The Seven Principles provide the **conceptual framework** that explains _why_ these capabilities work together effectively.

## 📚 Teaching Aid

## What You'll Learn

By the end of this chapter, you'll be able to:

- **Execute** the four-phase workflow (Explore, Plan, Implement, Commit) for any non-trivial task
- **Recognize** the five failure patterns before they waste your time
- **Apply** course correction techniques (Esc, checkpoints, /rewind) confidently
- **Configure** permission models that match your trust level
- **Use** the Interview Pattern to surface requirements before implementation
- **Create** CLAUDE.md files and ADRs that persist knowledge across sessions
- **Design** prompts that invoke principles explicitly for better results
- **Debug** AI workflows using activity logs and observability practices

## Key Prompt Patterns

| Principle               | Pattern                    | Example Prompt                                              |
| ----------------------- | -------------------------- | ----------------------------------------------------------- |
| **Bash is the Key**     | Command verification       | "Use `ls` to verify the directory exists before creating"   |
| **Code as Interface**   | Specification over prose   | "Write an interface for the expected input/output"          |
| **Verification**        | Test-first instruction     | "Write the test first, then implement to pass it"           |
| **Decomposition**       | Atomic commits             | "Break this into steps. Commit after each step works."      |
| **State Persistence**   | Context file creation      | "Add this decision to CLAUDE.md so future sessions know"    |
| **Constraints**         | Permission boundaries      | "Only modify files in the `src/` directory"                 |
| **Observability**       | Progress reporting         | "After each step, report what you did and what's next"      |

## Chapter Structure

| Lesson | Title                           | Focus                                                           |
| ------ | ------------------------------- | --------------------------------------------------------------- |
| 1      | Bash is the Key                 | Terminal as foundational agentic capability                     |
| 2      | Code as Universal Interface     | Precision through code vs. natural language                     |
| 3      | Verification as Core Step       | Continuous testing as primary workflow                          |
| 4      | Small, Reversible Decomposition | Atomic steps, git commits, revert-don't-fix mindset             |
| 5      | Persisting State in Files       | CLAUDE.md, ADRs, session journals                               |
| 6      | Constraints and Safety          | Permission models, guardrails, trust gradualism                 |
| 7      | Observability                   | Activity logs, progress tracking, debugging                     |
| 8      | Operational Best Practices      | Four-phase workflow, course correction, five failure patterns   |
| 9      | Putting It All Together         | Integrated workflows, the Director's Mindset                    |
| 10     | Principles Exercises            | 17 hands-on exercises across 8 modules with capstone projects   |
| 11     | Chapter Quiz                    | Assessment of principle understanding                           |

Remember the thesis: **General Agents BUILD Custom Agents.** The Seven Principles are HOW you direct those agents reliably—transforming from a typist who types prompts into a director who orchestrates outcomes.
