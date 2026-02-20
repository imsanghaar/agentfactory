#!/usr/bin/env bash
# Observability: Track all file modifications
# Triggered by: PostToolUse on Edit|Write

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0
validate_json "$INPUT" 2>/dev/null || exit 0

TOOL=$(parse_json "$INPUT" "tool_name" 2>/dev/null) || exit 0
FILE_PATH=$(parse_json "$INPUT" "tool_input.file_path" 2>/dev/null) || exit 0
SESSION_ID=$(parse_json "$INPUT" "session_id" 2>/dev/null) || SESSION_ID="unknown"

[ -z "$FILE_PATH" ] && exit 0

# Get file size if exists
FILE_SIZE="0"
if [ -f "$FILE_PATH" ]; then
    FILE_SIZE=$(wc -c < "$FILE_PATH" 2>/dev/null || echo "0")
fi

# Determine file type
FILE_EXT="${FILE_PATH##*.}"

audit_log "file_modified" "$SESSION_ID" "$FILE_PATH" "$TOOL" "size=$FILE_SIZE ext=$FILE_EXT"

exit 0
