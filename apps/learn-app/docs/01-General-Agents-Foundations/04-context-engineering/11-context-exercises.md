---
title: "Context Engineering Exercises"
practice_exercise: ch4-context
sidebar_label: "Context Exercises"
sidebar_position: 11
chapter: 4
lesson: 11
duration_minutes: 240

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Hands-on practice applying Lessons 1-10 context engineering techniques through 14 guided exercises and 3 capstones"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Context Diagnosis"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can identify all four context rot types and classify sections of a CLAUDE.md as signal, noise, or poisoned"

  - name: "Context Architecture"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital-Content-Creation"
    measurable_at_this_level: "Student can map information items to the correct context tool (CLAUDE.md, Skills, Subagents, Hooks) and calculate token budget impact"

  - name: "Context Engineering"
    proficiency_level: "A2"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can build a production-quality agent with optimized context, persistence, memory, and multi-agent isolation"

learning_objectives:
  - objective: "Diagnose context rot types and measure their impact on agent quality"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student audits a broken CLAUDE.md and produces a categorized rot report with baseline quality scores"

  - objective: "Apply signal-vs-noise audit and context architecture design to improve agent performance"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Student reduces a bloated CLAUDE.md to ~400 words, redistributes content to Skills/Hooks, and measures quality improvement"

  - objective: "Engineer persistent, lifecycle-managed, memory-enhanced agents with clean multi-agent isolation"
    proficiency_level: "A2"
    bloom_level: "Create"
    assessment_method: "Student builds a production agent that survives /clear, manages context zones, maintains quality across 20+ turns, and coordinates multiple agents without pollution"

cognitive_load:
  new_concepts: 0
  assessment: "Pure application — all concepts taught in L01-L10"

differentiation:
  extension_for_advanced: "Capstone C: Forensics challenge diagnosing 3 failing agents with different context problems"
  remedial_for_struggling: "Focus on Modules 1-3 (diagnosis and optimization) before attempting persistence and multi-agent modules"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 4
  session_title: "Capstone: Production-Quality Agents"
  key_points:
    - "This is a measurement-driven exercise lab — students apply every technique from Lessons 1-10 and score the results using a consistent rubric at each stage"
    - "The Contract Review Agent starts broken (missing red flags, contradicting itself, forgetting requirements) and improves measurably as each context engineering technique is applied"
    - "The progression from Module 1 (diagnosis) through Module 7 (multi-agent coordination) mirrors the chapter's lesson sequence, reinforcing each concept through practice"
    - "No new concepts are introduced — this is pure application of the full context engineering toolkit learned throughout the chapter"
  misconceptions:
    - "Students think exercises are optional supplementary practice — this is the chapter closer where concepts become measurable skills, and the quality scores prove the techniques work"
    - "Students skip measurement steps because they seem tedious — the before/after scores ARE the learning, showing quantified impact of each technique"
    - "Students try to jump to advanced modules without completing diagnosis modules first — Module 1-3 (rot diagnosis, signal audit, architecture) are prerequisites for everything after"
  discussion_prompts:
    - "After running the same three test tasks at each stage, which technique produced the largest measurable improvement? Was it the one you expected?"
    - "How would you adapt the Contract Review Agent exercises to your own professional domain?"
  teaching_tips:
    - "Emphasize that every module follows the same pattern: apply technique, then measure — this measurement discipline is the meta-skill being taught"
    - "Have students download the exercise files at the start of class to avoid setup delays — the ZIP contains all starter files and instructions per module"
    - "The three capstones at the end are the real assessment — Capstone A (build your own domain agent) is the minimum, Capstone C (forensics) is the stretch goal"
    - "Budget at least 4 hours across multiple sessions — this is a 240-minute exercise set that demonstrates multi-session work in practice"
  assessment_quick_check:
    - "After Module 3, what was your agent's quality score compared to the broken starting state?"
    - "Which context engineering technique produced the largest single improvement in your measurements?"
    - "Describe one thing you would do differently if you started the exercise lab over from scratch"
---

# Context Engineering Exercises: The Context Lab

You have spent ten lessons learning how context engineering works. You know that context rots when left unmanaged, that most CLAUDE.md files contain more noise than signal, that position inside the context window determines how much attention an instruction receives, and that multi-session work requires explicit persistence. You understand the theory. Now it is time to prove the theory works by measuring it.

These exercises use a single evolving project: a **Contract Review Agent** that starts broken and gets progressively better as you apply each context engineering technique. The agent reviews legal contracts and produces risk assessments. In its starting state, it misses obvious red flags, contradicts its own earlier findings, and forgets critical requirements mid-session. By Module 7, the same agent will catch every issue, maintain consistency across sessions, and coordinate multiple specialist reviewers without contamination. The difference between the broken version and the production version is not a better model or more data. It is better context engineering.

Every module follows the same pattern: apply a technique, then measure the result. You will run the same three contract review tasks at each stage and score the output using a consistent rubric. This measurement discipline is the most important thing you will learn. Context engineering is not hand-waving about "better prompts." It is an engineering discipline where you can quantify the impact of every change you make.

:::info Download Exercise Files
**[Download Context Engineering Exercises (ZIP)](https://github.com/imsanghaar/claude-code-context-exercises/releases/latest/download/context-exercises.zip)**

After downloading, unzip the file. Each module has its own folder with an `INSTRUCTIONS.md` and any starter files you need.

If the download link doesn't work, visit the [repository releases page](https://github.com/imsanghaar/claude-code-context-exercises/releases) directly.
:::

---

## How the Context Lab Works

Unlike standalone exercises where each problem is independent, the Context Lab is a **single project that evolves across all 7 modules**. You start with a broken Contract Review Agent and apply one context engineering technique per module. After each technique, you re-run the same three benchmark tasks and score the results. This lets you measure exactly how much each technique contributes.

**The workflow for every module:**

1. **Read the module folder** from the `context-exercises/` directory
2. **Read INSTRUCTIONS.md** inside the folder for setup steps and starter files
3. **Read the walkthrough below** for context on what you are practicing and why
4. **Apply the technique** (Exercise X.1) — make the specific change described
5. **Measure the result** (Exercise X.2) — re-run benchmark tasks, score output, compare to previous module
6. **Record your scores** in the tracking spreadsheet provided — this is your evidence of improvement
7. **Reflect** on what changed and why

You do not need to complete all 7 modules in one sitting. Each module takes 20-40 minutes. But you must complete them **in order** because each module builds on the previous one.

---

## Tool Guide

- **Claude Code** — Best for all exercises. Terminal-based interaction lets you test context changes, run /clear, manage sessions, and observe context behavior directly.
- **Cowork** — Suitable for the contract review tasks themselves, but Claude Code is required for exercises involving /clear, /compact, progress files, and multi-agent patterns.

---

## The Scoring Framework

Every time you run the three benchmark tasks, score each output on four criteria using a 1-5 scale:

| Criteria          | 1 (Poor)                                  | 3 (Adequate)                                      | 5 (Excellent)                                                          |
| ----------------- | ----------------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------- |
| **Completeness**  | Misses more than half the contract issues | Catches major issues, misses minor ones           | Identifies all issues including subtle patterns                        |
| **Accuracy**      | Multiple incorrect risk assessments       | Mostly correct, 1-2 errors                        | All risk levels correctly assessed with reasoning                      |
| **Consistency**   | Contradicts itself within the same review | Minor inconsistencies between sections            | Internally consistent, references its own earlier findings             |
| **Actionability** | Vague warnings like "review this section" | Identifies issues but recommendations are generic | Specific recommendations with clause references and suggested language |

**Maximum score per task:** 20 (4 criteria x 5 points)
**Maximum score per benchmark run:** 60 (3 tasks x 20 points)

The starter agent typically scores 25-35 out of 60. By Module 7, students routinely reach 50-58.

---

## Module 1: Context Rot

> **Technique:** Diagnosing the four types of context rot (Lesson 1)
>
> **What you will learn:** How to identify accumulation, contradiction, staleness, and poisoning in a real CLAUDE.md — and why each type degrades agent performance differently.

<ExerciseCard id="1.1" title="Rot Audit" />

### Exercise 1.1 — Rot Audit

**The Setup:**
Open the `module-1-context-rot/exercise-1.1-rot-audit/` folder. You will find a `starter-agent/` directory containing a CLAUDE.md, several rules files, and a skills directory. This is your Contract Review Agent in its broken starting state. The CLAUDE.md is 650 lines long and was accumulated over months of ad-hoc additions by multiple team members.

**Your Task:**
Read the entire CLAUDE.md and categorize every section into one of four rot types:

- **Accumulation** — content that was added over time without removing what it replaced (duplicate rules, overlapping instructions)
- **Contradiction** — instructions that conflict with each other (e.g., "always use formal tone" vs. "keep it casual and accessible")
- **Staleness** — content that was accurate when written but is now outdated (references to deprecated tools, old team members, changed processes)
- **Poisoning** — content that actively causes wrong behavior (incorrect examples, misleading heuristics, rules that produce bad output)

Produce a rot report: a table listing each section, its rot type, and the specific harm it causes. Count the total instructions and estimate what percentage are signal vs. noise.

**What to Expect:**
Most students find the starter CLAUDE.md contains 15-25% signal. The rest is rot. The most dangerous category is usually poisoning — instructions that look helpful but actively degrade output quality. Staleness is the most common by volume.

**Reflection Questions:**

1. Which rot type was hardest to identify? Why?
2. Did you find any instructions that seemed like signal but were actually poisoning? What made them dangerous?
3. How would you prevent each rot type from accumulating in the first place?

---

<ExerciseCard id="1.2" title="Baseline Measurement" />

### Exercise 1.2 — Baseline Measurement

**The Setup:**
Open the `module-1-context-rot/exercise-1.2-baseline-measurement/` folder. You will find three benchmark contract files and a scoring template. The benchmark contracts are designed to test different aspects of review quality: Contract A has obvious liability issues, Contract B has subtle inconsistencies between clauses, and Contract C has standard terms that should NOT be flagged (testing for false positives).

**Your Task:**
Run all three benchmark contracts through the starter agent (with the broken CLAUDE.md from Exercise 1.1). For each output, score it on the 4-criteria rubric. Record your scores in the provided tracking spreadsheet. This is your **Module 1 baseline** — every future module will be compared against these scores.

**What to Expect:**
Typical baseline scores range from 25-35 out of 60. The agent usually catches the obvious issues in Contract A but misses the subtle inconsistencies in Contract B and produces false positives on Contract C. Consistency scores tend to be lowest because contradictory CLAUDE.md instructions produce contradictory output.

**Reflection Questions:**

1. Which scoring criterion had the lowest score? Can you trace it back to a specific rot type from Exercise 1.1?
2. Did the agent produce any false positives on Contract C? What in the CLAUDE.md caused it to over-flag?
3. What is your prediction for how much improvement Module 2 will deliver?

---

## Module 2: Signal vs. Noise

> **Technique:** The 4-question signal audit (Lesson 2)
>
> **What you will learn:** How to separate actionable instructions from noise, and how dramatically a lean CLAUDE.md outperforms a bloated one.

<ExerciseCard id="2.1" title="Four-Question Audit" />

### Exercise 2.1 — Four-Question Audit

**The Setup:**
Open the `module-2-signal-noise/exercise-2.1-four-question-audit/` folder. You will find the CLAUDE.md from Module 1 plus the 4-question audit framework. The four questions are: (1) Would Claude ask about this if not told? (2) Is this specific enough to act on? (3) Does this change Claude's default behavior? (4) Can compliance be verified?

**Your Task:**
Apply the 4-question audit to every instruction in the CLAUDE.md. Remove everything that fails all four questions. Compress everything that passes some questions but not all. Keep only content where all four questions answer "yes." Your target is a CLAUDE.md of approximately 400 words — down from the original 650 lines.

Be ruthless. "Write high-quality reviews" fails all four questions (Claude already tries to write high-quality output, it is not specific, it does not change defaults, and compliance cannot be verified). "Flag any clause where liability exceeds 2x contract value" passes all four (Claude would not apply this threshold unprompted, it is specific, it changes behavior, and you can check compliance).

**What to Expect:**
Students typically reduce the CLAUDE.md from 650 lines to 40-60 lines. The process is uncomfortable — it feels like you are throwing away important information. The measurement in Exercise 2.2 will show that less is more.

**Reflection Questions:**

1. How many instructions survived all four questions? What percentage of the original?
2. What was the hardest instruction to cut? Did it feel important even though it failed the audit?
3. Where did you move the content you removed? Delete, external file, or skill?

---

<ExerciseCard id="2.2" title="Quality Comparison" />

### Exercise 2.2 — Quality Comparison

**The Setup:**
Open the `module-2-signal-noise/exercise-2.2-quality-comparison/` folder. Use the same three benchmark contracts from Module 1, but now run them through the agent with your optimized CLAUDE.md.

**Your Task:**
Re-run all three benchmark contracts. Score each output on the same 4-criteria rubric. Compare every score to your Module 1 baseline. Calculate the improvement per criterion and overall.

**What to Expect:**
Students typically see a 8-15 point improvement (out of 60) from signal optimization alone. The biggest gains are usually in Consistency (removing contradictions eliminates contradictory output) and Actionability (specific instructions produce specific recommendations). Completeness may stay flat or even dip slightly — you will recover it in Module 3 when you redistribute removed content to the right tools.

**Reflection Questions:**

1. Which criterion improved most? Does that match what you removed in Exercise 2.1?
2. Did any criterion get worse? Why might removing content reduce completeness?
3. If you could only keep 10 instructions in CLAUDE.md, which 10 from your optimized version would you choose?

---

## Module 3: Context Architecture

> **Technique:** Mapping content to the right context tool (Lesson 3)
>
> **What you will learn:** How to distribute information across CLAUDE.md, Skills, Hooks, and Subagents so that each piece lives where it gets the most attention at the lowest token cost.

<ExerciseCard id="3.1" title="Tool Mapping" />

### Exercise 3.1 — Tool Mapping

**The Setup:**
Open the `module-3-architecture/exercise-3.1-tool-mapping/` folder. You will find the content you removed in Module 2 plus a tool mapping worksheet. The worksheet lists each context tool (CLAUDE.md Zones 1/2/3, Skills, Hooks, Subagents, External Files) with its characteristics: when it is loaded, how many tokens it consumes, and what it is best for.

**Your Task:**
Take every piece of content you removed from CLAUDE.md in Module 2 and map it to the correct tool:

- **Zone 1 (top of CLAUDE.md):** Critical constraints that must always apply — the 3-5 rules that should never be forgotten
- **Zone 2 (middle of CLAUDE.md):** Reference material consulted when relevant
- **Zone 3 (bottom of CLAUDE.md):** Workflow triggers and session initialization protocols
- **Skills:** Domain expertise that should be loaded on demand (e.g., specific legal review checklists)
- **Hooks:** Dynamic injections based on what the agent is currently doing (e.g., inject relevant precedent when analyzing liability clauses)
- **Subagents:** Specialized tasks that benefit from isolated context (e.g., separate financial analysis from legal analysis)
- **External Files:** Stable reference material that rarely changes (e.g., company contract templates, approved clause language)

Create the actual files: write the skills, define the hook logic, specify the subagent prompts. Your Contract Review Agent should now have a multi-file context architecture, not just a single CLAUDE.md.

**What to Expect:**
Most students distribute content roughly: 30% stays in CLAUDE.md (across all three zones), 25% becomes skills, 15% becomes hook triggers, 10% defines subagent scope, and 20% moves to external reference files. The exact distribution depends on the content, but a common mistake is keeping too much in CLAUDE.md because it "feels safer."

**Reflection Questions:**

1. Which content was hardest to place? What made the decision difficult?
2. Did you find content that did not belong in any tool? What did you do with it?
3. How many tokens does your CLAUDE.md consume now vs. Module 1? What is the percentage reduction?

---

<ExerciseCard id="3.2" title="Token Budget" />

### Exercise 3.2 — Token Budget

**The Setup:**
Open the `module-3-architecture/exercise-3.2-token-budget/` folder. You will find a token budget calculator and instructions for estimating the token cost of your architecture.

**Your Task:**
Calculate the token budget for two scenarios:

1. **Module 1 architecture** (everything in CLAUDE.md): Estimate the token cost at session start, at turn 10, and at turn 30.
2. **Module 3 architecture** (distributed across tools): Estimate the same three measurements, accounting for skills loaded on-demand, hooks that fire conditionally, and subagents that run in isolated contexts.

Produce a comparison table showing: tokens consumed at each measurement point, percentage of context window used, and estimated attention quality based on the utilization curves from Lesson 6.

**What to Expect:**
The distributed architecture typically uses 40-60% fewer tokens at session start and degrades much more slowly over a 30-turn session. The most dramatic difference appears at turn 30, where the monolithic approach is often at 65-75% utilization (degraded attention) while the distributed approach stays at 35-45% (full attention).

**Reflection Questions:**

1. At which measurement point is the difference between architectures largest? Why?
2. Which tool contributes the most token savings? Skills (on-demand loading) or Subagents (isolated contexts)?
3. What is the theoretical maximum number of turns before each architecture hits the 70% degradation threshold?

---

## Module 4: Persistence

> **Technique:** Task DAGs and tacit knowledge extraction (Lessons 4-5)
>
> **What you will learn:** How to make your agent's work survive session boundaries — so that /clear does not destroy accumulated understanding.

<ExerciseCard id="4.1" title="Tasks and Knowledge" />

### Exercise 4.1 — Tasks and Knowledge

**The Setup:**
Open the `module-4-persistence/exercise-4.1-tasks-and-knowledge/` folder. You will find a multi-session contract review scenario: a complex 50-page vendor agreement that requires analysis across multiple sessions. The scenario includes session transcripts showing how a naive agent loses context between sessions.

**Your Task:**
Design two persistence artifacts for the Contract Review Agent:

1. **Task DAG:** Decompose the 50-page contract review into a dependency graph of tasks. Which sections can be reviewed independently? Which require understanding from earlier sections (e.g., definitions in Section 1 affect interpretation of liability in Section 15)? Express this as a task file with dependencies and completion status.

2. **Tacit Knowledge File:** Read the session transcripts and extract every piece of domain knowledge the agent discovered during review — interpretation of ambiguous clauses, relationships between sections, client-specific preferences. Encode these as explicit rules in a knowledge file that a fresh session can read.

**What to Expect:**
The task DAG typically has 8-12 tasks with 3-5 dependency chains. Students often underestimate dependencies — Section 15 (liability) depends not just on Section 1 (definitions) but also Section 8 (scope of work) because liability limits reference deliverable categories. The tacit knowledge file usually captures 10-15 rules that were implicit in the session transcripts.

**Reflection Questions:**

1. How many dependency chains did you identify? Were any circular (A depends on B depends on A)?
2. Which tacit knowledge rules were hardest to extract? Were they buried in casual observations or explicit decisions?
3. Could a new team member use your task DAG and knowledge file to continue the review without reading the session transcripts?

---

<ExerciseCard id="4.2" title="Survival Test" />

### Exercise 4.2 — Survival Test

**The Setup:**
Open the `module-4-persistence/exercise-4.2-survival-test/` folder. You will find instructions for the survival test: run a partial contract review session, execute /clear, then resume and verify continuity.

**Your Task:**
Conduct this three-phase test:

1. **Phase 1 (Pre-clear):** Start a session with your Contract Review Agent (using the Module 3 architecture + Module 4 persistence files). Review Contract A partially — complete 3 of the task DAG items. Note specific findings and decisions.

2. **Phase 2 (The clear):** Execute `/clear` to wipe the conversation context. This simulates a session boundary.

3. **Phase 3 (Post-clear):** Start a new message in the same session. The agent should read the task DAG and knowledge file to reconstruct state. Verify: Does it know which tasks are complete? Does it remember the findings from Phase 1? Can it continue the review without re-doing work?

Score the post-clear session on the same 4-criteria rubric and compare to pre-clear quality.

**What to Expect:**
With well-designed persistence files, post-clear quality typically scores within 2-3 points of pre-clear quality. The most common failure is losing tacit knowledge — findings that were discovered during Phase 1 but not captured in the knowledge file. Students who wrote thorough knowledge files in Exercise 4.1 see nearly perfect continuity.

**Reflection Questions:**

1. What information was lost after /clear? Was it captured in your persistence files or only in conversation history?
2. How long did it take the agent to "warm up" after /clear? What determined warmup time?
3. If you could add one more persistence artifact to improve continuity, what would it be?

---

## Module 5: Lifecycle

> **Technique:** Context zone monitoring and compaction strategy (Lessons 6-7)
>
> **What you will learn:** How to keep your agent performing well across long sessions by actively managing context utilization and knowing when to compact.

<ExerciseCard id="5.1" title="Zone Monitoring" />

### Exercise 5.1 — Zone Monitoring

**The Setup:**
Open the `module-5-lifecycle/exercise-5.1-zone-monitoring/` folder. You will find a 25-turn contract review session script and a zone monitoring worksheet. The worksheet tracks context utilization at each turn: how much is system prompt, CLAUDE.md, conversation history, tool outputs, and reserve.

**Your Task:**
Execute the 25-turn session with your Contract Review Agent. At turns 1, 5, 10, 15, 20, and 25, estimate the context composition:

- **Zone 1 (System + CLAUDE.md):** Approximately stable across turns
- **Zone 2 (Conversation history):** Grows with each turn
- **Zone 3 (Tool outputs):** Spikes when reading files, then gets compressed
- **Reserve:** Shrinks as other zones grow

Plot these on the utilization curve. Identify the turn where utilization crosses 60% (caution zone) and predict when it would cross 70% (degradation zone).

Add a progress file that the agent updates every 5 turns with: current task state, key findings since last update, and context health assessment.

**What to Expect:**
Most agents cross 60% utilization between turns 15-20, depending on how many files they read. The progress file adds 200-400 tokens per update but pays for itself by enabling effective compaction later. Students often discover that tool outputs (reading contract sections) are the biggest context consumer — not conversation history.

**Reflection Questions:**

1. At which turn did utilization cross 60%? Was it sooner or later than you expected?
2. What was the biggest context consumer — conversation history, tool outputs, or something else?
3. How would you redesign the workflow to delay the 60% threshold?

---

<ExerciseCard id="5.2" title="Compaction Strategy" />

### Exercise 5.2 — Compaction Strategy

**The Setup:**
Open the `module-5-lifecycle/exercise-5.2-compaction-strategy/` folder. You will find compaction instruction templates and a comparison framework.

**Your Task:**
Design and test three compaction strategies for your Contract Review Agent at the 60% threshold:

1. **Naive compaction:** `/compact Keep the important stuff`
2. **Structured compaction:** `/compact Preserve: [specific decisions, findings, current task]. Discard: [exploration, intermediate reasoning, resolved questions].`
3. **Progress-file compaction:** Update the progress file first, then `/compact Preserve only what is NOT in claude-progress.txt. The progress file is the source of truth for decisions and findings.`

Run each strategy and continue the review for 10 more turns. Score the output quality at turn 35 (10 turns after compaction) using the 4-criteria rubric.

**What to Expect:**
Naive compaction typically loses 30-50% of critical context. Structured compaction preserves most decisions but may lose rationale. Progress-file compaction consistently produces the best results because the critical context is safely persisted outside the context window before compaction discards it. The quality scores after compaction usually tell the story clearly.

**Reflection Questions:**

1. Which compaction strategy preserved the most quality? By how many points?
2. What did naive compaction lose that you did not expect?
3. When should you compact proactively (before hitting 60%) vs. reactively (after hitting 60%)?

---

## Module 6: Memory

> **Technique:** Designing a memory corpus for domain expertise (Lesson 8)
>
> **What you will learn:** How to build a persistent memory layer that makes your agent smarter over time — so turn 20 reviews are better than turn 1 reviews.

<ExerciseCard id="6.1" title="Memory Corpus" />

### Exercise 6.1 — Memory Corpus

**The Setup:**
Open the `module-6-memory/exercise-6.1-memory-corpus/` folder. You will find a set of 10 previously reviewed contracts with annotated findings. These represent the "experience" your agent should learn from. You will also find a memory corpus template.

**Your Task:**
Design a memory corpus for the contract review domain. For each of the 10 previously reviewed contracts, extract:

- **Patterns:** Recurring clause structures that indicate risk (e.g., "unlimited liability language often appears in Section 12 of vendor agreements")
- **Precedents:** Specific decisions and their rationale (e.g., "rejected auto-renewal clause in Contract #3 because client requires explicit opt-in")
- **Heuristics:** Rules of thumb learned from experience (e.g., "when indemnification exceeds 3x contract value, flag for executive review")

Organize these into a searchable memory structure. Define the injection strategy: which memories should be injected via hooks (PreToolUse), which should live in the knowledge file (always available), and which should be retrieved on-demand from external files.

**What to Expect:**
Students typically extract 25-40 memories from the 10 contracts. The hardest part is deciding granularity — a memory that is too broad ("watch out for liability clauses") is noise, while one that is too narrow ("Contract #3, Section 12.4(b) had a typo") is not transferable. The best memories are pattern-level: specific enough to act on, general enough to apply to new contracts.

**Reflection Questions:**

1. How many memories did you extract? How many were patterns vs. precedents vs. heuristics?
2. Which injection strategy did you choose for each type? Why?
3. How would you handle memory conflicts — when a new contract contradicts a previously learned pattern?

---

<ExerciseCard id="6.2" title="Drift Measurement" />

### Exercise 6.2 — Drift Measurement

**The Setup:**
Open the `module-6-memory/exercise-6.2-drift-measurement/` folder. You will find instructions for a controlled comparison test.

**Your Task:**
Run a controlled experiment:

1. **Turn 1 review:** Start a fresh session with your memory-enhanced agent. Review a new benchmark contract (Contract D, provided in the folder). Score the output.
2. **Turn 20 review:** Continue the session for 19 more turns of contract review work (the folder provides review tasks to fill the turns). Then review Contract D again at turn 20. Score the output.
3. **Compare:** Did the agent's review improve, degrade, or stay the same between turn 1 and turn 20?

The key question: does your memory injection system maintain quality as the session progresses, or does accumulated conversation history dilute the injected memories?

**What to Expect:**
With well-designed memory injection, turn 20 quality should be equal to or better than turn 1 — the agent has more context from the session's work. Without proper injection, turn 20 quality typically degrades by 3-5 points as conversation history crowds out memory content. Students who implemented deduplication in their hook design see the most stable results.

**Reflection Questions:**

1. Did turn 20 quality improve, degrade, or stay the same compared to turn 1? By how many points?
2. If quality degraded, what caused it? Too many memories injected? Conversation history diluting signal?
3. How would you modify your injection strategy to ensure quality never degrades below the turn 1 baseline?

---

## Module 7: Isolation

> **Technique:** Multi-agent pipeline with clean context boundaries (Lesson 9)
>
> **What you will learn:** How to split a complex review into parallel specialist agents that produce better results than a single generalist — by keeping each agent's context clean and focused.

<ExerciseCard id="7.1" title="Pipeline Design" />

### Exercise 7.1 — Pipeline Design

**The Setup:**
Open the `module-7-isolation/exercise-7.1-pipeline-design/` folder. You will find a complex contract (Contract E) that requires expertise in three domains: legal terms, financial analysis, and operational feasibility. You will also find a pipeline design template.

**Your Task:**
Split the Contract Review Agent into a multi-agent pipeline:

1. **Orchestrator:** Receives the contract, delegates to specialists, synthesizes findings
2. **Legal Reviewer:** Analyzes legal terms, liability, compliance — with legal-specific CLAUDE.md and skills
3. **Financial Analyst:** Analyzes pricing, payment terms, financial risk — with finance-specific context
4. **Operations Assessor:** Analyzes implementation timeline, resource requirements, feasibility — with operations-specific context

For each agent, define:

- Its isolated CLAUDE.md (only instructions relevant to its specialty)
- Its return format (structured summary, not raw analysis)
- Shared constraints (baseline contract terms all agents must assume)

For the orchestrator, define:

- How it delegates (what context each specialist receives)
- How it synthesizes (what format it expects back)
- How it handles conflicts between specialists

**What to Expect:**
The biggest design challenge is the orchestrator's synthesis prompt. Students who simply concatenate specialist outputs get confused results. Students who define structured return formats (Summary, Key Findings, Risk Level, Recommendations) and synthesize by category get clean, coherent final reports. The shared constraints document is often overlooked but critical — without it, specialists make incompatible assumptions.

**Reflection Questions:**

1. How much context overlap exists between your three specialists? Could you reduce it further?
2. What happens if the Legal Reviewer flags a clause as high-risk but the Financial Analyst says the financial terms are favorable? How does your orchestrator resolve this?
3. How many tokens does each specialist consume compared to the single-agent approach?

---

<ExerciseCard id="7.2" title="Clean vs. Dirty" />

### Exercise 7.2 — Clean vs. Dirty

**The Setup:**
Open the `module-7-isolation/exercise-7.2-clean-vs-dirty/` folder. You will find instructions for a head-to-head comparison test.

**Your Task:**
Run Contract E through two architectures and compare:

1. **Dirty slate:** Give one agent all three specialist contexts (legal + financial + operations) in a single CLAUDE.md. Run the full review. Score the output.
2. **Clean slate:** Use your multi-agent pipeline from Exercise 7.1. Run the same review. Score the output.

Compare scores across all four criteria. Pay special attention to Accuracy (does the dirty-slate agent conflate legal and financial concepts?) and Consistency (does it maintain clear boundaries between analysis domains?).

**What to Expect:**
The clean-slate pipeline typically scores 5-10 points higher than the dirty-slate single agent. The largest gains are in Accuracy and Consistency — isolated contexts prevent the cross-contamination that happens when legal, financial, and operational reasoning share the same attention space. Completeness often improves too, because specialists catch domain-specific issues that a generalist overlooks.

**Reflection Questions:**

1. Where did the clean-slate pipeline outperform the dirty-slate agent most? Does this match the theory from Lesson 9?
2. Did the dirty-slate agent make any errors that were clearly caused by context contamination — where information from one domain corrupted analysis in another?
3. What is the overhead cost (latency, complexity) of the multi-agent pipeline? Is the quality improvement worth it?

---

## Capstone Projects

> **Choose one (or more). These combine all seven modules — no step-by-step guidance provided.**

Capstones are different from the module exercises. There are no guided walkthroughs — you design the entire approach yourself. Each project requires applying multiple context engineering techniques together to solve a realistic problem.

<ExerciseCard id="A" title="Your Domain Agent" />

### Capstone A — Your Domain Agent

Open the `capstone-A-your-domain-agent/` folder. You will find a project template and self-assessment rubric.

**The Challenge:**
Build a production-quality agent for **your own profession or domain** using all seven context engineering techniques. This is not a contract review agent — it is an agent that does work you actually need done. A teacher might build a lesson planning agent. A marketer might build a campaign review agent. A developer might build a code review agent.

Apply every technique from the Context Lab:

- Audit for rot and optimize signal-to-noise ratio
- Distribute context across the right tools
- Design persistence that survives session boundaries
- Implement lifecycle management with compaction strategy
- Build a memory corpus from your domain expertise
- If applicable, design multi-agent isolation for complex workflows

**Deliverable:** A complete agent directory with CLAUDE.md, skills, hooks, persistence files, and memory corpus. Include a self-assessment scoring your agent on the Context Engineering Assessment Rubric (below).

---

<ExerciseCard id="B" title="Context Relay" />

### Capstone B — Context Relay

Open the `capstone-B-context-relay/` folder. You will find a 3-session project specification.

**The Challenge:**
Execute a complex project across three separate Claude Code sessions. The project requires building a small application (specified in the folder). The constraint: each session must start fresh (/clear between sessions). Your only continuity comes from the persistence artifacts you create.

- **Session 1:** Requirements analysis and architecture design. Persist everything needed for Session 2.
- **Session 2:** Implementation. Read Session 1's artifacts, build the application, persist state for Session 3.
- **Session 3:** Testing and refinement. Read Session 2's artifacts, verify the implementation, fix issues.

**Scoring:** Compare the quality of Session 3's output to what a single uninterrupted session would produce. Effective context engineering should make the multi-session version nearly as good as the single-session version.

---

<ExerciseCard id="C" title="Forensics Challenge" />

### Capstone C — Forensics Challenge

Open the `capstone-C-forensics-challenge/` folder. You will find three broken agents, each failing for a different context engineering reason.

**The Challenge:**
Diagnose each agent's failure without being told what is wrong. For each agent:

1. Run it on a test task and observe the failure mode
2. Audit its context artifacts (CLAUDE.md, skills, hooks, persistence files)
3. Identify the root cause using context engineering principles
4. Fix the agent and verify the fix with a re-test

The three agents have different problems — one is a rot issue, one is an architecture issue, and one is an isolation issue. You must determine which is which.

**Scoring:** For each agent, assess: (1) Did you correctly identify the failure type? (2) Was your root cause analysis accurate? (3) Did your fix resolve the problem without introducing new issues?

---

## The Context Engineering Assessment Rubric

Use this rubric to evaluate your overall context engineering skill after completing the modules. This is also the rubric for Capstone A.

| Criteria                    | Beginner (1)                                | Developing (2)                               | Proficient (3)                                                                      | Advanced (4)                                                                                   |
| --------------------------- | ------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Context Diagnosis**       | Cannot identify rot types                   | Identifies rot but cannot classify by type   | Identifies and classifies all four rot types; produces actionable rot report        | Spots rot proactively; predicts which instructions will rot fastest                            |
| **Architecture Design**     | Everything in one CLAUDE.md                 | Uses CLAUDE.md zones but nothing else        | Maps content to correct tools; calculates token budget impact                       | Designs adaptive architectures where context loads dynamically based on task                   |
| **Persistence Engineering** | No persistence — loses everything on /clear | Basic progress file with task list           | Task DAG with dependencies + tacit knowledge extraction; survives /clear cleanly    | Designs persistence that improves over time as more sessions contribute knowledge              |
| **Lifecycle Management**    | No awareness of context utilization         | Monitors utilization but compacts reactively | Proactive compaction strategy with structured instructions; manages all three zones | Designs compaction protocols that are automated via hooks and progress files                   |
| **Advanced Patterns**       | No memory or isolation                      | Basic memory file; single-agent only         | Memory corpus with injection strategy; multi-agent pipeline with clean handoff      | Memory with deduplication and decay; isolation patterns optimized for domain-specific analysis |

---

## Measuring Your Transformation

If you completed all seven modules in order, you now have a complete measurement trail: baseline scores from Module 1, incremental improvements from each module, and a final score from Module 7. Review your tracking spreadsheet and answer these questions:

1. **Total improvement:** What is the difference between your Module 1 baseline and your Module 7 final score? Express it as both points and percentage.

2. **Biggest single improvement:** Which module produced the largest score jump? Why do you think that technique had the most impact on your specific agent?

3. **Diminishing returns:** Did later modules produce smaller improvements than earlier ones? If so, what does that tell you about the order of operations for context engineering?

4. **Criterion analysis:** Which of the four scoring criteria (Completeness, Accuracy, Consistency, Actionability) improved most across all seven modules? Which improved least?

5. **The meta-lesson:** You transformed a 25-35 point agent into a 50-58 point agent without changing the model, adding training data, or writing code. The only variable was context engineering. What does this tell you about where to invest your effort when building AI agents?

---

## What's Next

You have practiced the three core skills — **context diagnosis** (identifying what is wrong with an agent's context), **context architecture** (designing where information should live), and **context engineering** (building production-quality context systems) — across 14 exercises and up to 3 capstones. These skills compound: every exercise builds intuition for recognizing context problems and knowing which technique to apply. Context engineering is not a one-time setup activity — it is an ongoing discipline that separates agents that degrade over time from agents that improve over time. Next in **Lesson 12: Chapter Quiz**, you will test your conceptual understanding of all context engineering principles and their interactions. The quiz focuses on scenario-based reasoning — exactly the kind of diagnosis you practiced throughout the Context Lab.
