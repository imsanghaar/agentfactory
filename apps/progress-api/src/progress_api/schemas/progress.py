"""Progress dashboard request/response schemas."""

from datetime import datetime

from pydantic import BaseModel


class UserInfo(BaseModel):
    """User display info."""

    display_name: str
    avatar_url: str | None


class StatsInfo(BaseModel):
    """Aggregate stats."""

    total_xp: int
    rank: int | None = None
    quizzes_completed: int
    perfect_scores: int
    current_streak: int
    longest_streak: int
    lessons_completed: int
    badge_count: int


class BadgeInfo(BaseModel):
    """An earned badge."""

    id: str
    name: str
    earned_at: datetime


class LessonInfo(BaseModel):
    """A completed lesson within a chapter."""

    lesson_slug: str
    active_duration_secs: int | None
    completed_at: datetime


class ChapterInfo(BaseModel):
    """Chapter progress summary."""

    slug: str
    title: str
    best_score: int | None
    attempts: int
    xp_earned: int
    lessons_completed: list[LessonInfo]


class ProgressResponse(BaseModel):
    """Response body for GET /api/v1/progress/me."""

    user: UserInfo
    stats: StatsInfo
    badges: list[BadgeInfo]
    chapters: list[ChapterInfo]
