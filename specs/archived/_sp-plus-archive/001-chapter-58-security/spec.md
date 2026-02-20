# Feature Specification: Chapter 58 - Production Security & Compliance

**Feature Branch**: `001-chapter-58-security`
**Created**: 2025-12-30
**Status**: Complete (PR #596)
**Proficiency Level**: B1 (Intermediate)
**Part**: 7 - AI Cloud Native Development (Enterprise Tier)

## Clarifications

### Session 2025-12-30

- Q: Technology version specifications? → A: Added Technology Versions section with Kubernetes 1.28+, Calico 3.26+, Trivy latest, Dapr 1.12+, ESO 0.9+, Cosign latest

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Kubernetes fundamentals: Pods, Deployments, Services, Namespaces (Ch50)
- Helm charts for packaging deployments (Ch51)
- Dapr building blocks: state, pub/sub, service invocation (Ch53)
- CI/CD and GitOps patterns (Ch54)
- Observability basics: metrics, logging, tracing (Ch55)
- Traffic engineering: Gateway API, rate limiting (Ch56)
- Basic RBAC awareness from Ch50 L10 (high-level only)
- The Task API running example from Ch40 through containerization and deployment

**What this chapter must explain from scratch**:
- 4C security model (Cloud, Cluster, Container, Code) - defense in depth philosophy
- Deep RBAC: Roles vs ClusterRoles, RoleBindings, ServiceAccounts, least privilege
- NetworkPolicy: default deny, allow rules, CNI requirements (Calico)
- Pod Security Standards (PSS/PSA): Privileged, Baseline, Restricted levels
- Secrets management hierarchy: K8s Secrets → Sealed Secrets → External Secrets Operator
- Image supply chain security: Trivy scanning, Cosign signing, SBOM generation
- Dapr-specific security: mTLS, API tokens, component scopes
- Compliance fundamentals: SOC2, HIPAA awareness (what technical controls support)

## User Scenarios & Testing

### User Story 1 - Student Builds Security Skill (Priority: P1)

Students create their own `cloud-security` skill in Lesson 0 before learning security concepts. This skill becomes the foundation that they test and improve throughout the chapter.

**Why this priority**: Skill-First pattern - students own reusable intelligence, not just knowledge.

**Independent Test**: Student has a working `cloud-security` skill in `.claude/skills/` that can generate security configurations.

**Acceptance Scenarios**:

1. **Given** a student opens the skills-lab, **When** they run the skill creation prompt, **Then** a `cloud-security` skill is created with references to official Kubernetes security docs
2. **Given** a student has created their skill, **When** they ask "secure my Task API deployment", **Then** the skill provides RBAC, NetworkPolicy, and PSS configuration

---

### User Story 2 - Student Understands Defense in Depth (Priority: P1)

Students learn the 4C security model and understand why each layer matters. They can identify which layer a security control belongs to and why layered security prevents single points of failure.

**Why this priority**: Mental model required before implementing any specific control.

**Independent Test**: Student can explain why Code-level security alone cannot compensate for Cluster-level vulnerabilities.

**Acceptance Scenarios**:

1. **Given** a student reads L01, **When** asked to classify RBAC, **Then** they correctly identify it as Cluster layer
2. **Given** a student understands 4C, **When** presented with a security breach scenario, **Then** they can identify which layer(s) failed

---

### User Story 3 - Student Implements RBAC for Task API (Priority: P1)

Students create ServiceAccounts, Roles, and RoleBindings that follow least privilege. They can test what permissions an account has using `kubectl auth can-i`.

**Why this priority**: RBAC is the foundation of Kubernetes access control.

**Independent Test**: Task API runs with a dedicated ServiceAccount that has only the permissions it needs.

**Acceptance Scenarios**:

1. **Given** a Task API deployment, **When** RBAC is applied, **Then** the pod runs with a dedicated ServiceAccount (not default)
2. **Given** RBAC configuration, **When** tested with `kubectl auth can-i`, **Then** only explicitly granted permissions are available
3. **Given** an attacker gains access to the pod, **When** they try to access secrets in other namespaces, **Then** access is denied

---

### User Story 4 - Student Implements Network Isolation (Priority: P1)

Students implement default-deny NetworkPolicies and add explicit allow rules. They understand CNI requirements and can debug connectivity issues.

**Why this priority**: Network isolation is critical for blast radius reduction.

**Independent Test**: Only explicitly allowed traffic reaches the Task API; all other traffic is blocked.

**Acceptance Scenarios**:

1. **Given** default-deny NetworkPolicy, **When** a pod tries to reach Task API without an allow rule, **Then** connection times out
2. **Given** default-deny is applied, **When** DNS egress is not allowed, **Then** pods cannot resolve service names (highlighting need for DNS allow rule)
3. **Given** proper allow rules, **When** Envoy Gateway sends traffic to Task API, **Then** traffic is allowed

---

### User Story 5 - Student Enforces Pod Security Standards (Priority: P2)

Students apply PSS labels to namespaces and understand the three security levels. They can write pod specs that comply with the Restricted profile.

**Why this priority**: PSS prevents privilege escalation and enforces container hardening.

**Independent Test**: Task API runs in a namespace with `enforce=restricted` label and pod is admitted.

**Acceptance Scenarios**:

1. **Given** a namespace with `pod-security.kubernetes.io/enforce=restricted`, **When** a privileged pod is submitted, **Then** the pod is rejected
2. **Given** the Task API pod spec, **When** PSS-compliant securityContext is added, **Then** pod runs successfully under restricted profile
3. **Given** a violation, **When** the warning is shown, **Then** student can identify which field violates PSS

---

### User Story 6 - Student Manages Secrets Securely (Priority: P2)

Students understand the secrets hierarchy and implement at least K8s Secrets with proper RBAC. Advanced students implement External Secrets Operator.

**Why this priority**: Credentials are high-value targets; proper secrets management is essential.

**Independent Test**: Task API database credentials are stored as K8s Secrets and consumed via volume mount, not environment variable in plain manifest.

**Acceptance Scenarios**:

1. **Given** database credentials, **When** stored as K8s Secret, **Then** they are base64 encoded and access-controlled by RBAC
2. **Given** a Secret, **When** consumed by pod via volume mount, **Then** credentials are available at specified path
3. **Given** ESO is configured, **When** external secret changes, **Then** K8s Secret is updated within refresh interval

---

### User Story 7 - Student Scans Images for Vulnerabilities (Priority: P2)

Students use Trivy to scan container images and understand severity levels. They can fail CI/CD on HIGH+ vulnerabilities.

**Why this priority**: Vulnerable images are a common attack vector.

**Independent Test**: Task API image is scanned before deployment; no CRITICAL vulnerabilities exist.

**Acceptance Scenarios**:

1. **Given** a container image, **When** `trivy image` is run, **Then** vulnerabilities are listed with severity levels
2. **Given** CI/CD pipeline, **When** `--exit-code 1 --severity HIGH,CRITICAL` is used, **Then** pipeline fails on HIGH+ vulnerabilities
3. **Given** a clean image, **When** SBOM is generated, **Then** dependencies are documented for supply chain transparency

---

### User Story 8 - Student Configures Dapr Security (Priority: P2)

Students verify mTLS is enabled between Dapr sidecars and understand component scopes. They can restrict which apps access which components.

**Why this priority**: Dapr is used throughout Part 7; its security must be explicit.

**Independent Test**: Only Task API can access its designated state store; other apps are denied.

**Acceptance Scenarios**:

1. **Given** Dapr in Kubernetes, **When** mTLS is checked, **Then** Sentry CA is healthy and certificates are valid
2. **Given** a state store component, **When** `scopes` is set to `task-api`, **Then** other apps cannot use that component
3. **Given** API token auth enabled, **When** request lacks token, **Then** request is rejected

---

### User Story 9 - Student Understands Compliance Basics (Priority: P3)

Students understand what SOC2 and HIPAA require technically and how Kubernetes controls support compliance. They know this is awareness, not certification.

**Why this priority**: Domain experts building agents for regulated industries need compliance awareness.

**Independent Test**: Student can list 3 Kubernetes controls that support audit logging for SOC2.

**Acceptance Scenarios**:

1. **Given** SOC2 access control requirements, **When** asked how to address them, **Then** student references RBAC and audit logging
2. **Given** HIPAA encryption requirements, **When** asked how to address them, **Then** student references TLS and encryption at rest
3. **Given** a compliance audit, **When** asked for evidence, **Then** student knows where to find audit logs

---

### User Story 10 - Student Completes Capstone Security Audit (Priority: P1)

Students apply all security patterns to the Task API in a capstone project. They perform a security checklist audit and document their security posture.

**Why this priority**: Integration of all concepts; proof of learning.

**Independent Test**: Task API passes a 10-point security checklist covering RBAC, NetworkPolicy, PSS, Secrets, and image scanning.

**Acceptance Scenarios**:

1. **Given** all lessons completed, **When** capstone is implemented, **Then** Task API has RBAC, NetworkPolicy, PSS, and scanned image
2. **Given** security checklist, **When** student audits their deployment, **Then** all items pass or have documented exceptions
3. **Given** completed capstone, **When** student runs penetration test scenarios, **Then** security controls block unauthorized access

---

### Edge Cases

- What happens when NetworkPolicy blocks DNS (pod can't resolve services)?
- How does Calico installation affect existing workloads on Docker Desktop?
- What if External Secrets Operator can't reach the external secret store?
- How do Dapr component scopes interact with RBAC?
- What if a pod legitimately needs privileged access (e.g., CNI plugin)?

## Requirements

### Functional Requirements

- **FR-001**: Chapter MUST start with L00 "Build Your Cloud Security Skill" following Skill-First pattern
- **FR-002**: Each lesson (L01-L08) MUST end with "Reflect on Your Skill" section testing and improving the student's skill
- **FR-003**: L01 MUST explain the 4C security model with Task API examples at each layer
- **FR-004**: L02 MUST teach RBAC with working examples: ServiceAccount, Role, RoleBinding for Task API
- **FR-005**: L03 MUST teach NetworkPolicy with default-deny pattern and explicit allows for DNS, ingress, and database
- **FR-006**: L04 MUST teach secrets hierarchy (K8s Secrets, mention sealed-secrets and ESO for production)
- **FR-007**: L05 MUST teach Pod Security Standards with namespace labels and compliant pod specs
- **FR-008**: L06 MUST teach Trivy image scanning with CI/CD integration patterns
- **FR-009**: L07 MUST teach Dapr-specific security: mTLS verification, component scopes, API tokens
- **FR-010**: L08 MUST provide compliance awareness (SOC2, HIPAA) without claiming to be a certification guide
- **FR-011**: L09 (Capstone) MUST integrate all patterns into a secure Task API deployment with audit checklist
- **FR-012**: All lessons MUST use Docker Desktop Kubernetes as the platform
- **FR-013**: Expertise skill (`.claude/skills/building-with-cloud-security/`) MUST be referenced for accurate patterns
- **FR-014**: Chapter MUST NOT cover TLS termination, JWT/OIDC, or rate limiting (covered in Ch56)

### Key Entities

- **ServiceAccount**: Identity for pods to authenticate to the Kubernetes API
- **Role/ClusterRole**: Set of permissions (verbs on resources)
- **RoleBinding/ClusterRoleBinding**: Associates Role with subjects (ServiceAccounts, users)
- **NetworkPolicy**: Firewall rules for pod network traffic
- **Pod Security Standard (PSS)**: Security profile (Privileged/Baseline/Restricted)
- **Secret**: Kubernetes object for storing sensitive data
- **Trivy Report**: Vulnerability scan output with severity levels
- **Dapr Component Scope**: Restriction on which apps can use a component

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students can create a working `cloud-security` skill in under 15 minutes (L00)
- **SC-002**: Students correctly classify 5+ security controls by 4C layer with 90% accuracy
- **SC-003**: Task API runs with dedicated ServiceAccount that has only ConfigMap read access (not wildcard)
- **SC-004**: Unauthorized traffic to Task API is blocked by NetworkPolicy (verifiable with test pod)
- **SC-005**: Task API pod passes PSS `restricted` profile validation
- **SC-006**: Task API image has no CRITICAL vulnerabilities as reported by Trivy
- **SC-007**: Students complete the 10-point security audit checklist in capstone with all items passing
- **SC-008**: Students can articulate 3 Kubernetes controls supporting SOC2 access control requirements

## Lesson Structure

### L00: Build Your Cloud Security Skill (15 min) - Layer 3

Students create their `cloud-security` skill using the skills-lab and `/skill-creator`. The skill fetches official Kubernetes security documentation and becomes the foundation for the chapter.

### L01: Cloud Native Security Model (25 min) - Layer 1

The 4C's: Cloud, Cluster, Container, Code. Defense in depth philosophy. Task API examples at each layer. Why outer layers must be secure for inner layers to matter.

### L02: RBAC Deep Dive (30 min) - Layer 1

ServiceAccounts, Roles, ClusterRoles, RoleBindings, ClusterRoleBindings. Principle of least privilege. Task API RBAC implementation. Testing with `kubectl auth can-i`.

### L03: NetworkPolicies (30 min) - Layer 1

Default deny pattern. Ingress and egress rules. Namespace isolation. Calico installation on Docker Desktop. Task API NetworkPolicy implementation. Debugging blocked traffic.

### L04: Secrets Management (25 min) - Layer 1

K8s Secrets creation and consumption. Volume mounts vs environment variables. Sealed Secrets overview. External Secrets Operator overview. Task API secrets for database credentials.

### L05: Pod Security Standards (25 min) - Layer 1

PSS levels: Privileged, Baseline, Restricted. Pod Security Admission. Namespace labels. Compliant pod securityContext. Task API PSS compliance.

### L06: Image Scanning & Supply Chain (25 min) - Layer 1

Trivy scanning. Severity levels. CI/CD integration. SBOM generation. Cosign signing overview. Task API image scanning workflow.

### L07: Dapr Security (25 min) - Layer 2

mTLS between sidecars. Sentry CA. API token authentication. Component scopes. Secret scopes. Task API Dapr security configuration.

### L08: Compliance Fundamentals (20 min) - Layer 1

SOC2 awareness (access control, audit logging). HIPAA awareness (encryption, access). How Kubernetes controls support compliance. Not a certification guide.

### L09: Capstone - Secure Task API (40 min) - Layer 4

Apply all patterns to Task API. 10-point security checklist audit. Documentation of security posture. Penetration test scenarios.

## Layer Progression

| Lesson | Layer | Description |
|--------|-------|-------------|
| L00 | L3 (Skill) | Create reusable security skill |
| L01 | L1 (Manual) | Mental model: 4C security |
| L02 | L1 (Manual) | Implement RBAC manually |
| L03 | L1 (Manual) | Implement NetworkPolicy manually |
| L04 | L1 (Manual) | Implement secrets manually |
| L05 | L1 (Manual) | Implement PSS manually |
| L06 | L1 (Manual) | Run Trivy scanning manually |
| L07 | L2 (Collaboration) | Collaborate with skill on Dapr security |
| L08 | L1 (Manual) | Understand compliance requirements |
| L09 | L4 (Orchestration) | Spec-driven capstone integrating all patterns |

## Prerequisites

- **Chapter 50**: Kubernetes fundamentals (Pods, Deployments, Services, Namespaces)
- **Chapter 53**: Dapr basics (for L07 Dapr security)
- **Chapter 49**: Docker (container image concepts for L06)
- **Running example**: Task API from Ch40 containerized and deployed

## References

- **Expertise Skill**: `.claude/skills/building-with-cloud-security/SKILL.md`
- **DACA Reference**: `08_daca_deployment_guide/02_Enterprise-Deployment-Kubernetes/03_Security_and_Compliance/`
- **Quality Standard**: Match structure of Ch49/Ch50 README and L00 lessons

## Technology Versions

- **Kubernetes**: 1.28+ (Docker Desktop ships with recent versions; PSS is stable)
- **Calico CNI**: 3.26+ (for NetworkPolicy support on Docker Desktop)
- **Trivy**: Latest (installed via brew/curl; version not pinned)
- **Dapr**: 1.12+ (mTLS enabled by default in production mode)
- **External Secrets Operator**: 0.9+ (if students choose to install)
- **Cosign**: Latest (for image signing demonstration)

## Assumptions

1. Docker Desktop Kubernetes is the target platform (no cloud IAM integration)
2. Calico CNI will be installed for NetworkPolicy support
3. Students have completed Ch50 and understand basic Kubernetes concepts
4. External Secrets Operator is shown but not required (K8s Secrets is the baseline)
5. Compliance section is awareness only - not a certification preparation guide
6. Image signing with Cosign is shown but not enforced (Docker Desktop limitation)

## Implementation Reflection (2025-12-30)

### What Worked Well

| Aspect | Outcome |
|--------|---------|
| **Skill-First Pattern** | Expertise skill built before content ensured accurate API patterns |
| **Parallel Subagent Execution** | Lessons L01-L03 and L04-L07 ran concurrently, improving throughput |
| **Layer Progression** | L3 → L1 → L2 → L4 validated by educational-validator |
| **Three Roles (L07)** | Framework invisible - no meta-commentary, natural narrative flow |
| **Security Checklist Asset** | Standalone 10-point audit tool students can reuse |
| **PHR Documentation** | 7 PHRs captured full workflow for reproducibility |

### Quality Metrics

| Metric | Value |
|--------|-------|
| Total Lines | 5,799 (content only) |
| Lesson Quality Range | 86-88/100 |
| Overall Quality Score | 92% |
| Constitution Compliance | PASS |
| Framework Invisibility | PASS |
| Files Changed | 33 |
| Total Insertions | 11,005 |

### Lessons Learned

1. **Label creation**: GitHub labels should be pre-created or omitted from issue creation
2. **Subagent verification**: Always verify file exists after subagent returns
3. **Skill grounding**: Building expertise skill from official docs prevents hallucination

### Artifacts Produced

- **Content**: 10 lessons + README + 2 assets
- **Skill**: `.claude/skills/building-with-cloud-security/` (4 files)
- **Specs**: spec.md, plan.md, tasks.md, checklists/requirements.md
- **PHRs**: 7 prompt history records
- **PR**: #596 (https://github.com/panaversity/agentfactory/pull/596)
