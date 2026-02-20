export type ErrorCode =
  | "CLAUDE_NOT_FOUND"
  | "EXERCISE_NOT_FOUND"
  | "DOWNLOAD_FAILED"
  | "DOWNLOAD_TIMEOUT"
  | "EXTRACTION_FAILED"
  | "PTY_SPAWN_FAILED"
  | "PTY_EXITED"
  | "SESSION_NOT_FOUND"
  | "INVALID_REQUEST";

export interface AppError {
  code: ErrorCode;
  message: string;
  action?: string;
}

export class AppErrorInstance extends Error {
  public readonly code: ErrorCode;
  public readonly action?: string;

  constructor(code: ErrorCode, message: string, action?: string) {
    super(message);
    this.name = "AppError";
    this.code = code;
    this.action = action;
  }

  toJSON(): AppError {
    return {
      code: this.code,
      message: this.message,
      ...(this.action ? { action: this.action } : {}),
    };
  }
}

export function appError(
  code: ErrorCode,
  message: string,
  action?: string,
): AppErrorInstance {
  return new AppErrorInstance(code, message, action);
}

/** Map error codes to HTTP status codes */
export function httpStatus(code: ErrorCode): 400 | 404 | 500 {
  switch (code) {
    case "INVALID_REQUEST":
      return 400;
    case "EXERCISE_NOT_FOUND":
    case "SESSION_NOT_FOUND":
      return 404;
    case "CLAUDE_NOT_FOUND":
    case "DOWNLOAD_FAILED":
    case "DOWNLOAD_TIMEOUT":
    case "EXTRACTION_FAILED":
    case "PTY_SPAWN_FAILED":
    case "PTY_EXITED":
      return 500;
  }
}
