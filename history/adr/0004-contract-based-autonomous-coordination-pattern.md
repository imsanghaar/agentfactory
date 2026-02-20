# ADR-0004: Contract-Based Autonomous Coordination Pattern

> **Scope**: This ADR documents the decision to use explicit integration contracts (contract.md) + completion hooks as the coordination mechanism for autonomous AI agent teams, rather than synchronous communication or implicit coordination.

- **Status:** Accepted
- **Date:** 2025-11-06
- **Feature:** 002-chapter-32-redesign
- **Context:** When coordinating 5-10 autonomous AI agents building independent features in parallel, we need a coordination mechanism that enables true autonomy (agents work without constant human supervision) while ensuring clean integration. The key pedagogical insight is teaching students that **good contracts eliminate coordination overhead**, a pattern transferable from AI agents → junior developers → distributed teams → organizational scaling.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: YES - Long-term consequence for how all multi-agent coordination works in Chapter 32 and future production systems
     2) Alternatives: YES - Multiple viable options considered (message passing, shared state, synchronous meetings, implicit coordination)
     3) Scope: YES - Cross-cutting concern affecting Lessons 6-8 and transferable to real-world team coordination
-->

## Decision

Use **Contract-Based Autonomous Coordination** as the primary pattern for multi-agent orchestration:

**Components of the Pattern:**

1. **contract.md artifact**: Explicit integration contract defining:
   - Feature boundaries ("What does this feature own?")
   - Integration points ("How do features connect?")
   - Acceptance criteria ("When is this feature done?")
   - Dependencies ("What must exist before this feature works?")

2. **Completion hooks**: Async notification mechanism:
   - Each agent session writes completion status to shared file (orchestrator-status.log)
   - Main orchestrator polls for ALL_COMPLETE signal
   - Human reviews results at checkpoints, not continuously

3. **Sandboxing**: OS-level isolation ensuring agents can't interfere with each other

4. **Shared constitution**: Quality standards preventing drift across parallel work

**Workflow:**
```
Phase 1: Human + AI co-create contract.md via /sp.specify
Phase 2: SpecKit Plus generates plan.md and tasks.md referencing contract
Phase 3: Agents work autonomously reading contract.md
Phase 4: Hooks notify completion → Human reviews
Phase 5: Integration validation against contract
```

## Consequences

### Positive

1. **True Autonomy**: Agents work without constant human monitoring (enabling creative independence)
2. **Async Coordination**: No synchronous meetings/check-ins required (scales to 7-9 agents)
3. **Integration Quality**: Explicit contracts catch boundary violations early (clean merges prove good contracts)
4. **Transferable Pattern**: Same pattern works for coordinating junior developers, distributed teams, organizational units
5. **Teachable**: Contract-first thinking is learnable skill (not tool-specific knowledge)
6. **Measurable**: Integration conflicts quantify contract quality (0 conflicts = excellent contracts)

### Negative

1. **Upfront Investment**: Writing good contracts takes 2-3x longer than "just start coding" (honest expectation setting required)
2. **Learning Curve**: Students must learn contract thinking, not just technical execution
3. **Contract Maintenance**: Contracts must evolve with system (stale contracts → integration problems)
4. **Not Always Beneficial**: Overkill for 1-2 features; value appears at 3+ independent units

## Alternatives Considered

### Alternative A: Synchronous Coordination (Traditional Team Meetings)
**Approach**: Agents communicate via shared chat/meetings, coordinate in real-time

**Why Rejected**:
- Defeats parallelization benefit (coordination overhead scales with N²)
- Doesn't teach decomposition thinking (relies on constant communication)
- Not transferable to async/distributed work
- Creates bottleneck at 5+ agents (too many meetings)

### Alternative B: Message-Passing Coordination (Event-Driven)
**Approach**: Agents publish events, subscribe to relevant streams, coordinate via messages

**Why Rejected**:
- Too complex for intermediate learners (introduces event-driven architecture prematurely)
- Requires additional infrastructure (message broker, event schema)
- Obscures core insight (good boundaries enable autonomy)
- Better suited for Parts 12-13 (event-driven architecture lessons)

### Alternative C: Shared State Coordination (Database/Store)
**Approach**: Agents write to shared database, poll for dependencies, coordinate via state

**Why Rejected**:
- Introduces data consistency challenges (race conditions, locking)
- Requires database setup (scope creep for Chapter 32)
- Implicit coordination (doesn't teach explicit boundary thinking)
- Harder to debug integration problems

### Alternative D: Implicit Coordination (Hope for the Best)
**Approach**: No explicit contracts, agents infer integration points from specs

**Why Rejected**:
- Guarantees integration conflicts (students experience pain, not learning)
- Doesn't scale beyond 2-3 features (implicit assumptions break down)
- Teaches wrong lesson ("parallelization is chaotic")
- Wastes time on avoidable merge conflicts

## Why Contract-Based Wins

**Decision Rationale**:
1. **Explicit > Implicit**: Contracts make integration points visible (easier to validate, debug, improve)
2. **Scales Well**: Coordination overhead remains constant as agents increase (not N²)
3. **Pedagogically Sound**: Teaches transferable decomposition thinking (not tool proficiency)
4. **Honest Tradeoffs**: Upfront contract time investment yields 10x overall gains (measurable via time tracking)
5. **Production-Ready Pattern**: Same pattern used by Anthropic, Vercel, distributed engineering teams

## References

- Feature Spec: `specs/002-chapter-32-redesign/spec.md` (User Stories 1-3)
- Implementation Plan: `specs/002-chapter-32-redesign/plan.md` (Lessons 6-7)
- Refactored Tasks: `specs/002-chapter-32-redesign/tasks-REFACTORED.md` (Task 4.1, 4.2)
- Related ADRs:
  - ADR-0001 (Two-Climax Structure - L6-7 deliver SECOND CLIMAX)
  - ADR-0002 (SpecKit Plus as Orchestrator - /sp.specify generates contracts)
  - ADR-0003 (Manual-First Progression - L5 motivates need for contracts)
- Evaluator Evidence: Contract quality measured via merge conflicts (0 conflicts = excellent contracts)
