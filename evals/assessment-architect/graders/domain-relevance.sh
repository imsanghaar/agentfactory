#!/bin/bash
# domain-relevance.sh — Checks whether exam scenarios are in the chapter's domain
# Usage: ./domain-relevance.sh <SLUG> [chapter-path]
# Example: ./domain-relevance.sh ch3-4-general-agents-seven-principles apps/learn-app/docs/01-General-Agents-Foundations/03-general-agents

set -euo pipefail

SLUG="${1:?Usage: domain-relevance.sh <SLUG> [chapter-path]}"
CHAPTER_PATH="${2:-}"
ASSESSMENTS_DIR="$(cd "$(dirname "$0")/../.." && pwd)/../assessments"
EXAM_FILE="$ASSESSMENTS_DIR/${SLUG}-exam.md"

if [[ ! -f "$EXAM_FILE" ]]; then
  echo "ERROR: Exam file not found: $EXAM_FILE"
  exit 1
fi

echo "=== Domain Relevance Check: $SLUG ==="
echo ""

# --- Detect chapter type and domain keywords ---
# Off-domain indicators: scenarios set in industries unrelated to software/AI development
OFF_DOMAIN_KEYWORDS=(
  "medical" "hospital" "patient" "radiology" "radiologist" "tumor" "imaging"
  "law firm" "attorney" "legal" "paralegal" "litigation"
  "manufacturing" "factory" "assembly line" "warehouse"
  "pharmaceutical" "clinical trial" "drug"
  "restaurant" "chef" "kitchen" "menu"
  "farming" "agriculture" "crop" "harvest"
  "airline" "pilot" "flight" "aviation"
  "retail" "store manager" "inventory"
  "insurance" "claims" "policyholder"
  "real estate" "property" "landlord"
  "banking" "loan officer" "mortgage"
  "mining" "drilling" "extraction"
  "logistics" "shipping" "freight"
)

# In-domain indicators for a practical-tool chapter about Claude Code / AI agents
# NOTE: Generic terms like "AI", "team", "data" excluded — they appear in any domain
# These keywords must specifically signal software development context
IN_DOMAIN_KEYWORDS=(
  "developer" "code" "coding" "programming" "software"
  "repository" "repo" "codebase" "source code"
  "deploy" "CI" "pipeline" "unit test" "debug" "debugging"
  "API" "server" "endpoint" "microservice"
  "Claude Code" "Claude" "LLM" "agent"
  "skill" "subagent" "hook" "MCP" "plugin"
  "git" "commit" "branch" "merge" "pull request"
  "terminal" "command" "shell" "CLI" "bash"
  "engineer" "architect" "DevOps" "SRE"
  "refactor" "migration" "config" "configuration"
  "container" "Kubernetes" "Docker"
  "startup" "tech company"
  "IDE" "editor" "linter" "formatter"
)

# --- Extract scenarios from questions ---
echo "-- Extracting scenarios from exam questions --"
echo ""

TOTAL_QUESTIONS=0
OFF_DOMAIN_COUNT=0
IN_DOMAIN_COUNT=0
NEUTRAL_COUNT=0
OFF_DOMAIN_QUESTIONS=()

# Extract each question's scenario text (lines between Q#. and the first option A))
current_scenario=""
current_q=""
in_scenario=false

while IFS= read -r line; do
  if [[ "$line" =~ ^Q([0-9]+)\. ]]; then
    # Process previous question if exists
    if [[ -n "$current_scenario" ]]; then
      ((TOTAL_QUESTIONS++))
      scenario_lower=$(echo "$current_scenario" | tr '[:upper:]' '[:lower:]')

      found_off=false
      off_match=""
      for kw in "${OFF_DOMAIN_KEYWORDS[@]}"; do
        if echo "$scenario_lower" | grep -qi "$kw"; then
          found_off=true
          off_match="$kw"
          break
        fi
      done

      found_in=false
      for kw in "${IN_DOMAIN_KEYWORDS[@]}"; do
        if echo "$scenario_lower" | grep -qi "$kw"; then
          found_in=true
          break
        fi
      done

      if [[ "$found_off" == "true" && "$found_in" == "false" ]]; then
        ((OFF_DOMAIN_COUNT++))
        OFF_DOMAIN_QUESTIONS+=("$current_q (domain: '$off_match')")
      elif [[ "$found_in" == "true" ]]; then
        ((IN_DOMAIN_COUNT++))
      else
        ((NEUTRAL_COUNT++))
      fi
    fi

    current_q="${BASH_REMATCH[0]}"
    current_scenario=""
    in_scenario=true
  elif [[ "$in_scenario" == "true" ]]; then
    if [[ "$line" =~ ^[ABCD]\) ]]; then
      in_scenario=false
    elif [[ "$line" != "---" && -n "$line" ]]; then
      current_scenario="$current_scenario $line"
    fi
  fi
done < "$EXAM_FILE"

# Process last question
if [[ -n "$current_scenario" ]]; then
  ((TOTAL_QUESTIONS++))
  scenario_lower=$(echo "$current_scenario" | tr '[:upper:]' '[:lower:]')

  found_off=false
  off_match=""
  for kw in "${OFF_DOMAIN_KEYWORDS[@]}"; do
    if echo "$scenario_lower" | grep -qi "$kw"; then
      found_off=true
      off_match="$kw"
      break
    fi
  done

  found_in=false
  for kw in "${IN_DOMAIN_KEYWORDS[@]}"; do
    if echo "$scenario_lower" | grep -qi "$kw"; then
      found_in=true
      break
    fi
  done

  if [[ "$found_off" == "true" && "$found_in" == "false" ]]; then
    ((OFF_DOMAIN_COUNT++))
    OFF_DOMAIN_QUESTIONS+=("$current_q (domain: '$off_match')")
  elif [[ "$found_in" == "true" ]]; then
    ((IN_DOMAIN_COUNT++))
  else
    ((NEUTRAL_COUNT++))
  fi
fi

echo "-- Results --"
echo "  Total questions analyzed: $TOTAL_QUESTIONS"
echo "  In-domain (development/AI/tools): $IN_DOMAIN_COUNT"
echo "  Off-domain (unrelated industry): $OFF_DOMAIN_COUNT"
echo "  Neutral (no clear domain signal): $NEUTRAL_COUNT"
echo ""

if [[ "$TOTAL_QUESTIONS" -gt 0 ]]; then
  IN_PCT=$((IN_DOMAIN_COUNT * 100 / TOTAL_QUESTIONS))
  OFF_PCT=$((OFF_DOMAIN_COUNT * 100 / TOTAL_QUESTIONS))
  NEUTRAL_PCT=$((NEUTRAL_COUNT * 100 / TOTAL_QUESTIONS))
  echo "  In-domain: ${IN_PCT}%"
  echo "  Off-domain: ${OFF_PCT}%"
  echo "  Neutral: ${NEUTRAL_PCT}%"
else
  IN_PCT=0
  OFF_PCT=0
fi

echo ""

# --- Report off-domain questions ---
if [[ "${#OFF_DOMAIN_QUESTIONS[@]}" -gt 0 ]]; then
  echo "-- Off-Domain Questions (flagged) --"
  for q in "${OFF_DOMAIN_QUESTIONS[@]}"; do
    echo "  FLAG: $q"
  done
  echo ""
fi

# --- Scoring ---
echo "-- Domain Relevance Score --"

# Score: 100 if all in-domain, penalize for off-domain
if [[ "$TOTAL_QUESTIONS" -gt 0 ]]; then
  # Each off-domain question reduces score proportionally
  # Score = 100 - (off_domain_pct * 1.5) — penalty is amplified since off-domain is a serious issue
  PENALTY=$((OFF_PCT * 3 / 2))
  SCORE=$((100 - PENALTY))
  if [[ "$SCORE" -lt 0 ]]; then SCORE=0; fi
else
  SCORE=0
fi

echo "  SCORE: $SCORE/100"
echo ""

# --- Verdict ---
if [[ "$SCORE" -ge 90 ]]; then
  echo "  VERDICT: EXCELLENT — scenarios are well-grounded in chapter domain"
elif [[ "$SCORE" -ge 75 ]]; then
  echo "  VERDICT: GOOD — minor domain drift detected"
elif [[ "$SCORE" -ge 60 ]]; then
  echo "  VERDICT: NEEDS WORK — several off-domain scenarios"
else
  echo "  VERDICT: FAIL — significant domain mismatch"
fi

# Output score for run-eval.sh to parse
echo ""
echo "DOMAIN_RELEVANCE_SCORE=$SCORE"
