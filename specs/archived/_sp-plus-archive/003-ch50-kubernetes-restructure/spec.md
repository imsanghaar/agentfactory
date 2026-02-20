# Feature Specification: Chapter 50 Kubernetes Restructure

**Feature Branch**: `003-ch50-kubernetes-restructure`
**Created**: 2025-12-27
**Status**: Draft
**Related Issues**: #548 (Replace Minikube), #549 (Reorganize lessons)

## Context

This is a RESTRUCTURE of Chapter 50: Kubernetes for AI Services.

**Current State**: 23 lessons using Minikube
**Target State**: 22 lessons (15 core + 7 optional) using Docker Desktop Kubernetes

**Part**: 7 - AI Cloud-Native Development
**Proficiency Level**: B1-B2 (Intermediate to Upper-Intermediate)

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Docker fundamentals from Chapter 49 (images, containers, Dockerfiles)
- Production container image of Task API pushed to registry (Ch49 capstone)
- FastAPI from Part 6
- Basic command-line operations

**What this chapter must explain from scratch**:
- Kubernetes architecture (control plane, workers, declarative model)
- All Kubernetes primitives (Pods, Deployments, Services, etc.)
- kubectl CLI operations
- YAML manifest syntax

## User Scenarios & Testing

### User Story 1 - Core Kubernetes Deployment (Priority: P1)

Students learn essential Kubernetes concepts to deploy their Task API container to a cluster with production-ready configuration.

**Why this priority**: Core path covers 90% of agent deployment needs. Most AI agents are stateless services that need Deployments, Services, ConfigMaps, health checks, and RBAC.

**Independent Test**: After completing core lessons 1-15, student can deploy Task API to Kubernetes with health checks, resource limits, autoscaling, and RBAC.

**Acceptance Scenarios**:

1. **Given** Docker Desktop installed, **When** student enables Kubernetes, **Then** `kubectl get nodes` shows `docker-desktop` Ready
2. **Given** Task API container image, **When** student applies Deployment manifest, **Then** Pod runs successfully
3. **Given** running Pod, **When** student applies Service manifest, **Then** API accessible via port-forward
4. **Given** configured health checks, **When** container health fails, **Then** Kubernetes restarts Pod automatically

---

### User Story 2 - AI-Assisted Operations (Priority: P2)

Students use kubectl-ai to generate manifests and debug cluster issues using natural language.

**Why this priority**: Layer 2 collaboration builds on Layer 1 foundation. Students must understand K8s concepts before AI-assisted generation.

**Independent Test**: Student uses kubectl-ai to generate and apply a complete deployment manifest from natural language description.

**Acceptance Scenarios**:

1. **Given** kubectl-ai installed, **When** student asks "deploy my-api with 3 replicas", **Then** tool generates valid Deployment YAML
2. **Given** failing Pod, **When** student asks "why is my-api pod failing", **Then** tool provides diagnostic steps

---

### User Story 3 - Capstone Deployment (Priority: P3)

Students complete spec-driven deployment of Task API with all production patterns.

**Why this priority**: Layer 4 capstone synthesizes all concepts into complete deployment.

**Independent Test**: Student deploys Task API with ConfigMaps, Secrets, health probes, resource limits, HPA, and RBAC using spec-driven approach.

**Acceptance Scenarios**:

1. **Given** deployment specification, **When** student implements all requirements, **Then** API runs with all production patterns
2. **Given** traffic spike, **When** HPA triggers, **Then** replicas scale automatically

---

### User Story 4 - Optional Advanced Patterns (Priority: P4)

Students learn advanced patterns (init containers, sidecars, StatefulSets, Ingress, persistent storage) for specialized use cases.

**Why this priority**: Optional for students who need these patterns. Not required for basic agent deployment.

**Independent Test**: Each optional lesson is standalone - student can complete any without others.

**Acceptance Scenarios**:

1. **Given** need for initialization, **When** student applies init container pattern, **Then** main container starts after init completes
2. **Given** need for sidecar logging, **When** student applies sidecar pattern, **Then** logs collected to separate container

---

### Edge Cases

- What happens when Docker Desktop Kubernetes fails to enable? Provide troubleshooting steps
- How to handle resource-constrained machines? Provide minimum specs and recommendations
- What if student's Task API image isn't in registry? Reference Ch49 push step

## Requirements

### Functional Requirements

- **FR-001**: Chapter MUST use Docker Desktop Kubernetes instead of Minikube
- **FR-002**: Lesson 2 MUST be completely rewritten for Docker Desktop enablement
- **FR-003**: All Minikube references across all lessons MUST be replaced
- **FR-004**: Core lessons (1-15) MUST provide complete agent deployment path
- **FR-005**: Optional lessons (16-22) MUST be clearly marked with "(Optional)" suffix
- **FR-006**: Helm lesson 21 MUST be moved to Chapter 51 as new lesson 01
- **FR-007**: All lessons MUST use Task API container from Ch49 as running example
- **FR-008**: Each lesson MUST have full YAML frontmatter (skills, learning_objectives, cognitive_load)
- **FR-009**: Each lesson MUST have 3 "Try With AI" prompts with explanations
- **FR-010**: All kubectl commands MUST show expected output blocks

### Lesson Mapping (Current → Target)

#### Core Lessons (Required)

| Target # | Source # | Title | Action |
|----------|----------|-------|--------|
| 01 | 01 | Kubernetes Architecture & Declarative Model | UPDATE |
| 02 | 02 | Enabling Kubernetes (Docker Desktop) | REWRITE |
| 03 | 03 | Pods: The Atomic Unit | UPDATE |
| 04 | 04 | Deployments: Self-Healing at Scale | UPDATE |
| 05 | 05 | Services & Networking | UPDATE |
| 06 | 08 | Namespaces: Virtual Clusters | UPDATE + RENUMBER |
| 07 | 11 | ConfigMaps & Secrets | UPDATE + RENUMBER |
| 08 | 14 | Resource Management & Debugging | UPDATE + RENUMBER |
| 09 | 15 | Horizontal Pod Autoscaler | UPDATE + RENUMBER |
| 10 | 16 | RBAC: Securing Agent Deployments | UPDATE + RENUMBER |
| 11 | 18 | Health Checks & Probes | UPDATE + RENUMBER |
| 12 | 19 | Jobs & CronJobs: Batch Workloads | UPDATE + RENUMBER |
| 13 | 20 | AI-Assisted K8s with kubectl-ai | UPDATE + RENUMBER |
| 14 | 22 | Capstone: Deploy Agent to K8s | UPDATE + RENUMBER |
| 15 | 23 | Building K8s Deployment Skill | UPDATE + RENUMBER |

#### Optional Lessons (Advanced)

| Target # | Source # | Title | Action |
|----------|----------|-------|--------|
| 16 | 06 | Init Containers (Optional) | UPDATE + RENAME + RENUMBER |
| 17 | 07 | Sidecar Containers (Optional) | UPDATE + RENAME + RENUMBER |
| 18 | 09 | Ingress: External Access (Optional) | UPDATE + RENAME + RENUMBER |
| 19 | 10 | Service Discovery Deep Dive (Optional) | UPDATE + RENAME + RENUMBER |
| 20 | 13 | StatefulSets (Optional) | UPDATE + RENAME + RENUMBER |
| 21 | 12 | Persistent Storage: PV/PVC (Optional) | UPDATE + RENAME + RENUMBER |
| 22 | 17 | Kubernetes Security Deep Dive (Optional) | UPDATE + RENAME + RENUMBER |

#### Removed (Moved to Chapter 51)

| Source # | Title | Destination |
|----------|-------|-------------|
| 21 | Helm Charts for AI Agent Packaging | Ch51 L01 |

### File Operations

#### Files to RENAME

| From | To |
|------|-----|
| 02-setting-up-minikube.md | 02-enabling-kubernetes-docker-desktop.md |
| 02-setting-up-minikube.summary.md | 02-enabling-kubernetes-docker-desktop.summary.md |

#### Files to DELETE from Ch50

| File | Reason |
|------|--------|
| 21-helm-charts-ai-agent-packaging.md | Moved to Ch51 |
| 21-helm-charts-ai-agent-packaging.summary.md | Moved to Ch51 |

#### Files to CREATE in Ch51

| File | Source |
|------|--------|
| 01-introduction-to-helm.md | Adapted from Ch50 L21 |
| 01-introduction-to-helm.summary.md | New |

#### Ch51 Files to RENUMBER

| From | To |
|------|-----|
| 01-advanced-go-templating.md | 02-advanced-go-templating.md |
| 02-named-templates-helpers.md | 03-named-templates-helpers.md |
| 03-values-deep-dive.md | 04-values-deep-dive.md |
| 04-chart-dependencies.md | 05-chart-dependencies.md |
| 05-helm-hooks-lifecycle.md | 06-helm-hooks-lifecycle.md |
| 06-testing-your-charts.md | 07-testing-your-charts.md |
| 07-oci-registries-distribution.md | 08-oci-registries-distribution.md |
| 08-library-charts-standardization.md | 09-library-charts-standardization.md |
| 09-ai-assisted-chart-development.md | 10-ai-assisted-chart-development.md |
| 10-capstone-production-agent-chart.md | 11-capstone-production-agent-chart.md |
| 11-building-helm-chart-skill.md | 12-building-helm-chart-skill.md |

### Minikube → Docker Desktop Replacements

| Minikube Command | Docker Desktop Equivalent |
|------------------|---------------------------|
| `minikube start` | Enable in Docker Desktop Settings → Kubernetes |
| `minikube stop` | Disable in settings (or leave running) |
| `minikube tunnel` | LoadBalancer works natively |
| `minikube dashboard` | `kubectl proxy` + dashboard URL |
| `minikube addons enable ingress` | `kubectl apply -f` ingress-nginx |
| `minikube ssh` | Not needed |
| `minikube docker-env` | Not needed (shares Docker daemon) |

### Key Entities

- **Lesson**: Educational content unit with frontmatter, narrative, exercises
- **Layer**: Teaching progression (L1=Manual, L2=AI-Collaboration, L3=Intelligence, L4=Spec-Driven)
- **Skill**: Reusable intelligence created in L3 lessons
- **Running Example**: Task API container from Chapter 49

## Success Criteria

### Measurable Outcomes

- **SC-001**: Core path reduced from 23 to 15 lessons for faster agent deployment
- **SC-002**: All 22 lessons have complete YAML frontmatter with skills mapping
- **SC-003**: All lessons have 3 "Try With AI" prompts with learning explanations
- **SC-004**: Zero Minikube references remain in chapter
- **SC-005**: Optional lessons clearly marked - students can skip without confusion
- **SC-006**: Chapter 51 properly receives Helm intro as new L01

### Layer Progression

| Phase | Lessons | Layer |
|-------|---------|-------|
| Core Foundation | 1-12 | L1 (Manual) |
| AI Collaboration | 13 | L2 |
| Synthesis | 14 | L4 (Capstone) |
| Intelligence | 15 | L3 (Skill) |
| Optional Advanced | 16-22 | L1 |

## Chapter Structure Summary

### Chapter 50: Kubernetes for AI Services (22 lessons)

**Core Path (Required)**: 15 lessons
- L1-12: Manual foundation with Task API examples
- L13: AI-assisted kubectl-ai collaboration
- L14: Spec-driven capstone deployment
- L15: Kubernetes deployment skill creation

**Advanced Path (Optional)**: 7 lessons
- L16-22: Init containers, sidecars, Ingress, service discovery, StatefulSets, storage, security deep dive

### Chapter 51: Helm Charts (12 lessons)

- L01: Introduction to Helm (NEW - moved from Ch50)
- L02-12: Existing lessons renumbered

## Quality Reference

Match structure and quality of:
- `apps/learn-app/docs/07-AI-Cloud-Native-Development/49-docker-for-ai-services/01-docker-installation-and-setup.md`
