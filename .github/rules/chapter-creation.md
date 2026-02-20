---
paths:
  - "apps/learn-app/docs/**/*.md"
---

# Chapter Creation Protocol (Technical Chapters)

**For new technical chapters (Part 5-6), use `/sp.chapter`:**

## Two-Phase Approach

```
PHASE A: Build Expertise Skill First
├── 1. Fetch official docs (Context7, DeepWiki)
├── 2. Research community patterns (WebSearch)
├── 3. Build programmatic skill with:
│   ├── Persona (expert identity)
│   ├── Logic (decision trees)
│   ├── Context (prerequisites)
│   ├── MCP (tool integrations)
│   ├── Data/Knowledge (API patterns)
│   └── Safety & Guardrails
├── 4. Test skill on real project (TaskManager)
└── 5. Validate and commit skill

PHASE B: Create Chapter Content
├── /sp.specify → Interview/Clarification → Plan Mode (native)
├── Tasks (native TaskCreate) → content-implementer subagent
├── validators (parallel): educational-validator, factual-verifier
├── Update progress.md, mark tasks complete
└── /sp.git.commit_pr
```

## Why Skill-First?

| Without Skill              | With Skill         |
| -------------------------- | ------------------ |
| Hallucinated APIs          | Verified patterns  |
| Memory-based facts         | Researched facts   |
| Inconsistent examples      | Tested examples    |
| 6 rewrites (Ch 2 incident) | First-time quality |

## Skill Components Required

| Component   | Purpose                     |
| ----------- | --------------------------- |
| **Persona** | Expert identity and voice   |
| **Logic**   | Decision trees, when-to-use |
| **Context** | Prerequisites, setup        |
| **MCP**     | Tool integrations           |
| **Data**    | API patterns, examples      |
| **Safety**  | Guardrails, what to avoid   |

**Command**: `/sp.chapter "Chapter N: Title"`

---

## Skill-First Learning Pattern (Parts 4-6)

**The thesis**: "manufacture Digital FTEs powered by agents, specs, skills"

**The insight**: Traditional learning produces knowledge. Skill-First produces **assets**.

### Key Principles

| Traditional                                | Skill-First                                 |
| ------------------------------------------ | ------------------------------------------- |
| Learn technology → Maybe build skill later | Build skill FIRST → Learn to improve it     |
| Knowledge from AI memory (unreliable)      | Knowledge from **official docs** (reliable) |
| Assume prior state                         | **Clone fresh each chapter**                |
| Student "figures it out"                   | Student writes **LEARNING-SPEC.md**         |
| Random skill quality                       | **Grounded in documentation**               |
