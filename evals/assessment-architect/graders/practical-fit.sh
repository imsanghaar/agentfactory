#!/bin/bash
# practical-fit.sh — Checks if question type distribution matches chapter type
# Usage: ./practical-fit.sh <SLUG> [chapter-type]
# chapter-type: practical-tool | conceptual | hybrid (auto-detected if not provided)
# Example: ./practical-fit.sh ch3-4-general-agents-seven-principles practical-tool

set -euo pipefail

SLUG="${1:?Usage: practical-fit.sh <SLUG> [chapter-type]}"
CHAPTER_TYPE="${2:-auto}"
ASSESSMENTS_DIR="$(cd "$(dirname "$0")/../.." && pwd)/../assessments"
KEY_FILE="$ASSESSMENTS_DIR/${SLUG}-answer-key.md"

if [[ ! -f "$KEY_FILE" ]]; then
  echo "ERROR: Answer key not found: $KEY_FILE"
  exit 1
fi

echo "=== Practical Fit Check: $SLUG ==="
echo ""

# --- Determine chapter type ---
if [[ "$CHAPTER_TYPE" == "auto" ]]; then
  # Heuristic: look at exam content for tool-related patterns
  EXAM_FILE="$ASSESSMENTS_DIR/${SLUG}-exam.md"
  if [[ -f "$EXAM_FILE" ]]; then
    CLI_PATTERNS=$(grep -ciE "CLI|command|terminal|install|config|hook|plugin|tool" "$EXAM_FILE" 2>/dev/null) || true
    PRINCIPLE_PATTERNS=$(grep -ciE "principle|pattern|architecture|design|when to|why|trade-off" "$EXAM_FILE" 2>/dev/null) || true

    if [[ "$CLI_PATTERNS" -gt "$PRINCIPLE_PATTERNS" ]]; then
      CHAPTER_TYPE="practical-tool"
    elif [[ "$PRINCIPLE_PATTERNS" -gt "$((CLI_PATTERNS * 2))" ]]; then
      CHAPTER_TYPE="conceptual"
    else
      CHAPTER_TYPE="hybrid"
    fi
  else
    CHAPTER_TYPE="hybrid"
    echo "  NOTE: No exam file for auto-detection, defaulting to hybrid"
  fi
fi

echo "  Chapter type: $CHAPTER_TYPE"
echo ""

# --- Extract type distribution from answer key ---
echo "-- Question Type Distribution --"

TOTAL=$(grep -cE "^\| [0-9]+ \|" "$KEY_FILE" 2>/dev/null) || true

if [[ "$TOTAL" -eq 0 ]]; then
  echo "ERROR: No questions found in answer key"
  exit 1
fi

# Count each type
SCENARIO_COUNT=$(grep -c "Scenario Analysis" "$KEY_FILE" 2>/dev/null) || true
RELATIONSHIP_COUNT=$(grep -c "Concept Relationship" "$KEY_FILE" 2>/dev/null) || true
TRANSFER_COUNT=$(grep -c "Transfer Application" "$KEY_FILE" 2>/dev/null) || true
EVALUATION_COUNT=$(grep -c "Critical Evaluation" "$KEY_FILE" 2>/dev/null) || true

SCENARIO_PCT=$((SCENARIO_COUNT * 100 / TOTAL))
RELATIONSHIP_PCT=$((RELATIONSHIP_COUNT * 100 / TOTAL))
TRANSFER_PCT=$((TRANSFER_COUNT * 100 / TOTAL))
EVALUATION_PCT=$((EVALUATION_COUNT * 100 / TOTAL))

echo "  Scenario Analysis:    $SCENARIO_COUNT ($SCENARIO_PCT%)"
echo "  Concept Relationship: $RELATIONSHIP_COUNT ($RELATIONSHIP_PCT%)"
echo "  Transfer Application: $TRANSFER_COUNT ($TRANSFER_PCT%)"
echo "  Critical Evaluation:  $EVALUATION_COUNT ($EVALUATION_PCT%)"
echo "  Total: $TOTAL"
echo ""

# --- Expected distributions by chapter type ---
echo "-- Expected vs Actual Distribution --"

SCORE=100
DEDUCTIONS=""

case "$CHAPTER_TYPE" in
  "practical-tool")
    # Expected: Scenario 60%, Relationship 20%, Transfer 5%, Evaluation 15%
    # Tolerance: +/- 10 percentage points
    EXP_SCENARIO=60; EXP_RELATIONSHIP=20; EXP_TRANSFER=5; EXP_EVALUATION=15

    echo "  Expected (practical-tool): Scenario=60% Relationship=20% Transfer=5% Evaluation=15%"
    echo "  Actual:                    Scenario=${SCENARIO_PCT}% Relationship=${RELATIONSHIP_PCT}% Transfer=${TRANSFER_PCT}% Evaluation=${EVALUATION_PCT}%"
    echo ""

    # Transfer Application should be minimal for practical-tool chapters
    if [[ "$TRANSFER_PCT" -gt 15 ]]; then
      PENALTY=$((( TRANSFER_PCT - 15 ) * 3))
      SCORE=$((SCORE - PENALTY))
      DEDUCTIONS="${DEDUCTIONS}  -${PENALTY}: Transfer Application at ${TRANSFER_PCT}% (expected <=15% for practical-tool chapter)\n"
    fi

    # Scenario Analysis should dominate
    if [[ "$SCENARIO_PCT" -lt 45 ]]; then
      PENALTY=$(((45 - SCENARIO_PCT) * 2))
      SCORE=$((SCORE - PENALTY))
      DEDUCTIONS="${DEDUCTIONS}  -${PENALTY}: Scenario Analysis at ${SCENARIO_PCT}% (expected >=45% for practical-tool chapter)\n"
    fi

    # Check if flat distribution (40/25/20/15) was used instead of adapted
    SCENARIO_DIFF=$((SCENARIO_PCT - 40))
    TRANSFER_DIFF=$((TRANSFER_PCT - 20))
    if [[ "${SCENARIO_DIFF#-}" -le 3 && "${TRANSFER_DIFF#-}" -le 3 ]]; then
      PENALTY=15
      SCORE=$((SCORE - PENALTY))
      DEDUCTIONS="${DEDUCTIONS}  -${PENALTY}: Distribution matches default 40/25/20/15 — not adapted to chapter type\n"
    fi
    ;;

  "conceptual")
    # Expected: Scenario 35%, Relationship 25%, Transfer 25%, Evaluation 15%
    EXP_SCENARIO=35; EXP_RELATIONSHIP=25; EXP_TRANSFER=25; EXP_EVALUATION=15

    echo "  Expected (conceptual): Scenario=35% Relationship=25% Transfer=25% Evaluation=15%"
    echo "  Actual:                Scenario=${SCENARIO_PCT}% Relationship=${RELATIONSHIP_PCT}% Transfer=${TRANSFER_PCT}% Evaluation=${EVALUATION_PCT}%"
    echo ""

    # Transfer should be substantial for conceptual chapters
    if [[ "$TRANSFER_PCT" -lt 15 ]]; then
      PENALTY=$(((15 - TRANSFER_PCT) * 2))
      SCORE=$((SCORE - PENALTY))
      DEDUCTIONS="${DEDUCTIONS}  -${PENALTY}: Transfer Application at ${TRANSFER_PCT}% (expected >=15% for conceptual chapter)\n"
    fi
    ;;

  "hybrid")
    # Expected: somewhere between practical and conceptual
    EXP_SCENARIO=50; EXP_RELATIONSHIP=22; EXP_TRANSFER=13; EXP_EVALUATION=15

    echo "  Expected (hybrid): Scenario=50% Relationship=22% Transfer=13% Evaluation=15%"
    echo "  Actual:            Scenario=${SCENARIO_PCT}% Relationship=${RELATIONSHIP_PCT}% Transfer=${TRANSFER_PCT}% Evaluation=${EVALUATION_PCT}%"
    echo ""

    if [[ "$TRANSFER_PCT" -gt 25 ]]; then
      PENALTY=$(((TRANSFER_PCT - 25) * 2))
      SCORE=$((SCORE - PENALTY))
      DEDUCTIONS="${DEDUCTIONS}  -${PENALTY}: Transfer Application at ${TRANSFER_PCT}% (high for hybrid chapter)\n"
    fi
    ;;
esac

# --- Lesson weighting check ---
echo "-- Lesson Weighting --"

# Check if question count suggests flat 2-per-lesson allocation
NOTES_FILE="$ASSESSMENTS_DIR/${SLUG}-notes.md"
if [[ -f "$NOTES_FILE" ]]; then
  LESSON_COUNT=$(grep -c "^## Lesson:" "$NOTES_FILE" 2>/dev/null) || LESSON_COUNT=0
  if [[ "$LESSON_COUNT" -gt 0 ]]; then
    EXPECTED_FLAT=$((LESSON_COUNT * 2))
    FLAT_DIFF=$((TOTAL - EXPECTED_FLAT))
    if [[ "${FLAT_DIFF#-}" -le 5 ]]; then
      PENALTY=10
      SCORE=$((SCORE - PENALTY))
      DEDUCTIONS="${DEDUCTIONS}  -${PENALTY}: Question count ($TOTAL) matches flat 2-per-lesson allocation ($EXPECTED_FLAT) — no importance weighting\n"
      echo "  Lessons: $LESSON_COUNT, Questions: $TOTAL, Expected flat: $EXPECTED_FLAT"
      echo "  WARNING: Count suggests mechanical 2-per-lesson, not importance-weighted"
    else
      echo "  Lessons: $LESSON_COUNT, Questions: $TOTAL (appears importance-weighted)"
    fi
  fi
else
  echo "  No notes file found for lesson count comparison"
fi

echo ""

# --- Clamp score ---
if [[ "$SCORE" -lt 0 ]]; then SCORE=0; fi
if [[ "$SCORE" -gt 100 ]]; then SCORE=100; fi

# --- Report ---
echo "-- Scoring --"
if [[ -n "$DEDUCTIONS" ]]; then
  echo "  Deductions:"
  echo -e "$DEDUCTIONS"
fi

echo "  SCORE: $SCORE/100"
echo ""

# --- Verdict ---
if [[ "$SCORE" -ge 90 ]]; then
  echo "  VERDICT: EXCELLENT — distribution well-adapted to chapter type"
elif [[ "$SCORE" -ge 75 ]]; then
  echo "  VERDICT: GOOD — minor distribution issues"
elif [[ "$SCORE" -ge 60 ]]; then
  echo "  VERDICT: NEEDS WORK — distribution not adapted to chapter type"
else
  echo "  VERDICT: FAIL — significant distribution mismatch for chapter type"
fi

echo ""
echo "PRACTICAL_FIT_SCORE=$SCORE"
