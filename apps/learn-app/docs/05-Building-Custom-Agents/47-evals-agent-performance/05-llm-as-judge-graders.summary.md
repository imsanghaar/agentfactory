### Core Concept
LLM-as-Judge evaluates subjective criteria that code cannot assess, but requires careful design: use binary criteria instead of numeric scales, evaluate independently instead of pairwise comparisons, and validate against human judgment.

### Key Mental Models
- Use LLM judges only when code cannot determine correctness (semantic understanding required)
- Position bias: LLMs systematically prefer outputs in certain positions when comparing A vs B
- Binary criteria produce stable judgments; numeric scales produce noise
- Independent evaluation avoids position bias - grade each response separately, compare scores mathematically

### Critical Patterns
- Grader prompt structure: Context, Criteria (5-7 yes/no questions), Response to evaluate, JSON output format
- Avoid pairwise comparison: "Which is better?" suffers from position bias; evaluate each independently
- Human validation: Target 70%+ exact match, 90%+ within-one agreement with human raters
- Each binary criterion should be unambiguous enough that two humans would likely agree

### AI Collaboration Keys
- Have AI design binary criteria for your agent's specific quality dimensions
- Debug low-agreement graders by analyzing disagreement cases with AI
- Create task-specific graders with AI that match your domain requirements

### Common Mistakes
- Using pairwise comparison ("Which response is better?") - position bias makes results unreliable
- Using 1-5 scales - calibration varies across runs, models, and contexts
- Trusting LLM judgments without human validation (target: 70%+ exact agreement)
- Using LLM judges when code-based checks would suffice (wastes money, adds noise)

### Connections
- **Builds on**: Lesson 04 (Binary criteria pattern, code-based graders)
- **Leads to**: Lesson 06 (Systematic Error Analysis)
