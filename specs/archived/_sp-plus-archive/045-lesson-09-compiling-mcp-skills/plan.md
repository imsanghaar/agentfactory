# Implementation Plan: Lesson 09 — Compiling MCP to Skills

**Feature ID**: 045-lesson-09-compiling-mcp-skills
**Version**: 1.0.0
**Created**: 2025-12-19
**Chapter**: 5 (Claude Code Features & Workflows)
**Lesson**: 09
**Duration**: 25 minutes
**Spec**: `/specs/045-lesson-09-compiling-mcp-skills/spec.md`

---

## I. Executive Summary

Lesson 09 teaches students to reduce MCP token bloat (8,000+ tokens per server) by 80-98% through a three-step process: **(1) Introspect** the MCP server to understand its tools, **(2) Compile** tool definitions into a lean SKILL.md + scripts, and **(3) Validate** token reduction through measurement.

The lesson is **Layer 2 (AI Collaboration)** with built-in **Three Roles** (invisible):
- **AI as Teacher**: Claude teaches introspection pattern and suggests skill structure
- **Student as Teacher**: Student provides context about which tools they actually use
- **Convergence**: Together they optimize toward token-efficient skill that works

The lesson directly applies knowledge from Lessons 04-06 (skills format) and Lesson 08 (MCP servers), making it a consolidation point where students see practical MCP optimization in action.

---

## II. Pedagogical Analysis

### Chapter Position & Prerequisites

| Component | Details |
|-----------|---------|
| **Chapter** | 5: Claude Code Features & Workflows |
| **Lesson Position** | 09 (new, inserted between MCP Integration and Subagents) |
| **Prerequisites** | Lessons 05 (concept behind skills), 06 (agent skills SKILL.md format), 08 (MCP integration) |
| **Proficiency Target** | B1-B2 (intermediate, applying multiple prior concepts) |
| **Cognitive Load** | 5 new concepts within B1-B2 limit |

### Layer 2 Implementation (AI Collaboration)

**Primary Layer**: Layer 2 (AI Collaboration with Three Roles)

**Foundation from Prior Layers**:
- Layer 1 (Lessons 04-06): Students understand skills, SKILL.md format, how skills work
- Layer 1 (Lesson 08): Students understand MCP, have working MCP servers installed

**Three Roles Implementation** (INVISIBLE to students—experienced through action):

1. **AI as Teacher**: Claude teaches introspection pattern and skill compilation
2. **Student as Teacher**: Student provides domain context (which tools they use)
3. **Convergence**: Together they optimize the compiled skill through iteration

**Why Framework Stays Invisible**:
- Don't label roles: No "AI as Teacher", no "now you're the student"
- Show through action: "Ask Claude to introspect", "Tell Claude which tools you use"
- Reflection at end: "What improved through iteration?" (student recognizes pattern without labels)

### Cognitive Load Analysis

**New Concepts Introduced** (count: 5, within B1-B2 limit):
1. **MCP Token Bloat** — Why loading all tool definitions wastes tokens
2. **Introspection Pattern** — How to ask Claude to extract tool definitions
3. **Code Execution Pattern** — Alternative to direct MCP tool calls
4. **Skill Compilation** — Converting introspected definitions to SKILL.md + scripts
5. **Progressive Disclosure Optimization** — Loading only needed tools, when needed

**Assessment**: 5 concepts × moderate complexity = within B1-B2 cognitive load ✓

---

## III. Content Structure (Section-by-Section)

### Section 1: The Problem — MCP Token Bloat (3 minutes)

**Learning Objective**: Analyze and articulate why MCP servers consume tokens wastefully

**Teaching Modality**: Narrative explanation with concrete examples and citations

**Key Content Points**:
1. **The Sentry Example** (Armin Ronacher) — 8,000 tokens at startup
2. **The Compounding Problem** — Multiple MCPs × data volume = massive token consumption
3. **The Waste Insight** — Most tokens fund unused tools
4. **Source Attribution** — Anthropic blog, Armin Ronacher article, SmartScope

**Validation Checkpoint**: Student can articulate why MCP token bloat exists

---

### Section 2: The Solution — Code Execution Pattern (3 minutes)

**Learning Objective**: Understand code execution pattern as alternative to direct MCP

**Teaching Modality**: Conceptual explanation with comparison table

**Key Content Points**:
1. **The Code Execution Pattern** — Write code locally, not call MCP tools directly
2. **Four-Step Workflow** — Introspect → Compile → Generate → Optimize
3. **Token Reduction Claim** — 80-98% savings (150,000 → 2,000 tokens)
4. **Why This Works** — Skill (~100 tokens) + local script (0 tokens) vs all tool definitions

**Validation Checkpoint**: Student can explain how code execution reduces tokens

---

### Section 3: Hands-On — Introspect Your MCP Server (5 minutes)

**Learning Objective**: Successfully extract MCP server tool definitions using Claude

**Teaching Modality**: Step-by-step guided exercise with exact prompts

**Introspection Workflow**:
1. **Choose MCP** — Context7 (beginner) or Playwright (advanced)
2. **Ask Claude to Introspect** — Use provided prompt to list tools
3. **Analyze Output** — Identify core tools and token costs
4. **Select Scope** — Choose 3-5 tools to compile

**Expected Output**: Structured list of tools with descriptions and token estimates

**Validation Checkpoint**: Artifact showing introspected tools exists in Claude conversation

**Three Roles Embedded**:
- **AI as Teacher**: Claude shows what tools exist and their costs
- **Student as Teacher**: "I only need X tools for my work"
- **Convergence**: "OK, let's build a skill around those X tools"

---

### Section 4: Hands-On — Compile to Skill (10 minutes)

**Learning Objective**: Create working compiled skill using skill-creator

**Teaching Modality**: Guided exercise with iteration loop (Three Roles in action)

**Compilation Steps**:
1. **Prepare Introspection Data** — From Section 3
2. **Use skill-creator** — Provide introspection data and use case
3. **Generate SKILL.md** — Matches Lesson 06 format exactly
4. **Create Supporting Script** — TypeScript/Python/Shell for execution
5. **Test Skill Discovery** — Verify Claude recognizes the skill
6. **Iterate** — Claude refines, student tests, convergence improves

**Expected Artifacts**:
```
.claude/skills/[skill-name]/
├── SKILL.md
└── scripts/
    └── [implementation file]
```

**Canonical Format Alignment**:
- Directory: `.claude/skills/[skill-name]/`
- File: `SKILL.md` with YAML frontmatter (name, description, version)
- Format: Matches Lesson 06 exactly (When to Use, Procedure, Output Format, Quality Criteria)

**Validation Checkpoint**: File exists, Claude discovers skill, format matches Lesson 06

**Three Roles Embedded**:
- **Iteration 1**: Claude generates, student tests
- **Iteration 2**: Student finds issue or improvement opportunity
- **Iteration 3**: Claude refines, together they converge on optimized skill

---

### Section 5: Hands-On — Validate Token Reduction (5 minutes)

**Learning Objective**: Measure token reduction through before/after comparison

**Teaching Modality**: Guided measurement exercise with calculation

**Validation Workflow**:
1. **Establish Baseline** — Use MCP directly, note token count
2. **Test Optimized** — Use compiled skill, note token count
3. **Calculate Reduction** — (Baseline - Optimized) / Baseline × 100%
4. **Document Results** — Create comparison table
5. **Reflect** — Answer reflection questions about effort vs savings

**Expected Output**: Comparison table showing ≥30% reduction (realistic for beginners)

**Validation Checkpoint**: Artifact documenting token savings exists

**Three Roles Embedded**:
- **AI as Teacher**: Claude explains measurement method
- **Student as Teacher**: Student tests with their actual workflow
- **Convergence**: "Your use case saves X% tokens—worth the effort"

---

### Section 6: Decision Framework — When to Compile vs Direct MCP (2 minutes)

**Learning Objective**: Apply decision logic to determine when compilation is justified

**Teaching Modality**: Decision matrix with real-world scenarios

**Decision Matrix**:

| Scenario | Recommendation | Reasoning |
|----------|----------------|-----------|
| One-off query | Direct MCP | Not worth 15 min compilation |
| Repeated workflow (3+ times/week) | Compile to skill | Savings justify effort |
| High-token tool definitions (8,000+) | Compile to skill | Problem large enough to fix |
| Rapidly changing API | Direct MCP | Maintenance burden too high |
| Privacy-sensitive data | Compile (local execution) | Data runs locally, not through context |
| Team collaboration | Compile to skill | Shared skill benefits everyone |
| Large data processing (100K+ tokens) | Compile to skill | Token leakage compounds |

**Decision Flowchart** (verbal):
```
Do you use this MCP?
├─ No → Skip it
└─ Yes → Is it repeated 3+ times/week?
    ├─ Yes → Compile
    └─ No → Estimate token cost
        ├─ >1,000/week → Compile
        └─ <1,000/week → Direct MCP OK
```

**Validation Checkpoint**: Student can apply matrix to hypothetical scenarios

---

### Section 7: Try With AI — Exploration Prompts (Open-Ended)

**Learning Objective**: Extend learning through guided discovery

**Prompts** (students choose one or more):
1. **Extend to Second MCP** — Compile multiple MCPs, question unified vs separate skills
2. **Optimize Existing Skill** — Implement caching, lazy loading, performance improvements
3. **Create Skill Suite** — Design coordinated skills for complex workflow (bridges to Lesson 10)
4. **Apply Decision Framework** — Analyze inventory of MCPs and prioritize compilation
5. **Plan MCP Evolution** — Maintenance strategy when MCPs change or versions update

---

## IV. Three Roles Framework Implementation (Invisible)

### Pattern 1: Introspection (Section 3)

**Flow**:
1. Claude introspects and teaches: "Here are all tools, here's their cost"
2. Student teaches: "I only need these 3 tools"
3. Convergence: "OK, we'll focus on those 3"

**Student Experience** (no role labels):
- Claude taught me what was in the MCP
- I taught Claude what I actually need
- Together we narrowed scope

### Pattern 2: Skill Compilation (Section 4)

**Flow**:
1. Claude generates initial SKILL.md and scripts
2. Student says: "Let me test this with my actual workflow..."
3. Claude refines based on feedback
4. Convergence: Neither party designed alone

### Pattern 3: Validation (Section 5)

**Flow**:
1. Claude teaches measurement method
2. Student tests with their workflow
3. Claude reflects: "That's significant because..."
4. Convergence: Agreement on success

### Meta-Commentary Prohibition

**Forbidden**:
- "AI as Teacher: Claude explains the introspection pattern"
- "What to notice: AI is teaching you something new"
- "AI learned from your feedback"

**Required Instead**:
- "Ask Claude to introspect the MCP"
- "Tell Claude which tools you actually use"
- "Reflection: What changed as you worked together?"

---

## V. Canonical Format Alignment

### SKILL.md Format Reference (Lesson 06)

The compiled skill MUST match Lesson 06 format exactly:

**Directory Structure**:
```
.claude/skills/[skill-name]/
└── SKILL.md    ← Required
└── scripts/    ← Optional (but used here)
```

**SKILL.md Content**:
```markdown
---
name: "[skill-name]"
description: "[Use formula: action + input + output + triggers]"
version: "1.0.0"
---

# [Skill Title]

## When to Use
- [Trigger 1]
- [Trigger 2]

## Procedure
1. [Step 1]
2. [Step 2]

## Output Format
[Expected format]

## Quality Criteria
[Standards maintained]
```

**Validation Checklist**:
- [ ] File location: `.claude/skills/[skill-name]/SKILL.md`
- [ ] YAML frontmatter: name, description, version
- [ ] Description uses formula: Action + Input + Output + Triggers
- [ ] Sections: "When to Use", "Procedure", "Output Format"
- [ ] No meta-commentary about how the skill works

---

## VI. Hands-On Exercise Details

### Exercise 1: Introspection (Section 3)

**Prompts to Provide**:

```
I have the [Context7/Playwright] MCP server installed.
Please introspect it and show me:
1. Complete list of tools (name, description, parameters)
2. For each tool, estimate tokens consumed
3. Which tools are high-token
4. Which are good candidates for optimization
```

**Troubleshooting**:
| Issue | Solution |
|-------|----------|
| "MCP not found" | Run `claude mcp list` to verify; re-run Lesson 08 setup |
| Output truncated | Ask: "Continue with remaining tools" |
| Token estimates seem high | Normal—tool definitions are verbose; this justifies compilation |

---

### Exercise 2: Skill Compilation (Section 4)

**Prompts to Provide**:

```
Using the skill-creator skill:

Create a skill that compiles [MCP] into token-efficient format.

Input:
- MCP Tools: [paste introspection list]
- Primary use case: [e.g., "API documentation lookup"]
- Scope: Focus on these tools only: [list 3-5]
- Script platform: [Python / TypeScript]

Output should be:
1. SKILL.md with lean description (~100 tokens max)
2. Implementation script (Python/TypeScript)
3. Installation instructions

Optimize for:
- Minimal token consumption
- Clear "When to Use" section
- Local execution where possible
```

**Expected Artifacts**:
```
.claude/skills/[skill-name]/
├── SKILL.md
└── scripts/
    └── [implementation.ts or .py]
```

**Troubleshooting**:
| Issue | Solution |
|-------|----------|
| skill-creator not available | Go back to Lesson 04 and create it |
| Script syntax errors | Use compatible language (Node.js for TS, Python 3.9+ for Py) |
| Skill not discovered | Check file path: `.claude/skills/[name]/SKILL.md` |

---

### Exercise 3: Token Validation (Section 5)

**Measurement Workflow**:

1. **Baseline Prompt**:
```
Use [MCP directly] to [task].
Note approximate token count.
```

2. **Optimized Prompt**:
```
Use [compiled-skill] to [task].
Note approximate token count.
```

3. **Calculation**:
```
Reduction % = (Baseline - Optimized) / Baseline × 100
```

4. **Documentation Template**:
```markdown
## Token Reduction Results

Task: [Description]

| Approach | Tokens |
|----------|--------|
| Direct MCP | X |
| Compiled Skill | Y |
| **Reduction** | **Z%** |
```

---

## VII. Assessment Strategy

### Formative Checkpoints

| Section | Checkpoint | Success Criteria |
|---------|-----------|------------------|
| 1 | Understanding MCP bloat | Articulates token waste problem |
| 2 | Conceptual grasp | Explains code execution pattern |
| 3 | Introspection skill | Lists tools with token estimates |
| 4 | Compilation | Working skill in correct location |
| 5 | Measurement | Shows ≥30% token reduction |
| 6 | Decision making | Applies matrix to scenarios |

### Summative Assessment

**Capstone Options**:

**Option A**: Compile second MCP server
- Full workflow demonstration
- Token reduction comparison
- Explain when to use vs direct MCP

**Option B**: Optimize and share
- Document optimization process
- Create usage guide
- Share with classmates

**Option C**: Prioritized roadmap
- Inventory all MCPs
- Apply decision matrix
- Create compilation roadmap

---

## VIII. Cross-Lesson Verification

### Lesson 06 Alignment

- [x] SKILL.md format matches Lesson 06 exactly
- [x] Directory structure: `.claude/skills/[name]/SKILL.md`
- [x] YAML frontmatter fields: name, description, version
- [x] Description formula from Lesson 06
- [x] Sections: "When to Use", "Procedure", "Output Format"

**Key Reference**:
`/apps/learn-app/docs/02-AI-Tool-Landscape/05-claude-code-features-and-workflows/06-agent-skills.md`

### Lesson 08 Alignment

- [x] MCP tool names and capabilities match Lesson 08
- [x] Setup commands from Lesson 08 still work
- [x] Security considerations referenced from Lesson 08

**Key Commands**:
- `claude mcp add --transport stdio playwright npx @playwright/mcp@latest`
- `claude mcp add --transport stdio context7 npx @upstash/context7-mcp`

### Lesson 04 Skill-Creator Reference

- [x] skill-creator skill available from Lesson 04
- [x] Can handle MCP compilation prompts
- [x] Output format matches requirements

---

## IX. Implementation Notes

### Known Challenges

**Challenge**: MCP availability varies (Context7 ≈ 5 tools, Playwright ≈ 12 tools)
**Mitigation**: Use Context7 as primary (simpler), Playwright as extension (advanced)

**Challenge**: Token estimation accuracy is approximate (±20-30%)
**Mitigation**: Focus on relative reduction, not exact numbers

**Challenge**: Three Roles framework must stay invisible
**Mitigation**: Grep for forbidden phrases; refocus on action not exposition

**Challenge**: Canonical format drift from Lesson 06
**Mitigation**: Compare SKILL.md example against Lesson 06 format before finalizing

---

## X. Time Breakdown

| Section | Activity | Duration |
|---------|----------|----------|
| 1 | MCP Token Bloat | 3 min |
| 2 | Code Execution Pattern | 3 min |
| 3 | Introspection Exercise | 5 min |
| 4 | Compilation Exercise | 10 min |
| 5 | Validation Exercise | 5 min |
| 6 | Decision Framework | 2 min |
| **Core Total** | — | **28 min** |
| 7 | Try With AI (optional) | 5-15 min |

---

## XI. Success Indicators

By end of Lesson 09, student will have:

✅ **Understanding**: Can articulate MCP token bloat problem and code execution solution

✅ **Application**: Can introspect MCP, compile skill, measure token reduction

✅ **Judgment**: Recognizes when AI teaches, provides context, sees iteration improve design

✅ **Integration**: Compiled skill works in correct location, matches Lesson 06 format

✅ **Decision-Making**: Can decide when to compile vs use direct MCP

---

## XII. Extension Pathways

**For Advanced**: Skill suites, performance optimization, MCP evolution strategy (Try With AI)

**For Struggling**: Simplified task (Context7 only), step-by-step walkthrough, work from template

---

## XIII. Ready for Content Implementation

This plan is ready when:
- ✅ Each section has learning objective, teaching modality, key points, validation
- ✅ Hands-on exercises have step-by-step instructions and exact prompts
- ✅ Cross-lesson references verified (Lesson 06 format, Lesson 08 MCPs)
- ✅ Three Roles woven invisibly (no meta-commentary)
- ✅ Assessment strategy includes formative checkpoints and summative capstone
- ✅ Sufficient detail for content writer, clear enough to debug during testing

**Status**: Ready for content implementation
**Next Step**: Write lesson markdown using this plan as detailed guide
