import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { renderHook, act, waitFor } from "@testing-library/react";
import { usePracticeServer } from "../components/TerminalPanel/usePracticeServer";

beforeEach(() => {
  vi.useFakeTimers();
  vi.stubGlobal("fetch", vi.fn());
});

afterEach(() => {
  vi.useRealTimers();
  vi.restoreAllMocks();
});

function mockFetchHealth(available: boolean) {
  (globalThis.fetch as ReturnType<typeof vi.fn>).mockResolvedValue({
    ok: available,
    json: async () => ({ status: "ok", version: "0.1.0", claudeInPath: true }),
  });
}

function mockFetchSession(sessionId = "test-session") {
  (globalThis.fetch as ReturnType<typeof vi.fn>).mockResolvedValue({
    ok: true,
    json: async () => ({ sessionId, wsUrl: `/sessions/${sessionId}/ws` }),
  });
}

function mockFetchError(
  status: number,
  error: { code: string; message: string },
) {
  (globalThis.fetch as ReturnType<typeof vi.fn>).mockResolvedValue({
    ok: false,
    status,
    statusText: "Error",
    json: async () => ({ error }),
  });
}

/**
 * Helper: render the hook with enabled=true and run a successful health check
 * so that the internal baseUrlRef is populated (required for startSession).
 */
async function renderWithServer() {
  mockFetchHealth(true);
  const hookResult = renderHook(() => usePracticeServer(true));

  // Let the initial health poll resolve (port discovery)
  await act(async () => {
    await vi.advanceTimersByTimeAsync(100);
  });

  expect(hookResult.result.current.serverAvailable).toBe(true);
  return hookResult;
}

describe("usePracticeServer", () => {
  describe("initial state", () => {
    it("starts with server unavailable", () => {
      const { result } = renderHook(() => usePracticeServer(false));
      expect(result.current.serverAvailable).toBe(false);
      expect(result.current.isStarting).toBe(false);
      expect(result.current.sessionError).toBeNull();
      expect(result.current.currentSession).toBeNull();
    });
  });

  describe("health polling", () => {
    it("does not poll when disabled", () => {
      renderHook(() => usePracticeServer(false));
      expect(globalThis.fetch).not.toHaveBeenCalled();
    });

    it("polls immediately when enabled", async () => {
      mockFetchHealth(true);
      renderHook(() => usePracticeServer(true));

      await act(async () => {
        await vi.advanceTimersByTimeAsync(0);
      });

      expect(globalThis.fetch).toHaveBeenCalledWith(
        expect.stringContaining("/health"),
        expect.any(Object),
      );
    });

    it("sets serverAvailable to true on healthy response", async () => {
      mockFetchHealth(true);
      const { result } = renderHook(() => usePracticeServer(true));

      await act(async () => {
        await vi.advanceTimersByTimeAsync(100);
      });

      expect(result.current.serverAvailable).toBe(true);
    });

    it("sets serverAvailable to false on failed response", async () => {
      mockFetchHealth(false);
      const { result } = renderHook(() => usePracticeServer(true));

      await act(async () => {
        await vi.advanceTimersByTimeAsync(100);
      });

      expect(result.current.serverAvailable).toBe(false);
    });

    it("stops polling when WS connects", async () => {
      mockFetchHealth(true);
      const { result } = renderHook(() => usePracticeServer(true));

      await act(async () => {
        await vi.advanceTimersByTimeAsync(100);
      });

      const callsBefore = (globalThis.fetch as ReturnType<typeof vi.fn>).mock
        .calls.length;

      act(() => {
        result.current.onWsConnected();
      });

      await act(async () => {
        await vi.advanceTimersByTimeAsync(10000);
      });

      // No additional fetch calls after WS connected
      expect(
        (globalThis.fetch as ReturnType<typeof vi.fn>).mock.calls.length,
      ).toBe(callsBefore);
    });
  });

  describe("startSession", () => {
    it("returns session info on success", async () => {
      const { result } = await renderWithServer();

      // Now mock the session start endpoint
      mockFetchSession("abc-123");

      let session: unknown;
      await act(async () => {
        session = await result.current.startSession("ch3-basics");
      });

      expect(session).toEqual({
        sessionId: "abc-123",
        wsUrl: expect.stringContaining("/sessions/abc-123/ws"),
      });
      expect(result.current.currentSession?.sessionId).toBe("abc-123");
      expect(result.current.isStarting).toBe(false);
    });

    it("sets isStarting during request", async () => {
      const { result } = await renderWithServer();

      let resolvePromise: () => void;
      (globalThis.fetch as ReturnType<typeof vi.fn>).mockReturnValue(
        new Promise((resolve) => {
          resolvePromise = () =>
            resolve({
              ok: true,
              json: async () => ({ sessionId: "x", wsUrl: "/sessions/x/ws" }),
            });
        }),
      );

      let promise: Promise<unknown>;
      act(() => {
        promise = result.current.startSession("ch3-basics");
      });

      expect(result.current.isStarting).toBe(true);

      await act(async () => {
        resolvePromise!();
        await promise!;
      });

      expect(result.current.isStarting).toBe(false);
    });

    it("sets sessionError on typed error response", async () => {
      const { result } = await renderWithServer();

      mockFetchError(404, { code: "EXERCISE_NOT_FOUND", message: "Not found" });

      await act(async () => {
        await result.current.startSession("nonexistent");
      });

      expect(result.current.sessionError).toEqual({
        code: "EXERCISE_NOT_FOUND",
        message: "Not found",
      });
      expect(result.current.currentSession).toBeNull();
    });

    it("passes subExercise to server", async () => {
      const { result } = await renderWithServer();

      mockFetchSession();

      await act(async () => {
        await result.current.startSession("ch3-basics", "1.1");
      });

      expect(globalThis.fetch).toHaveBeenCalledWith(
        expect.stringContaining("/sessions/start"),
        expect.objectContaining({
          body: JSON.stringify({
            exerciseId: "ch3-basics",
            subExercise: "1.1",
          }),
        }),
      );
    });

    it("returns null when server not discovered", async () => {
      // Don't run health check — baseUrlRef stays null
      const { result } = renderHook(() => usePracticeServer(false));

      let session: unknown;
      await act(async () => {
        session = await result.current.startSession("ch3-basics");
      });

      expect(session).toBeNull();
    });
  });

  describe("clearError", () => {
    it("clears session error", async () => {
      const { result } = await renderWithServer();

      mockFetchError(404, { code: "EXERCISE_NOT_FOUND", message: "Not found" });

      await act(async () => {
        await result.current.startSession("nonexistent");
      });
      expect(result.current.sessionError).not.toBeNull();

      act(() => {
        result.current.clearError();
      });
      expect(result.current.sessionError).toBeNull();
    });
  });

  describe("WS lifecycle callbacks", () => {
    it("onWsError sets session error", () => {
      const { result } = renderHook(() => usePracticeServer(true));

      act(() => {
        result.current.onWsError({
          code: "PTY_EXITED",
          message: "Process exited",
        });
      });

      expect(result.current.sessionError?.code).toBe("PTY_EXITED");
    });
  });
});
