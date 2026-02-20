#!/usr/bin/env bash
# Track setup/initialization events
# Triggered by: Setup (--init, --init-only, --maintenance)

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0

SESSION_ID=$(parse_json "$INPUT" "session_id") || SESSION_ID="unknown"
TRIGGER=$(parse_json "$INPUT" "trigger") || TRIGGER="unknown"

log_event "system" "$SESSION_ID" \
    "event" "setup" \
    "trigger" "$TRIGGER"

# Output helpful context for Claude
echo "<setup-hook>"
echo "Setup triggered: $TRIGGER"
echo "Project: $(basename "$ROOT_DIR")"
echo "Branch: $(get_branch)"
echo "User: $(get_user)"
echo "</setup-hook>"

exit 0
