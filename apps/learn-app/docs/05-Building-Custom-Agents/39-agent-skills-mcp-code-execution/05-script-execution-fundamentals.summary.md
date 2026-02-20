### Core Concept
Write-execute-analyze loop: Generate code from spec → execute → analyze errors/output → fix → iterate until spec satisfied. This generalizes beyond MCP—arbitrary computation not covered by existing tools.

### Key Mental Models
- **Three error types**: Syntax (won't parse), Runtime (crashes during execution), Logic (wrong results)
- **Convergence criteria**: Stop when spec satisfied OR max iterations reached
- **Safety constraints**: Whitelisted directories, rate limits, timeout protection, iteration limits
- **MCP vs Script**: MCP for external tools that exist; Script for custom computation that doesn't

### Critical Patterns
- Syntax error: Parser catches before execution → regenerate that section
- Runtime error: Code runs but KeyError/TypeError → add defensive checks, inspect data first
- Logic error: No error message but wrong output → compare output to spec, fix algorithm
- Resource guards: signal.alarm(30) for timeout, ALLOWED_DIRECTORIES for filesystem, max_retries for iteration

### AI Collaboration Keys
- Error messages tell you exactly what went wrong—read them carefully
- Each iteration should fix specific problem, not regenerate blindly
- Specification quality determines whether generated code will be correct first try

### Common Mistakes
- Not checking output against spec (assumes execution = success)
- No iteration limits (infinite loops)
- Accessing files outside whitelisted directories (security hole)

### Connections
- **Builds on**: Build Your MCP-Wrapping Skill (Lesson 4)
- **Leads to**: Build Script-Execution Skill (Lesson 6)
