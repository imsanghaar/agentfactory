import { describe, it, expect, beforeEach, afterEach } from "vitest";
import * as pty from "node-pty";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { mkdir, rm } from "node:fs/promises";
import { randomUUID } from "node:crypto";

// Test PTY spawning directly with node-pty (not through manager.ts which requires claude binary).
// This verifies node-pty works on the current platform.
// Skip in CI: GitHub Actions runners lack proper PTY support (posix_spawnp fails).
const isCI = !!process.env.CI;

let testDir: string;

beforeEach(async () => {
  testDir = join(tmpdir(), `pty-test-${randomUUID()}`);
  await mkdir(testDir, { recursive: true });
});

afterEach(async () => {
  await rm(testDir, { recursive: true, force: true });
});

describe.skipIf(isCI)("node-pty spawn", () => {
  it("spawns a process and receives output", async () => {
    const output: string[] = [];

    const proc = pty.spawn(
      "node",
      ["-e", 'process.stdout.write("hello-pty")'],
      {
        name: "xterm-256color",
        cols: 80,
        rows: 24,
        cwd: testDir,
      },
    );

    await new Promise<void>((resolve, reject) => {
      const timeout = setTimeout(
        () => reject(new Error("Timed out waiting for PTY output")),
        5000,
      );

      proc.onData((data) => {
        output.push(data);
        if (output.join("").includes("hello-pty")) {
          clearTimeout(timeout);
          resolve();
        }
      });

      proc.onExit(() => {
        clearTimeout(timeout);
        resolve();
      });
    });

    const fullOutput = output.join("");
    expect(fullOutput).toContain("hello-pty");

    proc.kill();
  });

  it("handles process exit", async () => {
    const proc = pty.spawn("node", ["-e", "process.exit(42)"], {
      name: "xterm-256color",
      cols: 80,
      rows: 24,
      cwd: testDir,
    });

    const exitCode = await new Promise<number>((resolve, reject) => {
      const timeout = setTimeout(
        () => reject(new Error("Timed out waiting for exit")),
        5000,
      );
      proc.onExit(({ exitCode }) => {
        clearTimeout(timeout);
        resolve(exitCode);
      });
    });

    expect(exitCode).toBe(42);
  });

  it("can write to stdin", async () => {
    const output: string[] = [];

    // Node script that reads stdin and echoes it
    const script = `
      process.stdin.setEncoding('utf8');
      process.stdin.on('data', (d) => {
        process.stdout.write('ECHO:' + d.trim());
        process.exit(0);
      });
    `;

    const proc = pty.spawn("node", ["-e", script], {
      name: "xterm-256color",
      cols: 80,
      rows: 24,
      cwd: testDir,
    });

    await new Promise<void>((resolve, reject) => {
      const timeout = setTimeout(() => reject(new Error("Timed out")), 5000);

      proc.onData((data) => {
        output.push(data);
        if (output.join("").includes("ECHO:test-input")) {
          clearTimeout(timeout);
          resolve();
        }
      });

      proc.onExit(() => {
        clearTimeout(timeout);
        resolve();
      });

      // Send data to stdin after a brief delay
      setTimeout(() => proc.write("test-input\r"), 100);
    });

    const fullOutput = output.join("");
    expect(fullOutput).toContain("ECHO:test-input");

    proc.kill();
  });

  it("supports resize", () => {
    const proc = pty.spawn("node", ["-e", "setTimeout(() => {}, 5000)"], {
      name: "xterm-256color",
      cols: 80,
      rows: 24,
      cwd: testDir,
    });

    // Resize should not throw
    expect(() => proc.resize(120, 40)).not.toThrow();

    proc.kill();
  });
});
