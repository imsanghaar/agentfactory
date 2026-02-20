import type { IPty } from "node-pty";
import type { WebSocket } from "ws";
import * as pty from "node-pty";
import { chmodSync, accessSync, constants } from "node:fs";
import { join, dirname } from "node:path";
import { platform, arch } from "node:os";
import { createRequire } from "node:module";
import type { AppError } from "../errors.js";
import { appError } from "../errors.js";
import { getCachedClaudePath } from "../claude-path.js";

interface Session {
  pty: IPty;
  ws: WebSocket | null;
  exerciseId: string;
  workspacePath: string;
  createdAt: Date;
}

const sessions = new Map<string, Session>();
const wsCleanups = new WeakMap<WebSocket, () => void>();

/**
 * node-pty ships a `spawn-helper` binary in prebuilds/ that must be executable.
 * npm tarballs can strip the execute bit during extraction (common with npx).
 * Fix it once at first spawn to avoid posix_spawnp failures.
 */
let spawnHelperFixed = false;
function ensureSpawnHelperExecutable(): void {
  if (spawnHelperFixed || platform() === "win32") return;
  spawnHelperFixed = true;

  try {
    // Resolve node-pty's actual location regardless of package manager layout
    const req = createRequire(import.meta.url);
    const nodePtyPkg = req.resolve("node-pty/package.json");
    const spawnHelper = join(
      dirname(nodePtyPkg),
      "prebuilds",
      `${platform()}-${arch()}`,
      "spawn-helper",
    );
    accessSync(spawnHelper, constants.F_OK);
    try {
      accessSync(spawnHelper, constants.X_OK);
    } catch {
      chmodSync(spawnHelper, 0o755);
      console.log("[pty] Fixed spawn-helper execute permission");
    }
  } catch {
    // spawn-helper not found at expected path — node-pty may be structured differently
  }
}

export function spawnSession(
  sessionId: string,
  exerciseId: string,
  workspacePath: string,
  initialPrompt?: string,
): void {
  // Single exercise enforcement: kill ALL existing sessions (only one at a time)
  if (sessions.size > 0) {
    console.log(
      `[pty] Killing ${sessions.size} existing session(s) before new spawn`,
    );
    killAllSessions();
  }

  const claudePath = getCachedClaudePath();
  if (!claudePath) {
    throw appError(
      "CLAUDE_NOT_FOUND",
      "Claude Code not found",
      "Install Claude Code and ensure it's in your PATH",
    );
  }

  // Build a clean environment: strip all Claude Code env vars to avoid
  // "nested session" detection when the practice server runs inside a Claude Code terminal.
  const cleanEnv: Record<string, string> = {};
  for (const [key, value] of Object.entries(process.env)) {
    if (value != null && !key.startsWith("CLAUDE")) {
      cleanEnv[key] = value;
    }
  }

  // If an initial prompt is provided, pass it as a CLI argument so Claude Code
  // starts in interactive mode with that message already submitted.
  const claudeArgs = initialPrompt ? [initialPrompt] : [];

  // On Windows, .cmd files (npm global installs) must be spawned through cmd.exe.
  // Direct pty.spawn of a .cmd fails because ConPTY expects an executable, not a batch script.
  const isWindows = process.platform === "win32";
  const isCmdFile = isWindows && claudePath.endsWith(".cmd");

  const file = isCmdFile ? process.env.ComSpec || "cmd.exe" : claudePath;
  const args = isCmdFile ? ["/c", claudePath, ...claudeArgs] : claudeArgs;

  ensureSpawnHelperExecutable();

  let ptyProcess: pty.IPty;
  try {
    ptyProcess = pty.spawn(file, args, {
      name: "xterm-256color",
      cols: 80,
      rows: 24,
      cwd: workspacePath,
      env: {
        ...cleanEnv,
        TERM: "xterm-256color",
      },
    });
  } catch (err) {
    throw appError(
      "PTY_SPAWN_FAILED",
      `Failed to start Claude Code: ${err instanceof Error ? err.message : String(err)}`,
      "Ensure Claude Code is installed and your terminal has proper permissions",
    );
  }

  sessions.set(sessionId, {
    pty: ptyProcess,
    ws: null,
    exerciseId,
    workspacePath,
    createdAt: new Date(),
  });

  ptyProcess.onExit(({ exitCode }) => {
    console.log(`[pty] Session ${sessionId} exited with code ${exitCode}`);
    // Guard: session may have been explicitly killed already (no double-delete)
    const session = sessions.get(sessionId);
    if (!session) return;

    // Send typed error frame before closing WebSocket (Decision #17)
    if (session.ws && session.ws.readyState === 1 /* OPEN */) {
      const error: AppError = {
        code: "PTY_EXITED",
        message: "Claude Code exited",
        action: "Click Restart to begin a new session",
      };
      session.ws.send(JSON.stringify({ type: "error", error }));
      session.ws.close(1000, "process_exited");
    }
    // Clean up: detach WS listeners, then remove from Map
    detachWs(sessionId);
    sessions.delete(sessionId);
  });

  console.log(
    `[pty] Spawned session ${sessionId} (exercise: ${exerciseId}, pid: ${ptyProcess.pid})`,
  );
}

export function resizeSession(
  sessionId: string,
  cols: number,
  rows: number,
): void {
  const session = sessions.get(sessionId);
  if (!session) return;
  session.pty.resize(cols, rows);
}

export function attachWs(sessionId: string, ws: WebSocket): void {
  const session = sessions.get(sessionId);
  if (!session) return;

  // Detach previous WS if any
  if (session.ws) {
    detachWs(sessionId);
  }

  session.ws = ws;

  // Pipe PTY output to WS
  const dataHandler = session.pty.onData((data: string) => {
    if (session.ws && session.ws.readyState === ws.OPEN) {
      session.ws.send(Buffer.from(data, "utf-8"));
    }
  });

  // Store cleanup reference via WeakMap (avoids mutating the WS instance)
  wsCleanups.set(ws, () => {
    dataHandler.dispose();
  });

  console.log(`[pty] Attached WS to session ${sessionId}`);
}

export function detachWs(sessionId: string): void {
  const session = sessions.get(sessionId);
  if (!session || !session.ws) return;

  const ws = session.ws;
  wsCleanups.get(ws)?.();
  wsCleanups.delete(ws);

  session.ws = null;
  console.log(`[pty] Detached WS from session ${sessionId} (PTY still alive)`);
}

export function killSession(sessionId: string): void {
  const session = sessions.get(sessionId);
  if (!session) return;

  detachWs(sessionId);
  session.pty.kill();
  sessions.delete(sessionId);
  console.log(`[pty] Killed session ${sessionId}`);
}

export function getSession(sessionId: string): {
  exerciseId: string;
  workspacePath: string;
  createdAt: Date;
  hasPty: boolean;
  hasWs: boolean;
} | null {
  const session = sessions.get(sessionId);
  if (!session) return null;

  return {
    exerciseId: session.exerciseId,
    workspacePath: session.workspacePath,
    createdAt: session.createdAt,
    hasPty: true,
    hasWs: session.ws !== null,
  };
}

/** Find an existing session that matches the given workspace path (dedup for double-mount). */
export function findSessionByPath(workspacePath: string): string | null {
  for (const [id, session] of sessions.entries()) {
    if (session.workspacePath === workspacePath) {
      console.log(`[pty] Reusing existing session ${id} for ${workspacePath}`);
      return id;
    }
  }
  return null;
}

export function killAllSessions(): void {
  console.log(`[pty] Killing all sessions (${sessions.size} active)`);
  for (const sessionId of [...sessions.keys()]) {
    killSession(sessionId);
  }
}

export function hasSession(sessionId: string): boolean {
  return sessions.has(sessionId);
}

export function writeToPtyStdin(sessionId: string, data: string): void {
  const session = sessions.get(sessionId);
  if (!session) return;
  session.pty.write(data);
}
