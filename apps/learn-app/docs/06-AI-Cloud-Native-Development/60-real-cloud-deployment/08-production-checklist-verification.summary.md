### Core Concept
Use the production checklist to verify every cloud deployment requirement—security, networking, observability, and operations—is implemented and tested before go-live.

### Key Mental Models
- **Evidence-based**: Each item needs proof (commands, dashboards, manifests).
- **Cross-layer coverage**: Networking, auth, secrets, SLOs, backups, and runbooks all matter.
- **Gatekeeper**: Checklist completion is a release gate, not a suggestion.

### Critical Patterns
- Validate ingress/TLS, RBAC/NetworkPolicies, secrets sourcing, and resource limits.
- Confirm observability (metrics/logs/traces), alerts, backups/restore tests, and autoscaling.
- Record ownership and links to evidence for auditability.

### Common Mistakes
- Checking boxes without verification artifacts.
- Ignoring operational items (runbooks, paging, on-call) while focusing only on manifests.
- Skipping negative tests (failing pods, blocked traffic) to prove controls work.

### Connections
- **Builds on**: Prior deployment and security lessons.
- **Leads to**: Final capstone deployment and ongoing production posture.
