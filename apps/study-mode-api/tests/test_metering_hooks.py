"""Unit tests for MeteringHooks integration."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException

from study_mode_api.metering.client import MeteringClient
from study_mode_api.metering.hooks import MeteringHooks, create_metering_hooks


class MockUsage:
    """Mock OpenAI Agents SDK Usage object."""

    def __init__(
        self,
        requests=1,
        input_tokens=500,
        output_tokens=300,
        total_tokens=800,
    ):
        self.requests = requests
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens
        self.input_tokens_details = MagicMock(cached_tokens=0)
        self.output_tokens_details = MagicMock(reasoning_tokens=0)


class MockRequestContext:
    """Mock ChatKit RequestContext."""

    def __init__(self, user_id="test-user"):
        self.user_id = user_id
        self.metadata = {}


class MockThread:
    """Mock ChatKit thread."""

    def __init__(self, thread_id="thread-123"):
        self.id = thread_id


class MockAgentContext:
    """Mock ChatKit AgentContext."""

    def __init__(self, user_id="test-user", thread_id="thread-123"):
        self.request_context = MockRequestContext(user_id)
        self.thread = MockThread(thread_id)


class MockHookContext:
    """Mock AgentHookContext with usage tracking."""

    def __init__(self, user_id="test-user", thread_id="thread-123"):
        self.context = MockAgentContext(user_id, thread_id)
        self.usage = MockUsage()


class MockAgent:
    """Mock Agent."""

    def __init__(self, model="deepseek-chat"):
        self.model = model


class TestMeteringHooksOnAgentStart:
    """Test on_agent_start hook behavior."""

    @pytest.mark.asyncio
    async def test_check_called_on_agent_start(self):
        """Verify /check is called when agent starts."""
        client = MagicMock(spec=MeteringClient)
        client.check = AsyncMock(
            return_value={
                "allowed": True,
                "reservation_id": "res_test123",
            }
        )

        hooks = MeteringHooks(client)
        context = MockHookContext(user_id="user-1")
        agent = MockAgent()

        await hooks.on_agent_start(context, agent)

        # Verify check was called with correct arguments
        client.check.assert_called_once()
        call_kwargs = client.check.call_args.kwargs
        assert call_kwargs["user_id"] == "user-1"
        assert "request_id" in call_kwargs

        # Verify reservation stored
        request_id = context.context.request_context.metadata["request_id"]
        assert request_id in hooks._reservations

    @pytest.mark.asyncio
    async def test_raises_402_when_blocked(self):
        """Verify HTTPException(402) raised when user is blocked."""
        client = MagicMock(spec=MeteringClient)
        # v5 format: error_code, balance, available_balance, required, is_expired
        client.check = AsyncMock(
            return_value={
                "allowed": False,
                "error_code": "INSUFFICIENT_BALANCE",
                "message": "Insufficient balance to complete request",
                "balance": 0,
                "available_balance": 0,
                "required": 5000,
                "is_expired": False,
            }
        )

        hooks = MeteringHooks(client)
        context = MockHookContext(user_id="blocked-user")
        agent = MockAgent()

        with pytest.raises(HTTPException) as exc_info:
            await hooks.on_agent_start(context, agent)

        assert exc_info.value.status_code == 402
        assert exc_info.value.detail["error_code"] == "INSUFFICIENT_BALANCE"
        assert exc_info.value.detail["balance"] == 0
        assert exc_info.value.detail["required"] == 5000

    @pytest.mark.asyncio
    async def test_failopen_on_network_error(self):
        """Verify fail-open behavior when metering API is unavailable."""
        client = MagicMock(spec=MeteringClient)
        # Return fail-open reservation on error
        client.check = AsyncMock(
            return_value={"allowed": True, "reservation_id": "failopen_abc"}
        )

        hooks = MeteringHooks(client)
        context = MockHookContext(user_id="user-failopen")
        agent = MockAgent()

        # Should not raise
        await hooks.on_agent_start(context, agent)

        # Should store failopen reservation
        request_id = context.context.request_context.metadata["request_id"]
        assert hooks._reservations[request_id] == "failopen_abc"


class TestMeteringHooksOnAgentEnd:
    """Test on_agent_end hook behavior."""

    @pytest.mark.asyncio
    async def test_deduct_called_on_agent_end(self):
        """Verify /deduct is called with correct usage when agent ends."""
        client = MagicMock(spec=MeteringClient)
        client.check = AsyncMock(
            return_value={"allowed": True, "reservation_id": "res_test123"}
        )
        client.deduct = AsyncMock(
            return_value={"status": "finalized", "transaction_id": 12345}
        )

        hooks = MeteringHooks(client)
        context = MockHookContext(user_id="user-1", thread_id="thread-abc")
        context.usage = MockUsage(
            requests=2,
            input_tokens=1000,
            output_tokens=500,
            total_tokens=1500,
        )
        agent = MockAgent(model="gpt-5-nano")

        # First call on_agent_start to create reservation
        await hooks.on_agent_start(context, agent)
        request_id = context.context.request_context.metadata["request_id"]

        # Now call on_agent_end
        await hooks.on_agent_end(context, agent, output="test output")

        # Verify deduct was called with correct arguments
        client.deduct.assert_called_once()
        call_kwargs = client.deduct.call_args.kwargs
        assert call_kwargs["user_id"] == "user-1"
        assert call_kwargs["request_id"] == request_id
        assert call_kwargs["input_tokens"] == 1000
        assert call_kwargs["output_tokens"] == 500
        assert call_kwargs["thread_id"] == "thread-abc"
        assert "usage_details" in call_kwargs
        assert call_kwargs["usage_details"]["requests"] == 2

        # Verify reservation was removed
        assert request_id not in hooks._reservations

    @pytest.mark.asyncio
    async def test_no_deduct_without_reservation(self):
        """Verify no deduct call if no reservation exists."""
        client = MagicMock(spec=MeteringClient)
        client.deduct = AsyncMock()

        hooks = MeteringHooks(client)
        context = MockHookContext(user_id="user-1")
        # Set request_id but don't create reservation
        context.context.request_context.metadata["request_id"] = "orphan-req"
        agent = MockAgent()

        await hooks.on_agent_end(context, agent, output="test")

        # Deduct should not be called
        client.deduct.assert_not_called()


class TestMeteringHooksReleaseOnError:
    """Test release_on_error method."""

    @pytest.mark.asyncio
    async def test_release_called_on_error(self):
        """Verify /release is called when agent errors."""
        client = MagicMock(spec=MeteringClient)
        client.check = AsyncMock(
            return_value={"allowed": True, "reservation_id": "res_error"}
        )
        client.release = AsyncMock(
            return_value={"status": "released", "reserved_tokens": 5000}
        )

        hooks = MeteringHooks(client)
        context = MockHookContext(user_id="user-error")
        agent = MockAgent()

        # Create reservation
        await hooks.on_agent_start(context, agent)
        request_id = context.context.request_context.metadata["request_id"]

        # Call release on error
        await hooks.release_on_error(context)

        # Verify release was called
        client.release.assert_called_once()
        call_kwargs = client.release.call_args.kwargs
        assert call_kwargs["user_id"] == "user-error"
        assert call_kwargs["request_id"] == request_id
        assert call_kwargs["reservation_id"] == "res_error"

        # Verify reservation was removed
        assert request_id not in hooks._reservations


class TestCreateMeteringHooks:
    """Test create_metering_hooks factory function."""

    def test_returns_none_when_disabled(self):
        """Verify returns None when metering is disabled."""
        with patch(
            "study_mode_api.metering.hooks.get_metering_client", return_value=None
        ):
            result = create_metering_hooks()
            assert result is None

    def test_returns_hooks_when_enabled(self):
        """Verify returns MeteringHooks when metering is enabled."""
        mock_client = MagicMock(spec=MeteringClient)

        with patch(
            "study_mode_api.metering.hooks.get_metering_client",
            return_value=mock_client,
        ):
            result = create_metering_hooks()
            assert isinstance(result, MeteringHooks)
            assert result.client is mock_client
