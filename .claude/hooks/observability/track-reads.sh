#!/usr/bin/env bash
# Track file read operations
# Triggered by: PostToolUse on Read
# Useful for understanding what context Claude gathered

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0

TOOL=$(parse_json "$INPUT" "tool_name") || exit 0
[ "$TOOL" != "Read" ] && exit 0

SESSION_ID=$(parse_json "$INPUT" "session_id") || SESSION_ID="unknown"
FILE_PATH=$(parse_json "$INPUT" "tool_input.file_path") || exit 0
OFFSET=$(parse_json "$INPUT" "tool_input.offset") || OFFSET="0"
LIMIT=$(parse_json "$INPUT" "tool_input.limit") || LIMIT="full"

log_event "reads" "$SESSION_ID" \
    "event" "file_read" \
    "file_path" "$FILE_PATH" \
    "offset" "$OFFSET" \
    "limit" "$LIMIT"

exit 0
