/**
 * ModeToggle Component
 *
 * Toggle between Teach and Ask modes
 */

import React from 'react';
import type { ChatMode } from '../../contexts/StudyModeContext';
import styles from './styles.module.css';

interface ModeToggleProps {
  mode: ChatMode;
  onModeChange: (mode: ChatMode) => void;
}

export function ModeToggle({ mode, onModeChange }: ModeToggleProps) {
  return (
    <div className={styles.modeToggle} role="tablist" aria-label="Chat mode">
      <button
        role="tab"
        aria-selected={mode === 'teach'}
        className={`${styles.modeButton} ${mode === 'teach' ? styles.modeButtonActive : ''}`}
        onClick={() => onModeChange('teach')}
      >
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" />
          <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" />
        </svg>
        Teach
      </button>
      <button
        role="tab"
        aria-selected={mode === 'ask'}
        className={`${styles.modeButton} ${mode === 'ask' ? styles.modeButtonActive : ''}`}
        onClick={() => onModeChange('ask')}
      >
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
          <circle cx="12" cy="12" r="10" />
          <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" />
          <line x1="12" y1="17" x2="12.01" y2="17" />
        </svg>
        Ask
      </button>
    </div>
  );
}
