"""Shared service utilities — DRY across quiz and lesson services.

Contains:
- upsert_user_from_jwt: Create or update user from JWT claims
- resolve_or_create_chapter: Resolve chapter slug to internal ID
- record_activity_day: Insert activity record for streak tracking
- update_user_progress: Atomic update of denormalized summary
- invalidate_user_cache: Clear cached progress data
"""

import logging
from datetime import UTC, date, datetime

from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser
from ..core.cache import invalidate_leaderboard_cache, invalidate_progress_cache
from ..core.redis import get_redis
from ..models.activity import ActivityDay
from ..models.chapter import Chapter, ChapterAlias
from ..models.progress import UserProgress
from ..models.user import User

logger = logging.getLogger(__name__)


async def upsert_user_from_jwt(session: AsyncSession, user: CurrentUser) -> User:
    """Create or update user from JWT claims.

    On first encounter, creates the user. On subsequent requests,
    updates display_name to keep it fresh from SSO.
    """
    result = await session.execute(select(User).where(User.id == user.id))
    db_user = result.scalar_one_or_none()

    if db_user is None:
        db_user = User(
            id=user.id,
            display_name=user.name or user.id,
            email=user.email,
        )
        session.add(db_user)
        await session.flush()
    else:
        # Keep display name fresh from JWT
        if user.name and user.name != db_user.display_name:
            db_user.display_name = user.name
        db_user.updated_at = datetime.now(UTC)

    return db_user


async def resolve_or_create_chapter(session: AsyncSession, slug: str) -> Chapter:
    """Resolve chapter_slug to internal chapter via chapter_aliases.

    If the alias doesn't exist, auto-creates chapter + alias.
    Uses ON CONFLICT DO NOTHING on the alias insert to handle concurrent
    requests for the same new slug (A4).
    """
    # Fast path: lookup existing alias
    result = await session.execute(
        select(Chapter)
        .join(ChapterAlias, Chapter.id == ChapterAlias.chapter_id)
        .where(ChapterAlias.slug == slug)
    )
    chapter = result.scalar_one_or_none()

    if chapter is not None:
        return chapter

    # Slow path: create chapter + alias with ON CONFLICT DO NOTHING
    parts = slug.split("/")
    part_slug = parts[0] if len(parts) > 1 else None
    title = parts[-1].replace("-", " ").title() if parts else slug

    chapter = Chapter(title=title, part_slug=part_slug)
    session.add(chapter)
    await session.flush()

    # ON CONFLICT DO NOTHING — if another request already created this alias,
    # we'll pick up their chapter in the re-fetch below.
    await session.execute(
        text(
            "INSERT INTO chapter_aliases (slug, chapter_id) "
            "VALUES (:slug, :chapter_id) ON CONFLICT (slug) DO NOTHING"
        ),
        {"slug": slug, "chapter_id": chapter.id},
    )

    # Re-fetch the canonical chapter via alias (ours or the concurrent winner's)
    result = await session.execute(
        select(Chapter)
        .join(ChapterAlias, Chapter.id == ChapterAlias.chapter_id)
        .where(ChapterAlias.slug == slug)
    )
    return result.scalar_one()


async def record_activity_day(
    session: AsyncSession,
    user_id: str,
    activity_date: date,
    activity_type: str,
    reference_id: str,
) -> None:
    """Record an activity day for streak tracking (ON CONFLICT DO NOTHING)."""
    # Use raw SQL for ON CONFLICT DO NOTHING (composite PK)
    await session.execute(
        text("""
            INSERT INTO activity_days (user_id, activity_date, activity_type, reference_id)
            VALUES (:user_id, :activity_date, :activity_type, :reference_id)
            ON CONFLICT (user_id, activity_date, activity_type, reference_id) DO NOTHING
        """),
        {
            "user_id": user_id,
            "activity_date": activity_date,
            "activity_type": activity_type,
            "reference_id": reference_id,
        },
    )


async def get_activity_dates(session: AsyncSession, user_id: str) -> list[date]:
    """Get all unique activity dates for a user (for streak calculation)."""
    result = await session.execute(
        select(ActivityDay.activity_date)
        .where(ActivityDay.user_id == user_id)
        .distinct()
        .order_by(ActivityDay.activity_date.desc())
    )
    return [row[0] for row in result.all()]


async def update_user_progress(
    session: AsyncSession,
    user_id: str,
    *,
    xp_delta: int = 0,
    quizzes_delta: int = 0,
    lessons_delta: int = 0,
    perfect_scores_delta: int = 0,
    badge_count_delta: int = 0,
    current_streak: int | None = None,
    longest_streak: int | None = None,
    last_activity_date: date | None = None,
) -> UserProgress:
    """Atomic update of user_progress summary row.

    Uses SELECT FOR UPDATE to prevent concurrent modifications.
    Creates the row if it doesn't exist.
    """
    # SELECT FOR UPDATE for atomicity
    result = await session.execute(
        select(UserProgress).where(UserProgress.user_id == user_id).with_for_update()
    )
    progress = result.scalar_one_or_none()

    if progress is None:
        progress = UserProgress(user_id=user_id)
        session.add(progress)
        await session.flush()
        # Re-fetch with lock
        result = await session.execute(
            select(UserProgress).where(UserProgress.user_id == user_id).with_for_update()
        )
        progress = result.scalar_one_or_none()

    progress.total_xp += xp_delta
    progress.quizzes_completed += quizzes_delta
    progress.lessons_completed += lessons_delta
    progress.perfect_scores += perfect_scores_delta
    progress.badge_count += badge_count_delta

    if current_streak is not None:
        progress.current_streak = current_streak
    if longest_streak is not None:
        progress.longest_streak = max(progress.longest_streak, longest_streak)
    if last_activity_date is not None:
        progress.last_activity_date = last_activity_date

    progress.updated_at = datetime.now(UTC)

    return progress


async def invalidate_user_cache(user_id: str) -> None:
    """Invalidate all cached data for a user (A3: skip if redis is None)."""
    redis = get_redis()
    await invalidate_progress_cache(redis, user_id)
    await invalidate_leaderboard_cache(redis)
