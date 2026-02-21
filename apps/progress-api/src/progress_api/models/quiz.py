"""QuizAttempt model."""

from datetime import datetime, timezone
from typing import Optional

import sqlalchemy as sa
from sqlmodel import Column, DateTime, Field, Relationship, SQLModel, func


class QuizAttempt(SQLModel, table=True):
    __tablename__ = "quiz_attempts"
    __table_args__ = (sa.Index("ix_quiz_attempts_user_chapter", "user_id", "chapter_id"),)

    id: int | None = Field(default=None, primary_key=True)
    user_id: str = Field(foreign_key="users.id")
    chapter_id: int = Field(foreign_key="chapters.id")
    score_pct: int
    questions_correct: int
    questions_total: int
    attempt_number: int
    xp_earned: int
    duration_secs: int | None = None
    created_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            default=lambda: datetime.now(timezone.utc),
        )
    )

    # Relationship
    user: Optional["User"] = Relationship(back_populates="quiz_attempts")  # noqa: F821
