# Assessment-Architect Eval Rubric

Scoring criteria for evaluating generated certification exams. Used by both deterministic graders and model-based rubric grading.

---

## Dimensions

### 1. Domain Relevance (40% of overall score)

Does the exam test competence **in the chapter's actual domain**?

| Score | Criteria |
|-------|----------|
| 90-100 | All scenarios are set in the chapter's domain or closely adjacent technical workflows |
| 70-89 | Most scenarios relevant; 1-3 drift to adjacent but reasonable domains |
| 50-69 | Mixed relevance; several questions use unrelated domains that don't test chapter skills |
| 30-49 | Many questions test abstract principles via unrelated industries (medical, legal, manufacturing) |
| 0-29 | Majority of scenarios have no connection to what the chapter teaches |

**For practical-tool chapters** (e.g., Claude Code CLI):
- GOOD: Development workflows, code editing, debugging, project setup, CI/CD, team collaboration
- BAD: Medical imaging, law firm document management, factory floor automation

**For conceptual chapters** (e.g., Seven Principles):
- GOOD: Diverse development scenarios that require applying the principle
- ACCEPTABLE: Adjacent technical scenarios showing principle transfer
- BAD: Scenarios so abstract the principle being tested is unclear

### 2. Practical Competence (30% of overall score)

Would passing this exam certify someone to **do the work**, not just know about it?

| Score | Criteria |
|-------|----------|
| 90-100 | Exam tests when to use which tool, what happens when misconfigured, how to combine tools |
| 70-89 | Most questions require application; a few test recognition only |
| 50-69 | Mixed — some questions could be answered without hands-on experience |
| 30-49 | Many questions test vocabulary or definitions rather than practical judgment |
| 0-29 | Exam tests recall of facts, not ability to work |

**Practical competence signals:**
- "Which approach would you use when..." (tool selection)
- "What happens if you..." (consequence understanding)
- "How would you combine..." (workflow integration)

**Non-practical signals:**
- "What is the definition of..." (vocabulary)
- "Which principle states that..." (memorization)

### 3. Question Quality (20% of overall score)

Are questions well-constructed, with plausible distractors and realistic scenarios?

| Score | Criteria |
|-------|----------|
| 90-100 | All distractors plausible; scenarios realistic; clear writing; requires thinking |
| 70-89 | Most questions well-crafted; 1-3 have weak distractors or contrived scenarios |
| 50-69 | Several questions have obviously wrong options or bloated writing |
| 30-49 | Many questions could be answered by elimination or are poorly written |
| 0-29 | Widespread quality issues: obvious answers, unrealistic scenarios, confusing writing |

**Quality signals:**
- Distractors represent common misconceptions (not random wrong answers)
- Scenarios are situations a practitioner would actually encounter
- Writing is concise — difficulty comes from thinking, not parsing
- Each question has exactly one defensible correct answer

**Quality failures:**
- "According to the chapter..." (memorization pattern)
- 130+ word scenarios with filler phrases
- Distractors that no reasonable person would choose
- Ambiguous stems where 2+ options could be correct

### 4. Coverage (10% of overall score)

Are important lessons proportionally represented?

| Score | Criteria |
|-------|----------|
| 90-100 | Core lessons get 3-5 questions; intro/setup lessons get 0-1; no major gaps |
| 70-89 | Generally proportional; 1-2 important topics underrepresented |
| 50-69 | Flat distribution (2 per lesson) regardless of importance |
| 30-49 | Some important lessons have 0 questions; trivial lessons overrepresented |
| 0-29 | Coverage is random — no relationship between lesson importance and question count |

**Importance heuristics:**
- Core capability lessons (skills, subagents, hooks, MCP) = high weight
- Setup/installation lessons = low weight
- Intro/overview lessons = minimal weight
- Capstone/integration lessons = high weight

---

## Overall Score Calculation

```
overall = (domain_relevance * 0.4) + (practical_competence * 0.3) + (question_quality * 0.2) + (coverage * 0.1)
```

**Passing threshold: 75/100**

| Range | Verdict |
|-------|---------|
| 90+ | Excellent — ready for use |
| 75-89 | Good — minor improvements possible |
| 60-74 | Needs work — specific dimensions failing |
| < 60 | Fail — fundamental issues with exam quality |

---

## Chapter Type Reference

The eval graders need to know the chapter type to set appropriate expectations:

| Type | Characteristics | Domain Expectation |
|------|----------------|-------------------|
| `practical-tool` | Teaches how to use a specific tool (CLI commands, configuration, workflows) | Scenarios must be in the tool's usage domain |
| `conceptual` | Teaches principles, patterns, architecture decisions | Diverse scenarios acceptable if principle is clearly tested |
| `hybrid` | Mix of tool-usage and principle lessons | Proportional domain expectations |

**Detection heuristic** (for graders):
- Has CLI commands, installation steps, configuration examples → `practical-tool`
- Focuses on "when to use" / "why" / principles / trade-offs → `conceptual`
- Mix → `hybrid`
