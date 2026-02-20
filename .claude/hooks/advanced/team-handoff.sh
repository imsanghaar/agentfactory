#!/usr/bin/env bash
# Advanced: Generate handoff summary when session ends
# Triggered by: SessionEnd
# Creates a summary for the next team member or session

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
SESSION_ID=$(parse_json "$INPUT" "session_id" 2>/dev/null) || SESSION_ID="unknown"

HANDOFF_DIR="$ROOT_DIR/.claude/handoffs"
mkdir -p "$HANDOFF_DIR" 2>/dev/null || exit 0

HANDOFF_FILE="$HANDOFF_DIR/handoff-${SESSION_ID:0:8}-$(date +%Y%m%d-%H%M%S).md"

# Gather session summary
{
    echo "# Session Handoff Summary"
    echo ""
    echo "**Session ID:** ${SESSION_ID:0:8}"
    echo "**Date:** $(date -u +"%Y-%m-%d %H:%M:%S UTC")"
    echo "**Branch:** $(git branch --show-current 2>/dev/null || echo "unknown")"
    echo ""

    echo "## Files Modified"
    git diff --name-only HEAD~5 2>/dev/null | head -20 || echo "No recent changes"
    echo ""

    echo "## Commits This Session"
    git log --oneline -5 2>/dev/null || echo "No commits"
    echo ""

    echo "## Outstanding TODOs"
    grep -r "TODO\|FIXME" --include="*.ts" --include="*.py" --include="*.go" . 2>/dev/null | head -10 || echo "None found"
    echo ""

    echo "## Skills Used"
    if [ -f "$LOGS_DIR/skills.jsonl" ]; then
        grep "$SESSION_ID" "$LOGS_DIR/skills.jsonl" 2>/dev/null | \
            jq -r '.skill' 2>/dev/null | sort | uniq -c | sort -rn | head -5 || echo "None"
    else
        echo "No skill logs"
    fi
    echo ""

    echo "## Next Steps"
    echo "*(Add your notes here)*"
    echo ""

} > "$HANDOFF_FILE" 2>/dev/null

# Notify team about handoff
notify_team "Session Handoff Ready" "Handoff summary created: $HANDOFF_FILE" "info"

exit 0
