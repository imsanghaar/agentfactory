"""Lesson completion service — idempotent lesson marking."""

import asyncio
import logging
from datetime import date

from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser
from ..models.lesson import LessonCompletion
from ..schemas.lesson import LessonCompleteRequest, LessonCompleteResponse
from ..schemas.quiz import StreakInfo
from ..services.engine.streaks import calculate_streak
from .leaderboard import debounced_refresh_leaderboard
from .shared import (
    get_activity_dates,
    invalidate_user_cache,
    record_activity_day,
    resolve_or_create_chapter,
    update_user_progress,
    upsert_user_from_jwt,
)

logger = logging.getLogger(__name__)


async def complete_lesson(
    session: AsyncSession,
    user: CurrentUser,
    request: LessonCompleteRequest,
) -> LessonCompleteResponse:
    """Mark a lesson as complete (idempotent).

    Steps:
    1. UPSERT user from JWT claims
    2. RESOLVE chapter_slug → chapter_id
    3. INSERT lesson_completion (ON CONFLICT DO NOTHING)
    4. UPSERT activity_day for today (type: 'lesson')
    5. CALCULATE streak from activity_days
    6. UPDATE user_progress summary (streak, last_activity_date, lessons_completed)
    7. COMMIT
    """
    today = date.today()

    # 1. UPSERT user
    await upsert_user_from_jwt(session, user)

    # 2. RESOLVE chapter (ensure it exists)
    await resolve_or_create_chapter(session, request.chapter_slug)

    # 3. INSERT lesson_completion (ON CONFLICT DO NOTHING for idempotency)
    # Check if already completed first
    result = await session.execute(
        select(LessonCompletion).where(
            LessonCompletion.user_id == user.id,
            LessonCompletion.chapter_slug == request.chapter_slug,
            LessonCompletion.lesson_slug == request.lesson_slug,
        )
    )
    existing = result.scalar_one_or_none()

    if existing is not None:
        # Already completed — return without modifying anything
        # Still calculate current streak for the response
        activity_dates = await get_activity_dates(session, user.id)
        current_streak, longest_streak = calculate_streak(activity_dates, today=today)

        return LessonCompleteResponse(
            completed=True,
            active_duration_secs=existing.active_duration_secs,
            streak=StreakInfo(current=current_streak, longest=longest_streak),
            already_completed=True,
        )

    # New completion — insert via raw SQL for ON CONFLICT safety
    await session.execute(
        text(
            "INSERT INTO lesson_completions"
            " (user_id, chapter_slug, lesson_slug, active_duration_secs)"
            " VALUES (:user_id, :chapter_slug, :lesson_slug, :active_duration_secs)"
            " ON CONFLICT (user_id, chapter_slug, lesson_slug) DO NOTHING"
        ),
        {
            "user_id": user.id,
            "chapter_slug": request.chapter_slug,
            "lesson_slug": request.lesson_slug,
            "active_duration_secs": request.active_duration_secs,
        },
    )

    # 4. UPSERT activity_day
    ref = f"{request.chapter_slug}/{request.lesson_slug}"
    await record_activity_day(session, user.id, today, "lesson", ref)

    # 5. CALCULATE streak
    activity_dates = await get_activity_dates(session, user.id)
    if today not in activity_dates:
        activity_dates.append(today)
    current_streak, longest_streak = calculate_streak(activity_dates, today=today)

    # 6. UPDATE user_progress summary
    # Award 1 XP if active reading time exceeds 60 seconds
    xp_earned = 1 if (request.active_duration_secs or 0) > 60 else 0
    await update_user_progress(
        session,
        user.id,
        xp_delta=xp_earned,
        lessons_delta=1,
        current_streak=current_streak,
        longest_streak=longest_streak,
        last_activity_date=today,
    )

    # 7. COMMIT
    await session.commit()

    # Invalidate caches + refresh leaderboard view
    await invalidate_user_cache(user.id)
    if xp_earned > 0:
        asyncio.create_task(debounced_refresh_leaderboard())

    return LessonCompleteResponse(
        completed=True,
        active_duration_secs=request.active_duration_secs,
        streak=StreakInfo(current=current_streak, longest=longest_streak),
        already_completed=False,
        xp_earned=xp_earned,
    )


