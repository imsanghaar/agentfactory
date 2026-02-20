"""Lesson complete request/response schemas."""

from pydantic import BaseModel, Field

from .quiz import StreakInfo


class LessonCompleteRequest(BaseModel):
    """Request body for POST /api/v1/lesson/complete."""

    chapter_slug: str = Field(min_length=1)
    lesson_slug: str = Field(min_length=1)
    active_duration_secs: int | None = Field(default=None, ge=0)


class LessonCompleteResponse(BaseModel):
    """Response body for POST /api/v1/lesson/complete."""

    completed: bool
    active_duration_secs: int | None
    streak: StreakInfo
    already_completed: bool
    xp_earned: int = 0
