"""Tests for XP calculation engine."""

from progress_api.services.engine.xp import calculate_xp


class TestCalculateXpFirstAttempt:
    """Attempt 1: XP = score_pct."""

    def test_score_zero(self):
        assert calculate_xp(score_pct=0, attempt_number=1, best_previous_score=None) == 0

    def test_score_fifty(self):
        assert calculate_xp(score_pct=50, attempt_number=1, best_previous_score=None) == 50

    def test_score_eighty_five(self):
        assert calculate_xp(score_pct=85, attempt_number=1, best_previous_score=None) == 85

    def test_score_hundred(self):
        assert calculate_xp(score_pct=100, attempt_number=1, best_previous_score=None) == 100


class TestCalculateXpSecondAttempt:
    """Attempt 2: XP = max(0, improvement) * 0.5."""

    def test_improvement(self):
        # Previous best 50, now 80 → improvement 30 * 0.5 = 15
        assert calculate_xp(score_pct=80, attempt_number=2, best_previous_score=50) == 15

    def test_no_improvement(self):
        # Previous best 80, now 70 → no improvement
        assert calculate_xp(score_pct=70, attempt_number=2, best_previous_score=80) == 0

    def test_same_score(self):
        assert calculate_xp(score_pct=50, attempt_number=2, best_previous_score=50) == 0

    def test_from_zero(self):
        # Previous best 0, now 100 → improvement 100 * 0.5 = 50
        assert calculate_xp(score_pct=100, attempt_number=2, best_previous_score=0) == 50


class TestCalculateXpThirdAttempt:
    """Attempt 3: XP = max(0, improvement) * 0.25."""

    def test_improvement(self):
        # Previous best 50, now 100 → improvement 50 * 0.25 = 12
        assert calculate_xp(score_pct=100, attempt_number=3, best_previous_score=50) == 12

    def test_no_improvement(self):
        assert calculate_xp(score_pct=50, attempt_number=3, best_previous_score=100) == 0


class TestCalculateXpFourthPlusAttempt:
    """Attempt 4+: XP = max(0, improvement) * 0.10."""

    def test_attempt_four(self):
        # Previous best 50, now 100 → improvement 50 * 0.10 = 5
        assert calculate_xp(score_pct=100, attempt_number=4, best_previous_score=50) == 5

    def test_attempt_hundred(self):
        # Even after 100 attempts, same formula
        assert calculate_xp(score_pct=100, attempt_number=100, best_previous_score=50) == 5

    def test_no_improvement_attempt_four(self):
        assert calculate_xp(score_pct=50, attempt_number=4, best_previous_score=50) == 0

    def test_negative_improvement_attempt_four(self):
        assert calculate_xp(score_pct=30, attempt_number=4, best_previous_score=50) == 0


class TestCalculateXpEdgeCases:
    """Edge cases."""

    def test_best_previous_none_second_attempt(self):
        # best_previous_score=None treated as 0 for reattempts
        assert calculate_xp(score_pct=80, attempt_number=2, best_previous_score=None) == 40

    def test_all_zeros(self):
        assert calculate_xp(score_pct=0, attempt_number=1, best_previous_score=None) == 0

    def test_perfect_first_attempt(self):
        assert calculate_xp(score_pct=100, attempt_number=1, best_previous_score=None) == 100

    def test_small_improvement_rounds_down(self):
        # improvement 1 * 0.10 = 0.1 → int(0.1) = 0
        assert calculate_xp(score_pct=51, attempt_number=4, best_previous_score=50) == 0

    def test_larger_improvement_rounds_down(self):
        # improvement 3 * 0.10 = 0.3 → int(0.3) = 0
        assert calculate_xp(score_pct=53, attempt_number=4, best_previous_score=50) == 0

    def test_significant_improvement_attempt_four(self):
        # improvement 20 * 0.10 = 2
        assert calculate_xp(score_pct=70, attempt_number=4, best_previous_score=50) == 2
