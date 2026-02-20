#!/usr/bin/env bash
# Track MCP tool usage
# Triggered by: PostToolUse on mcp__*
# MCP tools follow pattern: mcp__{server}__{tool}

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0

TOOL=$(parse_json "$INPUT" "tool_name") || exit 0

# Only track MCP tools (start with mcp__)
case "$TOOL" in
    mcp__*)
        ;;
    *)
        exit 0
        ;;
esac

SESSION_ID=$(parse_json "$INPUT" "session_id") || SESSION_ID="unknown"
TOOL_INPUT=$(parse_json "$INPUT" "tool_input") || TOOL_INPUT="{}"
TOOL_RESPONSE=$(parse_json "$INPUT" "tool_response") || TOOL_RESPONSE=""

# Parse server and tool from name (mcp__{server}__{tool})
MCP_SERVER=$(echo "$TOOL" | cut -d'_' -f4)
MCP_TOOL=$(echo "$TOOL" | cut -d'_' -f6-)

log_event "mcp" "$SESSION_ID" \
    "event" "tool_use" \
    "server" "$MCP_SERVER" \
    "tool" "$MCP_TOOL" \
    "input" "${TOOL_INPUT:0:300}" \
    "response_size" "${#TOOL_RESPONSE}"

exit 0
