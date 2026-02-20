"""OpenAI Agents SDK lifecycle hooks for token metering."""

import logging
from typing import Any
from uuid import uuid4

from agents import Agent, RunHooks
from agents.run_context import AgentHookContext
from chatkit.agents import AgentContext
from fastapi import HTTPException

from ..config import settings
from .client import MeteringClient, get_metering_client

logger = logging.getLogger(__name__)

# Token estimation constants
TOKENS_PER_WORD = 1  # Simple 1:1 for now; swap for tokenizer later
OUTPUT_BUFFER = 800  # Expected output tokens (typical teaching response)
MIN_ESTIMATE = 500  # Floor — never estimate below this


def estimate_tokens_from_context(
    metadata: dict[str, Any],
    agent: Agent[Any],
) -> int:
    """Estimate total tokens from available context (input + expected output).

    Counts words in lesson content and agent instructions, converts to tokens,
    adds an output buffer. Falls back to static default if no content available.
    """
    word_count = 0

    # Lesson content (usually the largest component)
    lesson_content = metadata.get("lesson_content", "")
    if lesson_content:
        word_count += len(lesson_content.split())

    # Agent instructions (system prompt)
    raw = getattr(agent, "instructions", None)
    instructions = raw if isinstance(raw, str) else ""
    if instructions:
        word_count += len(instructions.split())

    if word_count == 0:
        return settings.metering_default_estimate

    input_tokens = int(word_count * TOKENS_PER_WORD)
    total = input_tokens + OUTPUT_BUFFER
    return max(total, MIN_ESTIMATE)


class MeteringHooks(RunHooks[AgentContext]):
    """
    Lifecycle hooks for token metering using SDK's native Usage tracking.

    Integrates with the reservation pattern:
    - on_agent_start: Reserve tokens (POST /check)
    - on_agent_end: Finalize with actual usage (POST /deduct)
    - release_on_error: Cancel reservation if agent fails (POST /release)

    Note: The SDK's RunHooks does NOT have an on_error hook. Error handling
    must be done via try/except wrapper around Runner.run().
    """

    def __init__(self, client: MeteringClient):
        """
        Initialize metering hooks.

        Args:
            client: MeteringClient instance for API calls
        """
        self.client = client
        # Track reservations per request: request_id -> reservation_id
        self._reservations: dict[str, str] = {}

    async def on_agent_start(
        self,
        context: AgentHookContext[AgentContext],
        agent: Agent[AgentContext],
    ) -> None:
        """
        Check balance and create reservation before agent runs.

        Raises HTTPException(402) if user has insufficient balance/trial.
        """
        try:
            # Extract request context
            agent_ctx = context.context
            req_ctx = agent_ctx.request_context

            user_id = req_ctx.user_id
            # Generate or use existing request_id
            request_id = req_ctx.metadata.get("request_id") or str(uuid4())
            req_ctx.metadata["request_id"] = request_id  # Store for on_agent_end

            lesson_path = req_ctx.metadata.get("lesson_path")
            auth_token = req_ctx.metadata.get("auth_token")

            logger.info(
                f"[Metering] on_agent_start: user={user_id}, request={request_id}"
            )

            estimated = estimate_tokens_from_context(req_ctx.metadata, agent)
            logger.info(f"[Metering] Estimated tokens: {estimated}")

            result = await self.client.check(
                user_id=user_id,
                request_id=request_id,
                estimated_tokens=estimated,
                model=agent.model if isinstance(agent.model, str) else "deepseek-chat",
                lesson_path=lesson_path,
                auth_token=auth_token,
            )

            if not result.get("allowed"):
                error_code = result.get("error_code", "INSUFFICIENT_BALANCE")
                logger.warning(
                    f"[Metering] Blocked: user={user_id}, error_code={error_code}"
                )
                raise HTTPException(
                    status_code=402,
                    detail={
                        "error_code": error_code,
                        "message": result.get("message", "Insufficient balance"),
                        "balance": result.get("balance", 0),
                        "available_balance": result.get("available_balance", 0),
                        "required": result.get("required", 0),
                        "is_expired": result.get("is_expired", False),
                    },
                )

            # Store reservation for on_agent_end
            reservation_id = result.get("reservation_id", f"failopen_{request_id}")
            self._reservations[request_id] = reservation_id

            logger.info(
                f"[Metering] Reserved: user={user_id}, reservation={reservation_id}"
            )

        except HTTPException:
            raise  # Re-raise 402 errors
        except Exception as e:
            # Log but don't block on metering errors (fail-open)
            logger.error(f"[Metering] on_agent_start error (fail-open): {e}")

    async def on_agent_end(
        self,
        context: AgentHookContext[AgentContext],
        agent: Agent[AgentContext],
        output: Any,
    ) -> None:
        """
        Deduct actual tokens using SDK's rich Usage object.

        Called after agent completes successfully.
        """
        try:
            agent_ctx = context.context
            req_ctx = agent_ctx.request_context

            user_id = req_ctx.user_id
            request_id = req_ctx.metadata.get("request_id")
            thread_id = agent_ctx.thread.id if agent_ctx.thread else None
            lesson_path = req_ctx.metadata.get("lesson_path")
            auth_token = req_ctx.metadata.get("auth_token")

            if not request_id:
                logger.warning("[Metering] No request_id in on_agent_end, skipping")
                return

            reservation_id = self._reservations.pop(request_id, None)
            if not reservation_id:
                logger.warning(
                    f"[Metering] No reservation found for request={request_id}"
                )
                return

            # Get usage from context (SDK tracks this automatically)
            usage = context.usage

            logger.info(
                f"[Metering] on_agent_end: user={user_id}, "
                f"input={usage.input_tokens}, output={usage.output_tokens}, "
                f"requests={usage.requests}"
            )

            # Build rich usage details
            usage_details = {
                "requests": usage.requests,
                "total_tokens": usage.total_tokens,
                "cached_tokens": (
                    usage.input_tokens_details.cached_tokens
                    if usage.input_tokens_details
                    else 0
                ),
                "reasoning_tokens": (
                    usage.output_tokens_details.reasoning_tokens
                    if usage.output_tokens_details
                    else 0
                ),
            }

            # Determine model name
            model_name = (
                agent.model if isinstance(agent.model, str) else "deepseek-chat"
            )

            result = await self.client.deduct(
                user_id=user_id,
                request_id=request_id,
                reservation_id=reservation_id,
                input_tokens=usage.input_tokens,
                output_tokens=usage.output_tokens,
                model=model_name,
                lesson_path=lesson_path,
                thread_id=thread_id,
                usage_details=usage_details,
                auth_token=auth_token,
            )

            logger.info(
                f"[Metering] Finalized: user={user_id}, "
                f"transaction={result.get('transaction_id')}, "
                f"status={result.get('status')}"
            )

        except Exception as e:
            # Log but don't fail the request on metering errors
            logger.error(f"[Metering] on_agent_end error: {e}")

    async def release_on_error(
        self,
        context: AgentContext | AgentHookContext[AgentContext],
    ) -> None:
        """
        Release reservation when agent errors out.

        This must be called manually from a try/except wrapper around Runner.run()
        since the SDK does not have an on_error hook.

        Accepts either AgentContext directly or AgentHookContext wrapper.
        """
        try:
            # Handle both AgentContext and AgentHookContext
            if hasattr(context, "context"):
                # It's AgentHookContext - unwrap it
                agent_ctx = context.context
            else:
                # It's AgentContext directly
                agent_ctx = context
            req_ctx = agent_ctx.request_context

            user_id = req_ctx.user_id
            request_id = req_ctx.metadata.get("request_id")
            auth_token = req_ctx.metadata.get("auth_token")

            if not request_id:
                return

            reservation_id = self._reservations.pop(request_id, None)
            if not reservation_id:
                return

            logger.info(
                f"[Metering] Releasing reservation on error: "
                f"user={user_id}, reservation={reservation_id}"
            )

            await self.client.release(
                user_id=user_id,
                request_id=request_id,
                reservation_id=reservation_id,
                auth_token=auth_token,
            )

        except Exception as e:
            logger.error(f"[Metering] release_on_error failed: {e}")


def create_metering_hooks() -> MeteringHooks | None:
    """
    Create metering hooks if metering is enabled.

    Returns:
        MeteringHooks instance if metering is enabled, None otherwise
    """
    client = get_metering_client()
    if client is None:
        return None

    return MeteringHooks(client)
