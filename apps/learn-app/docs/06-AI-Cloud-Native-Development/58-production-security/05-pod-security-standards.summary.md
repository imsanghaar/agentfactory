### Core Concept
Pod Security Standards (PSS) set baseline, restricted, or privileged guardrails on pod specs to enforce safe defaults across namespaces.

### Key Mental Models
- **Policy tiers**: Privileged (most permissive), Baseline, Restricted (most secure); choose per namespace/environment.
- **Admission control**: PSS (or replacements like PSA/OPA/Gatekeeper) validate pod specs before they run.
- **Shift-left**: Catch violations in CI and at admission, not in production only.

### Critical Patterns
- Label namespaces to enforce Restricted/Baseline policies; keep ops namespaces separate if needing Privileged.
- Validate pods against PSS: non-root, drop capabilities, read-only rootfs, seccomp/apparmor set.
- Add admission policies and CI checks (kubectl/OPA) to block noncompliant specs early.

### Common Mistakes
- Running everything in Privileged namespaces out of convenience.
- Forgetting to set `runAsNonRoot`, dropping capabilities, or seccomp profiles.
- Enabling PSS without testing, causing app rollout failures.

### Connections
- **Builds on**: RBAC/NetworkPolicy/Secrets management.
- **Leads to**: Image scanning, Dapr security, and capstone hardening.
