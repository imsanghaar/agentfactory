"""Custom exceptions for unified error response format."""

from typing import Any


class ProgressAPIException(Exception):
    """Custom exception for consistent error response format.

    All error responses follow the same structure:
    {
        "error_code": "ERROR_CODE",
        "message": "Human-readable message",
        ...extra fields
    }
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
