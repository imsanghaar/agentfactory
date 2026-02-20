import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { render, screen, waitFor } from '@testing-library/react';
import React from 'react';
import { TerminalPanel } from '../components/TerminalPanel/index';

// Ensure real timers — usePracticeServer.test.ts uses fake timers which can
// leak when vitest runs files in the same thread.
beforeEach(() => {
  vi.useRealTimers();
});

afterEach(() => {
  vi.restoreAllMocks();
});

describe('TerminalPanel', () => {
  it('renders terminal container and status bar', () => {
    const { container } = render(
      <TerminalPanel wsUrl="ws://localhost:3100/sessions/test/ws" />,
    );
    expect(container.querySelector('.terminalContainer')).toBeInTheDocument();
    expect(container.querySelector('.statusBar')).toBeInTheDocument();
  });

  it('shows connecting state initially', () => {
    render(
      <TerminalPanel wsUrl="ws://localhost:3100/sessions/test/ws" />,
    );
    expect(screen.getByText('Connecting...')).toBeInTheDocument();
  });

  it('transitions to connected state after WS opens', async () => {
    render(
      <TerminalPanel wsUrl="ws://localhost:3100/sessions/test/ws" />,
    );

    await waitFor(() => {
      expect(screen.getByText('Connected')).toBeInTheDocument();
    });
  });

  it('calls onWsConnected when WS opens', async () => {
    const onWsConnected = vi.fn();
    render(
      <TerminalPanel
        wsUrl="ws://localhost:3100/sessions/test/ws"
        onWsConnected={onWsConnected}
      />,
    );

    await waitFor(() => {
      expect(onWsConnected).toHaveBeenCalledOnce();
    });
  });

  it('verifies onWsDisconnected is not called while connected', async () => {
    const onWsDisconnected = vi.fn();
    render(
      <TerminalPanel
        wsUrl="ws://localhost:3100/sessions/test/ws"
        onWsDisconnected={onWsDisconnected}
      />,
    );

    await waitFor(() => {
      expect(screen.getByText('Connected')).toBeInTheDocument();
    });

    // While connected, onWsDisconnected should not have been called
    expect(onWsDisconnected).not.toHaveBeenCalled();
  });

  it('renders terminal div for xterm', () => {
    const { container } = render(
      <TerminalPanel wsUrl="ws://localhost:3100/sessions/test/ws" />,
    );
    expect(container.querySelector('.terminal')).toBeInTheDocument();
  });

  it('shows status dot with connecting class initially', () => {
    const { container } = render(
      <TerminalPanel wsUrl="ws://localhost:3100/sessions/test/ws" />,
    );

    const dot = container.querySelector('.statusDot');
    expect(dot).toBeInTheDocument();
    expect(dot?.classList.contains('connecting')).toBe(true);
  });

  it('shows status dot with connected class after WS opens', async () => {
    const { container } = render(
      <TerminalPanel wsUrl="ws://localhost:3100/sessions/test/ws" />,
    );

    await waitFor(() => {
      const dot = container.querySelector('.statusDot');
      expect(dot?.classList.contains('connected')).toBe(true);
    });
  });

  it('does not show error overlay when no error', () => {
    const { container } = render(
      <TerminalPanel wsUrl="ws://localhost:3100/sessions/test/ws" />,
    );
    expect(container.querySelector('.errorOverlay')).toBeNull();
  });
});
