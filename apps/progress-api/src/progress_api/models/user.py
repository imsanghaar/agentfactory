"""User model."""

from datetime import datetime
from typing import Optional

from sqlmodel import Column, DateTime, Field, Relationship, SQLModel, text


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: str = Field(primary_key=True)
    display_name: str
    email: str | None = None
    avatar_url: str | None = None
    show_on_leaderboard: bool = Field(
        default=True,
        sa_column_kwargs={"server_default": text("true")},
    )
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=text("NOW()"))
    )
    updated_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=text("NOW()"))
    )

    # Relationships for selectinload
    badges: list["UserBadge"] = Relationship(back_populates="user")  # noqa: F821
    quiz_attempts: list["QuizAttempt"] = Relationship(back_populates="user")  # noqa: F821
    progress: Optional["UserProgress"] = Relationship(back_populates="user")  # noqa: F821
