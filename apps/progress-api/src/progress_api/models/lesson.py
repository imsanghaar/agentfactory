"""LessonCompletion model."""

from datetime import datetime, timezone

import sqlalchemy as sa
from sqlmodel import Column, DateTime, Field, SQLModel, func


class LessonCompletion(SQLModel, table=True):
    __tablename__ = "lesson_completions"

    user_id: str = Field(sa_column=Column(sa.String, sa.ForeignKey("users.id"), primary_key=True))
    chapter_slug: str = Field(sa_column=Column(sa.String, primary_key=True))
    lesson_slug: str = Field(sa_column=Column(sa.String, primary_key=True))
    active_duration_secs: int | None = None
    completed_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            default=lambda: datetime.now(timezone.utc),
        )
    )
