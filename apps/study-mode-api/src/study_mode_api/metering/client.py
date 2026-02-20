"""HTTP client for token-metering-api."""

import logging
from typing import Any

import httpx

from ..config import settings

logger = logging.getLogger(__name__)

# Timeout for metering API calls (15 seconds - cold start includes JWKS + DB init)
METERING_TIMEOUT = 15.0


class MeteringClient:
    """
    Async HTTP client for the token-metering-api.

    Provides check/deduct/release operations for the reservation pattern.
    """

    def __init__(self, base_url: str | None = None):
        """
        Initialize the metering client.

        Args:
            base_url: Override base URL (default: from settings.metering_api_url)
        """
        self.base_url = (base_url or settings.metering_api_url).rstrip("/")
        self._client: httpx.AsyncClient | None = None

    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create the HTTP client."""
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                timeout=METERING_TIMEOUT,
            )
        return self._client

    async def close(self) -> None:
        """Close the HTTP client."""
        if self._client:
            await self._client.aclose()
            self._client = None

    async def check(
        self,
        user_id: str,
        request_id: str,
        estimated_tokens: int,
        model: str,  # Required in v5 API
        lesson_path: str | None = None,
        context: dict[str, Any] | None = None,
        auth_token: str | None = None,
    ) -> dict[str, Any]:
        """
        Pre-request balance check with reservation.

        Args:
            user_id: User ID from JWT
            request_id: Client-generated UUID for idempotency
            estimated_tokens: Estimated total tokens for the request
            model: Model name for cost calculation (required in v5)
            lesson_path: Optional lesson context (stored in context dict)
            context: Optional additional context dict

        Returns:
            dict with 'allowed', 'reservation_id', 'reserved_credits', 'expires_at'
            OR dict with 'allowed'=False and error info

        Raises:
            httpx.HTTPError: On network/connection errors
        """
        client = await self._get_client()

        payload = {
            "user_id": user_id,
            "request_id": request_id,
            "estimated_tokens": estimated_tokens,
            "model": model,  # Required in v5
        }
        # v5: lesson_path goes inside context dict, not as top-level field
        if lesson_path or context:
            merged_context = context.copy() if context else {}
            if lesson_path:
                merged_context["lesson_path"] = lesson_path
            payload["context"] = merged_context

        try:
            headers = {"X-User-ID": user_id}
            if auth_token:
                headers["Authorization"] = auth_token

            response = await client.post(
                "/api/v1/metering/check",
                json=payload,
                headers=headers,
            )

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 402:
                # v5: Payment required - insufficient balance
                body = response.json()
                return {
                    "allowed": False,
                    "error_code": body.get("error_code", "INSUFFICIENT_BALANCE"),
                    "message": body.get("message", "Balance check failed"),
                    "balance": body.get("balance", 0),
                    "available_balance": body.get("available_balance", 0),
                    "required": body.get("required", 0),
                    "is_expired": body.get("is_expired", False),
                }
            elif response.status_code == 403:
                # v5: Account suspended
                body = response.json()
                error_code = body.get("error_code") or body.get("detail", {}).get(
                    "error_code", "ACCOUNT_SUSPENDED"
                )
                message = body.get("message") or body.get("detail", {}).get(
                    "message", "Account suspended"
                )
                return {
                    "allowed": False,
                    "error_code": error_code,
                    "message": message,
                }
            elif response.status_code == 409:
                # v5: Request ID conflict
                body = response.json()
                return {
                    "allowed": False,
                    "error_code": body.get("error_code", "REQUEST_ID_CONFLICT"),
                    "message": body.get("message", "Request ID already used"),
                }
            else:
                logger.error(
                    f"[Metering] Check failed: status={response.status_code}, "
                    f"body={response.text}"
                )
                # Fail-open: return allowed on unexpected errors
                return {"allowed": True, "reservation_id": f"failopen_{request_id}"}

        except httpx.TimeoutException as e:
            logger.error(f"[Metering] Check request timeout: {type(e).__name__}")
            # Fail-open on timeout
            return {"allowed": True, "reservation_id": f"failopen_{request_id}"}
        except httpx.HTTPError as e:
            logger.error(f"[Metering] Check request failed: {type(e).__name__}: {e}")
            # Fail-open on network errors
            return {"allowed": True, "reservation_id": f"failopen_{request_id}"}

    async def deduct(
        self,
        user_id: str,
        request_id: str,
        reservation_id: str,
        input_tokens: int,
        output_tokens: int,
        model: str,
        lesson_path: str | None = None,
        thread_id: str | None = None,
        usage_details: dict[str, Any] | None = None,
        auth_token: str | None = None,
    ) -> dict[str, Any]:
        """
        Post-request token deduction (finalize reservation).

        Args:
            user_id: User ID from JWT
            request_id: Matching request_id from check
            reservation_id: Reservation ID from check response
            input_tokens: Actual input tokens used
            output_tokens: Actual output tokens used
            model: Model name used
            lesson_path: Optional lesson context
            thread_id: Optional conversation/thread identifier
            usage_details: Optional rich usage details (requests, cached_tokens, etc.)

        Returns:
            dict with transaction details

        Raises:
            httpx.HTTPError: On network/connection errors
        """
        client = await self._get_client()

        payload: dict[str, Any] = {
            "user_id": user_id,
            "request_id": request_id,
            "reservation_id": reservation_id,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "model": model,
        }
        # v5: thread_id and usage_details are top-level fields per DeductRequest schema
        if thread_id:
            payload["thread_id"] = thread_id
        if usage_details:
            payload["usage_details"] = usage_details
        # Only lesson_path goes in context
        if lesson_path:
            payload["context"] = {"lesson_path": lesson_path}

        try:
            headers = {"X-User-ID": user_id}
            if auth_token:
                headers["Authorization"] = auth_token

            response = await client.post(
                "/api/v1/metering/deduct",
                json=payload,
                headers=headers,
            )

            if response.status_code == 200:
                return response.json()
            else:
                logger.error(
                    f"[Metering] Deduct failed: status={response.status_code}, "
                    f"body={response.text}"
                )
                return {"status": "failed", "error": response.text}

        except httpx.TimeoutException as e:
            logger.error(f"[Metering] Deduct request timeout: {type(e).__name__}")
            return {"status": "failed", "error": "timeout"}
        except httpx.HTTPError as e:
            logger.error(f"[Metering] Deduct request failed: {type(e).__name__}: {e}")
            return {"status": "failed", "error": str(e)}

    async def release(
        self,
        user_id: str,
        request_id: str,
        reservation_id: str,
        auth_token: str | None = None,
    ) -> dict[str, Any]:
        """
        Cancel reservation on LLM failure.

        Args:
            user_id: User ID from JWT
            request_id: Matching request_id from check
            reservation_id: Reservation ID from check response

        Returns:
            dict with release status

        Raises:
            httpx.HTTPError: On network/connection errors
        """
        client = await self._get_client()

        payload = {
            "user_id": user_id,
            "request_id": request_id,
            "reservation_id": reservation_id,
        }

        try:
            headers = {"X-User-ID": user_id}
            if auth_token:
                headers["Authorization"] = auth_token

            response = await client.post(
                "/api/v1/metering/release",
                json=payload,
                headers=headers,
            )

            if response.status_code == 200:
                return response.json()
            else:
                logger.warning(
                    f"[Metering] Release failed: status={response.status_code}, "
                    f"body={response.text}"
                )
                return {"status": "failed", "error": response.text}

        except httpx.TimeoutException as e:
            logger.warning(f"[Metering] Release request timeout: {type(e).__name__}")
            return {"status": "failed", "error": "timeout"}
        except httpx.HTTPError as e:
            logger.warning(f"[Metering] Release request failed: {type(e).__name__}: {e}")
            return {"status": "failed", "error": str(e)}


# Module-level client instance (lazy initialization)
_client: MeteringClient | None = None


def get_metering_client() -> MeteringClient | None:
    """
    Get the global metering client instance.

    Returns None if metering is disabled.
    """
    global _client

    if not settings.metering_enabled or not settings.metering_api_url:
        return None

    if _client is None:
        _client = MeteringClient()

    return _client
