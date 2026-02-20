### Core Concept

Finance subagents apply the orchestration pattern from Chapter 3 to create specialized AI assistants that mirror how finance teams actually work. Five key roles emerge: Financial Modeler (forecasts), Scenario Analyst (what-if), Risk Assessor (stress tests), Validator (integrity checks), and Narrative Generator (stakeholder communications). Each subagent has isolated context and focused expertise, coordinated by Claude Code like a project manager delegating to team members.

### Key Mental Models

- **Finance Team Analogy**: Human specialists (FP&A analyst, risk manager, controller, CFO) map to AI subagent roles—orchestration mirrors real team dynamics
- **Isolated Context Advantage**: Each subagent starts clean, uncluttered by previous conversations, producing more focused results
- **Orchestration Patterns**: Sequential (quality depends on order), Parallel (independent tasks), Conditional (exception-based routing)
- **Complexity Threshold**: "Would I delegate this to different team members?" If yes, use multi-agent; if one person handles it, use single conversation

### Key Facts

- **Five finance subagent roles**: Financial Modeler, Scenario Analyst, Risk Assessor, Validator, Narrative Generator
- **Month-end close example**: Sequential flow (Validator → Modeler → Analyst → Assessor → Narrative) reduces 5-7 hours to 30 minutes of review
- **Board prep example**: Parallel execution (Modeler + Analyst + Assessor) then sequential validation and narrative
- **Context handoffs**: Validator findings inform Risk Assessor, Modeler outputs feed Scenario Analyst, all quantitative outputs reach Narrative Generator

### Critical Patterns

- **Sequential orchestration**: Step-by-step with output from one becoming input to next (month-end close)
- **Parallel orchestration**: Independent tasks run simultaneously (board meeting prep)
- **Conditional orchestration**: Subagent invocation depends on prior results (Risk Assessor only runs when Validator finds anomalies)
- **Start small**: Begin with one or two subagents addressing biggest pain points, add more as you master orchestration

### Common Mistakes

- Building all five subagents at once instead of starting with highest-impact one
- Forgetting that subagent outputs are still suggestions requiring human approval
- Unclear context handoffs—each subagent needs explicit information about what flows between them
- Using multi-agent complexity when single-agent conversation would suffice (setup overhead exceeds time saved)

### Connections

- **Builds on**: Chapter 3 Lesson 11 (subagents and orchestration), Lesson 3 (finance skills), Lesson 9 (governance)
- **Leads to**: Capstone Finance Digital FTE where all subagents, skills, MCP connections, and governance combine into complete system
