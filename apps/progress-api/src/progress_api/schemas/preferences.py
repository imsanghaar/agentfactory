"""User preferences request/response schemas."""

from pydantic import BaseModel


class PreferencesUpdateRequest(BaseModel):
    """Request body for PATCH /api/v1/progress/me/preferences."""

    show_on_leaderboard: bool


class PreferencesResponse(BaseModel):
    """Response body for PATCH /api/v1/progress/me/preferences."""

    show_on_leaderboard: bool
