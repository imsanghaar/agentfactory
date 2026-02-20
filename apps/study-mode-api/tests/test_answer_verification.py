"""Tests for the answer verification module."""

from unittest.mock import AsyncMock, patch

import pytest

from study_mode_api.fte.answer_verification import (
    ANSWER_KEY_PREFIX,
    ANSWER_TTL_SECONDS,
    extract_and_store_correct_answer,
    get_stored_correct_answer,
    is_answer_message,
    normalize_answer,
    strip_answer_marker,
    verify_student_answer,
)


class TestStripAnswerMarker:
    """Tests for strip_answer_marker function."""

    def test_strips_correct_a_marker(self):
        """Should strip <!--CORRECT:A--> marker."""
        text = "What is 2+2? A) 4 B) 5 <!--CORRECT:A-->"
        result = strip_answer_marker(text)
        assert result == "What is 2+2? A) 4 B) 5"

    def test_strips_correct_b_marker(self):
        """Should strip <!--CORRECT:B--> marker."""
        text = "What is Python? A) Snake B) Language <!--CORRECT:B-->"
        result = strip_answer_marker(text)
        assert result == "What is Python? A) Snake B) Language"

    def test_strips_lowercase_marker(self):
        """Should strip lowercase marker (case insensitive)."""
        text = "Question <!--correct:a-->"
        result = strip_answer_marker(text)
        assert result == "Question"

    def test_no_marker_returns_original(self):
        """Should return original text if no marker present."""
        text = "Just a normal message"
        result = strip_answer_marker(text)
        assert result == "Just a normal message"

    def test_strips_marker_in_middle(self):
        """Should strip marker even if in middle of text."""
        text = "Before <!--CORRECT:A--> After"
        result = strip_answer_marker(text)
        assert result == "Before  After"

    def test_empty_string(self):
        """Should handle empty string."""
        result = strip_answer_marker("")
        assert result == ""


class TestIsAnswerMessage:
    """Tests for is_answer_message function."""

    def test_exact_a(self):
        """Should recognize 'A' as answer."""
        assert is_answer_message("A") is True

    def test_exact_b(self):
        """Should recognize 'B' as answer."""
        assert is_answer_message("B") is True

    def test_lowercase_a(self):
        """Should recognize lowercase 'a'."""
        assert is_answer_message("a") is True

    def test_lowercase_b(self):
        """Should recognize lowercase 'b'."""
        assert is_answer_message("b") is True

    def test_with_parenthesis(self):
        """Should recognize 'A)' format."""
        assert is_answer_message("A)") is True
        assert is_answer_message("B)") is True

    def test_option_a(self):
        """Should recognize 'option A' format."""
        assert is_answer_message("option A") is True
        assert is_answer_message("Option B") is True
        assert is_answer_message("OPTION A") is True

    def test_first_option(self):
        """Should recognize 'first option' as A."""
        assert is_answer_message("first option") is True
        assert is_answer_message("1st option") is True

    def test_second_option(self):
        """Should recognize 'second option' as B."""
        assert is_answer_message("second option") is True
        assert is_answer_message("2nd option") is True

    def test_with_whitespace(self):
        """Should handle leading/trailing whitespace."""
        assert is_answer_message("  A  ") is True
        assert is_answer_message("\nB\n") is True

    def test_not_answer_c(self):
        """Should not recognize 'C' as answer."""
        assert is_answer_message("C") is False

    def test_not_answer_sentence(self):
        """Should not recognize full sentences."""
        assert is_answer_message("I think A is correct") is False
        assert is_answer_message("The answer is B") is False

    def test_empty_string(self):
        """Should return False for empty string."""
        assert is_answer_message("") is False


class TestNormalizeAnswer:
    """Tests for normalize_answer function."""

    def test_normalize_a(self):
        """Should normalize 'A' to 'A'."""
        assert normalize_answer("A") == "A"
        assert normalize_answer("a") == "A"
        assert normalize_answer("A)") == "A"

    def test_normalize_b(self):
        """Should normalize 'B' to 'B'."""
        assert normalize_answer("B") == "B"
        assert normalize_answer("b") == "B"
        assert normalize_answer("B)") == "B"

    def test_normalize_option_format(self):
        """Should normalize 'option X' format."""
        assert normalize_answer("option A") == "A"
        assert normalize_answer("Option B") == "B"

    def test_normalize_first_second(self):
        """Should normalize ordinal formats."""
        assert normalize_answer("first option") == "A"
        assert normalize_answer("1st option") == "A"
        assert normalize_answer("second option") == "B"
        assert normalize_answer("2nd option") == "B"

    def test_partial_answer_extraction(self):
        """Should extract A/B from partial answers (enhanced parsing)."""
        assert normalize_answer("I think A") == "A"
        assert normalize_answer("I think B because...") == "B"
        assert normalize_answer("My answer is A") == "A"

    def test_invalid_returns_none(self):
        """Should return None for unrecognized formats."""
        assert normalize_answer("C") is None
        assert normalize_answer("hello") is None
        assert normalize_answer("I don't know") is None

    def test_empty_returns_none(self):
        """Should return None for empty string."""
        assert normalize_answer("") is None


class TestExtractAndStoreCorrectAnswer:
    """Tests for extract_and_store_correct_answer function."""

    @pytest.fixture
    def mock_redis(self):
        """Create a mock Redis client."""
        return AsyncMock()

    @patch("study_mode_api.fte.answer_verification.get_redis")
    async def test_extracts_and_stores_answer_a(self, mock_get_redis, mock_redis):
        """Should extract A and store in Redis."""
        mock_get_redis.return_value = mock_redis

        result = await extract_and_store_correct_answer(
            "thread-123",
            "What is 2+2? A) 4 B) 5 <!--CORRECT:A-->"
        )

        assert result == "A"
        mock_redis.set.assert_called_once_with(
            f"{ANSWER_KEY_PREFIX}thread-123",
            "A",
            ex=ANSWER_TTL_SECONDS
        )

    @patch("study_mode_api.fte.answer_verification.get_redis")
    async def test_extracts_and_stores_answer_b(self, mock_get_redis, mock_redis):
        """Should extract B and store in Redis."""
        mock_get_redis.return_value = mock_redis

        result = await extract_and_store_correct_answer(
            "thread-456",
            "Question <!--CORRECT:B-->"
        )

        assert result == "B"
        mock_redis.set.assert_called_once()

    @patch("study_mode_api.fte.answer_verification.get_redis")
    async def test_no_marker_returns_none_and_deletes_stale(self, mock_get_redis, mock_redis):
        """Should return None and delete stale key when no marker found."""
        mock_get_redis.return_value = mock_redis

        result = await extract_and_store_correct_answer(
            "thread-789",
            "Just a normal response without markers"
        )

        assert result is None
        mock_redis.delete.assert_called_once_with(f"{ANSWER_KEY_PREFIX}thread-789")

    @patch("study_mode_api.fte.answer_verification.get_redis")
    async def test_redis_unavailable_still_returns_answer(self, mock_get_redis):
        """Should return extracted answer even if Redis unavailable."""
        mock_get_redis.return_value = None

        result = await extract_and_store_correct_answer(
            "thread-000",
            "Question <!--CORRECT:A-->"
        )

        assert result == "A"

    @patch("study_mode_api.fte.answer_verification.get_redis")
    async def test_redis_error_handled_gracefully(self, mock_get_redis, mock_redis):
        """Should handle Redis errors gracefully."""
        mock_get_redis.return_value = mock_redis
        mock_redis.set.side_effect = Exception("Redis connection error")

        result = await extract_and_store_correct_answer(
            "thread-err",
            "Question <!--CORRECT:A-->"
        )

        # Should still return the extracted answer
        assert result == "A"


class TestGetStoredCorrectAnswer:
    """Tests for get_stored_correct_answer function."""

    @patch("study_mode_api.fte.answer_verification.get_redis")
    async def test_returns_stored_answer(self, mock_get_redis):
        """Should return stored answer from Redis."""
        mock_redis = AsyncMock()
        mock_redis.get.return_value = b"A"
        mock_get_redis.return_value = mock_redis

        result = await get_stored_correct_answer("thread-123")

        assert result == "A"
        mock_redis.get.assert_called_once_with(f"{ANSWER_KEY_PREFIX}thread-123")

    @patch("study_mode_api.fte.answer_verification.get_redis")
    async def test_returns_string_answer(self, mock_get_redis):
        """Should handle string return value from Redis."""
        mock_redis = AsyncMock()
        mock_redis.get.return_value = "B"
        mock_get_redis.return_value = mock_redis

        result = await get_stored_correct_answer("thread-456")

        assert result == "B"

    @patch("study_mode_api.fte.answer_verification.get_redis")
    async def test_returns_none_when_not_found(self, mock_get_redis):
        """Should return None when no answer stored."""
        mock_redis = AsyncMock()
        mock_redis.get.return_value = None
        mock_get_redis.return_value = mock_redis

        result = await get_stored_correct_answer("thread-new")

        assert result is None

    @patch("study_mode_api.fte.answer_verification.get_redis")
    async def test_returns_none_when_redis_unavailable(self, mock_get_redis):
        """Should return None when Redis unavailable."""
        mock_get_redis.return_value = None

        result = await get_stored_correct_answer("thread-123")

        assert result is None

    @patch("study_mode_api.fte.answer_verification.get_redis")
    async def test_handles_redis_error(self, mock_get_redis):
        """Should return None on Redis error."""
        mock_redis = AsyncMock()
        mock_redis.get.side_effect = Exception("Connection error")
        mock_get_redis.return_value = mock_redis

        result = await get_stored_correct_answer("thread-err")

        assert result is None


class TestVerifyStudentAnswer:
    """Tests for verify_student_answer function."""

    @patch("study_mode_api.fte.answer_verification.get_stored_correct_answer")
    async def test_correct_answer(self, mock_get_stored):
        """Should return 'correct' when answer matches."""
        mock_get_stored.return_value = "A"

        result = await verify_student_answer("thread-123", "A")

        assert result == "correct"

    @patch("study_mode_api.fte.answer_verification.get_stored_correct_answer")
    async def test_incorrect_answer(self, mock_get_stored):
        """Should return 'incorrect' when answer doesn't match."""
        mock_get_stored.return_value = "A"

        result = await verify_student_answer("thread-123", "B")

        assert result == "incorrect"

    @patch("study_mode_api.fte.answer_verification.get_stored_correct_answer")
    async def test_unknown_when_no_stored_answer(self, mock_get_stored):
        """Should return 'unknown' when no stored answer."""
        mock_get_stored.return_value = None

        result = await verify_student_answer("thread-new", "A")

        assert result == "unknown"

    @patch("study_mode_api.fte.answer_verification.get_stored_correct_answer")
    async def test_normalizes_student_answer(self, mock_get_stored):
        """Should normalize student answer before comparing."""
        mock_get_stored.return_value = "B"

        # All these should be normalized to "B" and match
        assert await verify_student_answer("t", "b") == "correct"
        assert await verify_student_answer("t", "B)") == "correct"
        assert await verify_student_answer("t", "option B") == "correct"
        assert await verify_student_answer("t", "second option") == "correct"

    @patch("study_mode_api.fte.answer_verification.get_stored_correct_answer")
    async def test_unknown_for_unnormalizable_answer(self, mock_get_stored):
        """Should return 'unknown' if answer can't be normalized."""
        mock_get_stored.return_value = "A"

        result = await verify_student_answer("thread-123", "hello world")

        assert result == "unknown"
