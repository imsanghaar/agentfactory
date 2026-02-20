#!/usr/bin/env bash
# Observability: Track Task tool (subagent) invocations
# Triggered by: PreToolUse on Task

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0
validate_json "$INPUT" 2>/dev/null || exit 0

TOOL=$(parse_json "$INPUT" "tool_name" 2>/dev/null) || exit 0
[ "$TOOL" != "Task" ] && exit 0

SUBAGENT_TYPE=$(parse_json "$INPUT" "tool_input.subagent_type" 2>/dev/null) || SUBAGENT_TYPE="unknown"
PROMPT=$(parse_json "$INPUT" "tool_input.prompt" 2>/dev/null) || PROMPT=""
SESSION_ID=$(parse_json "$INPUT" "session_id" 2>/dev/null) || SESSION_ID="unknown"
MODEL=$(parse_json "$INPUT" "tool_input.model" 2>/dev/null) || MODEL="inherit"
RUN_IN_BACKGROUND=$(parse_json "$INPUT" "tool_input.run_in_background" 2>/dev/null) || RUN_IN_BACKGROUND="false"
DESCRIPTION=$(parse_json "$INPUT" "tool_input.description" 2>/dev/null) || DESCRIPTION=""

TEMP_AGENT_ID="pending-$(date +%s)-$$"
echo "$TEMP_AGENT_ID" > "$CONTEXT_DIR/tasks/.pending-task-$SESSION_ID"

# Store FULL prompt for later retrieval (not truncated)
store_subagent_prompt "$TEMP_AGENT_ID" "$PROMPT" "$SUBAGENT_TYPE"

# Log with full context including model and background flag
PROMPT_SUMMARY="${PROMPT:0:300}"
log_event "tasks" "$SESSION_ID" \
    "event" "start" \
    "agent_id" "$TEMP_AGENT_ID" \
    "subagent_type" "$SUBAGENT_TYPE" \
    "description" "$DESCRIPTION" \
    "model" "$MODEL" \
    "run_in_background" "$RUN_IN_BACKGROUND" \
    "prompt_summary" "$PROMPT_SUMMARY" \
    "prompt_length" "${#PROMPT}"

exit 0
