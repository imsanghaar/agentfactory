#!/usr/bin/env bash
# Team: Smart skill suggestions based on prompt analysis
# Triggered by: UserPromptSubmit
# Outputs helpful suggestions to user

trap 'exit 0' ERR

INPUT=$(cat 2>/dev/null) || exit 0
[ -z "$INPUT" ] && exit 0

PROMPT=$(echo "$INPUT" | jq -r '.prompt // empty' 2>/dev/null) || exit 0
[ -z "$PROMPT" ] && exit 0

PROMPT_LOWER=$(echo "$PROMPT" | tr '[:upper:]' '[:lower:]' 2>/dev/null) || exit 0

SUGGESTIONS=""
REASONS=""

# Infrastructure skills (require interview-first)
if echo "$PROMPT_LOWER" | grep -qE '\b(kubernetes|k8s|kubectl|pod|deployment|ingress)\b' 2>/dev/null; then
    SUGGESTIONS="${SUGGESTIONS}kubernetes "
    REASONS="${REASONS}  - /kubernetes: K8s deployment detected (requires /interview first)\n"
fi

if echo "$PROMPT_LOWER" | grep -qE '\b(helm|chart|values\.yaml|release)\b' 2>/dev/null; then
    SUGGESTIONS="${SUGGESTIONS}helm "
    REASONS="${REASONS}  - /helm: Helm chart work detected (requires /interview first)\n"
fi

if echo "$PROMPT_LOWER" | grep -qE '\b(docker|dockerfile|container|image|compose)\b' 2>/dev/null; then
    SUGGESTIONS="${SUGGESTIONS}docker "
    REASONS="${REASONS}  - /docker: Container work detected (requires /interview first)\n"
fi

if echo "$PROMPT_LOWER" | grep -qE '\b(terraform|tf|tfvars|provider|module)\b' 2>/dev/null; then
    SUGGESTIONS="${SUGGESTIONS}terraform "
    REASONS="${REASONS}  - /terraform: Infrastructure-as-Code detected (requires /interview first)\n"
fi

# Development skills
if echo "$PROMPT_LOWER" | grep -qE '\b(test|tdd|jest|pytest|spec|unit test)\b' 2>/dev/null; then
    SUGGESTIONS="${SUGGESTIONS}tdd "
    REASONS="${REASONS}  - /tdd: Test-driven development patterns\n"
fi

if echo "$PROMPT_LOWER" | grep -qE '\b(bug|debug|fix|error|broken|failing)\b' 2>/dev/null; then
    SUGGESTIONS="${SUGGESTIONS}systematic-debugging "
    REASONS="${REASONS}  - /systematic-debugging: Root cause analysis methodology\n"
fi

if echo "$PROMPT_LOWER" | grep -qE '\b(nextjs|next\.js|app router|server component)\b' 2>/dev/null; then
    SUGGESTIONS="${SUGGESTIONS}building-nextjs-apps "
    REASONS="${REASONS}  - /building-nextjs-apps: Next.js 16 patterns\n"
fi

if echo "$PROMPT_LOWER" | grep -qE '\b(fastapi|sqlmodel|pydantic|async)\b' 2>/dev/null; then
    SUGGESTIONS="${SUGGESTIONS}fastapi-backend "
    REASONS="${REASONS}  - /fastapi-backend: FastAPI patterns\n"
fi

# Documentation/Research
if echo "$PROMPT_LOWER" | grep -qE '\b(docs|documentation|how to|api reference)\b' 2>/dev/null; then
    SUGGESTIONS="${SUGGESTIONS}fetch-library-docs "
    REASONS="${REASONS}  - /fetch-library-docs: Get official library documentation\n"
fi

# Planning/Collaboration
if echo "$PROMPT_LOWER" | grep -qE '\b(interview|requirements|spec|why|scope|clarify)\b' 2>/dev/null; then
    SUGGESTIONS="${SUGGESTIONS}interview "
    REASONS="${REASONS}  - /interview: Discover requirements before implementing\n"
fi

if echo "$PROMPT_LOWER" | grep -qE '\b(code review|review pr|pull request)\b' 2>/dev/null; then
    SUGGESTIONS="${SUGGESTIONS}code-review "
    REASONS="${REASONS}  - /code-review: PR review with best practices\n"
fi

# Output suggestions if any
if [ -n "$SUGGESTIONS" ]; then
    echo "<user-prompt-submit-hook>"
    echo "Skill Suggestions"
    echo ""
    echo -e "$REASONS"
    echo ""
    echo "Infrastructure skills (kubernetes, helm, docker, terraform) require /interview first."
    echo "</user-prompt-submit-hook>"
fi

exit 0
