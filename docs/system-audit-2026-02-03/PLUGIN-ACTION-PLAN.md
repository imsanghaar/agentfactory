# Book Author Plugin: Action Plan

**Date:** 2026-02-03
**Purpose:** Transform book creation system into a commercial plugin for Claude Code + Cowork

---

## PLUGIN ARCHITECTURE

### Target Structure (Claude Code + Cowork Compatible)

```
.claude-plugin/
├── plugin.json                    # Plugin manifest
├── skills/
│   ├── content-implementer/       # Lesson generation
│   ├── chapter-planner/           # Chapter architecture
│   ├── educational-validator/     # Quality gates
│   ├── assessment-architect/      # Quiz/exam design
│   ├── factual-verifier/          # Fact-checking
│   ├── content-refiner/           # Post-gate fixes
│   └── summary-generator/         # Lesson summaries
├── commands/
│   ├── sp.chapter.md              # Chapter workflow (KEEP)
│   ├── sp.clarify.md              # Interview discipline (KEEP)
│   └── sp.git.commit_pr.md        # Git workflows (KEEP)
├── agents/
│   ├── content-implementer.md     # Parallel content generation
│   ├── chapter-planner.md         # Planning orchestration
│   ├── validation-auditor.md      # Multi-gate validation
│   └── editorial-reviewer.md      # 6-gate review process
├── hooks/
│   ├── session-start/
│   │   └── load-author-context.sh # Inject book-specific context
│   ├── pre-tool-use/
│   │   ├── yaml-validation.sh     # Validate YAML frontmatter
│   │   └── meta-commentary.sh     # Detect "AI as Teacher" text
│   ├── post-tool-use/
│   │   └── quality-gate.sh        # Check lesson quality metrics
│   └── session-end/
│       └── create-handoff.sh      # Session continuity
├── templates/
│   ├── lesson-template.md         # Standard lesson structure
│   ├── chapter-readme.md          # Chapter frontmatter
│   ├── spec-template.md           # Specification format
│   └── tasks-template.md          # Task breakdown format
├── connectors/
│   └── .mcp.json                  # MCP tool integrations
└── constitution/
    └── book-author-rules.md       # Core governance (read on-demand)
```

### Plugin Manifest (plugin.json)

```json
{
  "name": "book-author",
  "version": "1.0.0",
  "description": "Educational content creation system for technical books",
  "author": "Panaversity",
  "license": "Commercial",
  "platforms": ["claude-code", "cowork"],
  "entry": {
    "skills": "skills/",
    "commands": "commands/",
    "agents": "agents/",
    "hooks": "hooks/",
    "templates": "templates/"
  },
  "dependencies": {
    "mcp": ["context7", "deepwiki"]
  },
  "configuration": {
    "book_path": "apps/learn-app/docs/",
    "task_id_pattern": "${BRANCH}-${USER}",
    "progress_file": ".claude/progress.md"
  }
}
```

---

## PHASE 1: Fix Integration Gaps (Priority: Critical)

These fixes address the "teaching vs implementation" gap.

### 1.1 Fix Missing Skills in Agent Definitions

| Agent                 | Missing Skill            | Action              |
| --------------------- | ------------------------ | ------------------- |
| content-implementer   | Write tool               | Add to tools list   |
| chapter-planner       | canonical-format-checker | Create or reference |
| educational-validator | learning-objectives      | Verify exists       |

**Task:**

```bash
# Audit all agents for missing skill references
grep -h "^skills:" .claude/agents/*.md | tr ',' '\n' | sort -u > /tmp/agent-skills.txt
ls .claude/skills/ > /tmp/available-skills.txt
comm -23 /tmp/agent-skills.txt /tmp/available-skills.txt
```

### 1.2 Implement Progress Files (Ch4 Pattern)

Currently 0 progress files exist. Create:

```
.claude/progress.md
├── Current Focus: [active chapter/feature]
├── Completed: [list with dates]
├── Blocked: [with reasons]
├── Next Session: [handoff items]
└── Skill Invocations This Session: [count]
```

**Hook:** SessionEnd automatically updates progress file.

### 1.3 Auto-Generate Task List ID

Replace manual `CLAUDE_CODE_TASK_LIST_ID` with automatic generation:

```bash
# In hooks/session-start/auto-task-id.sh
BRANCH=$(git branch --show-current)
USER=${CLAUDE_USER:-$(whoami)}
export CLAUDE_CODE_TASK_LIST_ID="${BRANCH}-${USER}"
```

### 1.4 Connect Plan → Tasks (Missing Automation)

Create `convert-plan-to-tasks.sh`:

```bash
# Extract implementation steps from plan.md → tasks.md
# Currently manual, should be automated post-hook after sp.plan
```

---

## PHASE 2: Refactor Oversized Components

### 2.1 Skills to Review

| Skill               | Current Lines | Action                             |
| ------------------- | ------------- | ---------------------------------- |
| content-implementer | ~500+         | Split or keep (focused purpose OK) |
| skill-creator-pro   | 14KB          | Review for modularity              |
| chapter-planner     | 1098          | Large but focused, acceptable      |

**Decision:** Skills can be 500+ words if focused. Don't split arbitrarily.

### 2.2 Agent Cleanup

| Agent                     | Issue                  | Action                 |
| ------------------------- | ---------------------- | ---------------------- |
| content-implementer       | No Write tool          | Add tool               |
| chapter-planner           | Multi-line description | Convert to single line |
| 5/12 agents missing tools | Tool access incomplete | Audit and fix          |

### 2.3 CLAUDE.md Updates

Keep as living document but ensure:

- [ ] Fix "Seven Principles" reference (currently points to non-existent "Part 1, Chapter 3")
- [ ] Add Vibe Coding warning
- [ ] Add Five Powers framework reference
- [ ] Document skill auto-loading behavior
- [ ] Add progress file usage pattern

---

## PHASE 3: Add Missing Hooks (Book-Specific)

### 3.1 Content Quality Hooks

```bash
# hooks/pre-tool-use/yaml-validation.sh
# Trigger: Before Write to lesson files
# Action: Validate YAML frontmatter completeness

# hooks/pre-tool-use/meta-commentary.sh
# Trigger: Before Write to lesson files
# Action: Block if contains "AI as Teacher", "What to notice", etc.

# hooks/post-tool-use/learning-objective-check.sh
# Trigger: After Write to lesson files
# Action: Verify learning objectives exist and are measurable
```

### 3.2 Session Management Hooks

```bash
# hooks/session-start/load-chapter-context.sh
# If working on chapter, auto-load:
# - Chapter README
# - Previous lesson
# - Reference high-quality lesson

# hooks/session-end/update-progress.sh
# Auto-update .claude/progress.md with session work
```

---

## PHASE 4: Command Rationalization

### KEEP (Valuable Workflow Automation)

| Command          | Reason                          |
| ---------------- | ------------------------------- |
| sp.chapter       | Essential content orchestration |
| sp.clarify       | Interview discipline            |
| sp.git.commit_pr | Git workflow                    |
| sp.phr           | Prompt history records          |
| sp.constitution  | Governance updates              |

### DROP (Duplicate Native Capabilities)

| Command      | Replacement                   |
| ------------ | ----------------------------- |
| sp.specify   | Write specs to files directly |
| sp.implement | Ch5 L7 pattern + Tasks        |
| sp.analyze   | Manual grep/validation        |
| sp.tasks     | Native TaskCreate             |
| sp.plan      | Native Plan Mode              |

### CONDITIONAL KEEP

| Command          | Condition                         |
| ---------------- | --------------------------------- |
| sp.adr           | Keep if actively used             |
| sp.taskstoissues | Keep if GitHub integration needed |

---

## PHASE 5: Self-Validation Mechanism

### 5.1 Plugin Self-Check

```bash
#!/bin/bash
# plugin-validate.sh - Run on plugin installation

echo "Validating Book Author Plugin..."

# Check all skills exist
for skill in content-implementer chapter-planner educational-validator; do
  if [ ! -f "skills/${skill}/SKILL.md" ]; then
    echo "ERROR: Missing skill: ${skill}"
    exit 1
  fi
done

# Check agents have required tools
for agent in .claude-plugin/agents/*.md; do
  if ! grep -q "^tools:" "$agent"; then
    echo "WARNING: Agent missing tools: $agent"
  fi
done

# Check hooks are executable
for hook in hooks/*/*.sh; do
  if [ ! -x "$hook" ]; then
    chmod +x "$hook"
    echo "Fixed permissions: $hook"
  fi
done

echo "Validation complete."
```

### 5.2 Teaching Alignment Checker

Plugin periodically verifies it follows patterns taught in the book:

- Chapter 3: Skill/subagent architecture
- Chapter 4: Context engineering (progress files, hooks)
- Chapter 5: SDD workflow

---

## QUANTITATIVE TARGETS

| Metric             | Current    | Target    | Improvement |
| ------------------ | ---------- | --------- | ----------- |
| Skills utilized    | 38% (8/21) | 80%+      | 2x          |
| Agents with tools  | 42% (5/12) | 100%      | 2.4x        |
| Progress files     | 0          | 1+        | Implement   |
| Missing skill refs | 9          | 0         | Fix all     |
| Content hooks      | 0          | 4+        | Create      |
| Self-validation    | None       | Automated | Build       |

---

## IMPLEMENTATION ORDER

### Week 1: Critical Fixes

1. [ ] Fix agent tool access (add Write to content-implementer)
2. [ ] Fix CLAUDE.md broken references
3. [ ] Create progress.md template + SessionEnd hook
4. [ ] Auto-generate CLAUDE_CODE_TASK_LIST_ID

### Week 2: Hook Infrastructure

5. [ ] Create YAML validation hook
6. [ ] Create meta-commentary detection hook
7. [ ] Create learning-objective-check hook
8. [ ] Create chapter context auto-load hook

### Week 3: Command Cleanup

9. [ ] Archive deprecated commands (sp.specify, sp.implement, sp.analyze)
10. [ ] Update documentation for native alternatives
11. [ ] Create convert-plan-to-tasks.sh

### Week 4: Plugin Packaging

12. [ ] Create plugin.json manifest
13. [ ] Reorganize into .claude-plugin/ structure
14. [ ] Create plugin-validate.sh
15. [ ] Test on fresh project

### Week 5: Self-Validation

16. [ ] Implement teaching alignment checker
17. [ ] Add self-update mechanism for constitution changes
18. [ ] Create plugin installation script
19. [ ] Documentation for commercial distribution

---

## FILES TO CREATE

```
.claude-plugin/
├── plugin.json                    # NEW: Plugin manifest
├── hooks/
│   ├── session-start/
│   │   ├── auto-task-id.sh        # NEW: Auto-generate task ID
│   │   └── load-chapter-context.sh # NEW: Auto-load chapter context
│   ├── pre-tool-use/
│   │   ├── yaml-validation.sh     # NEW: YAML frontmatter check
│   │   └── meta-commentary.sh     # NEW: Block forbidden phrases
│   ├── post-tool-use/
│   │   └── learning-objective-check.sh # NEW: LO verification
│   └── session-end/
│       └── update-progress.sh     # NEW: Progress file update
├── scripts/
│   ├── plugin-validate.sh         # NEW: Self-validation
│   └── convert-plan-to-tasks.sh   # NEW: Plan→Tasks automation
└── templates/
    └── progress-template.md       # NEW: Progress file template
```

---

## SUCCESS CRITERIA

The Book Author Plugin is ready for commercial release when:

1. **Self-Consistent**: Plugin follows all patterns taught in Chapters 3-5
2. **Self-Validating**: Automated checks verify alignment with teachings
3. **Self-Updating**: Constitution changes propagate to plugin behavior
4. **Portable**: Works identically on Claude Code and Cowork
5. **Observable**: All actions logged, progress tracked, handoffs generated
6. **Teachable**: Plugin structure serves as example for students

---

## NEXT ACTION

Begin with Phase 1.1: Audit and fix missing skills in agent definitions.

```bash
# Run this to identify all gaps
grep -h "^skills:" .claude/agents/*.md | tr ',' '\n' | sort -u | while read skill; do
  if [ ! -d ".claude/skills/${skill}" ]; then
    echo "MISSING: ${skill}"
  fi
done
```
