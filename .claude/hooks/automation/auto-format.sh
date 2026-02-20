#!/usr/bin/env bash
# Automation: Auto-format files after modification
# Triggered by: PostToolUse on Edit|Write

trap 'exit 0' ERR

file_path=$(jq -r '.tool_input.file_path // empty' 2>/dev/null) || exit 0

[ -z "$file_path" ] && exit 0
[ ! -f "$file_path" ] && exit 0

case "$file_path" in
    *.py)
        if command -v ruff &>/dev/null; then
            ruff format --quiet "$file_path" 2>/dev/null || true
            ruff check --fix --quiet "$file_path" 2>/dev/null || true
        elif command -v black &>/dev/null; then
            black --quiet "$file_path" 2>/dev/null || true
        fi
        ;;

    *.ts|*.tsx|*.js|*.jsx|*.json|*.md)
        if command -v npx &>/dev/null && [ -f "package.json" ]; then
            npx prettier --write "$file_path" 2>/dev/null || true
        fi
        ;;

    *.go)
        if command -v gofmt &>/dev/null; then
            gofmt -w "$file_path" 2>/dev/null || true
        fi
        if command -v goimports &>/dev/null; then
            goimports -w "$file_path" 2>/dev/null || true
        fi
        ;;

    *.yaml|*.yml)
        if command -v yamlfmt &>/dev/null; then
            yamlfmt "$file_path" 2>/dev/null || true
        fi
        ;;

    *.sh)
        if command -v shfmt &>/dev/null; then
            shfmt -w "$file_path" 2>/dev/null || true
        fi
        ;;

    *.rs)
        if command -v rustfmt &>/dev/null; then
            rustfmt "$file_path" 2>/dev/null || true
        fi
        ;;
esac

exit 0
