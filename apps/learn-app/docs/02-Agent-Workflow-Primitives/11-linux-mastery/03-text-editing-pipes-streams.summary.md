### Core Concept
**Small tools connected by pipes are the heart of the Unix philosophy — each command does one thing well, and you combine them like building blocks.** This lesson covers editing files with nano, chaining commands with pipes, and controlling output with I/O redirection.

### Key Mental Models
- **Three Streams**: Every command has three channels — stdin (input), stdout (output), and stderr (errors). They look the same on screen but can be redirected independently.
- **Pipes as Assembly Lines**: `|` connects stdout of one command to stdin of the next, transforming data one step further at each stage.
- **Overwrite vs Append**: `>` replaces file contents; `>>` adds to the end. Logs always use `>>`.

### Critical Patterns
- **nano for quick edits**: Open, edit, Ctrl+O to save, Ctrl+X to exit — six shortcuts cover 90% of needs.
- **Pipe chaining**: `ls ~ | wc -l` counts items; `ps aux | grep python` finds processes.
- **Separate error logging**: `command > output.log 2> errors.log` splits normal output and errors into different files.
- **Self-help**: `man command` and `command --help` — look things up on your system before searching the web.

### Common Mistakes
- **Using > when you mean >>**: Silently destroys existing file content with one wrong redirect.
- **Forgetting stderr goes to screen**: Errors and output both appear on screen but are separate. Use `2>` to redirect errors.
- **Not using man pages**: Memorizing every flag instead of building the habit of `man command`.
