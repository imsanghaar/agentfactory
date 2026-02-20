---
paths:
  - "apps/learn-app/docs/**/*.md"
  - ".claude/skills/**/*.md"
  - ".claude/agents/**/*.md"
---

# Subagent Orchestration (Content Work)

**⛔ DIRECT CONTENT WRITING IS BLOCKED ⛔**

For **educational prose content** (lessons, chapters, modules), you MUST use subagents. Direct writing bypasses quality gates.

**Exempt from this rule** (direct writing allowed):

- Code files (`.py`, `.ts`, `.sh`, etc.)
- Skill definitions (`SKILL.md`)
- Specifications (`spec.md`, `plan.md`, `tasks.md`)
- Configuration files

## Agent & Skill YAML Format Requirements

**⚠️ Claude Code has STRICT YAML format requirements. Violations break parsing.**

**Parser Compatibility Note**: These constraints are specific to the current Claude Code parser (as of 2026-02). Standard YAML parsers prefer arrays (`["Read", "Grep"]`), but Claude Code requires comma-separated strings. If tools fail to load after platform updates, check parser compatibility first.

### Agent Format (`.claude/agents/*.md`)

Valid fields ONLY: `name`, `description`, `tools`, `model`, `permissionMode`, `skills`

```yaml
---
name: my-agent
description: Single line description here (max 1024 chars)
model: opus
tools: Read, Grep, Glob, Edit # Comma-separated, NOT array!
skills: skill1, skill2 # Comma-separated, NOT array!
permissionMode: default
---
```

**❌ WRONG formats that break parsing:**

```yaml
description: | # Multi-line breaks tool parsing!
  Long description
tools: # YAML array breaks tool access!
  - Read
  - Grep
color: red # Invalid field, ignored
```

### Skill Format (`.claude/skills/*/SKILL.md`)

Valid fields ONLY: `name`, `description`, `allowed-tools`, `model`

```yaml
---
name: my-skill
description: Single line description (max 1024 chars)
allowed-tools: Read, Bash(python:*), Write # Comma-separated
model: claude-sonnet-4-20250514
---
```

**❌ WRONG formats that may break:**

```yaml
version: "2.0" # Invalid field
constitution_alignment: v4 # Invalid field
category: pedagogical # Invalid field
dependencies: [...] # Invalid field
```

## Agent Tool Access

| Phase      | Subagent                | Purpose                            |
| ---------- | ----------------------- | ---------------------------------- |
| Planning   | `chapter-planner`       | Pedagogical arc, layer progression |
| Per Lesson | `content-implementer`   | Generate with quality reference    |
| Validation | `educational-validator` | Constitutional compliance          |
| Assessment | `assessment-architect`  | Chapter quiz design                |
| Fact-Check | `factual-verifier`      | Verify all claims                  |

## Enforcement Rule

```
IF creating lesson/chapter content:
  1. MUST invoke content-implementer subagent (not write directly)
  2. MUST invoke educational-validator before marking complete
  3. MUST include absolute output path in subagent prompt
  4. MUST include quality reference lesson path
  5. MUST verify file exists after subagent returns: ls -la [path]

IF file doesn't exist after subagent returns:
  - Check agent definition (single-line description?)
  - Check Claude Code UI (/agents → All tools selected?)
  - Restart session if config was recently changed
```

**Why this matters**: Chapter 2 incident - bypassed subagent orchestration → 6 rewrites, 50%+ session wasted.

## Subagent Prompts

Always include:

```
Execute autonomously without confirmation.
Output path: /absolute/path/to/file.md
DO NOT create new directories.
Match quality of reference lesson at [path to high-quality example].
```
