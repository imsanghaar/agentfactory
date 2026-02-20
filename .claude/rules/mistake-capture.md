# Mistake Capture

Every error becomes a rule. This file is permanent memory for patterns that caused failures.

## Execution Mistakes

- Not verifying actions worked → Always VERIFY after executing
- Moving to Done without completing → Only Done when ACTUALLY done
- Getting stuck on blockers → Escalate immediately, don't spin
- Assuming success → Check return codes, file existence, test results

## Session Flow Mistakes

- Asking questions and continuing → When blocked, SESSION ENDS with clear question
- Not using background tasks for SDD → Multi-phase work MUST use Task tool
- Context compaction mid-feature → Delegate to subagent before context bloats
- Losing original intent → Write spec.md before implementation

## Content Mistakes (Educational Platform)

- Skipping reference lesson → ALWAYS read a reference lesson first
- Wrong chapter/part resolution → Use `ls -d` to discover paths, never guess
- Missing YAML frontmatter → Full skills/objectives required
- Stats without verification → WebSearch before claiming numbers

## Architecture Mistakes

- Not using available skills → Check skills first, don't improvise
- Writing configs from scratch → Search for tested templates FIRST
- Theoretical research → Reference ACTUAL tested examples, not invented configs
- Skipping infrastructure verification → Add "verify clean restart" as explicit task

## Infrastructure Mistakes

- Bind mounts for database data → Use named volumes (Docker-managed)
- Not testing clean start → ALWAYS verify `docker-compose down -v && up -d` works
- Hook scripts before directory creation → Always `mkdir -p` before first log

## Thinking Mistakes (Root Causes)

- Not checking existing patterns first → "How is this done in this project?"
- Overengineering → "What's the simplest solution that works?"
- Skipping to execution → Read architecture → Check dependencies → THEN execute
- Skills exist ≠ ready to execute → Skills describe what SHOULD happen

## How to Use This File

1. **When you make a mistake**: Add it here immediately
2. **Before starting work**: Scan relevant sections
3. **During reviews**: Check if any patterns were violated
4. **Format**: `- [Mistake] → [Correction]`
