"""XP calculation engine — pure functions."""


def calculate_xp(
    score_pct: int,
    attempt_number: int,
    best_previous_score: int | None,
) -> int:
    """Calculate XP earned for a quiz attempt.

    Formula:
        Attempt 1: XP = score_pct
        Attempt 2: XP = max(0, score_pct - best_previous_score) * 0.5
        Attempt 3: XP = max(0, score_pct - best_previous_score) * 0.25
        Attempt 4+: XP = max(0, score_pct - best_previous_score) * 0.10

    Args:
        score_pct: Score percentage (0-100)
        attempt_number: 1-indexed attempt number
        best_previous_score: Best score from prior attempts, or None if first attempt

    Returns:
        XP earned (non-negative integer)
    """
    if attempt_number == 1:
        return score_pct

    if best_previous_score is None:
        best_previous_score = 0

    improvement = max(0, score_pct - best_previous_score)

    if attempt_number == 2:
        multiplier = 0.5
    elif attempt_number == 3:
        multiplier = 0.25
    else:
        multiplier = 0.10

    return int(improvement * multiplier)
