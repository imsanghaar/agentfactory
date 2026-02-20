"""Quiz submit request/response schemas."""

from datetime import datetime

from pydantic import BaseModel, Field


class QuizSubmitRequest(BaseModel):
    """Request body for POST /api/v1/quiz/submit."""

    chapter_slug: str = Field(min_length=1)
    score_pct: int = Field(ge=0, le=100)
    questions_correct: int = Field(ge=0)
    questions_total: int = Field(ge=1)
    duration_secs: int | None = Field(default=None, ge=0)


class BadgeEarned(BaseModel):
    """A badge earned in this submission."""

    id: str
    name: str
    earned_at: datetime


class StreakInfo(BaseModel):
    """Current streak information."""

    current: int
    longest: int


class QuizSubmitResponse(BaseModel):
    """Response body for POST /api/v1/quiz/submit."""

    xp_earned: int
    total_xp: int
    attempt_number: int
    best_score: int
    new_badges: list[BadgeEarned]
    streak: StreakInfo
