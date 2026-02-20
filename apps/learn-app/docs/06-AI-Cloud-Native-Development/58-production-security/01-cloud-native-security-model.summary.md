### Core Concept
Kubernetes security is defense-in-depth across four concentric layers—Cloud, Cluster, Container, Code—and the weakest outer layer invalidates protections inside, so controls must be mapped and enforced per layer.

### Key Mental Models
- **4C layers**: Cloud (IAM, network, encryption) → Cluster (API hardening, RBAC, NetworkPolicies) → Container (image integrity, runtime constraints) → Code (app security, secrets handling).
- **Outer-layer dependency**: A secure container is meaningless if the cluster/API is open; secure each ring before assuming inner safety.
- **Control classification**: Each security control belongs to a specific layer; coverage gaps reveal attack paths.

### Critical Patterns
- Map common controls to layers (e.g., VPC/IAM to Cloud; RBAC/NetworkPolicy/API hardening to Cluster; non-root/read-only/scan to Container; input validation/secret use to Code).
- Use layer-specific examples for Task API: restricted RBAC and ingress NetworkPolicy at cluster layer; non-root/read-only, dropped capabilities at container layer; input validation and secret handling at code layer.
- Apply the “leaky bucket” test: list controls per layer, then identify which missing outer-layer control undermines inner protections.

### Common Mistakes
- Securing code or containers while leaving cluster/API open (anonymous auth, broad RBAC).
- Mixing controls without understanding layer placement, leading to false confidence.
- Ignoring cloud-account security (IAM/MFA/network boundaries), leaving the whole stack exposed.

### Connections
- **Builds on**: Skill-first setup from Lesson 0 and Kubernetes fundamentals (Ch. 49–51).
- **Leads to**: Specific controls in RBAC, NetworkPolicies, Pod Security Standards, secrets, and supply chain lessons that implement this layered model.
