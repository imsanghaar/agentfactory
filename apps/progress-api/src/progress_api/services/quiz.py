"""Quiz submission service — orchestrates the 12-step transaction."""

import asyncio
import logging
from datetime import UTC, date, datetime

from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser
from ..models.badge import UserBadge
from ..models.quiz import QuizAttempt
from ..schemas.quiz import BadgeEarned, QuizSubmitRequest, QuizSubmitResponse, StreakInfo
from ..services.engine.badges import BADGE_DEFINITIONS, evaluate_badges
from ..services.engine.streaks import calculate_streak
from ..services.engine.xp import calculate_xp
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


async def submit_quiz(
    session: AsyncSession,
    user: CurrentUser,
    request: QuizSubmitRequest,
) -> QuizSubmitResponse:
    """Process a quiz submission in a single transaction.

    Steps:
    1. UPSERT user from JWT claims
    2. RESOLVE chapter_slug → chapter_id
    3. COUNT previous attempts
    4. GET best previous score
    5. CALCULATE XP
    6. INSERT quiz_attempt
    7. CHECK badge conditions
    8. INSERT new badges
    9. UPSERT activity_day
    10. CALCULATE streak
    11. UPDATE user_progress summary
    12. COMMIT
    """
    today = date.today()

    # 1. UPSERT user
    await upsert_user_from_jwt(session, user)

    # 2. RESOLVE chapter
    chapter = await resolve_or_create_chapter(session, request.chapter_slug)

    # 3. COUNT previous attempts for (user, chapter)
    # Lock matching rows first (FOR UPDATE), then count via subquery.
    # PostgreSQL forbids FOR UPDATE directly on aggregate functions.
    result = await session.execute(
        text(
            "SELECT COUNT(*) FROM ("
            "  SELECT 1 FROM quiz_attempts"
            "  WHERE user_id = :uid AND chapter_id = :cid"
            "  FOR UPDATE"
            ") locked_rows"
        ),
        {"uid": user.id, "cid": chapter.id},
    )
    previous_count = result.scalar_one()
    attempt_number = previous_count + 1

    # 4. GET best previous score
    result = await session.execute(
        select(func.max(QuizAttempt.score_pct)).where(
            QuizAttempt.user_id == user.id, QuizAttempt.chapter_id == chapter.id
        )
    )
    best_previous_score = result.scalar_one()  # None if no previous attempts

    # 5. CALCULATE XP
    xp_earned = calculate_xp(
        score_pct=request.score_pct,
        attempt_number=attempt_number,
        best_previous_score=best_previous_score,
    )

    # 7a. COUNT total quizzes BEFORE insert (auto-flush would inflate count)
    result = await session.execute(
        select(func.count()).select_from(QuizAttempt).where(QuizAttempt.user_id == user.id)
    )
    total_quizzes_before = result.scalar_one()
    is_first_quiz_ever = total_quizzes_before == 0

    # 6. INSERT quiz_attempt
    quiz_attempt = QuizAttempt(
        user_id=user.id,
        chapter_id=chapter.id,
        score_pct=request.score_pct,
        questions_correct=request.questions_correct,
        questions_total=request.questions_total,
        attempt_number=attempt_number,
        xp_earned=xp_earned,
        duration_secs=request.duration_secs,
    )
    session.add(quiz_attempt)

    # 9. UPSERT activity_day (do this before streak calc)
    await record_activity_day(session, user.id, today, "quiz", request.chapter_slug)

    # 10. CALCULATE streak
    activity_dates = await get_activity_dates(session, user.id)
    # Add today if not already present (the record_activity_day may not be visible yet via ORM)
    if today not in activity_dates:
        activity_dates.append(today)
    current_streak, longest_streak = calculate_streak(activity_dates, today=today)

    # 7. CHECK badge conditions
    # Get existing badge IDs
    result = await session.execute(select(UserBadge.badge_id).where(UserBadge.user_id == user.id))
    existing_badge_ids = {row[0] for row in result.all()}

    new_badge_ids = evaluate_badges(
        score_pct=request.score_pct,
        attempt_number=attempt_number,
        is_first_quiz_ever=is_first_quiz_ever,
        current_streak=current_streak,
        existing_badge_ids=existing_badge_ids,
    )

    # 8. INSERT new badges
    now = datetime.now(UTC)
    new_badges_response: list[BadgeEarned] = []
    for badge_id in new_badge_ids:
        badge = UserBadge(
            user_id=user.id,
            badge_id=badge_id,
            earned_at=now,
            trigger_ref=f"quiz:{request.chapter_slug}:attempt:{attempt_number}",
        )
        session.add(badge)
        badge_def = BADGE_DEFINITIONS.get(badge_id)
        new_badges_response.append(
            BadgeEarned(
                id=badge_id,
                name=badge_def.name if badge_def else badge_id,
                earned_at=now,
            )
        )

    # 11. UPDATE user_progress summary
    perfect_delta = 1 if request.score_pct == 100 else 0
    progress = await update_user_progress(
        session,
        user.id,
        xp_delta=xp_earned,
        quizzes_delta=1,
        perfect_scores_delta=perfect_delta,
        badge_count_delta=len(new_badge_ids),
        current_streak=current_streak,
        longest_streak=longest_streak,
        last_activity_date=today,
    )

    # 12. COMMIT
    await session.commit()

    # Invalidate caches
    await invalidate_user_cache(user.id)

    # Refresh leaderboard materialized view in background (debounced: max once per 10 min)
    asyncio.create_task(debounced_refresh_leaderboard())

    # Calculate best score (include current attempt)
    best_score = max(request.score_pct, best_previous_score or 0)

    return QuizSubmitResponse(
        xp_earned=xp_earned,
        total_xp=progress.total_xp,
        attempt_number=attempt_number,
        best_score=best_score,
        new_badges=new_badges_response,
        streak=StreakInfo(current=current_streak, longest=longest_streak),
    )


