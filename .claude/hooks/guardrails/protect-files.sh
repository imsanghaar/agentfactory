#!/usr/bin/env bash
# Guardrail: Protect sensitive files from accidental modification
# Triggered by: PreToolUse on Edit|Write
# Exit 2 = BLOCK with message to Claude

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0
validate_json "$INPUT" 2>/dev/null || exit 0

FILE_PATH=$(parse_json "$INPUT" "tool_input.file_path" 2>/dev/null) || exit 0
SESSION_ID=$(parse_json "$INPUT" "session_id" 2>/dev/null) || SESSION_ID="unknown"

[ -z "$FILE_PATH" ] && exit 0

# Check if file is protected
if is_protected_file "$FILE_PATH"; then
    audit_log "file_protection" "$SESSION_ID" "$FILE_PATH" "blocked" "Protected file modification attempted"

    # Return JSON to ask user for permission
    echo '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"This file is protected. Please confirm you want to modify it."}}'
    exit 0
fi

exit 0
