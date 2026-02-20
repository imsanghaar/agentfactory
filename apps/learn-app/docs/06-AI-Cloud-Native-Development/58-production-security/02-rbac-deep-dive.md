---
sidebar_position: 2
title: "RBAC Deep Dive"
description: "Implement Kubernetes RBAC for Task API with ServiceAccounts, Roles, and RoleBindings following the principle of least privilege"
keywords: [kubernetes rbac, serviceaccount, role, rolebinding, clusterrole, least privilege, kubectl auth, security]
chapter: 58
lesson: 2
duration_minutes: 30

skills:
  - name: "RBAC Implementation"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "4. Safety"
    measurable_at_this_level: "Student creates ServiceAccount, Role, and RoleBinding following least privilege principles"
  - name: "Least Privilege Design"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "4. Safety"
    measurable_at_this_level: "Student analyzes permission requirements and selects minimal necessary access"
  - name: "RBAC Troubleshooting"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "5. Problem Solving"
    measurable_at_this_level: "Student uses kubectl auth can-i to verify and debug permissions"

learning_objectives:
  - objective: "Create a dedicated ServiceAccount with automountServiceAccountToken disabled"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "kubectl get serviceaccount shows SA with automount disabled"
  - objective: "Implement Role with minimal verbs and resources using the least privilege principle"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Role YAML contains no wildcards and only necessary permissions"
  - objective: "Connect ServiceAccount to Role using RoleBinding"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "RoleBinding correctly references both ServiceAccount and Role"
  - objective: "Test RBAC permissions using kubectl auth can-i --as=system:serviceaccount:..."
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "Student verifies allowed and denied operations correctly"
  - objective: "Apply the Role vs ClusterRole decision matrix to select appropriate scope"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student correctly justifies namespace-scoped Role for Task API"

cognitive_load:
  new_concepts: 7
  assessment: "Seven concepts: ServiceAccount, Role, ClusterRole, RoleBinding, ClusterRoleBinding, automountServiceAccountToken, least privilege. Within B1 limits with progressive introduction."

differentiation:
  extension_for_advanced: "Create ClusterRole for cross-namespace monitoring scenarios"
  remedial_for_struggling: "Focus on the three-resource pattern (SA + Role + RoleBinding) before decision matrix"
---

# RBAC Deep Dive

In December 2023, a security researcher discovered that thousands of Kubernetes clusters on the public internet had exposed dashboards running with cluster-admin privileges. Attackers weren't exploiting vulnerabilities—they were using the default service account that Kubernetes automatically mounts into every pod, which often had more permissions than the application ever needed.

Your Task API doesn't need cluster-admin access. It doesn't need access to secrets across all namespaces. It needs exactly one thing: the ability to read its own ConfigMap. RBAC (Role-Based Access Control) lets you specify precisely that—and nothing more.

This lesson builds the RBAC foundation that protects your Task API from privilege escalation attacks. By the end, you'll understand why every production workload needs its own ServiceAccount, and you'll have the pattern to implement least privilege for any Kubernetes application.

---

## What RBAC Actually Controls

Before creating RBAC resources, understand what you're protecting. Every Kubernetes API request goes through three checkpoints:

| Checkpoint | Question | Denial Result |
|------------|----------|---------------|
| **Authentication** | "Who are you?" | 401 Unauthorized |
| **Authorization (RBAC)** | "Are you allowed to do this?" | 403 Forbidden |
| **Admission Control** | "Is this request valid?" | Request rejected |

RBAC handles the second checkpoint. When your Task API pod tries to read a ConfigMap, RBAC answers: "Is this ServiceAccount allowed to get ConfigMaps in this namespace?"

---

## The Four RBAC Building Blocks

RBAC uses four types of resources that work together:

```
┌─────────────────────────────────────────────────────────────┐
│                    RBAC Architecture                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  SUBJECT                    BINDING                 ROLE     │
│  (who)                      (connects)              (what)   │
│                                                              │
│  ┌───────────────┐     ┌──────────────┐     ┌─────────────┐ │
│  │ ServiceAccount├────►│ RoleBinding  ├────►│    Role     │ │
│  │ (task-api-sa) │     │              │     │ (configmap  │ │
│  └───────────────┘     └──────────────┘     │  read only) │ │
│                                             └─────────────┘ │
│                                                              │
│  Namespace-scoped: Role + RoleBinding                        │
│  Cluster-scoped: ClusterRole + ClusterRoleBinding            │
└─────────────────────────────────────────────────────────────┘
```

| Resource | Scope | Purpose |
|----------|-------|---------|
| **ServiceAccount** | Namespace | Identity for pods (like a user account for applications) |
| **Role** | Namespace | Defines what actions are allowed on which resources |
| **RoleBinding** | Namespace | Connects a ServiceAccount to a Role |
| **ClusterRole** | Cluster | Like Role, but applies across all namespaces |
| **ClusterRoleBinding** | Cluster | Connects a ServiceAccount to a ClusterRole |

---

## Step 1: Create a Dedicated ServiceAccount

First, create a namespace for your Task API if it doesn't exist:

```bash
kubectl create namespace task-api
```

**Output:**

```
namespace/task-api created
```

Now create a dedicated ServiceAccount. The critical setting is `automountServiceAccountToken: false`, which prevents Kubernetes from automatically mounting the token into your pods. Create `task-api-sa.yaml`:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: task-api-sa
  namespace: task-api
automountServiceAccountToken: false
```

Apply the ServiceAccount:

```bash
kubectl apply -f task-api-sa.yaml
```

**Output:**

```
serviceaccount/task-api-sa created
```

### Why Disable Auto-Mounting?

By default, Kubernetes mounts a token into every pod at `/var/run/secrets/kubernetes.io/serviceaccount/`. This token grants API access. If your application doesn't need to call the Kubernetes API, mounting this token only creates attack surface.

Verify the setting:

```bash
kubectl get serviceaccount task-api-sa -n task-api -o yaml | grep automount
```

**Output:**

```
automountServiceAccountToken: false
```

---

## Step 2: Define the Role (Minimum Required Permissions)

Your Task API needs to read its ConfigMap for configuration. It doesn't need to create, update, or delete ConfigMaps. It doesn't need access to Secrets. Define exactly that. Create `task-api-role.yaml`:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: task-api-role
  namespace: task-api
rules:
- apiGroups: [""]           # Core API group (ConfigMaps, Secrets, Pods, etc.)
  resources: ["configmaps"]  # Only ConfigMaps
  verbs: ["get", "list"]     # Read-only operations
```

Apply the Role:

```bash
kubectl apply -f task-api-role.yaml
```

**Output:**

```
role.rbac.authorization.k8s.io/task-api-role created
```

### Understanding the Rules

Each rule has three components:

| Field | Example | Meaning |
|-------|---------|---------|
| `apiGroups` | `[""]` | Core API group (empty string means v1 resources like ConfigMaps, Pods) |
| `resources` | `["configmaps"]` | Which resource types this rule applies to |
| `verbs` | `["get", "list"]` | Allowed operations |

Available verbs:

| Verb | kubectl equivalent | Description |
|------|-------------------|-------------|
| `get` | `kubectl get [resource] [name]` | Read a single resource |
| `list` | `kubectl get [resources]` | List all resources of this type |
| `watch` | `kubectl get [resources] --watch` | Stream updates |
| `create` | `kubectl create` | Create new resources |
| `update` | `kubectl apply` (existing) | Modify existing resources |
| `patch` | `kubectl patch` | Partial modification |
| `delete` | `kubectl delete` | Remove resources |

:::warning Never Use Wildcards
Using `"*"` for apiGroups, resources, or verbs grants far more access than needed. Explicit lists are always safer:

```yaml
# DANGEROUS - avoid this
rules:
- apiGroups: ["*"]
  resources: ["*"]
  verbs: ["*"]

# SAFE - explicit and minimal
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get", "list"]
```
:::

---

## Step 3: Create the RoleBinding

The RoleBinding connects your ServiceAccount to the Role. Create `task-api-binding.yaml`:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: task-api-binding
  namespace: task-api
subjects:
- kind: ServiceAccount
  name: task-api-sa
  namespace: task-api
roleRef:
  kind: Role
  name: task-api-role
  apiGroup: rbac.authorization.k8s.io
```

Apply the RoleBinding:

```bash
kubectl apply -f task-api-binding.yaml
```

**Output:**

```
rolebinding.rbac.authorization.k8s.io/task-api-binding created
```

---

## Step 4: Test RBAC with kubectl auth can-i

Before deploying your application, verify that permissions work as expected. The `kubectl auth can-i` command tests whether an action is allowed:

### Test Allowed Operations

```bash
kubectl auth can-i get configmaps \
  --as=system:serviceaccount:task-api:task-api-sa \
  -n task-api
```

**Output:**

```
yes
```

```bash
kubectl auth can-i list configmaps \
  --as=system:serviceaccount:task-api:task-api-sa \
  -n task-api
```

**Output:**

```
yes
```

### Test Denied Operations

```bash
kubectl auth can-i create configmaps \
  --as=system:serviceaccount:task-api:task-api-sa \
  -n task-api
```

**Output:**

```
no
```

```bash
kubectl auth can-i get secrets \
  --as=system:serviceaccount:task-api:task-api-sa \
  -n task-api
```

**Output:**

```
no
```

```bash
kubectl auth can-i get configmaps \
  --as=system:serviceaccount:task-api:task-api-sa \
  -n default
```

**Output:**

```
no
```

The ServiceAccount can read ConfigMaps in its own namespace, but cannot create them, cannot access Secrets, and cannot access resources in other namespaces.

---

## Role vs ClusterRole: The Decision Matrix

When should you use Role (namespace-scoped) versus ClusterRole (cluster-scoped)?

| Scenario | Use | Why |
|----------|-----|-----|
| App reads its own ConfigMap | **Role + RoleBinding** | Namespace isolation is sufficient |
| App reads ConfigMaps in multiple namespaces | **ClusterRole + RoleBinding per namespace** | Reuse role definition without cluster-wide access |
| CI/CD creates Deployments across namespaces | **ClusterRole + RoleBinding per namespace** | Avoid ClusterRoleBinding's full cluster scope |
| Monitoring reads all Pods cluster-wide | **ClusterRole + ClusterRoleBinding** | Legitimate need for cluster-wide read access |
| Log aggregator collects from all namespaces | **ClusterRole + ClusterRoleBinding** | Must access every namespace |

### Key Principle: Prefer RoleBinding Over ClusterRoleBinding

Even when using a ClusterRole, you can bind it with a RoleBinding to limit scope to one namespace:

```yaml
# ClusterRole can be reused across namespaces
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: configmap-reader
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get", "list"]
---
# RoleBinding limits to specific namespace
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: dev-configmap-reader
  namespace: development
subjects:
- kind: ServiceAccount
  name: app-sa
  namespace: development
roleRef:
  kind: ClusterRole
  name: configmap-reader
  apiGroup: rbac.authorization.k8s.io
```

This pattern gives you reusable role definitions without cluster-wide access.

---

## Deploying with the ServiceAccount

To use your ServiceAccount in a Deployment, specify it in the pod spec:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: task-api
  namespace: task-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: task-api
  template:
    metadata:
      labels:
        app: task-api
    spec:
      serviceAccountName: task-api-sa
      automountServiceAccountToken: false  # Explicit override
      containers:
      - name: task-api
        image: ghcr.io/your-org/task-api:v1.0.0
        ports:
        - containerPort: 8000
```

When the pod needs to access the Kubernetes API (for example, to read its ConfigMap), you must explicitly mount the token:

```yaml
spec:
  serviceAccountName: task-api-sa
  automountServiceAccountToken: true  # Enable when API access needed
```

---

## Debugging RBAC Issues

When you see "403 Forbidden" errors, use these commands to diagnose:

### Check What Permissions a ServiceAccount Has

```bash
kubectl auth can-i --list \
  --as=system:serviceaccount:task-api:task-api-sa \
  -n task-api
```

**Output:**

```
Resources                                       Non-Resource URLs   Resource Names   Verbs
configmaps                                      []                  []               [get list]
selfsubjectaccessreviews.authorization.k8s.io   []                  []               [create]
selfsubjectrulesreviews.authorization.k8s.io    []                  []               [create]
```

### Describe RoleBinding to Verify Configuration

```bash
kubectl describe rolebinding task-api-binding -n task-api
```

**Output:**

```
Name:         task-api-binding
Namespace:    task-api
Role:
  Kind:  Role
  Name:  task-api-role
Subjects:
  Kind            Name           Namespace
  ----            ----           ---------
  ServiceAccount  task-api-sa    task-api
```

### Common RBAC Mistakes

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| All requests denied | RoleBinding missing or wrong namespace | Check binding exists in correct namespace |
| Can access in one namespace but not another | Using Role instead of ClusterRole | Create RoleBinding in each needed namespace |
| Token not found in pod | `automountServiceAccountToken: false` | Set to `true` if API access needed |
| Wrong ServiceAccount used | `serviceAccountName` not specified | Add `serviceAccountName` to pod spec |

---

## The Complete RBAC Pattern

Here's the complete set of resources in a single file for easy deployment. Create `task-api-rbac-complete.yaml`:

```yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: task-api-sa
  namespace: task-api
automountServiceAccountToken: false
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: task-api-role
  namespace: task-api
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: task-api-binding
  namespace: task-api
subjects:
- kind: ServiceAccount
  name: task-api-sa
  namespace: task-api
roleRef:
  kind: Role
  name: task-api-role
  apiGroup: rbac.authorization.k8s.io
```

Apply everything:

```bash
kubectl apply -f task-api-rbac-complete.yaml
```

**Output:**

```
serviceaccount/task-api-sa created
role.rbac.authorization.k8s.io/task-api-role created
rolebinding.rbac.authorization.k8s.io/task-api-binding created
```

---

## Reflect on Your Skill

Test whether your cloud-security skill generates least-privilege RBAC:

1. **Does your skill set `automountServiceAccountToken: false` by default?** If not, pods get tokens they might not need.

2. **Does your skill avoid wildcards in Role rules?** Check for `"*"` in apiGroups, resources, or verbs.

3. **Does your skill include the `kubectl auth can-i` verification step?** Testing before deploying prevents production issues.

If you found gaps, update your skill with the patterns from this lesson. Your skill should now generate the three-resource pattern (ServiceAccount + Role + RoleBinding) with least privilege defaults.

---

## Try With AI

Use your cloud-security skill to practice RBAC design for different scenarios.

**Prompt 1:**

```
Using my cloud-security skill, generate RBAC for a metrics-collector
ServiceAccount that needs to read Pod metrics across all namespaces.
Should I use Role or ClusterRole?
```

**What you're learning:** This scenario requires cluster-wide read access, which means ClusterRole + ClusterRoleBinding. Notice how the decision matrix guides you from requirements to the correct resource types. The skill should explain why Role won't work here.

**Prompt 2:**

```
My pod is getting "forbidden: User ... cannot get resource pods"
errors. Here's my Role definition. What's wrong?

apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: monitoring
rules:
- apiGroups: ["apps"]
  resources: ["pods"]
  verbs: ["get"]
```

**What you're learning:** Debugging RBAC errors by analyzing rule definitions. Pods are in the core API group (empty string ""), not "apps". The skill should identify this mismatch and provide the corrected YAML.

**Prompt 3:**

```
Audit this RBAC configuration for security issues:

rules:
- apiGroups: ["*"]
  resources: ["secrets"]
  verbs: ["*"]
```

**What you're learning:** Security review of RBAC rules. This rule grants full access to Secrets across all API groups, which violates least privilege. The skill should identify the wildcards as dangerous and suggest specific, minimal permissions instead.

:::warning Security Reminder
Always test RBAC changes with `kubectl auth can-i` before deploying. A misconfigured RoleBinding can grant more access than intended or block legitimate operations.
:::
