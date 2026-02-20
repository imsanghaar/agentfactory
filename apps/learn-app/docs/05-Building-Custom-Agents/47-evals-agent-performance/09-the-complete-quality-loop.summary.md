### Core Concept
Agent development alternates between Building (prompts, tools, guardrails) and Analysis (evals, error patterns, measurement). Successful agent builders flip the typical 90/10 building/analysis ratio - more time understanding WHY failures occur leads to faster shipping.

### Key Mental Models
- Two Activities Framework: Building mode vs Analysis mode - analysis time is investment that prevents wasted effort
- The 10-step loop: Build -> Dataset -> Evals -> Error Analysis -> Fix -> Re-eval -> Decision -> Deploy -> Monitor -> Grow dataset
- Ship decision factors: Pass rate, improvement trajectory, failure mode (graceful vs confident-wrong), user stakes
- Quality-first optimization order: Quality THEN latency THEN cost - never optimize before quality threshold is met

### Critical Patterns
- Iteration pattern: Target lowest-scoring component each cycle (highest leverage improvement)
- Ship thresholds: 95%+ (high-stakes), 90-95% (normal), 80-90% (low-stakes with monitoring), 70-80% (prototypes only)
- Diminishing returns: If stuck at same level for 3+ iterations, consider shipping if above 85%
- Cost optimization rule: Run full eval suite after ANY optimization; reject if quality drops more than 2%

### AI Collaboration Keys
- Analyze your current development process against the 10-step loop with AI
- Have AI help make ship/iterate decisions based on context factors
- Plan optimization phase systematically with AI (what to try, in what order)

### Common Mistakes
- 90% time building, 10% analyzing (invert this ratio for faster shipping)
- Optimizing for cost/latency before quality meets threshold
- Shipping based on pass rate alone without considering failure mode and trajectory
- Treating the loop as linear rather than continuous (production failures feed back into dataset)

### Connections
- **Builds on**: Lessons 01-08 (All evaluation components synthesized)
- **Leads to**: Lesson 10 (Finalize Your Evals Skill)
