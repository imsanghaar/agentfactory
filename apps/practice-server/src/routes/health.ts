import { Hono } from "hono";
import { getCachedQwenPath } from "../qwen-path.js";

const health = new Hono();

health.get("/health", (c) => {
  return c.json({
    status: "ok",
    version: process.env.PRACTICE_VERSION || "0.0.0",
    qwenInPath: getCachedQwenPath() !== null,
  });
});

export default health;
