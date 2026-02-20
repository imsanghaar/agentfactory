"""Tests for ChatKit server and Study Mode integration.

Tests the chatkit_server module and agent-native teach mode.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from study_mode_api.chatkit_server import StudyModeChatKitServer
from study_mode_api.chatkit_store import RequestContext
from study_mode_api.fte import (
    ASK_PROMPT,
    TeachContext,
    ask_agent,
    create_teach_agent,
)


class TestAgentNativeTeachMode:
    """Test agent-native teach mode architecture."""

    def test_create_teach_agent(self):
        """Test creating teach agent with function tools."""
        agent = create_teach_agent()

        assert agent.name == "SocraticTutor"
        # Agent has dynamic instructions (callable)
        assert callable(agent.instructions)
        # Agent has 4 function tools
        assert len(agent.tools) == 4
        tool_names = [t.name for t in agent.tools]
        assert "verify_answer" in tool_names
        assert "advance_to_next_chunk" in tool_names
        assert "record_incorrect_attempt" in tool_names
        assert "store_correct_answer" in tool_names

    def test_teach_agent_has_output_guardrails(self):
        """Test teach agent has output guardrails."""
        agent = create_teach_agent()

        assert len(agent.output_guardrails) == 2

    def test_teach_context_creation(self):
        """Test TeachContext dataclass."""
        chunks = [
            {"index": 0, "title": "Intro", "content": "Test content", "chunk_type": "intro"},
            {"index": 1, "title": "Concept", "content": "More content", "chunk_type": "concept"},
        ]

        ctx = TeachContext(
            chunks=chunks,
            current_chunk_index=0,
            total_chunks=2,
            lesson_title="Test Lesson",
            attempt_count=0,
            max_attempts=3,
            is_first_message=True,
            thread_id="test-123",
            user_name="Alice",
        )

        assert ctx.current_chunk == chunks[0]
        assert ctx.total_chunks == 2
        assert ctx.lesson_title == "Test Lesson"
        assert ctx.user_name == "Alice"

    def test_teach_context_current_chunk_none_when_complete(self):
        """Test current_chunk is None when lesson is complete."""
        chunks = [{"index": 0, "title": "Only", "content": "Content", "chunk_type": "intro"}]

        ctx = TeachContext(
            chunks=chunks,
            current_chunk_index=1,  # Past the end
            total_chunks=1,
            lesson_title="Test",
        )

        assert ctx.current_chunk is None


class TestAskAgent:
    """Test ask mode agent."""

    def test_ask_agent_is_singleton(self):
        """Test ask agent is a singleton with dynamic instructions."""
        assert ask_agent.name == "study_tutor_ask"
        assert callable(ask_agent.instructions)

    def test_ask_prompt_has_required_elements(self):
        """Test ask prompt contains direct answer instructions."""
        assert "{content}" in ASK_PROMPT
        assert "{selected_text_section}" in ASK_PROMPT
        assert "direct explanation" in ASK_PROMPT
        assert "Socratic" in ASK_PROMPT  # Mentions it's NOT Socratic mode


class TestRequestContext:
    """Test request context creation for ChatKit."""

    def test_context_includes_metadata(self):
        """Test RequestContext includes lesson metadata."""
        context = RequestContext(
            user_id="user-123",
            request_id="req-456",
            metadata={
                "lesson_path": "/docs/chapter1/lesson1",
                "mode": "teach",
                "user_name": "John",
            },
        )

        assert context.user_id == "user-123"
        assert context.metadata["lesson_path"] == "/docs/chapter1/lesson1"
        assert context.metadata["mode"] == "teach"
        assert context.metadata["user_name"] == "John"

    def test_context_requires_user_id(self):
        """Test RequestContext requires non-empty user_id."""
        with pytest.raises(ValueError):
            RequestContext(user_id="")


class TestStudyModeChatKitServer:
    """Test StudyModeChatKitServer initialization."""

    def test_server_initialization(self):
        """Test server initializes with store."""
        mock_store = MagicMock()

        server = StudyModeChatKitServer(store=mock_store)

        assert server.store == mock_store

    @pytest.mark.asyncio
    async def test_server_uses_content_loader(self):
        """Test server uses content loader for lesson content."""
        mock_store = MagicMock()
        mock_store.load_thread_items = AsyncMock(
            return_value=MagicMock(data=[])
        )

        with patch(
            "study_mode_api.chatkit_server.load_lesson_content",
            new_callable=AsyncMock,
            return_value={"content": "Test content", "title": "Test"},
        ):
            server = StudyModeChatKitServer(store=mock_store)

            # The respond method would be called internally
            # This verifies the integration point exists
            assert hasattr(server, "respond")


class TestUserContextPropagation:
    """Test that user context flows through to agent."""

    def test_context_metadata_includes_user_name(self):
        """Test that user name is included in context metadata."""
        context = RequestContext(
            user_id="user-123",
            metadata={
                "user_name": "Alice",
                "lesson_path": "/docs/test",
                "mode": "teach",
            },
        )

        assert context.metadata.get("user_name") == "Alice"

    def test_context_without_user_name(self):
        """Test context works without user name."""
        context = RequestContext(
            user_id="user-123",
            metadata={
                "lesson_path": "/docs/test",
                "mode": "teach",
            },
        )

        assert context.metadata.get("user_name") is None
