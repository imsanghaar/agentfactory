import { IncomingMessage } from "node:http";
import { Duplex } from "node:stream";
import { WebSocketServer, WebSocket } from "ws";
import {
  attachWs,
  detachWs,
  hasSession,
  writeToPtyStdin,
  resizeSession,
} from "../pty/manager.js";
import { isValidOrigin } from "../middleware/origin.js";

export interface HeartbeatOptions {
  pingInterval?: number; // ms, default 30000
  pongTimeout?: number; // ms, default 10000
}

const DEFAULT_PING_INTERVAL = 30_000;
const DEFAULT_PONG_TIMEOUT = 10_000;

const wss = new WebSocketServer({ noServer: true });

/** Exported for testing. Starts a ping/pong heartbeat on the given WebSocket. */
export function startHeartbeat(
  ws: WebSocket,
  options: HeartbeatOptions = {},
): () => void {
  const pingInterval = options.pingInterval ?? DEFAULT_PING_INTERVAL;
  const pongTimeout = options.pongTimeout ?? DEFAULT_PONG_TIMEOUT;

  let pongTimer: ReturnType<typeof setTimeout> | null = null;
  let alive = true;

  ws.on("pong", () => {
    alive = true;
    if (pongTimer) {
      clearTimeout(pongTimer);
      pongTimer = null;
    }
  });

  const pingTimer = setInterval(() => {
    if (!alive) {
      // Previous ping never got a pong — connection is dead
      ws.terminate();
      return;
    }

    alive = false;
    ws.ping();

    // If no pong within timeout, terminate
    pongTimer = setTimeout(() => {
      ws.terminate();
    }, pongTimeout);
  }, pingInterval);

  // Return cleanup function
  return () => {
    clearInterval(pingTimer);
    if (pongTimer) {
      clearTimeout(pongTimer);
      pongTimer = null;
    }
  };
}

export function handleUpgrade(
  req: IncomingMessage,
  socket: Duplex,
  head: Buffer,
  heartbeatOptions?: HeartbeatOptions,
): void {
  // Validate origin (security: prevent cross-origin WebSocket hijacking)
  if (!isValidOrigin(req)) {
    console.warn(`[ws] Rejected upgrade from origin: ${req.headers.origin}`);
    socket.write("HTTP/1.1 403 Forbidden\r\n\r\n");
    socket.destroy();
    return;
  }

  // Extract session ID from URL: /sessions/:id/ws
  const match = req.url?.match(/^\/sessions\/([^/]+)\/ws$/);
  if (!match) {
    socket.write("HTTP/1.1 404 Not Found\r\n\r\n");
    socket.destroy();
    return;
  }

  const sessionId = match[1];
  if (!hasSession(sessionId)) {
    socket.write("HTTP/1.1 404 Not Found\r\n\r\n");
    socket.destroy();
    return;
  }

  wss.handleUpgrade(req, socket, head, (ws) => {
    console.log(`[ws] Client connected to session ${sessionId}`);

    // Attach WebSocket to PTY session
    attachWs(sessionId, ws);

    // Start server-side heartbeat (ping/pong)
    const stopHeartbeat = startHeartbeat(ws, heartbeatOptions);

    // Handle incoming messages from browser
    ws.on("message", (data: Buffer, isBinary: boolean) => {
      if (isBinary) {
        // Binary frame: raw terminal input (keystrokes)
        writeToPtyStdin(sessionId, data.toString("utf-8"));
      } else {
        // Text frame: control messages (resize, etc.)
        try {
          const msg = JSON.parse(data.toString("utf-8"));
          if (
            msg.type === "resize" &&
            typeof msg.cols === "number" &&
            typeof msg.rows === "number"
          ) {
            resizeSession(sessionId, msg.cols, msg.rows);
          }
        } catch {
          // Ignore malformed control messages
        }
      }
    });

    ws.on("close", () => {
      console.log(`[ws] Client disconnected from session ${sessionId}`);
      stopHeartbeat();
      detachWs(sessionId);
    });

    ws.on("error", (err) => {
      console.error(`[ws] Error on session ${sessionId}:`, err.message);
    });
  });
}
