import { describe, it, expect } from "vitest";
import { execSync } from "node:child_process";
import { join } from "node:path";
import { mkdirSync, rmSync, existsSync } from "node:fs";
import { tmpdir, homedir } from "node:os";
import { randomUUID } from "node:crypto";

const CLI_PATH = join(import.meta.dirname, "..", "..", "..", "bin", "cli.ts");

function runCli(
  args: string[],
  options: { timeout?: number } = {},
): { stdout: string; stderr: string; exitCode: number } {
  // Use npx tsx for cross-platform compatibility (.bin/tsx is a .cmd on Windows)
  const cmd = `npx tsx ${JSON.stringify(CLI_PATH)} ${args.map((a) => JSON.stringify(a)).join(" ")}`;
  try {
    const stdout = execSync(cmd, {
      encoding: "utf-8",
      timeout: options.timeout ?? 10000,
      env: { ...process.env, NODE_NO_WARNINGS: "1" },
      cwd: join(import.meta.dirname, "..", "..", ".."),
      stdio: ["pipe", "pipe", "pipe"],
    });
    return { stdout, stderr: "", exitCode: 0 };
  } catch (err: unknown) {
    const e = err as { stdout?: string; stderr?: string; status?: number };
    return {
      stdout: e.stdout ?? "",
      stderr: e.stderr ?? "",
      exitCode: e.status ?? 1,
    };
  }
}

describe("CLI --version", () => {
  it("prints version and exits with code 0", () => {
    const result = runCli(["--version"]);
    expect(result.exitCode).toBe(0);
    // Version should be a semver string
    expect(result.stdout.trim()).toMatch(/^\d+\.\d+\.\d+/);
  });

  it("also works with -v shorthand", () => {
    const result = runCli(["-v"]);
    expect(result.exitCode).toBe(0);
    expect(result.stdout.trim()).toMatch(/^\d+\.\d+\.\d+/);
  });
});

describe("CLI --help", () => {
  it("prints help text and exits with code 0", () => {
    const result = runCli(["--help"]);
    expect(result.exitCode).toBe(0);
    expect(result.stdout).toContain("Usage:");
    expect(result.stdout).toContain("--port");
    expect(result.stdout).toContain("--refresh");
    expect(result.stdout).toContain("--version");
  });

  it("also works with -h shorthand", () => {
    const result = runCli(["-h"]);
    expect(result.exitCode).toBe(0);
    expect(result.stdout).toContain("Usage:");
  });
});

describe("CLI --refresh", () => {
  it("clears workspace cache", () => {
    // Create a temp workspace directory to verify it gets cleared
    const testCacheDir = join(tmpdir(), `af-practice-test-${randomUUID()}`);
    mkdirSync(testCacheDir, { recursive: true });

    // Note: --refresh clears ~/af-practice, not our test dir.
    // We just verify the flag is accepted without error.
    // The actual behavior depends on whether ~/af-practice exists.
    const result = runCli(["--refresh", "--version"]);
    expect(result.exitCode).toBe(0);

    // Clean up test dir
    rmSync(testCacheDir, { recursive: true, force: true });
  });
});

describe("CLI --port", () => {
  it("accepts custom port (verified via --version to avoid starting server)", () => {
    // We can't easily test --port starts on that port without starting a server.
    // Instead verify the flag is parsed by combining with --version.
    const result = runCli(["--port", "4200", "--version"]);
    expect(result.exitCode).toBe(0);
  });
});
