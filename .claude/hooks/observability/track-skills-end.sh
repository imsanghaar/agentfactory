#!/usr/bin/env bash
# Observability: Track skill completion
# Triggered by: PostToolUse on Skill
# Tracks which agent used skill + duration

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0
validate_json "$INPUT" 2>/dev/null || exit 0

TOOL=$(parse_json "$INPUT" "tool_name" 2>/dev/null) || exit 0
[ "$TOOL" != "Skill" ] && exit 0

SKILL_NAME=$(parse_json "$INPUT" "tool_input.skill" 2>/dev/null) || exit 0
SESSION_ID=$(parse_json "$INPUT" "session_id" 2>/dev/null) || SESSION_ID="unknown"

[ -z "$SKILL_NAME" ] && exit 0

# Detect invoker (main agent or subagent)
TRANSCRIPT_PATH=$(parse_json "$INPUT" "transcript_path" 2>/dev/null) || TRANSCRIPT_PATH=""
AGENT_TYPE=$(parse_json "$INPUT" "agent_type" 2>/dev/null) || AGENT_TYPE=""

INVOKER="main"
if echo "$TRANSCRIPT_PATH" | grep -q "subagents/" 2>/dev/null; then
    INVOKER=$(basename "$TRANSCRIPT_PATH" .jsonl 2>/dev/null) || INVOKER="subagent"
elif [ -n "$AGENT_TYPE" ]; then
    INVOKER="$AGENT_TYPE"
fi

# Determine status from result
TOOL_RESULT=$(parse_json "$INPUT" "tool_result" 2>/dev/null) || TOOL_RESULT=""
TOOL_RESPONSE=$(parse_json "$INPUT" "tool_response" 2>/dev/null) || TOOL_RESPONSE=""
STATUS="success"
if echo "$TOOL_RESULT$TOOL_RESPONSE" | grep -qiE 'error|failed|exception|blocked' 2>/dev/null; then
    STATUS="failure"
fi

# Calculate duration if start time exists
DURATION_MS="unknown"
START_FILE="$CONTEXT_DIR/.skill-start-$SESSION_ID-$SKILL_NAME"
if [ -f "$START_FILE" ]; then
    rm -f "$START_FILE"
fi

# Log with full context
log_event "skills" "$SESSION_ID" \
    "event" "end" \
    "skill" "$SKILL_NAME" \
    "status" "$STATUS" \
    "invoked_by" "$INVOKER" \
    "output_size" "${#TOOL_RESPONSE}"

# Mark interview completion if interview skill
if [ "$SKILL_NAME" = "interview" ] && [ "$STATUS" = "success" ]; then
    mark_interviewed "$SESSION_ID"
fi

exit 0
