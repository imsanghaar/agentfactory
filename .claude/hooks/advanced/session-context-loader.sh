#!/usr/bin/env bash
# Advanced: Load rich context at session start
# Triggered by: SessionStart
# Injects project state, open issues, team context

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
SESSION_ID=$(parse_json "$INPUT" "session_id" 2>/dev/null) || SESSION_ID="unknown"
SOURCE=$(parse_json "$INPUT" "source" 2>/dev/null) || SOURCE="startup"

# Only run on fresh startup, not resume/compact
[ "$SOURCE" != "startup" ] && exit 0

# Build context injection
CONTEXT=""

# Git branch info
BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
CONTEXT="${CONTEXT}Current branch: $BRANCH\n"

# Recent commits (last 5)
if command -v git &>/dev/null; then
    RECENT_COMMITS=$(git log --oneline -5 2>/dev/null || echo "No commits")
    CONTEXT="${CONTEXT}\nRecent commits:\n$RECENT_COMMITS\n"
fi

# Open GitHub issues (if gh cli available)
if command -v gh &>/dev/null; then
    OPEN_ISSUES=$(gh issue list --limit 5 --state open 2>/dev/null | head -5 || echo "")
    if [ -n "$OPEN_ISSUES" ]; then
        CONTEXT="${CONTEXT}\nOpen issues:\n$OPEN_ISSUES\n"
    fi
fi

# Team member who started session (from git config)
GIT_USER=$(git config user.name 2>/dev/null || echo "Unknown")
CONTEXT="${CONTEXT}\nSession started by: $GIT_USER\n"

# Project type detection
if [ -f "package.json" ]; then
    CONTEXT="${CONTEXT}Project type: Node.js\n"
elif [ -f "requirements.txt" ] || [ -f "pyproject.toml" ]; then
    CONTEXT="${CONTEXT}Project type: Python\n"
elif [ -f "go.mod" ]; then
    CONTEXT="${CONTEXT}Project type: Go\n"
elif [ -f "Cargo.toml" ]; then
    CONTEXT="${CONTEXT}Project type: Rust\n"
fi

# Output context for Claude
echo "<session-start-hook>"
echo "Session Context"
echo ""
echo -e "$CONTEXT"
echo "</session-start-hook>"

exit 0
