### Core Concept
RAG evaluation measures four dimensions: Correctness (matches expected), Relevance (answers question), Groundedness (supported by context), Retrieval Quality (right docs found). LLM-as-Judge pattern uses structured output for automated evaluation. RAGAS provides battle-tested metrics.

### Key Mental Models
- **Four failure modes**: Wrong answer, irrelevant answer, hallucination, bad retrieval
- **LLM-as-Judge**: Evaluator LLM grades outputs against criteria
- **Metric interpretation**: 0.85+ excellent, 0.70-0.84 good, below 0.50 critical
- **Debug via metric**: Low faithfulness → hallucination, low context precision → retrieval issue

### Critical Patterns
- Evaluator: `with_structured_output(GradeSchema, method="json_schema", strict=True)`
- LangSmith: `@traceable` decorator + `client.evaluate()` for systematic testing
- RAGAS metrics: `Faithfulness()`, `ResponseRelevancy()`, `ContextPrecision()`, `ContextRecall()`
- Dataset: 20-30 examples covering factual, procedural, edge cases

### AI Collaboration Keys
- Design evaluation datasets covering diverse query types
- Debug failing metrics with targeted investigation
- Create domain-specific evaluators for specialized requirements

### Common Mistakes
- Skipping evaluation (shipping broken systems)
- Too few test examples (unreliable metrics)
- Not tracking metrics over time (degradation goes unnoticed)

### Connections
- **Builds on**: RAG for Task API (Lesson 6)
- **Leads to**: RAG Architecture Patterns Capstone (Lesson 8)
