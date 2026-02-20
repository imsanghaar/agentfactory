### Core Concept
Run your full eval suite on every change. Before any code ships, you know whether it improved things, broke things, or left quality unchanged. The eval suite becomes your safety net against the regression trap where improvements in one area cause regressions in another.

### Key Mental Models
- Regression trap: Improvements in one area (routing) often break another area (output formatting)
- Baseline before change: Record current state before modifying any agent code
- Hidden regressions: Overall score can improve while individual criteria regress - improvements mask problems
- Threshold by criticality: High-stakes (any drop = block), Normal (5% = investigate), Experimental (10% = investigate)

### Critical Patterns
- Eval-on-every-change workflow: Change code -> Run eval suite -> Compare to baseline -> Investigate if drop > threshold
- Before/after comparison: Track overall delta AND per-criterion deltas
- Hidden regression detection: Check per-criterion even when overall improves
- Iteration loop: Identify lowest-scoring criterion -> Fix that specific component -> Re-eval -> Repeat

### AI Collaboration Keys
- Design regression protection specific to your agent's criticality level
- Debug masked regressions by analyzing per-criterion breakdown
- Build iteration plan to reach target pass rate with AI-assisted prioritization

### Common Mistakes
- Not establishing baseline before making changes (cannot compare)
- Only checking overall pass rate (misses hidden per-criterion regressions)
- Using same thresholds for all agents regardless of criticality
- Shipping improvements without verifying no regressions in other areas

### Connections
- **Builds on**: Lesson 07 (E2E verification after component tuning)
- **Leads to**: Lesson 09 (The Complete Quality Loop)
