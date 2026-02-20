import { execFileSync } from "node:child_process";
import { accessSync, constants } from "node:fs";
import { join } from "node:path";
import { homedir } from "node:os";

const isWindows = process.platform === "win32";

let cachedPath: string | null = null;
let resolved = false;

/** Resolve full path to `claude` binary. Cross-platform. Called once at startup. Idempotent. */
export function resolveClaudePath(): void {
  if (resolved) return;
  resolved = true;

  // Strategy 1: Use the system's PATH lookup command
  cachedPath = resolveViaPathLookup();
  if (cachedPath) {
    console.log(`[claude-path] Resolved: ${cachedPath}`);
    return;
  }

  // Strategy 2: Check common install locations
  cachedPath = resolveViaFallbackPaths();
  if (cachedPath) {
    console.log(`[claude-path] Resolved (fallback): ${cachedPath}`);
    return;
  }

  console.warn("[claude-path] Claude binary not found in PATH");
  cachedPath = null;
}

function resolveViaPathLookup(): string | null {
  try {
    if (isWindows) {
      // On Windows, `where.exe` finds executables in PATH (equivalent to `which`)
      const result = execFileSync("where.exe", ["claude"], {
        encoding: "utf-8",
        timeout: 5000,
        windowsHide: true,
      });
      // `where` can return multiple lines; take the first match
      return result.trim().split(/\r?\n/)[0];
    } else {
      // On Unix, use the user's login shell so that ~/.bashrc / ~/.zshrc PATH additions are visible
      const userShell = process.env.SHELL || "/bin/bash";
      const result = execFileSync(userShell, ["-l", "-c", "which claude"], {
        encoding: "utf-8",
        timeout: 5000,
      });
      return result.trim();
    }
  } catch {
    return null;
  }
}

function resolveViaFallbackPaths(): string | null {
  const home = homedir();
  const paths: string[] = isWindows
    ? [
        // Claude Code Windows installer locations
        join(
          process.env.LOCALAPPDATA || join(home, "AppData", "Local"),
          "Programs",
          "claude-code",
          "claude.exe",
        ),
        join(
          process.env.LOCALAPPDATA || join(home, "AppData", "Local"),
          "Microsoft",
          "WinGet",
          "Packages",
          "Anthropic.Claude_*",
          "claude.exe",
        ),
        // npm global
        join(
          process.env.APPDATA || join(home, "AppData", "Roaming"),
          "npm",
          "claude.cmd",
        ),
      ]
    : [
        join(home, ".local", "bin", "claude"),
        "/usr/local/bin/claude",
        join(home, ".claude", "bin", "claude"),
      ];

  for (const p of paths) {
    if (isExecutable(p)) return p;
  }
  return null;
}

function isExecutable(filePath: string): boolean {
  try {
    // On Windows, accessSync with X_OK checks if file exists and is executable.
    // On Unix, it checks the execute permission bit.
    accessSync(filePath, constants.X_OK);
    return true;
  } catch {
    return false;
  }
}

/** Get the cached claude path. Returns null if claude was not found at startup. */
export function getCachedClaudePath(): string | null {
  return cachedPath;
}
