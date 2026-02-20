---
sidebar_position: 6
title: "Part 6: AI Cloud Native Development"
---

# Part 6: AI Cloud Native Development

Part 7 takes the agent you built in Part 6 and turns it into a production cloud service. You'll containerize the stack, orchestrate it on Kubernetes, automate delivery, and operate it with observability, security, and cost controls. The goal: a reliable Digital FTE that runs 24/7 for real users.

**Prerequisites**: Parts 4-6. You need a working agent service to deploy.

---

## Goals

By completing Part 7, you will:

- **Containerize agent services** with production Dockerfiles and image optimization
- **Orchestrate at scale** using Kubernetes deployments, services, and Helm charts
- **Adopt event-driven patterns** through Kafka-based messaging
- **Leverage Dapr** for service invocation, state, pub/sub, and workflows
- **Automate delivery** with CI/CD pipelines and GitOps via ArgoCD
- **Operate with excellence** through observability, security, governance, and cost management

---

## Chapter Progression

Seven stages build deployment capability step-by-step:

- **Containerization & Orchestration (49-51)**: Docker fundamentals → Kubernetes deployments → Helm packaging.
- **Event-Driven Architecture (52)**: Kafka for asynchronous agent communication.
- **Dapr Core (53)**: Sidecar patterns for state, pub/sub, and secrets.
- **Automation (54)**: GitHub Actions plus ArgoCD for repeatable releases.
- **Operations Excellence (55-58)**: Observability, API gateways, security, and infrastructure-as-code for cloud clusters.
- **Advanced Dapr (59)**: Actors and workflows for long-running, stateful agents.
- **Real Cloud Deployment (60)**: Apply everything on a managed cloud environment.

**Why this order?** Containerization precedes orchestration; orchestration precedes automation; automation precedes operations; advanced patterns come after the foundations are stable.

---

## Outcome & Method

You finish with a sellable Digital FTE: containerized, deployed to Kubernetes, scalable, observable, secure, and cost-aware. The same spec-driven approach continues—write infrastructure specs, let AI draft manifests/pipelines, and validate against requirements.
