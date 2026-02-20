# af-practice

Local practice server for [Agent Factory](https://agentfactory.dev) exercises. Launches Claude Code in a PTY with managed exercise workspaces.

## Quick Start

```bash
npx af-practice
```

The server starts on port 3100 and auto-discovers Claude Code on your system.

## Options

```
--port <number>  Port to listen on (default: 3100)
--refresh        Clear cached workspaces before starting
--version, -v    Print version and exit
--help, -h       Show this help message
```

## Requirements

- Node.js >= 18
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) installed and in PATH

## How It Works

1. The learn-app frontend scans ports 3100-3110 for a running practice server
2. When a student opens an exercise, the frontend requests a session via REST API
3. The server downloads the exercise repo (GitHub release), extracts it, and spawns Claude Code in the workspace
4. Terminal I/O is streamed over WebSocket to an xterm.js terminal in the browser

## API

| Endpoint                  | Method | Description                                      |
| ------------------------- | ------ | ------------------------------------------------ |
| `/health`                 | GET    | Server status, version, Claude Code availability |
| `/sessions/start`         | POST   | Start a new exercise session                     |
| `/sessions/reset`         | POST   | Reset an exercise workspace                      |
| `/ws/terminal/:sessionId` | WS     | Terminal I/O stream                              |

## Platform Support

| Platform         | Status    |
| ---------------- | --------- |
| macOS            | Supported |
| Linux            | Supported |
| Windows (native) | Supported |
| Windows (WSL)    | Supported |

## License

MIT
