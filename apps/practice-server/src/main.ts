import { Hono } from "hono";
import { cors } from "hono/cors";
import { serve } from "@hono/node-server";
import healthRoutes from "./routes/health.js";
import sessionRoutes from "./routes/sessions.js";
import { handleUpgrade } from "./ws/terminal.js";
import { killAllSessions } from "./pty/manager.js";
import { corsOrigin } from "./middleware/origin.js";

const PORT = parseInt(process.env.PORT || "3100", 10);

const app = new Hono();

app.use("*", cors({ origin: corsOrigin }));

app.route("/", healthRoutes);
app.route("/", sessionRoutes);

const server = serve({ fetch: app.fetch, port: PORT });

// WebSocket upgrade handling
server.on("upgrade", (req, socket, head) => {
  handleUpgrade(req, socket, head);
});

console.log(`[practice] Listening on port ${PORT}`);
console.log(`[practice] Health: http://localhost:${PORT}/health`);

// Graceful shutdown
function shutdown(signal: string) {
  console.log(`\n[practice] Received ${signal}, shutting down...`);
  killAllSessions();
  server.close(() => {
    console.log("[practice] Server closed");
    process.exit(0);
  });
  // Force exit after 5 seconds
  setTimeout(() => {
    console.log("[practice] Forcing exit");
    process.exit(1);
  }, 5000).unref();
}

process.on("SIGTERM", () => shutdown("SIGTERM"));
process.on("SIGINT", () => shutdown("SIGINT"));
