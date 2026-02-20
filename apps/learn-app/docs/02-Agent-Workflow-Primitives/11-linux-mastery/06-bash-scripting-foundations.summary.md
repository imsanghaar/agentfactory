### Core Concept
**Bash scripts capture your deployment knowledge as executable files — reusable automation that runs the same way every time, eliminating manual errors and forgotten steps.** Instead of typing commands one by one, a script encodes the exact sequence, handles errors gracefully, and runs identically whether executed at 2 PM or 2 AM.

### Key Mental Models
- **Scripts as Encoded Knowledge**: A script captures repeatable sequences so deployment knowledge is versioned and shareable, not locked in your head.
- **Three Script Essentials**: Shebang (`#!/bin/bash`) identifies the interpreter, `chmod +x` grants execute permission, `set -euo pipefail` makes it fail safely.
- **Functions as Reusable Blocks**: Wrap repeating logic in functions with `local` variables. One definition, multiple calls with different arguments.

### Critical Patterns
- **set -euo pipefail on line 2**: `-e` stops on errors, `-u` catches undefined variables, `-o pipefail` prevents hidden pipe failures.
- **Always quote variables**: `"${VAR}"` preserves spaces. Unquoted variables break on paths with spaces.
- **Conditionals with [[ ]]**: Modern test syntax. Use `-d` for directory existence, `-f` for files, `-z` for empty strings.
- **for loops for batch operations**: Iterate over arrays instead of duplicating code for each item.

### Common Mistakes
- **Skipping set -euo pipefail**: Without it, scripts silently continue after failures — a failed `cd` followed by `rm -rf *` deletes files in the wrong directory.
- **Forgetting chmod +x**: Scripts need executable permission. Without it, you get "Permission denied" even though the script is correct.
- **Unquoted variables**: `DIR=/tmp/my agent` without quotes breaks on the space. Always wrap expansions in double quotes.
