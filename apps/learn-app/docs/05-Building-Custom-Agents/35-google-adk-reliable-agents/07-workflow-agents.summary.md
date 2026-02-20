### Core Concept
Workflow agents sacrifice LLM flexibility for deterministic execution. SequentialAgent guarantees order, ParallelAgent enables concurrency for independent tasks, LoopAgent supports iterative refinement with exit conditions.

### Key Mental Models
- **LLM routing = flexible but unpredictable**: Can't guarantee order, hard to test
- **Workflow agents = deterministic**: Fixed execution path, predictable testing
- **Trade-off axis**: Flexibility (routing) vs Predictability (workflow agents)

### Critical Patterns
- Sequential: `SequentialAgent(sub_agents=[researcher, writer, editor])`
- Parallel: `ParallelAgent(sub_agents=[fact_checker, sentiment_analyzer])`
- Loop: `LoopAgent(sub_agents=[generator], max_iterations=5)` with `exit_loop` tool
- Composite: Sequential containing Parallel, Loop within Parallel

### AI Collaboration Keys
- Use routing for novel decisions requiring adaptability
- Use workflow agents for standardized, repeatable processes
- Hybrid: Routing decides WHICH workflow to invoke

### Common Mistakes
- Parallelizing dependent tasks (Task B needs Task A's output)
- No max_iterations on LoopAgent (infinite loop risk)
- Using workflow agents when flexibility is actually needed

### Connections
- **Builds on**: Multi-Agent Orchestration (Lesson 6)
- **Leads to**: Capstone News Podcast (Lesson 8)
