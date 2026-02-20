"""Background scheduler for periodic tasks.

Uses asyncio.create_task for a simple refresh loop.
No external dependencies (APScheduler not needed for a single task).
"""

import asyncio
import logging

logger = logging.getLogger(__name__)

# Refresh interval in seconds (default 10 minutes)
LEADERBOARD_REFRESH_INTERVAL = 600

_refresh_task: asyncio.Task | None = None


async def _refresh_loop() -> None:
    """Periodically refresh the leaderboard materialized view."""
    from ..core.database import async_session
    from ..services.leaderboard import refresh_leaderboard

    while True:
        await asyncio.sleep(LEADERBOARD_REFRESH_INTERVAL)
        try:
            async with async_session() as session:
                await refresh_leaderboard(session)
        except Exception as e:
            logger.error(f"[Scheduler] Leaderboard refresh failed: {e}")


def start_scheduler() -> None:
    """Start the background refresh scheduler."""
    global _refresh_task

    _refresh_task = asyncio.create_task(_refresh_loop())
    logger.info(f"[Scheduler] Leaderboard refresh every {LEADERBOARD_REFRESH_INTERVAL}s")


def stop_scheduler() -> None:
    """Cancel the background refresh task."""
    global _refresh_task

    if _refresh_task is not None:
        _refresh_task.cancel()
        _refresh_task = None
        logger.info("[Scheduler] Stopped")
