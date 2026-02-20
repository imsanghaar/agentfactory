### Core Concept
**Your terminal becomes a personalized power tool when you install software with apt, create shortcuts with aliases, and add smart navigation with zoxide and fzf.** Customizing your shell eliminates repetitive typing and transforms daily workflows from tedious to effortless.

### Key Mental Models
- **apt as Supply Chain**: The package manager downloads, installs, and removes software from trusted repositories. Always update the catalog first — check inventory before shopping.
- **.bashrc as Terminal Memory**: `~/.bashrc` runs every time you open a terminal. Aliases, tool initialization, and variables added there become permanent.
- **Aliases as Shortcuts**: Map a short name to a long command. Temporary aliases last one session; aliases in `.bashrc` survive reboots.

### Critical Patterns
- **Two-step install**: Always `sudo apt update` then `sudo apt install package -y`. Verify with `which program`.
- **Backup before editing**: `cp ~/.bashrc ~/.bashrc.backup` before changes. A broken config can lock you out.
- **source to reload**: After editing `.bashrc`, run `source ~/.bashrc` to apply changes immediately.
- **zoxide for navigation**: `z log` jumps to `/var/log` based on visit frequency — replaces typing full paths.

### Common Mistakes
- **Forgetting sudo**: Package installation requires admin privileges. Without `sudo`, apt returns permission denied.
- **Editing .bashrc without backup**: One syntax error breaks every new terminal session.
- **Not reloading**: Edits don't take effect until `source ~/.bashrc` or opening a new terminal.
