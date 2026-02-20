### Core Concept
**AI agents live on Linux servers, and CLI mastery is your direct connection to them.** The command line isn't about memorizing commands—it's about building a mental map of the filesystem that lets you navigate, manage, and troubleshoot deployed agents efficiently.

### Key Mental Models
- **Filesystem as Tree**: Linux uses a single unified tree starting at `/` (root), not drive letters like Windows. Everything branches from this one point.
- **Paths as Routes**: Absolute paths start from root (`/usr/bin`), relative paths start from your current location (`bin`). Know which to use when.
- **Terminal vs Shell**: Terminal = the window/interface you type in. Shell = the command interpreter that reads and executes your commands. Different shells (bash, zsh) have different features.
- **Agents Need Homes**: Your Digital FTEs will live at `/var/agents/` with configs in `/etc/agents/` and logs in `/var/log/agents/`. This organization matters for production management.

### Critical Patterns
- **Basic Navigation Commands**: `pwd` (print working directory—where am I?), `ls` (list contents), `cd` (change directory). These are your foundational movement tools.
- **Path Awareness**: Always know your current directory before running commands. Use `pwd` frequently when learning. Distinguish absolute paths (unambiguous, complete) from relative paths (context-dependent, flexible).
- **Hidden Files Matter**: `ls -la` reveals hidden files (starting with `.`) and detailed permissions. Dotfiles like `.bashrc` configure your shell environment.
- **Special Directory Shortcuts**: `.` = current directory, `..` = parent directory (up one level), `~` = your home directory. Use these for efficient navigation.
- **Directory Organization**: Linux has standard locations—`/home` (user files), `/etc` (configuration), `/var` (variable data including logs), `/usr` (installed software), `/bin` (essential commands).

### Common Mistakes
- **Not Verifying Location**: Running commands without knowing where you are (`pwd`). This leads to executing in wrong directories or deleting files accidentally.
- **Confusing Path Types**: Using relative paths when you need absolute (scripts, automation) or vice versa. Absolute paths are reliable and unambiguous; relative paths are flexible but context-dependent.
- **Ignoring Permissions**: Not understanding that `ls -la` shows permissions (`drwxr-xr-x`) and ownership. This causes "permission denied" errors when accessing files.
- **Forgetting Root Power**: Running commands with `sudo` grants temporary admin access. This is powerful but dangerous—only use when necessary, never for routine navigation.
- **Missing the Mental Model**: Trying to memorize commands instead of understanding the filesystem tree. Building the mental map scales; memorizing doesn't.
