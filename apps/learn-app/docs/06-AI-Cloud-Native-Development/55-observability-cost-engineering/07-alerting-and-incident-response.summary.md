### Core Concept
Multi-window, multi-burn-rate alerting replaces noisy threshold alerts by asking "how fast are we burning error budget?" and requiring both short (5m) and long (1h) windows to confirm sustained problems before paging.

### Key Mental Models
- **Burn Rate**: error_rate / error_budget; 14.4x consumes 2% budget in 1 hour, 6x consumes 5% in 6 hours
- **Multi-Window**: Short window (5m) detects quickly; long window (1h) confirms not a spike; both must be true
- **Severity Levels**: Critical = page immediately (PagerDuty), Warning = next business day (Slack), Info = dashboard only
- **Actionability Test**: Is it actionable? Is it urgent? Is there a runbook? If any "no", don't page

### Critical Patterns
- Critical alert: `error_ratio:rate5m > 14.4 * 0.001 AND error_ratio:rate1h > 14.4 * 0.001`
- Warning alert: `error_ratio:rate30m > 6 * 0.001 AND error_ratio:rate6h > 6 * 0.001`
- Alertmanager routing: match severity and slo labels to route to PagerDuty vs Slack
- Runbook annotations: `runbook_url` and `dashboard_url` in alert annotations

### AI Collaboration Keys
- Ask Claude to review burn rate thresholds for your SLO and business needs
- Request runbook generation with diagnostic commands, decision tree, and escalation path
- Have AI design Alertmanager routing tree for multi-severity, multi-team alerting

### Common Mistakes
- Using threshold alerting (error_rate > 1%) instead of burn rate (causes alert fatigue)
- Not using both short and long windows (false positives from brief spikes)
- Paging without a runbook (responder wastes time figuring out what to do)

### Connections
- **Builds on**: Lesson 6 - SRE Foundations: SLIs, SLOs, and Error Budgets
- **Leads to**: Lesson 8 - Cost Engineering and FinOps
