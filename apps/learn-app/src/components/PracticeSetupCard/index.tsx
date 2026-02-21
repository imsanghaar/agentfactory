import React, { useState } from "react";

interface PracticeSetupCardProps {
  onRetry?: () => void;
}

export function PracticeSetupCard({ onRetry }: PracticeSetupCardProps) {
  const [copied, setCopied] = useState(false);
  const [showClaudeInfo, setShowClaudeInfo] = useState(false);
  const command = "npx af-practice";

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(command);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch {
      // Clipboard API not available
    }
  };

  return (
    <div className="practice-setup-card">
      <h3>
        Start Practice Server{" "}
        <span className="practice-terminal-beta">Beta</span>
      </h3>
      <p>Run this command to start the practice server:</p>
      <code className="practice-setup-cmd" onClick={handleCopy}>
        {command}
        <span className="practice-setup-copy">
          {copied ? "Copied!" : "Click to copy"}
        </span>
      </code>
      <div className="practice-setup-waiting">
        <span className="practice-setup-dot" />
        Waiting for server...
      </div>
      <button
        className="practice-setup-expand"
        onClick={() => setShowClaudeInfo(!showClaudeInfo)}
      >
        {showClaudeInfo ? "Hide" : "Don't have Qwen CLI?"}
      </button>
      {showClaudeInfo && (
        <div className="practice-setup-info">
          <p>
            Qwen CLI is required for practice exercises. Install it with:{" "}
            <code>npm install -g @qwen-code/qwen-code@latest</code>
          </p>
          <p>
            Learn more at:{" "}
            <a
              href="https://github.com/QwenLM/qwen-code"
              target="_blank"
              rel="noopener noreferrer"
            >
              github.com/QwenLM/qwen-code
            </a>
          </p>
        </div>
      )}
      {onRetry && (
        <button onClick={onRetry} className="practice-setup-retry">
          Retry
        </button>
      )}
    </div>
  );
}
