#!/usr/bin/env bash
# Observability: Track Task tool completion
# Triggered by: PostToolUse on Task

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0
validate_json "$INPUT" 2>/dev/null || exit 0

TOOL=$(parse_json "$INPUT" "tool_name" 2>/dev/null) || exit 0
[ "$TOOL" != "Task" ] && exit 0

SESSION_ID=$(parse_json "$INPUT" "session_id" 2>/dev/null) || SESSION_ID="unknown"
SUBAGENT_TYPE=$(parse_json "$INPUT" "tool_input.subagent_type" 2>/dev/null) || SUBAGENT_TYPE="unknown"
TOOL_OUTPUT=$(parse_json "$INPUT" "tool_result" 2>/dev/null) || TOOL_OUTPUT=""

# Try to extract agent_id from output
AGENT_ID=$(echo "$TOOL_OUTPUT" | grep -oE 'agentId: [a-zA-Z0-9]+' | head -1 | cut -d' ' -f2 2>/dev/null) || AGENT_ID=""

if [ -z "$AGENT_ID" ]; then
    PENDING_FILE="$CONTEXT_DIR/tasks/.pending-task-$SESSION_ID"
    if [ -f "$PENDING_FILE" ]; then
        AGENT_ID=$(cat "$PENDING_FILE" 2>/dev/null) || AGENT_ID="unknown"
        rm -f "$PENDING_FILE" 2>/dev/null || true
    else
        AGENT_ID="unknown"
    fi
fi

STATUS="success"
if echo "$TOOL_OUTPUT" | grep -qiE 'error|failed|exception|timeout' 2>/dev/null; then
    STATUS="failure"
fi

# Get original prompt that was given to subagent
ORIGINAL_PROMPT=$(get_subagent_prompt "$AGENT_ID")

# Log with full details
log_event "tasks" "$SESSION_ID" \
    "event" "end" \
    "agent_id" "$AGENT_ID" \
    "subagent_type" "$SUBAGENT_TYPE" \
    "status" "$STATUS" \
    "original_prompt" "${ORIGINAL_PROMPT:0:500}" \
    "output_summary" "${TOOL_OUTPUT:0:500}"

# Cleanup stored prompt
cleanup_subagent_files "$AGENT_ID"

exit 0
