import { describe, it, expect } from 'vitest';

describe('vitest setup', () => {
  it('runs in jsdom environment', () => {
    expect(document).toBeDefined();
    expect(window).toBeDefined();
  });

  it('has WebSocket mock available', () => {
    expect(WebSocket).toBeDefined();
  });

  it('has clipboard mock available', () => {
    expect(navigator.clipboard).toBeDefined();
    expect(navigator.clipboard.writeText).toBeDefined();
  });
});
