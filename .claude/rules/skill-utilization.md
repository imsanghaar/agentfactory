# Skill Utilization

**Problem identified (2026-02-03)**: Skills are underutilized (24:1 subagent:skill ratio in logs).

## How Skills Work in Claude Code

1. **Auto-loading**: Skill names and descriptions are loaded with CLAUDE.md at session start
2. **Pattern matching**: When your task matches a skill description, INVOKE IT
3. **Three-level loading**:
   - L1: Metadata always loaded (name, description)
   - L2: Full SKILL.md loaded on-demand when invoked
   - L3: Supporting files (scripts/, references/) if needed

## When to Use Skills vs Subagents

| Use Case                   | Use Skill                          | Use Subagent             |
| -------------------------- | ---------------------------------- | ------------------------ |
| Quick lookup/generation    | ✅ `/fetch-library-docs fastapi`   | ❌ Overkill              |
| Content evaluation         | ✅ `/content-evaluation-framework` | ❌ Overkill              |
| Multi-file lesson creation | ❌ Too limited                     | ✅ `content-implementer` |
| Chapter planning           | ❌ Too limited                     | ✅ `chapter-planner`     |
| Fact-checking lesson       | ✅ `/fact-check-lesson`            | ❌ Unless complex        |

## Skill vs Subagent Hierarchy

**Skills** = Atomic operations (analysis, evaluation, generation, lookup)
**Subagents** = Orchestrated workflows (multi-file writes, complex state changes)

**Decision rule**: If the task writes multiple files or requires orchestration → Subagent. Otherwise → Skill.

## Available Skills (Check Before Spawning Subagent)

```
Code Review & Analysis:
- /spec-review                  → Single-pass spec-vs-implementation review
- /code-review:code-review      → PR code review

Content Quality:
- /content-evaluation-framework  → 6-category rubric scoring
- /content-refiner              → Fix Gate 4 failures
- /technical-clarity            → Grandma Test, jargon check
- /fact-check-lesson            → Verify factual claims

Pedagogy:
- /learning-objectives          → Generate measurable outcomes
- /concept-scaffolding          → Progressive learning sequences
- /ai-collaborate-teaching      → Three Roles Framework
- /skills-proficiency-mapper    → CEFR/Bloom's mapping

Assessment:
- /quiz-generator               → 50-question interactive quizzes
- /assessment-architect         → Certification exams

Research:
- /fetch-library-docs           → Official docs via Context7
- /session-intelligence-harvester → Extract session learnings

Creation:
- /skill-creator-pro            → Build new skills
- /skill-validator              → Validate skill quality
```

## Skill Invocation Rule

```
BEFORE spawning a subagent for a task:
1. Check if a skill exists for that task (see list above)
2. If skill exists → Use skill (faster, less overhead)
3. If skill insufficient → Then spawn subagent
```
