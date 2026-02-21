# af-practice

Local practice server for [Agent Factory](https://agentfactory.dev) exercises. Launches Qwen CLI in a PTY with managed exercise workspaces.

## Quick Start

```bash
npx af-practice
```

The server starts on port 3100 and auto-discovers Qwen CLI on your system.

## Options

```
--port <number>  Port to listen on (default: 3100)
--refresh        Clear cached workspaces before starting
--version, -v    Print version and exit
--help, -h       Show this help message
```

## Requirements

- Node.js >= 18
- [Qwen CLI](https://github.com/QwenLM/qwen-agent) installed and in PATH

## How It Works

1. The learn-app frontend scans ports 3100-3110 for a running practice server
2. When a student opens an exercise, the frontend requests a session via REST API
3. The server downloads the exercise repo (GitHub release), extracts it, and spawns Qwen CLI in the workspace
4. Terminal I/O is streamed over WebSocket to an xterm.js terminal in the browser

## API

| Endpoint                  | Method | Description                                      |
| ------------------------- | ------ | ------------------------------------------------ |
| `/health`                 | GET    | Server status, version, Qwen CLI availability    |
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
