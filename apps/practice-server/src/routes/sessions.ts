import { Hono } from "hono";
import crypto from "node:crypto";
import { z } from "zod";
import { getExercise } from "../exercises/registry.js";
import {
  downloadAndExtract,
  resolveExerciseDir,
  resetWorkspace,
} from "../exercises/workspace.js";
import {
  spawnSession,
  getSession,
  findSessionByPath,
  killAllSessions,
} from "../pty/manager.js";
import { appError, httpStatus, AppErrorInstance } from "../errors.js";

export const StartSessionSchema = z.object({
  exerciseId: z
    .string()
    .min(1)
    .regex(/^[\w-]+$/),
  subExercise: z
    .string()
    .regex(/^[\w.-]+$/)
    .optional(),
});

const sessions = new Hono();

sessions.post("/sessions/start", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    const err = appError("INVALID_REQUEST", "Invalid JSON");
    return c.json({ error: err.toJSON() }, 400);
  }

  console.log(`[sessions] POST /sessions/start body:`, JSON.stringify(body));

  const parsed = StartSessionSchema.safeParse(body);
  if (!parsed.success) {
    const err = appError(
      "INVALID_REQUEST",
      parsed.error.issues.map((i) => i.message).join("; "),
    );
    return c.json({ error: err.toJSON() }, httpStatus(err.code));
  }

  const { exerciseId, subExercise } = parsed.data;

  const exercise = getExercise(exerciseId);
  if (!exercise) {
    const err = appError(
      "EXERCISE_NOT_FOUND",
      `Unknown exercise: ${exerciseId}`,
    );
    return c.json({ error: err.toJSON() }, httpStatus(err.code));
  }

  try {
    console.log(
      `[sessions] Starting session for exercise: ${exerciseId}` +
        (subExercise ? ` (sub: ${subExercise})` : ""),
    );

    const workspacePath = await downloadAndExtract(exerciseId);

    // Resolve exercise-specific subdirectory (e.g., "1.1" -> module-1/exercise-1.1-messy-downloads/)
    const cwd = subExercise
      ? await resolveExerciseDir(workspacePath, subExercise)
      : workspacePath;

    // Reuse existing session for the same workspace (handles React StrictMode double-mount)
    const existingId = findSessionByPath(cwd);
    if (existingId) {
      console.log(`[sessions] Reusing session ${existingId} at ${cwd}`);
      return c.json({
        sessionId: existingId,
        wsUrl: `/sessions/${existingId}/ws`,
      });
    }

    const sessionId = crypto.randomUUID();

    // When a specific exercise is targeted, auto-prompt Claude to read INSTRUCTIONS.md
    const initialPrompt = subExercise
      ? "Read INSTRUCTIONS.md and present a brief overview of this exercise, then ask me what I'd like to work on."
      : undefined;

    spawnSession(sessionId, exerciseId, cwd, initialPrompt);

    console.log(`[sessions] Session ${sessionId} created at ${cwd}`);

    return c.json({
      sessionId,
      wsUrl: `/sessions/${sessionId}/ws`,
    });
  } catch (err) {
    console.error(`[sessions] Failed to start session:`, err);
    if (err instanceof AppErrorInstance) {
      return c.json({ error: err.toJSON() }, httpStatus(err.code));
    }
    const fallback = appError("DOWNLOAD_FAILED", "Failed to start session");
    return c.json({ error: fallback.toJSON() }, httpStatus(fallback.code));
  }
});

export const ResetSchema = z.object({
  exerciseId: z
    .string()
    .min(1)
    .regex(/^[\w-]+$/),
});

sessions.post("/sessions/reset", async (c) => {
  let body: unknown;
  try {
    body = await c.req.json();
  } catch {
    const err = appError("INVALID_REQUEST", "Invalid JSON");
    return c.json({ error: err.toJSON() }, 400);
  }

  console.log(`[sessions] POST /sessions/reset body:`, JSON.stringify(body));

  const parsed = ResetSchema.safeParse(body);
  if (!parsed.success) {
    const err = appError(
      "INVALID_REQUEST",
      parsed.error.issues.map((i) => i.message).join("; "),
    );
    return c.json({ error: err.toJSON() }, httpStatus(err.code));
  }

  const { exerciseId } = parsed.data;

  try {
    // Kill all active sessions (they may be using this workspace)
    killAllSessions();

    // Delete the workspace so it gets re-downloaded on next start
    await resetWorkspace(exerciseId);

    return c.json({ ok: true });
  } catch (err) {
    console.error(`[sessions] Failed to reset:`, err);
    const fallback = appError(
      "DOWNLOAD_FAILED",
      "Failed to reset exercise workspace",
    );
    return c.json({ error: fallback.toJSON() }, httpStatus(fallback.code));
  }
});

sessions.get("/sessions/:id/status", (c) => {
  const session = getSession(c.req.param("id"));

  if (!session) {
    const err = appError("SESSION_NOT_FOUND", "Session not found");
    return c.json({ error: err.toJSON() }, httpStatus(err.code));
  }

  return c.json({
    sessionId: c.req.param("id"),
    ...session,
  });
});

export default sessions;
