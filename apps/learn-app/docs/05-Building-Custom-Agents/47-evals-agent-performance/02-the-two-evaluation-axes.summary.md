### Core Concept
Every evaluation falls on two axes: Axis 1 (Objective/Code-checkable vs Subjective/LLM-judged) and Axis 2 (Ground truth available vs No ground truth), creating four quadrants that determine the appropriate grading strategy.

### Key Mental Models
- Four Quadrants: Q1 (Objective + Ground Truth), Q2 (Subjective + Ground Truth), Q3 (Objective + No GT), Q4 (Subjective + No GT)
- Prefer lower quadrants for cost/reliability: Q1 > Q2, Q3 > Q4
- Objective criteria use deterministic functions; Subjective criteria need LLM reasoning
- Ground truth enables comparison against reference; No ground truth requires rubric-based assessment

### Critical Patterns
- Q1 (cheapest, fastest): Exact extraction, expected tool calls - code compares output to expected
- Q2: Gold standard talking points, reference comparisons - LLM checks semantic coverage
- Q3: Format rules, length limits, constraint satisfaction - code verifies without reference
- Q4 (most expensive): Rubric-based quality, helpfulness, clarity - LLM judges against criteria
- Decision flow: Ground truth available? -> Code can verify? -> Select quadrant

### AI Collaboration Keys
- Ask AI to classify your agent's behaviors into the four quadrants
- Have AI design a rubric for Q4 evals (subjective + no ground truth)
- Challenge your quadrant classification to find cheaper alternatives without losing signal

### Common Mistakes
- Using LLM judges when code suffices (wastes money, adds noise)
- Expecting code to check what requires semantic judgment (misses quality issues)
- Misclassifying Q1/Q3 as Q4 (slow, expensive evals that should be instant)

### Connections
- **Builds on**: Lesson 01 (TDD vs Evals distinction)
- **Leads to**: Lesson 03 (Designing Eval Datasets)
