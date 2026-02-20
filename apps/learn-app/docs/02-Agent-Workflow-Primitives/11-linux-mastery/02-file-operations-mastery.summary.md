### Core Concept
**File operations are the construction tools of the CLI architect — creating, copying, moving, and reading files builds the workspace structures your Digital FTEs depend on.** Navigation was reading the blueprint; now you're picking up the hammer.

### Key Mental Models
- **Construction Toolkit**: Each command is a specific tool — `touch` creates, `cp` duplicates, `mv` relocates, `rm` demolishes. Match the tool to the job.
- **Brace Expansion as Blueprint**: `mkdir -p agent/{src,config,logs,data}` builds an entire workspace in one command — stamping out a pre-designed floor plan.
- **Recursive Flag (-r)**: Without `-r`, commands operate on single files. With it, they operate on entire directory trees.

### Critical Patterns
- **mkdir -p for nested structures**: Creates all parent directories and never fails on existing paths.
- **Verify after every operation**: Run `ls` after creating, copying, or moving files to confirm results.
- **Wildcards for batch operations**: `*` matches anything, `?` matches one character, `[]` matches a set.
- **Safe deletion**: Use `rm -i` (interactive) before `rm -rf` (recursive force). There is no undo.

### Common Mistakes
- **Using rm -rf without thinking**: Recursive force delete is permanent. Always double-check the path.
- **Forgetting -p with mkdir**: `mkdir nested/path` fails if the parent doesn't exist.
- **Copying directories without -r**: `cp mydir/ backup/` silently skips contents. Use `cp -r` for full trees.
