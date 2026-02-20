### Core Concept

If you have to remember where a tool lives, it's not a tool yet. A script becomes a real tool when you can run it by name from any directory. Shell aliases stored in config files (`.bashrc` or `.zshrc`) make commands permanent across terminal sessions. The test: close your terminal, open a new one, and the command still works.

### Key Mental Models

- **Script vs tool gap**: A script in a random folder requires remembering the full path every time. A tool is available everywhere by name. Twenty minutes of setup now prevents hours of "I know I built this already" frustration later.
- **Config file persistence**: Your shell reads `.bashrc` or `.zshrc` every time a terminal opens. Anything in that file is permanent. `source` reloads it without reopening.

### Critical Patterns

- Prompt pattern: "I want to use [script] from anywhere. Make it a permanent command."
- The setup sequence: `mkdir -p ~/tools` → `cp script.py ~/tools/` → `chmod +x` → add alias to shell config → `source` to reload
- The shebang (`#!/usr/bin/env python3`) tells the OS which interpreter to use when running the file directly

### Common Mistakes

- Forgetting to run `source ~/.zshrc` after adding an alias — the current terminal won't see the new alias until the config is reloaded
- Not testing in a fresh terminal — `source` proves the alias works now, but only a new terminal proves it's truly permanent
- Leaving scripts scattered across project folders instead of organizing them in one place like `~/tools` — people rebuild scripts from scratch months later because they can't find the original

### Connections

- **Builds on**: sum-expenses.py from Lesson 3
- **Leads to**: Tax categorization with regex (Lesson 5) — your tools can sum, but they can't tell Dr. Pepper from a doctor visit
