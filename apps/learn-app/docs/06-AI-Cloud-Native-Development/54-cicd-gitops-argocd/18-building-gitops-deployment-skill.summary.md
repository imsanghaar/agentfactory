### Core Concept
Transform tacit GitOps knowledge into a reusable skill with three components: Persona (DevOps architect reasoning stance), Contextual Questions (gather decision-relevant constraints), and Decision Principles (reasoning frameworks with statements, why-it-matters, and application guidance).

### Key Mental Models
- **Persona**: Adopts DevOps architect mindset prioritizing automation, auditability, and reliability
- **Contextual Questions**: Deployment environment, GitOps architecture, team capability, production readiness
- **Decision Principles**: Declarative > Imperative, Progressive Complexity, Git Audit Trail, Sync Strategy by Risk, Secrets Never in Git, Health Before Traffic
- **Skill Application**: Adopt persona, answer questions, apply principles, document decisions

### Critical Patterns
- P1 (Declarative): All production workloads defined in Git; no manual kubectl modifications
- P4 (Sync Strategy): Dev auto-syncs, staging auto-syncs but manual prune, prod requires manual sync
- P5 (Secrets): External Secrets or Sealed Secrets; validate with `grep -r "password|token|key" manifests/`
- Validation checklist: manifests version-controlled, sync matches risk, no plaintext secrets, probes defined

### AI Collaboration Keys
- Ask Claude to refine your persona for GitOps deployment reasoning
- Request principle application to specific scenarios (internal tool vs customer API vs migration)
- Have AI identify gaps in contextual questions for batch job or ML pipeline deployments

### Common Mistakes
- Creating skills that prescribe steps rather than activating reasoning
- Skipping the contextual questions that reveal environment constraints
- Not validating that someone unfamiliar with your thinking can use the skill

### Connections
- **Builds on**: Lessons 0-17 - Complete CI/CD and GitOps chapter
- **Leads to**: Chapter 55 - Observability and Cost Engineering
