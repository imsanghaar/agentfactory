#!/usr/bin/env bash
# Team: Notify when Claude needs permission
# Triggered by: Notification (permission_prompt)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || true

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0

NOTIFICATION_TYPE=$(parse_json "$INPUT" "notification_type" || echo "")
MESSAGE=$(parse_json "$INPUT" "message" || echo "Claude needs your attention")
SESSION_ID=$(parse_json "$INPUT" "session_id" || echo "")

case "$NOTIFICATION_TYPE" in
    "permission_prompt")
        notify_team "Permission Required" "$MESSAGE" "warning"
        ;;
    "idle_prompt")
        notify_team "Claude Waiting" "$MESSAGE" "info"
        ;;
    *)
        notify_team "Claude Notification" "$MESSAGE" "info"
        ;;
esac

exit 0
