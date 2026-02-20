# Rubric Grader — Model-Based Exam Quality Assessment

Use this prompt template to grade a generated exam against the success rubric. Replace `{EXAM_CONTENT}`, `{ANSWER_KEY}`, and `{CHAPTER_SUMMARY}` with actual content.

---

## Prompt Template

```
You are evaluating a certification exam for quality. Score it against four dimensions.

## Chapter Context

{CHAPTER_SUMMARY}

Chapter type: {CHAPTER_TYPE}
Chapter domain keywords: {DOMAIN_KEYWORDS}
Lesson count: {LESSON_COUNT}

## Exam to Evaluate

{EXAM_CONTENT}

## Answer Key

{ANSWER_KEY}

## Scoring Dimensions

Rate each dimension 0-100:

### 1. Domain Relevance (weight: 40%)

Are scenarios set in the chapter's actual domain?

- For practical-tool chapters: scenarios should involve development workflows, the specific tools taught, coding/engineering contexts
- For conceptual chapters: diverse scenarios acceptable if the principle is clearly tested
- Penalty: scenarios in unrelated industries (medical, legal, manufacturing) when chapter teaches coding tools

Questions to consider:
- Would a practitioner of THIS chapter's topic recognize these scenarios?
- Are the scenarios testing competence with the SPECIFIC tools/concepts taught?
- How many questions could have their scenario replaced with a development scenario without changing the concept tested?

### 2. Practical Competence (weight: 30%)

Would passing certify someone to DO the work?

- Test tool selection, consequence understanding, workflow integration
- NOT vocabulary, definitions, or "which principle states..."
- A passing student should be able to USE the tools, not just NAME them

Questions to consider:
- Could someone pass by reading summaries without hands-on practice?
- Do questions require understanding of what happens when tools are misconfigured?
- Are there questions testing WHEN to use one approach vs another?

### 3. Question Quality (weight: 20%)

Are questions well-constructed?

- Distractors should be plausible (common misconceptions, not obviously wrong)
- Scenarios should be realistic (situations a practitioner would encounter)
- Writing should be concise (difficulty in thinking, not reading)
- Each question should have exactly one defensible answer

Questions to consider:
- Can any questions be answered by elimination (2+ options obviously wrong)?
- Are any scenarios contrived or unrealistic?
- Are questions bloated with unnecessary words?
- Are there ambiguous questions where 2+ options could be correct?

### 4. Coverage (weight: 10%)

Are important topics proportionally represented?

- Core capabilities should get more questions than setup/intro lessons
- No major chapter topic should have 0 questions
- Question count should reflect lesson importance, not flat allocation

Questions to consider:
- Are there major chapter topics with no questions?
- Do trivial lessons (intro, setup) get as many questions as core lessons?
- Is there evidence of mechanical "2 per lesson" allocation?

## Output Format

Respond with ONLY this JSON (no other text):

{
  "domain_relevance": {
    "score": <0-100>,
    "failures": ["<specific question numbers and why they're off-domain>"],
    "summary": "<1-2 sentence assessment>"
  },
  "practical_competence": {
    "score": <0-100>,
    "failures": ["<questions that test recall not competence>"],
    "summary": "<1-2 sentence assessment>"
  },
  "question_quality": {
    "score": <0-100>,
    "failures": ["<questions with weak distractors, bloated writing, or ambiguity>"],
    "summary": "<1-2 sentence assessment>"
  },
  "coverage": {
    "score": <0-100>,
    "gaps": ["<topics with 0 or insufficient questions>"],
    "over_represented": ["<topics with too many questions relative to importance>"],
    "summary": "<1-2 sentence assessment>"
  },
  "overall": {
    "weighted_score": <calculated: domain*0.4 + practical*0.3 + quality*0.2 + coverage*0.1>,
    "verdict": "<EXCELLENT|GOOD|NEEDS WORK|FAIL>",
    "top_3_improvements": ["<most impactful changes to improve the exam>"]
  }
}
```

---

## Usage Notes

1. **Chapter summary**: Provide a brief description of what the chapter teaches (topics, tools, concepts)
2. **Chapter type**: Use `practical-tool`, `conceptual`, or `hybrid`
3. **Domain keywords**: Extract from lesson filenames and content (e.g., "Claude Code, CLI, skills, subagents, hooks, MCP")
4. **Model**: Use claude-sonnet-4-20250514 for cost efficiency; opus for detailed analysis
5. **Parse output**: The JSON output can be parsed by `run-eval.sh` for the weighted score

---

## Example Chapter Summary

```
Chapter 3 (General Agents) teaches Claude Code CLI usage: installation, authentication,
CLAUDE.md project files, skills creation, subagent orchestration, MCP integration,
compiling MCP to skills, settings hierarchy, hooks/extensibility, plugins, Ralph Wiggum
loop, Cowork mode, browser integration, connectors, and building a skills business.
This is a practical-tool chapter teaching hands-on use of Claude Code.
```
