### Core Concept
LLMs are poorly calibrated on 1-5 scale ratings. Instead, use binary yes/no criteria and sum them for consistent, meaningful scores. A 3/5 from binary criteria means exactly "met criteria 1, 2, and 4 but missed 3 and 5" - actionable information.

### Key Mental Models
- Binary criteria leverage LLM strengths (classification, identification, verification) and avoid weaknesses (arbitrary scaling, holistic judgment)
- Sum-of-binaries scoring: 5 criteria, all YES = 100%; 3 YES = 60% - meaningful and reproducible
- Decomposition: Break subjective quality dimensions into specific, observable binary checks
- Code-first, LLM-second: Use code graders for objective criteria (fast, cheap, deterministic); LLM judges only for semantic judgment

### Critical Patterns
- Code-based grader structure: `checks = {...}`, `score = sum(checks.values())`, return structured result
- LLM grader prompt template: "For EACH criterion, answer YES or NO only" with numbered criteria
- Combined grader pattern: Run code checks first; only run LLM if code checks pass (saves money)
- Binary criteria guidelines: Be specific enough to verify, be observable not inferential, avoid double-barreled questions

### AI Collaboration Keys
- Ask AI to decompose vague quality dimensions (like "professional tone") into 5 binary criteria
- Have AI debug low-agreement graders by analyzing criteria ambiguity
- Generate domain-specific graders with both objective and subjective criteria

### Common Mistakes
- Using 1-5 scales (noisy, inconsistent - same response gets 3 on one run, 4 on another)
- Double-barreled questions ("Is it accurate and helpful?" - two criteria in one)
- Running LLM judges on criteria code can check (wastes money, adds noise)
- Not testing graders against edge cases (graders may score bad responses high)

### Connections
- **Builds on**: Lesson 03 (Eval dataset design with expected behaviors)
- **Leads to**: Lesson 05 (LLM-as-Judge Graders)
