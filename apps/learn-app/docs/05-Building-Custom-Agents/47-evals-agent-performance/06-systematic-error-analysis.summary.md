### Core Concept
Less experienced teams spend too much time building and too little time analyzing. Systematic error counting reveals which component causes most failures, preventing wasted effort fixing the wrong thing. 30 minutes counting errors beats 30 hours fixing the wrong component.

### Key Mental Models
- Trace: All intermediate outputs from a single agent run (the complete journey)
- Span: Output of a single step within a trace (one leg of the journey)
- Build-Analyze loop: Run evals -> Error analysis -> Identify failing component -> Fix -> Re-eval
- Prioritization formula: Priority = Frequency x Feasibility

### Critical Patterns
- Spreadsheet method: Columns for each component/span, mark OK or ERROR, count Error Location column
- Error attribution: Identify which span FIRST introduced the error (downstream spans inherit upstream errors)
- Counting corrects biases: Availability bias (recent errors feel common), confirmation bias (errors matching your theory), expertise bias (focus on familiar components)
- Feasibility estimation: 0.9-1.0 (trivial fix), 0.5-0.6 (known approach, days), 0.0-0.2 (unknown cause)

### AI Collaboration Keys
- Have AI design error categories specific to your agent's component architecture
- Use AI to estimate feasibility for your error types (what does fixing actually involve?)
- Generate framework-specific error analysis code with AI

### Common Mistakes
- Guessing which component to fix instead of counting errors systematically
- Fixing the last error you saw or the failure that frustrated you most
- Working on components you understand best regardless of failure frequency
- Confusing symptom location with root cause (trace back through upstream components)

### Connections
- **Builds on**: Lesson 05 (Graders that detect failures)
- **Leads to**: Lesson 07 (Component vs End-to-End Evals)
