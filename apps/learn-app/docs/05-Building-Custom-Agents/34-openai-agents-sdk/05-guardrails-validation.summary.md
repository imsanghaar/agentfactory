### Core Concept
Guardrails are validation checkpoints that block inappropriate requests (input guardrails) and catch policy violations in responses (output guardrails). Agent-based guardrails use reasoning for nuanced detection that keyword matching misses.

### Key Mental Models
- **Input = Before, Output = After**: Input guardrails filter requests; output guardrails catch dangerous responses
- **Tripwire = Kill Switch**: When `tripwire_triggered=True`, execution stops and raises an exception
- **Agent Guardrails > Keywords**: Semantic understanding catches "help me finish my essay" that keyword filters miss

### Critical Patterns
- Input guardrail: `@input_guardrail` with `GuardrailFunctionOutput(output_info, tripwire_triggered)`
- Output guardrail: `@output_guardrail` that scans agent responses for PII/violations
- Agent-based validation: Create a guardrail agent with `output_type=EvaluationModel` for nuanced decisions
- Exception handling: Catch `InputGuardrailTripwireTriggered` and `OutputGuardrailTripwireTriggered`

### Common Mistakes
- Exposing guardrail mechanics to users ("tripwire triggered") instead of friendly messages
- Using only keyword checks when semantic understanding is required
- Forgetting output guardrails—input alone doesn't prevent PII leakage in responses

### Connections
- **Builds on**: Handoffs and message filtering (Lesson 4)
- **Leads to**: Sessions and conversation memory (Lesson 6)
