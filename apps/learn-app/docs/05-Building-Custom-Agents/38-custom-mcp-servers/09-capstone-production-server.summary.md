### Core Concept
Build a complete Research Assistant Server integrating all Chapter 38 patterns: Context for observability, sampling for AI reasoning, progress for feedback, roots for security, error handling for resilience. Follow specification-first methodology to create a deployable Digital FTE component.

### Key Mental Models
- **Specification-first (Layer 4)**: Write spec before code; decisions captured upfront
- **Feature integration**: Deterministic tools (search, list) + sampling tools (summarize, synthesize)
- **Architectural decisions**: Document WHY (sampling for reasoning, roots for security)
- **Digital FTE component**: Packaged, installable, customer-ready product

### Critical Patterns
- Spec structure: Intent, Success Criteria, Tools (each with inputs/outputs/error handling), Constraints, Architectural Decisions
- Tool classification: Deterministic (no tokens) vs Sampling (needs reasoning)
- validate_path(): Security check before ANY file operation
- Retry with backoff: 3 attempts with exponential delay for sampling failures
- Graceful degradation: Skip failed documents, continue synthesis with remaining

### AI Collaboration Keys
- Spec-driven: Claude implements to specification, not guessing requirements
- Multi-step operations: Progress per document, not just at start/end
- Production readiness: Error handling, logging, packaging all included

### Common Mistakes
- Skipping specification (leads to rework)
- Using sampling for simple file operations (wastes tokens)
- Not testing with MCP Inspector before Claude Desktop integration

### Connections
- **Builds on**: All lessons 1-8 (Context, Sampling, Progress, Roots, Transport, Scaling, Errors, Packaging)
- **Leads to**: Chapter Quiz (Lesson 10)
