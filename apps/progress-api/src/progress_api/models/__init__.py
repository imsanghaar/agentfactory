"""Models package — re-exports all models + SQLModel."""

from sqlmodel import SQLModel

from .activity import ActivityDay
from .badge import UserBadge
from .chapter import Chapter, ChapterAlias
from .lesson import LessonCompletion
from .progress import UserProgress
from .quiz import QuizAttempt
from .user import User

__all__ = [
    "SQLModel",
    "ActivityDay",
    "Chapter",
    "ChapterAlias",
    "LessonCompletion",
    "QuizAttempt",
    "User",
    "UserBadge",
    "UserProgress",
]
