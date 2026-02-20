import React from "react";
import type { AppError } from "@/types/practice";

interface PracticeErrorCardProps {
  error: AppError;
  onRetry?: () => void;
  onRestart?: () => void;
}

const RETRYABLE_CODES = new Set([
  "DOWNLOAD_FAILED",
  "DOWNLOAD_TIMEOUT",
  "EXTRACTION_FAILED",
]);

/** Extra guidance per error code */
const ERROR_GUIDANCE: Record<string, string> = {
  CLAUDE_NOT_FOUND:
    "Install Claude Code: https://docs.anthropic.com/en/docs/claude-code/overview",
  PTY_SPAWN_FAILED:
    "Check that Claude Code runs in your terminal (`claude --version`) and that you have proper permissions.",
};

export function PracticeErrorCard({
  error,
  onRetry,
  onRestart,
}: PracticeErrorCardProps) {
  const isRetryable = RETRYABLE_CODES.has(error.code);
  const isPtyExited = error.code === "PTY_EXITED";
  const guidance = ERROR_GUIDANCE[error.code];

  return (
    <div className="practice-error-card">
      <div className="practice-error-icon">!</div>
      <div className="practice-error-content">
        <p className="practice-error-message">{error.message}</p>
        {error.action && (
          <p className="practice-error-action">{error.action}</p>
        )}
        {guidance && <p className="practice-error-guidance">{guidance}</p>}
      </div>
      <div className="practice-error-actions">
        {isRetryable && onRetry && (
          <button
            onClick={onRetry}
            className="practice-error-btn practice-error-btn-retry"
          >
            Try Again
          </button>
        )}
        {isPtyExited && onRestart && (
          <button
            onClick={onRestart}
            className="practice-error-btn practice-error-btn-restart"
          >
            Restart
          </button>
        )}
      </div>
    </div>
  );
}
