### Core Concept
Build a skill that automates write-execute-analyze loop. Components: generate_code from spec, execute_code with timeout, analyze_error, generate_fix, check_convergence. Test with clean data, malformed data, empty files, and large files.

### Key Mental Models
- **Spec-driven generation**: Complete specification = AI generates correct code without clarification
- **Component architecture**: Code generation → Execution → Error analysis → Fix generation → Convergence check
- **Five-scenario testing**: Clean (happy path), Missing columns, Wrong types, Empty file, Large file
- **Convergence validation**: All required fields present + correct format + no errors + edge cases handled

### Critical Patterns
- Main loop: While iteration &lt; max: generate/execute/check convergence; if error: analyze/fix/retry
- Execution safety: subprocess with timeout, capture stdout/stderr, return (success, output, error)
- Convergence check: Parse output, verify required fields, validate format, check domain constraints
- Error recovery prompts: Show error + code + spec → ask for specific fix

### AI Collaboration Keys
- Three prompt types: Design recovery patterns, Implement convergence testing, Stress-test with intentional failures
- Testing failures matters more than testing success
- Recovery isn't magic—it's spec clarity + intelligent prompting + validation

### Common Mistakes
- Incomplete specification (AI guesses, generates wrong code)
- No convergence check (keeps iterating after spec satisfied)
- Not testing error recovery (only testing happy path)

### Connections
- **Builds on**: Script Execution Fundamentals (Lesson 5)
- **Leads to**: Full Workflow Orchestration (Lesson 7)
