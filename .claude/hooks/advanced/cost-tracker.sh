#!/usr/bin/env bash
# Advanced: Track estimated API costs per session
# Triggered by: PostToolUse on Task (subagent usage)
# Estimates token consumption for budget awareness

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
TOOL=$(parse_json "$INPUT" "tool_name" 2>/dev/null) || exit 0

[ "$TOOL" != "Task" ] && exit 0

SESSION_ID=$(parse_json "$INPUT" "session_id" 2>/dev/null) || SESSION_ID="unknown"
SUBAGENT_TYPE=$(parse_json "$INPUT" "tool_input.subagent_type" 2>/dev/null) || SUBAGENT_TYPE="unknown"
PROMPT=$(parse_json "$INPUT" "tool_input.prompt" 2>/dev/null) || PROMPT=""
OUTPUT=$(parse_json "$INPUT" "tool_result" 2>/dev/null) || OUTPUT=""

# Rough token estimation (1 token ≈ 4 chars)
PROMPT_CHARS=${#PROMPT}
OUTPUT_CHARS=${#OUTPUT}
ESTIMATED_TOKENS=$(( (PROMPT_CHARS + OUTPUT_CHARS) / 4 ))

# Cost estimates (very rough, adjust for your pricing tier)
# Sonnet: ~$3/1M input, ~$15/1M output
# Opus: ~$15/1M input, ~$75/1M output
COST_PER_1K_TOKENS="0.01"  # Simplified average

ESTIMATED_COST=$(echo "scale=4; $ESTIMATED_TOKENS * $COST_PER_1K_TOKENS / 1000" | bc 2>/dev/null || echo "0")

# Track in cost log
COST_FILE="$LOGS_DIR/costs.jsonl"
ENTRY=$(create_json \
    "timestamp" "$(get_timestamp)" \
    "session_id" "$SESSION_ID" \
    "subagent_type" "$SUBAGENT_TYPE" \
    "estimated_tokens" "$ESTIMATED_TOKENS" \
    "estimated_cost_usd" "$ESTIMATED_COST")

write_jsonl "$COST_FILE" "$ENTRY"

# Warn if session is getting expensive
TOTAL_SESSION_COST=$(grep "$SESSION_ID" "$COST_FILE" 2>/dev/null | \
    jq -s '[.[].estimated_cost_usd | tonumber] | add' 2>/dev/null || echo "0")

if [ "$(echo "$TOTAL_SESSION_COST > 1.00" | bc 2>/dev/null)" = "1" ]; then
    echo "<cost-warning>"
    echo "Session cost estimate: \$$TOTAL_SESSION_COST"
    echo "Consider completing the task to manage costs."
    echo "</cost-warning>"
fi

exit 0
