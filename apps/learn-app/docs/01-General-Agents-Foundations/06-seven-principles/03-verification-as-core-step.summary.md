### Core Concept
Verification must be continuous and integrated into every step of agentic workflows, not treated as a final step. AI systems are confident pattern-completers that can be wrong without knowing it, so confirming that AI-generated work matches intent is the non-negotiable step that makes agentic collaboration reliable--whether through running tests (Code) or reviewing outputs (Cowork).

### Key Mental Models
- **Continuous Verification Loop**: Generate -> Verify -> Generate -> Verify (not Generate -> Generate -> Generate -> Verify at the end). Errors caught immediately cost minutes; errors caught later cost hours.
- **Trust Zones**: Zone 1 (Unverified--verify everything), Zone 2 (Pattern-Recognized--spot-check), Zone 3 (Domain-Mastered--verify integration), Zone 4 (Never Fully Trusted--always verify thoroughly for critical systems like payments/security).
- **Risk-Based Verification**: Match verification depth to consequence of failure--catastrophic (thorough + audit), significant (tests + integration), moderate (tests), low (syntax check).
- **80/20 Rule of Verification**: Syntax check + type check + tests + quick scan = ~3 minutes total, catching ~90% of issues.
- **Confidence Trap**: AI generates incorrect code with the same certainty as correct code--there is no built-in uncertainty indicator.

### Key Facts
- **AI hallucinates APIs**: Trained on many codebases, patterns blend together, creating plausible but nonexistent method calls
- **Automated verification time**: Lint (~10s) + type-check (~30s) + tests (~2min) + obvious issue scan (~30s) = ~3 minutes to catch 90% of issues
- **Verification scales reliability**: Without verification, complexity makes systems unreliable; with continuous verification, confidence compounds with each verified success

### Critical Patterns
- Four verification strategies with increasing depth: Syntax (seconds, "does it run?"), Unit (minutes, "do functions work?"), Integration (tens of minutes, "does it work with existing code?"), Manual (variable, "does it solve the real problem?")
- The verification mindset asks four categories of questions: Functional Correctness, Integration, Security, and Maintainability
- Trust is earned through evidence, not assumed--start with thorough verification and accelerate only as track record builds
- The principle generalizes to Cowork: checking document sections exist, data is accurate, and formatting matches requirements is the same verification habit applied to non-code outputs

### Common Mistakes
- Accepting AI output because it "looks correct" without running tests (the CSV parser example: looks fine for happy path, breaks on quoted fields, empty fields, and mixed line endings)
- Treating verification as a final step rather than continuous practice (errors compound when generation happens without intermediate checking)
- Applying the same verification depth to all tasks regardless of risk (low-risk internal tools need quick checks; payment processing needs thorough audits)
- Fully trusting AI in any domain after repeated successes (critical systems like security and payments should have capped trust--always verify thoroughly)

### Connections
- **Builds on**: Principle 2 (Code as Universal Interface)--code provides the precise, testable artifacts that make verification possible through automated tests
- **Leads to**: Principle 4 (Small, Reversible Decomposition)--verification works best on small changes where the scope of what might be wrong is limited
