#!/bin/bash
# run-eval.sh — Orchestrates all assessment-architect eval graders
# Usage: ./run-eval.sh <SLUG> [chapter-type] [chapter-path]
# Example: ./run-eval.sh ch3-4-general-agents-seven-principles practical-tool

set -euo pipefail

SLUG="${1:?Usage: run-eval.sh <SLUG> [chapter-type] [chapter-path]}"
CHAPTER_TYPE="${2:-auto}"
CHAPTER_PATH="${3:-}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
GRADERS_DIR="$SCRIPT_DIR/graders"
ASSESSMENTS_DIR="$SCRIPT_DIR/../../assessments"

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║           Assessment-Architect Eval Runner                   ║"
echo "╠══════════════════════════════════════════════════════════════╣"
echo "║  Slug: $SLUG"
echo "║  Chapter type: $CHAPTER_TYPE"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# --- Run Structural Checks ---
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  PHASE 1: Structural Checks"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

STRUCTURAL_PASS=true
if bash "$GRADERS_DIR/structural.sh" "$SLUG"; then
  STRUCTURAL_SCORE=100
else
  STRUCTURAL_PASS=false
  STRUCTURAL_SCORE=50  # Partial score if some checks pass
fi
echo ""

# --- Run Domain Relevance ---
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  PHASE 2: Domain Relevance"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

DOMAIN_OUTPUT=$(bash "$GRADERS_DIR/domain-relevance.sh" "$SLUG" "$CHAPTER_PATH" 2>&1) || true
echo "$DOMAIN_OUTPUT"
DOMAIN_SCORE=$(echo "$DOMAIN_OUTPUT" | grep "^DOMAIN_RELEVANCE_SCORE=" | cut -d= -f2 || echo "0")
if [[ -z "$DOMAIN_SCORE" ]]; then DOMAIN_SCORE=0; fi
echo ""

# --- Run Practical Fit ---
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  PHASE 3: Practical Fit"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

PRACTICAL_OUTPUT=$(bash "$GRADERS_DIR/practical-fit.sh" "$SLUG" "$CHAPTER_TYPE" 2>&1) || true
echo "$PRACTICAL_OUTPUT"
PRACTICAL_SCORE=$(echo "$PRACTICAL_OUTPUT" | grep "^PRACTICAL_FIT_SCORE=" | cut -d= -f2 || echo "0")
if [[ -z "$PRACTICAL_SCORE" ]]; then PRACTICAL_SCORE=0; fi
echo ""

# --- Model-Based Rubric Grade ---
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  PHASE 4: Rubric Grade (model-based via claude -p)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

EXAM_FILE_PATH="$ASSESSMENTS_DIR/${SLUG}-exam.md"
KEY_FILE_FOR_RUBRIC="$ASSESSMENTS_DIR/${SLUG}-answer-key.md"
USE_RUBRIC=false
RUBRIC_QUALITY_SCORE=0
RUBRIC_COVERAGE_SCORE=0

# Check if claude CLI is available
if command -v claude &>/dev/null && [[ -f "$EXAM_FILE_PATH" ]] && [[ -f "$KEY_FILE_FOR_RUBRIC" ]]; then
  echo "  Running model-based quality assessment..."
  echo ""

  # Build the grading prompt in a temp file (avoids heredoc escaping issues with file content)
  TMPFILE=$(mktemp)
  trap "rm -f $TMPFILE" EXIT

  cat > "$TMPFILE" <<'HEADER'
You are evaluating a certification exam for quality.

Score these four dimensions (0-100 each):

1. DOMAIN RELEVANCE: Are scenarios set in the chapter's actual domain (development/coding/AI tools)? Or do they drift to unrelated industries (medical, legal, manufacturing)?

2. PRACTICAL COMPETENCE: Would passing certify someone to DO the work? Do questions test tool selection, consequence understanding, workflow decisions? Or just vocabulary/definitions?

3. QUESTION QUALITY: Are distractors plausible (common misconceptions)? Are scenarios realistic? Is writing concise (difficulty in thinking, not reading)? Any obviously wrong options that can be eliminated without thinking?

4. COVERAGE: Are important topics proportionally represented? Any major topics with 0 questions? Evidence of mechanical flat allocation vs importance-weighted?

Respond with ONLY a JSON object, no other text:
{"domain_relevance": <score>, "practical_competence": <score>, "question_quality": <score>, "coverage": <score>, "top_failures": ["failure1", "failure2", "failure3"]}

---

EXAM (first 40 questions):

HEADER

  # Append exam content (first ~40 questions)
  head -400 "$EXAM_FILE_PATH" >> "$TMPFILE"

  echo "" >> "$TMPFILE"
  echo "---" >> "$TMPFILE"
  echo "" >> "$TMPFILE"
  echo "ANSWER KEY:" >> "$TMPFILE"
  echo "" >> "$TMPFILE"
  cat "$KEY_FILE_FOR_RUBRIC" >> "$TMPFILE"

  # Run claude in non-interactive mode with haiku for cost efficiency
  RUBRIC_OUTPUT=$(claude -p --model haiku < "$TMPFILE" 2>/dev/null) || RUBRIC_OUTPUT=""
  rm -f "$TMPFILE"

  if [[ -n "$RUBRIC_OUTPUT" ]]; then
    # Parse JSON scores using grep/sed (portable, no jq dependency)
    RUBRIC_DOMAIN=$(echo "$RUBRIC_OUTPUT" | grep -o '"domain_relevance":[[:space:]]*[0-9]*' | grep -o '[0-9]*$') || RUBRIC_DOMAIN=0
    RUBRIC_PRACTICAL=$(echo "$RUBRIC_OUTPUT" | grep -o '"practical_competence":[[:space:]]*[0-9]*' | grep -o '[0-9]*$') || RUBRIC_PRACTICAL=0
    RUBRIC_QUALITY_SCORE=$(echo "$RUBRIC_OUTPUT" | grep -o '"question_quality":[[:space:]]*[0-9]*' | grep -o '[0-9]*$') || RUBRIC_QUALITY_SCORE=0
    RUBRIC_COVERAGE_SCORE=$(echo "$RUBRIC_OUTPUT" | grep -o '"coverage":[[:space:]]*[0-9]*' | grep -o '[0-9]*$') || RUBRIC_COVERAGE_SCORE=0

    # Extract top failures
    RUBRIC_FAILURES=$(echo "$RUBRIC_OUTPUT" | grep -o '"top_failures":\[.*\]' | sed 's/"top_failures":\[//;s/\]$//') || RUBRIC_FAILURES=""

    if [[ "$RUBRIC_QUALITY_SCORE" -gt 0 || "$RUBRIC_COVERAGE_SCORE" -gt 0 ]]; then
      USE_RUBRIC=true
      echo "  Model-based scores:"
      echo "    Domain Relevance (model):     $RUBRIC_DOMAIN/100"
      echo "    Practical Competence (model):  $RUBRIC_PRACTICAL/100"
      echo "    Question Quality (model):      $RUBRIC_QUALITY_SCORE/100"
      echo "    Coverage (model):              $RUBRIC_COVERAGE_SCORE/100"
      if [[ -n "$RUBRIC_FAILURES" ]]; then
        echo ""
        echo "  Top failures identified:"
        echo "    $RUBRIC_FAILURES"
      fi
    else
      echo "  Model returned scores but parsing failed. Raw output:"
      echo "  $RUBRIC_OUTPUT" | head -5
    fi
  else
    echo "  claude -p returned no output (may need authentication or API key)"
    echo "  Falling back to deterministic scores only."
  fi
else
  if ! command -v claude &>/dev/null; then
    echo "  claude CLI not found — skipping model-based grading"
  else
    echo "  Exam or answer key file missing — skipping model-based grading"
  fi
  echo "  Using deterministic scores only."
fi
echo ""

# --- Overall Score ---
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  OVERALL SCORE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Weights: Domain(40%) + Practical(30%) + Quality(20%) + Coverage(10%)
# Deterministic graders measure domain + distribution fit
# Model-based grader measures quality + coverage (things grep can't judge)
if [[ "$USE_RUBRIC" == "true" ]]; then
  # Blend: deterministic domain/fit + model-based quality/coverage
  OVERALL=$(( (DOMAIN_SCORE * 40 + PRACTICAL_SCORE * 30 + RUBRIC_QUALITY_SCORE * 20 + RUBRIC_COVERAGE_SCORE * 10) / 100 ))
  echo "  Domain Relevance (deterministic): $DOMAIN_SCORE/100 (weight: 40%)"
  echo "  Practical Fit (deterministic):    $PRACTICAL_SCORE/100 (weight: 30%)"
  echo "  Question Quality (model):         $RUBRIC_QUALITY_SCORE/100 (weight: 20%)"
  echo "  Coverage (model):                 $RUBRIC_COVERAGE_SCORE/100 (weight: 10%)"
else
  # Without model scores, use deterministic only (reweighted)
  OVERALL=$(( (DOMAIN_SCORE * 57 + PRACTICAL_SCORE * 43) / 100 ))
  echo "  Domain Relevance (deterministic): $DOMAIN_SCORE/100 (weight: 57% — reweighted)"
  echo "  Practical Fit (deterministic):    $PRACTICAL_SCORE/100 (weight: 43% — reweighted)"
  echo "  (Quality + Coverage: no model scores — install claude CLI for full eval)"
fi

# Structural failures are a hard gate
if [[ "$STRUCTURAL_PASS" == "false" ]]; then
  echo ""
  echo "  ⚠ Structural checks FAILED — capping overall at 50"
  if [[ "$OVERALL" -gt 50 ]]; then OVERALL=50; fi
fi

echo ""
echo "  ┌─────────────────────────────────┐"
echo "  │  OVERALL SCORE: $OVERALL/100"
echo "  └─────────────────────────────────┘"
echo ""

if [[ "$OVERALL" -ge 90 ]]; then
  echo "  VERDICT: EXCELLENT — exam is ready for use"
elif [[ "$OVERALL" -ge 75 ]]; then
  echo "  VERDICT: GOOD — minor improvements possible"
elif [[ "$OVERALL" -ge 60 ]]; then
  echo "  VERDICT: NEEDS WORK — specific dimensions failing"
else
  echo "  VERDICT: FAIL — fundamental issues with exam quality"
fi

echo ""
echo "OVERALL_SCORE=$OVERALL"
echo "STRUCTURAL_PASS=$STRUCTURAL_PASS"
echo "DOMAIN_SCORE=$DOMAIN_SCORE"
echo "PRACTICAL_SCORE=$PRACTICAL_SCORE"
