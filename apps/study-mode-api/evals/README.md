# Teach Me Tutor — Eval Suite

Automated evaluations for the Socratic tutor prompt using [OpenAI Evals API](https://platform.openai.com/docs/guides/evals).

Based on learning sciences research from [eval-driven-edu-agents_research](https://github.com/mjunaidca/eval-driven-edu-agents_research).

## Quick Start

```bash
# Run all evals (creates eval + uploads data + runs + waits for results)
cd apps/study-mode-api
uv run python evals/run_eval.py

# Re-run after prompt changes (reuse existing eval and data)
uv run python evals/run_eval.py --eval-id eval_xxx --file-id file_xxx --run-name "prompt-v3"

# Create eval without running (use dashboard instead)
uv run python evals/run_eval.py --create-only
```

## Grader Architecture (2 Layers)

### Layer 1: Surface Safety (String Checks — fast, deterministic)

| # | Check | Type |
|---|-------|------|
| 1 | No "Great question" filler | `not_contains` |
| 2 | No "Nice start" filler | `not_contains` |
| 3 | No "Micro-explain" label | `not_contains` |
| 4 | No "Micro_explain" label | `not_contains` |
| 5 | No "STEP 1" label | `not_contains` |

### Layer 2: Education-Centric Model Graders (GPT-4.1 as judge)

| Grader | Dimension | What It Measures |
|--------|-----------|-----------------|
| **A. Content Grounding** | Faithfulness | All claims grounded in lesson content, no hallucination |
| **B. Teaching Intent** | Pedagogy | Teaches and guides, not just answers like a chatbot |
| **C. Pedagogical Structure** | Flow | Acknowledge → Teach → Check pattern |
| **D. Cognitive Scaffolding** | Adaptation | Meets learner where they are, simplifies when stuck |
| **E. Question Quality** | Instruction | One question, after teaching, narrow and specific |
| **F. Study Mode Integrity** | Safety | No shortcuts, no spoon-feeding, concise, no filler |

## Why These 6 Graders?

From the research, evals for educational agents must answer:
> "Did this response behave like a TEACHER?"

Not "Was it fluent?" or "Was it friendly?"

| Grader | Maps to Prompt Rule |
|--------|-------------------|
| A. Grounding | "Use LESSON CONTENT" — no external knowledge |
| B. Teaching Intent | "GUIDING them — not lecturing" |
| C. Structure | "TEACH → CHECK → ADAPT" pattern |
| D. Scaffolding | "WHEN STUDENT SAYS NO — TEACH FIRST" |
| E. Question Quality | "ONE question per response, after teaching" |
| F. Integrity | "NEVER DO" rules (filler, labels, multiple-choice) |

## Test Scenarios (20 cases)

| Scenario | Count | Tests |
|----------|-------|-------|
| `first_message` | 1 | Greeting + topic + diagnostic question |
| `student_says_no` | 3 | "no", "not really", "nope" → must teach |
| `student_stuck` | 5 | "I don't know", "I can't", "not sure", "confusing", "what?" |
| `correct_answer` | 3 | Confirm + advance to next concept |
| `wrong_answer` | 1 | Gentle correction with analogy |
| `partially_correct` | 1 | Correct the gap, re-ask simpler |
| `student_asks_question` | 4 | Answer directly, connect to lesson |
| `student_confirms` | 2 | "ok got it", "yeah makes sense" |

## Eval-Driven Development Workflow

```
Change prompt in triage.py
    → Run: uv run python evals/run_eval.py
    → Check dashboard scores (A-F graders)
    → Fix failing graders
    → Re-run eval
    → All passing → Push to PR
```
