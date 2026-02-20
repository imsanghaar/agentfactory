### Core Concept
Move beyond local Docker Desktop to real cloud environments, addressing differences in networking, storage, IAM, and reliability.

### Key Mental Models
- **Local vs cloud gaps**: Load balancers, persistent volumes, IAM, and multi-node behaviors differ from local clusters.
- **Shared responsibility**: Cloud provider services (LB, storage, DNS) must be configured securely.
- **Parity mindset**: Keep dev/prod patterns aligned while respecting cloud realities.

### Critical Patterns
- Plan for cloud load balancers, persistent storage classes, and external DNS/cert management.
- Update manifests/Helm values for cloud-specific settings (node selectors, tolerations, storage).
- Validate connectivity and security (NetworkPolicies, ingress) in multi-node setups.

### Common Mistakes
- Assuming local defaults (NodePort, hostPath) work in cloud.
- Ignoring IAM and network boundaries, leaving services exposed.
- Not testing multi-node scheduling/taints leading to deployment failures.

### Connections
- **Builds on**: Skill-first deployment setup.
- **Leads to**: Cloud account setup, cluster provisioning, and DNS/LB configuration.
