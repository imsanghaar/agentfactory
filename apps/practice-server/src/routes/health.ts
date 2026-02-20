import { Hono } from "hono";
import { getCachedClaudePath } from "../claude-path.js";

const health = new Hono();

health.get("/health", (c) => {
  return c.json({
    status: "ok",
    version: process.env.PRACTICE_VERSION || "0.0.0",
    claudeInPath: getCachedClaudePath() !== null,
  });
});

export default health;
