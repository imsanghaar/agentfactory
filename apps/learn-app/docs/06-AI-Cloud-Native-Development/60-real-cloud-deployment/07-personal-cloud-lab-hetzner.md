---
sidebar_position: 7
title: "Personal Cloud Lab - Hetzner + K3s"
description: "Set up a budget-friendly ~$5/month personal Kubernetes lab using Hetzner Cloud and hetzner-k3s CLI"
keywords:
  - hetzner
  - k3s
  - kubernetes
  - personal cloud lab
  - hetzner-k3s
  - budget kubernetes
  - lightweight kubernetes
chapter: 60
lesson: 7
duration_minutes: 30

# HIDDEN SKILLS METADATA
skills:
  - name: "Creating Hetzner Cloud Account"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3. Digital Content Creation"
    measurable_at_this_level: "Student creates Hetzner Cloud account and generates API token for programmatic cluster management"

  - name: "Installing hetzner-k3s CLI"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3.4 Programming"
    measurable_at_this_level: "Student installs hetzner-k3s CLI tool using go install or binary download"

  - name: "Writing K3s Cluster Configuration"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "3.4 Programming"
    measurable_at_this_level: "Student creates cluster.yaml file with master/worker pool definitions for budget-friendly cluster"

  - name: "Provisioning K3s on Hetzner"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Apply"
    digcomp_area: "5.3 Using digital tools to solve problems"
    measurable_at_this_level: "Student provisions K3s cluster using hetzner-k3s CLI and verifies nodes with kubectl"

  - name: "Understanding K3s vs Full Kubernetes"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "1.2 Understanding digital concepts and terminology"
    measurable_at_this_level: "Student explains differences between K3s and standard Kubernetes, including resource efficiency and feature tradeoffs"

  - name: "Cost Optimization for Cloud Resources"
    proficiency_level: "B1"
    category: "Conceptual"
    bloom_level: "Understand"
    digcomp_area: "4.4 Identifying digital competence gaps"
    measurable_at_this_level: "Student calculates monthly costs for Hetzner K3s clusters and compares with managed Kubernetes alternatives"

learning_objectives:
  - objective: "Create Hetzner Cloud account and generate API token for programmatic access"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Successfully generate API token and store securely as environment variable"

  - objective: "Install hetzner-k3s CLI tool using go install or binary download"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Verify installation with hetzner-k3s version command"

  - objective: "Write cluster.yaml configuration file for K3s cluster provisioning"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Valid YAML file with master pool, worker pool, and SSH configuration"

  - objective: "Provision K3s cluster on Hetzner Cloud using hetzner-k3s CLI"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "kubectl get nodes shows Ready status for all cluster nodes"

  - objective: "Explain differences between K3s and standard Kubernetes including resource efficiency"
    proficiency_level: "B1"
    bloom_level: "Understand"
    assessment_method: "Verbal explanation identifying K3s as lightweight distribution with single binary, sqlite storage, and reduced resource requirements"

cognitive_load:
  new_concepts: 6
  assessment: "6 concepts (Hetzner Cloud, API token, hetzner-k3s CLI, K3s, cluster.yaml, CCM) at target for B1 tier (7-10 concepts). Heavy scaffolding through step-by-step CLI commands and complete configuration examples."

differentiation:
  extension_for_advanced: "Configure HA setup with multiple masters; add private networking with Hetzner VPC; integrate with Hetzner Cloud Controller Manager for LoadBalancer services"
  remedial_for_struggling: "Focus on single-node cluster first; use exact configuration file provided without modification; verify each step before proceeding"
---

# Personal Cloud Lab - Hetzner + K3s

DigitalOcean DOKS is production-grade, but at ~$24+/month minimum, it's expensive for learning and experimentation. Sometimes you want a personal Kubernetes cluster where you can break things, try experimental configurations, and learn without worrying about costs.

Hetzner Cloud offers the most cost-effective path: real cloud servers at ~$5/month for a functional K3s cluster. K3s is a lightweight Kubernetes distribution that runs on smaller instances while remaining fully Kubernetes-compatible. Your kubectl commands, Helm charts, and Dapr configurations work identically.

---

## Why Hetzner + K3s for a Personal Lab?

Before diving into setup, understand why this combination works for budget-conscious learning.

### The Cost Comparison

| Provider | Minimum Setup | Monthly Cost | What You Get |
|----------|---------------|--------------|--------------|
| **DigitalOcean DOKS** | 2 nodes | ~$24 | Managed control plane, automatic updates |
| **Hetzner + K3s** | 1 master + 2 workers | ~$5-10 | Self-managed, full control, real servers |
| **AWS EKS** | 2 nodes + control plane | ~$75+ | Enterprise features, managed |
| **Docker Desktop K8s** | Local only | $0 | Not accessible externally |

Hetzner's CPX11 instances (2 vCPU, 2GB RAM) cost approximately $5.59/month (EUR 4.99). A minimal K3s cluster (1 master + 2 workers) runs around $17/month, or a single-node setup for learning costs under $6/month.

### What is K3s?

K3s is Kubernetes, stripped down to essentials:

```
Standard Kubernetes (K8s)          K3s (Lightweight)
┌──────────────────────┐          ┌──────────────────────┐
│ kube-apiserver       │          │                      │
│ kube-controller      │          │   Single binary      │
│ kube-scheduler       │    →     │   (k3s server)       │
│ etcd (cluster)       │          │   + sqlite/etcd      │
│ kubelet              │          │   + containerd       │
│ Multiple binaries    │          │                      │
└──────────────────────┘          └──────────────────────┘
   ~1GB+ RAM overhead                ~512MB RAM overhead
```

K3s achieves this by:
- **Single binary**: All components compiled into one executable
- **SQLite by default**: No separate etcd cluster needed (optional etcd for HA)
- **Containerd only**: No Docker dependency
- **Reduced features**: Removes legacy/alpha features rarely used
- **ARM support**: Runs on Raspberry Pi and ARM servers

**The key insight**: K3s is a certified Kubernetes distribution. Your kubectl commands, Helm charts, and YAML manifests work exactly the same. You're learning real Kubernetes, not a simulation.

---

## Prerequisites

Before starting, verify you have:

| Requirement | How to Check |
|-------------|--------------|
| **SSH key pair** | `ls ~/.ssh/id_rsa.pub` (must exist) |
| **Go installed** (for CLI) | `go version` (or use binary download) |
| **kubectl installed** | `kubectl version --client` |
| **Terminal access** | You're reading this, so you have one |

### Generate SSH Key (If Missing)

If you don't have an SSH key:

```bash
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
```

**Output:**
```
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/you/.ssh/id_rsa): [press Enter]
Enter passphrase (empty for no passphrase): [optional]
Your public key has been saved in /Users/you/.ssh/id_rsa.pub.
```

Accept defaults. This creates `~/.ssh/id_rsa` (private) and `~/.ssh/id_rsa.pub` (public).

---

## Step 1: Create Hetzner Cloud Account

Hetzner is a German cloud provider known for competitive pricing and reliable infrastructure.

### 1.1 Sign Up

1. Visit [console.hetzner.cloud](https://console.hetzner.cloud)
2. Click "Register" and create an account
3. Verify your email address
4. Complete identity verification (Hetzner requires this for new accounts)

**Note**: Hetzner's verification process may take 24-48 hours. They manually review accounts to prevent abuse. Plan ahead if you need the cluster immediately.

### 1.2 Create a Project

After verification:

1. Log into Hetzner Cloud Console
2. Click "New Project"
3. Name it something descriptive (e.g., "k3s-lab")
4. Click "Create Project"

### 1.3 Generate API Token

The hetzner-k3s CLI needs an API token to provision resources:

1. Select your project in Hetzner Console
2. Click "Security" in the left sidebar
3. Click "API Tokens" tab
4. Click "Generate API Token"
5. Name: `hetzner-k3s-cli`
6. Permissions: **Read & Write**
7. Click "Generate API Token"
8. **Copy the token immediately** (it won't be shown again)

**Security warning**: This token has full access to create and destroy resources. Store it securely.

### 1.4 Export Token as Environment Variable

```bash
export HCLOUD_TOKEN="your-api-token-here"
```

Add to your shell profile (~/.zshrc or ~/.bashrc) for persistence:

```bash
echo 'export HCLOUD_TOKEN="your-api-token-here"' >> ~/.zshrc
source ~/.zshrc
```

---

## Step 2: Install hetzner-k3s CLI

The hetzner-k3s CLI automates K3s cluster provisioning on Hetzner Cloud. It handles server creation, K3s installation, and kubeconfig generation.

### Option A: Install with Go (Recommended)

If you have Go installed:

```bash
go install github.com/vitobotta/hetzner-k3s@latest
```

**Output:**
```
go: downloading github.com/vitobotta/hetzner-k3s v2.x.x
```

Verify installation:

```bash
hetzner-k3s version
```

**Output:**
```
hetzner-k3s version 2.0.x
```

### Option B: Download Binary

If you don't have Go, download the binary directly:

**macOS (Apple Silicon):**
```bash
curl -L https://github.com/vitobotta/hetzner-k3s/releases/latest/download/hetzner-k3s-darwin-arm64 -o hetzner-k3s
chmod +x hetzner-k3s
sudo mv hetzner-k3s /usr/local/bin/
```

**macOS (Intel):**
```bash
curl -L https://github.com/vitobotta/hetzner-k3s/releases/latest/download/hetzner-k3s-darwin-amd64 -o hetzner-k3s
chmod +x hetzner-k3s
sudo mv hetzner-k3s /usr/local/bin/
```

**Linux (AMD64):**
```bash
curl -L https://github.com/vitobotta/hetzner-k3s/releases/latest/download/hetzner-k3s-linux-amd64 -o hetzner-k3s
chmod +x hetzner-k3s
sudo mv hetzner-k3s /usr/local/bin/
```

Verify:

```bash
hetzner-k3s version
```

---

## Step 3: Write cluster.yaml Configuration

The hetzner-k3s CLI uses a YAML configuration file to define your cluster. Create a file named `cluster.yaml`:

```yaml
---
cluster_name: task-api-lab
kubeconfig_path: ./kubeconfig
k3s_version: v1.31.4+k3s1

networking:
  ssh:
    port: 22
    use_agent: false
    public_key_path: ~/.ssh/id_rsa.pub
    private_key_path: ~/.ssh/id_rsa

masters_pool:
  instance_type: cpx11
  instance_count: 1
  location: fsn1

worker_pools:
  - name: default
    instance_type: cpx11
    instance_count: 2
    location: fsn1
```

### Understanding the Configuration

| Field | Value | Purpose |
|-------|-------|---------|
| `cluster_name` | task-api-lab | Name for your cluster and server prefix |
| `kubeconfig_path` | ./kubeconfig | Where to save cluster credentials |
| `k3s_version` | v1.31.4+k3s1 | K3s version to install |
| `masters_pool.instance_type` | cpx11 | Hetzner instance type (2 vCPU, 2GB RAM) |
| `masters_pool.instance_count` | 1 | Number of control plane nodes |
| `masters_pool.location` | fsn1 | Hetzner datacenter (Falkenstein, Germany) |
| `worker_pools[0].instance_count` | 2 | Number of worker nodes |

### Hetzner Instance Types

| Type | vCPU | RAM | Price/Month |
|------|------|-----|-------------|
| **cpx11** | 2 | 2 GB | ~$5.59 |
| cpx21 | 3 | 4 GB | ~$8.50 |
| cpx31 | 4 | 8 GB | ~$14.50 |
| cpx41 | 8 | 16 GB | ~$27.00 |

For a learning lab, `cpx11` is sufficient. Your Task API and supporting services fit comfortably in 2GB per node.

### Hetzner Locations

| Code | Location | Region |
|------|----------|--------|
| **fsn1** | Falkenstein, Germany | EU |
| nbg1 | Nuremberg, Germany | EU |
| hel1 | Helsinki, Finland | EU |
| ash | Ashburn, Virginia | US East |
| hil | Hillsboro, Oregon | US West |

Choose the location closest to you for lower latency.

---

## Step 4: Provision the Cluster

With configuration ready, provision your cluster:

```bash
hetzner-k3s create --config cluster.yaml
```

**Output:**
```
Creating master server...
Master server created: task-api-lab-master-1 (10.0.0.2)
Installing K3s on master...
K3s installed successfully
Creating worker servers...
Worker server created: task-api-lab-worker-1 (10.0.0.3)
Worker server created: task-api-lab-worker-2 (10.0.0.4)
Installing K3s on workers...
All workers joined the cluster
Kubeconfig saved to ./kubeconfig
```

This process takes 3-5 minutes. The CLI:
1. Creates Hetzner Cloud servers for master and workers
2. Installs K3s on the master node
3. Joins worker nodes to the cluster
4. Downloads kubeconfig to your local machine

---

## Step 5: Connect to Your Cluster

Set the KUBECONFIG environment variable to use your new cluster:

```bash
export KUBECONFIG=./kubeconfig
```

Verify connectivity:

```bash
kubectl get nodes
```

**Output:**
```
NAME                     STATUS   ROLES                  AGE   VERSION
task-api-lab-master-1    Ready    control-plane,master   2m    v1.31.4+k3s1
task-api-lab-worker-1    Ready    <none>                 1m    v1.31.4+k3s1
task-api-lab-worker-2    Ready    <none>                 1m    v1.31.4+k3s1
```

All nodes show `Ready` status. Your K3s cluster is operational.

### Verify Cluster Health

Check that system pods are running:

```bash
kubectl get pods -n kube-system
```

**Output:**
```
NAME                                      READY   STATUS    RESTARTS   AGE
coredns-7b98449c4-x7vqd                   1/1     Running   0          3m
local-path-provisioner-6c79684f77-8vhqj   1/1     Running   0          3m
metrics-server-5f9f776df5-k8xvz           1/1     Running   0          3m
traefik-6b84f7cbc-9gflw                   1/1     Running   0          3m
```

K3s includes:
- **CoreDNS**: Cluster DNS
- **Traefik**: Ingress controller (built-in)
- **Local Path Provisioner**: Default storage class
- **Metrics Server**: Resource metrics for kubectl top

---

## Step 6: Understanding Hetzner Cloud Controller Manager

When you create LoadBalancer services on Hetzner, the cluster needs the **Hetzner Cloud Controller Manager (CCM)** to provision Hetzner Load Balancers automatically.

The hetzner-k3s CLI can install CCM automatically. Add to your cluster.yaml:

```yaml
# ... existing configuration ...

additional_packages:
  - hetzner-ccm
```

If you already created your cluster, install CCM manually:

```bash
# Create secret with Hetzner API token
kubectl -n kube-system create secret generic hcloud \
  --from-literal=token=$HCLOUD_TOKEN \
  --from-literal=network=default

# Deploy CCM
kubectl apply -f https://github.com/hetznercloud/hcloud-cloud-controller-manager/releases/latest/download/ccm.yaml
```

**Output:**
```
secret/hcloud created
serviceaccount/cloud-controller-manager created
deployment.apps/hcloud-cloud-controller-manager created
```

With CCM installed, creating a `type: LoadBalancer` service automatically provisions a Hetzner Load Balancer (~$6/month additional).

---

## Step 7: Deploy a Test Application

Verify your cluster works by deploying a simple application:

```bash
kubectl create deployment nginx --image=nginx
kubectl expose deployment nginx --port=80 --type=NodePort
```

**Output:**
```
deployment.apps/nginx created
service/nginx exposed
```

Check the deployment:

```bash
kubectl get pods,svc
```

**Output:**
```
NAME                        READY   STATUS    RESTARTS   AGE
pod/nginx-76d6c9b8c-7xvqd   1/1     Running   0          30s

NAME                 TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/kubernetes   ClusterIP   10.43.0.1      <none>        443/TCP        5m
service/nginx        NodePort    10.43.45.123   <none>        80:31234/TCP   15s
```

Access nginx through any node's public IP:

```bash
# Get node external IPs
kubectl get nodes -o wide

# Access nginx (replace with your node IP and NodePort)
curl http://<node-external-ip>:31234
```

**Output:**
```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
```

Clean up the test:

```bash
kubectl delete deployment nginx
kubectl delete service nginx
```

---

## Cost Breakdown: What You're Paying

With the configuration in this lesson:

| Resource | Count | Monthly Cost |
|----------|-------|--------------|
| Master (cpx11) | 1 | ~$5.59 |
| Workers (cpx11) | 2 | ~$11.18 |
| **Total** | - | **~$16.77** |

For a minimal single-node learning cluster:

```yaml
masters_pool:
  instance_type: cpx11
  instance_count: 1
  location: fsn1

worker_pools: []  # No workers, master runs workloads
```

This costs ~$5.59/month. K3s can run workloads on the control plane node.

### Comparison with DOKS

| Setup | Hetzner K3s | DigitalOcean DOKS |
|-------|-------------|-------------------|
| Single-node learning | ~$6/month | N/A (2 nodes minimum) |
| 1 master + 2 workers | ~$17/month | ~$24/month |
| Managed control plane | No | Yes |
| Auto-updates | No | Yes |
| Support SLA | Community | Business |

**When to choose Hetzner K3s**:
- Learning and experimentation
- Budget-conscious projects
- Full control needed
- Non-production workloads

**When to choose DOKS**:
- Production workloads
- Team environments
- Need managed upgrades
- SLA requirements

---

## Cleanup: Destroying Your Cluster

When you're done experimenting, destroy the cluster to stop charges:

```bash
hetzner-k3s delete --config cluster.yaml
```

**Output:**
```
Deleting worker servers...
Deleted: task-api-lab-worker-1
Deleted: task-api-lab-worker-2
Deleting master servers...
Deleted: task-api-lab-master-1
Cluster task-api-lab deleted
```

**Important**: This permanently destroys all servers and data. Export any important configurations first.

---

## Try With AI

Now that you have a personal cloud lab, explore K3s and Hetzner further with your AI companion.

### Prompt 1: Understand K3s Architecture

```
I just provisioned a K3s cluster on Hetzner Cloud. K3s runs as a single binary
instead of multiple components like standard Kubernetes. Help me understand:

1. What components are compiled into the k3s binary?
2. How does K3s handle storage without etcd in single-server mode?
3. What are the tradeoffs of using K3s vs full Kubernetes for production?

I want to understand when K3s is appropriate and when I should choose managed
Kubernetes like DOKS or EKS.
```

**What you're learning**: Understanding K3s architecture helps you make informed decisions about when lightweight Kubernetes is appropriate versus when you need full enterprise features.

### Prompt 2: Compare Cloud Provider Costs

```
I'm running a personal K3s lab on Hetzner at ~$15/month. Compare the costs if
I wanted to run similar workloads on:

1. DigitalOcean (DOKS or droplets + K3s)
2. AWS (EKS or EC2 + K3s)
3. Google Cloud (GKE or Compute Engine + K3s)

Include hidden costs like egress bandwidth, load balancers, and persistent
storage. I want to understand the true cost of cloud Kubernetes.
```

**What you're learning**: Cloud pricing is complex. Understanding all cost components helps you budget accurately and choose providers based on your actual workload patterns.

### Prompt 3: Plan Production Migration

```
I've been learning on my Hetzner K3s cluster. Now I want to migrate my Task API
to production. Help me plan the migration:

1. What would I need to change in my Helm charts for managed Kubernetes?
2. How do I handle the transition from Traefik (K3s default) to other ingress controllers?
3. What configurations are K3s-specific vs portable to any Kubernetes?

I want to ensure my learning transfers to production without major rewrites.
```

**What you're learning**: Skill portability is the goal. Understanding what's K3s-specific versus universal Kubernetes ensures your learning applies to any cluster.

### Safety Note

Hetzner servers have public IPs by default. Your cluster is internet-accessible. Before deploying sensitive workloads, implement network policies, firewall rules, and authentication. Never expose sensitive services without TLS and proper access controls.

---

## Reflect on Your Skill

You built a `multi-cloud-deployer` skill in Lesson 0. Test and improve it based on what you learned about Hetzner and K3s.

### Test Your Skill

```
Using my multi-cloud-deployer skill, generate the hetzner-k3s configuration
for a minimal learning cluster (1 node, cpx11, fsn1 location).
```

Does your skill produce valid cluster.yaml? Does it explain K3s versus full Kubernetes tradeoffs?

### Identify Gaps

Ask yourself:
- Does my skill include Hetzner-specific patterns (API token, instance types, locations)?
- Can it generate both single-node and multi-node configurations?
- Does it explain K3s architecture and when to choose it?

### Improve Your Skill

If you found gaps:

```
My multi-cloud-deployer skill is missing Hetzner K3s patterns. Update it to include:
- Hetzner Cloud API token configuration
- hetzner-k3s CLI installation and usage
- cluster.yaml templates for single-node and multi-node setups
- K3s vs full Kubernetes comparison for decision-making
```

---
