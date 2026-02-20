# Golden Questions: Chapter 3 (General Agents — Claude Code CLI)

10 hand-written ideal questions demonstrating the quality standard for a practical-tool chapter. These questions test practical competence with Claude Code CLI features using in-domain scenarios.

---

## Q1. [Scenario Analysis] [Concept: Hooks vs Instructions]

A developer needs every commit message to follow a `type(scope): description` convention. They could add the rule to CLAUDE.md, create a skill, or configure a hook.

Which approach guarantees the convention is enforced on every commit?

A) Add the convention format to CLAUDE.md project instructions
B) Create a commit-message skill with the format template
C) Configure a pre-commit hook that validates and rejects non-conforming messages
D) Add the convention to the team's README documentation

**Answer:** C
**Reasoning:** Hooks are deterministic — they execute on every event regardless of whether Claude follows instructions. CLAUDE.md and skills are probabilistic (Claude usually follows them but can deviate). A hook that rejects bad commits guarantees enforcement. README is purely informational with no enforcement mechanism.

---

## Q2. [Scenario Analysis] [Concept: Subagent Context Isolation]

A team uses Claude Code to process sensitive customer data in one subagent and generate marketing copy in another. They notice the marketing subagent occasionally references specific customer names from the data processing context.

What architectural issue does this reveal?

A) The subagents share a conversation context when they should be isolated
B) The marketing subagent needs more restrictive permission settings
C) Customer data should be encrypted before the data processing subagent accesses it
D) The model is hallucinating customer names from its training data

**Answer:** A
**Reasoning:** Subagents should have isolated contexts — each receives only its assigned inputs (concept map, reference files). If marketing output contains customer names, the contexts are leaking. This isn't a permissions issue (B), encryption issue (C), or hallucination (D) — it's a context isolation failure.

---

## Q3. [Concept Relationship] [Concept: Skills + MCP Integration]

A developer's skill calls an external API via an MCP server to fetch project data. The MCP server goes down. The skill invocation fails completely — no fallback, no partial result.

What does this reveal about the relationship between skills and MCP?

A) Skills can function independently without MCP by using built-in tools
B) MCP provides optional enrichment — skills should degrade gracefully without it
C) Skills that depend on MCP inherit its availability constraints as hard dependencies
D) The skill should cache MCP responses to avoid runtime failures

**Answer:** C
**Reasoning:** When a skill's logic requires MCP data, the MCP server becomes a hard dependency. The skill can't produce its output without the external data. (A) is true for some skills but not this one. (B) describes ideal design but doesn't match the observed behavior. (D) is a mitigation strategy, not what the failure reveals about the relationship.

---

## Q4. [Critical Evaluation] [Concept: Settings Hierarchy]

A team sets `model: haiku` in their project-level `.claude/settings.json` for cost control. A developer overrides to `model: opus` in their user-level settings for complex refactoring work. They're confused that Claude still uses haiku.

Why does the override fail?

A) User-level settings only apply when no project-level settings exist
B) Project-level settings override user-level settings in the hierarchy
C) Model selection requires enterprise-level permission to change
D) The user-level file has a syntax error preventing the override

**Answer:** B
**Reasoning:** In Claude Code's settings hierarchy, project-level settings take precedence over user-level settings (more specific scope wins). The developer's user-level override is superseded by the project's explicit model choice. This isn't about missing settings (A), enterprise permissions (C), or syntax errors (D) — it's the hierarchy working as designed.

---

## Q5. [Scenario Analysis] [Concept: CLAUDE.md Project Context]

Two developers join a team that uses Claude Code. Developer A reads the onboarding docs and memorizes the team's conventions. Developer B skips onboarding entirely but clones the repo with its CLAUDE.md file.

When both ask Claude to write tests, whose tests match the team's conventions?

A) Developer A's, because they internalized the conventions
B) Developer B's, because CLAUDE.md automatically provides project context to Claude
C) Both equally, because Claude infers conventions from existing test files
D) Neither, because conventions require explicit prompting each time

**Answer:** B
**Reasoning:** CLAUDE.md is read automatically by Claude Code, providing project context (naming patterns, test conventions, commit formats) without the developer needing to know or specify them. Developer A's knowledge helps them personally but doesn't affect Claude's behavior. Claude doesn't reliably infer conventions from files (C), and CLAUDE.md eliminates the need for repeated prompting (D).

---

## Q6. [Transfer Application] [Concept: Small Reversible Decomposition]

A DevOps engineer needs to migrate 50 microservices from Docker Compose to Kubernetes. Each service has different dependencies, health checks, and scaling requirements.

Applying the principle of small reversible decomposition, what migration strategy minimizes risk?

A) Migrate all 50 services simultaneously with a rollback plan for the entire cluster
B) Migrate one service at a time, validating it works on K8s before starting the next
C) Group services by dependency chains and migrate each group together
D) Run both systems in parallel for a month, then cut over all at once

**Answer:** B
**Reasoning:** Small reversible decomposition means making one change, verifying it works, then proceeding. One service at a time is the smallest unit that's independently verifiable. (A) is the opposite — a big-bang migration. (C) is better than (A) but still groups multiple changes. (D) delays risk rather than decomposing it.

---

## Q7. [Scenario Analysis] [Concept: Ralph Wiggum Loop]

A developer wants Claude Code to continuously monitor a log file and restart a failing service whenever specific error patterns appear — without human intervention between iterations.

Which Claude Code feature enables this autonomous loop pattern?

A) A hook that triggers on log file changes
B) The Ralph Wiggum loop with completion criteria tied to error resolution
C) A skill that reads the log file when manually invoked
D) A subagent dedicated to log monitoring with periodic polling

**Answer:** B
**Reasoning:** The Ralph Wiggum loop enables continuous autonomous execution where Claude keeps working until completion criteria are met. This matches the "monitor and act without human intervention" requirement. Hooks (A) trigger on Claude Code events, not external file changes. Skills (C) require manual invocation. Subagents (D) don't have a built-in polling mechanism.

---

## Q8. [Concept Relationship] [Concept: Verification + Observability]

A team uses Claude Code for automated refactoring. After each refactoring step, Claude runs tests and reports results. The tests pass, but the team later discovers Claude silently removed error handling code that wasn't covered by tests.

What gap between verification and observability does this expose?

A) Tests verify correctness but don't observe what was changed — the team couldn't see the removals
B) Observability failed because Claude didn't log its actions
C) Verification was too narrow (only tests) when it should include code review
D) Both verification and observability worked correctly — the tests simply need expanding

**Answer:** A
**Reasoning:** Verification (tests passing) confirmed the code still works but didn't reveal WHAT changed. Observability (seeing what happened) would show that error handling was removed. The gap is: passing tests ≠ understanding changes. (B) misidentifies the problem as logging. (C) is a solution, not an identification of the gap. (D) denies the gap exists.

---

## Q9. [Critical Evaluation] [Concept: Compiling MCP to Skills]

A team compiled their frequently-used MCP database queries into a skill for faster access. The skill works well for months. Then the database schema changes — new columns, renamed tables. The compiled skill now returns errors, but the raw MCP connection to the updated database works fine.

What is the fundamental weakness of the compiled-skill approach here?

A) Skills execute faster than MCP but sacrifice real-time schema discovery
B) The skill should have been written to query the schema dynamically
C) Compiled skills create a frozen snapshot that diverges from the live MCP source over time
D) The team should have updated the skill when the schema changed

**Answer:** C
**Reasoning:** Compiling MCP to a skill trades flexibility for speed/reliability. The skill captured the schema at compile time. When the source changes, the compiled version is stale. This is the fundamental trade-off: frozen snapshot vs. live connection. (A) identifies a speed benefit but not the core weakness. (B) and (D) are solutions, not the weakness identification the question asks for.

---

## Q10. [Scenario Analysis] [Concept: Permission Model / Trust Gradualism]

A solo developer uses Claude Code with full autonomy (no approval prompts). They join a regulated fintech team where Claude Code requires approval for every file write, shell command, and git operation.

What aspect of Claude Code's permission model enables this difference?

A) The team uses a different Claude Code subscription tier with stricter defaults
B) Project-level settings can restrict permissions regardless of user preferences, enforcing team-wide constraints
C) The solo developer has a less restrictive CLAUDE.md file
D) Claude Code automatically detects regulated industries and adjusts permissions

**Answer:** B
**Reasoning:** Claude Code's permission model allows project-level settings to enforce constraints that override individual user preferences. This is trust gradualism — the team operates at a more restrictive trust level than a solo developer. (A) is wrong — permission granularity isn't tied to subscription. (C) confuses CLAUDE.md (instructions) with permission settings. (D) is fabricated — there's no automatic industry detection.

---

## Quality Standards Demonstrated

These questions show:

1. **Domain relevance** — All scenarios involve development workflows, Claude Code features, or adjacent technical decisions
2. **Practical competence** — Answering correctly requires understanding how tools work in practice, not just definitions
3. **Concise writing** — Scenarios are 2-3 sentences; stems are direct questions; options are one idea each
4. **Plausible distractors** — Wrong options represent real misconceptions, not obviously absurd choices
5. **Concept grounding** — Each question maps to a specific chapter concept and tests its application
