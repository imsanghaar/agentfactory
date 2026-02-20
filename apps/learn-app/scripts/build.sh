#!/bin/bash
# Build script that conditionally adds --localstorage-file flag for Node.js 25+

# Change to learn-app directory (parent of scripts/)
cd "$(dirname "$0")/.."

NODE_VERSION=$(node -v | cut -d'.' -f1 | sed 's/v//')

# Increase heap size for OG image generation (default is often too small in CI)
# 4GB should handle 200+ docs with OG image generation
HEAP_SIZE="--max-old-space-size=4096"

# Determine the localstorage file path based on OS
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  # Windows
  LOCALSTORAGE_FILE="/tmp/docusaurus-localstorage"
else
  # Linux/Mac (including Vercel)
  LOCALSTORAGE_FILE="/tmp/docusaurus-localstorage"
fi

if [ "$NODE_VERSION" -ge 25 ]; then
  # Node.js 25+ requires --localstorage-file flag
  # Use npx to properly resolve the docusaurus binary
  NODE_OPTIONS="$HEAP_SIZE --localstorage-file=$LOCALSTORAGE_FILE" npx docusaurus build
else
  # Node.js 20-24 doesn't need the flag
  NODE_OPTIONS="$HEAP_SIZE" npx docusaurus build
fi
