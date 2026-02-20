### Core Concept
Spec-Driven Development (SDD) is a methodology where you write complete specifications before writing code, then AI agents implement against those specifications while you focus on design, architecture, and validation. The core equation: vague idea + AI = 5+ iterations of misalignment; clear specification + AI = 1-2 iterations of refinement. The bottleneck has shifted from implementation to specification quality.

### Key Mental Models
- **SDD Six-Phase Workflow**: Specify (define what/why) -> Clarify (remove ambiguity) -> Plan (design how) -> Tasks (break down work) -> Implement (AI executes) -> Validate (verify quality). Each phase removes ambiguity before the next begins.
- **Four Specification Qualities**: Clarity (no ambiguity -- measurable, not vague), Completeness (all scenarios covered -- functional, non-functional, integration), Constraints (explicit boundaries -- technical, business, design), Testability (every criterion verifiable -- quantified, not subjective).
- **SDD vs Vibe Coding**: SDD invests 20% time specifying and 80% building; Vibe Coding spends 80% coding and 20% fixing. SDD scales to complex systems; Vibe Coding falls apart beyond 1,000 lines.
- **AI Asks During Planning, Not Implementation**: With SDD, clarifying questions happen in the Clarify phase. Without SDD, AI must guess requirements during implementation, causing misalignment iterations.
- **Decision Framework for SDD Depth**: Full SDD (production features, complex systems, security-critical), Lightweight SDD (simple utilities, prototypes, well-understood patterns), Skip SDD (learning experiments, throwaway code, trivial changes).

### Key Facts
- **Specification has four elements**: Intent (why this exists), Success Criteria (what correct looks like), Constraints (limits that exist), Non-Goals (what we are NOT building)
- **Quality gate phases**: Each of the six phases has explicit pass/fail criteria before proceeding to the next
- **Developer A vs B comparison**: Developer A (code-first) spends 3 months debugging edge cases; Developer B (spec-first) has complete tested implementation in 2 weeks and builds features in months 2-3
- **Vibe Coding works for**: Learning new frameworks, prototyping throwaway code, simple scripts under 50 lines
- **SDD is essential for**: Production features, multi-component systems, security/compliance requirements, AI-assisted development, team projects
- **Task sizing rule**: No single task should exceed 2 hours of work

### Critical Patterns
- The specification document structure: Intent (user problem solved) -> Success Criteria (measurable outcomes) -> Constraints (performance, security, compliance, scale) -> Non-Goals (explicit scope boundaries preventing creep)
- The Clarify phase catches unknowns before they become expensive: edge cases, integration points, error handling specifics, business logic ambiguities
- The Plan includes architecture, dependency sequence, testing strategy, and documented tradeoffs with rationale
- Validation confirms implementation matches specification across all success criteria, constraints, edge cases, and quality gates

### Common Mistakes
- Writing the spec after the code (turns specification into retrospective documentation rather than a guide that drives implementation quality)
- Using vague success criteria like "user-friendly" or "good performance" instead of measurable criteria like "95th percentile response time < 200ms" or "new users complete in < 60 seconds"
- Skipping Non-Goals (without explicit scope boundaries, every conversation becomes "should we add X?" leading to scope creep)
- Treating specs as static documents rather than living artifacts that update when requirements change (spec-implementation drift makes both unreliable)

### Connections
- **Builds on**: The orchestrator role (Lesson 2) where specification writing is the primary skill; the Nine Pillars (Lesson 6) where SDD is Pillar 7 orchestrating all others; AIDD characteristics (Lesson 6) including Specification-Driven, Quality-Gated, and Human-Verified
- **Leads to**: The Synthesis lesson (Lesson 8) where SDD is positioned as the methodology enabling reliable Digital FTE delegation; practical SDD workflows in later chapters where students execute the six phases on real features
