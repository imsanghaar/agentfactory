"""Agent-native teaching mode with function tools and guardrails.

This module implements the reviewer's suggested architecture:
- 4 function tools for agent autonomy
- 1 output guardrail for marker enforcement
- 1 agent creation function

Per reviewer: agent has full autonomy, server has zero branching.
"""

import logging
import re

from agents import (
    Agent,
    GuardrailFunctionOutput,
    RunContextWrapper,
    function_tool,
    output_guardrail,
)

from .answer_verification import normalize_answer
from .teach_context import TeachContext
from .teach_instructions import teach_instructions

logger = logging.getLogger(__name__)

# Redis key patterns
ANSWER_KEY = "teach:correct_answer:{thread_id}"


# =============================================================================
# FUNCTION TOOLS (Exactly 4 per reviewer)
# =============================================================================


@function_tool
async def verify_answer(
    ctx: RunContextWrapper[TeachContext],
    answer: str,
) -> str:
    """
    Deterministic check against Redis-stored correct answer.

    Args:
        answer: Student's answer ("A", "B", or variations like "I think A")

    Returns:
        "CORRECT", "INCORRECT", or "UNKNOWN"
    """
    from ..core.redis_cache import get_redis

    thread_id = ctx.context.thread_id
    logger.info(f"[{thread_id}] verify_answer({answer})")

    redis = get_redis()
    if not redis:
        logger.warning(f"[{thread_id}] Redis unavailable")
        return "UNKNOWN"

    # Normalize answer
    normalized = normalize_answer(answer)
    if not normalized:
        logger.warning(f"[{thread_id}] Could not normalize: {answer}")
        return "UNKNOWN"

    # Get stored answer
    key = ANSWER_KEY.format(thread_id=thread_id)
    try:
        stored = await redis.get(key)
    except Exception as e:
        logger.error(f"[{thread_id}] Redis error: {e}")
        return "UNKNOWN"

    if not stored:
        logger.warning(f"[{thread_id}] No stored answer")
        return "UNKNOWN"

    stored_str = stored.decode("utf-8") if isinstance(stored, bytes) else stored

    if normalized == stored_str:
        logger.info(f"[{thread_id}] -> CORRECT")
        return "CORRECT"

    logger.info(f"[{thread_id}] -> INCORRECT ({normalized} != {stored_str})")
    return "INCORRECT"


@function_tool
async def advance_to_next_chunk(
    ctx: RunContextWrapper[TeachContext],
) -> str:
    """
    Move to next concept. Agent calls this after correct answer or max attempts.
    For single-chunk lessons, agent tracks progress via conversation history.

    Returns:
        Next chunk content as string, or "LESSON_COMPLETE"
    """
    thread_id = ctx.context.thread_id
    logger.info(f"[{thread_id}] advance_to_next_chunk()")

    ctx.context.current_chunk_index += 1
    ctx.context.attempt_count = 0

    if ctx.context.current_chunk_index >= ctx.context.total_chunks:
        logger.info(f"[{thread_id}] -> LESSON_COMPLETE")
        return "LESSON_COMPLETE"

    chunk = ctx.context.current_chunk
    logger.info(f"[{thread_id}] -> NEXT_CHUNK: {chunk['title']}")
    return f"NEXT_CHUNK: {chunk['title']}\n\n{chunk['content']}"


@function_tool
async def record_incorrect_attempt(
    ctx: RunContextWrapper[TeachContext],
) -> str:
    """
    Track failed attempt. Agent calls this after incorrect answer.

    Returns:
        "MAX_ATTEMPTS_REACHED" or current attempt status
    """
    thread_id = ctx.context.thread_id
    logger.info(f"[{thread_id}] record_incorrect_attempt()")

    ctx.context.attempt_count += 1

    if ctx.context.attempt_count >= ctx.context.max_attempts:
        logger.info(f"[{thread_id}] -> MAX_ATTEMPTS_REACHED")
        return "MAX_ATTEMPTS_REACHED"

    result = f"ATTEMPT_{ctx.context.attempt_count}_OF_{ctx.context.max_attempts}"
    logger.info(f"[{thread_id}] -> {result}")
    return result


@function_tool
async def store_correct_answer(
    ctx: RunContextWrapper[TeachContext],
    correct_option: str,
) -> str:
    """
    Store which option is correct. Agent MUST call after asking every question.

    Args:
        correct_option: "A" or "B"

    Returns:
        "STORED" or error message
    """
    from ..core.redis_cache import get_redis

    thread_id = ctx.context.thread_id
    logger.info(f"[{thread_id}] store_correct_answer({correct_option})")

    if correct_option not in ("A", "B"):
        logger.error(f"[{thread_id}] Invalid option: {correct_option}")
        return "ERROR: Must be A or B"

    redis = get_redis()
    if not redis:
        logger.warning(f"[{thread_id}] Redis unavailable")
        return "ERROR: Redis unavailable"

    key = ANSWER_KEY.format(thread_id=thread_id)
    try:
        await redis.set(key, correct_option, ex=3600)  # 1 hour TTL
        logger.info(f"[{thread_id}] -> STORED")
        return "STORED"
    except Exception as e:
        logger.error(f"[{thread_id}] Redis error: {e}")
        return f"ERROR: {e}"


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================


# =============================================================================
# OUTPUT GUARDRAILS
# =============================================================================


def _extract_options(output: str) -> tuple[str, str] | None:
    """Extract option A and B text from output."""
    # Multiple patterns to handle different formats:
    # - **A)** text
    # - A) text
    # - **A:** text

    # Try to find option A - look for A) or A:** followed by text until B) or newlines
    pattern_a = re.search(
        r'(?:\*\*)?A\)?(?:\*\*)?\s*[:\)]?\s*(.+?)(?=(?:\*\*)?B\)?(?:\*\*)?|\n\n|\n\*|$)',
        output, re.DOTALL | re.IGNORECASE
    )

    # Try to find option B - look for B) or B:** followed by text until end markers
    pattern_b = re.search(
        r'(?:\*\*)?B\)?(?:\*\*)?\s*[:\)]?\s*(.+?)(?=\n\n|\*Type|<!--|Type [AB]|$)',
        output, re.DOTALL | re.IGNORECASE
    )

    if pattern_a and pattern_b:
        opt_a = pattern_a.group(1).strip()
        opt_b = pattern_b.group(1).strip()
        # Clean up any remaining markdown
        opt_a = re.sub(r'\*+', '', opt_a).strip()
        opt_b = re.sub(r'\*+', '', opt_b).strip()
        if opt_a and opt_b:
            return opt_a, opt_b

    return None


def _extract_marker(output: str) -> str | None:
    """Extract the correct answer from <!--CORRECT:X--> marker."""
    match = re.search(r'<!--CORRECT:([AB])-->', output)
    return match.group(1) if match else None


def _score_option_relevance(option_text: str, lesson_content: str) -> float:
    """
    Score how relevant an option is to the lesson content.
    Higher score = more relevant = likely correct answer.

    Uses multiple signals:
    1. Word overlap with lesson content (weighted by word importance)
    2. Phrase matching (multi-word sequences)
    3. Negative patterns (absurd claims, contradictions)
    4. Linguistic cues (hedging language in wrong answers)
    """
    option_lower = option_text.lower()
    lesson_lower = lesson_content.lower()
    score = 0.0

    # === 1. WORD OVERLAP (core signal) ===
    # Common words to filter out (expanded list)
    common_words = {
        'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had',
        'her', 'was', 'one', 'our', 'out', 'has', 'have', 'been', 'will', 'more',
        'when', 'who', 'oil', 'its', 'say', 'she', 'two', 'way', 'could', 'people',
        'than', 'first', 'water', 'been', 'call', 'would', 'about', 'this', 'that',
        'with', 'from', 'they', 'which', 'their', 'what', 'there', 'make', 'because',
        'just', 'like', 'only', 'into', 'over', 'such', 'through', 'also', 'back',
        'after', 'most', 'even', 'being', 'where', 'between', 'both', 'under',
        'some', 'then', 'these', 'them', 'each', 'other', 'same', 'those', 'very',
    }

    # Extract meaningful words from option
    option_words = set(word for word in re.findall(r'\b[a-z]{4,}\b', option_lower)
                       if word not in common_words)

    # Extract meaningful words from lesson
    lesson_words = set(word for word in re.findall(r'\b[a-z]{4,}\b', lesson_lower)
                       if word not in common_words)

    # Calculate overlap - words that appear in both
    overlap = option_words & lesson_words
    score += len(overlap) * 1.5

    # Extra boost for longer/technical words (likely key concepts)
    for word in overlap:
        if len(word) >= 7:  # Longer words are more significant
            score += 1.0
        if len(word) >= 10:  # Very long words are key concepts
            score += 1.5

    # === 2. PHRASE MATCHING (strong signal) ===
    # Extract 2-3 word phrases from lesson
    lesson_bigrams = re.findall(r'\b([a-z]{4,}\s+[a-z]{4,})\b', lesson_lower)
    lesson_trigrams = re.findall(r'\b([a-z]{4,}\s+[a-z]{4,}\s+[a-z]{4,})\b', lesson_lower)

    # Phrase match is strong evidence
    for phrase in set(lesson_bigrams):
        if phrase in option_lower:
            score += 3.0

    for phrase in set(lesson_trigrams):
        if phrase in option_lower:
            score += 5.0

    # === 3. NEGATIVE PATTERNS (wrong answer indicators) ===

    # Absurd/impossible claims
    absurd_patterns = [
        r'\b(?:banned|illegal|prohibited|forbidden)\b',
        r'\bregulations?\s+(?:will|would|must)\b',
        r'\bgovernment\s+(?:will|would|must)\b',
        r'\b(?:always|never|impossible|guaranteed)\b',  # Extreme language
        r'\breplac(?:e|ing|ed)\s+(?:all|every)\s+human',  # Extreme AI claims
    ]

    for pattern in absurd_patterns:
        if re.search(pattern, option_lower):
            score -= 15.0

    # Contradiction patterns - "not X" where X is key concept
    # Extract key verbs/nouns from lesson for dynamic negation detection
    lesson_key_words = [w for w in lesson_words if len(w) >= 5][:20]  # Top key words

    for key_word in lesson_key_words:
        # Check if option negates a key concept
        negation_pattern = (
            rf"\b(?:not|don't|doesn't|won't|cannot|can't)"
            rf"\s+(?:\w+\s+)?{key_word}"
        )
        if re.search(negation_pattern, option_lower):
            score -= 10.0

    # Generic negation of action verbs
    generic_negations = [
        r'\bnot\s+(?:build|creat|develop|implement|use|learn|apply)\w*',
        r'\b(?:without|instead\s+of|rather\s+than)\s+(?:build|creat|develop|implement|use|learn)\w*',
    ]

    for pattern in generic_negations:
        if re.search(pattern, option_lower):
            score -= 8.0

    # === 4. LINGUISTIC CUES ===

    # Hedging language often appears in wrong answers
    hedging = [
        r'\bmight\s+sometimes\b',
        r'\bcould\s+potentially\b',
        r'\bpossibly\s+(?:could|might|may)\b',
        r'\bsometimes\s+(?:can|may|might)\b',
    ]

    for pattern in hedging:
        if re.search(pattern, option_lower):
            score -= 3.0

    # === 5. OUT-OF-SCOPE DETECTION ===
    # Words in option but NOT in lesson at all (suspicious)
    out_of_scope = option_words - lesson_words
    # Penalize slightly if option has many words not in lesson
    if len(option_words) > 0:
        out_of_scope_ratio = len(out_of_scope) / len(option_words)
        if out_of_scope_ratio > 0.7:  # More than 70% of words not in lesson
            score -= 5.0

    return score


@output_guardrail
async def ensure_answer_marker(
    ctx: RunContextWrapper[TeachContext],
    agent: Agent,
    output: str,
) -> GuardrailFunctionOutput:
    """
    Reject output that has A/B question but missing <!--CORRECT:X--> marker.

    Simple check per reviewer's specification.
    """
    has_question = "A)" in output and "B)" in output
    has_marker = "<!--CORRECT:" in output

    if has_question and not has_marker:
        logger.warning(f"[{ctx.context.thread_id}] Guardrail triggered: missing marker")
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=True)

    return GuardrailFunctionOutput(output_info=None, tripwire_triggered=False)


@output_guardrail
async def validate_correct_answer(
    ctx: RunContextWrapper[TeachContext],
    agent: Agent,
    output: str,
) -> GuardrailFunctionOutput:
    """
    Validate that the marked correct answer actually matches the lesson content.

    This catches cases where the LLM puts correct content in option A but marks B as correct.
    Instead of rejecting (which causes errors in streaming), we FIX the stored answer.
    """
    from ..core.redis_cache import get_redis

    # Only validate if this is a question (has options)
    if "A)" not in output or "B)" not in output:
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=False)

    # Extract options and marker
    options = _extract_options(output)
    marker = _extract_marker(output)

    if not options or not marker:
        # Can't validate, let other guardrails handle
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=False)

    option_a, option_b = options

    # Get lesson content from context
    chunk = ctx.context.current_chunk
    if not chunk:
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=False)

    lesson_content = chunk.get('content', '')

    # Score each option's relevance to lesson content
    score_a = _score_option_relevance(option_a, lesson_content)
    score_b = _score_option_relevance(option_b, lesson_content)

    logger.info(
        f"[{ctx.context.thread_id}] Answer validation: "
        f"A={score_a:.1f}, B={score_b:.1f}, marker={marker}"
    )

    # CONSERVATIVE OVERRIDE: Only override when one option is CLEARLY absurd
    # This prevents false positives where both options are reasonable
    # Condition: One option must be very negative (< -10) AND the other must be positive
    expected_correct = None

    if score_a < -10 and score_b > 0:
        # A is absurd, B should be correct
        expected_correct = "B"
    elif score_b < -10 and score_a > 0:
        # B is absurd, A should be correct
        expected_correct = "A"

    if expected_correct is None:
        # No clear absurd answer detected - trust the model
        logger.info(
            f"[{ctx.context.thread_id}] No absurd answer detected "
            f"(A={score_a:.1f}, B={score_b:.1f}), trusting model"
        )
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=False)

    # Check if marker matches expected
    if marker != expected_correct:
        logger.warning(
            f"[{ctx.context.thread_id}] ANSWER MISMATCH DETECTED! "
            f"Marker says {marker} but content analysis says {expected_correct}. "
            f"A({score_a:.1f}): '{option_a[:50]}...' | "
            f"B({score_b:.1f}): '{option_b[:50]}...' "
            f"FIXING: Overwriting Redis with correct answer {expected_correct}"
        )

        # FIX the stored answer instead of rejecting
        redis = get_redis()
        if redis:
            key = ANSWER_KEY.format(thread_id=ctx.context.thread_id)
            try:
                await redis.set(key, expected_correct, ex=3600)
                logger.info(f"[{ctx.context.thread_id}] Answer CORRECTED to {expected_correct}")
            except Exception as e:
                logger.error(f"[{ctx.context.thread_id}] Failed to correct answer: {e}")

        # Don't trigger tripwire - we fixed it
        return GuardrailFunctionOutput(output_info=None, tripwire_triggered=False)

    logger.info(f"[{ctx.context.thread_id}] Answer validation PASSED: {marker} is correct")
    return GuardrailFunctionOutput(output_info=None, tripwire_triggered=False)


# =============================================================================
# AGENT CREATION
# =============================================================================


def create_teach_agent() -> Agent:
    """Create the Socratic teaching agent with tools and guardrails."""
    return Agent(
        name="SocraticTutor",
        model="gpt-5-mini",
        instructions=teach_instructions,  # Dynamic callable
        tools=[
            verify_answer,
            advance_to_next_chunk,
            record_incorrect_attempt,
            store_correct_answer,
        ],
        output_guardrails=[
            ensure_answer_marker,      # Check marker exists
            validate_correct_answer,   # Validate marker matches content
        ],
    )
