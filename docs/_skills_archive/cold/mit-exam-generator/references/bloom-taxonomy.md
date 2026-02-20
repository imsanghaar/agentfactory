# Bloom's Taxonomy for Exam Questions

Cognitive level classification and distribution guidance.

**Reference:** [Bloom's Taxonomy - Vanderbilt University](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/)

---

## Level Distribution (PhD Qualifying)

| Level | % | Questions (of 200) |
|-------|---|-------------------|
| Remember/Understand | 25% | 50 |
| Apply | 20% | 40 |
| Analyze | 25% | 50 |
| Evaluate | 18% | 36 |
| Create/Synthesize | 12% | 24 |

---

## Level 1: Remember/Understand (25%)

**Cognitive Task:** Recall facts, recognize patterns, explain concepts.

**Question Stems:**
- "According to the document..."
- "Which definition best describes..."
- "What is the primary purpose of..."
- "The document states that..."

**Appropriate For:**
- Precision Recall questions
- Basic Conceptual Distinction
- Foundational Architecture Analysis

**Indicators:**
- Single correct answer from source
- No calculation required
- No judgment needed

---

## Level 2: Apply (20%)

**Cognitive Task:** Use knowledge in new situations, execute procedures.

**Question Stems:**
- "Given [scenario], which approach..."
- "How would you implement..."
- "Calculate the [metric] given..."
- "Apply [principle] to [situation]..."

**Appropriate For:**
- Economic/Quantitative questions
- Specification Design
- Procedural questions

**Indicators:**
- Requires using a learned procedure
- Context differs from source examples
- Clear right/wrong application

---

## Level 3: Analyze (25%)

**Cognitive Task:** Break down, compare, identify relationships.

**Question Stems:**
- "Which BEST differentiates..."
- "What is the relationship between..."
- "Compare [X] and [Y] in terms of..."
- "What component is responsible for..."

**Appropriate For:**
- Conceptual Distinction
- Architecture Analysis
- Decision Matrix

**Indicators:**
- Requires breaking down complexity
- Multiple factors to consider
- Identifying cause-effect or part-whole relationships

---

## Level 4: Evaluate (18%)

**Cognitive Task:** Judge, critique, justify, assess trade-offs.

**Question Stems:**
- "What is the PRIMARY limitation..."
- "Which criticism is MOST valid..."
- "The strongest argument against..."
- "What is the MOST significant risk..."

**Appropriate For:**
- Critical Evaluation questions
- Trade-off analysis
- Risk assessment

**Indicators:**
- Requires judgment
- Multiple valid perspectives exist
- Must prioritize/rank considerations

---

## Level 5: Create/Synthesize (12%)

**Cognitive Task:** Design, propose, integrate multiple concepts.

**Question Stems:**
- "To achieve [goal] while maintaining..."
- "Design an approach that..."
- "Which combination would..."
- "If [principle] were applied to [novel case]..."

**Appropriate For:**
- Strategic Synthesis
- Research Extension
- Novel scenario design

**Indicators:**
- Requires combining multiple concepts
- Novel situation not in source
- Creative application needed

---

## Mapping Question Types to Bloom's Levels

| Question Type | Primary Level | Secondary |
|---------------|---------------|-----------|
| Precision Recall | Remember | - |
| Conceptual Distinction | Understand/Analyze | - |
| Decision Matrix | Analyze | Apply |
| Architecture Analysis | Analyze | Understand |
| Economic/Quantitative | Apply | Analyze |
| Specification Design | Apply | Create |
| Critical Evaluation | Evaluate | Analyze |
| Strategic Synthesis | Create | Evaluate |
| Research Extension | Create | Evaluate |

---

## Difficulty Correlation

| Bloom Level | Typical Difficulty |
|-------------|-------------------|
| Remember/Understand | Easy-Medium |
| Apply | Medium |
| Analyze | Medium-Hard |
| Evaluate | Hard |
| Create/Synthesize | Hard-Expert |

**Note:** Difficulty also depends on content complexity. A "Remember" question about advanced topic may be harder than an "Apply" question about basics.

---

## Auto-Detection Heuristics

When analyzing source content, estimate Bloom distribution:

```
IF content has:
  - Many definitions, facts, numbers → Emphasize Remember (30%)
  - Procedures, workflows, examples → Emphasize Apply (25%)
  - Comparisons, architectures → Emphasize Analyze (25%)
  - Trade-offs, limitations discussed → Emphasize Evaluate (20%)
  - Design principles, frameworks → Emphasize Create (15%)
```

Adjust distribution based on content emphasis while maintaining minimum coverage of all levels.
