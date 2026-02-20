#!/usr/bin/env node

import { readFileSync, rmSync, existsSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { homedir } from "node:os";

const __dirname = dirname(fileURLToPath(import.meta.url));

// Parse CLI arguments BEFORE node-pty check so --version/--help always work
const args = process.argv.slice(2);

// Read version from package.json
// Source: bin/cli.ts → one level up. Dist: dist/bin/cli.js → two levels up.
const pkgPath = existsSync(join(__dirname, "..", "package.json"))
  ? join(__dirname, "..", "package.json")
  : join(__dirname, "..", "..", "package.json");
const pkg = JSON.parse(readFileSync(pkgPath, "utf-8"));

if (args.includes("--version") || args.includes("-v")) {
  console.log(pkg.version);
  process.exit(0);
}

if (args.includes("--help") || args.includes("-h")) {
  console.log(`
af-practice v${pkg.version}

Usage: npx af-practice [options]

Options:
  --port <number>  Port to listen on (default: 3100)
  --refresh        Clear cached workspaces before starting
  --version, -v    Print version and exit
  --help, -h       Show this help message
`);
  process.exit(0);
}

// Handle --refresh: clear workspace cache
if (args.includes("--refresh")) {
  const practiceRoot = join(homedir(), "af-practice");
  console.log(`[cli] Clearing workspace cache at ${practiceRoot}`);
  try {
    rmSync(practiceRoot, { recursive: true, force: true });
    console.log("[cli] Cache cleared");
  } catch (err) {
    console.warn(
      "[cli] Could not clear cache:",
      err instanceof Error ? err.message : err,
    );
  }
}

// Handle --port
const portIndex = args.indexOf("--port");
if (portIndex !== -1 && args[portIndex + 1]) {
  process.env.PORT = args[portIndex + 1];
}

// Check node-pty availability before starting the server (Decision #19)
// This is after flag parsing so --version/--help work without native deps
try {
  await import("node-pty");
} catch {
  console.error("Could not load terminal support (node-pty).");
  console.error("");
  if (process.platform === "darwin") {
    console.error("  Fix: xcode-select --install");
  } else if (process.platform === "linux") {
    console.error("  Fix: sudo apt-get install -y build-essential");
  } else {
    console.error("  Your platform may need a C++ compiler.");
  }
  console.error("");
  console.error("Or use the manual exercise download workflow instead.");
  process.exit(1);
}

// Make version available to server routes (health endpoint)
process.env.PRACTICE_VERSION = pkg.version;

// Import and start the server (this triggers resolveClaudePath() at startup)
const { resolveClaudePath, getCachedClaudePath } =
  await import("../src/claude-path.js");
resolveClaudePath();

const port = process.env.PORT || "3100";
const claudePath = getCachedClaudePath();

console.log("");
console.log(`  af-practice v${pkg.version}`);
console.log(`  ──────────────────────────────────────`);
console.log(`  Port:   ${port}`);
console.log(
  `  Claude: ${claudePath ? claudePath : "NOT FOUND (install Claude Code)"}`,
);
console.log(`  Health: http://localhost:${port}/health`);
console.log("");

// Start the server by importing main.ts (it self-starts on import)
await import("../src/main.js");
