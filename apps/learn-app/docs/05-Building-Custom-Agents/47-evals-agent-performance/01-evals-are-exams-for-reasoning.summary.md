### Core Concept
TDD tests whether code produces correct outputs (deterministic PASS/FAIL), while Evals test whether agents make the right decisions (probabilistic scores) - like the difference between testing if a calculator works versus testing if a student knows when to use multiplication.

### Key Mental Models
- Calculator vs Student: TDD checks if the calculation is correct, Evals check if the student chose the right operation
- Probabilistic outcomes: Same prompt can produce varying quality responses due to model randomness, context interpretation, and ambiguity
- Eval-driven development loop: Build -> Eval -> Error Analysis -> Fix -> Re-eval -> Ship
- Initial Evals are "final exams"; Regression Evals are "pop quizzes"

### Critical Patterns
- Use TDD for deterministic correctness: API returns valid JSON, authentication works, database connects
- Use Evals for judgment calls: intent interpretation, tool selection, output quality, context handling
- Rule of thumb: exactly one correct answer = TDD; range of acceptable answers requiring judgment = Evals
- Evals produce scores (0.0 to 1.0), not binary verdicts

### AI Collaboration Keys
- Ask AI to give examples of behaviors that seem testable but actually need evaluation
- Have AI classify your agent's behaviors into TDD vs Evals categories
- Challenge analogies with AI to understand their limitations

### Common Mistakes
- Running test suite and assuming agent works because all tests pass (missing reasoning failures)
- Treating agent quality as binary (works/doesn't work) instead of as a spectrum
- Skipping the eval-driven development loop and guessing what to fix

### Connections
- **Builds on**: Lesson 00 (Skill-First approach, LEARNING-SPEC)
- **Leads to**: Lesson 02 (The Two Evaluation Axes)
