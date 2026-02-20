# Prompt History Record: Chapter 6 File Processing Workflows - Complete Rewrite

**ID**: PHR-062-001
**Date**: 2025-01-27
**Stage**: green (implementation)
**Feature**: 062-ch6-file-workflow

---

## Prompt (Summary)

Implement all lessons for Chapter 6 following the Seven Principles chapter. Content should be beginner-friendly with proper hooks and reasonable cognitive load.

**Critical Correction**: User identified fundamental misunderstanding - Part 2 is about creating workflows WITH General Agent, not teaching manual bash commands. Students should DIRECT Claude Code, not type commands themselves.

---

## Response (Summary)

### Complete Rewrite Completed

**Initial approach (WRONG)**: Teaching students to type bash commands manually.

**Corrected approach**: Students DIRECT Claude Code through conversation, OBSERVE it work, and VERIFY results.

### Files Created (Final)

| File                                  | Lines | Purpose                                  |
| ------------------------------------- | ----- | ---------------------------------------- |
| `README.md`                           | 84    | Chapter overview - agent direction focus |
| `01-your-first-agent-workflow.md`     | ~290  | Survey files through conversation        |
| `02-the-safety-first-pattern.md`      | ~300  | Learn to require backups                 |
| `03-the-organization-workflow.md`     | ~320  | Design and execute categorization        |
| `04-batch-operations-workflow.md`     | ~340  | Transform tasks into scripts             |
| `05-search-and-discovery-workflow.md` | ~340  | Find lost files through description      |
| `06-capstone-your-file-toolkit.md`    | ~380  | Build personal prompt library            |

### Seven Principles Observed (Not Taught)

Students observe principles in agent behavior:

- **L01**: P1 (Bash - agent uses it), P7 (Observability - agent makes chaos visible)
- **L02**: P6 (Safety - agent creates backups), P3 (Verification - confirms success)
- **L03**: P5 (State - rules.md), P4 (Decomposition - test small first), P3 (Verify each step)
- **L04**: P2 (Code as Interface - agent creates scripts), P7 (Preview before action)
- **L05**: P1 (Bash tools combined), P7 (Search process visible)
- **L06**: All principles integrated, reflection and toolkit building

### Teaching Approach

Each lesson follows: Problem → Conversation → Observe → Verify → Pattern

**Key deliverable**: Prompt patterns, not bash knowledge.

---

## Key Decisions

1. **Complete rewrite** - Initial approach fundamentally misunderstood Part 2's purpose
2. **Multiple workflows** - Not stuck to one workflow; 5 practical mini-workflows + capstone
3. **Conversation-based lessons** - Show actual student-agent dialogue
4. **Observation-based learning** - Principles emerge from watching agent work
5. **Prompt patterns as deliverables** - Students build a toolkit of reusable prompts

---

## Files Deleted (Old Approach)

```
DELETED:
├── 01-survey-your-chaos.md
├── 02-safety-first-backup.md
├── 03-categorize-with-rules.md
├── 04-build-your-organizer-script.md
├── 05-run-with-verification.md
└── 06-capstone-clean-machine.md
```

## Files Created (Correct Approach)

```
apps/learn-app/docs/02-Applied-General-Agent-Workflows/06-file-processing/
├── README.md
├── 01-your-first-agent-workflow.md
├── 02-the-safety-first-pattern.md
├── 03-the-organization-workflow.md
├── 04-batch-operations-workflow.md
├── 05-search-and-discovery-workflow.md
└── 06-capstone-your-file-toolkit.md
```

---

## Lesson Learned

**Part 2 chapters teach workflows WITH General Agent**:

- OLD (wrong): Student types `ls -la`
- NEW (correct): Student asks "Show me what's in this folder"

Students learn to DIRECT and SUPERVISE, not to become bash scripters.

---

## Next Steps

1. Run validation-auditor for constitutional compliance
2. Generate summary files for each lesson
3. Review for MDX safety issues
