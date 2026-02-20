# Gap Analysis: Current System vs Book Author Plugin

**Date:** 2026-02-03 (Updated)
**Status:** Corrected analysis - tools omission = ALL tools

---

## CORRECTED: Agent Tool Access

**Claude Code behavior**: When `tools:` field is OMITTED, agent gets ALL tools (not none).

### Agents with ALL tools (no `tools:` field = full access):

| Agent                | Purpose                 | Status           |
| -------------------- | ----------------------- | ---------------- |
| content-implementer  | Main content generation | ✅ Has ALL tools |
| chapter-planner      | Planning orchestration  | ✅ Has ALL tools |
| assessment-architect | Quiz/exam design        | ✅ Has ALL tools |
| monorepo-agent       | Monorepo operations     | ✅ Has ALL tools |
| pedagogical-designer | Learning design         | ✅ Has ALL tools |
| super-orchestra      | Multi-agent workflow    | ✅ Has ALL tools |
| validation-auditor   | Multi-gate validation   | ✅ Has ALL tools |

### Agents with RESTRICTED tools (explicit `tools:` field):

| Agent                        | Restricted To                         | Potential Gap                    |
| ---------------------------- | ------------------------------------- | -------------------------------- |
| editorial-reviewer           | Read, Grep, Glob, Edit, Bash          | Missing WebSearch for fact-check |
| factual-verifier             | Read, Grep, Glob, WebSearch, WebFetch | Missing Write (can't fix errors) |
| educational-validator        | TBD                                   | Check if missing tools           |
| lesson-deletion-orchestrator | TBD                                   | Check if missing tools           |
| spec-architect               | TBD                                   | Check if missing tools           |

**Note:** Restricted tools may be intentional (principle of least privilege) or may limit agent capability.

---

## CRITICAL: Missing Skills

**9 skills referenced by agents but don't exist:**

| Missing Skill                  | Referenced By  | Action                            |
| ------------------------------ | -------------- | --------------------------------- |
| assessment-builder             | Unknown agent  | Create or remove reference        |
| book-scaffolding               | Unknown agent  | Create or remove reference        |
| exercise-designer              | Unknown agent  | Create or remove reference        |
| fetching-library-docs          | Unknown agent  | Create (for Context7 integration) |
| monorepo-team-lead             | monorepo-agent | Create for monorepo support       |
| monorepo-workflow              | monorepo-agent | Create for workflow patterns      |
| nx-monorepo                    | monorepo-agent | Create for Nx operations          |
| researching-with-deepwiki      | Unknown agent  | Create (for DeepWiki integration) |
| session-intelligence-harvester | Unknown agent  | Create or remove reference        |

**Available skills not referenced (potential waste):**

- docker
- docx
- notebooklm-slides
- pptx
- seo-aeo-best-practices
- skill-creator-pro
- skill-validator
- upload-chapter-slides

---

## UTILIZATION METRICS

| Metric            | Value      | Target | Gap                        |
| ----------------- | ---------- | ------ | -------------------------- |
| Agents with tools | 42% (5/12) | 100%   | 7 agents need tools        |
| Skills referenced | 21         | -      | -                          |
| Skills existing   | 21         | -      | -                          |
| Skills MISSING    | 9          | 0      | 9 to create or dereference |
| Skills unused     | 8          | 0      | Review for deprecation     |

---

## IMMEDIATE ACTIONS (Priority Order)

### 1. Fix content-implementer (BLOCKER)

This is the main content generation agent and has NO tools.

```yaml
# Add to .claude/agents/content-implementer.md
tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
```

### 2. Fix chapter-planner (HIGH)

Planning agent cannot read codebase.

```yaml
# Add to .claude/agents/chapter-planner.md
tools: Read, Grep, Glob, Task
```

### 3. Fix validation-auditor (HIGH)

Validation agent cannot check files.

```yaml
# Add to .claude/agents/validation-auditor.md
tools: Read, Grep, Glob, WebSearch
```

### 4. Fix assessment-architect (MEDIUM)

Assessment creation limited.

```yaml
# Add to .claude/agents/assessment-architect.md
tools: Read, Grep, Glob, Write, Edit
```

### 5. Create fetching-library-docs skill (MEDIUM)

For Context7 MCP integration.

### 6. Create researching-with-deepwiki skill (MEDIUM)

For DeepWiki MCP integration.

### 7. Clean up orphan skill references (LOW)

Remove references to non-existent skills from agent definitions.

---

## VERIFICATION COMMANDS

After fixes, run:

```bash
# Verify all agents have tools
for f in .claude/agents/*.md; do
  if ! grep -q "^tools:" "$f"; then
    echo "MISSING TOOLS: $(basename $f)"
  fi
done

# Verify all referenced skills exist
grep -h "^skills:" .claude/agents/*.md | tr ',' '\n' | \
  sed 's/skills://g' | sed 's/^[[:space:]]*//g' | grep -v '^$' | \
  sort -u | while read skill; do
    if [ ! -d ".claude/skills/${skill}" ]; then
      echo "MISSING SKILL: ${skill}"
    fi
  done
```

---

## SUMMARY

The book creation system has significant integration gaps:

1. **58% of agents cannot access tools** - They are defined but non-functional
2. **9 skills referenced but don't exist** - Agent definitions point to phantoms
3. **8 skills exist but unused** - Potential waste or documentation gap

These gaps explain why:

- Subagent:skill ratio is 24:1 (skills underutilized)
- Content quality requires multiple rewrites
- "Eating your own dog food" failure

**Priority:** Fix agent tool access first (especially content-implementer), then resolve missing skills.
