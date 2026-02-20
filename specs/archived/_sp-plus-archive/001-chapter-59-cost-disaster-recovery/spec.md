# Feature Specification: Chapter 59 - Cost & Disaster Recovery

**Feature Branch**: `001-chapter-59-cost-disaster-recovery`
**Created**: 2025-12-30
**Status**: Draft
**Proficiency Level**: B1 (Intermediate)
**Part**: 7 - AI Cloud Native Development (Enterprise Tier)

## Overview

Chapter 59 teaches domain experts to build cost-aware and resilient Kubernetes applications. Students apply FinOps practices for cost visibility and optimization, implement backup/disaster recovery strategies, and validate system resilience through chaos engineering. The chapter uses the Task API as a running example, transforming it into an operationally excellent service.

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Kubernetes fundamentals: Deployments, Services, ConfigMaps, Secrets (Ch50)
- Helm charts for packaging applications (Ch51)
- Resource requests/limits basics (Ch50)
- HPA/KEDA autoscaling concepts (Ch56)
- Prometheus metrics collection (Ch55)
- GitOps with ArgoCD (Ch54)
- Docker Desktop Kubernetes environment

**What this chapter must explain from scratch**:
- FinOps discipline and the Visibility → Optimization → Operation cycle
- VPA (Vertical Pod Autoscaler) for right-sizing recommendations
- OpenCost for cost allocation and visibility
- RTO (Recovery Time Objective) vs RPO (Recovery Point Objective)
- The 3-2-1 backup rule
- Velero for Kubernetes backup/restore
- Chaos engineering principles and Chaos Mesh
- Data sovereignty and compliance considerations

## Skill-First Learning Pattern

**Student Skill**: `operational-excellence`

| Lesson | What Students Learn | Skill Improvement |
|--------|---------------------|-------------------|
| **L00** | Build Your Operational Excellence Skill | **Created from official docs** |
| L01 | Cloud Cost Fundamentals | Add: cost model understanding |
| L02 | Right-Sizing with VPA | Add: VPA patterns, modes |
| L03 | OpenCost Visibility | Add: cost queries, allocation |
| L04 | FinOps Practices | Add: tagging strategy, alerts |
| L05 | Backup Fundamentals | Add: RTO/RPO, 3-2-1 rule |
| L06 | Velero for K8s | Add: backup/restore patterns |
| L07 | Chaos Engineering | Add: PodChaos, game days |
| L08 | Data Sovereignty | Add: compliance patterns |
| **L09** | **Capstone** | **Production-ready skill** |

Every lesson L01+ ends with "Reflect on Your Skill" section where students test and improve their skill.

## User Scenarios & Testing

### User Story 1 - Build Operational Excellence Skill (Priority: P1)

A domain expert who completed Part 6 wants to add cost awareness and resilience to their agent. They start by building an operational-excellence skill that encodes production patterns from official documentation, giving them a knowledge foundation for the chapter.

**Why this priority**: The skill-first pattern ensures students own reusable intelligence before learning concepts. Without this foundation, students would learn patterns but not retain them as sellable assets.

**Independent Test**: Can be tested by invoking the created skill to generate a VPA manifest for a sample deployment.

**Acceptance Scenarios**:

1. **Given** a student has cloned the skills-lab, **When** they follow L00 instructions to build the skill, **Then** they have a working `operational-excellence` skill in `.claude/skills/`
2. **Given** a completed skill, **When** student asks it to generate a Velero backup schedule, **Then** the skill produces valid YAML with correct CRD structure

---

### User Story 2 - Understand Cloud Costs (Priority: P1)

A domain expert deploys their Task API to Kubernetes but receives an unexpectedly high cloud bill. They need to understand what drives costs (compute, storage, network, egress) and how to measure them.

**Why this priority**: Cost visibility is the foundation of FinOps. Without understanding cost drivers, optimization efforts are misdirected.

**Independent Test**: Student can explain the cost components of a Kubernetes workload and identify which resources drive costs for their Task API.

**Acceptance Scenarios**:

1. **Given** a running Task API, **When** student lists cost components, **Then** they correctly identify compute (CPU/memory), storage (PVC), and network (egress) costs
2. **Given** L01 completion, **When** student examines a Kubernetes manifest, **Then** they can estimate relative cost impact of different resource configurations

---

### User Story 3 - Right-Size Resources with VPA (Priority: P2)

A domain expert's Task API is either over-provisioned (wasting money) or under-provisioned (causing OOM kills). They want to use VPA to get data-driven resource recommendations.

**Why this priority**: Right-sizing reduces costs while maintaining performance. VPA provides objective recommendations rather than guesswork.

**Independent Test**: Student can install VPA, apply it to a deployment in "Off" mode, and interpret the recommendations.

**Acceptance Scenarios**:

1. **Given** a Deployment with arbitrary resource requests, **When** VPA is applied in Off mode, **Then** recommendations appear in the VPA status after pod runs for a few minutes
2. **Given** VPA recommendations, **When** student compares to current requests, **Then** they can quantify potential savings or required increases

---

### User Story 4 - Implement Cost Visibility with OpenCost (Priority: P2)

A domain expert manages multiple namespaces (dev, staging, production) and needs to track costs per environment and per team. They implement OpenCost for cost allocation.

**Why this priority**: Showback/chargeback requires cost visibility. OpenCost provides the foundation for FinOps practices.

**Independent Test**: Student can query OpenCost API for cost breakdown by namespace.

**Acceptance Scenarios**:

1. **Given** OpenCost installed with Prometheus, **When** student queries `/allocation` API with `aggregate=namespace`, **Then** they see cost breakdown for each namespace
2. **Given** pods with cost allocation labels (team, app, environment), **When** querying OpenCost, **Then** costs are aggregated by those labels

---

### User Story 5 - Define Backup Strategy (Priority: P1)

A domain expert's Task API stores important task data. They need to define recovery objectives (RTO/RPO) and implement the 3-2-1 backup rule to protect against data loss.

**Why this priority**: Backups are critical for business continuity. Understanding RTO/RPO before implementing backups ensures the solution meets business needs.

**Independent Test**: Student can articulate RTO/RPO requirements for their Task API and explain how their backup strategy achieves them.

**Acceptance Scenarios**:

1. **Given** a business requirement "lose no more than 1 hour of data", **When** student designs backup strategy, **Then** they configure backups at least hourly (1-hour RPO)
2. **Given** the 3-2-1 rule, **When** student explains their strategy, **Then** they identify 3 copies, 2 storage types, 1 offsite location

---

### User Story 6 - Implement Velero Backups (Priority: P2)

A domain expert implements automated backups for their Task API namespace using Velero, including database-aware hooks for consistent snapshots.

**Why this priority**: Velero provides the actual backup capability. Understanding the CRDs and hooks enables production-grade backups.

**Independent Test**: Student can create a Velero Schedule that backs up a namespace daily with 30-day retention.

**Acceptance Scenarios**:

1. **Given** Velero installed with MinIO backend, **When** student creates a Schedule CRD, **Then** backups appear in storage on the defined schedule
2. **Given** a backup exists, **When** student performs a restore to a different namespace, **Then** resources are recreated successfully

---

### User Story 7 - Validate Resilience with Chaos Mesh (Priority: P2)

A domain expert wants to verify their Task API recovers gracefully from failures. They implement chaos experiments to inject pod failures and measure recovery time.

**Why this priority**: Chaos engineering builds confidence in system resilience. Testing failures in controlled environments prevents production surprises.

**Independent Test**: Student can create a PodChaos experiment that kills Task API pods and observe recovery.

**Acceptance Scenarios**:

1. **Given** Chaos Mesh installed, **When** student applies PodChaos to staging Task API, **Then** pods are killed and Kubernetes recreates them
2. **Given** a chaos experiment, **When** student measures recovery time, **Then** they can verify it meets their RTO

---

### User Story 8 - Capstone Integration (Priority: P3)

A domain expert applies all chapter concepts to create a production-ready Task API with cost labels, scheduled backups, and validated resilience through chaos testing.

**Why this priority**: The capstone demonstrates mastery by integrating all concepts into a cohesive operational excellence posture.

**Independent Test**: Complete Task API with cost labels visible in OpenCost, Velero backups running, and passing chaos experiment.

**Acceptance Scenarios**:

1. **Given** completed capstone, **When** inspecting Task API manifests, **Then** all resources have cost allocation labels
2. **Given** completed capstone, **When** checking Velero status, **Then** daily backups are scheduled and last backup succeeded
3. **Given** completed capstone, **When** running chaos experiment, **Then** Task API recovers within defined RTO

---

### Edge Cases

- What happens when VPA recommendations exceed node capacity?
- How does Velero handle backups during high cluster load?
- What if MinIO storage is unavailable when backup runs?
- How to handle chaos experiments that cause cascading failures?
- What happens when VPA is enabled alongside HPA on the same metrics?

## Requirements

### Functional Requirements

**Skill-First Pattern**:
- **FR-001**: L00 MUST guide students to build an `operational-excellence` skill using `/fetching-library-docs` and `/skill-creator`
- **FR-002**: Every lesson L01-L08 MUST end with a "Reflect on Your Skill" section
- **FR-003**: L09 (Capstone) MUST have students finalize their skill as a production-ready asset

**Cost Management**:
- **FR-004**: Chapter MUST explain cloud cost components (compute, storage, network, egress)
- **FR-005**: Chapter MUST teach VPA installation, configuration, and interpretation of recommendations
- **FR-006**: Chapter MUST teach OpenCost installation and cost allocation queries
- **FR-007**: Chapter MUST cover FinOps practices: tagging strategy, showback before chargeback

**Disaster Recovery**:
- **FR-008**: Chapter MUST explain RTO vs RPO concepts with practical examples
- **FR-009**: Chapter MUST teach the 3-2-1 backup rule
- **FR-010**: Chapter MUST cover Velero installation, Schedule CRD, and backup hooks
- **FR-011**: Chapter MUST demonstrate restore procedures

**Chaos Engineering**:
- **FR-012**: Chapter MUST explain chaos engineering principles ("break things on purpose")
- **FR-013**: Chapter MUST teach Chaos Mesh installation and PodChaos experiments
- **FR-014**: Chapter MUST cover Game Day patterns for structured resilience testing
- **FR-015**: Chapter MUST emphasize safety: staging before production, namespace filtering

**Compliance**:
- **FR-016**: Chapter MUST introduce data sovereignty and GDPR considerations
- **FR-017**: Chapter MUST cover audit trails for compliance

**Running Example**:
- **FR-018**: All lessons MUST use Task API as the running example
- **FR-019**: Capstone MUST produce a cost-aware, resilient Task API

### Key Entities

- **VPA (VerticalPodAutoscaler)**: CRD that analyzes pod resource usage and recommends optimal requests/limits
- **OpenCost**: CNCF cost visibility tool that integrates with Prometheus for cost allocation
- **Velero Backup**: Snapshot of Kubernetes resources and optional volume data
- **Velero Schedule**: Cron-based automated backup configuration
- **Velero Restore**: Process of recreating resources from a backup
- **PodChaos**: Chaos Mesh CRD for injecting pod failures
- **Cost Allocation Labels**: Kubernetes labels used to attribute costs (team, app, environment, cost-center)

## Lesson Structure

| # | Title | Layer | Duration | Focus |
|---|-------|-------|----------|-------|
| 0 | Build Your Operational Excellence Skill | L3 | 15 min | Create skill from official docs |
| 1 | Cloud Cost Fundamentals | L1 | 20 min | Compute, storage, network, egress costs |
| 2 | Right-Sizing with VPA | L1 | 25 min | VPA modes, recommendations, VPA+HPA coexistence |
| 3 | OpenCost/Kubecost Visibility | L1 | 25 min | Installation, cost allocation, showback |
| 4 | FinOps Practices & Budget Alerts | L1 | 20 min | Tagging strategy, cost centers, alerts |
| 5 | Backup Fundamentals | L1 | 20 min | RTO vs RPO, 3-2-1 rule, backup strategies |
| 6 | Velero for K8s Backup/Restore | L1→L2 | 30 min | Schedules, hooks, disaster recovery |
| 7 | Chaos Engineering Basics | L1→L2 | 30 min | Chaos Mesh, PodChaos, Game Days |
| 8 | Data Sovereignty & Compliance | L1 | 20 min | GDPR, data residency, audit trails |
| 9 | Capstone - Resilient, Cost-Aware Task API | L4 | 40 min | Full integration with spec-driven approach |

**Total Duration**: ~245 minutes (~4 hours)

## 4-Layer Teaching Progression

- **L00 (Layer 3)**: Students build skill first using `/fetching-library-docs` and `/skill-creator` - establishing reusable intelligence
- **L01-L04 (Layer 1)**: Manual learning of cost concepts - build vocabulary before AI collaboration
- **L05-L08 (Layer 1→L2)**: DR and chaos engineering with gradual AI collaboration
- **L09 (Layer 4)**: Capstone integrates all concepts with spec-driven approach

## Technology Choices

| Purpose | Technology | Rationale |
|---------|------------|-----------|
| Cost Visibility | OpenCost | CNCF Incubating, vendor-neutral, Prometheus integration |
| Right-Sizing | VPA | Official Kubernetes autoscaler, production-proven |
| Backup/Restore | Velero | CNCF project, de facto K8s backup standard |
| Chaos Engineering | Chaos Mesh | CNCF Incubating, Kubernetes-native |
| Local Object Storage | MinIO | S3-compatible, works with Docker Desktop |

## NOT in Chapter 59 (Covered Elsewhere)

- HPA/KEDA autoscaling (Ch56 - Traffic Engineering)
- Resource requests/limits basics (Ch50 - Kubernetes Fundamentals)
- Prometheus/Grafana observability (Ch55 - Observability)
- Alerting with AlertManager (Ch55 - Observability)

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students can build an operational-excellence skill that generates valid VPA and Velero manifests
- **SC-002**: Students can explain the FinOps cycle (Visibility → Optimization → Operation) and apply it to their Task API
- **SC-003**: Students can interpret VPA recommendations and calculate potential cost savings
- **SC-004**: Students can query OpenCost to break down costs by namespace and label
- **SC-005**: Students can define RTO/RPO requirements for a given business scenario
- **SC-006**: Students can create a Velero Schedule with appropriate retention and hooks
- **SC-007**: Students can execute a chaos experiment and measure recovery time
- **SC-008**: Students can articulate data sovereignty implications for multi-region deployments
- **SC-009**: Capstone produces a Task API with cost labels, backup schedule, and passing chaos test
- **SC-010**: Students demonstrate skill improvement through 9 "Reflect on Your Skill" iterations

## Assumptions

- Students have Docker Desktop Kubernetes enabled (Ch49-50 prerequisite)
- Students have Prometheus installed (Ch55 prerequisite)
- Students have Task API from Part 6 available for the running example
- MinIO is used as S3-compatible storage for Velero (works locally)
- Chaos experiments run in staging namespace to avoid production impact
- OpenCost is taught conceptually for cloud costs; actual cost data may differ in local environment

## Dependencies

- **Ch50**: Kubernetes fundamentals (Deployments, Services, resource requests/limits)
- **Ch51**: Helm charts (for installing VPA, OpenCost, Velero, Chaos Mesh)
- **Ch55**: Prometheus (OpenCost requires Prometheus for metrics)
- **Ch56**: HPA/KEDA (understanding when VPA vs HPA applies)
- **Part 6**: Task API as running example

## Out of Scope

- Cloud provider-specific cost APIs (focus on Kubernetes-native tools)
- Multi-cluster disaster recovery (single cluster focus for B1 level)
- Advanced chaos experiments (IOChaos, DNSChaos - mention but don't deep-dive)
- Compliance certifications (SOC2, ISO27001 - conceptual only)
- Real cloud billing integration (conceptual understanding with local simulation)
