#!/usr/bin/env bash
# Observability: Track all user prompts
# Triggered by: UserPromptSubmit
# Never block - always exit 0

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0
validate_json "$INPUT" 2>/dev/null || exit 0

PROMPT=$(parse_json "$INPUT" "prompt" 2>/dev/null) || exit 0
SESSION_ID=$(parse_json "$INPUT" "session_id" 2>/dev/null) || SESSION_ID="unknown"

[ -z "$PROMPT" ] && exit 0

TIMESTAMP=$(get_timestamp)

LOG_ENTRY=$(create_json \
    "timestamp" "$TIMESTAMP" \
    "session_id" "$SESSION_ID" \
    "prompt" "$PROMPT")

write_jsonl "$LOGS_DIR/prompts.jsonl" "$LOG_ENTRY"

exit 0
