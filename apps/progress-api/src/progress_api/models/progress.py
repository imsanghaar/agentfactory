"""UserProgress model."""

import datetime as dt
from typing import Optional

import sqlalchemy as sa
from sqlmodel import Column, DateTime, Field, Relationship, SQLModel, text


class UserProgress(SQLModel, table=True):
    __tablename__ = "user_progress"

    user_id: str = Field(sa_column=Column(sa.String, sa.ForeignKey("users.id"), primary_key=True))
    total_xp: int = Field(default=0)
    quizzes_completed: int = Field(default=0)
    lessons_completed: int = Field(default=0)
    perfect_scores: int = Field(default=0)
    current_streak: int = Field(default=0)
    longest_streak: int = Field(default=0)
    badge_count: int = Field(default=0)
    last_activity_date: dt.date | None = None
    updated_at: dt.datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=text("NOW()"))
    )

    # Relationship
    user: Optional["User"] = Relationship(back_populates="progress")  # noqa: F821
