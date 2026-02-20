#!/usr/bin/env bash
# Guardrail: Enforce interview-first for infrastructure skills
# Triggered by: PreToolUse on Skill
# Exit 2 = BLOCK with message to Claude

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0
validate_json "$INPUT" 2>/dev/null || exit 0

TOOL=$(parse_json "$INPUT" "tool_name" 2>/dev/null) || exit 0
[ "$TOOL" != "Skill" ] && exit 0

SKILL_NAME=$(parse_json "$INPUT" "tool_input.skill" 2>/dev/null) || exit 0
[ -z "$SKILL_NAME" ] && exit 0

SESSION_ID=$(parse_json "$INPUT" "session_id" 2>/dev/null) || SESSION_ID="unknown"

# Check governance
BLOCK_MSG=$(enforce_governance "$SKILL_NAME" "$SESSION_ID" 2>&1)
BLOCK_CODE=$?

if [ $BLOCK_CODE -ne 0 ]; then
    audit_log "governance_blocked" "$SESSION_ID" "$SKILL_NAME" "blocked" "$BLOCK_MSG"
    track_skill_end "$SKILL_NAME" "$SESSION_ID" "blocked" 2>/dev/null || true
    echo "$BLOCK_MSG" >&2
    exit 2
fi

exit 0
