import * as schema from "../../../auth-schema"; // Use Better Auth generated schema

// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
// Environment Variable Validation
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

/**
 * Get database URL with clear error messages for missing configuration
 */
const getDatabaseUrl = (): string => {
  if (process.env.DATABASE_URL) {
    return process.env.DATABASE_URL;
  }
  
  // In production (Vercel runtime), DATABASE_URL is absolutely required
  if (process.env.NODE_ENV === "production" && !process.env.NEXT_PHASE) {
    console.error("[DB] CRITICAL: DATABASE_URL not set in production!");
    console.error("[DB] Please add DATABASE_URL to your Vercel environment variables.");
    console.error("[DB] Get a free PostgreSQL database at: https://neon.tech");
    throw new Error(
      "DATABASE_URL must be set in production. " +
      "Add it to Vercel environment variables (Production scope)."
    );
  }
  
  // Development/build placeholder (prevents build failures)
  return "postgresql://placeholder:placeholder@localhost:5432/placeholder";
};

/**
 * Initialize database connection with environment-aware driver selection
 *
 * - Production/Neon: Uses @neondatabase/serverless (HTTP/WebSockets)
 * - CI/Standard PostgreSQL: Uses postgres (TCP)
 *
 * Detection: If DATABASE_URL contains "localhost" or "127.0.0.1", use standard PostgreSQL
 */
function initDatabase() {
  const databaseUrl = getDatabaseUrl();
  const isLocalPostgres =
    databaseUrl.includes("localhost") || databaseUrl.includes("127.0.0.1");

  if (isLocalPostgres) {
    // Standard PostgreSQL (CI, local development with standard Postgres)
    const postgres = require("postgres");
    const { drizzle } = require("drizzle-orm/postgres-js");
    const sql = postgres(databaseUrl);
    return drizzle(sql, { schema });
  } else {
    // Neon serverless (production, staging)
    const { neon } = require("@neondatabase/serverless");
    const { drizzle } = require("drizzle-orm/neon-http");
    const sql = neon(databaseUrl);
    return drizzle(sql, { schema });
  }
}

export const db = initDatabase();

export type Database = typeof db;
