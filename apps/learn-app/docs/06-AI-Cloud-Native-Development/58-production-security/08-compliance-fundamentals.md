---
sidebar_position: 8
title: "Compliance Fundamentals: SOC2 and HIPAA Awareness"
description: "Identify Kubernetes controls that support SOC2 and HIPAA compliance requirements, understand audit evidence collection, and map security primitives to regulatory frameworks"
keywords: [compliance, soc2, hipaa, kubernetes security, audit, rbac, network policy, pod security standards, evidence collection, regulatory]
chapter: 58
lesson: 8
duration_minutes: 20

skills:
  - name: "Compliance-to-Control Mapping"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "4. Safety"
    measurable_at_this_level: "Student articulates 3 Kubernetes controls that support SOC2 access control requirements (RBAC, NetworkPolicy, PSS)"
  - name: "Audit Evidence Identification"
    proficiency_level: "A2"
    category: "Technical"
    bloom_level: "Remember"
    digcomp_area: "4. Safety"
    measurable_at_this_level: "Student lists the types of evidence auditors request for Kubernetes deployments"
  - name: "Regulatory Framework Awareness"
    proficiency_level: "A2"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "4. Safety"
    measurable_at_this_level: "Student explains the difference between compliance awareness and compliance certification"
  - name: "Security Control Documentation"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "5. Problem Solving"
    measurable_at_this_level: "Student creates basic control documentation linking Kubernetes resources to compliance requirements"

learning_objectives:
  - objective: "Identify three Kubernetes controls that support SOC2 access control requirements"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student articulates how RBAC, NetworkPolicy, and PSS map to SOC2 CC6.1 access control"
  - objective: "Recognize Kubernetes controls relevant to HIPAA technical safeguards"
    proficiency_level: "A2"
    bloom_level: "Remember"
    assessment_method: "Student matches encryption at rest/transit and access controls to HIPAA requirements"
  - objective: "Describe audit evidence types that auditors request for Kubernetes deployments"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Student explains what YAML exports, audit logs, and RBAC bindings demonstrate to auditors"
  - objective: "Distinguish compliance awareness from compliance certification"
    proficiency_level: "A2"
    bloom_level: "Understand"
    assessment_method: "Student explains why this lesson provides awareness, not certification guidance"

cognitive_load:
  new_concepts: 5
  assessment: "Five concepts (SOC2 control mapping, HIPAA safeguards, audit evidence, compliance vs certification, evidence collection) within B1 limit (7-10 concepts)"

differentiation:
  extension_for_advanced: "Research your organization's specific compliance requirements; create a complete control matrix for one framework"
  remedial_for_struggling: "Focus on the three SOC2 controls first (RBAC, NetworkPolicy, PSS); add HIPAA awareness after mastering SOC2 mapping"
---

# Compliance Fundamentals: SOC2 and HIPAA Awareness

Your Kubernetes cluster runs production workloads. An auditor from your compliance team schedules a meeting: "We need evidence that access controls meet SOC2 requirements." You've configured RBAC, NetworkPolicies, and Pod Security Standards throughout this chapter. But can you explain how those controls satisfy compliance requirements?

This lesson teaches you to connect Kubernetes security primitives to regulatory frameworks. By the end, you'll articulate which Kubernetes controls support which compliance requirements—a critical skill when engineering teams interface with compliance auditors.

:::warning Important Disclaimer
**This is compliance AWARENESS, not compliance CERTIFICATION guidance.** Completing this lesson does not make you a compliance expert. SOC2 and HIPAA certifications require:
- Professional auditors
- Organizational policies beyond technical controls
- Legal review
- Continuous compliance programs

Use this lesson to understand HOW Kubernetes controls support compliance. Work with qualified compliance professionals for actual certification.
:::

---

## Compliance vs Security: Understanding the Difference

Security and compliance are related but distinct:

| Aspect | Security | Compliance |
|--------|----------|------------|
| **Goal** | Protect systems from threats | Demonstrate adherence to standards |
| **Focus** | What controls exist | Can you PROVE controls exist |
| **Audience** | Engineering team | Auditors, regulators, customers |
| **Output** | Working security controls | Documentation and evidence |

A secure system without documentation fails compliance audits. A well-documented system without actual security controls passes audits but gets breached. You need both.

---

## SOC2 Trust Service Criteria and Kubernetes Controls

SOC2 (Service Organization Control 2) audits evaluate controls across five trust service criteria. This lesson focuses on **Security** (Common Criteria), specifically access control.

### SOC2 Controls Relevant to Kubernetes

| SOC2 Criterion | Requirement | Kubernetes Control |
|----------------|-------------|-------------------|
| **CC6.1** | Logical access to systems restricted | RBAC, NetworkPolicy |
| **CC6.2** | Access removed when no longer needed | ServiceAccount lifecycle |
| **CC6.3** | Physical and logical access restricted | PSS (container restrictions) |
| **CC6.6** | System boundaries protected | NetworkPolicy default-deny |
| **CC7.2** | System changes monitored | Audit logging |

### The Three Kubernetes Controls for SOC2 Access Control

When an auditor asks "How do you restrict access?", you point to three controls you've configured throughout this chapter:

**1. RBAC (Role-Based Access Control)**

RBAC answers: "Who can perform what actions on which resources?"

```yaml
# Evidence: Role limiting pod access
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: task-api-reader
  namespace: production
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list"]  # Read-only, no create/delete
```

**SOC2 mapping:** CC6.1 requires that "logical access to information assets is restricted." RBAC implements this by binding specific permissions to specific identities.

**2. NetworkPolicy (Network Segmentation)**

NetworkPolicy answers: "Which pods can communicate with which other pods?"

```yaml
# Evidence: Default-deny with explicit allow
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: task-api-network
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: task-api
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: frontend
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          name: database
```

**SOC2 mapping:** CC6.6 requires "system boundaries are protected." NetworkPolicy creates boundaries between application components, restricting lateral movement.

**3. Pod Security Standards (Container Restrictions)**

PSS answers: "What can containers do on the host system?"

```yaml
# Evidence: Namespace enforcing restricted profile
apiVersion: v1
kind: Namespace
metadata:
  name: production
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: latest
```

**SOC2 mapping:** CC6.3 requires "physical and logical access is restricted." PSS prevents container escape and privilege escalation—logical access restrictions at the container level.

---

## HIPAA Technical Safeguards and Kubernetes Controls

HIPAA (Health Insurance Portability and Accountability Act) applies to Protected Health Information (PHI). If your Task API handles healthcare data, these controls matter.

### HIPAA Technical Safeguards Mapped to Kubernetes

| HIPAA Requirement | Technical Safeguard | Kubernetes Control |
|-------------------|--------------------|--------------------|
| **164.312(a)(1)** | Access control | RBAC, ServiceAccounts |
| **164.312(a)(2)(iv)** | Encryption at rest | etcd encryption, PV encryption |
| **164.312(e)(1)** | Encryption in transit | TLS, service mesh mTLS |
| **164.312(b)** | Audit controls | Kubernetes audit logging |
| **164.312(c)(1)** | Integrity | Image signing, admission control |

### Encryption Requirements

HIPAA requires encryption for PHI both at rest and in transit:

**Encryption at Rest:**

Kubernetes Secrets are base64-encoded by default—NOT encrypted. For HIPAA, enable etcd encryption:

```yaml
# etcd encryption config (managed by cluster admin)
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
    - secrets
    providers:
    - aescbc:
        keys:
        - name: key1
          secret: <base64-encoded-key>
```

**Evidence for auditors:** Encryption configuration file showing secrets are encrypted at rest.

**Encryption in Transit:**

All Kubernetes API traffic uses TLS. For service-to-service traffic, enable mTLS via Dapr (Lesson 7) or a service mesh.

```bash
# Verify mTLS is active (from Lesson 7)
dapr status -k | grep dapr-sentry
```

**Output:**

```
dapr-sentry            dapr-system  True     Running  1         1.12.0
```

**Evidence for auditors:** mTLS status showing Sentry CA is healthy and issuing certificates.

---

## Audit Evidence Collection

When auditors arrive, they request evidence. Preparation means knowing what to export and where to find it.

### Evidence Collection Checklist

| Evidence Type | Kubernetes Command | What It Proves |
|---------------|-------------------|----------------|
| **RBAC bindings** | `kubectl get rolebindings,clusterrolebindings -A -o yaml` | Who has access to what |
| **NetworkPolicies** | `kubectl get networkpolicies -A -o yaml` | Network segmentation exists |
| **PSS labels** | `kubectl get namespaces --show-labels` | Container restrictions enforced |
| **Audit logs** | Export from logging system | Actions were logged |
| **Secret encryption** | etcd encryption config | Data encrypted at rest |

### Generating Evidence Reports

Create a compliance evidence export:

```bash
#!/bin/bash
# compliance-evidence.sh - Generate evidence for auditors

EVIDENCE_DIR="./compliance-evidence-$(date +%Y%m%d)"
mkdir -p "$EVIDENCE_DIR"

# RBAC evidence
echo "Collecting RBAC bindings..."
kubectl get rolebindings -A -o yaml > "$EVIDENCE_DIR/rolebindings.yaml"
kubectl get clusterrolebindings -o yaml > "$EVIDENCE_DIR/clusterrolebindings.yaml"

# NetworkPolicy evidence
echo "Collecting NetworkPolicies..."
kubectl get networkpolicies -A -o yaml > "$EVIDENCE_DIR/networkpolicies.yaml"

# PSS evidence
echo "Collecting namespace labels..."
kubectl get namespaces -o yaml > "$EVIDENCE_DIR/namespaces.yaml"

# ServiceAccount evidence
echo "Collecting ServiceAccounts..."
kubectl get serviceaccounts -A -o yaml > "$EVIDENCE_DIR/serviceaccounts.yaml"

echo "Evidence collected in $EVIDENCE_DIR"
ls -la "$EVIDENCE_DIR"
```

**Output:**

```
Collecting RBAC bindings...
Collecting NetworkPolicies...
Collecting namespace labels...
Collecting ServiceAccounts...
Evidence collected in ./compliance-evidence-20250115
total 48
-rw-r--r--  1 user  staff  12543 Jan 15 10:30 rolebindings.yaml
-rw-r--r--  1 user  staff   8921 Jan 15 10:30 clusterrolebindings.yaml
-rw-r--r--  1 user  staff   4532 Jan 15 10:30 networkpolicies.yaml
-rw-r--r--  1 user  staff   2156 Jan 15 10:30 namespaces.yaml
-rw-r--r--  1 user  staff   6234 Jan 15 10:30 serviceaccounts.yaml
```

### Audit Policy Configuration

Kubernetes audit logging records who did what when. Configure audit policy for compliance. Create `audit-policy.yaml`:

```yaml
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
# Log authentication decisions
- level: Metadata
  resources:
  - group: ""
    resources: ["secrets", "configmaps"]

# Log RBAC changes at RequestResponse level (full details)
- level: RequestResponse
  resources:
  - group: "rbac.authorization.k8s.io"
    resources: ["roles", "rolebindings", "clusterroles", "clusterrolebindings"]

# Log pod creation/deletion
- level: Request
  resources:
  - group: ""
    resources: ["pods"]
  verbs: ["create", "delete"]

# Don't log read-only operations on common resources
- level: None
  resources:
  - group: ""
    resources: ["events", "endpoints"]
  verbs: ["get", "list", "watch"]
```

**What this policy captures:**

- All secret access (who accessed sensitive data)
- All RBAC changes with full request/response (who modified permissions)
- Pod creation/deletion (workload changes)
- Excludes noisy read operations on events/endpoints

---

## Task API Compliance Mapping

Let's apply these frameworks to your Task API. Here's how your security controls map to compliance requirements:

### Task API Control Matrix

| Control | Kubernetes Resource | SOC2 | HIPAA | Evidence Location |
|---------|---------------------|------|-------|-------------------|
| Access control | task-api-sa ServiceAccount | CC6.1 | 164.312(a)(1) | `kubectl get sa task-api-sa -n production -o yaml` |
| Least privilege | task-api-role Role | CC6.1 | 164.312(a)(1) | `kubectl get role task-api-role -n production -o yaml` |
| Network segmentation | task-api-policy NetworkPolicy | CC6.6 | N/A | `kubectl get networkpolicy task-api-policy -n production -o yaml` |
| Container restrictions | production namespace PSS | CC6.3 | 164.312(c)(1) | `kubectl get ns production --show-labels` |
| Encryption in transit | Dapr mTLS | N/A | 164.312(e)(1) | `dapr status -k` |
| Audit logging | Audit policy | CC7.2 | 164.312(b) | API server audit log configuration |

### Example Auditor Conversation

**Auditor:** "How do you ensure only authorized users can access the Task API database?"

**Your response:** "Access is restricted through three layers:

1. **RBAC:** The Task API runs with a dedicated ServiceAccount (`task-api-sa`) that has read-only access to its own namespace resources. I can show you the RoleBinding.

2. **NetworkPolicy:** The Task API pod can only communicate with the database namespace. All other egress is denied by default. Here's the policy YAML.

3. **Pod Security Standards:** The production namespace enforces the `restricted` profile, preventing privilege escalation even if a container is compromised.

Let me export the evidence for your records."

---

## What This Lesson Does NOT Cover

Compliance certification requires more than technical controls:

| Requirement | Covered Here? | Where to Address |
|-------------|---------------|------------------|
| Technical controls | Yes | This lesson |
| Written policies | No | Legal/compliance team |
| Employee training | No | HR/training program |
| Incident response plan | No | Security operations |
| Vendor risk management | No | Procurement/legal |
| Physical security | No | Facilities/cloud provider |
| Business continuity | No | Operations team |

**Your role as an engineer:** Implement and document technical controls. Work with compliance professionals for the complete program.

---

## Reflect on Your Skill

Test your `cloud-security` skill against compliance scenarios:

```
Using my cloud-security skill, prepare for a SOC2 audit of a payment
processing API that:
- Handles credit card data (PCI-DSS adjacent)
- Must demonstrate access control evidence
- Needs to show network segmentation between tiers
- Requires audit logging for all sensitive operations
```

**Evaluation questions:**

1. Does your skill identify the three key Kubernetes controls (RBAC, NetworkPolicy, PSS)?
2. Does your skill include evidence collection commands?
3. Does your skill explain what each control proves to auditors?
4. Does your skill clarify scope (technical controls only, not full compliance)?

If any answers are "no," update your skill with the compliance mapping patterns from this lesson.

---

## Try With AI

Test your understanding of compliance-to-control mapping and evidence collection.

**Prompt 1:**

```
I'm preparing for a SOC2 audit. The auditor asked: "How do you ensure
terminated employees can't access Kubernetes resources?" What Kubernetes
controls and evidence should I show them?
```

**What you're learning:** Access lifecycle management. The answer involves ServiceAccount deletion, RBAC binding removal, and audit logs showing access revocation. Notice if AI explains the connection between identity management and Kubernetes RBAC.

**Prompt 2:**

```
My application handles healthcare data and needs HIPAA compliance. Which
Kubernetes controls address the "encryption at rest" requirement? How do
I prove encryption is enabled?
```

**What you're learning:** HIPAA technical safeguard mapping. The answer involves etcd encryption configuration and evidence collection (encryption config files, API server flags). Notice if AI distinguishes between base64 encoding (not encryption) and actual encryption.

**Prompt 3:**

```
An auditor says: "Show me evidence that network traffic between your
services is encrypted." I'm using Dapr with mTLS. What commands do I run
and what output do I show them?
```

**What you're learning:** Evidence demonstration for encryption in transit. The answer uses `dapr status -k` to show Sentry health and certificate inspection commands from Lesson 7. Notice if AI provides specific commands versus general guidance.

:::tip Compliance Is Ongoing
Compliance is not a one-time achievement. Controls must be continuously monitored, evidence regularly collected, and documentation kept current. The controls you've built throughout this chapter form the technical foundation—but compliance requires organizational commitment beyond engineering.
:::
