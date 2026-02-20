### Core Concept
E2E evals tell you IF there's a problem (noisy signal from multiple variance sources); component evals tell you WHERE the problem is (clear signal from isolated single component). Use E2E for ship decisions and monitoring; use component evals for debugging and tuning.

### Key Mental Models
- Noise problem: Each component introduces variance; with 4 components at 90% each, E2E reliability is only 65.6%
- E2E finds problems; Component evals FIX problems
- Gold standard resources: Known-good inputs and expected outputs for testing components in isolation
- Component evals run fast (seconds); E2E runs slow (full workflow) - enables rapid iteration

### Critical Patterns
- 5-Step Decision Flow: (1) E2E eval for baseline, (2) Error analysis identifies component, (3) Build component eval, (4) Tune with component eval (fast iteration), (5) Verify with E2E
- Component eval structure: Provide known-good inputs, check for expected outputs, no upstream/downstream variance
- Use E2E for: Ship decisions, monitoring, validating component integration, regression tests
- Use Component for: Debugging specific failures, tuning single behaviors, fast iteration

### AI Collaboration Keys
- Have AI design your component eval strategy based on error patterns
- Create gold standard datasets for specific components with AI help
- Walk through the 5-step flow with AI to ensure systematic improvement

### Common Mistakes
- Only using E2E evals (too noisy for debugging - cannot isolate which component failed)
- Skipping E2E verification after component improvement (components might work in isolation but fail when integrated)
- Not creating gold standard resources for component evals (need known-correct inputs and outputs)
- Trying to tune components with E2E feedback (too slow, too noisy)

### Connections
- **Builds on**: Lesson 06 (Error analysis identifying problem components)
- **Leads to**: Lesson 08 (Regression Protection)
