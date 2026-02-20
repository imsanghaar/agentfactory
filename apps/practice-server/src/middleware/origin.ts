import type { IncomingMessage } from "node:http";

/** Localhost origins (dev) */
const LOCALHOST_RE = /^https?:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/;

/** Production origins that may connect to the local practice server */
const PROD_ORIGINS = [
  "https://agentfactory.panaversity.org",
  "https://agentfactory.dev",
];

export { LOCALHOST_RE as ORIGIN_RE };

/**
 * CORS origin callback for Hono cors() middleware.
 * Allows localhost (dev) and production origins (students visiting the live site
 * connect to their own local practice server).
 */
export function corsOrigin(origin: string): string | undefined {
  if (!origin) return origin;
  if (LOCALHOST_RE.test(origin)) return origin;
  if (PROD_ORIGINS.includes(origin)) return origin;
  return undefined;
}

/**
 * Validate that a WebSocket upgrade request comes from a trusted origin.
 */
export function isValidOrigin(req: IncomingMessage): boolean {
  const origin = req.headers.origin || "";
  // Allow requests with no origin (e.g., curl, wscat)
  if (!origin) return true;
  if (LOCALHOST_RE.test(origin)) return true;
  if (PROD_ORIGINS.includes(origin)) return true;
  return false;
}
