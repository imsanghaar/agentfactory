### Core Concept
Build a personal cloud lab on Hetzner (or similar) to replicate production patterns cost-effectively while practicing real-world provisioning and security.

### Key Mental Models
- **Portable patterns**: Reuse IaC, networking, and security setups across providers.
- **Cost-aware labs**: Choose sizes/regions and automation that keep lab spend low.
- **Isolation**: Keep lab resources separate from production to avoid accidental impact.

### Critical Patterns
- Provision nodes/networking/firewalls via Hetzner APIs/IaC; secure SSH and access.
- Install Kubernetes or target stack with the same ingress/TLS/secrets patterns as prod.
- Monitor costs and automate teardown/scale-down when idle.

### Common Mistakes
- Reusing prod credentials or mixing prod/test resources.
- Leaving lab resources running idle, driving unexpected bills.
- Skipping security basics (firewalls/MFA) because it’s “just a lab.”

### Connections
- **Builds on**: Cloud deployment skills and DO provisioning patterns.
- **Leads to**: Final checklist and full production capstone readiness.
