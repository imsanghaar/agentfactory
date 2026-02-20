import { describe, it, expect } from 'vitest';
import { AppErrorInstance, appError, httpStatus } from '../../errors.js';
import type { ErrorCode, AppError } from '../../errors.js';

describe('AppErrorInstance', () => {
  it('extends Error', () => {
    const err = new AppErrorInstance('CLAUDE_NOT_FOUND', 'not found');
    expect(err).toBeInstanceOf(Error);
  });

  it('sets name to AppError', () => {
    const err = new AppErrorInstance('CLAUDE_NOT_FOUND', 'not found');
    expect(err.name).toBe('AppError');
  });

  it('stores code, message, and action', () => {
    const err = new AppErrorInstance('DOWNLOAD_FAILED', 'bad download', 'Try again');
    expect(err.code).toBe('DOWNLOAD_FAILED');
    expect(err.message).toBe('bad download');
    expect(err.action).toBe('Try again');
  });

  it('action is optional', () => {
    const err = new AppErrorInstance('PTY_EXITED', 'process ended');
    expect(err.action).toBeUndefined();
  });

  describe('toJSON', () => {
    it('returns structured AppError with action', () => {
      const err = new AppErrorInstance('EXTRACTION_FAILED', 'corrupt zip', 'Retry');
      const json: AppError = err.toJSON();
      expect(json).toEqual({
        code: 'EXTRACTION_FAILED',
        message: 'corrupt zip',
        action: 'Retry',
      });
    });

    it('omits action when not provided', () => {
      const err = new AppErrorInstance('SESSION_NOT_FOUND', 'no session');
      const json = err.toJSON();
      expect(json).toEqual({
        code: 'SESSION_NOT_FOUND',
        message: 'no session',
      });
      expect('action' in json).toBe(false);
    });

    it('is JSON-serializable', () => {
      const err = new AppErrorInstance('INVALID_REQUEST', 'bad input', 'Fix request');
      const serialized = JSON.stringify({ error: err.toJSON() });
      const parsed = JSON.parse(serialized);
      expect(parsed.error.code).toBe('INVALID_REQUEST');
      expect(parsed.error.message).toBe('bad input');
      expect(parsed.error.action).toBe('Fix request');
    });
  });
});

describe('appError helper', () => {
  it('creates AppErrorInstance', () => {
    const err = appError('PTY_SPAWN_FAILED', 'spawn failed');
    expect(err).toBeInstanceOf(AppErrorInstance);
    expect(err.code).toBe('PTY_SPAWN_FAILED');
  });

  it('passes action through', () => {
    const err = appError('DOWNLOAD_TIMEOUT', 'timed out', 'Check internet');
    expect(err.action).toBe('Check internet');
  });
});

describe('httpStatus', () => {
  it('returns 400 for INVALID_REQUEST', () => {
    expect(httpStatus('INVALID_REQUEST')).toBe(400);
  });

  it('returns 404 for not-found errors', () => {
    expect(httpStatus('EXERCISE_NOT_FOUND')).toBe(404);
    expect(httpStatus('SESSION_NOT_FOUND')).toBe(404);
  });

  it('returns 500 for server errors', () => {
    const serverErrors: ErrorCode[] = [
      'CLAUDE_NOT_FOUND',
      'DOWNLOAD_FAILED',
      'DOWNLOAD_TIMEOUT',
      'EXTRACTION_FAILED',
      'PTY_SPAWN_FAILED',
      'PTY_EXITED',
    ];
    for (const code of serverErrors) {
      expect(httpStatus(code), `${code} should be 500`).toBe(500);
    }
  });

  it('covers all error codes', () => {
    const allCodes: ErrorCode[] = [
      'CLAUDE_NOT_FOUND',
      'EXERCISE_NOT_FOUND',
      'DOWNLOAD_FAILED',
      'DOWNLOAD_TIMEOUT',
      'EXTRACTION_FAILED',
      'PTY_SPAWN_FAILED',
      'PTY_EXITED',
      'SESSION_NOT_FOUND',
      'INVALID_REQUEST',
    ];
    for (const code of allCodes) {
      const status = httpStatus(code);
      expect(status, `httpStatus('${code}') should return a number`).toBeGreaterThanOrEqual(400);
      expect(status).toBeLessThan(600);
    }
  });
});
