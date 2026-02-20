# Chapter 58 Assessment: Production Security & Compliance

**Target Proficiency**: B1 (Intermediate - Independent Application)
**Bloom's Levels**: Apply (40%), Analyze (60%)
**Time Limit**: 45 minutes
**Total Points**: 100
**Passing Score**: 70%

---

## Learning Objectives Assessed

| ID | Objective | Success Criterion |
|----|-----------|-------------------|
| LO-001 | Apply the 4C security model to classify controls | SC-002 |
| LO-002 | Implement ServiceAccount RBAC with least privilege | SC-003 |
| LO-003 | Configure NetworkPolicy default-deny with explicit allows | SC-004 |
| LO-004 | Write PSS Restricted-compliant pod specifications | SC-005 |
| LO-005 | Interpret Trivy vulnerability scan results | SC-006 |
| LO-006 | Execute and interpret 10-point security audit | SC-007 |
| LO-007 | Map Kubernetes controls to compliance frameworks | SC-008 |
| LO-008 | Apply skill-first learning pattern for security | SC-001 |

---

## Cognitive Distribution

| Bloom's Level | Question Count | Percentage |
|---------------|----------------|------------|
| Apply | 4 | 40% |
| Analyze | 6 | 60% |

---

## Section A: Multiple Choice (20 points)

### Question 1 (5 points) [Type: MCQ] [Bloom: Analyze] [SC-002]

Your Task API needs to access ConfigMaps for configuration, communicate with a PostgreSQL database in another namespace, and write logs to a persistent volume. You are classifying security controls by 4C layer. Which classification is CORRECT?

A) ConfigMap access control: Code layer; Database NetworkPolicy: Container layer; Volume encryption: Cluster layer

B) ConfigMap access control: Cluster layer; Database NetworkPolicy: Cluster layer; Volume encryption: Cloud layer

C) ConfigMap access control: Container layer; Database NetworkPolicy: Code layer; Volume encryption: Cluster layer

D) ConfigMap access control: Cloud layer; Database NetworkPolicy: Container layer; Volume encryption: Code layer

---

### Question 2 (5 points) [Type: MCQ] [Bloom: Analyze] [SC-003]

You run `kubectl auth can-i get secrets --as=system:serviceaccount:task-api:task-api-sa -n task-api` and receive "yes". Your Role definition is:

```yaml
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get", "list"]
```

What is the MOST LIKELY cause of this security violation?

A) The ServiceAccount has a ClusterRoleBinding granting additional permissions beyond the Role

B) The Role should use `apiGroups: ["v1"]` instead of `apiGroups: [""]` to properly restrict access

C) The verbs array needs `["get"]` only because "list" implicitly includes secret access

D) The namespace label is missing `pod-security.kubernetes.io/enforce: restricted`

---

### Question 3 (5 points) [Type: MCQ] [Bloom: Apply] [SC-004]

After applying a default-deny NetworkPolicy, your Task API pods cannot resolve service names. The nslookup command times out. Which NetworkPolicy egress rule CORRECTLY fixes DNS resolution?

A)
```yaml
egress:
- to:
  - podSelector:
      matchLabels:
        k8s-app: kube-dns
  ports:
  - protocol: UDP
    port: 53
```

B)
```yaml
egress:
- to:
  - namespaceSelector:
      matchLabels:
        kubernetes.io/metadata.name: kube-system
  ports:
  - protocol: UDP
    port: 53
  - protocol: TCP
    port: 53
```

C)
```yaml
egress:
- to:
  - ipBlock:
      cidr: 10.96.0.0/16
  ports:
  - protocol: UDP
    port: 53
```

D)
```yaml
egress:
- to:
  - namespaceSelector: {}
  ports:
  - protocol: UDP
    port: 53
```

---

### Question 4 (5 points) [Type: MCQ] [Bloom: Analyze] [SC-001]

In the skill-first learning pattern used in this chapter, you created your `cloud-security` skill BEFORE learning the detailed security concepts. What is the PRIMARY pedagogical reason for this approach?

A) Skills created before learning are automatically more accurate because they use official documentation

B) Creating the skill first establishes ownership and provides a concrete artifact to test and improve as concepts are learned

C) AI skills should always be created at the beginning of each chapter to ensure consistent formatting

D) The skill creation process is faster when the student has less domain knowledge to interfere with AI suggestions

---

## Section B: Code Completion (30 points)

### Question 5 (15 points) [Type: Code-Completion] [Bloom: Apply] [SC-005]

Complete the missing `securityContext` fields in this Deployment to make it PSS Restricted-compliant. The Task API writes temporary files to `/tmp` and runs the application as user 1000.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: task-api
  namespace: production
spec:
  template:
    spec:
      # Pod-level security context
      securityContext:
        runAsNonRoot: ___(A)___
        runAsUser: ___(B)___
        runAsGroup: 1000
        fsGroup: 1000
        seccompProfile:
          type: ___(C)___

      containers:
      - name: task-api
        image: task-api:v1.0.0

        # Container-level security context
        securityContext:
          allowPrivilegeEscalation: ___(D)___
          readOnlyRootFilesystem: ___(E)___
          capabilities:
            drop:
              - ___(F)___

        volumeMounts:
        - name: tmp
          mountPath: /tmp

      volumes:
      - name: tmp
        emptyDir: {}
```

**Fill in the blanks:**

| Blank | Your Answer | Explanation (required) |
|-------|-------------|------------------------|
| (A) | | |
| (B) | | |
| (C) | | |
| (D) | | |
| (E) | | |
| (F) | | |

---

### Question 6 (15 points) [Type: Code-Completion] [Bloom: Apply] [SC-003, SC-004]

Complete this RBAC configuration for a monitoring service that needs to read Pod metrics across the `production` and `staging` namespaces, but NOT other namespaces. The service should NOT have cluster-wide access.

```yaml
# ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: metrics-collector-sa
  namespace: monitoring
automountServiceAccountToken: ___(A)___

---
# Reusable permission definition (not namespace-scoped)
apiVersion: rbac.authorization.k8s.io/v1
kind: ___(B)___
metadata:
  name: pod-metrics-reader
rules:
- apiGroups: ["metrics.k8s.io"]
  resources: ["pods"]
  verbs: ["get", "list"]

---
# Binding for production namespace
apiVersion: rbac.authorization.k8s.io/v1
kind: ___(C)___
metadata:
  name: metrics-production
  namespace: production
subjects:
- kind: ServiceAccount
  name: metrics-collector-sa
  namespace: ___(D)___
roleRef:
  kind: ___(E)___
  name: pod-metrics-reader
  apiGroup: rbac.authorization.k8s.io

---
# Binding for staging namespace (same pattern)
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: metrics-staging
  namespace: staging
subjects:
- kind: ServiceAccount
  name: metrics-collector-sa
  namespace: monitoring
roleRef:
  kind: ClusterRole
  name: pod-metrics-reader
  apiGroup: rbac.authorization.k8s.io
```

**Fill in the blanks:**

| Blank | Your Answer | Why this choice? (required) |
|-------|-------------|----------------------------|
| (A) | | |
| (B) | | |
| (C) | | |
| (D) | | |
| (E) | | |

---

## Section C: Scenario Analysis (30 points)

### Question 7 (10 points) [Type: Scenario-Analysis] [Bloom: Analyze] [SC-006]

You run a Trivy scan on your Task API image and receive this output:

```
task-api:v1.2.0 (debian 12.5)
=============================
Total: 47 (UNKNOWN: 0, LOW: 32, MEDIUM: 11, HIGH: 3, CRITICAL: 1)

Library          Vulnerability   Severity   Installed      Fixed Version
libssl3          CVE-2024-0727   CRITICAL   3.0.11-1       3.0.13-1
libcurl4         CVE-2024-2398   HIGH       7.88.1-10      7.88.1-10+deb12u5
python3.11       CVE-2024-0450   HIGH       3.11.2-6       3.11.2-6+deb12u2
zlib1g           CVE-2023-45853  HIGH       1.2.13         (not yet fixed)
```

**Part A (4 points)**: Your CI/CD pipeline uses `trivy image --exit-code 1 --severity CRITICAL`. Will this build PASS or FAIL? Explain why.

**Your answer:**

---

**Part B (3 points)**: For the HIGH vulnerability in `zlib1g` with no fixed version, what is the MOST appropriate immediate action?

A) Wait for upstream fix and do nothing
B) Remove zlib1g from the image since it's optional
C) Document the risk, monitor for exploits, consider alternative base images
D) Downgrade to an older version of zlib1g

**Your answer and justification:**

---

**Part C (3 points)**: After fixing the CRITICAL vulnerability and the two fixable HIGH vulnerabilities, you rebuild. The scan now shows `Total: 44 (LOW: 32, MEDIUM: 11, HIGH: 1)`. Is this image ready for production deployment according to the 10-point audit? Why or why not?

**Your answer:**

---

### Question 8 (10 points) [Type: Scenario-Analysis] [Bloom: Analyze] [SC-007]

You are executing the 10-point security audit on your Task API deployment. Here are the results for three checks:

**Check 2 (Minimal RBAC):**
```bash
$ kubectl auth can-i get secrets --as=system:serviceaccount:task-api:task-api-sa -n task-api
no
$ kubectl auth can-i get configmaps --as=system:serviceaccount:task-api:task-api-sa -n task-api
yes
$ kubectl auth can-i get configmaps --as=system:serviceaccount:task-api:task-api-sa -n kube-system
no
```

**Check 3 (Default-deny NetworkPolicy):**
```bash
$ kubectl get networkpolicy -n task-api default-deny-all -o jsonpath='{.spec.policyTypes}'
["Ingress"]
```

**Check 6 (PSS Restricted):**
```bash
$ kubectl apply -f deployment.yaml --dry-run=server
deployment.apps/task-api created (server dry run)
```

**Part A (4 points)**: Which checks PASS and which FAIL? Complete the table:

| Check | Status (PASS/FAIL) | Evidence |
|-------|-------------------|----------|
| Check 2 | | |
| Check 3 | | |
| Check 6 | | |

---

**Part B (3 points)**: For any FAILED check, what is the specific fix needed?

**Your answer:**

---

**Part C (3 points)**: If Check 3 fails, what security vulnerability does this create for your Task API pods?

**Your answer:**

---

### Question 9 (10 points) [Type: Scenario-Analysis] [Bloom: Analyze] [SC-008]

An auditor asks: "How do you demonstrate SOC2 CC6.1 (logical access restriction) and HIPAA 164.312(e)(1) (transmission security) for your Task API?"

**Part A (5 points)**: Map TWO Kubernetes controls to SOC2 CC6.1. For each, provide the evidence collection command.

| Control | How It Satisfies CC6.1 | Evidence Command |
|---------|----------------------|------------------|
| 1. | | |
| 2. | | |

---

**Part B (5 points)**: Explain how Dapr mTLS satisfies HIPAA 164.312(e)(1) transmission security. Include the verification command that demonstrates mTLS is active.

**Your answer:**

---

## Section D: Practical Exercise (20 points)

### Question 10 (20 points) [Type: Practical-Exercise] [Bloom: Apply/Analyze] [SC-002, SC-003, SC-004, SC-005]

**Scenario**: You are deploying a new `payment-processor` service that:
- Processes credit card transactions (PCI-DSS relevant)
- Needs to read Secrets (not ConfigMaps) in its own namespace
- Must communicate ONLY with a `payment-gateway` service in the same namespace
- Should NOT reach the internet or other namespaces
- Must run with maximum container security restrictions

**Task**: Design the complete security configuration by answering each part.

---

**Part A (5 points)**: Write the RBAC Role that grants ONLY the necessary permissions for reading Secrets.

```yaml
# Your Role YAML here:


```

---

**Part B (5 points)**: Write a default-deny NetworkPolicy AND an ingress allow rule that permits traffic ONLY from pods with label `app: payment-gateway` within the same namespace.

```yaml
# Your NetworkPolicy YAML here (can be multiple policies):


```

---

**Part C (5 points)**: List the 6 `securityContext` fields required for PSS Restricted compliance and their correct values for this payment service running as UID 2000.

| Level | Field | Value |
|-------|-------|-------|
| Pod | 1. | |
| Pod | 2. | |
| Pod | 3. | |
| Container | 4. | |
| Container | 5. | |
| Container | 6. | |

---

**Part D (5 points)**: A penetration tester deploys this pod in the `payment` namespace:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: attacker
  namespace: payment
spec:
  containers:
  - name: attacker
    image: curlimages/curl
    command: ["sleep", "3600"]
```

The tester then runs: `kubectl exec -n payment attacker -- curl -s payment-processor:8080/health`

**Question**: Will this request succeed or be blocked? Explain which control prevents or allows it, and what the attacker would need to change to bypass that control.

**Your answer:**

---

## Answer Key

### Section A: Multiple Choice

**Question 1**: B
- ConfigMap RBAC is Cluster layer (Kubernetes authorization)
- Database NetworkPolicy is Cluster layer (pod-to-pod traffic rules)
- Volume encryption at rest is Cloud layer (cloud provider infrastructure)
- Distractor A confuses Code with Cluster, Container with Cluster
- Distractor C reverses multiple layers
- Distractor D inverts the entire model

**Question 2**: A
- A ClusterRoleBinding can grant additional permissions beyond namespace-scoped Roles
- This is the most common RBAC misconfiguration
- Distractor B: Empty string "" correctly identifies core API group
- Distractor C: "list" does not grant secret access
- Distractor D: PSS labels affect pod creation, not RBAC permissions

**Question 3**: B
- Must use `namespaceSelector` with `kubernetes.io/metadata.name: kube-system` to target CoreDNS
- Must include BOTH UDP and TCP port 53 (large DNS responses use TCP)
- Distractor A: `podSelector` alone cannot cross namespace boundaries
- Distractor C: IP blocks are fragile and may not match CoreDNS IPs
- Distractor D: Empty `namespaceSelector` allows all namespaces (too permissive)

**Question 4**: B
- Skill-first creates ownership and a testable artifact that improves with each lesson
- The skill becomes an asset, not just knowledge
- Distractor A: Skills are grounded in docs, but that's not the pedagogical reason
- Distractor C: Not all chapters use skill-first pattern
- Distractor D: Less knowledge doesn't improve skill quality

### Section B: Code Completion

**Question 5**:
| Blank | Answer | Explanation |
|-------|--------|-------------|
| (A) | `true` | PSS Restricted requires containers run as non-root |
| (B) | `1000` | Explicit non-root UID matching the application user |
| (C) | `RuntimeDefault` | PSS Restricted requires a seccomp profile |
| (D) | `false` | Prevents privilege escalation via setuid/setgid |
| (E) | `true` | Prevents filesystem modification (security + immutability) |
| (F) | `ALL` | Drop all Linux capabilities for minimal attack surface |

**Question 6**:
| Blank | Answer | Explanation |
|-------|--------|-------------|
| (A) | `false` | API access not needed, reduces attack surface |
| (B) | `ClusterRole` | Reusable across namespaces without granting cluster-wide access |
| (C) | `RoleBinding` | Limits scope to production namespace only |
| (D) | `monitoring` | SA exists in monitoring namespace, must specify |
| (E) | `ClusterRole` | References the ClusterRole defined above |

### Section C: Scenario Analysis

**Question 7**:
- **Part A**: FAIL. The scan found 1 CRITICAL vulnerability (CVE-2024-0727 in libssl3). The `--exit-code 1` flag causes Trivy to return exit code 1 when vulnerabilities matching the severity filter are found.
- **Part B**: C. Document the risk, monitor for exploits, consider alternative base images. The vulnerability has no fix yet, so waiting is required, but active risk management (monitoring, documentation, considering Alpine/Distroless) is the responsible approach.
- **Part C**: YES, ready for production. The 10-point audit check 7 requires "No CRITICAL vulnerabilities." With 0 CRITICAL remaining, this check passes. HIGH vulnerabilities should be tracked but don't block deployment under the audit criteria.

**Question 8**:
- **Part A**:

| Check | Status | Evidence |
|-------|--------|----------|
| Check 2 | PASS | Secrets denied, ConfigMaps allowed in own namespace, denied in other namespaces |
| Check 3 | FAIL | Only "Ingress" in policyTypes, missing "Egress" |
| Check 6 | PASS | Dry-run accepted without PSS violations |

- **Part B**: Check 3 fix: Add `"Egress"` to the policyTypes array in the default-deny NetworkPolicy. The spec should read `policyTypes: ["Ingress", "Egress"]`.
- **Part C**: Without egress default-deny, compromised pods can make outbound connections to any destination (data exfiltration, command & control, lateral movement to other namespaces, cryptocurrency mining).

**Question 9**:
- **Part A**:

| Control | How It Satisfies CC6.1 | Evidence Command |
|---------|----------------------|------------------|
| RBAC (Roles/RoleBindings) | Restricts API access to specific resources and verbs per identity | `kubectl get rolebindings -n task-api -o yaml` |
| NetworkPolicy | Restricts network access to explicitly allowed services only | `kubectl get networkpolicies -n task-api -o yaml` |

- **Part B**: Dapr mTLS encrypts all service-to-service communication between Dapr sidecars using mutual TLS certificates issued by the Dapr Sentry CA. This ensures data in transit is encrypted, satisfying HIPAA transmission security. Verification: `dapr status -k | grep dapr-sentry` should show Sentry "Running" with healthy status.

### Section D: Practical Exercise

**Question 10**:

**Part A**:
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: payment-processor-role
  namespace: payment
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "list"]
```

**Part B**:
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: payment
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
---
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-payment-gateway
  namespace: payment
spec:
  podSelector:
    matchLabels:
      app: payment-processor
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: payment-gateway
    ports:
    - protocol: TCP
      port: 8080
```

**Part C**:
| Level | Field | Value |
|-------|-------|-------|
| Pod | runAsNonRoot | true |
| Pod | runAsUser | 2000 |
| Pod | seccompProfile.type | RuntimeDefault |
| Container | allowPrivilegeEscalation | false |
| Container | readOnlyRootFilesystem | true |
| Container | capabilities.drop | ["ALL"] |

**Part D**:
The request will be **BLOCKED** by the NetworkPolicy. The `allow-payment-gateway` ingress rule only permits traffic from pods with label `app: payment-gateway`. The attacker pod has no labels, so it doesn't match the selector.

To bypass this control, the attacker would need to:
1. Add the label `app: payment-gateway` to their pod (requires RBAC permissions to patch pods)
2. Or compromise an existing pod that already has the gateway label
3. Or delete the NetworkPolicy (requires RBAC permissions)

---

## Rubric for Open-Ended Questions

### Code Completion (Q5, Q6)

**Excellent (15 points each)**: All blanks correct with accurate explanations showing understanding of why each value is required for security.

**Good (12 points each)**: 4-5 blanks correct, minor explanation gaps.

**Adequate (9 points each)**: 3-4 blanks correct, explanations show partial understanding.

**Needs Improvement (6 points each)**: 2 or fewer blanks correct, explanations missing or incorrect.

### Scenario Analysis (Q7, Q8, Q9)

**Excellent (10 points each)**: All parts answered correctly with specific technical details and security reasoning.

**Good (8 points each)**: Most parts correct, minor technical inaccuracies.

**Adequate (6 points each)**: Partial understanding demonstrated, some parts missing or incorrect.

**Needs Improvement (3 points each)**: Significant gaps in understanding, multiple incorrect answers.

### Practical Exercise (Q10)

**Excellent (20 points)**: All four parts complete and correct. YAML is syntactically valid and follows security best practices.

**Good (16 points)**: 3-4 parts correct, minor YAML errors or missing fields.

**Adequate (12 points)**: 2-3 parts correct, demonstrates understanding of core concepts.

**Needs Improvement (6 points)**: 1 or fewer parts correct, fundamental misunderstanding of security concepts.

---

## Diagnostic Indicators

| If student fails... | Gap type | Remediation |
|--------------------|----------|-------------|
| Q1 (4C classification) | Conceptual | Review L01 4C model, practice classification exercise |
| Q2, Q5, Q6 (RBAC) | Procedural | Review L02 RBAC patterns, practice `kubectl auth can-i` |
| Q3, Q8 Part C, Q10 Part B (NetworkPolicy) | Procedural | Review L03 default-deny + DNS, trace traffic flow |
| Q5, Q10 Part C (PSS) | Procedural | Review L05 securityContext fields checklist |
| Q7 (Trivy interpretation) | Analytical | Review L06 severity levels and remediation framework |
| Q8 (Audit execution) | Evaluative | Practice running audit script, interpret each check |
| Q9 (Compliance mapping) | Conceptual | Review L08 SOC2/HIPAA control matrix |
| Q4, Q10 Part D (Security reasoning) | Integrative | Capstone review, connect controls to attack prevention |

---

## Success Criteria Mapping

| Success Criterion | Questions Testing It |
|-------------------|---------------------|
| SC-001: Skill creation timing | Q4 |
| SC-002: 4C layer classification | Q1 |
| SC-003: ServiceAccount RBAC | Q2, Q6, Q10A |
| SC-004: NetworkPolicy blocking | Q3, Q8, Q10B |
| SC-005: PSS restricted compliance | Q5, Q10C |
| SC-006: Trivy vulnerability scanning | Q7 |
| SC-007: 10-point audit checklist | Q8 |
| SC-008: Compliance control mapping | Q9 |

---

**Assessment Version**: 1.0.0
**Aligned with**: Chapter 58 spec v1.0.0
**Reviewed by**: assessment-architect agent
**Date**: 2025-12-30
