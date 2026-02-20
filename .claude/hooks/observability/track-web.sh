#!/usr/bin/env bash
# Track web searches and fetches
# Triggered by: PostToolUse on WebSearch|WebFetch
# Useful for understanding research patterns

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0

TOOL=$(parse_json "$INPUT" "tool_name") || exit 0
SESSION_ID=$(parse_json "$INPUT" "session_id") || SESSION_ID="unknown"

case "$TOOL" in
    WebSearch)
        QUERY=$(parse_json "$INPUT" "tool_input.query") || QUERY=""
        log_event "web" "$SESSION_ID" \
            "event" "search" \
            "query" "$QUERY"
        ;;
    WebFetch)
        URL=$(parse_json "$INPUT" "tool_input.url") || URL=""
        PROMPT=$(parse_json "$INPUT" "tool_input.prompt") || PROMPT=""
        log_event "web" "$SESSION_ID" \
            "event" "fetch" \
            "url" "$URL" \
            "prompt" "${PROMPT:0:200}"
        ;;
    *)
        exit 0
        ;;
esac

exit 0
