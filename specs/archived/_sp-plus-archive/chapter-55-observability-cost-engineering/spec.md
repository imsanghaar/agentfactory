# Chapter Specification: Chapter 55 - Observability & Cost Engineering

**Chapter Location**: `apps/learn-app/docs/07-AI-Cloud-Native-Development/55-observability-cost-engineering/`
**Created**: 2025-12-29
**Status**: Draft
**Proficiency Level**: B1 (Intermediate)
**Part**: 7 - AI Cloud Native Development (Tier 2: Enterprise)

## Chapter Overview

This chapter teaches students to implement production-grade observability and cost engineering for cloud-native AI applications. Students will learn the three pillars of observability (metrics, tracing, logging), SRE foundations (SLIs/SLOs/error budgets), and FinOps practices for Kubernetes cost optimization. The chapter applies these concepts to the running Task API example, culminating in a complete observability stack.

### Learning Outcomes

By the end of this chapter, students will be able to:
1. Implement metrics collection with Prometheus and visualize with Grafana dashboards
2. Instrument applications with OpenTelemetry and trace requests through Jaeger
3. Configure centralized logging with Loki and query logs with LogQL
4. Define and measure SLIs, SLOs, and error budgets for their services
5. Set up cost monitoring with OpenCost and implement FinOps practices
6. Integrate Dapr observability features (metrics and tracing)
7. Build a complete observability stack for production AI applications

## Assumed Knowledge

**What students know BEFORE this chapter**:
- Docker containerization and image building (Ch49)
- Kubernetes core concepts: Pods, Deployments, Services, ConfigMaps (Ch50)
- Helm charts for packaging and deploying applications (Ch51)
- Event-driven patterns with Kafka (Ch52)
- Dapr sidecar pattern and building blocks (Ch53)
- GitOps workflows with ArgoCD (Ch54)
- Dapr Actors and Workflows (Ch57)
- Python/FastAPI application development (Part 6)

**What this chapter must explain from scratch**:
- The three pillars of observability (metrics, traces, logs)
- Prometheus architecture and PromQL query language
- OpenTelemetry instrumentation concepts
- SLI/SLO/SLA definitions and error budget calculations
- FinOps principles and cost allocation strategies
- Multi-burn-rate alerting patterns

## DACA Source Material Mapping

| Lesson | DACA Source Files |
|--------|-------------------|
| L02 | `05_Observability/Install-Prometheus-Grafana.md` |
| L03 | `05_Observability/Install-Prometheus-Grafana.md` (Grafana sections) |
| L04 | `05_Observability/Enable-Dapr-Metrics-and-Tracing.md` (tracing sections) |
| L05 | `05_Observability/Centralized-Logging-with-Loki-or-EFK.md` |
| L06 | `06_Load_Testing_and_Capacity_Planning/Define-SLOs-and-SLAs.md` |
| L08 | `06_Load_Testing_and_Capacity_Planning/Resource-Sizing-Guidelines.md`, `03_Advanced_Autoscaling_and_Cost_Optimization/Use-of-Spot-Instances.md` |
| L09 | `05_Observability/Enable-Dapr-Metrics-and-Tracing.md` |

## Skill-First Pattern

**Student Skill**: `observability-cost-engineer`
**Expertise Skill (Claude)**: `.claude/skills/building-with-observability/SKILL.md`

### L00 Structure
Students create their `observability-cost-engineer` skill by:
1. Cloning the skills-lab repository
2. Writing a LEARNING-SPEC.md defining what they want to learn
3. Using `/fetching-library-docs` to fetch Prometheus, OpenTelemetry, and Loki documentation
4. Using `/skill-creator` to build the initial skill
5. Testing the skill with a simple metrics query

### Skill Progression by Lesson

| Lesson | Skill Additions |
|--------|-----------------|
| L01 | Observability concepts vocabulary |
| L02 | Prometheus patterns, PromQL queries |
| L03 | Grafana dashboard JSON, alerting rules |
| L04 | OpenTelemetry instrumentation, span creation |
| L05 | LogQL queries, log aggregation patterns |
| L06 | SLI/SLO definitions, error budget calculations |
| L07 | Multi-burn-rate alerting, incident runbooks |
| L08 | OpenCost queries, cost allocation labels |
| L09 | Dapr observability configuration |
| L10 | Complete stack integration patterns |

---

## User Scenarios & Testing

### User Story 1 - Learn Observability Fundamentals (Priority: P1)

A developer new to observability needs to understand what metrics, traces, and logs are, when to use each, and how they work together to provide system visibility.

**Why this priority**: Foundation concepts required before any hands-on implementation.

**Independent Test**: Student can explain the three pillars and correctly identify which pillar addresses a given debugging scenario.

**Acceptance Scenarios**:

1. **Given** a student with no observability background, **When** they complete L01-L05, **Then** they can explain each pillar's purpose and identify appropriate tools
2. **Given** a slow API response scenario, **When** asked how to investigate, **Then** student correctly identifies tracing as the primary tool

---

### User Story 2 - Implement Metrics and Dashboards (Priority: P1)

A developer needs to add Prometheus metrics to their FastAPI application and create Grafana dashboards to visualize service health.

**Why this priority**: Metrics are the most fundamental observability signal; dashboards make data actionable.

**Independent Test**: Student can deploy Prometheus stack and see their application metrics in Grafana.

**Acceptance Scenarios**:

1. **Given** a running Task API, **When** student adds Prometheus instrumentation, **Then** `/metrics` endpoint returns valid Prometheus format
2. **Given** Prometheus scraping the app, **When** student creates a Grafana dashboard, **Then** request rate and error rate graphs display correctly

---

### User Story 3 - Trace Requests Across Services (Priority: P1)

A developer needs to trace requests through their distributed system to identify performance bottlenecks and debug cross-service issues.

**Why this priority**: Tracing is essential for debugging microservices and AI agent workflows.

**Independent Test**: Student can view a complete trace from HTTP request through Dapr sidecar to database.

**Acceptance Scenarios**:

1. **Given** Task API with OpenTelemetry instrumentation, **When** a request is made, **Then** trace appears in Jaeger UI with all spans
2. **Given** a slow request, **When** student examines the trace, **Then** they can identify which span took the longest

---

### User Story 4 - Set Up Centralized Logging (Priority: P2)

A developer needs to aggregate logs from all pods and query them efficiently to debug issues.

**Why this priority**: Logging provides event-level detail complementing metrics and traces.

**Independent Test**: Student can query Loki for error logs from a specific namespace.

**Acceptance Scenarios**:

1. **Given** Loki stack deployed, **When** application logs an error, **Then** log appears in Grafana Explore with correct labels
2. **Given** multiple pods running, **When** student queries `{namespace="default"} |= "error"`, **Then** results include logs from all pods

---

### User Story 5 - Define and Track SLOs (Priority: P2)

A developer needs to define service level objectives for their API and track error budget consumption.

**Why this priority**: SLOs enable data-driven reliability decisions and balance reliability vs feature velocity.

**Independent Test**: Student can view SLO compliance percentage and remaining error budget in Grafana.

**Acceptance Scenarios**:

1. **Given** a defined 99.9% availability SLO, **When** errors occur, **Then** dashboard shows error budget consumption rate
2. **Given** error budget burn rate > 14.4x, **When** alert fires, **Then** on-call receives notification

---

### User Story 6 - Monitor and Optimize Costs (Priority: P2)

A developer needs to understand their Kubernetes cluster costs and identify optimization opportunities.

**Why this priority**: Cost visibility enables sustainable cloud-native development.

**Independent Test**: Student can view cost breakdown by namespace and identify the most expensive workloads.

**Acceptance Scenarios**:

1. **Given** OpenCost deployed, **When** student queries cost by namespace, **Then** they see accurate cost allocation
2. **Given** cost data, **When** student identifies over-provisioned resources, **Then** they can recommend right-sizing changes

---

### Edge Cases

- What happens when Prometheus storage fills up? (Lesson 02 covers retention configuration)
- How does system handle partial trace collection due to sampling? (Lesson 04 covers sampling strategies)
- What happens when error budget is exhausted? (Lesson 06 covers error budget policies)
- How to handle noisy alerts that cause alert fatigue? (Lesson 07 covers alert hygiene)
- What if cost data is incomplete for on-prem clusters? (Lesson 08 covers custom pricing)

---

## Requirements

### Functional Requirements

#### Observability Stack
- **FR-001**: Chapter MUST teach installation of kube-prometheus-stack via Helm
- **FR-002**: Chapter MUST teach PromQL fundamentals (selectors, aggregations, histograms)
- **FR-003**: Chapter MUST teach Grafana dashboard creation (JSON model, variables, panels)
- **FR-004**: Chapter MUST teach OpenTelemetry Python SDK instrumentation for FastAPI
- **FR-005**: Chapter MUST teach Jaeger deployment and trace visualization
- **FR-006**: Chapter MUST teach Loki stack deployment and LogQL queries

#### SRE Foundations
- **FR-007**: Chapter MUST explain SLI/SLO/SLA relationships with concrete examples
- **FR-008**: Chapter MUST teach error budget calculation and burn rate alerting
- **FR-009**: Chapter MUST teach multi-window, multi-burn-rate alerting (Google SRE pattern)
- **FR-010**: Chapter MUST cover incident response basics and runbook structure

#### Cost Engineering
- **FR-011**: Chapter MUST teach OpenCost deployment and cost allocation queries
- **FR-012**: Chapter MUST teach resource tagging for cost allocation by team/product
- **FR-013**: Chapter MUST cover right-sizing recommendations and waste detection
- **FR-014**: Chapter MUST introduce FinOps principles (rate vs usage optimization)

#### Dapr Integration
- **FR-015**: Chapter MUST teach Dapr metrics configuration and ServiceMonitor setup
- **FR-016**: Chapter MUST teach Dapr tracing configuration with OpenTelemetry Collector
- **FR-017**: Chapter MUST cover observability patterns for Dapr Actors and Workflows

#### Skill-First Pattern
- **FR-018**: L00 MUST guide students to create `observability-cost-engineer` skill
- **FR-019**: Every lesson L01+ MUST end with "Reflect on Your Skill" section
- **FR-020**: Capstone MUST integrate all observability components into Task API

### Key Entities

- **Metric**: Time-series numerical data with labels (name, value, timestamp, labels)
- **Trace**: Distributed request path with spans (trace_id, span_id, parent_span_id, operation, duration)
- **Log**: Event record with structured data (timestamp, level, message, labels)
- **SLO**: Service Level Objective (target, window, indicator type)
- **Error Budget**: Allowed failure rate derived from SLO (budget = 100% - SLO target)
- **Alert Rule**: Condition-based notification trigger (expr, for, labels, annotations)

---

## Success Criteria

### Measurable Outcomes

- **SC-001**: Students can install the complete observability stack (Prometheus, Grafana, Loki, Jaeger) in under 30 minutes
- **SC-002**: Students can instrument a FastAPI application with OpenTelemetry and see traces in Jaeger within 15 minutes
- **SC-003**: Students can write PromQL queries for the 4 golden signals (latency, traffic, errors, saturation)
- **SC-004**: Students can define an SLO and create a multi-burn-rate alert rule for their service
- **SC-005**: Students can identify the top 3 cost drivers in their Kubernetes namespace using OpenCost
- **SC-006**: Students can create a dashboard showing SLO compliance and error budget remaining
- **SC-007**: 90% of students complete the capstone with a working observability stack for Task API
- **SC-008**: Students can explain when to use metrics vs traces vs logs for debugging scenarios

---

## Lesson Structure

### L00: Build Your Observability Skill (25 min)
**Layer**: L3 (Skill Building)
**Proficiency**: B1

Students create their `observability-cost-engineer` skill as the foundation for the chapter.

**Contents**:
- Clone skills-lab repository
- Write LEARNING-SPEC.md for observability
- Fetch official docs via `/fetching-library-docs`
- Create initial skill with `/skill-creator`
- Test skill with basic metrics prompt

---

### L01: Three Pillars of Observability (20 min)
**Layer**: L1 (Manual/Conceptual)
**Proficiency**: B1
**DACA Source**: (New content - conceptual foundation)

Foundation lesson introducing metrics, traces, and logs as complementary signals.

**Contents**:
- Why observability matters for AI applications
- Metrics: aggregated numerical data (Prometheus)
- Traces: request flow across services (Jaeger)
- Logs: event-level detail (Loki)
- Choosing the right signal for debugging scenarios
- The 4 Golden Signals (latency, traffic, errors, saturation)

---

### L02: Metrics with Prometheus (30 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**DACA Source**: `Install-Prometheus-Grafana.md`

Hands-on Prometheus installation and PromQL fundamentals.

**Contents**:
- Installing kube-prometheus-stack via Helm
- Prometheus architecture (scraping, TSDB, rules)
- PromQL basics: selectors, functions, aggregations
- Adding metrics to Task API with `prometheus_client`
- Creating ServiceMonitor for custom apps
- Recording rules for efficient queries

---

### L03: Visualization with Grafana (25 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**DACA Source**: `Install-Prometheus-Grafana.md`

Building effective dashboards for service monitoring.

**Contents**:
- Grafana dashboard JSON model
- Creating panels for the 4 golden signals
- Dashboard variables for multi-service views
- Importing community dashboards
- Dashboard best practices (don't overload, use consistent colors)

---

### L04: Distributed Tracing with OpenTelemetry & Jaeger (30 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**DACA Source**: `Enable-Dapr-Metrics-and-Tracing.md`

Instrumenting applications for distributed tracing.

**Contents**:
- OpenTelemetry concepts: traces, spans, context propagation
- Instrumenting FastAPI with `opentelemetry-instrumentation-fastapi`
- Creating custom spans for business operations
- Deploying Jaeger for trace visualization
- Analyzing traces to find bottlenecks
- Sampling strategies for production (1% vs 100%)

---

### L05: Centralized Logging with Loki (25 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**DACA Source**: `Centralized-Logging-with-Loki-or-EFK.md`

Setting up centralized log aggregation.

**Contents**:
- Loki architecture (index labels, not content)
- Installing Loki stack with Promtail
- LogQL queries: stream selectors, filters, parsers
- Structured logging in Python for queryability
- Log retention and storage considerations
- Correlating logs with traces via trace_id

---

### L06: SRE Foundations - SLIs, SLOs, and Error Budgets (30 min)
**Layer**: L1 (Manual/Conceptual) → L2 (AI Collaboration)
**Proficiency**: B1
**DACA Source**: `Define-SLOs-and-SLAs.md`

Applying SRE practices to measure and improve reliability.

**Contents**:
- SLI vs SLO vs SLA: definitions with examples
- Choosing good SLIs (availability, latency, correctness)
- Setting realistic SLO targets (99.9% vs 99.99%)
- Error budget calculation and interpretation
- Creating SLO recording rules in Prometheus
- Building SLO dashboards in Grafana

---

### L07: Alerting and Incident Response (25 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**DACA Source**: (New content - alerting patterns)

Setting up effective alerting that avoids alert fatigue.

**Contents**:
- Multi-window, multi-burn-rate alerting (Google SRE pattern)
- PrometheusRule CRD for alert definitions
- Alertmanager routing and notification
- Alert hygiene: severity levels, actionability
- Incident response basics: runbooks, escalation
- Post-incident reviews and SLO impact

---

### L08: Cost Engineering and FinOps (30 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**DACA Source**: `Resource-Sizing-Guidelines.md`, `Use-of-Spot-Instances.md`

Implementing cost visibility and optimization.

**Contents**:
- FinOps principles: visibility, optimization, operation
- Installing OpenCost for Kubernetes cost monitoring
- Cost allocation by namespace, team, and product (labels)
- Identifying waste: idle resources, over-provisioning
- Right-sizing with VPA recommendations
- Cost dashboards and budget alerts
- Scheduling non-production for savings

---

### L09: Dapr Observability Integration (25 min)
**Layer**: L2 (AI Collaboration)
**Proficiency**: B1
**DACA Source**: `Enable-Dapr-Metrics-and-Tracing.md`

Leveraging Dapr's built-in observability features.

**Contents**:
- Dapr metrics configuration (Configuration CRD)
- Creating ServiceMonitor for Dapr sidecars
- Dapr tracing with OpenTelemetry Collector
- Observability for Dapr Actors (actor activation, method calls)
- Observability for Dapr Workflows (step duration, failures)
- Correlating app traces with Dapr traces

---

### L10: Capstone - Full Observability Stack for Task API (40 min)
**Layer**: L4 (Spec-Driven Orchestration)
**Proficiency**: B1
**DACA Source**: All previous sources integrated

Building production-ready observability for Task API.

**Contents**:
- Deploy complete observability stack via Helm
- Instrument Task API with metrics, traces, and structured logs
- Define SLOs for Task API (99.9% availability, P95 < 200ms)
- Create Task API SLO dashboard
- Set up multi-burn-rate alerts
- Configure cost allocation labels
- Finalize and test `observability-cost-engineer` skill

---

## Assumptions

1. **Platform**: Students have Docker Desktop Kubernetes running locally
2. **Helm**: Students completed Ch51 and can deploy Helm charts
3. **Dapr**: Students completed Ch53 and have Dapr installed
4. **Running Example**: Task API from earlier chapters is available to instrument
5. **Tool Versions**: Prometheus 2.45+, Grafana 10+, Loki 2.9+, Jaeger 1.50+, OpenCost 1.105+
6. **No cloud billing APIs**: Cost monitoring uses resource-based estimation (OpenCost on-prem mode)

---

## Constraints

- **Platform Scope**: Docker Desktop Kubernetes only (no cloud-specific features)
- **Cost Scope**: Focus on resource-based cost estimation, not cloud billing integration
- **Tracing Scope**: OpenTelemetry + Jaeger (not Zipkin or proprietary solutions)
- **Logging Scope**: Loki (not EFK stack to reduce complexity)
- **No KEDA**: Autoscaling covered in separate chapter (Ch56)

---

## Dependencies

- **Ch49**: Docker basics for understanding container resource limits
- **Ch50**: Kubernetes knowledge for deploying observability stack
- **Ch51**: Helm for installing kube-prometheus-stack, Loki, Jaeger
- **Ch53**: Dapr for observing Dapr sidecars, actors, workflows
- **Ch54**: GitOps for deploying observability stack declaratively
- **Ch57**: Dapr Actors for observability of actor-based patterns

---

## Out of Scope

- Cloud-provider-specific cost tools (AWS Cost Explorer, GCP Billing)
- APM platforms (Datadog, New Relic, Dynatrace)
- Advanced tracing (Tempo, Grafana Traces)
- EFK/ELK stack (simplified to Loki)
- Chaos engineering and reliability testing
- Multi-cluster observability
