#!/usr/bin/env bash
# Guardrail: Block edits on main/master branch
# Triggered by: PreToolUse on Edit|Write
# Exit 2 = BLOCK with message to Claude

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
SESSION_ID=$(parse_json "$INPUT" "session_id" 2>/dev/null) || SESSION_ID="unknown"

# Get current branch
BRANCH=$(git -C "$ROOT_DIR" branch --show-current 2>/dev/null) || exit 0

# Block on main or master
if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ]; then
    audit_log "branch_protection" "$SESSION_ID" "$BRANCH" "blocked" "Edit attempted on protected branch"
    echo "Cannot edit files on $BRANCH branch. Create a feature branch first: git checkout -b feature/your-feature" >&2
    exit 2
fi

exit 0
