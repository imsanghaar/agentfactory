import React, { useEffect, useRef, useCallback, useState } from "react";
import { Terminal } from "@xterm/xterm";
import { FitAddon } from "@xterm/addon-fit";
import "@xterm/xterm/css/xterm.css";
import styles from "./styles.module.css";
import { PracticeErrorCard } from "../PracticeErrorCard";
import type { AppError } from "@/types/practice";

type ConnectionState =
  | "connecting"
  | "connected"
  | "reconnecting"
  | "disconnected";

interface TerminalPanelProps {
  wsUrl: string;
  onDisconnect?: () => void;
  onWsConnected?: () => void;
  onWsDisconnected?: () => void;
  onWsError?: (error: AppError) => void;
  onRestart?: () => void;
}

export function TerminalPanel({
  wsUrl,
  onDisconnect,
  onWsConnected,
  onWsDisconnected,
  onWsError,
  onRestart,
}: TerminalPanelProps) {
  const termRef = useRef<HTMLDivElement>(null);
  const terminalRef = useRef<Terminal | null>(null);
  const fitAddonRef = useRef<FitAddon | null>(null);
  const wsRef = useRef<WebSocket | null>(null);
  const [connectionState, setConnectionState] =
    useState<ConnectionState>("connecting");
  const [wsError, setWsError] = useState<AppError | null>(null);

  // Stabilize callback refs to prevent terminal teardown/reconnect on parent re-render
  const onWsConnectedRef = useRef(onWsConnected);
  const onWsDisconnectedRef = useRef(onWsDisconnected);
  const onWsErrorRef = useRef(onWsError);
  const onDisconnectRef = useRef(onDisconnect);

  useEffect(() => {
    onWsConnectedRef.current = onWsConnected;
  }, [onWsConnected]);
  useEffect(() => {
    onWsDisconnectedRef.current = onWsDisconnected;
  }, [onWsDisconnected]);
  useEffect(() => {
    onWsErrorRef.current = onWsError;
  }, [onWsError]);
  useEffect(() => {
    onDisconnectRef.current = onDisconnect;
  }, [onDisconnect]);

  const connect = useCallback(() => {
    if (!terminalRef.current) return;

    setConnectionState("connecting");
    setWsError(null);
    const ws = new WebSocket(wsUrl);
    ws.binaryType = "arraybuffer";
    wsRef.current = ws;

    ws.onopen = () => {
      setConnectionState("connected");
      onWsConnectedRef.current?.();
      // Send initial resize
      if (terminalRef.current) {
        const { cols, rows } = terminalRef.current;
        ws.send(JSON.stringify({ type: "resize", cols, rows }));
      }
    };

    ws.onmessage = (event) => {
      if (terminalRef.current) {
        if (event.data instanceof ArrayBuffer) {
          // Binary frame: terminal output
          terminalRef.current.write(new Uint8Array(event.data));
        } else {
          // Text frame: could be error or other control message
          try {
            const msg = JSON.parse(event.data);
            if (msg.type === "error" && msg.error) {
              const error: AppError = msg.error;
              setWsError(error);
              onWsErrorRef.current?.(error);
              return;
            }
          } catch {
            // Not JSON — treat as plain text terminal output
          }
          terminalRef.current.write(event.data);
        }
      }
    };

    ws.onclose = () => {
      setConnectionState("disconnected");
      onWsDisconnectedRef.current?.();
      onDisconnectRef.current?.();
    };

    ws.onerror = () => {
      setConnectionState("disconnected");
    };
  }, [wsUrl]);

  useEffect(() => {
    if (!termRef.current) return;

    const terminal = new Terminal({
      cursorBlink: true,
      fontSize: 14,
      fontFamily: "'SF Mono', 'Fira Code', 'Cascadia Code', Menlo, monospace",
      scrollback: 5000,
      theme: {
        background: "#1a1b26",
        foreground: "#c0caf5",
        cursor: "#c0caf5",
        selectionBackground: "#33467c",
        black: "#15161e",
        red: "#f7768e",
        green: "#9ece6a",
        yellow: "#e0af68",
        blue: "#7aa2f7",
        magenta: "#bb9af7",
        cyan: "#7dcfff",
        white: "#a9b1d6",
      },
      allowProposedApi: true,
    });

    const fitAddon = new FitAddon();
    terminal.loadAddon(fitAddon);
    terminal.open(termRef.current);
    fitAddon.fit();

    terminalRef.current = terminal;
    fitAddonRef.current = fitAddon;

    // Handle user input -> send to WS
    terminal.onData((data) => {
      if (wsRef.current?.readyState === WebSocket.OPEN) {
        // Send as binary
        const encoder = new TextEncoder();
        wsRef.current.send(encoder.encode(data));
      }
    });

    // Handle resize with debounced fit() to prevent TUI flicker during drag
    let fitTimer: ReturnType<typeof setTimeout> | null = null;
    const resizeObserver = new ResizeObserver(() => {
      if (fitTimer) clearTimeout(fitTimer);
      fitTimer = setTimeout(() => {
        fitAddon.fit();
        if (
          wsRef.current?.readyState === WebSocket.OPEN &&
          terminalRef.current
        ) {
          const { cols, rows } = terminalRef.current;
          wsRef.current.send(JSON.stringify({ type: "resize", cols, rows }));
        }
      }, 150);
    });

    if (termRef.current) {
      resizeObserver.observe(termRef.current);
    }

    // Connect WebSocket
    connect();

    return () => {
      if (fitTimer) clearTimeout(fitTimer);
      resizeObserver.disconnect();
      wsRef.current?.close();
      terminal.dispose();
      terminalRef.current = null;
      fitAddonRef.current = null;
    };
  }, [connect]);

  const statusText = {
    connecting: "Connecting...",
    connected: "Connected",
    reconnecting: "Reconnecting...",
    disconnected: "Disconnected",
  };

  return (
    <div className={styles.terminalContainer}>
      <div className={styles.statusBar}>
        <span className={`${styles.statusDot} ${styles[connectionState]}`} />
        <span className={styles.statusText}>{statusText[connectionState]}</span>
      </div>
      <div ref={termRef} className={styles.terminal} />
      {wsError && (
        <div className={styles.errorOverlay}>
          <PracticeErrorCard
            error={wsError}
            onRetry={() => {
              setWsError(null);
              connect();
            }}
            onRestart={onRestart}
          />
        </div>
      )}
    </div>
  );
}
