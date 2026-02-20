import { describe, it, expect, beforeAll, afterAll } from "vitest";
import { Hono } from "hono";
import { cors } from "hono/cors";
import { serve, type ServerType } from "@hono/node-server";
import { WebSocket } from "ws";
import healthRoutes from "../../routes/health.js";
import sessionRoutes from "../../routes/sessions.js";
import { handleUpgrade } from "../../ws/terminal.js";
import { killAllSessions } from "../../pty/manager.js";
import { corsOrigin } from "../../middleware/origin.js";

let server: ServerType;
let baseUrl: string;
let port: number;

beforeAll(async () => {
  const app = new Hono();
  app.use("*", cors({ origin: corsOrigin }));
  app.route("/", healthRoutes);
  app.route("/", sessionRoutes);

  server = serve({ fetch: app.fetch, port: 0 });

  server.on("upgrade", (req, socket, head) => {
    handleUpgrade(req, socket, head, { pingInterval: 100, pongTimeout: 50 });
  });

  await new Promise<void>((resolve) => {
    server.on("listening", () => {
      const addr = server.address();
      if (typeof addr === "object" && addr) {
        port = addr.port;
        baseUrl = `http://localhost:${port}`;
      }
      resolve();
    });
  });
});

afterAll(async () => {
  killAllSessions();
  await new Promise<void>((resolve) => {
    server.close(() => resolve());
  });
});

describe("health endpoint", () => {
  it("returns JSON with status ok", async () => {
    const res = await fetch(`${baseUrl}/health`);
    expect(res.ok).toBe(true);

    const body = await res.json();
    expect(body.status).toBe("ok");
    expect(body).toHaveProperty("version");
    expect(body).toHaveProperty("claudeInPath");
    expect(typeof body.claudeInPath).toBe("boolean");
  });

  it("responds with correct content-type", async () => {
    const res = await fetch(`${baseUrl}/health`);
    expect(res.headers.get("content-type")).toContain("application/json");
  });
});

describe("sessions endpoint", () => {
  it("returns 400 for missing exerciseId", async () => {
    const res = await fetch(`${baseUrl}/sessions/start`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({}),
    });
    expect(res.status).toBe(400);

    const body = await res.json();
    expect(body.error).toBeDefined();
    expect(body.error.code).toBe("INVALID_REQUEST");
  });

  it("returns 400 for invalid exerciseId characters", async () => {
    const res = await fetch(`${baseUrl}/sessions/start`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ exerciseId: "../bad" }),
    });
    expect(res.status).toBe(400);

    const body = await res.json();
    expect(body.error.code).toBe("INVALID_REQUEST");
  });

  it("returns 404 for unknown exercise", async () => {
    const res = await fetch(`${baseUrl}/sessions/start`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ exerciseId: "nonexistent-exercise" }),
    });
    expect(res.status).toBe(404);

    const body = await res.json();
    expect(body.error.code).toBe("EXERCISE_NOT_FOUND");
  });

  it("returns 404 for nonexistent session status", async () => {
    const res = await fetch(`${baseUrl}/sessions/fake-id/status`);
    expect(res.status).toBe(404);

    const body = await res.json();
    expect(body.error.code).toBe("SESSION_NOT_FOUND");
  });
});

describe("CORS", () => {
  it("allows localhost origin", async () => {
    const res = await fetch(`${baseUrl}/health`, {
      headers: { Origin: `http://localhost:${port}` },
    });
    expect(res.ok).toBe(true);
    // cors middleware sets this header for allowed origins
    expect(res.headers.get("access-control-allow-origin")).toBeTruthy();
  });
});

describe("WebSocket upgrade", () => {
  it("rejects upgrade for nonexistent session", async () => {
    const ws = new WebSocket(`ws://localhost:${port}/sessions/nonexistent/ws`);

    const closePromise = new Promise<{ code: number }>((resolve) => {
      ws.on("error", () => {
        // Expected - connection refused or closed
      });
      ws.on("close", (code) => {
        resolve({ code });
      });
    });

    const result = await closePromise;
    // WebSocket should be closed (connection rejected)
    expect(ws.readyState).toBeGreaterThanOrEqual(WebSocket.CLOSING);
  });

  it("rejects upgrade for invalid URL path", async () => {
    const ws = new WebSocket(`ws://localhost:${port}/invalid/path`);

    await new Promise<void>((resolve) => {
      ws.on("error", () => resolve());
      ws.on("close", () => resolve());
    });

    expect(ws.readyState).toBeGreaterThanOrEqual(WebSocket.CLOSING);
  });
});
