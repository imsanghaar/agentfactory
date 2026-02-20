#!/usr/bin/env bash
# Advanced: Require code review comments for certain file types
# Triggered by: PostToolUse on Edit|Write
# Reminds Claude to add review-worthy comments for complex changes

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
FILE_PATH=$(parse_json "$INPUT" "tool_input.file_path" 2>/dev/null) || exit 0

[ -z "$FILE_PATH" ] && exit 0
[ ! -f "$FILE_PATH" ] && exit 0

# High-scrutiny file patterns
SCRUTINY_PATTERNS=(
    "auth"
    "security"
    "payment"
    "billing"
    "crypto"
    "password"
    "token"
    "api/v"
    "middleware"
)

NEEDS_REVIEW="false"
for pattern in "${SCRUTINY_PATTERNS[@]}"; do
    if echo "$FILE_PATH" | grep -qi "$pattern" 2>/dev/null; then
        NEEDS_REVIEW="true"
        break
    fi
done

# Check file size (large changes need review)
if [ -f "$FILE_PATH" ]; then
    LINES=$(wc -l < "$FILE_PATH" 2>/dev/null | tr -d ' ')
    if [ "$LINES" -gt 500 ]; then
        NEEDS_REVIEW="true"
    fi
fi

if [ "$NEEDS_REVIEW" = "true" ]; then
    echo "<post-tool-use-hook>"
    echo "Code Review Reminder"
    echo ""
    echo "This file ($FILE_PATH) is in a high-scrutiny area."
    echo "Consider:"
    echo "  - Adding inline comments explaining complex logic"
    echo "  - Documenting security implications"
    echo "  - Requesting human review before merging"
    echo "</post-tool-use-hook>"
fi

exit 0
