"""Leaderboard request/response schemas."""

from pydantic import BaseModel


class LeaderboardEntry(BaseModel):
    """A single leaderboard entry."""

    rank: int
    user_id: str
    display_name: str
    avatar_url: str | None
    total_xp: int
    badge_count: int
    badge_ids: list[str] = []


class LeaderboardResponse(BaseModel):
    """Response body for GET /api/v1/leaderboard."""

    entries: list[LeaderboardEntry]
    current_user_rank: int | None = None
    total_users: int
