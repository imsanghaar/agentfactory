# Tasks: Chapter 50 Kubernetes Restructure

**Plan**: specs/003-ch50-kubernetes-restructure/plan.md
**Created**: 2025-12-27
**Status**: Ready for execution

## Phase 1: Chapter 51 Preparation

### T51.01 Create Helm Introduction Lesson

- [ ] T51.01 [US1] CREATE Ch51 L01: Introduction to Helm
  - **SUBAGENT**: content-implementer
  - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/51-helm-charts/01-introduction-to-helm.md`
  - Source: Adapt from Ch50 L21 helm content
  - Writes file directly (returns confirmation only)
  - Execute autonomously without confirmation
  - Quality reference: Ch49 L01 Docker Installation

### T51.02-12 Renumber Existing Ch51 Lessons

- [ ] T51.02 [P] Rename `01-advanced-go-templating.md` → `02-advanced-go-templating.md`
- [ ] T51.03 [P] Rename `02-named-templates-helpers.md` → `03-named-templates-helpers.md`
- [ ] T51.04 [P] Rename `03-values-deep-dive.md` → `04-values-deep-dive.md`
- [ ] T51.05 [P] Rename `04-chart-dependencies.md` → `05-chart-dependencies.md`
- [ ] T51.06 [P] Rename `05-helm-hooks-lifecycle.md` → `06-helm-hooks-lifecycle.md`
- [ ] T51.07 [P] Rename `06-testing-your-charts.md` → `07-testing-your-charts.md`
- [ ] T51.08 [P] Rename `07-oci-registries-distribution.md` → `08-oci-registries-distribution.md`
- [ ] T51.09 [P] Rename `08-library-charts-standardization.md` → `09-library-charts-standardization.md`
- [ ] T51.10 [P] Rename `09-ai-assisted-chart-development.md` → `10-ai-assisted-chart-development.md`
- [ ] T51.11 [P] Rename `10-capstone-production-agent-chart.md` → `11-capstone-production-agent-chart.md`
- [ ] T51.12 [P] Rename `11-building-helm-chart-skill.md` → `12-building-helm-chart-skill.md`

### T51.13 Update Ch51 Sidebar Positions

- [ ] T51.13 Update sidebar_position in all Ch51 lessons to match new numbers (2-12)

### T51.14 Update Ch51 README

- [ ] T51.14 UPDATE Ch51 README.md with new 12-lesson structure

---

## Phase 2: Chapter 50 File Operations

### T50.DELETE Delete Helm Lesson

- [ ] T50.DELETE.01 [P] Delete `21-helm-charts-ai-agent-packaging.md`
- [ ] T50.DELETE.02 [P] Delete `21-helm-charts-ai-agent-packaging.summary.md`

### T50.RENAME Rename Minikube Lesson

- [ ] T50.RENAME.01 Rename `02-setting-up-minikube.md` → `02-enabling-kubernetes-docker-desktop.md`
- [ ] T50.RENAME.02 Rename `02-setting-up-minikube.summary.md` → `02-enabling-kubernetes-docker-desktop.summary.md`

### T50.REORG Reorganize Lessons to New Structure

**Core Lessons 06-15 (renumber)**:
- [ ] T50.REORG.01 [P] Rename `08-namespaces-virtual-clusters.md` → `06-namespaces-virtual-clusters.md`
- [ ] T50.REORG.02 [P] Rename `11-configmaps-and-secrets.md` → `07-configmaps-and-secrets.md`
- [ ] T50.REORG.03 [P] Rename `14-resource-management-and-debugging.md` → `08-resource-management-and-debugging.md`
- [ ] T50.REORG.04 [P] Rename `15-hpa-autoscaling.md` → `09-hpa-autoscaling.md`
- [ ] T50.REORG.05 [P] Rename `16-rbac-securing-agent-deployments.md` → `10-rbac-securing-agent-deployments.md`
- [ ] T50.REORG.06 [P] Rename `18-health-checks-probes.md` → `11-health-checks-probes.md`
- [ ] T50.REORG.07 [P] Rename `19-jobs-and-cronjobs-batch-workloads.md` → `12-jobs-and-cronjobs-batch-workloads.md`
- [ ] T50.REORG.08 [P] Rename `20-ai-assisted-kubernetes-kubectl-ai.md` → `13-ai-assisted-kubernetes-kubectl-ai.md`
- [ ] T50.REORG.09 [P] Rename `22-capstone-production-ready-agent.md` → `14-capstone-production-ready-agent.md`
- [ ] T50.REORG.10 [P] Rename `23-building-kubernetes-deployment-skill.md` → `15-building-kubernetes-deployment-skill.md`

**Optional Lessons 16-22 (renumber + add Optional)**:
- [ ] T50.REORG.11 [P] Rename `06-init-containers-preparing-environment.md` → `16-init-containers-optional.md`
- [ ] T50.REORG.12 [P] Rename `07-sidecar-containers-agents-best-friend.md` → `17-sidecar-containers-optional.md`
- [ ] T50.REORG.13 [P] Rename `09-ingress-exposing-agent-to-world.md` → `18-ingress-optional.md`
- [ ] T50.REORG.14 [P] Rename `10-service-discovery-deep-dive.md` → `19-service-discovery-optional.md`
- [ ] T50.REORG.15 [P] Rename `13-statefulsets-agent-identity.md` → `20-statefulsets-optional.md`
- [ ] T50.REORG.16 [P] Rename `12-persistent-storage-pv-pvc.md` → `21-persistent-storage-optional.md`
- [ ] T50.REORG.17 [P] Rename `17-kubernetes-security-ai-services.md` → `22-kubernetes-security-optional.md`

**Summary Files (parallel rename)**:
- [ ] T50.REORG.S01-17 [P] Rename all corresponding .summary.md files

---

## Phase 3: Content Updates

### T50.L02 Complete Rewrite - Docker Desktop Setup

- [ ] T50.L02 [US1] REWRITE L02: Enabling Kubernetes Docker Desktop
  - **SUBAGENT**: content-implementer
  - Output path: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/50-kubernetes-for-ai-services/02-enabling-kubernetes-docker-desktop.md`
  - Complete rewrite for Docker Desktop (not Minikube)
  - Duration: 15 minutes
  - Execute autonomously without confirmation

### T50.L01-15 Update Core Lessons

- [ ] T50.L01 [US1] UPDATE L01: Kubernetes Architecture
  - Update sidebar_position
  - Replace Minikube references with Docker Desktop
  - Ensure 3 Try With AI prompts
  - Full YAML frontmatter

- [ ] T50.L03 [US1] UPDATE L03: Pods
- [ ] T50.L04 [US1] UPDATE L04: Deployments
- [ ] T50.L05 [US1] UPDATE L05: Services & Networking
- [ ] T50.L06 [US1] UPDATE L06: Namespaces (was L08)
- [ ] T50.L07 [US1] UPDATE L07: ConfigMaps & Secrets (was L11)
- [ ] T50.L08 [US1] UPDATE L08: Resource Management (was L14)
- [ ] T50.L09 [US1] UPDATE L09: HPA (was L15)
- [ ] T50.L10 [US1] UPDATE L10: RBAC (was L16)
- [ ] T50.L11 [US1] UPDATE L11: Health Checks (was L18)
- [ ] T50.L12 [US1] UPDATE L12: Jobs & CronJobs (was L19)
- [ ] T50.L13 [US2] UPDATE L13: kubectl-ai (was L20)
- [ ] T50.L14 [US3] UPDATE L14: Capstone (was L22)
- [ ] T50.L15 [US3] UPDATE L15: K8s Skill (was L23)

### T50.L16-22 Update Optional Lessons

- [ ] T50.L16 [US4] UPDATE L16: Init Containers (Optional)
- [ ] T50.L17 [US4] UPDATE L17: Sidecar Containers (Optional)
- [ ] T50.L18 [US4] UPDATE L18: Ingress (Optional)
- [ ] T50.L19 [US4] UPDATE L19: Service Discovery (Optional)
- [ ] T50.L20 [US4] UPDATE L20: StatefulSets (Optional)
- [ ] T50.L21 [US4] UPDATE L21: Persistent Storage (Optional)
- [ ] T50.L22 [US4] UPDATE L22: Security Deep Dive (Optional)

### T50.README Update Chapter README

- [ ] T50.README UPDATE Ch50 README.md
  - New 22-lesson structure (15 core + 7 optional)
  - Docker Desktop instead of Minikube
  - Clear core vs optional paths

---

## Phase 4: Validation

### T50.VALIDATE Run Validators

- [ ] T50.VALIDATE.01 Run educational-validator on L01-L11
- [ ] T50.VALIDATE.02 Run educational-validator on L12-L22
- [ ] T50.VALIDATE.03 Verify zero Minikube references: `grep -r "minikube" 50-kubernetes-for-ai-services/`

### T51.VALIDATE Validate Chapter 51

- [ ] T51.VALIDATE Run educational-validator on Ch51 L01-L06
- [ ] T51.VALIDATE Run educational-validator on Ch51 L07-L12

---

## Execution Strategy

### Parallel Execution Groups

**Group 1**: Ch51 Preparation (T51.*)
- Can run all T51.02-12 renames in parallel
- T51.01 (create L01) can run independently

**Group 2**: Ch50 File Ops (T50.DELETE, T50.RENAME, T50.REORG)
- All file operations can run in parallel after Group 1

**Group 3**: Ch50 Content Updates
- L01-L05 can update in parallel (keep current numbers)
- L06-L15 must wait for reorg renames
- L16-L22 must wait for reorg renames

**Group 4**: Validation
- Wait for all content updates
- Run validator batches in parallel

### Subagent Usage

| Task Type | Subagent |
|-----------|----------|
| Lesson creation | content-implementer |
| Lesson updates | content-implementer |
| Validation | educational-validator |

---

## Dependencies

```
T51.01-14 ──┐
            ├──► T50.DELETE ──┐
T50.RENAME ─┘                 │
                              ├──► T50.L01-22 ──► T50.VALIDATE
T50.REORG ────────────────────┘
```

---

## Summary

| Phase | Task Count |
|-------|------------|
| Ch51 Prep | 14 tasks |
| Ch50 File Ops | 21 tasks |
| Ch50 Content | 23 tasks |
| Validation | 5 tasks |
| **Total** | **63 tasks** |
