#!/usr/bin/env bash
# Track permission requests (what Claude asked for)
# Triggered by: PermissionRequest (all tools)

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0

TOOL=$(parse_json "$INPUT" "tool_name") || exit 0
SESSION_ID=$(parse_json "$INPUT" "session_id") || SESSION_ID="unknown"
TOOL_INPUT=$(parse_json "$INPUT" "tool_input") || TOOL_INPUT="{}"

# Extract key details based on tool type
case "$TOOL" in
    Bash)
        DETAIL=$(parse_json "$INPUT" "tool_input.command") || DETAIL=""
        ;;
    Edit|Write|Read)
        DETAIL=$(parse_json "$INPUT" "tool_input.file_path") || DETAIL=""
        ;;
    *)
        DETAIL=$(echo "$TOOL_INPUT" | head -c 200)
        ;;
esac

log_event "permissions" "$SESSION_ID" \
    "event" "request" \
    "tool" "$TOOL" \
    "detail" "$DETAIL"

exit 0
