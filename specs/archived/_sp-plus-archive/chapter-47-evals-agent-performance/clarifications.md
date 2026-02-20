# Clarifications: Chapter 47 - Evals: Measuring Agent Performance

**Status**: Self-clarified (autonomous execution mode)
**Date**: 2025-12-30

## Clarification Questions & Resolutions

### CQ-1: What is the relationship between this chapter and existing evaluation skill?

**Question**: The codebase has `.claude/skills/evaluation/SKILL.md` focused on context engineering evaluation. How does Chapter 47 relate?

**Resolution**: Chapter 47 uses the NEW `agent-evals` skill (created in Phase A) which focuses specifically on Andrew Ng's methodology for agent evaluation. The existing `evaluation` skill covers broader context engineering evaluation concepts. They are complementary but distinct:
- `evaluation` skill: Context window management, degradation testing
- `agent-evals` skill: Reasoning quality, graders, error analysis

### CQ-2: Should examples be SDK-specific or truly framework-agnostic?

**Question**: The spec says "framework-agnostic" but students have learned OpenAI, Claude, and Google ADK. Should examples show all three?

**Resolution**: Examples should be conceptual with Python pseudocode that works with any SDK. Where code is needed:
- Use generic function signatures (not SDK-specific)
- Show the PATTERN, not the framework
- Include a note: "This pattern works with OpenAI Agents SDK, Claude SDK, or Google ADK"

### CQ-3: How deep should the running example go?

**Question**: Task API agent is the running example. How complex should the evals be?

**Resolution**: Keep evals focused on demonstrable concepts:
- **Routing eval**: Did agent route to correct handler (create/update/query)?
- **Tool selection eval**: Did agent call correct tools?
- **Output format eval**: Is response properly structured?
- Avoid complex multi-step scenarios that obscure the eval methodology

### CQ-4: What constitutes "Reflect on Your Skill" sections?

**Question**: The spec mentions each lesson ends with skill reflection. What format?

**Resolution**: Each "Reflect on Your Skill" section should:
1. State what the lesson added to the student's `agent-evals` skill
2. Include 1-2 questions prompting the student to update their skill
3. Be 3-5 sentences, not a full exercise

Example format:
```
## Reflect on Your Skill

This lesson taught you binary criteria grading. Update your `agent-evals` skill with:
- A template for converting 1-5 rubrics to binary criteria
- The pattern: 5 yes/no checks → sum for 0-5 score

Ask yourself: What criteria would you use to grade YOUR agent's outputs?
```

### CQ-5: Should L00 create skill from scratch or extend existing skill?

**Question**: Students may have the `evaluation` skill from context engineering. Does L00 create a new `agent-evals` skill or extend it?

**Resolution**: L00 creates a NEW `agent-evals` skill:
- Clone skills-lab fresh (no assumptions about prior state)
- Create `agent-evals` skill with evaluation methodology focus
- This is DIFFERENT from the context engineering `evaluation` skill
- By L10, students have a focused, tested `agent-evals` skill

### CQ-6: How to handle the Andrew Ng video content licensing?

**Question**: The skill and lessons reference Andrew Ng's course. Can we quote directly?

**Resolution**:
- Quote SHORT excerpts (under 30 words) with attribution
- Paraphrase longer concepts
- Always cite: "Based on Andrew Ng's Agentic AI Course"
- Focus on teaching the METHODOLOGY, not reproducing the course

### CQ-7: What's the minimum viable eval dataset size?

**Question**: Spec says 10-20 cases. Is there a minimum for exercises?

**Resolution**:
- L03 exercise: 20 cases (as specified)
- Quick exercises: 5-10 cases acceptable
- Key insight: "Start with 10-20, not 1000" - emphasize quality over quantity

### CQ-8: How technical should LLM-as-judge implementation be?

**Question**: L05 teaches LLM-as-judge. Should students implement full infrastructure?

**Resolution**: Keep it conceptual + minimal code:
- Show prompt template structure
- Demonstrate calling any LLM API with the prompt
- Parse JSON response for scores
- NOT: Building a full evaluation pipeline, caching, batching, etc.

### CQ-9: Error analysis spreadsheet - what tool?

**Question**: L06 uses spreadsheet for error counting. What tool should students use?

**Resolution**: Tool-agnostic:
- Show CSV structure that works anywhere
- Students can use Excel, Google Sheets, or plain CSV
- Include Python code to generate CSV from eval results
- Focus on the THINKING, not the tool

### CQ-10: What level of pytest knowledge is assumed?

**Question**: Spec assumes pytest from Ch46. What specific features?

**Resolution**: Assume students know from Ch46:
- Basic test functions (`def test_...`)
- Assertions (`assert result == expected`)
- Fixtures (`@pytest.fixture`)
- Running tests (`pytest tests/`)

Do NOT assume:
- Parameterization
- Mocking (brief reminder if needed)
- Coverage tools

---

## Resolved Ambiguities

| Area | Resolution |
|------|------------|
| SDK specificity | Framework-agnostic patterns, not SDK-specific code |
| Running example depth | Simple routing/tool/output evals, not complex scenarios |
| Skill relationship | New `agent-evals` skill, distinct from `evaluation` skill |
| Quote attribution | Short quotes with Andrew Ng attribution |
| Tool requirements | Minimal: Python, any LLM API, any spreadsheet |
| Pytest assumptions | Basic features only (from Ch46) |

---

## Implementation Notes

1. **Lesson Videos**: No lesson videos for this chapter (unlike Ch1 which had embedded videos)
2. **Try With AI**: Each lesson needs 3 prompts following the quality reference pattern
3. **Safety Notes**: Include note about LLM grader limitations (not perfect judges)
4. **Code Blocks**: Use Python for all code examples, generic signatures
5. **Tables**: Use comparison tables extensively (TDD vs Evals, Component vs E2E, etc.)
