#!/usr/bin/env bash
# Track tool failures (critical for debugging!)
# Triggered by: PostToolUseFailure (all tools)

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0

TOOL=$(parse_json "$INPUT" "tool_name") || exit 0
SESSION_ID=$(parse_json "$INPUT" "session_id") || SESSION_ID="unknown"
TOOL_RESPONSE=$(parse_json "$INPUT" "tool_response") || TOOL_RESPONSE=""

# Extract error details
ERROR=$(echo "$TOOL_RESPONSE" | head -c 500)

# Extract what was attempted
case "$TOOL" in
    Bash)
        ATTEMPTED=$(parse_json "$INPUT" "tool_input.command") || ATTEMPTED=""
        ;;
    Edit|Write)
        ATTEMPTED=$(parse_json "$INPUT" "tool_input.file_path") || ATTEMPTED=""
        ;;
    *)
        ATTEMPTED=$(parse_json "$INPUT" "tool_input" | head -c 200) || ATTEMPTED=""
        ;;
esac

log_event "errors" "$SESSION_ID" \
    "event" "tool_failure" \
    "tool" "$TOOL" \
    "attempted" "$ATTEMPTED" \
    "error" "$ERROR"

# Notify team on critical failures
if echo "$ERROR" | grep -qiE "permission denied|access denied|forbidden|unauthorized" 2>/dev/null; then
    notify_team "Tool Failure: $TOOL" "Permission issue: $ATTEMPTED" "warning"
fi

exit 0
