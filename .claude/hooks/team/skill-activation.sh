#!/usr/bin/env bash
# Force Claude to evaluate skills before proceeding
# Research shows 84% activation vs 20% with simple suggestions
# Triggered by: UserPromptSubmit

trap 'exit 0' ERR

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/_common.sh" 2>/dev/null || exit 0

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0

PROMPT=$(parse_json "$INPUT" "prompt") || exit 0

# Skip short prompts (greetings, confirmations)
[ ${#PROMPT} -lt 30 ] && exit 0

# Skip if prompt is just a slash command
[[ "$PROMPT" == /* ]] && exit 0

# Get list of available skills
SKILLS_DIR="$ROOT_DIR/.claude/skills"
[ ! -d "$SKILLS_DIR" ] && exit 0

# Build skill list with descriptions
SKILL_LIST=""
SKILL_COUNT=0
for skill_dir in "$SKILLS_DIR"/*/; do
    [ -d "$skill_dir" ] || continue
    skill_name=$(basename "$skill_dir")
    skill_file="$skill_dir/SKILL.md"

    if [ -f "$skill_file" ]; then
        # Extract description from SKILL.md
        desc=$(grep -A3 "^description:" "$skill_file" 2>/dev/null | tail -3 | tr '\n' ' ' | cut -c1-150)
        if [ -n "$desc" ]; then
            SKILL_LIST="$SKILL_LIST- /$skill_name: $desc
"
            SKILL_COUNT=$((SKILL_COUNT + 1))
        fi
    fi
done

# Skip if no skills found
[ -z "$SKILL_LIST" ] && exit 0
# Note: Removed skill count threshold - always evaluate skills regardless of count

# Output forced evaluation prompt
cat << EOF
<skill-activation>
SKILL EVALUATION REQUIRED

Available skills for this task:
$SKILL_LIST
EVALUATE: Which skills match this request? For matching skills, invoke them with /skill-name before implementing.

Skipping skill activation wastes specialized knowledge.
</skill-activation>
EOF

exit 0
