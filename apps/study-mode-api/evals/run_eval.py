"""OpenAI Evals for Teach Me Socratic Tutor.

This script creates and runs evaluations against the Teach Me tutor prompt
to ensure it meets quality criteria. Run this after any prompt changes to
catch regressions.

Usage:
    # First time: creates eval + uploads data + runs
    python evals/run_eval.py

    # Re-run with existing eval (after prompt changes)
    python evals/run_eval.py --eval-id eval_xxx --file-id file_xxx

    # Run from dashboard instead (copy eval ID from output)
    python evals/run_eval.py --create-only

Environment:
    OPENAI_API_KEY must be set
"""

import argparse
import sys
import time
from pathlib import Path

from openai import OpenAI

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

MODEL = "gpt-5-nano-2025-08-07"
EVAL_NAME = "Teach Me Tutor - Prompt Quality"
TEST_DATA_FILE = Path(__file__).parent / "tutor_test_data.jsonl"

# Sample lesson content used in the eval (abbreviated for token efficiency)
LESSON_CONTENT = """\
The Agent Factory Thesis: In the AI era, the most valuable companies will \
be those that can manufacture Digital Full-Time Equivalents (FTEs) — AI \
employees powered by six key components: agents, specs, skills, MCP, \
autonomy, and cloud-native technologies.

An AI agent is an autonomous software entity that can perceive its \
environment, make decisions, and take actions to achieve goals — unlike a \
chatbot which only responds to direct prompts.

Key concepts:
- **Digital FTE**: An AI employee that replaces or augments human work
- **Agents**: Autonomous software that acts on behalf of users
- **Specs**: Formal instructions and rules agents follow (like a job description)
- **Skills**: Packaged capabilities agents can use (like job skills)
- **MCP (Model Context Protocol)**: A standard for connecting agents to tools
- **Autonomy**: Agents can make decisions and act without constant human input
- **Cloud-native**: Built for scalable, modern cloud infrastructure
"""

# ---------------------------------------------------------------------------
# Prompt templates (must match triage.py exactly)
# ---------------------------------------------------------------------------

FIRST_MESSAGE_SYSTEM_PROMPT = """\
You are Sage, an approachable-yet-dynamic tutor for the AI Agent Factory \
book. You help the student learn by GUIDING them — not by lecturing. \
Follow these strict rules for every response.
STUDENT NAME: Test Student

## STRICT RULES
1. Build on existing knowledge. Connect new ideas to what the student knows.
2. Guide, don't just give answers. Use questions, hints, and small steps so \
the student discovers concepts themselves.
3. Check and reinforce. After hard parts, have the student restate or apply \
the idea. Offer quick summaries to help it stick.
4. Vary the rhythm. Mix micro-explanations, guiding questions, practice \
rounds, and "explain it back to me" — keep it conversational, not a lecture.

## LESSON CONTENT
📚 The Agent Factory Thesis
---
""" + LESSON_CONTENT + """
---

This is the first message. Greet the student warmly as "Hi Test Student!" \
and introduce the topic **The Agent Factory Thesis** in one sentence. \
Then ask a lightweight diagnostic question to gauge what they already \
know — e.g. 'Have you come across [key concept] before?' or 'What comes \
to mind when you hear [topic]?' Keep it short. ONE question only. \
Do NOT lecture yet.

## HOW TO RESPOND (choose ONE approach per turn — NEVER show these labels)
- Ask what they know about a concept before explaining it.
- Give a short explanation (2-3 sentences max) with an analogy or example.
- Ask ONE focused question to lead them to discover the answer.
- Confirm correct answers briefly, then introduce the next concept.
- Ask them to explain it back in their own words.
- Give a related mini-task to apply what they learned.
- Switch modes — quiz, roleplay, or "teach it back to me."

## CRITICAL: WHEN STUDENT SAYS "NO", "I DON'T KNOW", OR SEEMS STUCK
This is the most important rule. When a student says "no", "not really", \
"I don't know", or seems stuck, you MUST:
1. TEACH the concept simply with an analogy (2-3 sentences)
2. Then ask them to restate what you just explained
You must NEVER respond to these with another probing question like \
"What do you think about...?" or "What do you already know about...?" \
TEACH FIRST, then ask.

## RESPONSE RULES
- Be warm, patient, and plain-spoken. Few emoji, no exclamation overload.
- Be BRIEF. No essay-length responses. Aim for good back-and-forth.
- ONE question per response. Never ask multiple questions.
- Do NOT do the student's thinking for them. Guide with hints and steps.
- Use **bold** for key terms when first introduced.
- NEVER show internal labels like "Micro-explain:" in your response.

## NEVER DO
❌ Say "Great question!", "Nice start!" or any filler praise
❌ Give long lectures — keep explanations to 2-3 sentences max
❌ Ask multiple questions or give multiple-choice options
❌ Respond to "no" or "I don't know" with more questions — TEACH first
❌ Show move labels like "Micro-explain:" or "Guide question:" in output
❌ Ignore what the student said — always build on their response"""

FOLLOW_UP_SYSTEM_PROMPT = """\
You are Sage, an approachable-yet-dynamic tutor for the AI Agent Factory \
book. You help the student learn by GUIDING them — not by lecturing. \
Follow these strict rules for every response.
STUDENT NAME: Test Student

## STRICT RULES
1. Build on existing knowledge. Connect new ideas to what the student knows.
2. Guide, don't just give answers. Use questions, hints, and small steps so \
the student discovers concepts themselves.
3. Check and reinforce. After hard parts, have the student restate or apply \
the idea. Offer quick summaries to help it stick.
4. Vary the rhythm. Mix micro-explanations, guiding questions, practice \
rounds, and "explain it back to me" — keep it conversational, not a lecture.

## LESSON CONTENT
📚 The Agent Factory Thesis
---
""" + LESSON_CONTENT + """
---

FOLLOW-UP — do NOT greet again.

Adapt based on what the student said:

If CORRECT: Confirm briefly ("Right!"), then teach the next concept or ask \
them to explain it back in their own words.

If PARTIALLY CORRECT: Gently correct the gap with a short explanation \
(1-2 sentences), then re-ask a simpler version.

If WRONG: Correct charitably with a short analogy or example that makes \
it click, then check again with an easier question.

If "NO", "I DON'T KNOW", "NOT REALLY", or STUCK: This is critical — \
do NOT ask another probing question. TEACH the concept in 2-3 simple \
sentences with an analogy. Then ask them to restate what you just explained.

If they ASK A QUESTION: Answer it directly and concisely, connect it back \
to the lesson, then ask one follow-up question.

ALWAYS end with exactly ONE question. Keep response brief. No filler praise.

## HOW TO RESPOND (choose ONE approach per turn — NEVER show these labels)
- Ask what they know about a concept before explaining it.
- Give a short explanation (2-3 sentences max) with an analogy or example.
- Ask ONE focused question to lead them to discover the answer.
- Confirm correct answers briefly, then introduce the next concept.
- Ask them to explain it back in their own words.
- Give a related mini-task to apply what they learned.
- Switch modes — quiz, roleplay, or "teach it back to me."

## CRITICAL: WHEN STUDENT SAYS "NO", "I DON'T KNOW", OR SEEMS STUCK
This is the most important rule. When a student says "no", "not really", \
"I don't know", or seems stuck, you MUST:
1. TEACH the concept simply with an analogy (2-3 sentences)
2. Then ask them to restate what you just explained
You must NEVER respond to these with another probing question like \
"What do you think about...?" or "What do you already know about...?" \
TEACH FIRST, then ask.

## RESPONSE RULES
- Be warm, patient, and plain-spoken. Few emoji, no exclamation overload.
- Be BRIEF. No essay-length responses. Aim for good back-and-forth.
- ONE question per response. Never ask multiple questions.
- Do NOT do the student's thinking for them. Guide with hints and steps.
- Use **bold** for key terms when first introduced.
- NEVER show internal labels like "Micro-explain:" in your response.

## NEVER DO
❌ Say "Great question!", "Nice start!" or any filler praise
❌ Give long lectures — keep explanations to 2-3 sentences max
❌ Ask multiple questions or give multiple-choice options
❌ Respond to "no" or "I don't know" with more questions — TEACH first
❌ Show move labels like "Micro-explain:" or "Guide question:" in output
❌ Ignore what the student said — always build on their response"""

# ---------------------------------------------------------------------------
# Testing Criteria (Graders)
# ---------------------------------------------------------------------------

TESTING_CRITERIA = [
    # ===================================================================
    # Education-Centric Model Graders (from Learning Sciences)
    # Based on: mjunaidca/eval-driven-edu-agents_research
    # These measure "Did this response behave like a TEACHER?"
    #
    # Note: Surface checks (filler praise, leaked labels) are covered
    # by Grader F (Study Mode Integrity) using GPT-4.1 as judge.
    # OpenAI Evals string_check only supports eq/ne/like/ilike,
    # so "not contains" checks must use model graders.
    # ===================================================================
    #
    # GRADER A: Content Grounding & Faithfulness
    # -------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "A. Content Grounding & Faithfulness",
        "model": "gpt-4.1",
        "input": [
            {
                "role": "user",
                "content": "You are evaluating a Study Mode teaching response for CONTENT GROUNDING.\n\nLESSON CONTENT PROVIDED TO TUTOR:\n\"\"\"\n"  # noqa: E501
                + LESSON_CONTENT
                + "\"\"\"\n\nTUTOR RESPONSE: \"{{ sample.output_text }}\"\n\nEVALUATION CRITERIA:\nThe tutor's response must be strictly grounded in the lesson content above.\n\nCHECK:\n- Are all factual claims supported by the lesson?\n- Does the tutor avoid introducing external facts or general AI knowledge not in the lesson?\n- Does the tutor avoid inventing terminology?\n- Are analogies reasonable extensions of lesson concepts (not fabricated facts)?\n\nScore 1.0 if the response is well-grounded in the lesson.\nScore 0.5 if mostly grounded with minor extrapolation.\nScore 0.0 if the response introduces significant claims not found in the lesson content.",  # noqa: E501
            }
        ],
        "pass_threshold": 0.5,
    },
    # -------------------------------------------------------------------
    # GRADER B: Teaching Intent Alignment
    # -------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "B. Teaching Intent Alignment",
        "model": "gpt-4.1",
        "input": [
            {
                "role": "user",
                "content": "You are evaluating whether a response behaves like a TEACHER, not a chatbot or Q&A system.\n\nSCENARIO: {{ item.scenario }}\nSTUDENT SAID: \"{{ item.student_message }}\"\nTUTOR RESPONSE: \"{{ sample.output_text }}\"\n\nEVALUATION CRITERIA:\nA teaching response should:\n- Explain concepts to build understanding\n- Use instructional language\n- Guide the student toward discovery\n- NOT just dump a final answer like StackOverflow\n- NOT treat the student as asking for a solution\n\nThe core question: Does this response prioritize TEACHING and UNDERSTANDING rather than just answering?\n\nScore 1.0 if clearly teaching-oriented (explains, guides, checks understanding).\nScore 0.5 if partially teaching (answers but with some explanation).\nScore 0.0 if it just gives a direct answer with no teaching effort, or responds like a chatbot.",  # noqa: E501
            }
        ],
        "pass_threshold": 0.5,
    },
    # -------------------------------------------------------------------
    # GRADER C: Pedagogical Structure
    # -------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "C. Pedagogical Structure",
        "model": "gpt-4.1",
        "input": [
            {
                "role": "user",
                "content": "You are evaluating the TEACHING STRUCTURE of a tutor's response.\n\nSCENARIO: {{ item.scenario }}\nTUTOR RESPONSE: \"{{ sample.output_text }}\"\n\nEVALUATION CRITERIA:\nA well-structured teaching response should have a clear flow:\n1. Acknowledge or connect to what the student said\n2. Explain or teach a core idea (with example/analogy)\n3. Check understanding with a question\n\nIt should NOT be:\n- Random paragraphs with no logical flow\n- A list of facts without progression\n- An abrupt or incomplete response\n- Multiple topics crammed together\n\nScore 1.0 if the response has clear pedagogical flow (acknowledge -> teach -> check).\nScore 0.5 if structure is present but could be clearer.\nScore 0.0 if the response has no discernible teaching structure.",  # noqa: E501
            }
        ],
        "pass_threshold": 0.5,
    },
    # -------------------------------------------------------------------
    # GRADER D: Cognitive Scaffolding
    # -------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "D. Cognitive Scaffolding",
        "model": "gpt-4.1",
        "input": [
            {
                "role": "user",
                "content": "You are evaluating COGNITIVE SCAFFOLDING in a tutor's response.\n\nSCENARIO: {{ item.scenario }}\nSTUDENT SAID: \"{{ item.student_message }}\"\nCONVERSATION CONTEXT: {{ item.conversation_history }}\nTUTOR RESPONSE: \"{{ sample.output_text }}\"\n\nEVALUATION CRITERIA:\nScaffolding means meeting the learner where they are:\n- Concepts introduced gradually (simple first, complex later)\n- New terms explained in context, not dropped as jargon\n- Uses analogies or concrete examples to bridge gaps\n- Adapts difficulty based on what the student said\n- When student is stuck: simplifies, doesn't escalate\n\nCHECK:\n- If student said 'no'/'I don't know': Does the tutor TEACH simply before asking? (Critical rule)\n- If student was correct: Does the tutor advance to the next concept?\n- If student was wrong: Does the tutor simplify and re-explain?\n\nScore 1.0 if the response adapts well to the student's level and scaffolds learning.\nScore 0.5 if partially scaffolded.\nScore 0.0 if the response assumes too much prior knowledge, drops jargon, or overwhelms the learner.",  # noqa: E501
            }
        ],
        "pass_threshold": 0.5,
    },
    # -------------------------------------------------------------------
    # GRADER E: Instructional Question Quality
    # -------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "E. Instructional Question Quality",
        "model": "gpt-4.1",
        "input": [
            {
                "role": "user",
                "content": "You are evaluating HOW QUESTIONS ARE USED in a tutor's response.\n\nSCENARIO: {{ item.scenario }}\nSTUDENT SAID: \"{{ item.student_message }}\"\nTUTOR RESPONSE: \"{{ sample.output_text }}\"\n\nEVALUATION CRITERIA:\nQuestions in a teaching response must be:\n- At most ONE question per response\n- The question checks understanding of what was just taught\n- The question is narrow and specific (not vague)\n- Questions come AFTER teaching, not before\n\nFAIL if:\n- Multiple questions in one response\n- Open-ended 'what do you think?' without teaching first\n- Questions asked BEFORE any teaching (when student is stuck)\n- Multiple-choice options (A, B, or C?)\n\nSPECIAL CASE: If student said 'no'/'I don't know'/'not sure'/'I can't' and the tutor asks a question WITHOUT teaching first -> Score 0.0 (most critical rule)\n\nScore 1.0 if question usage is excellent (one focused question after teaching).\nScore 0.5 if acceptable but could be better.\nScore 0.0 if questions are misused (multiple, before teaching, or multiple-choice).",  # noqa: E501
            }
        ],
        "pass_threshold": 0.5,
    },
    # -------------------------------------------------------------------
    # GRADER F: Study Mode Integrity & Safety
    # -------------------------------------------------------------------
    {
        "type": "score_model",
        "name": "F. Study Mode Integrity",
        "model": "gpt-4.1",
        "input": [
            {
                "role": "user",
                "content": "You are evaluating STUDY MODE INTEGRITY of a tutor's response.\n\nTUTOR RESPONSE: \"{{ sample.output_text }}\"\nSCENARIO: {{ item.scenario }}\n\nEVALUATION CRITERIA:\nStudy Mode is a TEACHING mode, not a chat mode. The tutor must:\n- Encourage understanding, not memorization\n- Not provide shortcuts or spoon-feed answers\n- Not bypass learning steps\n- Guide the student to think, not just consume\n- Keep responses concise (under 200 words)\n- Not use filler praise ('Great question!', 'Nice start!', 'Excellent!', 'Good job!')\n- Not leak internal labels ('Micro-explain:', 'Guide question:', 'STEP 1')\n- Not re-greet on follow-up messages\n\nScore 1.0 if the response fully maintains Study Mode integrity.\nScore 0.5 if mostly compliant with minor issues.\nScore 0.0 if the response breaks Study Mode rules (filler praise, labels leaked, chatbot behavior, spoon-feeding).",  # noqa: E501
            }
        ],
        "pass_threshold": 0.5,
    },
]

# ---------------------------------------------------------------------------
# Data source schema
# ---------------------------------------------------------------------------

DATA_SOURCE_CONFIG = {
    "type": "custom",
    "item_schema": {
        "type": "object",
        "properties": {
            "student_message": {"type": "string"},
            "scenario": {"type": "string"},
            "lesson_title": {"type": "string"},
            "is_first_message": {"type": "boolean"},
            "conversation_history": {"type": "string"},
        },
        "required": [
            "student_message",
            "scenario",
            "lesson_title",
            "is_first_message",
        ],
    },
    "include_sample_schema": True,
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def create_eval(client: OpenAI) -> str:
    """Create the eval configuration. Returns eval ID."""
    print("[1/3] Creating eval...")
    eval_obj = client.evals.create(
        name=EVAL_NAME,
        data_source_config=DATA_SOURCE_CONFIG,
        testing_criteria=TESTING_CRITERIA,
    )
    print(f"  Eval created: {eval_obj.id}")
    return eval_obj.id


def upload_test_data(client: OpenAI) -> str:
    """Upload test data JSONL file. Returns file ID."""
    print("[2/3] Uploading test data...")
    with open(TEST_DATA_FILE, "rb") as f:
        file_obj = client.files.create(file=f, purpose="evals")
    print(f"  File uploaded: {file_obj.id} ({file_obj.filename})")
    return file_obj.id


def run_eval(
    client: OpenAI, eval_id: str, file_id: str, run_name: str = "prompt-v2"
) -> dict:
    """Run the eval with our prompt. Returns run object."""
    print(f"[3/3] Running eval '{run_name}' with model {MODEL}...")

    # Build the message template
    # For first messages, use the first-message prompt
    # For follow-ups, use the follow-up prompt
    # We use a single template that works for both by including
    # conversation history as context
    system_prompt = FOLLOW_UP_SYSTEM_PROMPT

    run = client.evals.runs.create(
        eval_id,
        name=run_name,
        data_source={
            "type": "responses",
            "model": MODEL,
            "input_messages": {
                "type": "template",
                "template": [
                    {
                        "role": "developer",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": (
                            "Previous context: {{ item.conversation_history }}\n"
                            "Student message: {{ item.student_message }}"
                        ),
                    },
                ],
            },
            "source": {"type": "file_id", "id": file_id},
        },
    )
    print(f"  Run started: {run.id}")
    print(f"  Dashboard: {run.report_url}")
    return run


def wait_for_run(client: OpenAI, eval_id: str, run_id: str) -> dict:
    """Poll until run completes."""
    print("\n  Waiting for eval to complete", end="", flush=True)
    while True:
        run = client.evals.runs.retrieve(run_id, eval_id=eval_id)
        if run.status in ("completed", "failed", "canceled"):
            print(f"\n  Status: {run.status}")
            return run
        print(".", end="", flush=True)
        time.sleep(5)


def print_results(client: OpenAI, eval_id: str, run) -> None:
    """Print eval results summary with per-sample scores."""
    print("\n" + "=" * 70)
    print("EVAL RESULTS")
    print("=" * 70)

    counts = run.result_counts
    total = counts.total if counts else 0
    passed = counts.passed if counts else 0
    failed = counts.failed if counts else 0
    errored = counts.errored if counts else 0

    print(f"  Total: {total} | Passed: {passed} | Failed: {failed} | Errors: {errored}")

    if total > 0:
        score = passed / total * 100
        print(f"  Score: {score:.0f}%")

    # Build threshold lookup from TESTING_CRITERIA
    threshold_map = {}
    for tc in TESTING_CRITERIA:
        threshold_map[tc["name"]] = tc.get("pass_threshold", 0.5)

    if run.per_testing_criteria_results:
        print("\n  Per-Criteria Results:")
        print(f"  {'Criteria':<40} {'Threshold':>10} {'Pass':>6} {'Fail':>6} {'Rate':>7}")
        print("  " + "-" * 69)
        for r in run.per_testing_criteria_results:
            name = r.testing_criteria.split("-")[0].strip()[:39]
            t = threshold_map.get(name, 0.5)
            rate = r.passed / (r.passed + r.failed) * 100 if (r.passed + r.failed) > 0 else 0
            print(f"  {name:<40} {t:>10.1f} {r.passed:>6} {r.failed:>6} {rate:>6.0f}%")

    # Fetch per-sample output items to show individual scores
    print("\n  Per-Sample Scores:")
    print(f"  {'#':<4} {'Scenario':<25} {'Student Message':<30} {'Result':>8}")
    print("  " + "-" * 69)
    try:
        output_items = client.evals.runs.output_items.list(
            run.id, eval_id=eval_id
        )
        for idx, item in enumerate(output_items.data, 1):
            scenario = getattr(item, "datasource_item", {})
            if isinstance(scenario, dict):
                sc = scenario.get("item", {}).get("scenario", "?")
                msg = scenario.get("item", {}).get("student_message", "")
            else:
                sc = getattr(getattr(scenario, "item", None), "scenario", "?")
                msg = getattr(getattr(scenario, "item", None), "student_message", "")
            msg_short = (msg[:27] + "...") if len(msg) > 30 else msg
            status = getattr(item, "status", "?")
            print(f"  {idx:<4} {sc:<25} {msg_short:<30} {status:>8}")

            # Show individual grader scores if available
            results = getattr(item, "results", [])
            if results:
                for res in results:
                    grader = getattr(res, "name", getattr(res, "testing_criteria", "?"))
                    g_score = getattr(res, "score", None)
                    g_passed = getattr(res, "passed", None)
                    g_short = grader[:36] if grader else "?"
                    score_str = f"{g_score:.1f}" if g_score is not None else "n/a"
                    pass_str = "PASS" if g_passed else "FAIL"
                    print(f"       {g_short:<38} score={score_str:>5}  {pass_str}")
    except Exception as e:
        print(f"  (Could not fetch per-sample details: {e})")

    print(f"\n  Full report: {run.report_url}")
    print("=" * 70)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Run Teach Me tutor evals")
    parser.add_argument("--eval-id", help="Existing eval ID (skip creation)")
    parser.add_argument("--file-id", help="Existing file ID (skip upload)")
    parser.add_argument(
        "--run-name",
        default="prompt-v2",
        help="Name for this eval run (default: prompt-v2)",
    )
    parser.add_argument(
        "--create-only",
        action="store_true",
        help="Only create eval + upload data, don't run",
    )
    parser.add_argument(
        "--no-wait",
        action="store_true",
        help="Don't wait for results (just kick off the run)",
    )
    args = parser.parse_args()

    client = OpenAI()

    # Step 1: Create or reuse eval
    eval_id = args.eval_id or create_eval(client)

    # Step 2: Upload or reuse test data
    file_id = args.file_id or upload_test_data(client)

    if args.create_only:
        print(f"\n  Eval ID: {eval_id}")
        print(f"  File ID: {file_id}")
        print("  Run from dashboard or with:")
        print(f"    python evals/run_eval.py --eval-id {eval_id} --file-id {file_id}")
        return

    # Step 3: Run eval
    run = run_eval(client, eval_id, file_id, args.run_name)

    if args.no_wait:
        print(f"\n  Run kicked off. Check dashboard: {run.report_url}")
        return

    # Wait and show results
    completed_run = wait_for_run(client, eval_id, run.id)
    print_results(client, eval_id, completed_run)

    # Exit with error code if any tests failed
    if completed_run.result_counts and completed_run.result_counts.failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
