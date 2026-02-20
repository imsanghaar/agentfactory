import { describe, it, expect, vi } from 'vitest';
import { Terminal } from '@xterm/xterm';
import { FitAddon } from '@xterm/addon-fit';

describe('xterm mock', () => {
  it('creates Terminal instance without canvas', () => {
    const term = new Terminal();
    expect(term).toBeDefined();
    expect(term.open).toBeDefined();
    expect(term.write).toBeDefined();
    expect(term.dispose).toBeDefined();
  });

  it('Terminal.open does not throw', () => {
    const term = new Terminal();
    expect(() => term.open(document.createElement('div'))).not.toThrow();
  });

  it('Terminal.onData returns disposable', () => {
    const term = new Terminal();
    const disposable = term.onData(() => {});
    expect(disposable.dispose).toBeDefined();
  });
});

describe('FitAddon mock', () => {
  it('creates FitAddon instance', () => {
    const addon = new FitAddon();
    expect(addon.fit).toBeDefined();
    expect(addon.dispose).toBeDefined();
    expect(addon.proposeDimensions).toBeDefined();
  });

  it('proposeDimensions returns cols and rows', () => {
    const addon = new FitAddon();
    const dims = addon.proposeDimensions();
    expect(dims).toEqual({ cols: 80, rows: 24 });
  });
});

describe('WebSocket mock', () => {
  it('has static constants', () => {
    expect(WebSocket.CONNECTING).toBe(0);
    expect(WebSocket.OPEN).toBe(1);
    expect(WebSocket.CLOSING).toBe(2);
    expect(WebSocket.CLOSED).toBe(3);
  });
});

describe('clipboard mock', () => {
  it('writeText resolves', async () => {
    await expect(navigator.clipboard.writeText('test')).resolves.toBeUndefined();
  });
});
