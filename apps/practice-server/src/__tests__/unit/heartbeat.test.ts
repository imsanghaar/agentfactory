import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { EventEmitter } from "node:events";
import type { WebSocket } from "ws";
import { startHeartbeat } from "../../ws/terminal.js";

/** Minimal mock that satisfies startHeartbeat's needs: on("pong"), ping(), terminate() */
function createMockWs() {
  const emitter = new EventEmitter();
  const ping = vi.fn();
  const terminate = vi.fn();
  Object.assign(emitter, { ping, terminate });
  return emitter as unknown as WebSocket & {
    ping: typeof ping;
    terminate: typeof terminate;
    emit: EventEmitter["emit"];
  };
}

describe("startHeartbeat", () => {
  beforeEach(() => {
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.useRealTimers();
  });

  it("sends ping at the configured interval", () => {
    const ws = createMockWs();
    const stop = startHeartbeat(ws, { pingInterval: 100, pongTimeout: 50 });

    expect(ws.ping).not.toHaveBeenCalled();

    vi.advanceTimersByTime(100);
    expect(ws.ping).toHaveBeenCalledTimes(1);

    // Simulate pong response so connection stays alive
    ws.emit("pong");

    vi.advanceTimersByTime(100);
    expect(ws.ping).toHaveBeenCalledTimes(2);

    stop();
  });

  it("terminates connection when pong is not received within timeout", () => {
    const ws = createMockWs();
    const stop = startHeartbeat(ws, { pingInterval: 100, pongTimeout: 50 });

    // First ping fires at 100ms
    vi.advanceTimersByTime(100);
    expect(ws.ping).toHaveBeenCalledTimes(1);
    expect(ws.terminate).not.toHaveBeenCalled();

    // No pong received — wait for pongTimeout (50ms)
    vi.advanceTimersByTime(50);
    expect(ws.terminate).toHaveBeenCalledTimes(1);

    stop();
  });

  it("does not terminate if pong arrives before timeout", () => {
    const ws = createMockWs();
    const stop = startHeartbeat(ws, { pingInterval: 100, pongTimeout: 50 });

    vi.advanceTimersByTime(100);
    expect(ws.ping).toHaveBeenCalledTimes(1);

    // Pong arrives 20ms after ping (before 50ms timeout)
    vi.advanceTimersByTime(20);
    ws.emit("pong");

    // Wait past the pong timeout — should NOT terminate
    vi.advanceTimersByTime(50);
    expect(ws.terminate).not.toHaveBeenCalled();

    stop();
  });

  it("terminates on second ping if first pong was missed", () => {
    const ws = createMockWs();
    const stop = startHeartbeat(ws, { pingInterval: 100, pongTimeout: 200 });

    // First ping at 100ms, pong timeout is 200ms
    vi.advanceTimersByTime(100);
    expect(ws.ping).toHaveBeenCalledTimes(1);

    // Don't send pong, but second interval fires before pong timeout
    // alive is still false at the next interval tick -> terminate
    vi.advanceTimersByTime(100);
    expect(ws.terminate).toHaveBeenCalledTimes(1);

    stop();
  });

  it("cleanup function stops all timers", () => {
    const ws = createMockWs();
    const stop = startHeartbeat(ws, { pingInterval: 100, pongTimeout: 50 });

    stop();

    // Advance well past intervals — nothing should fire
    vi.advanceTimersByTime(500);
    expect(ws.ping).not.toHaveBeenCalled();
    expect(ws.terminate).not.toHaveBeenCalled();
  });
});
