"""Leaderboard service — reads from materialized view."""

import logging

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.auth import CurrentUser
from ..core.cache import get_cached_leaderboard, set_leaderboard_cache
from ..core.redis import get_redis
from ..schemas.leaderboard import LeaderboardEntry, LeaderboardResponse

logger = logging.getLogger(__name__)

# Maximum entries returned in the leaderboard
TOP_N = 100


async def get_leaderboard(
    session: AsyncSession,
    user: CurrentUser | None,
) -> LeaderboardResponse:
    """Fetch leaderboard from materialized view (or cache).

    Steps:
    1. Check Redis cache for leaderboard data
    2. If cache miss, query materialized view for top N
    3. Find current user's rank (even if not in top N) — only if authenticated
    4. Cache the result
    """
    redis = get_redis()
    user_id = user.id if user else None
    logger.debug(f"[Leaderboard] redis client: {'connected' if redis else 'None'}")

    # 1. Check cache
    cached = await get_cached_leaderboard(redis)
    logger.debug(f"[Leaderboard] cache {'HIT' if cached is not None else 'MISS'}")
    if cached is not None:
        # Still need to find current user's rank
        current_user_rank = None
        if user_id:
            for entry in cached:
                if entry["user_id"] == user_id:
                    current_user_rank = entry["rank"]
                    break

            if current_user_rank is None:
                current_user_rank = await _get_user_rank(session, user_id)

        return LeaderboardResponse(
            entries=[LeaderboardEntry(**e) for e in cached],
            current_user_rank=current_user_rank,
            total_users=len(cached),
        )

    # 2. Query materialized view for top N
    result = await session.execute(
        text(
            "SELECT id, display_name, avatar_url, total_xp, rank, badge_count"
            " FROM leaderboard"
            " ORDER BY rank ASC"
            " LIMIT :limit"
        ),
        {"limit": TOP_N},
    )
    rows = result.all()

    # Lazy refresh: if view is empty but users with XP exist, refresh and retry
    if not rows:
        has_data = await session.execute(
            text("SELECT 1 FROM user_progress WHERE total_xp > 0 LIMIT 1")
        )
        if has_data.first() is not None:
            logger.info("[Leaderboard] View empty but data exists — refreshing")
            try:
                await refresh_leaderboard(session)
                result = await session.execute(
                    text(
                        "SELECT id, display_name, avatar_url, total_xp, rank, badge_count"
                        " FROM leaderboard"
                        " ORDER BY rank ASC"
                        " LIMIT :limit"
                    ),
                    {"limit": TOP_N},
                )
                rows = result.all()
                logger.info(f"[Leaderboard] After refresh: {len(rows)} entries")
            except Exception as e:
                logger.error(f"[Leaderboard] Lazy refresh failed: {e}")

            # Ultimate fallback: query tables directly if view refresh failed
            if not rows:
                logger.warning(
                    "[Leaderboard] View still empty after refresh — querying tables directly"
                )
                rows = await _query_leaderboard_live(session)
        else:
            logger.info("[Leaderboard] View empty and no users with XP")

    # Fetch badge_ids for all users in the result set
    user_ids = [row.id for row in rows]
    badge_map: dict[str, list[str]] = {uid: [] for uid in user_ids}
    if user_ids:
        badge_result = await session.execute(
            text(
                "SELECT user_id, badge_id FROM user_badges"
                " WHERE user_id = ANY(:user_ids)"
                " ORDER BY earned_at ASC"
            ),
            {"user_ids": user_ids},
        )
        for badge_row in badge_result.all():
            badge_map[badge_row.user_id].append(badge_row.badge_id)

    entries = []
    current_user_rank = None
    for row in rows:
        entry = LeaderboardEntry(
            rank=row.rank,
            user_id=row.id,
            display_name=row.display_name,
            avatar_url=row.avatar_url,
            total_xp=row.total_xp,
            badge_count=row.badge_count,
            badge_ids=badge_map.get(row.id, []),
        )
        entries.append(entry)
        if user_id and row.id == user_id:
            current_user_rank = row.rank

    # 3. If current user not in top N, find their rank separately
    if user_id and current_user_rank is None:
        current_user_rank = await _get_user_rank(session, user_id)

    total_users = len(entries)

    # 4. Cache the entries (not the user-specific rank)
    # Only cache non-empty results — empty results should trigger lazy refresh next time
    if entries:
        entry_dicts = [e.model_dump() for e in entries]
        redis_status = "connected" if redis else "None"
        logger.debug(f"[Leaderboard] caching {len(entry_dicts)} entries (redis={redis_status})")
        await set_leaderboard_cache(redis, entry_dicts)

    return LeaderboardResponse(
        entries=entries,
        current_user_rank=current_user_rank,
        total_users=total_users,
    )


async def _get_user_rank(session: AsyncSession, user_id: str) -> int | None:
    """Get a specific user's rank from the materialized view, with live fallback."""
    result = await session.execute(
        text("SELECT rank FROM leaderboard WHERE id = :user_id"),
        {"user_id": user_id},
    )
    row = result.first()
    if row:
        return row.rank

    # Fallback: calculate rank live from user_progress
    try:
        # Only calculate rank if user actually has progress with XP
        has_progress = await session.execute(
            text("SELECT 1 FROM user_progress WHERE user_id = :uid AND total_xp > 0"),
            {"uid": user_id},
        )
        if has_progress.first() is None:
            return None

        result = await session.execute(
            text(
                "SELECT COUNT(*) + 1 FROM user_progress up"
                " JOIN users u ON up.user_id = u.id"
                " WHERE u.show_on_leaderboard = TRUE"
                " AND up.total_xp > ("
                "   SELECT COALESCE(total_xp, 0) FROM user_progress WHERE user_id = :uid"
                " )"
            ),
            {"uid": user_id},
        )
        return result.scalar()
    except Exception:
        return None


async def _query_leaderboard_live(session: AsyncSession) -> list:
    """Direct query against tables — fallback when materialized view is stale."""
    result = await session.execute(
        text(
            "SELECT u.id, u.display_name, u.avatar_url, p.total_xp,"
            " RANK() OVER (ORDER BY p.total_xp DESC) AS rank,"
            " p.badge_count"
            " FROM users u JOIN user_progress p ON u.id = p.user_id"
            " WHERE u.show_on_leaderboard = TRUE AND p.total_xp > 0"
            " ORDER BY p.total_xp DESC"
            " LIMIT :limit"
        ),
        {"limit": TOP_N},
    )
    rows = result.all()
    logger.info(f"[Leaderboard] Live query returned {len(rows)} entries")
    return rows


async def refresh_leaderboard(session: AsyncSession) -> None:
    """Refresh the materialized view.

    Tries CONCURRENTLY first (allows reads during refresh), falls back
    to non-concurrent if the view has never been populated.
    """
    try:
        await session.execute(text("REFRESH MATERIALIZED VIEW CONCURRENTLY leaderboard"))
        await session.commit()
        logger.info("[Leaderboard] Materialized view refreshed (concurrent)")
    except Exception as e:
        logger.warning(f"[Leaderboard] Concurrent refresh failed: {e}, trying non-concurrent")
        await session.rollback()
        await session.execute(text("REFRESH MATERIALIZED VIEW leaderboard"))
        await session.commit()
        logger.info("[Leaderboard] Materialized view refreshed (non-concurrent)")


# Cooldown: only refresh once per 10 minutes across all replicas
REFRESH_COOLDOWN_SECS = 600
_REFRESH_LOCK_KEY = "leaderboard:refresh_lock"


async def debounced_refresh_leaderboard() -> None:
    """Refresh leaderboard if last refresh was >10 min ago (Redis-debounced).

    Uses Redis SET NX EX for distributed coordination across Cloud Run replicas.
    If Redis is unavailable, falls back to always-refresh (current behavior).
    """
    redis = get_redis()

    if redis:
        try:
            # SET NX EX: only sets if key doesn't exist, with TTL
            acquired = await redis.set(
                _REFRESH_LOCK_KEY, "1", nx=True, ex=REFRESH_COOLDOWN_SECS
            )
            if not acquired:
                logger.debug("[Leaderboard] Refresh debounced — last refresh was <10 min ago")
                return
        except Exception as e:
            logger.warning(f"[Leaderboard] Redis debounce check failed: {e}, refreshing anyway")

    # Either Redis unavailable, debounce check failed, or cooldown expired — do refresh
    try:
        from ..core.database import async_session

        async with async_session() as session:
            await refresh_leaderboard(session)
    except Exception as e:
        logger.warning(f"[Leaderboard] Background refresh failed: {e}")
