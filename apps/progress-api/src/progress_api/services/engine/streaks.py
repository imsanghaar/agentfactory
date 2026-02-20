"""Streak calculation engine — pure functions."""

from datetime import date, timedelta


def calculate_streak(activity_dates: list[date], today: date | None = None) -> tuple[int, int]:
    """Calculate current and longest streak from a list of activity dates.

    Args:
        activity_dates: List of dates when the user was active (may contain duplicates)
        today: Reference date for "current" streak (defaults to today)

    Returns:
        Tuple of (current_streak, longest_streak)
    """
    if not activity_dates:
        return 0, 0

    if today is None:
        today = date.today()

    # Deduplicate and sort descending (most recent first)
    unique_dates = sorted(set(activity_dates), reverse=True)

    # Calculate current streak (must include today or yesterday to be "current")
    current_streak = 0
    if unique_dates[0] >= today - timedelta(days=1):
        expected_date = unique_dates[0]
        for d in unique_dates:
            if d == expected_date:
                current_streak += 1
                expected_date -= timedelta(days=1)
            elif d < expected_date:
                break

    # Calculate longest streak (scan all dates, ascending)
    ascending = sorted(set(activity_dates))
    longest_streak = 1
    run = 1
    for i in range(1, len(ascending)):
        if ascending[i] - ascending[i - 1] == timedelta(days=1):
            run += 1
            longest_streak = max(longest_streak, run)
        else:
            run = 1

    longest_streak = max(longest_streak, current_streak)

    return current_streak, longest_streak
