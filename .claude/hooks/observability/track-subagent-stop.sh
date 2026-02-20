#!/usr/bin/env bash
# Track subagent completion (SubagentStop event)
# Triggered by: SubagentStop
# Contains agent_transcript_path for full subagent conversation!

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0

AGENT_ID=$(parse_json "$INPUT" "agent_id") || AGENT_ID="unknown"
SESSION_ID=$(parse_json "$INPUT" "session_id") || SESSION_ID="unknown"
TRANSCRIPT_PATH=$(parse_json "$INPUT" "agent_transcript_path") || TRANSCRIPT_PATH=""
STOP_HOOK_ACTIVE=$(parse_json "$INPUT" "stop_hook_active") || STOP_HOOK_ACTIVE="false"

# Get original prompt if we stored it
ORIGINAL_PROMPT=$(get_subagent_prompt "$AGENT_ID")

# Calculate duration if start time exists
DURATION="unknown"
START_FILE="$CONTEXT_DIR/subagents/.start-$AGENT_ID"
if [ -f "$START_FILE" ]; then
    START_TIME=$(cat "$START_FILE")
    rm -f "$START_FILE"
    # Duration calculation would need epoch - simplified here
fi

# Get summary from transcript if available
SUMMARY=""
if [ -n "$TRANSCRIPT_PATH" ] && [ -f "$TRANSCRIPT_PATH" ]; then
    # Get last few lines of transcript for summary
    SUMMARY=$(tail -5 "$TRANSCRIPT_PATH" | head -c 500)
fi

log_event "subagents" "$SESSION_ID" \
    "event" "stop" \
    "agent_id" "$AGENT_ID" \
    "transcript_path" "$TRANSCRIPT_PATH" \
    "prompt_given" "${ORIGINAL_PROMPT:0:300}" \
    "summary" "${SUMMARY:0:300}"

# Cleanup stored prompt
cleanup_subagent_files "$AGENT_ID"

exit 0
