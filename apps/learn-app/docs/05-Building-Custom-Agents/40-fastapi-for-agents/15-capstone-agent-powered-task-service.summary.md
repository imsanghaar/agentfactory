### Core Concept
Specification-driven development: write spec with success criteria before implementation, then validate. Compose all chapter patterns (CRUD, auth, database, streaming, agents) into deployable multi-agent service. Triage agent routes to specialists (scheduler, breakdown, blocker).

### Key Mental Models
- **Spec as contract**: Checkboxes become testing checklist; tables become routing guide
- **Pattern composition**: Every lesson contributes—L1-L5 CRUD, L6-L9 config/auth, L10 DI, L11-L12 streaming/agents
- **Multi-agent routing**: Triage determines specialist; streaming shows handoff to user
- **Digital FTE product**: Add docs, monitoring, deployment, pricing = sellable service

### Critical Patterns
- Spec structure: Success criteria checkboxes, endpoint table with Method/Auth/Rate Limit
- Project layout: `app/auth/`, `app/tasks/`, `app/agents/` directories
- Triage system: Returns specialist ID (scheduler/breakdown/blocker) based on intent
- Specialist call: Streaming response with `with client.messages.stream(...)`
- Test structure: `class TestAuthentication:`, `class TestTaskCRUD:` validate spec criteria

### AI Collaboration Keys
- Prompt 1: Agent memory—conversation history per task for continuity
- Prompt 2: OpenTelemetry tracing—timing across multi-agent flow
- Prompt 3: Custom specialist—domain-specific system prompts for your industry

### Common Mistakes
- Starting implementation before specification (unclear success criteria)
- Not testing against spec (implementation diverges from contract)
- Single agent for everything (specialists provide focused expertise)
- Missing deployment configuration (skill without monetization path)

### Connections
- **Builds on**: Agent Integration (Lesson 14) + all L1-L12 patterns
- **Leads to**: Chapter 41 (ChatKit Server) / Part 7 deployment chapters
