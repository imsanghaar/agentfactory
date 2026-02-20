# ADR-0003: Manual-First Then Programmatic Workflow Template for AI Product Management

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-11-06
- **Feature:** 002-chapter-32-redesign
- **Context:** User feedback indicated this redesign "changes how we design the book remaining work and organize daily work as AI Products managers and all chores." Chapter 32's two-climax structure establishes a fundamental workflow template: manual validation (human judgment) before programmatic automation (scale). This pattern must be documented as reusable template for remaining book chapters and daily AI Product Manager workflows.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security? YES - affects how all future book content is organized and how AI Product Managers structure daily work
     2) Alternatives: Multiple viable options considered with tradeoffs? YES - automation-first, manual-only, simultaneous
     3) Scope: Cross-cutting concern (not an isolated detail)? YES - applies to remaining 23 book chapters and daily workflow patterns
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Establish **Manual-First → Programmatic** as the standard workflow template for:
1. **Remaining book chapter design** (Chapters 33-55)
2. **Daily AI Product Manager workflows** (how to organize work, delegate tasks, validate quality)
3. **SpecKit Plus SDD loop evolution** (Spec → Plan → Tasks → Implement → Validate)

**Template Structure**:

**Phase 1: MANUAL VALIDATION (Human Judgment Required)**
- Learn the pattern/workflow/concept through hands-on experience
- Understand WHY it works through manual execution
- Develop intuition and judgment (can recognize good vs bad quality)
- Establish baseline metrics (time, quality, success criteria)
- Success criteria: Can execute manually and explain reasoning

**Phase 2: PROGRAMMATIC AUTOMATION (Scale Through Tooling)**
- Automate the validated pattern using tools/scripts
- Preserve human judgment at key decision points (approval gates)
- Scale what was proven manually (3x → 10x → 50x)
- Monitor automated execution for quality drift
- Success criteria: Automation amplifies quality, doesn't replace judgment

**Application to Chapter 32**:
- MANUAL PHASE (Lessons 1-4, FIRST CLIMAX): Experience decomposition thinking through manual parallel workflows
- PROGRAMMATIC PHASE (Lessons 5-8, SECOND CLIMAX): Automate via headless mode, sandboxing, Super Orchestrator
- VALIDATION PHASE (Lesson 9): Prove mastery with choice (manual OR programmatic)

**Application to Remaining Book Chapters**:
- Chapter 33+: Teach concept manually → Show automation pathway → Student chooses approach
- Example: Database migrations (manual SQL first → automation tools second)
- Example: Deployment pipelines (manual docker build/push first → CI/CD automation second)
- Example: Monitoring setup (manual log inspection first → automated dashboards second)

**Application to Daily AI Product Manager Workflows**:
- Feature specification: Write first spec manually → Use templates/automation for subsequent specs
- Code review: Review first 3-5 PRs manually → Establish automated quality gates for remaining PRs
- Testing: Write first tests manually → Generate additional tests via AI with human validation
- Documentation: Write first docs manually → Use AI to expand/maintain with human editing

**Organizational Principle**:
> "Manual first teaches judgment. Programmatic second teaches scale. Skip manual = automation without understanding. Skip programmatic = judgment without leverage."

## Consequences

### Positive

- **Transferable template**: All remaining chapters can follow same Manual → Programmatic progression
- **Clear AI Product Manager workflow**: Organize daily work as "validate manually, then scale programmatically"
- **Prevents premature automation**: Human judgment established before automation (avoids "automated chaos")
- **Scalable learning**: Students build intuition (manual) before tools (programmatic)
- **Portfolio differentiation**: Students who complete both phases demonstrate judgment AND automation capability
- **Risk mitigation**: Manual phase catches problems before automation amplifies them
- **Explicit skill progression**: Recognition (watch demo) → Application (manual execution) → Automation (programmatic scale)
- **Daily chore organization**: AI Product Managers know when to do work manually vs when to automate

### Negative

- **Longer timeline**: Manual phase adds time before automation benefits (mitigated by making automation phase optional for time-constrained students)
- **Impatient students**: Some want to "skip to automation" (mitigated by gating automation on manual understanding)
- **Perceived redundancy**: "Why learn manual if I'll automate it?" (mitigated by emphasizing judgment development)
- **Implementation overhead**: Every remaining chapter must follow template (increases planning complexity)
- **Risk of dogma**: Template might not fit all topics (mitigated by allowing exceptions with ADR justification)

## Alternatives Considered

**Alternative A: Automation-First Template**
- Structure: Teach programmatic automation from start, skip manual phase entirely
- Why rejected: Students learn syntax without judgment - can run scripts but can't recognize quality problems
- Tradeoff: Faster initial learning but weaker foundation, higher risk of "automated bad practices"
- Example failure mode: Student automates deployment without understanding rollback strategies

**Alternative B: Manual-Only Template (No Automation Phase)**
- Structure: Teach manual execution, never show automation pathway
- Why rejected: Students don't see path to scale - learn patterns but can't apply at 10x-50x multiplier
- Tradeoff: Deeper judgment but limited leverage
- Example limitation: Student can coordinate 3 features manually but can't envision coordinating 15

**Alternative C: Simultaneous Manual + Programmatic**
- Structure: Teach manual and programmatic approaches in same lesson, let students choose
- Why rejected: Cognitive overload - students trying to learn two approaches simultaneously
- Tradeoff: Appears more flexible but actually overwhelming
- Example confusion: "Should I learn bash script or do it manually? I don't know which is better."

**Alternative D: Programmatic with Manual Fallback**
- Structure: Teach automation first, provide "manual instructions if automation fails"
- Why rejected: Positions manual as "fallback" rather than foundation - students skip manual, lack judgment
- Tradeoff: Appears efficient but produces students dependent on automation without understanding

**Alternative E: Topic-Dependent (No Standard Template)**
- Structure: Some chapters manual-first, some automation-first, decided case-by-case
- Why rejected: Inconsistent learning progression - students can't predict chapter structure
- Tradeoff: More flexibility but loses pedagogical coherence across book

## References

- Feature Spec: `/Users/mjs/Documents/code/panaversity-official/tutorgpt-build/bbb/specs/002-chapter-32-redesign/spec.md`
- Implementation Plan: `/Users/mjs/Documents/code/panaversity-official/tutorgpt-build/bbb/specs/002-chapter-32-redesign/plan.md`
- Implementation Tasks: `/Users/mjs/Documents/code/panaversity-official/tutorgpt-build/bbb/specs/002-chapter-32-redesign/tasks.md`
- Related ADRs:
  - ADR-0001 (Two-Climax Pedagogical Structure) - demonstrates template in practice
  - ADR-0002 (SpecKit Plus Workflow Focus) - defines what "workflow" means in this context
- Evaluator Evidence:
  - User feedback establishing organizational scope: "Let's document as this changes how we design the book remaining work and organize daily work as AI Products managers and all chores"
  - PHR 0005: Manual → Programmatic progression validated through two-climax design

## Implementation Guidance for Remaining Chapters

**For Chapter Authors**:
1. Identify core pattern/workflow to teach
2. Design MANUAL PHASE: How do students learn this hands-on?
3. Design PROGRAMMATIC PHASE: What tools/automation amplify the manual pattern?
4. Validate: Does manual phase teach judgment? Does programmatic phase preserve judgment while adding scale?

**For AI Product Managers (Daily Workflow)**:
1. New task/project: Execute first instance manually to understand pattern
2. Establish quality criteria through manual validation
3. Identify repetitive elements suitable for automation
4. Automate with human checkpoints at key decision points
5. Monitor automated results, adjust automation when quality drifts

**Exception Criteria** (when template doesn't apply):
- Topic is purely conceptual (no manual vs programmatic distinction)
- Automation is inherently unsafe (security-critical manual steps)
- Manual approach is deprecated/obsolete (automation is industry standard)
- Document exception with separate ADR justifying deviation from template
