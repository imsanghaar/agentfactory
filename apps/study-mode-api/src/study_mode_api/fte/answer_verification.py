"""Answer verification system for interactive teaching mode.

This module provides server-side verification of student answers to ensure
the LLM correctly identifies correct/incorrect responses.

Flow:
1. When agent generates a question, it includes <!--CORRECT:A--> or <!--CORRECT:B-->
2. This marker is parsed and stored in Redis with thread_id as key
3. When student sends "A" or "B", we verify against stored answer
4. We pass verification result to the LLM so it responds appropriately
"""

import logging
import re
from typing import Literal

from ..core.redis_cache import get_redis

logger = logging.getLogger(__name__)

# Pattern to extract correct answer marker from response
CORRECT_ANSWER_PATTERN = re.compile(r"<!--CORRECT:([AB])-->", re.IGNORECASE)

# Redis key prefix for storing correct answers
ANSWER_KEY_PREFIX = "teach:correct_answer:"

# TTL for stored answers (1 hour)
ANSWER_TTL_SECONDS = 3600


async def extract_and_store_correct_answer(
    thread_id: str,
    response_text: str,
) -> str | None:
    """
    Extract correct answer marker from response and store in Redis.

    If no marker is found, deletes any stale answer from previous questions
    to prevent incorrect verification of subsequent answers.

    Args:
        thread_id: The thread ID to associate the answer with
        response_text: The full response text from the agent

    Returns:
        The correct answer ("A" or "B") if found, None otherwise
    """
    key = f"{ANSWER_KEY_PREFIX}{thread_id}"
    redis = get_redis()

    match = CORRECT_ANSWER_PATTERN.search(response_text)
    if not match:
        logger.debug("[AnswerVerify] No correct answer marker found in response")
        # Delete stale answer to prevent incorrect verification
        if redis:
            try:
                await redis.delete(key)
                logger.debug(f"[AnswerVerify] Deleted stale answer for {thread_id}")
            except Exception as e:
                logger.warning(f"[AnswerVerify] Failed to delete stale answer: {e}")
        return None

    correct_answer = match.group(1).upper()

    # Store in Redis
    if not redis:
        logger.warning("[AnswerVerify] Redis not available, cannot store answer")
        return correct_answer
    try:
        await redis.set(key, correct_answer, ex=ANSWER_TTL_SECONDS)
        logger.info(f"[AnswerVerify] Stored answer '{correct_answer}' for {thread_id}")
    except Exception as e:
        logger.error(f"[AnswerVerify] Failed to store answer in Redis: {e}")

    return correct_answer


async def get_stored_correct_answer(thread_id: str) -> str | None:
    """
    Get the stored correct answer for a thread.

    Args:
        thread_id: The thread ID to look up

    Returns:
        The correct answer ("A" or "B") if found, None otherwise
    """
    key = f"{ANSWER_KEY_PREFIX}{thread_id}"
    redis = get_redis()
    if not redis:
        logger.warning("[AnswerVerify] Redis not available, cannot get answer")
        return None
    try:
        answer = await redis.get(key)
        if answer:
            # Redis returns bytes, decode to string
            if isinstance(answer, bytes):
                answer_str = answer.decode("utf-8")
            else:
                answer_str = answer
            logger.info(f"[AnswerVerify] Retrieved answer '{answer_str}' for {thread_id}")
            return answer_str
    except Exception as e:
        logger.error(f"[AnswerVerify] Failed to get answer from Redis: {e}")

    return None


async def verify_student_answer(
    thread_id: str,
    student_answer: str,
) -> Literal["correct", "incorrect", "unknown"]:
    """
    Verify if the student's answer is correct.

    Args:
        thread_id: The thread ID
        student_answer: The student's answer (can be "A", "B", "1st option", etc.)

    Returns:
        "correct" if answer matches, "incorrect" if not, "unknown" if no stored answer
    """
    correct_answer = await get_stored_correct_answer(thread_id)

    if not correct_answer:
        logger.warning(f"[AnswerVerify] No stored answer for thread {thread_id}")
        return "unknown"

    # Normalize the student's answer to A or B
    normalized = normalize_answer(student_answer)
    if not normalized:
        logger.warning(f"[AnswerVerify] Could not normalize answer: '{student_answer}'")
        return "unknown"

    if normalized == correct_answer:
        logger.info(f"[AnswerVerify] Student answered CORRECTLY ({normalized})")
        return "correct"
    else:
        logger.info(f"[AnswerVerify] INCORRECT ({normalized} != {correct_answer})")
        return "incorrect"


def strip_answer_marker(text: str) -> str:
    """
    Remove the <!--CORRECT:X--> marker from response text.

    This should be called before sending the response to the client
    so they don't see the hidden marker.

    Args:
        text: The response text that may contain the marker

    Returns:
        The text with the marker removed
    """
    return CORRECT_ANSWER_PATTERN.sub("", text).strip()


def is_answer_message(text: str) -> bool:
    """
    Check if a message is a student answer selection.

    Handles variations like: A, B, a, b, A), B), option A, 1st option, etc.

    Args:
        text: The message text

    Returns:
        True if the message is an answer selection
    """
    import re
    clean = text.strip().upper()

    # Exact match
    if clean in ("A", "B"):
        return True

    # Match A) or B) format
    if clean in ("A)", "B)"):
        return True

    # Match "option A", "option B"
    if re.match(r"^OPTION\s*[AB]$", clean):
        return True

    # Match "1st option" or "first option" -> A, "2nd option" or "second option" -> B
    if re.match(r"^(1ST|FIRST)\s*OPTION$", clean):
        return True
    if re.match(r"^(2ND|SECOND)\s*OPTION$", clean):
        return True

    return False


def normalize_answer(text: str) -> str | None:
    """
    Normalize answer text to "A" or "B".

    Enhanced parsing with word boundary matching for partial answers.
    E.g., "I think A because..." -> "A"

    Args:
        text: The message text

    Returns:
        "A" or "B" if recognizable, None otherwise
    """
    import re
    clean = text.strip().upper()

    # Exact A or B
    if clean in ("A", "B", "A)", "B)"):
        return clean[0]  # Return just A or B

    # Match "option A", "option B"
    match = re.match(r"^OPTION\s*([AB])$", clean)
    if match:
        return match.group(1)

    # Match "1st option" or "first option" -> A
    if re.match(r"^(1ST|FIRST)\s*(OPTION|ONE)?$", clean):
        return "A"

    # Match "2nd option" or "second option" -> B
    if re.match(r"^(2ND|SECOND)\s*(OPTION|ONE)?$", clean):
        return "B"

    # Word boundary match for partial answers
    # "I think A because..." → "A"
    # "My answer is B" → "B"
    word_match = re.search(r'\b([AB])\b', clean)
    if word_match:
        return word_match.group(1)

    return None


# Special request patterns for off-topic handling
HINT_PATTERNS = ["hint", "help", "confused", "don't understand", "explain", "dont understand"]
SKIP_PATTERNS = ["skip", "next", "move on", "pass"]
OPTION_CONFUSION_PATTERNS = [
    "both wrong", "both are wrong", "both options are wrong",
    "neither", "neither is correct", "neither option",
    "none of these", "none correct",
    "don't agree", "dont agree", "disagree with both"
]


def detect_special_request(text: str) -> str | None:
    """
    Detect if the message is a special request (hint, skip, option confusion).

    Args:
        text: The message text

    Returns:
        "hint", "skip", "option_confusion", or None
    """
    lower = text.lower().strip()

    # Check for hint/help requests
    for pattern in HINT_PATTERNS:
        if pattern in lower:
            return "hint"

    # Check for skip requests
    for pattern in SKIP_PATTERNS:
        if pattern in lower:
            return "skip"

    # Check for option confusion ("both wrong", "neither", etc.)
    for pattern in OPTION_CONFUSION_PATTERNS:
        if pattern in lower:
            return "option_confusion"

    return None
