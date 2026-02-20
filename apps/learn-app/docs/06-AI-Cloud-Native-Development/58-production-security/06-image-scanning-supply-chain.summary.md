### Core Concept
Secure the supply chain by scanning images, pinning provenance, and controlling what reaches the cluster through signed artifacts and policy enforcement.

### Key Mental Models
- **Shift-left scanning**: Scan during build and admission to stop known CVEs early.
- **Provenance and signing**: Use SBOMs and signatures (Cosign) to verify source and integrity.
- **Registry and policy gates**: Allow only trusted registries/images via admission controls.

### Critical Patterns
- Integrate scanners (Trivy/Grype) into CI; fail builds on critical vulnerabilities.
- Generate SBOMs, sign images with Cosign, and verify signatures at admission (e.g., Policy Controller/Gatekeeper).
- Restrict image pull to approved registries and tags (SHA-pins, no `latest`).
- Automate patch cadence and rescans; track exceptions with expiry.

### Common Mistakes
- Pulling unsigned images from public registries without verification.
- Allowing `latest` tags or mutable tags in production.
- Treating one-time scans as sufficient; skipping admission verification.

### Connections
- **Builds on**: PSS, RBAC, secrets, network policies.
- **Leads to**: Dapr security and capstone secure Task API deployment.
