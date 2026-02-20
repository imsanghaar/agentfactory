# Feature Specification: Chapter 60 - Real Cloud Deployment

**Feature Branch**: `001-ch60-cloud-deployment`
**Created**: 2025-12-30
**Status**: Draft
**Input**: User description: "Chapter 60: Real Cloud Deployment - Deploy Task API to real cloud providers"

---

## Chapter Overview

Chapter 60 is the culmination of Part 7: AI Cloud Native Development. Students have containerized their Task API (Ch49), orchestrated it on local Kubernetes (Ch50), packaged it with Helm (Ch51), and configured enterprise infrastructure (Ch52-59). This chapter takes them to **real cloud production**.

**Key Insight**: Only cluster provisioning differs between cloud providers. Once you have a kubeconfig, everything else—kubectl, Helm, Dapr, Ingress, cert-manager—works identically across all clouds.

**Proficiency Level**: B1 (Intermediate)

---

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Docker containerization and multi-stage builds (Ch49)
- Kubernetes core concepts: Pods, Deployments, Services, ConfigMaps, Secrets (Ch50)
- Helm chart creation and templating (Ch51)
- Kafka event-driven patterns (Ch52)
- Dapr sidecar patterns, state management, pub/sub (Ch53)
- CI/CD with GitHub Actions and ArgoCD (Ch54)
- Observability with Prometheus, Grafana, OpenTelemetry (Ch55)
- Ingress, TLS/cert-manager, API Gateway patterns (Ch56)
- Security hardening and governance (Ch57-58)
- Infrastructure-as-Code concepts (Ch58)
- Dapr actors and workflows (Ch59)
- Task API application (Ch40)

**What this chapter must explain from scratch**:
- Cloud provider differences (pricing, features, CLI tools)
- Managed vs self-managed Kubernetes tradeoffs
- Cloud-specific CLI tools (doctl, az, gcloud, eksctl, civo, hetzner-k3s)
- Cloud LoadBalancer service behavior (vs local NodePort)
- DNS configuration for real domains
- Production cost estimation and management
- Budget-conscious cloud lab strategies

---

## Two Learning Paths

| Path | Provider | Cost | Best For |
|------|----------|------|----------|
| **Production** | DigitalOcean DOKS | ~$24+/mo | Real production deployments |
| **Learning Sandbox** | Hetzner + K3s | ~$5/mo | Persistent practice, budget learners |

---

## User Scenarios & Testing

### User Story 1 - Build Cloud Deployment Skill (Priority: P1)

A student creates a `multi-cloud-deployer` skill BEFORE learning cloud deployment details, following the Skill-First Learning Pattern. This skill becomes their reusable asset that improves throughout the chapter.

**Why this priority**: The Skill-First pattern ensures students OWN an asset, not just accumulate knowledge. This skill compounds across all future cloud deployments.

**Independent Test**: Student runs Claude Code with the skills-lab, creates a multi-cloud-deployer skill, and can use it to generate cloud deployment plans.

**Acceptance Scenarios**:

1. **Given** student has cloned skills-lab, **When** they run the skill creator prompt with DigitalOcean + K3s docs, **Then** a multi-cloud-deployer skill appears at `.claude/skills/multi-cloud-deployer/`
2. **Given** the skill exists, **When** student asks "help me deploy to DigitalOcean", **Then** skill provides accurate doctl commands

---

### User Story 2 - Deploy to Managed Kubernetes (DigitalOcean DOKS) (Priority: P1)

A student deploys their Task API to a real DigitalOcean Kubernetes cluster with full production stack (Dapr, Ingress, TLS, monitoring).

**Why this priority**: DOKS is the primary production path—simple, reliable, with free control plane and $200 new user credit.

**Independent Test**: Student can access https://tasks.yourdomain.com/health and receive a healthy response from their cloud-deployed Task API.

**Acceptance Scenarios**:

1. **Given** student has DigitalOcean account, **When** they run `doctl kubernetes cluster create`, **Then** a 3-node cluster is provisioned in ~5 minutes
2. **Given** cluster is running, **When** they run the same Helm install commands from Ch51, **Then** Task API deploys successfully (proving "same patterns everywhere")
3. **Given** LoadBalancer service is created, **When** DO provisions an external IP, **Then** student can configure DNS and access their API
4. **Given** cert-manager is installed, **When** Certificate is created, **Then** Let's Encrypt issues a valid TLS certificate

---

### User Story 3 - Set Up Budget Cloud Lab (Hetzner + K3s) (Priority: P2)

A student creates a persistent personal Kubernetes lab for ~$5/month using Hetzner Cloud and hetzner-k3s CLI.

**Why this priority**: Not all students can afford $24+/month. Hetzner + K3s provides real cloud experience at minimal cost, enabling persistent practice.

**Independent Test**: Student can kubectl get nodes against their Hetzner cluster and deploy the same Helm charts that worked on DOKS.

**Acceptance Scenarios**:

1. **Given** student has Hetzner Cloud account and API token, **When** they run `hetzner-k3s create --config cluster.yaml`, **Then** a K3s cluster is created in 2-3 minutes
2. **Given** Hetzner cluster is running, **When** student runs `helm upgrade --install task-api`, **Then** deployment succeeds (same chart works)
3. **Given** K3s includes Cloud Controller Manager, **When** student creates LoadBalancer Service, **Then** Hetzner LB is auto-provisioned

---

### User Story 4 - Understand Multi-Cloud Portability (Priority: P2)

A student learns that their kubectl, Helm, Dapr, and Ingress skills transfer across ALL cloud providers, with only the provisioning step being different.

**Why this priority**: This insight liberates students from cloud vendor lock-in fear. They understand they're learning universal patterns.

**Independent Test**: Student can explain the universal pattern: provision → connect → deploy, and identify which commands are cloud-specific vs universal.

**Acceptance Scenarios**:

1. **Given** student knows doctl commands, **When** they see AKS/GKE/EKS equivalents, **Then** they recognize the same provision → connect pattern
2. **Given** student has deployed to DOKS, **When** they switch kubeconfig to another provider, **Then** all kubectl/helm commands work unchanged

---

### User Story 5 - Production Checklist Verification (Priority: P2)

A student validates their cloud deployment against production readiness criteria before considering it "done".

**Why this priority**: Real production requires health checks, resource limits, monitoring integration, and cost awareness—not just "it deploys".

**Independent Test**: Student can run through a checklist and verify each item (health endpoint responds, resource limits set, Prometheus scrapes metrics).

**Acceptance Scenarios**:

1. **Given** Task API is deployed, **When** student checks `/health` endpoint, **Then** it returns healthy status
2. **Given** deployment has resource requests/limits, **When** student runs `kubectl describe pod`, **Then** limits are visible
3. **Given** Prometheus is installed (from Ch55), **When** student queries Grafana, **Then** Task API metrics appear

---

### User Story 6 - Cost Management and Teardown (Priority: P3)

A student understands the cost implications of their cloud resources and knows how to tear down clusters to avoid waste.

**Why this priority**: Students need to be cost-conscious. Leaving clusters running wastes money.

**Independent Test**: Student can estimate monthly cost for their cluster and successfully delete all resources.

**Acceptance Scenarios**:

1. **Given** cluster is running, **When** student calculates cost (nodes + LB + storage), **Then** estimate matches cloud provider dashboard
2. **Given** practice is complete, **When** student runs delete command, **Then** all cloud resources are removed

---

### Edge Cases

- What happens when student's credit card is declined? (Account creation fails gracefully)
- How does system handle cluster creation timeout? (Retry with `--wait` or check status)
- What if DNS propagation takes hours? (Test with IP first, explain DNS TTL)
- What happens when Let's Encrypt rate limits are hit? (Use staging issuer for testing)
- How to handle region/zone unavailability? (Choose alternative region)
- What if student already has a domain? (Use it; otherwise suggest free alternatives)

---

## Requirements

### Functional Requirements

- **FR-001**: Chapter MUST start with L00 "Build Your Cloud Deployment Skill" lesson following Skill-First pattern
- **FR-002**: Each lesson (L01-L10) MUST end with "Reflect on Your Skill" section
- **FR-003**: Chapter MUST cover DigitalOcean DOKS as primary production path with complete CLI workflow
- **FR-004**: Chapter MUST cover Hetzner + K3s as budget learning path (~$5/month)
- **FR-005**: Chapter MUST demonstrate that kubectl, Helm, Dapr, Ingress commands are identical across providers
- **FR-006**: Chapter MUST provide quick-start references for Azure AKS, GCP GKE, AWS EKS, and Civo
- **FR-007**: Chapter MUST include cost comparison table across providers with current pricing
- **FR-008**: Chapter MUST teach LoadBalancer service behavior in cloud (vs NodePort locally)
- **FR-009**: Chapter MUST cover DNS configuration for real domains with production TLS
- **FR-010**: Chapter MUST include production readiness checklist (health checks, resources, monitoring)
- **FR-011**: Chapter MUST provide explicit teardown instructions to avoid cost waste
- **FR-012**: Student skill name MUST be `multi-cloud-deployer`
- **FR-013**: Capstone MUST offer choice of three deployment paths (DOKS, Hetzner, AKS)
- **FR-014**: Chapter MUST use Task API as running example, consistent with Ch40-59

### Key Entities

- **Cloud Provider**: Organization offering managed or IaaS Kubernetes (DigitalOcean, Azure, Google, AWS, Civo, Hetzner)
- **Managed Kubernetes**: Provider-operated control plane with user-managed worker nodes
- **Self-Managed Kubernetes**: User operates everything (control plane + workers) on cloud VMs
- **LoadBalancer Service**: Kubernetes service type that provisions cloud load balancer with external IP
- **Cluster Provisioning CLI**: Cloud-specific tool for creating clusters (doctl, az, gcloud, eksctl, civo, hetzner-k3s)

---

## Lesson Structure

| # | Title | Layer | Duration | Focus |
|---|-------|-------|----------|-------|
| **L00** | Build Your Cloud Deployment Skill | L3 (Skill) | 15 min | Create multi-cloud-deployer skill |
| **L01** | Beyond Docker Desktop | L1 (Manual) | 25 min | Why real cloud, managed vs self-managed |
| **L02** | DigitalOcean Account & doctl Setup | L1 (Manual) | 20 min | Account, CLI, authentication |
| **L03** | Provisioning DOKS Cluster | L1 (Manual) | 30 min | Create cluster, connect kubectl |
| **L04** | Cloud Load Balancer & DNS | L1 (Manual) | 25 min | LoadBalancer service, DNS config |
| **L05** | Deploying Task API to DOKS | L2 (Collaboration) | 35 min | Full stack deployment |
| **L06** | Production Secrets & Configuration | L2 (Collaboration) | 25 min | Cloud secrets, ConfigMaps |
| **L07** | Personal Cloud Lab - Hetzner + K3s | L1 (Manual) | 30 min | Budget alternative setup |
| **L08** | Production Checklist & Verification | L2 (Collaboration) | 25 min | Health, resources, monitoring |
| **L09** | Same Patterns, Different Clouds | L2 (Collaboration) | 20 min | Multi-cloud portability |
| **L10** | Capstone - Full Production Deployment | L4 (Orchestration) | 45 min | End-to-end deployment |

**Total Duration**: ~295 minutes (~5 hours)

---

## Layer Progression

- **L00**: L3 (Skill) - Build skill upfront (Skill-First pattern)
- **L01-L04, L07**: L1 (Manual) - Build vocabulary and mental models through hands-on work
- **L05-L06, L08-L09**: L2 (Collaboration) - AI assists with deployment decisions
- **L10**: L4 (Orchestration) - Spec-driven capstone integrating all patterns

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students can provision a DigitalOcean DOKS cluster using doctl in under 10 minutes
- **SC-002**: Students can deploy Task API to cloud with full stack (Dapr + Ingress + TLS) in under 30 minutes
- **SC-003**: Students can access their deployed API via HTTPS on a real domain
- **SC-004**: Students understand that 90%+ of their Kubernetes commands work unchanged across providers
- **SC-005**: Students can provision a Hetzner K3s cluster for ~$5/month as a learning lab
- **SC-006**: Students can tear down all cloud resources and verify zero ongoing cost
- **SC-007**: Students' multi-cloud-deployer skill can generate accurate CLI commands for at least 3 providers
- **SC-008**: 100% of code examples include expected output blocks

---

## Prerequisites

- Chapter 40: Task API (the application to deploy)
- Chapter 49: Docker (containerized Task API image)
- Chapter 50: Kubernetes (kubectl skills, manifest understanding)
- Chapter 51: Helm (task-api chart exists)
- Chapter 53: Dapr (sidecar configuration)
- Chapter 55: Observability (optional but referenced)
- Chapter 56: Ingress/TLS (cert-manager, Traefik patterns)

---

## Not In Scope (Covered Elsewhere)

- Ingress controller deep dive (Ch56)
- TLS/cert-manager configuration details (Ch56)
- Helm chart creation from scratch (Ch51)
- Observability stack setup (Ch55)
- Security hardening details (Ch57-58)
- Dapr advanced patterns (Ch53, Ch59)

---

## Assumptions

- Students have completed Ch49-59 or equivalent
- Students have a credit/debit card for cloud account creation
- DigitalOcean $200 free credit is available for new users
- Students have a domain (or will use nip.io/sslip.io for testing)
- Task API Helm chart from Ch51 is available
- Container image is published to GHCR from Ch49/Ch54

---

## References

- Expertise Skill: `.claude/skills/building-with-multi-cloud/SKILL.md`
- DigitalOcean DOKS: https://docs.digitalocean.com/products/kubernetes/
- hetzner-k3s: https://github.com/vitobotta/hetzner-k3s
- Azure AKS: https://learn.microsoft.com/en-us/azure/aks/
- Google GKE: https://cloud.google.com/kubernetes-engine/docs
- AWS EKS: https://docs.aws.amazon.com/eks/
- Civo: https://www.civo.com/docs/kubernetes
