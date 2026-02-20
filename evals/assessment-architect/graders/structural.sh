#!/bin/bash
# structural.sh — Deterministic structural checks for assessment exams
# Usage: ./structural.sh <SLUG>
# Example: ./structural.sh ch3-4-general-agents-seven-principles

set -euo pipefail

SLUG="${1:?Usage: structural.sh <SLUG>}"
ASSESSMENTS_DIR="$(cd "$(dirname "$0")/../.." && pwd)/../assessments"
EXAM_FILE="$ASSESSMENTS_DIR/${SLUG}-exam.md"
KEY_FILE="$ASSESSMENTS_DIR/${SLUG}-answer-key.md"
CONCEPTS_FILE="$ASSESSMENTS_DIR/${SLUG}-concepts.md"

PASS=0
FAIL=0
WARN=0

pass() { echo "  PASS: $1"; PASS=$((PASS + 1)); }
fail() { echo "  FAIL: $1"; FAIL=$((FAIL + 1)); }
warn() { echo "  WARN: $1"; WARN=$((WARN + 1)); }

echo "=== Structural Checks: $SLUG ==="
echo ""

# --- File Existence ---
echo "-- File Existence --"
if [[ -f "$EXAM_FILE" ]]; then
  pass "Exam file exists: ${SLUG}-exam.md"
else
  fail "Exam file missing: ${SLUG}-exam.md"
  echo "Cannot proceed without exam file."
  echo ""
  echo "RESULT: 0 PASS, 1 FAIL, 0 WARN"
  exit 1
fi

if [[ -f "$KEY_FILE" ]]; then
  pass "Answer key exists: ${SLUG}-answer-key.md"
else
  fail "Answer key missing: ${SLUG}-answer-key.md"
fi

if [[ -f "$CONCEPTS_FILE" ]]; then
  pass "Concept map exists: ${SLUG}-concepts.md"
else
  warn "Concept map missing: ${SLUG}-concepts.md"
fi

echo ""

# --- Anti-Memorization Patterns ---
echo "-- Anti-Memorization Patterns --"

ACCORDING_COUNT=$(grep -ci "according to" "$EXAM_FILE" 2>/dev/null) || ACCORDING_COUNT=0
if [[ "$ACCORDING_COUNT" -eq 0 ]]; then
  pass "No 'According to' patterns"
else
  fail "Found $ACCORDING_COUNT 'According to' patterns (memorization cue)"
fi

LESSON_REF_COUNT=$(grep -cE "[Ll]esson [0-9]" "$EXAM_FILE" 2>/dev/null) || LESSON_REF_COUNT=0
if [[ "$LESSON_REF_COUNT" -eq 0 ]]; then
  pass "No 'Lesson N' references"
else
  fail "Found $LESSON_REF_COUNT 'Lesson N' references (memorization cue)"
fi

DOC_STATES_COUNT=$(grep -ci "the document states\|as discussed in\|the chapter describes" "$EXAM_FILE" 2>/dev/null) || DOC_STATES_COUNT=0
if [[ "$DOC_STATES_COUNT" -eq 0 ]]; then
  pass "No document-reference patterns"
else
  fail "Found $DOC_STATES_COUNT document-reference patterns"
fi

echo ""

# --- Internal Tags Leaked ---
echo "-- Internal Tags (must not appear in student exam) --"

TAG_COUNT=$(grep -cE "\[(Scenario Analysis|Concept Relationship|Transfer Application|Critical Evaluation)\]" "$EXAM_FILE" 2>/dev/null) || TAG_COUNT=0
if [[ "$TAG_COUNT" -eq 0 ]]; then
  pass "No question type tags in student exam"
else
  fail "Found $TAG_COUNT internal type tags leaked into student exam"
fi

CONCEPT_TAG_COUNT=$(grep -cE "\[Concept:" "$EXAM_FILE" 2>/dev/null) || CONCEPT_TAG_COUNT=0
if [[ "$CONCEPT_TAG_COUNT" -eq 0 ]]; then
  pass "No [Concept:] tags in student exam"
else
  fail "Found $CONCEPT_TAG_COUNT [Concept:] tags leaked into student exam"
fi

ANSWER_IN_EXAM=$(grep -cE "^\*\*Answer:\*\*|^Answer:" "$EXAM_FILE" 2>/dev/null) || ANSWER_IN_EXAM=0
if [[ "$ANSWER_IN_EXAM" -eq 0 ]]; then
  pass "No answer lines in student exam"
else
  fail "Found $ANSWER_IN_EXAM answer lines leaked into student exam"
fi

REASONING_IN_EXAM=$(grep -cE "^\*\*Reasoning:\*\*|^Reasoning:" "$EXAM_FILE" 2>/dev/null) || REASONING_IN_EXAM=0
if [[ "$REASONING_IN_EXAM" -eq 0 ]]; then
  pass "No reasoning sections in student exam"
else
  fail "Found $REASONING_IN_EXAM reasoning sections leaked into student exam"
fi

echo ""

# --- Answer Distribution (from answer key) ---
echo "-- Answer Distribution --"

if [[ -f "$KEY_FILE" ]]; then
  # Extract answer column from the table (format: | Q | Answer | ...)
  TOTAL=$(grep -cE "^\| [0-9]+ \|" "$KEY_FILE" 2>/dev/null) || TOTAL=0

  if [[ "$TOTAL" -gt 0 ]]; then
    COUNT_A=$(grep -E "^\| [0-9]+ \| A " "$KEY_FILE" 2>/dev/null | wc -l | tr -d ' ')
    COUNT_B=$(grep -E "^\| [0-9]+ \| B " "$KEY_FILE" 2>/dev/null | wc -l | tr -d ' ')
    COUNT_C=$(grep -E "^\| [0-9]+ \| C " "$KEY_FILE" 2>/dev/null | wc -l | tr -d ' ')
    COUNT_D=$(grep -E "^\| [0-9]+ \| D " "$KEY_FILE" 2>/dev/null | wc -l | tr -d ' ')

    PCT_A=$((COUNT_A * 100 / TOTAL))
    PCT_B=$((COUNT_B * 100 / TOTAL))
    PCT_C=$((COUNT_C * 100 / TOTAL))
    PCT_D=$((COUNT_D * 100 / TOTAL))

    echo "  Distribution: A=$COUNT_A($PCT_A%) B=$COUNT_B($PCT_B%) C=$COUNT_C($PCT_C%) D=$COUNT_D($PCT_D%) [Total=$TOTAL]"

    DIST_OK=true
    for letter in A B C D; do
      eval "pct=\$PCT_$letter"
      if [[ "$pct" -lt 20 || "$pct" -gt 30 ]]; then
        fail "Letter $letter at ${pct}% — outside 20-30% range"
        DIST_OK=false
      fi
    done
    if [[ "$DIST_OK" == "true" ]]; then
      pass "All letters within 20-30% range"
    fi

    # Check consecutive same-letter answers
    ANSWERS=$(grep -E "^\| [0-9]+ \|" "$KEY_FILE" | sed 's/.*| \([ABCD]\) .*/\1/')
    MAX_CONSEC=0
    CURRENT_CONSEC=1
    PREV=""
    while IFS= read -r letter; do
      if [[ "$letter" == "$PREV" ]]; then
        ((CURRENT_CONSEC++))
        if [[ "$CURRENT_CONSEC" -gt "$MAX_CONSEC" ]]; then
          MAX_CONSEC=$CURRENT_CONSEC
        fi
      else
        CURRENT_CONSEC=1
      fi
      PREV="$letter"
    done <<< "$ANSWERS"

    if [[ "$MAX_CONSEC" -le 3 ]]; then
      pass "Max consecutive same letter: $MAX_CONSEC (<=3)"
    else
      fail "Max consecutive same letter: $MAX_CONSEC (>3 not allowed)"
    fi
  else
    warn "Could not parse answer distribution from key file"
  fi
else
  warn "Skipping distribution check — no answer key file"
fi

echo ""

# --- Question Count ---
echo "-- Question Count --"

Q_COUNT=$(grep -cE "^Q[0-9]+\." "$EXAM_FILE" 2>/dev/null) || Q_COUNT=0
echo "  Questions found: $Q_COUNT"

if [[ "$Q_COUNT" -ge 30 ]]; then
  pass "Question count >= 30 minimum"
else
  fail "Question count $Q_COUNT is below 30 minimum"
fi

echo ""

# --- Scenario Presence ---
echo "-- Scenario Presence (spot check) --"

# Check first 5 questions have text before the stem (a ? line)
QUESTIONS_WITHOUT_SCENARIO=0
in_question=false
has_text_before_stem=false
q_num=0

while IFS= read -r line; do
  if [[ "$line" =~ ^Q[0-9]+\. ]]; then
    if [[ "$in_question" == "true" && "$has_text_before_stem" == "false" ]]; then
      ((QUESTIONS_WITHOUT_SCENARIO++))
    fi
    in_question=true
    has_text_before_stem=false
    ((q_num++))
    if [[ "$q_num" -gt 10 ]]; then break; fi
  elif [[ "$in_question" == "true" && "$line" =~ \?$ ]]; then
    # This is the stem — check if we saw text before it
    : # stem found
  elif [[ "$in_question" == "true" && -n "$line" && ! "$line" =~ ^[ABCD]\) && ! "$line" =~ ^--- ]]; then
    has_text_before_stem=true
  fi
done < "$EXAM_FILE"

if [[ "$QUESTIONS_WITHOUT_SCENARIO" -eq 0 ]]; then
  pass "First 10 questions all have scenario text before stem"
else
  warn "Found $QUESTIONS_WITHOUT_SCENARIO questions (of first 10) possibly missing scenarios"
fi

echo ""

# --- Summary ---
echo "=== STRUCTURAL SUMMARY ==="
echo "  PASS: $PASS"
echo "  FAIL: $FAIL"
echo "  WARN: $WARN"
echo ""

if [[ "$FAIL" -eq 0 ]]; then
  echo "  VERDICT: PASS (all structural checks passed)"
  exit 0
else
  echo "  VERDICT: FAIL ($FAIL structural failures detected)"
  exit 1
fi
