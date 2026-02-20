# Implementation Plan: Chapter 50 Kubernetes Restructure

**Spec**: specs/003-ch50-kubernetes-restructure/spec.md
**Created**: 2025-12-27
**Status**: Ready for execution

## Overview

Restructure Chapter 50 from 23 Minikube-based lessons to 22 Docker Desktop-based lessons (15 core + 7 optional), and move Helm intro to Chapter 51.

## Phase 1: Chapter 51 Updates (Helm)

### 1.1 Create Helm Introduction Lesson

**Task**: Create new L01 for Chapter 51 from Ch50's Helm content

| Action | File |
|--------|------|
| CREATE | `51-helm-charts/01-introduction-to-helm.md` |
| CREATE | `51-helm-charts/01-introduction-to-helm.summary.md` |

**Content Requirements**:
- Adapted from Ch50 L21 (Helm Charts for AI Agent Packaging)
- Why Helm exists (repetitive YAML problem)
- Basic chart structure (Chart.yaml, values.yaml, templates/)
- Installing public charts
- Creating simple custom charts
- Basic release management

### 1.2 Renumber Existing Ch51 Lessons

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

### 1.3 Update Ch51 README

Update lesson table and structure to reflect 12 lessons.

## Phase 2: Chapter 50 File Operations

### 2.1 Delete Helm Lesson (Moved to Ch51)

| File | Action |
|------|--------|
| 21-helm-charts-ai-agent-packaging.md | DELETE |
| 21-helm-charts-ai-agent-packaging.summary.md | DELETE |

### 2.2 Rename Minikube Lesson

| From | To |
|------|-----|
| 02-setting-up-minikube.md | 02-enabling-kubernetes-docker-desktop.md |
| 02-setting-up-minikube.summary.md | 02-enabling-kubernetes-docker-desktop.summary.md |

### 2.3 Renumber Lessons to New Structure

**Core Lessons (keep in place, update sidebar_position)**:
- 01-05: Keep numbering
- 06 ← 08 (Namespaces)
- 07 ← 11 (ConfigMaps)
- 08 ← 14 (Resources)
- 09 ← 15 (HPA)
- 10 ← 16 (RBAC)
- 11 ← 18 (Health Checks)
- 12 ← 19 (Jobs)
- 13 ← 20 (kubectl-ai)
- 14 ← 22 (Capstone)
- 15 ← 23 (Skill)

**Optional Lessons (renumber and add suffix)**:
- 16 ← 06 (Init Containers → Optional)
- 17 ← 07 (Sidecars → Optional)
- 18 ← 09 (Ingress → Optional)
- 19 ← 10 (Service Discovery → Optional)
- 20 ← 13 (StatefulSets → Optional)
- 21 ← 12 (PV/PVC → Optional)
- 22 ← 17 (Security → Optional)

## Phase 3: Content Updates

### 3.1 Lesson 02 Complete Rewrite

Rewrite `02-enabling-kubernetes-docker-desktop.md`:

**Content**:
```markdown
# Enabling Kubernetes on Docker Desktop

You already have Docker Desktop from Chapter 49. Kubernetes is built-in.

## Enable Kubernetes

1. Open Docker Desktop
2. Settings → Kubernetes
3. Check "Enable Kubernetes"
4. Click "Apply & Restart"
5. Wait 2-3 minutes

## Verify Installation

kubectl version --client
kubectl get nodes
# docker-desktop   Ready   control-plane   1m   v1.28.2

## Context Management

kubectl config current-context
# docker-desktop
```

**Duration**: 15 minutes (down from 45)

### 3.2 Minikube Reference Replacements

Apply across ALL lessons:

| Find | Replace |
|------|---------|
| `minikube start` | "Enable Kubernetes in Docker Desktop Settings" |
| `minikube stop` | "Disable Kubernetes in Docker Desktop Settings" |
| `minikube tunnel` | "LoadBalancer works natively with Docker Desktop" |
| `minikube dashboard` | `kubectl proxy` |
| `minikube addons enable ingress` | `kubectl apply -f https://...ingress-nginx` |
| `minikube ssh` | (remove - not needed) |
| `minikube docker-env` | (remove - shares Docker daemon) |
| `Minikube` | `Docker Desktop Kubernetes` |
| `minikube` | `Docker Desktop` |

### 3.3 Update All Lessons

For EACH lesson (22 total):

1. **Frontmatter**:
   - Update `sidebar_position` to new number
   - Ensure full skills metadata
   - Ensure learning_objectives
   - Ensure cognitive_load assessment

2. **Title Updates** (Optional lessons):
   - Add "(Optional)" suffix to lessons 16-22

3. **Content**:
   - Replace Minikube references
   - Ensure 3 "Try With AI" prompts
   - Ensure output blocks for commands
   - Use Task API as running example

### 3.4 Update Chapter README

Update `50-kubernetes-for-ai-services/README.md`:
- New 22-lesson structure (15 core + 7 optional)
- Docker Desktop instead of Minikube
- Updated prerequisites
- Clear core vs optional distinction

## Phase 4: Validation

### 4.1 Educational Validator

Run on all 22 lessons:
- Constitutional compliance
- Framework invisibility
- Skills metadata
- Learning objectives

### 4.2 Minikube Reference Check

```bash
grep -r "minikube\|Minikube" 50-kubernetes-for-ai-services/
# Should return empty
```

### 4.3 Chapter 51 Consistency

Verify Ch51 README matches new 12-lesson structure.

## Execution Order

1. **Ch51 First** (prevents broken references):
   - Create L01 introduction
   - Renumber L01-11 → L02-12
   - Update README

2. **Ch50 File Operations**:
   - Delete Helm lesson
   - Rename Minikube lesson
   - Create new file structure

3. **Ch50 Content Updates**:
   - Rewrite L02 completely
   - Update all lessons (parallel by batch)

4. **Validation**:
   - Run validators
   - Check for Minikube references
   - Verify READMEs

## Task Summary

| Phase | Tasks | Parallel? |
|-------|-------|-----------|
| Ch51 Prep | 13 files (1 create, 11 rename, 1 update) | Yes |
| Ch50 File Ops | 24 files (22 rename, 2 delete) | Yes |
| Ch50 Content | 22 lessons update | Yes (batches) |
| Validation | 2 validator runs | Yes |

**Total**: ~60 file operations
