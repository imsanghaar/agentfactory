#!/usr/bin/env bash
# Advanced: Intelligent stop hook that evaluates task completion
# Triggered by: Stop
# Uses prompt-based hook to decide if Claude should continue

# This script outputs JSON that tells Claude Code whether to continue
# Based on checking for uncommitted work, failing tests, etc.

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
STOP_HOOK_ACTIVE=$(parse_json "$INPUT" "stop_hook_active" 2>/dev/null) || STOP_HOOK_ACTIVE="false"

# Prevent infinite loops
if [ "$STOP_HOOK_ACTIVE" = "true" ]; then
    exit 0
fi

SHOULD_CONTINUE="false"
REASON=""

# Check for uncommitted changes
if command -v git &>/dev/null; then
    UNCOMMITTED=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
    if [ "$UNCOMMITTED" -gt 0 ]; then
        # Don't force continue for uncommitted - let git-auto-commit handle it
        :
    fi
fi

# Check for failing tests (if test command exists in package.json)
if [ -f "package.json" ] && command -v npm &>/dev/null; then
    if grep -q '"test"' package.json 2>/dev/null; then
        # Could run: npm test --silent 2>/dev/null
        # But this is expensive, so we skip by default
        :
    fi
fi

# Check for TODO comments in recently modified files
if command -v git &>/dev/null; then
    RECENT_FILES=$(git diff --name-only HEAD~1 2>/dev/null | head -5)
    TODO_COUNT=0
    for f in $RECENT_FILES; do
        if [ -f "$f" ]; then
            TODOS=$(grep -c "TODO\|FIXME\|XXX" "$f" 2>/dev/null || echo "0")
            TODO_COUNT=$((TODO_COUNT + TODOS))
        fi
    done
    if [ "$TODO_COUNT" -gt 3 ]; then
        # Optionally flag this but don't force continue
        :
    fi
fi

# Output decision
if [ "$SHOULD_CONTINUE" = "true" ]; then
    echo '{"decision":"block","reason":"'"$REASON"'"}'
fi

exit 0
