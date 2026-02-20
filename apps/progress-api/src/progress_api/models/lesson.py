"""LessonCompletion model."""

from datetime import datetime

import sqlalchemy as sa
from sqlmodel import Column, DateTime, Field, SQLModel, text


class LessonCompletion(SQLModel, table=True):
    __tablename__ = "lesson_completions"

    user_id: str = Field(sa_column=Column(sa.String, sa.ForeignKey("users.id"), primary_key=True))
    chapter_slug: str = Field(sa_column=Column(sa.String, primary_key=True))
    lesson_slug: str = Field(sa_column=Column(sa.String, primary_key=True))
    active_duration_secs: int | None = None
    completed_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=text("NOW()"))
    )
