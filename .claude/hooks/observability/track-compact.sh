#!/usr/bin/env bash
# Track context compaction events
# Triggered by: PreCompact
# Important for understanding context window usage

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0

SESSION_ID=$(parse_json "$INPUT" "session_id") || SESSION_ID="unknown"
TRIGGER=$(parse_json "$INPUT" "trigger") || TRIGGER="unknown"
CUSTOM_INSTRUCTIONS=$(parse_json "$INPUT" "custom_instructions") || CUSTOM_INSTRUCTIONS=""

log_event "system" "$SESSION_ID" \
    "event" "context_compact" \
    "trigger" "$TRIGGER" \
    "custom_instructions" "$CUSTOM_INSTRUCTIONS"

# If auto-triggered, this means context was full - worth noting
if [ "$TRIGGER" = "auto" ]; then
    notify_team "Context Compaction" "Session ${SESSION_ID:0:8} auto-compacted (context full)" "info"
fi

exit 0
