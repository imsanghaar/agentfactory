---
sidebar_position: 10
title: "Capstone: Full Production Deployment"
description: "Complete an end-to-end production deployment using specification-first approach, producing a deployable Digital FTE component"
keywords: [kubernetes, cloud deployment, production, DOKS, Hetzner, specification, capstone, digital-fte]
chapter: 60
lesson: 10
duration_minutes: 45
proficiency_level: B1
teaching_stage: 4
stage_name: "Spec-Driven Integration"
stage_description: "Apply all cloud deployment skills through specification-first capstone project"

skills:
  - name: "Specification-First Deployment"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Create"
    digcomp_area: "3.4 Programming"
    measurable_at_this_level: "Student writes deployment specification before provisioning any infrastructure"

  - name: "Multi-Cloud Cluster Provisioning"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3.4 Programming"
    measurable_at_this_level: "Student provisions Kubernetes cluster on chosen provider using CLI tools"

  - name: "Full Stack Deployment"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3.4 Programming"
    measurable_at_this_level: "Student deploys Dapr, Ingress, cert-manager, and application in correct sequence"

  - name: "Production Verification"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Evaluate"
    digcomp_area: "5.3 Problem Solving"
    measurable_at_this_level: "Student validates HTTPS endpoint accessibility and health check responses"

  - name: "Cost-Conscious Teardown"
    proficiency_level: "B1"
    category: "Procedural"
    bloom_level: "Apply"
    digcomp_area: "5.3 Problem Solving"
    measurable_at_this_level: "Student executes complete teardown and verifies zero ongoing costs"

learning_objectives:
  - objective: "Write complete deployment specification before provisioning infrastructure"
    proficiency_level: "B1"
    bloom_level: "Create"
    assessment_method: "Complete specification document with provider, resources, stack components, and success criteria"

  - objective: "Provision Kubernetes cluster on chosen cloud provider"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "kubectl get nodes returns Ready status for all nodes"

  - objective: "Deploy complete production stack including Dapr, Ingress, and TLS"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "All deployments show Running status, Ingress has external IP"

  - objective: "Validate production deployment with HTTPS endpoint"
    proficiency_level: "B1"
    bloom_level: "Evaluate"
    assessment_method: "curl https://tasks.yourdomain.com/health returns 200 with valid certificate"

  - objective: "Execute complete teardown with cost verification"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Provider dashboard shows no active resources, billing confirms $0 ongoing charges"

cognitive_load:
  new_concepts: 4
  assessment: "Specification-first workflow, convergence loop, skill composition, cost verification"

differentiation:
  extension_for_advanced: "Deploy to secondary provider using same specification pattern, compare deployment times"
  remedial_for_struggling: "Use provided specification template, focus on single provider path"
---

# Capstone: Full Production Deployment

Throughout this chapter, you've built cloud deployment knowledge step by step: cluster provisioning with doctl and hetzner-k3s, load balancer configuration, stack deployment with Dapr and Traefik, secrets management, and production verification. Now it's time to apply everything to a complete production scenario.

In previous lessons, you deployed components individually. You tested pieces in isolation. But production deployment isn't about individual commands working in isolation. Production deployment is about the complete sequence: from empty cloud account to working HTTPS endpoint serving real traffic.

This capstone brings it all together. You'll write a deployment specification FIRST, provision real infrastructure, deploy your complete stack, verify with HTTPS, and execute a clean teardown. The specification-first approach is what separates professional cloud engineering from Vibe Coding.

The result: your `multi-cloud-deployer` skill becomes production-ready. It's not a theoretical exercise. It's a verified, tested Digital FTE component you can use for real deployments.

---

## Phase 1: Write the Deployment Specification

Before touching any CLI tools, write your specification. This forces you to think about environment choices, resource requirements, success criteria, and cost constraints before any infrastructure exists.

**Create this file in your project directory:**

**File: deployment-spec.md**

```markdown
# Deployment Specification: Task API Production

## Target Environment
- **Provider**: [DOKS | Hetzner | AKS]
- **Region**: [region]
- **Cluster Name**: task-api-prod
- **Domain**: tasks.yourdomain.com

## Resource Requirements
- **Nodes**: 3
- **Node Size**: 2 vCPU, 4GB RAM
- **Replicas**: 2
- **Memory Limit**: 512Mi
- **CPU Limit**: 500m

## Stack Components
- [x] Task API (FastAPI + SQLModel)
- [x] Dapr sidecar (state management)
- [x] Traefik Ingress
- [x] cert-manager + Let's Encrypt

## Success Criteria
- [ ] Cluster provisioned in < 10 minutes
- [ ] Full deployment in < 30 minutes
- [ ] HTTPS endpoint accessible
- [ ] Health check returns 200
- [ ] Teardown verified ($0 cost)

## Non-Goals
- [ ] Database persistence (use in-memory for capstone)
- [ ] Monitoring stack (covered in Ch55)
- [ ] CI/CD integration (covered in Ch54)
```

**Why specification first?**

Without a spec, you'd start running `doctl kubernetes cluster create` and figure things out as you go. That's Vibe Coding. You might choose the wrong node size. You might forget TLS configuration until you're debugging certificate errors at 2 AM. You might deploy to the most expensive region.

The spec makes constraints explicit BEFORE you provision. It's your contract with yourself and your budget.

---

## Phase 2: Choose Your Deployment Path

This capstone supports three deployment paths. Each path produces identical outcomes with different providers and cost profiles.

### Path A: DigitalOcean DOKS (Production Path)

**Best for:** Teams, real traffic, managed SLA

**Monthly cost:** ~$48+ (3-node cluster minimum)

**Provisioning command:**

```bash
doctl kubernetes cluster create task-api-prod \
  --region nyc1 \
  --node-pool "name=default;size=s-2vcpu-4gb;count=3" \
  --wait
```

**Output:**
```
Notice: Cluster is provisioning, waiting for cluster to be running
..............
Notice: Cluster created, fetching credentials
Notice: Adding cluster credentials to kubeconfig file found in "/home/user/.kube/config"
```

**Connect and verify:**

```bash
doctl kubernetes cluster kubeconfig save task-api-prod
kubectl get nodes
```

**Output:**
```
NAME                      STATUS   ROLES    AGE   VERSION
task-api-prod-default-0   Ready    <none>   2m    v1.28.2
task-api-prod-default-1   Ready    <none>   2m    v1.28.2
task-api-prod-default-2   Ready    <none>   2m    v1.28.2
```

---

### Path B: Hetzner + K3s (Budget Path)

**Best for:** Personal practice, budget-conscious learners

**Monthly cost:** ~$15 (3x CX22 servers)

**Provisioning command:**

```bash
hetzner-k3s create \
  --cluster-name task-api-prod \
  --location fsn1 \
  --masters-pool-size 1 \
  --workers-pool-size 2 \
  --instance-type cx22
```

**Output:**
```
Creating cluster task-api-prod in fsn1...
Creating master node...
Creating worker nodes...
Installing k3s on master...
Joining workers to cluster...
Cluster ready. Kubeconfig saved to ./kubeconfig
```

**Connect and verify:**

```bash
export KUBECONFIG=./kubeconfig
kubectl get nodes
```

**Output:**
```
NAME                       STATUS   ROLES                  AGE   VERSION
task-api-prod-master-1     Ready    control-plane,master   3m    v1.28.2+k3s1
task-api-prod-worker-1     Ready    <none>                 2m    v1.28.2+k3s1
task-api-prod-worker-2     Ready    <none>                 2m    v1.28.2+k3s1
```

---

### Path C: Azure AKS (Enterprise Path)

**Best for:** Enterprise environments, Azure ecosystem integration

**Monthly cost:** ~$75+ (3-node cluster)

**Provisioning command:**

```bash
az aks create \
  --resource-group task-api-rg \
  --name task-api-prod \
  --location eastus \
  --node-count 3 \
  --node-vm-size Standard_B2s \
  --generate-ssh-keys
```

**Connect and verify:**

```bash
az aks get-credentials --resource-group task-api-rg --name task-api-prod
kubectl get nodes
```

---

## Phase 3: Deploy the Complete Stack

With your cluster provisioned, deploy the complete production stack. This sequence is universal across all providers.

### Step 1: Install Dapr

```bash
dapr init -k --wait
```

**Output:**
```
Making the jump to hyperspace...
Deploying the Dapr control plane to your cluster...
Success! Dapr has been installed to namespace dapr-system.
```

**Verify:**

```bash
dapr status -k
```

**Output:**
```
NAME                   NAMESPACE    HEALTHY  STATUS   REPLICAS  VERSION
dapr-sentry            dapr-system  True     Running  1         1.12.0
dapr-operator          dapr-system  True     Running  1         1.12.0
dapr-placement-server  dapr-system  True     Running  1         1.12.0
dapr-sidecar-injector  dapr-system  True     Running  1         1.12.0
```

### Step 2: Install Traefik Ingress

```bash
helm repo add traefik https://traefik.github.io/charts
helm repo update
helm install traefik traefik/traefik -n traefik --create-namespace
```

**Output:**
```
NAME: traefik
NAMESPACE: traefik
STATUS: deployed
```

**Get the Load Balancer IP:**

```bash
kubectl get svc traefik -n traefik -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
```

**Output:**
```
143.244.156.78
```

Record this IP for DNS configuration.

### Step 3: Install cert-manager

```bash
helm repo add jetstack https://charts.jetstack.io
helm repo update
helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --set installCRDs=true
```

**Output:**
```
NAME: cert-manager
NAMESPACE: cert-manager
STATUS: deployed
```

### Step 4: Configure Let's Encrypt ClusterIssuer

**File: cluster-issuer.yaml**

```yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    email: your-email@example.com
    server: https://acme-v02.api.letsencrypt.org/directory
    privateKeySecretRef:
      name: letsencrypt-prod-key
    solvers:
      - http01:
          ingress:
            class: traefik
```

**Apply:**

```bash
kubectl apply -f cluster-issuer.yaml
```

**Output:**
```
clusterissuer.cert-manager.io/letsencrypt-prod created
```

### Step 5: Deploy Task API

**File: task-api-deployment.yaml**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: task-api
  annotations:
    dapr.io/enabled: "true"
    dapr.io/app-id: "task-api"
    dapr.io/app-port: "8000"
spec:
  replicas: 2
  selector:
    matchLabels:
      app: task-api
  template:
    metadata:
      labels:
        app: task-api
      annotations:
        dapr.io/enabled: "true"
        dapr.io/app-id: "task-api"
        dapr.io/app-port: "8000"
    spec:
      containers:
        - name: task-api
          image: yourusername/task-api:v1
          ports:
            - containerPort: 8000
          resources:
            limits:
              memory: "512Mi"
              cpu: "500m"
            requests:
              memory: "256Mi"
              cpu: "250m"
          livenessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 10
            periodSeconds: 30
          readinessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 5
            periodSeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: task-api
spec:
  selector:
    app: task-api
  ports:
    - port: 80
      targetPort: 8000
```

**Apply:**

```bash
kubectl apply -f task-api-deployment.yaml
```

**Output:**
```
deployment.apps/task-api created
service/task-api created
```

### Step 6: Configure Ingress with TLS

**File: task-api-ingress.yaml**

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: task-api-ingress
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  ingressClassName: traefik
  tls:
    - hosts:
        - tasks.yourdomain.com
      secretName: task-api-tls
  rules:
    - host: tasks.yourdomain.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: task-api
                port:
                  number: 80
```

**Apply:**

```bash
kubectl apply -f task-api-ingress.yaml
```

**Output:**
```
ingress.networking.k8s.io/task-api-ingress created
```

---

## Phase 4: The Convergence Loop

Real deployments rarely work perfectly on the first try. This phase demonstrates the iterative refinement process that produces working production systems.

### Iteration 1: Initial Deployment Attempt

After applying all resources, check status:

```bash
kubectl get pods
kubectl get ingress
kubectl get certificate
```

**Common issues and their indicators:**

| Issue | Symptom | Detection Command |
|-------|---------|-------------------|
| Image pull failure | `ImagePullBackOff` status | `kubectl describe pod task-api-xxx` |
| DNS not propagated | Certificate stuck at `False` | `kubectl get certificate` |
| Health check failing | `CrashLoopBackOff` | `kubectl logs task-api-xxx` |
| Load Balancer pending | `EXTERNAL-IP: <pending>` | `kubectl get svc traefik -n traefik` |

### Iteration 2: Troubleshoot and Fix

**For image pull issues:**

```bash
kubectl describe pod task-api-xxx | grep -A 5 "Events"
```

If you see "unauthorized," create an image pull secret:

```bash
kubectl create secret docker-registry regcred \
  --docker-server=docker.io \
  --docker-username=yourusername \
  --docker-password=yourtoken
```

**For DNS issues:**

Point your domain's A record to the Load Balancer IP. Verify propagation:

```bash
dig tasks.yourdomain.com +short
```

**Output:**
```
143.244.156.78
```

**For certificate issues:**

Check cert-manager logs:

```bash
kubectl logs -n cert-manager -l app=cert-manager
```

### Iteration 3: Verify Success

When all issues are resolved:

```bash
# All pods running
kubectl get pods
```

**Output:**
```
NAME                        READY   STATUS    RESTARTS   AGE
task-api-7b9f5d6c4d-abc12   2/2     Running   0          5m
task-api-7b9f5d6c4d-def34   2/2     Running   0          5m
```

```bash
# Certificate ready
kubectl get certificate
```

**Output:**
```
NAME           READY   SECRET         AGE
task-api-tls   True    task-api-tls   3m
```

```bash
# HTTPS endpoint working
curl https://tasks.yourdomain.com/health
```

**Output:**
```json
{"status": "healthy", "service": "task-api"}
```

---

## Phase 5: Production Verification Checklist

Go back to your specification and verify each success criterion:

| Success Criterion | Status | Evidence |
|-------------------|--------|----------|
| Cluster provisioned in &lt; 10 minutes | PASS | `kubectl get nodes` shows Ready in 8m |
| Full deployment in &lt; 30 minutes | PASS | Total deployment time: 22 minutes |
| HTTPS endpoint accessible | PASS | `curl https://tasks.yourdomain.com/health` returns 200 |
| Health check returns 200 | PASS | Response: `{"status": "healthy"}` |
| Teardown verified ($0 cost) | PENDING | Execute Phase 6 |

---

## Phase 6: Complete Teardown with Cost Verification

Production capstones aren't complete without teardown. You must prove zero ongoing costs.

### For DigitalOcean DOKS

```bash
# Delete the cluster
doctl kubernetes cluster delete task-api-prod --force

# Verify no lingering resources
doctl kubernetes cluster list
doctl compute load-balancer list
```

**Output:**
```
ID    Name    Region    Status
(empty - no clusters)
```

### For Hetzner + K3s

```bash
# Delete the cluster
hetzner-k3s delete --cluster-name task-api-prod

# Verify no servers remain
hcloud server list
```

**Output:**
```
ID   NAME   STATUS   IPV4   IPV6   DATACENTER
(empty - no servers)
```

### For Azure AKS

```bash
# Delete the resource group (removes everything)
az group delete --name task-api-rg --yes --no-wait

# Verify deletion
az aks list --output table
```

### Cost Verification

**Check your provider dashboard:**

1. Log in to your cloud provider's billing console
2. Verify no active resources
3. Confirm next billing cycle shows $0 for this project

Update your specification checklist:

| Success Criterion | Status |
|-------------------|--------|
| Teardown verified ($0 cost) | PASS |

**All criteria met. Specification satisfied.**

---

## Final Skill Evaluation Rubric

Your `multi-cloud-deployer` skill has been tested and refined throughout this chapter. Evaluate its production readiness:

| Criterion | Weight | Pass Criteria | Your Score |
|-----------|--------|---------------|------------|
| Spec completeness | 20% | All required sections present | /20 |
| Deployment success | 40% | HTTPS endpoint accessible | /40 |
| Skill quality | 30% | Generates commands for 3+ providers | /30 |
| Teardown verification | 10% | $0 ongoing cost confirmed | /10 |

**Total: /100**

**Scoring guide:**

- **90-100:** Your skill is production-ready and sellable as a Digital FTE component
- **70-89:** Minor gaps to address, but functional for personal use
- **50-69:** Significant improvements needed before production use
- **Below 50:** Return to earlier lessons and rebuild skill foundations

---

## Reflect on Your Skill

Your `multi-cloud-deployer` skill has evolved through this chapter. It started as a skeleton created from official documentation. Now it's been tested against real cloud infrastructure.

**Final Test:** Ask your skill:

```text
Generate a complete deployment plan for Task API on DigitalOcean DOKS
with Dapr, Ingress, and TLS.
```

**Evaluate the output:**

- Does it include all provisioning commands (`doctl kubernetes cluster create`)?
- Does it include the deployment sequence (Dapr -> Traefik -> cert-manager -> app)?
- Does it include verification steps (`kubectl get pods`, `curl https://...`)?
- Does it include teardown commands (`doctl kubernetes cluster delete`)?

**Your skill is production-ready when:**

- It generates accurate CLI commands for at least 3 providers (DOKS, Hetzner, AKS)
- It includes the universal "provision -> connect -> deploy" pattern
- It can answer questions about cost and tradeoffs between providers
- It produces deployment sequences that work on first try (or identifies likely issues)

**This skill is now part of your Digital FTE portfolio.**

You don't just "know cloud deployment." You OWN a verified, production-tested skill that can deploy AI agent services to any major cloud provider. This is the outcome of the Skill-First Learning Pattern: not knowledge, but assets.

---

## Try With AI

You've completed the capstone by following the specification-first approach. Now extend your deployment skills through AI collaboration.

**Prompt 1: Specification Review**

```text
Review my deployment specification for gaps:

[Paste your deployment-spec.md content]

Questions to consider:
- What failure scenarios am I not accounting for?
- Should I add rollback procedures?
- What monitoring should I configure for production?
```

**What you're learning:** AI can review specifications and identify blind spots. It might suggest failover strategies, backup procedures, or monitoring configurations you hadn't considered. You evaluate each suggestion against your actual production requirements.

**Prompt 2: Multi-Cloud Comparison**

```text
I've deployed my Task API to DigitalOcean DOKS. Help me understand:

1. What would change if I deployed to GKE instead?
2. What would change if I deployed to EKS?
3. What's truly universal vs provider-specific?

Focus on practical differences that affect deployment time and cost.
```

**What you're learning:** The "provision -> connect -> deploy" pattern is universal, but provisioning commands differ. AI helps you understand which skills transfer directly and which require adaptation.

**Prompt 3: Production Hardening**

```text
My Task API is deployed with HTTPS. What production hardening steps
am I missing? Consider:

- Network policies
- Pod security standards
- Resource quotas
- Backup procedures

Prioritize by risk: what gaps would cause the biggest production issues?
```

**What you're learning:** A working deployment isn't a hardened deployment. AI helps you identify the gap between "it runs" and "it's production-ready." You evaluate each recommendation against your application's actual risk profile.

**Safety note:** When sharing deployment specifications with AI, redact actual domain names, IP addresses, and cloud credentials. Replace real values with placeholders like `yourdomain.com` or `YOUR_API_TOKEN`.
