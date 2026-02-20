#!/usr/bin/env bash
# Observability: Track skill invocations (start)
# Triggered by: PreToolUse on Skill
# Now tracks which agent (main or subagent) used the skill

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
SKILL_ARGS=$(parse_json "$INPUT" "tool_input.args" 2>/dev/null) || SKILL_ARGS=""

# Try to detect if this is from a subagent
# Check transcript_path for subagent pattern or agent_type field
TRANSCRIPT_PATH=$(parse_json "$INPUT" "transcript_path" 2>/dev/null) || TRANSCRIPT_PATH=""
AGENT_TYPE=$(parse_json "$INPUT" "agent_type" 2>/dev/null) || AGENT_TYPE=""

INVOKER="main"
if echo "$TRANSCRIPT_PATH" | grep -q "subagents/" 2>/dev/null; then
    # Extract subagent ID from path
    INVOKER=$(basename "$TRANSCRIPT_PATH" .jsonl 2>/dev/null) || INVOKER="subagent"
elif [ -n "$AGENT_TYPE" ]; then
    INVOKER="$AGENT_TYPE"
fi

[ -z "$SKILL_NAME" ] && exit 0

# Log with agent context
log_event "skills" "$SESSION_ID" \
    "event" "start" \
    "skill" "$SKILL_NAME" \
    "args" "$SKILL_ARGS" \
    "invoked_by" "$INVOKER"

# Store start time
echo "$(get_timestamp)" > "$CONTEXT_DIR/.skill-start-$SESSION_ID-$SKILL_NAME"

exit 0
