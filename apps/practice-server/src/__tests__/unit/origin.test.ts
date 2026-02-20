import { describe, it, expect } from "vitest";
import {
  ORIGIN_RE,
  isValidOrigin,
  corsOrigin,
} from "../../middleware/origin.js";
import type { IncomingMessage } from "node:http";

function fakeReq(origin?: string): IncomingMessage {
  return { headers: { origin } } as unknown as IncomingMessage;
}

describe("ORIGIN_RE regex", () => {
  it("matches http://localhost", () => {
    expect(ORIGIN_RE.test("http://localhost")).toBe(true);
  });

  it("matches http://localhost with port", () => {
    expect(ORIGIN_RE.test("http://localhost:3000")).toBe(true);
  });

  it("matches https://localhost", () => {
    expect(ORIGIN_RE.test("https://localhost")).toBe(true);
  });

  it("matches https://localhost with port", () => {
    expect(ORIGIN_RE.test("https://localhost:8080")).toBe(true);
  });

  it("matches http://127.0.0.1", () => {
    expect(ORIGIN_RE.test("http://127.0.0.1")).toBe(true);
  });

  it("matches http://127.0.0.1 with port", () => {
    expect(ORIGIN_RE.test("http://127.0.0.1:3100")).toBe(true);
  });

  it("matches https://127.0.0.1 with port", () => {
    expect(ORIGIN_RE.test("https://127.0.0.1:443")).toBe(true);
  });

  it("rejects external domains", () => {
    expect(ORIGIN_RE.test("https://example.com")).toBe(false);
  });

  it("rejects localhost substring in domain", () => {
    expect(ORIGIN_RE.test("https://notlocalhost:3000")).toBe(false);
  });

  it("rejects localhost with path", () => {
    expect(ORIGIN_RE.test("http://localhost:3000/path")).toBe(false);
  });

  it("rejects empty string", () => {
    expect(ORIGIN_RE.test("")).toBe(false);
  });

  it("rejects 127.0.0.1 with extra octets", () => {
    expect(ORIGIN_RE.test("http://127.0.0.10:3000")).toBe(false);
  });

  it("matches high port numbers", () => {
    expect(ORIGIN_RE.test("http://localhost:65535")).toBe(true);
  });

  it("rejects ftp protocol", () => {
    expect(ORIGIN_RE.test("ftp://localhost:3000")).toBe(false);
  });

  it("rejects IPv6 localhost", () => {
    expect(ORIGIN_RE.test("http://[::1]:3000")).toBe(false);
  });
});

describe("isValidOrigin", () => {
  it("allows requests with no origin header (curl, wscat)", () => {
    expect(isValidOrigin(fakeReq(undefined))).toBe(true);
  });

  it("allows requests with empty origin header", () => {
    expect(isValidOrigin(fakeReq(""))).toBe(true);
  });

  it("allows localhost origin", () => {
    expect(isValidOrigin(fakeReq("http://localhost:3000"))).toBe(true);
  });

  it("allows 127.0.0.1 origin", () => {
    expect(isValidOrigin(fakeReq("http://127.0.0.1:3100"))).toBe(true);
  });

  it("rejects external origin", () => {
    expect(isValidOrigin(fakeReq("https://evil.com"))).toBe(false);
  });

  it("rejects origin with localhost as subdomain", () => {
    expect(isValidOrigin(fakeReq("https://localhost.evil.com"))).toBe(false);
  });
});

describe("corsOrigin", () => {
  it("returns the origin for localhost", () => {
    expect(corsOrigin("http://localhost:3000")).toBe("http://localhost:3000");
  });

  it("returns the origin for 127.0.0.1", () => {
    expect(corsOrigin("http://127.0.0.1:3100")).toBe("http://127.0.0.1:3100");
  });

  it("returns undefined for external origins", () => {
    expect(corsOrigin("https://evil.com")).toBeUndefined();
  });

  it("returns empty string as-is for missing origin", () => {
    // Hono passes empty string when no Origin header is present
    expect(corsOrigin("")).toBe("");
  });
});
