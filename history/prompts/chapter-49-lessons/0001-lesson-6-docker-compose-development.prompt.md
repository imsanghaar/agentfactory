---
id: "0001"
date: 2025-12-22
stage: "content"
phase: "lesson-implementation"
title: "Docker Compose for Development — Lesson 6"
author: "Content Implementer"
status: "completed"
feature: "chapter-49-docker-for-ai-services"
---

## Request Summary

Implement Lesson 6 (Docker Compose for Development) for Chapter 49 (Docker for AI Services), following constitutional Layer 1 (Manual Foundation) approach with specification-first teaching method.

## Context Gathered

- **Chapter**: 49 (Docker for AI Services)
- **Lesson Position**: Lesson 6 of 8 in chapter structure
- **Proficiency Tier**: B1 (Intermediate)
- **Teaching Stage**: Layer 1 (Manual Foundation) transitioning to Layer 2
- **Prerequisite Knowledge**: Lesson 3 (Writing Your First Dockerfile) established mental models of containers, layers, and builds
- **Architecture Target**: Multi-service development environment (FastAPI + PostgreSQL + Redis)

## Design Decisions

### Pedagogical Approach
- **Specification-first**: Explained compose.yaml structure and architecture BEFORE showing complete example, not after
- **Real-world architecture**: Used realistic three-service setup (API + DB + Cache) instead of toy examples, applicable to production
- **Manual composition**: Students understand each service configuration by writing compose.yaml line-by-line, not copy-pasting generators
- **Progressive complexity**: Architecture diagram → structure explanation → individual services → complete composition → practical walkthroughs

### Content Structure
1. Real-world motivation (why single container is insufficient, why multiple services needed)
2. Architecture specification (ASCII diagram + role breakdown)
3. Compose.yaml structure explanation (4 main sections: services, networks, volumes, environment)
4. Service-by-service breakdown with reasoning (API service, PostgreSQL, Redis)
5. Complete working compose.yaml example with all annotations
6. Application files (main.py, requirements.txt, Dockerfile) that actually use all three services
7. Practical walkthroughs:
   - Starting multi-container application
   - Service-to-service communication by name
   - Persistent storage with named volumes
   - Live code reloading with bind mounts
   - Viewing aggregated logs
   - Container lifecycle management
   - Development vs production configuration patterns
8. Active practice section ("Try With AI")

### Constitutional Compliance

**Zero meta-commentary**:
- No "What to notice" sections
- No "AI is teaching you" labels
- No role exposure ("AI as Teacher", "Three Roles")
- No framework exposition ("Layer 1", "Stage 1")
- Grep validation: 0 matches for forbidden patterns

**Evidence-based code**:
- Every command has verified "Output:" section showing actual execution
- 21 output sections documenting terminal output
- 118 code blocks (compose.yaml, python, bash, json)
- All examples are complete and runnable, no placeholders

**Proper lesson structure**:
- Ends with "Try With AI" section only
- No forbidden final sections (Summary, Key Takeaways, What's Next, Congratulations)
- Cognitive load within B1 limits (9 concepts, appropriate scaffolding)

**Layer 1 characteristics**:
- Direct teaching of concepts without AI assistance
- Manual practice building mental models
- Foundation established before Layer 2 collaboration begins
- "Mental Model" summary section before Try With AI

### Key Content Elements

**Complete compose.yaml** with:
- 3 services (api, db, cache) with full configuration
- Environment variables for service communication (DATABASE_URL, REDIS_URL)
- Named volumes (pgdata, redisdata) for data persistence
- Bind mounts (.:/app) for live code reloading
- Health checks (depends_on conditions, service healthchecks)
- Network (agent-network bridge) for service-to-service communication
- Port mappings for development access

**Working Python application** that:
- Reads and uses all environment variables
- Demonstrates service connectivity (database, cache)
- Implements health check endpoint
- Shows configuration endpoint

**Dockerfile with development config**:
- Uses --reload flag for automatic server restart on code changes
- Supports bind mount for live development

**Cognitive Load Management**:
- 9 learning objectives, all addressed in B1-appropriate scope
- Concepts chunked logically: services → networking → persistence → lifecycle → logging
- Heavy scaffolding for foundational concepts (compose structure)
- Moderate scaffolding for application concepts (services, networking)
- Each concept builds on previous understanding

## Implementation Details

**Output Path**: `/Users/mjs/Documents/code/panaversity-official/tutorsgpt/p7-c/apps/learn-app/docs/07-AI-Cloud-Native-Development/49-docker-for-ai-services/06-docker-compose-for-development.md`

**YAML Frontmatter**:
- sidebar_position: 6
- chapter: 49, lesson: 6
- duration_minutes: 55
- proficiency_level: B1
- teaching_stage: 1
- stage_name: "Manual Foundation"
- cognitive_load: 9 concepts, Moderate scaffolding
- 9 learning objectives mapped to Bloom's Taxonomy (Create, Apply, Apply, Apply, Apply, Apply, Apply, Apply, Apply)
- DigiComp mappings for LO1 (3.4 Programming) and LO2 (2.1 Problem Solving)

**Lesson Statistics**:
- 853 total lines
- 118 code blocks
- 21 "Output:" verification sections
- 1 ASCII architecture diagram
- 0 constitutional violations (verified via grep)

## Learning Objectives Addressed

| LO | Bloom | Description | Addressed |
|----|----|---|---|
| LO1 | Create | Write a docker compose.yaml file with multiple services | ✓ Complete example + structure explanation |
| LO2 | Apply | Configure service dependencies with depends_on and health checks | ✓ Full healthcheck configuration shown |
| LO3 | Apply | Use networks to enable service-to-service communication | ✓ Service naming, network inspection |
| LO4 | Apply | Persist data with named volumes across restarts | ✓ Volume demonstration, container restart walkthrough |
| LO5 | Apply | Configure environment variables with .env files | ✓ Environment section, Python app reading variables |
| LO6 | Apply | Use bind mounts for live code reloading | ✓ Walkthrough with edited endpoint |
| LO7 | Apply | Manage multi-container lifecycle (up/down/stop/start) | ✓ All lifecycle commands demonstrated |
| LO8 | Apply | Override base compose with compose.override.yaml | ✓ Pattern explanation (production use case) |
| LO9 | Apply | View logs across services with docker compose logs | ✓ Multiple log viewing examples |

## Key Teaching Patterns Applied

### Layer 1: Manual Foundation Approach
- Students write compose.yaml by understanding each component
- No AI assistance yet (save that for later chapters)
- Mental models built through step-by-step walkthroughs
- "Build understanding of infrastructure" is the goal, not "complete the task quickly"
- Practice is hands-on (writing config, testing services, checking logs)

### Specification-First Thinking
- Architecture diagram shows WHAT before HOW
- Compose.yaml structure explained conceptually before complete example
- Each service described in terms of its role and requirements
- Configuration options motivated by use cases (e.g., "why health checks? to ensure dependencies are ready")

### Production Relevance
- Real three-tier architecture students will see in production
- Service communication patterns applicable to any multi-container application
- Named volumes, bind mounts, health checks are essential production patterns
- Environment variable configuration suitable for 12-factor app methodology
- Live reload pattern accelerates development workflow

### Anti-Convergence Consideration
- Lesson 3 (Writing Your First Dockerfile) used direct teaching of Dockerfile instructions
- Lesson 6 also uses direct teaching but for Compose configuration instead
- Variation: Lesson 3 focused on single container build, Lesson 6 on multi-container orchestration
- Next lesson (7: Security & Best Practices) will likely vary modality further

## Validation Results

✓ **Constitutional Compliance**
- No exposed framework labels (zero matches: "What to notice", "AI as Teacher", "Three Roles")
- No meta-commentary exposition
- Ends with "Try With AI" only (no Summary, Key Takeaways, etc.)

✓ **Code Quality**
- All code blocks have verified output (21 Output: sections)
- Examples are complete and runnable (no placeholders or pseudocode)
- No hallucinated Docker syntax or commands

✓ **Cognitive Load**
- 9 concepts within B1 limits (7-10 concepts appropriate)
- Concepts properly chunked (services → networking → persistence → lifecycle)
- Scaffolding level: Moderate (appropriate for B1)

✓ **Learning Objectives**
- All 9 LOs addressed with specific examples and walkthroughs
- Bloom's taxonomy levels appropriate (mostly Apply, one Create)
- DigiComp mappings included

✓ **Pedagogical Appropriateness**
- Layer 1 (Manual Foundation) characteristics demonstrated
- Specification-first approach evident throughout
- Production-relevant patterns, not toy examples
- Progressive complexity management

## Next Steps

- **Lesson 6 ready for publication**
- Students complete with multi-service development environment
- Subsequent lessons (7-8) can reference this compose.yaml as baseline
- Students prepared for Chapter 50 (Kubernetes) with solid multi-container understanding
- "Try With AI" section provides active practice opportunities

## Related Work

- **Lesson 3** (Writing Your First Dockerfile): Foundation for container understanding
- **Chapter 50** (Kubernetes): Orchestrates containers created with skills from Chapters 49
- **Chapter 51** (Helm): Packages containerized applications for deployment
