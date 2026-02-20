---
sidebar_position: 12
title: "Chapter 12: Version Control & Safe Experimentation"
---

# Chapter 12: Version Control & Safe Experimentation

You've been working on a document for three hours. You try something experimental. It breaks everything. You frantically press Ctrl+Z twenty times hoping to get back to the working version. Sometimes it works. Sometimes you lose an hour of progress.

**The problem isn't experimentation. It's experimenting without a safety net.**

This chapter teaches you to use Git and GitHub — not by memorizing commands, but by understanding how version control gives you the confidence to experiment freely. Every change is tracked. Every experiment can be rolled back. Your AI Employee will use these same patterns to work autonomously without risking your data.

## Principles Applied

| Principle                           | How It Applies                                            |
| ----------------------------------- | --------------------------------------------------------- |
| **Small, Reversible Decomposition** | Commit small changes you can undo; branch for experiments |
| **Verification as Core Step**       | Check status before and after every operation             |
| **Constraints and Safety**          | Branches isolate experiments; never push untested code    |
| **Observability**                   | Git log shows exactly what changed, when, and why         |
| **Bash is the Key**                 | Git operations happen in the terminal                     |

## Interface Focus

**Primary**: Code (Git is a command-line tool)
**Secondary**: Cowork (for understanding concepts and planning branching strategies)

## What You'll Learn

By the end of this chapter, you'll be able to:

- Create repositories and track changes with meaningful commit messages
- View differences and safely undo changes at multiple levels
- Use branches to test ideas without risking working code
- Push to GitHub for cloud backup and portfolio building
- Use pull requests for code review (even reviewing your own AI-generated code)
- Apply reusable Git patterns for common development scenarios

## Lessons

| Lesson                                         | Title                           | Focus                                           |
| ---------------------------------------------- | ------------------------------- | ----------------------------------------------- |
| [L01](./01-your-first-git-repository.md)       | Your First Git Repository       | init, add, commit — the basic snapshot cycle    |
| [L02](./02-viewing-changes-safe-undo.md)       | Viewing Changes & Safe Undo     | diff, log, restore — understanding what changed |
| [L03](./03-testing-ai-safely-with-branches.md) | Testing AI Safely with Branches | branch, checkout, merge — isolated experiments  |
| [L04](./04-cloud-backup-portfolio.md)          | Cloud Backup & Portfolio        | remote, push, pull — GitHub as your safety net  |
| [L05](./05-code-review-pull-requests.md)       | Code Review & Pull Requests     | PR workflow for reviewing AI-generated changes  |
| [L06](./06-reusable-git-patterns.md)           | Reusable Git Patterns           | Common workflows you'll use repeatedly          |
| [Quiz](./08-chapter-quiz.md)                   | Chapter Quiz                    | Test your understanding                         |

## Connection to Building Your AI Employee (Chapter 13)

The version control patterns you build here provide the safety infrastructure for building your own AI Employee. In Chapter 13, Git enables:

- Tracking all changes your AI Employee makes to your vault
- Rolling back automated actions that produce unexpected results
- Branching strategies for testing new employee behaviors
- Audit trails showing exactly what your employee did and when

**Version control is what makes autonomous AI operation safe.**
