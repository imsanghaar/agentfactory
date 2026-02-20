#!/usr/bin/env bash
# Track subagent spawning (SubagentStart event)
# Triggered by: SubagentStart
# Different from Task PreToolUse - this fires when actual subagent starts

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0

AGENT_ID=$(parse_json "$INPUT" "agent_id") || AGENT_ID="unknown"
AGENT_TYPE=$(parse_json "$INPUT" "agent_type") || AGENT_TYPE="unknown"
SESSION_ID=$(parse_json "$INPUT" "session_id") || SESSION_ID="unknown"

log_event "subagents" "$SESSION_ID" \
    "event" "start" \
    "agent_id" "$AGENT_ID" \
    "agent_type" "$AGENT_TYPE"

# Store start time for duration calculation
echo "$(get_timestamp)" > "$CONTEXT_DIR/subagents/.start-$AGENT_ID"

exit 0
