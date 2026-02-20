"""Custom exceptions for unified error response format."""

from typing import Any


class MeteringAPIException(Exception):
    """Custom exception for consistent error response format.

    All error responses follow the same structure:
    {
        "error_code": "ERROR_CODE",
        "message": "Human-readable message",
        ...extra fields
    }

    Usage:
        raise MeteringAPIException(
            status_code=403,
            error_code="USER_MISMATCH",
            message="user_id doesn't match JWT",
        )

        raise MeteringAPIException(
            status_code=404,
            error_code="NOT_FOUND",
            message="Account not found",
            user_id="user-123",  # extra field
        )
    """

    def __init__(
        self,
        status_code: int,
        error_code: str,
        message: str,
        **extra: Any,
    ) -> None:
        self.status_code = status_code
        self.error_code = error_code
        self.message = message
        self.extra = extra
        super().__init__(message)
