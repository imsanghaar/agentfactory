### Core Concept
**tmux creates terminal sessions that live on the server, independent of your connection — your connection should never be your agent's single point of failure.** When SSH drops, WiFi dies, or your laptop sleeps, processes inside tmux keep running. For Digital FTE deployment where agents run for hours or days, tmux is non-negotiable.

### Key Mental Models
- **Session as Persistent Workspace**: A tmux session is a room you walk into, set up your work, walk out of, and return to find everything exactly as you left it. Sessions survive disconnections.
- **Panes as Split Views**: Panes divide a single screen into independent terminals — run an agent in one, watch logs in another, monitor resources in a third. All visible simultaneously.
- **Windows as Tabs**: Windows give you entirely separate screens within the same session. Think browser tabs — each has its own content and pane layout.
- **Session Scripts as Blueprints**: A bash script that creates sessions, splits panes, and sends commands eliminates manual layout setup. One command recreates your entire monitoring dashboard.

### Critical Patterns
- **Four lifecycle operations**: `tmux new-session -s name` (create), `Ctrl+b d` (detach), `tmux attach -t name` (reattach), `tmux kill-session -t name` (destroy).
- **Named sessions for project isolation**: Create separate sessions per project (`api-agent`, `data-pipeline`, `debug`) so each maintains independent state.
- **Pane splitting for monitoring**: `Ctrl+b %` splits vertically, `Ctrl+b "` splits horizontally. Navigate with `Ctrl+b arrow-key`.
- **Copy mode for scrollback**: `Ctrl+b [` enters copy mode for scrolling through output history and searching with `/pattern`.

### Common Mistakes
- **Not naming sessions**: Unnamed sessions get numbers (0, 1, 2) which become confusing with multiple projects. Always use `-s name`.
- **Forgetting the prefix key**: Every tmux command starts with `Ctrl+b` followed by another key. Pressing keys without the prefix does nothing in tmux.
- **Running kill-session on the wrong target**: `tmux kill-session` permanently destroys a session and all processes inside it. Always verify the session name with `tmux ls` first.
