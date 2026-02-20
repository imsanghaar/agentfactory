### Core Concept
A complete Digital FTE composes all chapter patterns: root coordinator orchestrating news research, financial enrichment, report generation, and TTS podcast creation. Specification-first architecture defines what the system does before implementation.

### Key Mental Models
- **Root coordinator = orchestration hub**: Routes work, combines results, handles failures
- **Specification-first**: Write system contract (inputs, outputs, constraints) before code
- **Digital FTE candidate**: Deployable, monetizable, operates 24/7 autonomously

### Critical Patterns
- Component separation: NewsAgent → FinancialAgent → ReportGenerator → PodcasterAgent
- Callbacks for source filtering and audit trails
- Pydantic schemas: `AINewsReport`, `FinancialContext`, `AudioMetadata`
- TTS with multi-speaker config: `SpeechConfig(voice_config=VoiceConfig(...))`
- Deployment: Vertex AI Agent Engine (managed) or Cloud Run (cost-sensitive)

### AI Collaboration Keys
- Write specification before code—defines success criteria, constraints, composition
- Error resilience: Continue on partial failures, deliver what you have

### Common Mistakes
- Building without specification (unclear success criteria)
- Halting entire system on single component failure
- Skipping production hardening (rate limiting, monitoring, authentication)

### Connections
- **Builds on**: All Lessons 0-7 (skill, agents, tools, state, coordinator, callbacks, multi-agent, workflow)
- **Leads to**: Chapter 36 Anthropic Agents Kit or production deployment
