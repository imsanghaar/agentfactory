#!/usr/bin/env bash
# Team: Notify when Claude completes a response
# Triggered by: Stop
# Useful for async/background work

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || true

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0

STOP_HOOK_ACTIVE=$(parse_json "$INPUT" "stop_hook_active" || echo "false")

# Don't notify if in a continuation loop
if [ "$STOP_HOOK_ACTIVE" = "true" ]; then
    exit 0
fi

SESSION_ID=$(parse_json "$INPUT" "session_id" || echo "")
CWD=$(parse_json "$INPUT" "cwd" || echo "")

SHORT_SESSION=""
[ -n "$SESSION_ID" ] && SHORT_SESSION="${SESSION_ID:0:8}"

PROJECT_NAME=""
[ -n "$CWD" ] && PROJECT_NAME=$(basename "$CWD")

MESSAGE="Task completed"
[ -n "$SHORT_SESSION" ] && MESSAGE="$MESSAGE (session: $SHORT_SESSION)"
[ -n "$PROJECT_NAME" ] && MESSAGE="$MESSAGE in $PROJECT_NAME"

notify_team "Claude Code Complete" "$MESSAGE" "info"

exit 0
