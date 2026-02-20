---
title: "Practical SDD Exercises"
practice_exercise: ch5-sdd
sidebar_position: 9
chapter: 5
lesson: 9
duration_minutes: 120

# PEDAGOGICAL LAYER METADATA
primary_layer: "Layer 1"
layer_progression: "L1 (Manual Foundation)"
layer_1_foundation: "Hands-on practice applying Lessons 01-08 SDD concepts through 27 guided exercises"
layer_2_collaboration: "N/A"
layer_3_intelligence: "N/A"
layer_4_capstone: "N/A"

# HIDDEN SKILLS METADATA
skills:
  - name: "Specification Writing"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can write structured specifications with clear success criteria, constraints, and scope boundaries"
  - name: "Research & Refinement"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Information and Data Literacy"
    measurable_at_this_level: "Student can conduct multi-angle research and use interview-style refinement to surface hidden assumptions"
  - name: "Task Delegation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "Problem Solving"
    measurable_at_this_level: "Student can decompose specifications into atomic, dependency-ordered tasks suitable for agent delegation"

learning_objectives:
  - objective: "Write structured specifications with explicit constraints, success criteria, and scope boundaries"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Quality of specs written across Modules 3-4 exercises"
  - objective: "Conduct research and use refinement interviews to surface hidden assumptions before implementation"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Completion of research and refinement exercises in Modules 2 and 5"
  - objective: "Decompose specifications into atomic tasks with clear dependencies and delegation boundaries"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Task breakdowns produced in Module 6 and capstone projects"

cognitive_load:
  new_concepts: 3
  assessment: "3 concepts (spec writing, research-driven refinement, task delegation) — within B1 limit. Exercises reinforce existing L01-L08 knowledge through hands-on application."

differentiation:
  extension_for_advanced: "Complete all 3 capstone projects; attempt exercises without starter prompts"
  remedial_for_struggling: "Start with Module 1 only; use the starter prompts provided and work through one module per session"

teaching_guide:
  lesson_type: "hands-on"
  session_group: 3
  session_title: "Implementation and Judgment"
  key_points:
    - "27 exercises across 8 modules progressively build three skills: specification writing, research-driven refinement, and task delegation"
    - "None of these exercises involve writing code — SDD is a thinking methodology that applies to event planning, business operations, and content creation"
    - "The exercise framework (Research → Specify → Refine → Execute → Verify → Iterate) mirrors the four-phase SDD workflow with verification added"
    - "Capstone C (Personal Goal System) has real stakes — students build deliverables they actually keep using after the course"
  misconceptions:
    - "Students think SDD exercises require programming — emphasize these are deliberately non-code to show SDD as a universal methodology"
    - "Students try to complete all 27 exercises in one sitting — recommend one module per session for proper reflection"
    - "Students skip the reflection questions — the reflection is where real learning happens, not just completing the deliverable"
  discussion_prompts:
    - "After completing Module 1 exercises, which was more eye-opening: the event aftermath or the side-by-side comparison?"
    - "For the capstones, which project resonates most with your actual life or work — and why does that make it the best learning opportunity?"
  teaching_tips:
    - "Assign Module 1 as the first homework — the side-by-side comparison exercise converts SDD skeptics faster than any lecture"
    - "The assessment rubric (Beginner through Advanced) is useful for self-evaluation — have students rate themselves after each module"
    - "For classroom use, Module 4 Exercise 4.3 (Constraint Stress Test) works brilliantly as a paired exercise where students try to break each other's specs"
    - "Capstone C (Personal Goal System) is the strongest exercise because students discover their stated goal isn't their real goal during refinement"
  assessment_quick_check:
    - "Name the six steps of the SDD Exercise Framework and explain how they map to the four SDD phases from earlier lessons"
    - "What's the difference between a 'Beginner' and 'Proficient' score on the Constraint Coverage rubric dimension?"
---

# Practical SDD Exercises

You know the four-phase SDD workflow. You understand why specs beat vibe coding, how research prevents wrong assumptions, and how refinement catches what you missed. That knowledge gives you a vocabulary — but vocabulary without practice is just terminology.

These exercises put you in messy, realistic situations where the only path to a good outcome is the SDD discipline you learned in Lessons 1-8. Each one starts with a deliberately vague or chaotic scenario and asks you to transform it into something an AI agent can execute reliably. Three skills run through every exercise: **specification writing** (turning vague goals into precise, actionable documents), **research and refinement** (gathering context and surfacing hidden assumptions before committing to a plan), and **task delegation** (breaking specs into atomic, ordered tasks that an agent can execute independently).

None of these exercises involve writing code. SDD is a thinking methodology — it works for event planning, business operations, content creation, and any complex project where "just do it" leads to rework.

:::info Download Exercise Files
**[Download SDD Exercises (ZIP)](https://github.com/imsanghaar/claude-code-sdd-exercises/releases/latest/download/sdd-exercises.zip)**

After downloading, unzip the file. Each exercise has its own folder with an `INSTRUCTIONS.md` and any starter files you need.

If the download link doesn't work, visit the [repository releases page](https://github.com/imsanghaar/claude-code-sdd-exercises/releases) directly.
:::

---

## How to Use These Exercises

The workflow for every exercise is the same:

1. **Open the exercise folder** from the `claude-code-sdd-exercises/` directory
2. **Read the INSTRUCTIONS.md** inside the folder — it has setup steps and starter files
3. **Read the walkthrough below** for context on what you're practicing and why
4. **Start Claude Code or Cowork** and point it at the exercise folder
5. **Work through the exercise** — write your own specs, don't just copy the starter
6. **Reflect** using the questions provided — this is where the real learning happens

You don't need to complete all 27 in one sitting. Work through one module at a time. Each module targets a different phase of the SDD workflow.

---

## Tool Guide

- 🖥️ = **Claude Code** (terminal-based, best for exercises involving file creation and multi-step workflows)
- 🗂️ = **Cowork** (desktop app — point it at a folder and describe the task, best for research and document review)
- Most exercises work with either tool. Start with whichever you're comfortable with.

---

## The SDD Exercise Framework

Use this for every exercise:

1. **Research** — What do I need to know before I can specify this? What assumptions am I making?
2. **Specify** — Write it down: goals, constraints, success criteria, what's out of scope
3. **Refine** — What did I miss? Interview stakeholders (or yourself). Find the ambiguities.
4. **Execute** — Hand the spec to Claude. Let the spec do the talking.
5. **Verify** — Does the output match the spec? Not "does it look okay" — does it meet every criterion?
6. **Iterate** — What would I change in the spec? Not in the output — in the spec itself.

This framework mirrors the four-phase SDD workflow from the chapter, with verification and iteration added because exercises give you the luxury of immediate feedback. In professional work, this same loop runs across days or weeks.

---

## Assessment Rubric

For each exercise, evaluate yourself on:

| Criteria                | Beginner (1)                    | Developing (2)                    | Proficient (3)                                  | Advanced (4)                                       |
| ----------------------- | ------------------------------- | --------------------------------- | ----------------------------------------------- | -------------------------------------------------- |
| **Research Quality**    | Skipped research entirely       | Gathered some context             | Systematic multi-angle investigation            | Identified non-obvious sources and cross-validated |
| **Spec Completeness**   | Vague description, no structure | Has goals but missing constraints | Goals, constraints, success criteria, scope     | Reusable spec with edge cases anticipated          |
| **Constraint Coverage** | No constraints defined          | Listed obvious limits             | Explicit inclusions AND exclusions              | Tested constraints against edge cases              |
| **Refinement Depth**    | No refinement pass              | Caught 1-2 gaps                   | Systematic ambiguity hunt with stakeholder lens | Refinement changed the spec's direction            |
| **Task Delegation**     | Monolithic "do everything"      | Broke into a few chunks           | Atomic tasks with clear dependencies            | Tasks any agent could execute independently        |

---

## Module 1: Spec vs. Vibe — Seeing the Difference

> **Core Skill:** Recognizing the gap between vague instructions and precise specifications by experiencing both side by side.

<ExerciseCard id="1.1" title="The Event Gone Wrong" />

### Exercise 1.1 — The Event Gone Wrong 🗂️🖥️

**The Problem:**
Open the `event-gone-wrong/` folder in the exercise directory. You'll find `vibe-prompt.md` — a single vague instruction someone gave to an AI: "Plan a team building event for next month." You'll also find `aftermath.md` — a description of everything that went wrong when the AI executed that prompt (wrong date, wrong budget, activities nobody wanted, dietary restrictions ignored, no parking info).

**Your Task:**
Read the aftermath document and reverse-engineer what the original prompt should have said. Write a complete specification that would have prevented every single problem described in the aftermath. Don't just add details — structure it with goals, constraints, attendee requirements, and measurable success criteria.

**What You'll Learn:**

- Why vague prompts produce unpredictable results even when the AI "tries its best"
- How to identify the gap between what you assumed and what you specified
- That most project failures trace back to specification gaps, not execution errors

**Starter Prompt (Intentionally Vague):**

> "Plan a team building event for next month."

**Better Prompt (Build Toward This):**
Think about: Who is attending? What's the budget ceiling? Are there date constraints? Dietary restrictions? Accessibility requirements? What does "successful" mean — how would you measure it? What should definitely NOT happen?

**Reflection Questions:**

1. How many of the aftermath problems could you trace to a single missing sentence in the original prompt?
2. What assumptions did the AI make that seemed reasonable but turned out wrong?
3. Could your revised spec be handed to a completely different AI agent and still produce the right event?

---

<ExerciseCard id="1.2" title="The Side-by-Side Test" />

### Exercise 1.2 — The Side-by-Side Test 🗂️🖥️

**The Problem:**
Open the `side-by-side/` folder. You'll find a project brief: creating a company welcome packet for new employees. The brief has enough information to work with but plenty of ambiguity.

**Your Task:**
Approach this project TWO different ways:

1. **Vibe approach:** Give Claude the brief and a single-sentence instruction: "Create a welcome packet based on this brief." Save the output.
2. **SDD approach:** Before touching Claude, write a full specification — goals, audience, required sections, tone constraints, success criteria, what NOT to include. Then give Claude the spec. Save the output.

Compare the two outputs side by side.

**What You'll Learn:**

- The measurable difference between vibe-coded and spec-driven output
- How specifications prevent the AI from making reasonable-but-wrong assumptions
- That writing the spec takes 10 minutes but saves hours of revision

**Starter Prompt (Intentionally Vague):**

> "Create a welcome packet based on this brief."

**Better Prompt (Build Toward This):**
Before prompting, write a spec document answering: What sections must be included? What tone (formal? friendly? casual)? What's the maximum length? What topics are off-limits? What should a new hire be able to DO after reading it? Who approved the content?

**Reflection Questions:**

1. Which output would you actually send to a new employee? What specific differences made it better?
2. How long did the spec take to write versus the time you'd spend fixing the vibe output?
3. Were there any areas where the vibe approach actually produced something the spec approach missed?

---

<ExerciseCard id="1.3" title="Vibe-to-Spec Rescue" />

### Exercise 1.3 — Vibe-to-Spec Rescue 🗂️🖥️

**The Problem:**
Open the `vibe-rescue/` folder. You'll find three files — outputs from vibe-coded AI sessions that went sideways. Each one almost works but has fundamental problems: a marketing email with the wrong tone, a project timeline with impossible dependencies, and a budget spreadsheet with missing categories.

**Your Task:**
For each failed output:

1. Identify exactly what went wrong and why
2. Write the specification that should have been written BEFORE the AI was asked to produce this
3. Run your spec through Claude and compare the new output to the original failure

**What You'll Learn:**

- How to diagnose specification failures from their symptoms in the output
- That "fixing the output" is treating symptoms — fixing the spec treats the cause
- The pattern of working backward from failure to missing specification

**Reflection Questions:**

1. Which of the three failures was hardest to diagnose? Why?
2. Did writing the spec after seeing the failure feel different from writing one cold?
3. How would you explain the "fix the spec, not the output" principle to a colleague?

---

## Module 2: Research Phase — Gathering Context

> **Core Skill:** Transforming a broad question into a structured research task that produces actionable context for specification writing.

<ExerciseCard id="2.1" title="The Multi-Angle Investigation" />

### Exercise 2.1 — The Multi-Angle Investigation 🗂️🖥️

**The Problem:**
Open the `multi-angle/` folder. You'll find `project-brief.md` — a one-paragraph description of a project: building an internal knowledge base for a 50-person company. The brief is deliberately thin. Before you can write a useful spec, you need to understand the landscape.

**Your Task:**
Ask Claude to research this topic from four different angles — write a separate research prompt for each:

1. **User angle:** What do employees actually need from an internal knowledge base? What frustrations do they have with existing approaches?
2. **Technical angle:** What platforms, formats, and organizational patterns exist for internal knowledge bases?
3. **Organizational angle:** What change management challenges come with introducing a knowledge base? What makes adoption succeed or fail?
4. **Competitive angle:** What do similar-sized companies use? What worked and what didn't?

Synthesize the four research outputs into a single "Research Summary" document.

**What You'll Learn:**

- How different research angles reveal different constraints you'd otherwise miss
- That a single research prompt produces shallow results — multi-angle research produces specification-ready context
- How to structure research so its output feeds directly into specification writing

**Starter Prompt (Intentionally Vague):**

> "Research internal knowledge bases for me."

**Better Prompt (Build Toward This):**
Write four separate, focused research prompts — each targeting one angle. Specify what format you want the findings in (bullet points? comparison table? summary paragraph?). Include a final synthesis prompt that combines all four into a research summary document.

**Reflection Questions:**

1. Which research angle produced the most surprising findings?
2. How would skipping any one angle have changed your understanding of the project?
3. Did the synthesis reveal contradictions between angles (e.g., users want simplicity but the technical landscape is complex)?

---

<ExerciseCard id="2.2" title="Source Reliability Audit" />

### Exercise 2.2 — Source Reliability Audit 🗂️🖥️

**The Problem:**
Open the `source-audit/` folder. You'll find `research-output.md` — a research document Claude produced about "best practices for remote team communication." The document is plausible but contains a mix of well-supported claims, vague generalizations, outdated references, and at least two statements that sound authoritative but are unverifiable.

**Your Task:**

1. Read the research document carefully
2. For each major claim, classify it: **Verified** (can confirm source), **Plausible** (reasonable but unverified), **Suspect** (sounds wrong or outdated), or **Unverifiable** (no way to check)
3. Create an audit report that flags every suspect and unverifiable claim
4. Ask Claude to redo the research with explicit instructions about sourcing: "Only include claims you can attribute to a specific source. Flag anything uncertain."
5. Compare the original and audited versions

**What You'll Learn:**

- That AI research output requires verification, not trust
- How to build source-checking into your research workflow
- The difference between "sounds right" and "is right"

**Reflection Questions:**

1. How many claims in the original did you flag as suspect or unverifiable?
2. Did the audited version produce fewer claims overall? Was that a good tradeoff?
3. How would you incorporate source reliability checking into a real SDD research phase?

---

<ExerciseCard id="2.3" title="Research Summary Document" />

### Exercise 2.3 — Research Summary Document 🗂️🖥️

**The Problem:**
Open the `research-summary/` folder. You'll find three separate research files — each covers a different aspect of the same topic (launching a community newsletter): audience analysis, content strategy research, and distribution platform comparison. They were produced independently and use different formats.

**Your Task:**

1. Read all three research files
2. Write a specification for a unified "Research Summary Document" — define the sections, format, how conflicts between sources should be handled, and what the document must contain to be useful for specification writing
3. Give Claude your spec plus the three raw research files
4. Evaluate the output: Does it actually synthesize (finding connections and conflicts) or just summarize (restating each file)?

**What You'll Learn:**

- That synthesis and summarization are different skills — and your spec must demand synthesis
- How to write specs for research outputs (meta-specification)
- Why research quality determines specification quality

**The Challenge:**
After generating the research summary, write the first draft of a specification for the community newsletter — using ONLY the research summary as your input. Note everywhere you wish the research had gone deeper.

**Reflection Questions:**

1. Did Claude synthesize or summarize? What in your spec made the difference?
2. Where did the research summary fall short when you tried to write a spec from it?
3. What would you add to your research prompts next time to produce more spec-ready output?

---

## Module 3: Writing Your First Spec

> **Core Skill:** Transforming messy real-world requirements into structured specifications with clear goals, constraints, and success criteria.

<ExerciseCard id="3.1" title="The Home Renovation Spec" />

### Exercise 3.1 — The Home Renovation Spec 🗂️🖥️

**The Problem:**
Open the `home-renovation/` folder. You'll find `homeowner-notes.md` — a rambling, stream-of-consciousness dump from a homeowner describing what they want done to their kitchen. It's full of contradictions ("I want it modern but also cozy"), vague preferences ("nice countertops"), budget hand-waving ("not too expensive"), and missing information (no measurements, no timeline, no mention of permits).

**Your Task:**
Transform the homeowner's notes into a structured renovation specification. Your spec must include:

1. **Clear objectives** — What exactly is being renovated and why
2. **Constraints** — Budget range, timeline, must-keep elements, non-negotiables
3. **Success criteria** — How will the homeowner know the renovation succeeded?
4. **Scope boundaries** — What is explicitly included AND excluded
5. **Open questions** — What information is still missing that you'd need before a contractor could start

**What You'll Learn:**

- How to extract structure from unstructured input without inventing information
- The discipline of marking what you DON'T know instead of filling in assumptions
- That good specs explicitly state their own gaps

**Starter Prompt (Intentionally Vague):**

> "Turn these renovation notes into a project plan."

**Better Prompt (Build Toward This):**
Don't ask for a plan — ask for a spec. Tell Claude: "Extract goals, constraints, and success criteria from these notes. For anything ambiguous or missing, create an 'Open Questions' section rather than making assumptions. Format as a structured specification document."

**Reflection Questions:**

1. How many contradictions did you find in the homeowner's notes? How did your spec handle them?
2. How long was your "Open Questions" section? Does that tell you something about the quality of the original input?
3. Could a contractor read your spec and give an accurate quote without additional conversation?

---

<ExerciseCard id="3.2" title="The Charity Fundraiser Spec" />

### Exercise 3.2 — The Charity Fundraiser Spec 🗂️🖥️

**The Problem:**
Open the `charity-fundraiser/` folder. You'll find `committee-email-thread.md` — an email thread from a 5-person charity event committee. Everyone has different ideas. One wants a gala dinner, another wants a fun run, a third wants an online auction. They agree on the cause but not the approach. The thread also reveals unstated constraints: one member can't do weekends, the venue contact is the chair's personal connection, and there's an implicit assumption about the budget that nobody's confirmed.

**Your Task:**
Write a specification for the fundraiser that:

1. Captures all stated AND unstated constraints from the email thread
2. Resolves (or explicitly flags) the disagreements between committee members
3. Defines what "successful fundraiser" means in measurable terms
4. Includes a "Decisions Required" section listing every choice the committee still needs to make
5. Is structured so each committee member can review the section relevant to them

**What You'll Learn:**

- How to extract specifications from multi-stakeholder input where people disagree
- The critical skill of separating "decided" from "still open"
- That surfacing unstated constraints is more valuable than solving stated ones

**Reflection Questions:**

1. How many unstated constraints did you find in the email thread?
2. Did structuring the disagreements as "Decisions Required" make them easier or harder to resolve?
3. Would this spec work as the agenda for the next committee meeting?

---

<ExerciseCard id="3.3" title="Spec from Chaos" />

### Exercise 3.3 — Spec from Chaos 🗂️🖥️

**The Problem:**
Open the `spec-from-chaos/` folder. You'll find a mix of input files — a voice memo transcript (`transcript.md`), a whiteboard photo description (`whiteboard.md`), a Slack conversation export (`slack-thread.md`), and a half-finished project brief (`draft-brief.md`). Together they describe a project to create an employee onboarding program, but no single document tells the whole story.

**Your Task:**

1. Read all four input files
2. Create a "Source Map" — for each piece of information in your spec, note which source it came from
3. Write a complete specification that synthesizes all four sources
4. Identify contradictions between sources and resolve them (or flag them in a "Conflicts" section)
5. List everything that's assumed but not confirmed by any source

**What You'll Learn:**

- How to synthesize multiple messy sources into a single coherent spec
- The discipline of traceability — knowing where each spec requirement came from
- That real-world specifications rarely come from a single clean brief

**The Twist:**
After writing your spec, remove one of the four source documents and see what's missing. This reveals which sources contributed unique information versus redundant context.

**Reflection Questions:**

1. Which source contributed the most unique information? Which was mostly redundant?
2. How did contradictions between sources change the spec compared to using any single source?
3. Would you structure the information-gathering phase differently if you could start over?

---

## Module 4: Constraints & Success Criteria

> **Core Skill:** Writing constraints and success criteria that are specific enough to verify and broad enough to allow creative solutions.

<ExerciseCard id="4.1" title="The Missing Guardrails" />

### Exercise 4.1 — The Missing Guardrails 🗂️🖥️

**The Problem:**
Open the `missing-guardrails/` folder. You'll find three specifications (`spec-a.md`, `spec-b.md`, `spec-c.md`) that each have goals and some structure but are missing critical constraints. Spec A is for a company blog content calendar — no constraints on topics, frequency, or voice. Spec B is for an office supply ordering system — no budget limits, no approval process. Spec C is for a customer feedback survey — no length limit, no scope boundary, no privacy constraints.

**Your Task:**
For each specification:

1. Identify what would go wrong if Claude executed this spec as-is (predict the failure mode)
2. Add the missing constraints — be specific, not vague ("budget: $500/month" not "reasonable budget")
3. For each constraint you add, write a one-sentence justification of why it's necessary
4. Run both versions (original and constrained) through Claude and compare outputs

**What You'll Learn:**

- That specifications without constraints produce technically-correct-but-useless output
- How to anticipate failure modes by reading a spec critically
- The difference between constraints that prevent harm and constraints that shape quality

**Starter Prompt (Intentionally Vague):**

> "Create a content calendar for our blog."

**Better Prompt (Build Toward This):**
Before giving the task, list what MUST NOT happen: no topics outside our expertise areas, no posts longer than 1200 words, no more than 3 posts per week, no promotional tone in educational content. Then list what MUST happen: every post needs a clear CTA, every post targets one of our 4 audience segments.

**Reflection Questions:**

1. Which specification was most dangerous without constraints? Why?
2. Did adding constraints change the output quality or just prevent problems?
3. How many constraints is "too many"? Did any of your constraints fight each other?

---

<ExerciseCard id="4.2" title="Measurable vs. Vague" />

### Exercise 4.2 — Measurable vs. Vague 🗂️🖥️

**The Problem:**
Open the `measurable-vs-vague/` folder. You'll find `success-criteria.md` — a list of 15 success criteria from various real projects. Some are measurable ("newsletter opens exceed 25% within 3 months"), some are vague ("users should find it easy to use"), and some are somewhere in between.

**Your Task:**

1. Classify each criterion as **Measurable**, **Vague**, or **Borderline**
2. Rewrite every vague and borderline criterion to make it measurable
3. For each rewrite, note what decision you had to make (e.g., "easy to use" required defining easy for whom, doing what, measured how)
4. Pick 3 of your rewritten criteria and ask Claude to create a verification plan — how would you actually test whether the criterion was met?

**What You'll Learn:**

- The difference between success criteria that sound good and ones you can verify
- That making criteria measurable forces you to make decisions you'd otherwise defer
- How verification plans expose criteria that are technically measurable but impractical to check

**Reflection Questions:**

1. Which vague criterion was hardest to make measurable? What made it hard?
2. Did any measurable-sounding criteria turn out to be unverifiable when you wrote the verification plan?
3. How would you explain the value of measurable criteria to a stakeholder who says "we'll know it when we see it"?

---

<ExerciseCard id="4.3" title="Constraint Stress Test" />

### Exercise 4.3 — Constraint Stress Test 🗂️🖥️

**The Problem:**
Open the `constraint-stress-test/` folder. You'll find a well-written specification for an employee training program (`training-spec.md`). It has goals, constraints, success criteria — the works. Your job is to break it.

**Your Task:**

1. Read the spec carefully
2. Write 5 scenarios that technically satisfy every constraint but produce a terrible outcome (malicious compliance)
3. For each scenario, identify the missing constraint that would have prevented it
4. Add your new constraints to the spec
5. Try to break the updated spec with 3 more scenarios
6. Repeat until you can't find loopholes

**What You'll Learn:**

- That "stress testing" specifications is as important as stress testing code
- How to think adversarially about your own specifications
- That the best constraints come from imagining how they could be maliciously obeyed

**The Twist:**
Swap your stress-tested spec with a classmate's (or set it aside for 24 hours and return fresh). Can you find loopholes they missed? Can they find yours?

**Reflection Questions:**

1. How many rounds of stress testing did it take before you couldn't find more loopholes?
2. Did adversarial thinking change how you write constraints going forward?
3. Is there a point where adding more constraints makes the spec harder to work with?

---

## Module 5: Refinement — Finding What's Missing

> **Core Skill:** Using structured interviews and systematic review to surface the assumptions, ambiguities, and gaps that survive the first draft.

<ExerciseCard id="5.1" title="The Interview Challenge" />

### Exercise 5.1 — The Interview Challenge 🗂️🖥️

**The Problem:**
Open the `interview-challenge/` folder. You'll find `draft-spec.md` — a first-draft specification for a company offsite retreat. It covers the basics (date, location, activities) but has the typical first-draft problems: unexamined assumptions, missing stakeholder perspectives, and ambiguities that would cause problems during execution.

**Your Task:**

1. Read the draft spec
2. Ask Claude to play the role of "tough interviewer" — someone whose job is to find every assumption, ambiguity, and gap. Use this prompt pattern: "Read this spec and ask me every question that, if left unanswered, could cause the project to fail or deliver the wrong result."
3. Answer Claude's questions honestly (you'll discover that some answers require decisions you haven't made yet)
4. Update the spec based on the interview
5. Compare the before and after versions

**What You'll Learn:**

- That first drafts always contain hidden assumptions — the interview process surfaces them
- How to use Claude as a refinement partner, not just an executor
- The difference between "I think the spec is done" and "the spec has survived questioning"

**Starter Prompt (Intentionally Vague):**

> "Review my spec and tell me if it's good."

**Better Prompt (Build Toward This):**
Be specific about what you want challenged: "Read this spec. For every statement, ask: What could go wrong if this is ambiguous? What assumption am I making? What stakeholder perspective is missing? Don't be polite — find the gaps."

**Reflection Questions:**

1. How many questions did Claude ask that you couldn't answer without making a new decision?
2. Which question surprised you the most?
3. How much did the spec change after the interview? Was it cosmetic or structural?

---

<ExerciseCard id="5.2" title="Ambiguity Hunter" />

### Exercise 5.2 — Ambiguity Hunter 🗂️🖥️

**The Problem:**
Open the `ambiguity-hunter/` folder. You'll find `polished-spec.md` — a specification that looks complete and professional. It has sections, formatting, success criteria — all the right structure. But it contains 10 deliberate ambiguities hidden in plain sight. They're not typos or missing sections — they're statements that two reasonable people would interpret differently.

**Your Task:**

1. Read the spec and find as many ambiguities as you can
2. For each ambiguity, write two different interpretations that are both valid
3. Ask Claude to find ambiguities you missed (compare its list to yours)
4. Resolve each ambiguity by rewriting the statement to be unambiguous
5. Check your answer against `answer-key.md` — how many of the 10 did you catch?

**What You'll Learn:**

- That professional-looking specs can hide dangerous ambiguities
- How ambiguity differs from vagueness — ambiguous statements feel clear until two people disagree
- The discipline of reading specs as if you're trying to misunderstand them

**Reflection Questions:**

1. How many of the 10 ambiguities did you catch before checking the answer key?
2. Were the ambiguities you missed different in character from the ones you caught?
3. Did Claude find ambiguities you missed, or did you outperform it?

---

<ExerciseCard id="5.3" title="Stakeholder Perspectives" />

### Exercise 5.3 — Stakeholder Perspectives 🗂️🖥️

**The Problem:**
Open the `stakeholder-perspectives/` folder. You'll find `product-spec.md` — a specification for a new internal tool. It was written from the project manager's perspective. Your job is to review it from three other perspectives that weren't consulted.

**Your Task:**

1. Review the spec as the **end user** — someone who'll use this tool daily. What's missing? What would frustrate you?
2. Review the spec as the **IT administrator** — someone responsible for security, maintenance, and integration. What concerns you?
3. Review the spec as the **executive sponsor** — someone funding this and expecting ROI. What success criteria are missing?
4. Write a "Stakeholder Review Summary" documenting every gap, concern, and missing requirement from each perspective
5. Update the spec to address the most critical findings

**What You'll Learn:**

- That every spec has blind spots determined by who wrote it
- How different stakeholders see different risks and requirements in the same project
- The practice of systematic perspective-shifting as a refinement technique

**The Extension:**
Ask Claude to review the spec from a perspective you didn't think of — a compliance officer, a competitor, or a new employee encountering the tool for the first time. Did this novel perspective reveal anything the three standard perspectives missed?

**Reflection Questions:**

1. Which perspective found the most critical gaps?
2. Were there requirements that one perspective demanded but another would oppose?
3. How many perspectives is "enough" for a real project? How do you decide when to stop?

---

## Module 6: Task Breakdown & Delegation

> **Core Skill:** Decomposing specifications into atomic, dependency-ordered tasks that an AI agent (or human team) can execute independently.

<ExerciseCard id="6.1" title="The Dependency Map" />

### Exercise 6.1 — The Dependency Map 🗂️🖥️

**The Problem:**
Open the `dependency-map/` folder. You'll find `project-spec.md` — a specification for organizing a 3-day workshop. The spec lists 20 deliverables (venue booking, schedule creation, materials preparation, speaker coordination, catering, AV setup, registration system, etc.) but doesn't specify any ordering or dependencies.

**Your Task:**

1. Read the spec and identify all 20 deliverables
2. Map the dependencies: which tasks must complete before others can start? Which can run in parallel?
3. Create a visual dependency map (as a text diagram or table) showing the critical path
4. Identify which tasks are "blocking" (many things depend on them) vs. "independent" (can happen anytime)
5. Ask Claude to execute the first 3 tasks from your dependency map in the correct order

**What You'll Learn:**

- That task ordering isn't obvious — the same deliverables can be sequenced many valid ways
- How to identify critical-path tasks that block everything else
- The difference between sequential constraints (A must finish before B) and resource constraints (only one person, so A and B can't actually be parallel)

**Starter Prompt (Intentionally Vague):**

> "Break this project into tasks and do them."

**Better Prompt (Build Toward This):**
Don't ask Claude to just "break it down." Ask: "Identify all deliverables, map which ones depend on which, find the critical path, and tell me which 3 tasks should start first and why. Show the dependency map as a diagram."

**Reflection Questions:**

1. How many dependency relationships did you find? Were any surprising?
2. Which task is the biggest bottleneck — the one where a delay cascades to the most other tasks?
3. If you had two AI agents working in parallel, which tasks would you assign to each?

---

<ExerciseCard id="6.2" title="Atomic Task Writer" />

### Exercise 6.2 — Atomic Task Writer 🗂️🖥️

**The Problem:**
Open the `atomic-tasks/` folder. You'll find `bad-tasks.md` — a list of 10 task descriptions that are too vague for an AI agent to execute reliably. Examples: "Handle the marketing stuff," "Make the website better," "Deal with customer feedback." Each task is an actual instruction someone might give, and each one would produce unpredictable results.

**Your Task:**

1. For each vague task, rewrite it as 2-4 atomic tasks that are specific enough for Claude to execute without follow-up questions
2. Each atomic task must pass the "hand-off test": could you give this task description to someone with zero context and get the right result?
3. Include for each atomic task: a clear deliverable, an input (what the agent needs), and a verification check (how to confirm it's done correctly)
4. Test 3 of your atomic tasks by actually giving them to Claude — does the output match your expectations?

**What You'll Learn:**

- The difference between human-understandable tasks and agent-executable tasks
- How to write task descriptions that don't require follow-up questions
- That the "hand-off test" is the gold standard for task specification

**Reflection Questions:**

1. Which vague task was hardest to make atomic? What made it resist decomposition?
2. Did any of your "atomic" tasks still produce unexpected output from Claude? What was still ambiguous?
3. How granular is "too granular"? Where's the line between helpfully specific and micromanaging?

---

<ExerciseCard id="6.3" title="Delegation Simulation" />

### Exercise 6.3 — Delegation Simulation 🗂️🖥️

**The Problem:**
Open the `delegation-sim/` folder. You'll find `product-launch-spec.md` — a complete specification for launching a new product. Your job is to act as the project manager: break the spec into tasks, assign them, sequence them, and manage the execution.

**Your Task:**

1. Break the spec into 8-12 atomic tasks
2. Identify which tasks could be delegated to different "agents" (in a real workflow, these would be Claude Code subagents)
3. Write a delegation plan: which agent gets which task, in what order, with what inputs
4. Execute the first 3 tasks by giving Claude each task description one at a time (simulating separate agent contexts)
5. After each task, verify the output meets the spec before moving to the next
6. Write a brief "execution report" noting where the delegation plan worked and where it needed adjustment

**What You'll Learn:**

- The full loop from spec to tasks to delegation to execution to verification
- That delegation plans need adjustment during execution — rigid plans break
- How task handoffs work when each "agent" has no memory of what the previous one did

**The Goal:**
Your delegation plan should be detailed enough that someone else could manage the execution by following your plan, without understanding the original spec.

**Reflection Questions:**

1. Did any task's output not match what the next task expected as input? How did you handle the handoff?
2. Which tasks benefited from being in separate "agent" contexts, and which suffered from losing shared context?
3. How would you change your delegation plan if you were doing this project again?

---

## Module 7: Full SDD Cycle — End to End

> **Core Skill:** Running the complete SDD workflow — from research through execution — on a single real-world project.

<ExerciseCard id="7.1" title="Community Newsletter" />

### Exercise 7.1 — Community Newsletter 🗂️🖥️

**The Problem:**
Open the `community-newsletter/` folder. You'll find `brief.md` — a brief from a neighborhood association that wants to start a monthly community newsletter. The brief mentions wanting to "keep everyone informed" but is otherwise vague. No format, no content strategy, no distribution plan, no budget.

**Your Task:**
Run the complete SDD cycle:

1. **Research:** Investigate what successful community newsletters look like (ask Claude to research formats, frequency, content types, distribution methods, common mistakes)
2. **Specify:** Write a complete specification covering content strategy, format, distribution, schedule, roles, and success criteria
3. **Refine:** Ask Claude to interview you about the spec — let it challenge your assumptions about audience, content mix, and sustainability
4. **Execute:** Break the spec into tasks and have Claude produce the first issue (template, content outline, distribution plan)
5. **Verify:** Check every output against your spec's success criteria

**What You'll Learn:**

- How the four SDD phases feel when you run them end-to-end on a real project
- Where you're tempted to skip phases (research and refinement, usually)
- That the discipline pays off in output quality, not just process compliance

**Reflection Questions:**

1. Which phase took the longest? Which produced the most value per minute spent?
2. Where were you tempted to skip ahead? What would you have missed?
3. Could someone run the second newsletter issue using only your spec, without talking to you?

---

<ExerciseCard id="7.2" title="Office Move Planner" />

### Exercise 7.2 — Office Move Planner 🗂️🖥️

**The Problem:**
Open the `office-move/` folder. You'll find `scenario.md` — a scenario where a 30-person company needs to move to a new office in 8 weeks. The scenario includes constraints (budget, lease dates, IT requirements, employees with accessibility needs) and a few curveballs (the CEO wants a standing desk area, the server room needs special cooling, two teams refuse to sit near each other).

**Your Task:**
Run the complete SDD cycle:

1. **Research:** What does a successful office move require? What goes wrong most often? What's typically forgotten?
2. **Specify:** Write a move specification covering timeline, budget allocation, space planning requirements, IT migration, employee communication plan, and contingency provisions
3. **Refine:** Have Claude interview you about the spec — particularly around the curveball requirements (standing desks, cooling, seating politics)
4. **Execute:** Break into phased tasks (Week 1-2, 3-4, 5-6, 7-8) with dependencies and have Claude produce the deliverables for Phase 1
5. **Verify:** Check Phase 1 output against spec criteria

**What You'll Learn:**

- How SDD handles projects with hard deadlines and non-negotiable constraints
- How curveball requirements stress-test your specification's flexibility
- The value of phased execution with verification checkpoints

**The Twist:**
After completing Phase 1 deliverables, introduce a change: the budget just got cut by 20%. Update the spec and re-plan remaining phases. This tests whether your spec is adaptable or brittle.

**Reflection Questions:**

1. How did the curveball requirements affect your spec? Did they require structural changes or just additions?
2. When the budget changed, how much of your spec survived versus needed rewriting?
3. What would have happened if you'd started executing without a spec and THEN the budget changed?

---

<ExerciseCard id="7.3" title="Product Launch Playbook" />

### Exercise 7.3 — Product Launch Playbook 🗂️🖥️

**The Problem:**
Open the `product-launch/` folder. You'll find `pitch.md` — an entrepreneur's pitch for a new local meal prep delivery service. The pitch is passionate but disorganized — part business plan, part feature list, part marketing copy. Your job is to turn this chaos into an executable launch playbook using the full SDD cycle.

**Your Task:**
Run the complete SDD cycle:

1. **Research:** Investigate the meal prep delivery market (competitors, pricing models, common failure modes, regulatory requirements for food businesses)
2. **Specify:** Write a launch playbook specification covering: pre-launch tasks, launch day plan, first-week operations, success metrics, budget allocation, and risk mitigation
3. **Refine:** Interview yourself from three perspectives — the entrepreneur, a potential customer, and a skeptical investor. Update the spec based on what each perspective reveals.
4. **Execute:** Break into tasks and have Claude produce: a launch timeline, a marketing plan outline, an operations checklist, and a budget spreadsheet
5. **Verify:** Score every deliverable against the spec's success criteria

**What You'll Learn:**

- How SDD transforms an unstructured vision into an executable plan
- How multi-perspective refinement catches blind spots a single viewpoint misses
- The end-to-end experience of going from chaos to structured deliverables

**Reflection Questions:**

1. How different is the final playbook from what the entrepreneur originally described in the pitch?
2. Which perspective (entrepreneur, customer, investor) changed the spec the most?
3. Is the playbook actually executable — could the entrepreneur follow it starting tomorrow?

---

## Module 8: Capstone Projects

> **Choose one (or more). Spend real time on it. This is where everything comes together.**

Capstones are different from the exercises above. There are no starter prompts — you design the entire SDD workflow yourself. Each project is complex enough to require genuine research, meaningful refinement, and multi-phase task delegation.

<ExerciseCard id="A" title="Wedding Planner System" />

### Capstone A — Wedding Planner System 🗂️🖥️

Open the `capstone-wedding/` folder. You'll find `couple-brief.md` — a couple's wish list for their wedding (150 guests, outdoor ceremony, indoor reception, specific dietary mix, budget range, 3 potential dates). The brief has the usual contradictions (elegant but casual, locally-sourced but affordable) and missing information (no mention of accessibility, weather contingency, or vendor preferences).

Run the full SDD cycle to produce a complete wedding planning system:

- Research: venue options, vendor categories, timeline benchmarks, common disaster scenarios
- Specification: comprehensive wedding spec with every vendor category, timeline, budget allocation, guest management approach, and contingency plans
- Refinement: interview from four perspectives (couple, guest, venue coordinator, day-of coordinator)
- Execution: produce a master timeline, budget tracker, vendor comparison matrices, guest management system, and day-of run sheet
- Verification: every deliverable checked against the spec

**What You'll Learn:**

- How SDD handles emotionally-charged projects where stakeholders have conflicting desires
- How to manage specifications with hundreds of interconnected details
- The full professional workflow from client brief to deliverable package

---

<ExerciseCard id="B" title="Small Business Launch Kit" />

### Capstone B — Small Business Launch Kit 🗂️🖥️

You're helping a friend launch a tutoring business. Open the `capstone-business/` folder for the `founder-vision.md` — a mix of market observations, personal goals, service ideas, and financial hopes. No structure, many assumptions, some unrealistic expectations.

Run the full SDD cycle to produce a complete business launch kit:

- Research: local tutoring market, pricing models, legal requirements, marketing channels for education businesses, common failure modes in first-year tutoring businesses
- Specification: business plan spec covering services, pricing, target market, marketing strategy, operations, financial projections, and legal/compliance requirements
- Refinement: interview from four perspectives (founder, parent/customer, competing tutor, accountant)
- Execution: produce a business plan document, pricing calculator, marketing calendar, client intake form, and first-month operations checklist
- Verification: every deliverable checked against measurable success criteria

**What You'll Learn:**

- How SDD applies to business planning where most decisions are interconnected
- How research prevents common first-business mistakes (underpricing, overcommitting, skipping legal)
- Building a complete deliverable package that a real founder could use

---

<ExerciseCard id="C" title="Personal Goal System" />

### Capstone C — Personal Goal System 🗂️🖥️

This capstone is different. Instead of a provided scenario, you build a system for YOUR real goals. Open the `capstone-personal/` folder for a template, but the content comes from you.

Pick a real personal goal (career change, fitness target, financial milestone, learning objective, creative project) and run the full SDD cycle:

- Research: what does success look like for this type of goal? What do people who achieved it say about the process? What are common failure modes?
- Specification: write a personal goal spec with milestones, constraints (time, money, energy), success criteria, and a realistic timeline
- Refinement: have Claude interview you ruthlessly — challenge your assumptions about available time, motivation sustainability, and whether your criteria are truly meaningful to you
- Execution: produce a tracking system, weekly review template, milestone checklist, and contingency plans for common obstacles
- Verification: does every deliverable actually serve the goal? Would you use it tomorrow?

**What Makes This Special:**
Unlike Capstones A and B, this one has real stakes. The SDD cycle applied to your actual goals produces deliverables you'll keep using after this course. The refinement phase — where Claude challenges your assumptions — often reveals that the goal you stated isn't quite the goal you meant.

**What You'll Learn:**

- How SDD applies to personal planning, not just business or technical projects
- That the refinement interview is most valuable when the stakes are personal
- The difference between a vague aspiration and a specified, executable goal

---

## What's Next

You've practiced the three core SDD skills — specification writing, research-driven refinement, and task delegation — across 27 exercises. These skills compound: each exercise builds intuition for transforming vague intentions into precise, executable plans. The SDD workflow you practiced here isn't just for software development — it's a general methodology for any complex project where "just figure it out" leads to rework. Up next is the Chapter 5 Quiz, where you'll test your conceptual understanding of everything from vibe coding failure modes to the four-phase workflow and the decision framework.
