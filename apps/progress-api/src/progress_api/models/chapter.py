"""Chapter and ChapterAlias models."""

from datetime import datetime

from sqlmodel import Column, DateTime, Field, SQLModel, text


class Chapter(SQLModel, table=True):
    __tablename__ = "chapters"

    id: int | None = Field(default=None, primary_key=True)
    title: str
    part_slug: str | None = None
    is_active: bool = Field(default=True)
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=text("NOW()"))
    )


class ChapterAlias(SQLModel, table=True):
    __tablename__ = "chapter_aliases"

    slug: str = Field(primary_key=True)
    chapter_id: int = Field(foreign_key="chapters.id")
