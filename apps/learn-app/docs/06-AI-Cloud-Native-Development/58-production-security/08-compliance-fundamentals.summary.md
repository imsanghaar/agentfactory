### Core Concept
Compliance turns security controls into auditable evidence aligned to frameworks (SOC 2, ISO, HIPAA); it’s continuous, not a one-time checklist.

### Key Mental Models
- **Control → evidence**: Every requirement needs artifacts (policies, logs, tickets) proving enforcement.
- **Shared responsibility**: Cloud, cluster, container, and code layers each own parts of compliance.
- **Continuous assurance**: Ongoing reviews, audits, and exception tracking keep controls effective.

### Critical Patterns
- Maintain policies/runbooks for access, change, incident, and data handling; map them to technical controls.
- Enable and retain audit logs (K8s API, cloud IAM) per framework requirements.
- Track exceptions/waivers with owners and expiry; review regularly.
- Build a control matrix linking RBAC/NetworkPolicy/PSS/scanning to compliance clauses.

### Common Mistakes
- Treating compliance as paperwork without real control implementation.
- Missing audit logging/retention, leaving evidence gaps.
- Static checklists with no ownership or cadence for review.

### Connections
- **Builds on**: Security controls from earlier lessons.
- **Leads to**: Capstone secure Task API where evidence and controls are validated together.
