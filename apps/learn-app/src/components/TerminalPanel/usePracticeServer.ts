import { useState, useEffect, useCallback, useRef } from "react";
import type { AppError } from "@/types/practice";

const HEALTH_POLL_INTERVAL = 5000;
const SCAN_PORTS = [
  3100, 3101, 3102, 3103, 3104, 3105, 3106, 3107, 3108, 3109, 3110,
];
const SCAN_TIMEOUT_MS = 1000;

interface SessionInfo {
  sessionId: string;
  wsUrl: string;
}

/**
 * Scan ports 3100-3110 in parallel; first healthy response wins.
 * Returns base URL like "http://localhost:3102" or null.
 */
async function discoverPracticeServer(): Promise<string | null> {
  const results = await Promise.allSettled(
    SCAN_PORTS.map(async (port) => {
      const res = await fetch(`http://localhost:${port}/health`, {
        signal: AbortSignal.timeout(SCAN_TIMEOUT_MS),
      });
      if (res.ok) return port;
      throw new Error("not ok");
    }),
  );
  const found = results.find(
    (r): r is PromiseFulfilledResult<number> => r.status === "fulfilled",
  );
  return found ? `http://localhost:${found.value}` : null;
}

export function usePracticeServer(enabled = false) {
  const [serverAvailable, setServerAvailable] = useState(false);
  const [isStarting, setIsStarting] = useState(false);
  const [sessionError, setSessionError] = useState<AppError | null>(null);
  const [currentSession, setCurrentSession] = useState<SessionInfo | null>(
    null,
  );
  const [wsConnected, setWsConnected] = useState(false);
  const pollRef = useRef<ReturnType<typeof setInterval> | null>(null);
  /** Cache discovered base URL for the session */
  const baseUrlRef = useRef<string | null>(null);

  const stopPolling = useCallback(() => {
    if (pollRef.current) {
      clearInterval(pollRef.current);
      pollRef.current = null;
    }
  }, []);

  const checkHealth = useCallback(async (): Promise<boolean> => {
    try {
      // If we already know the port, check only that one
      if (baseUrlRef.current) {
        const res = await fetch(`${baseUrlRef.current}/health`, {
          signal: AbortSignal.timeout(3000),
        });
        if (res.ok) {
          setServerAvailable(true);
          return true;
        }
        // Port went away — clear cache and re-scan next time
        baseUrlRef.current = null;
      }

      // Full port scan
      const url = await discoverPracticeServer();
      if (url) {
        baseUrlRef.current = url;
        setServerAvailable(true);
        return true;
      }
    } catch {
      // Server not available
    }
    setServerAvailable(false);
    return false;
  }, []);

  const startSession = useCallback(
    async (
      exerciseId: string,
      subExercise?: string,
    ): Promise<SessionInfo | null> => {
      const serverUrl = baseUrlRef.current;
      if (!serverUrl) return null;

      setIsStarting(true);
      setSessionError(null);
      try {
        const res = await fetch(`${serverUrl}/sessions/start`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ exerciseId, subExercise }),
        });
        if (!res.ok) {
          const body = await res.json().catch(() => ({}));
          if (body.error?.code) {
            throw body.error as AppError;
          }
          throw {
            code: "UNKNOWN",
            message: body.error || `Failed to start session: ${res.statusText}`,
          } as AppError;
        }
        const data = await res.json();
        // Derive WS URL from discovered base URL
        const wsBase = serverUrl.replace(/^http/, "ws");
        const session: SessionInfo = {
          sessionId: data.sessionId,
          wsUrl: `${wsBase}${data.wsUrl}`,
        };
        setCurrentSession(session);
        return session;
      } catch (err) {
        const appError: AppError = (err as AppError).code
          ? (err as AppError)
          : {
              code: "UNKNOWN",
              message:
                err instanceof Error ? err.message : "Failed to start session",
            };
        console.error("Failed to start practice session:", appError.message);
        setSessionError(appError);
        return null;
      } finally {
        setIsStarting(false);
      }
    },
    [],
  );

  const clearError = useCallback(() => {
    setSessionError(null);
  }, []);

  const resetSession = useCallback(
    async (exerciseId: string): Promise<boolean> => {
      const serverUrl = baseUrlRef.current;
      if (!serverUrl) return false;

      try {
        const res = await fetch(`${serverUrl}/sessions/reset`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ exerciseId }),
        });
        if (!res.ok) return false;
        setCurrentSession(null);
        setSessionError(null);
        return true;
      } catch {
        return false;
      }
    },
    [],
  );

  /** Called by TerminalPanel when WS connects */
  const onWsConnected = useCallback(() => {
    setWsConnected(true);
  }, []);

  /** Called by TerminalPanel when WS disconnects */
  const onWsDisconnected = useCallback(() => {
    setWsConnected(false);
  }, []);

  /** Called by TerminalPanel when WS receives an error frame */
  const onWsError = useCallback((error: AppError) => {
    setSessionError(error);
  }, []);

  // Health poll lifecycle: poll when enabled + server not available + WS not connected
  // Stop polling when WS connects, resume when WS disconnects
  useEffect(() => {
    if (!enabled) {
      stopPolling();
      return;
    }

    // Don't poll while WS is connected — session is active
    if (wsConnected) {
      stopPolling();
      return;
    }

    if (!serverAvailable) {
      checkHealth(); // Immediate check
      pollRef.current = setInterval(checkHealth, HEALTH_POLL_INTERVAL);
    } else if (pollRef.current) {
      stopPolling();
    }

    return stopPolling;
  }, [enabled, serverAvailable, wsConnected, checkHealth, stopPolling]);

  return {
    serverAvailable,
    isStarting,
    sessionError,
    currentSession,
    startSession,
    resetSession,
    checkHealth,
    clearError,
    onWsConnected,
    onWsDisconnected,
    onWsError,
  };
}
