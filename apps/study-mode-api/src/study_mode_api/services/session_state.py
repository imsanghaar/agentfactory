"""
Session state management for chunked teaching mode.

Tracks student progress through lesson chunks:
- concept_index: Which chunk we're currently teaching
- attempt_count: How many attempts at current question
- last_question: The question we asked (for context on retry)
- last_student_answer: What the student said (for re-explanation)

State is stored in Redis with 24-hour TTL.
"""

import json
import logging
from typing import TypedDict

from ..core.redis_cache import get_redis

logger = logging.getLogger(__name__)

# Redis key prefix for session state
SESSION_KEY_PREFIX = "teach:session:"

# TTL for session state (24 hours)
SESSION_TTL_SECONDS = 60 * 60 * 24  # 24 hours


class TeachSessionState(TypedDict):
    """Session state for chunked teaching."""
    concept_index: int  # Which chunk we're on (0-indexed)
    attempt_count: int  # Attempts at current question
    last_question: str | None  # The question we asked
    expected_keywords: list[str]  # Keywords expected in answer
    last_student_answer: str | None  # What student said (for retry context)
    status: str  # "teaching" | "awaiting_answer" | "complete"
    total_chunks: int  # Total number of chunks in lesson
    lesson_path: str  # For validation


def create_initial_state(lesson_path: str, total_chunks: int) -> TeachSessionState:
    """Create initial session state for a new lesson."""
    return {
        "concept_index": 0,
        "attempt_count": 0,
        "last_question": None,
        "expected_keywords": [],
        "last_student_answer": None,
        "status": "teaching",
        "total_chunks": total_chunks,
        "lesson_path": lesson_path,
    }


async def get_session_state(thread_id: str) -> TeachSessionState | None:
    """
    Get session state for a thread.

    Args:
        thread_id: The thread ID

    Returns:
        Session state if exists, None otherwise
    """
    redis = get_redis()
    if not redis:
        logger.warning("[SessionState] Redis not available")
        return None

    key = f"{SESSION_KEY_PREFIX}{thread_id}"

    try:
        data = await redis.get(key)
        if data:
            if isinstance(data, bytes):
                data = data.decode("utf-8")
            state: TeachSessionState = json.loads(data)
            logger.debug(f"[SessionState] Loaded: {thread_id[:8]}, idx={state['concept_index']}")
            return state
    except Exception as e:
        logger.error(f"[SessionState] Failed to get state: {e}")

    return None


async def save_session_state(thread_id: str, state: TeachSessionState) -> bool:
    """
    Save session state for a thread.

    Args:
        thread_id: The thread ID
        state: The session state to save

    Returns:
        True if saved successfully
    """
    redis = get_redis()
    if not redis:
        logger.warning("[SessionState] Redis not available")
        return False

    key = f"{SESSION_KEY_PREFIX}{thread_id}"

    try:
        await redis.setex(key, SESSION_TTL_SECONDS, json.dumps(state))
        logger.debug(
            f"[SessionState] Saved state for {thread_id}: "
            f"index={state['concept_index']}, status={state['status']}"
        )
        return True
    except Exception as e:
        logger.error(f"[SessionState] Failed to save state: {e}")
        return False


async def advance_to_next_chunk(
    thread_id: str,
    state: TeachSessionState,
) -> TeachSessionState:
    """
    Advance to the next chunk after correct answer.

    Args:
        thread_id: The thread ID
        state: Current session state

    Returns:
        Updated session state
    """
    state["concept_index"] += 1
    state["attempt_count"] = 0
    state["last_question"] = None
    state["expected_keywords"] = []
    state["last_student_answer"] = None

    # Check if lesson is complete
    if state["concept_index"] >= state["total_chunks"]:
        state["status"] = "complete"
        logger.info(f"[SessionState] Lesson COMPLETE for {thread_id}")
    else:
        state["status"] = "teaching"
        logger.info(
            f"[SessionState] Advanced to chunk {state['concept_index']} "
            f"for {thread_id}"
        )

    await save_session_state(thread_id, state)
    return state


async def record_incorrect_attempt(
    thread_id: str,
    state: TeachSessionState,
    student_answer: str,
) -> TeachSessionState:
    """
    Record an incorrect attempt (stay on same chunk).

    Args:
        thread_id: The thread ID
        state: Current session state
        student_answer: What the student said

    Returns:
        Updated session state
    """
    state["attempt_count"] += 1
    state["last_student_answer"] = student_answer
    state["status"] = "awaiting_answer"

    logger.info(
        f"[SessionState] Incorrect attempt {state['attempt_count']} "
        f"on chunk {state['concept_index']} for {thread_id}"
    )

    await save_session_state(thread_id, state)
    return state


async def update_question_asked(
    thread_id: str,
    state: TeachSessionState,
    question: str,
    expected_keywords: list[str] | None = None,
) -> TeachSessionState:
    """
    Update state after asking a question.

    Args:
        thread_id: The thread ID
        state: Current session state
        question: The question we asked
        expected_keywords: Keywords expected in correct answer

    Returns:
        Updated session state
    """
    state["last_question"] = question
    state["expected_keywords"] = expected_keywords or []
    state["status"] = "awaiting_answer"

    await save_session_state(thread_id, state)
    return state


async def delete_session_state(thread_id: str) -> bool:
    """
    Delete session state for a thread.

    Called when lesson is complete or thread is deleted.
    """
    redis = get_redis()
    if not redis:
        return False

    key = f"{SESSION_KEY_PREFIX}{thread_id}"

    try:
        await redis.delete(key)
        logger.info(f"[SessionState] Deleted state for {thread_id}")
        return True
    except Exception as e:
        logger.warning(f"[SessionState] Failed to delete state: {e}")
        return False


async def get_or_create_session_state(
    thread_id: str,
    lesson_path: str,
    total_chunks: int,
) -> TeachSessionState:
    """
    Get existing session state or create new one.

    Args:
        thread_id: The thread ID
        lesson_path: Path to the lesson
        total_chunks: Total number of chunks

    Returns:
        Session state (existing or new)
    """
    existing = await get_session_state(thread_id)

    if existing:
        # Validate it's for the same lesson
        if existing.get("lesson_path") == lesson_path:
            return existing
        else:
            # Different lesson, start fresh
            logger.info(
                f"[SessionState] Lesson changed for {thread_id}, "
                f"resetting state"
            )

    # Create new state
    state = create_initial_state(lesson_path, total_chunks)
    await save_session_state(thread_id, state)
    return state
