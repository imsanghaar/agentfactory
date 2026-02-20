### Core Concept
Right-sizing with Vertical Pod Autoscaler (VPA) replaces guesswork for requests/limits by recommending or applying values based on observed usage.

### Key Mental Models
- **Measure, then adjust**: Use recommendation mode before automatic updates.
- **Safety bounds**: Set min/max to avoid runaway allocations.
- **Iterative tuning**: Revisit recommendations as workloads change.

### Critical Patterns
- Deploy VPA components; start with `updateMode: Off` to gather safe recommendations.
- Apply suggested requests/limits and re-measure; consider HPA interplay.
- Exclude bursty/latency-sensitive pods or cap adjustments with policies.

### Common Mistakes
- Enabling auto-update without bounds, causing thrash or resource spikes.
- Ignoring VPA when HPA is present—ensure signals don’t conflict.
- Using short windows that misrepresent typical load patterns.

### Connections
- **Builds on**: Cost fundamentals and observability data.
- **Leads to**: Opencost visibility, budget alerts, and overall FinOps practices.
