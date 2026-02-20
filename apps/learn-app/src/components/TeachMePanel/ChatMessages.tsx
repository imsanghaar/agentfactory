/**
 * ChatMessages Component
 *
 * Displays the conversation history with user and assistant messages
 * Includes auto-scroll and loading indicator
 */

import React, { useEffect, useRef } from 'react';
import type { Message } from '../../contexts/StudyModeContext';
import styles from './styles.module.css';

interface ChatMessagesProps {
  messages: Message[];
  isLoading: boolean;
}

export function ChatMessages({ messages, isLoading }: ChatMessagesProps) {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isLoading]);

  if (messages.length === 0 && !isLoading) {
    return (
      <div className={styles.emptyState}>
        <div className={styles.emptyIcon}>
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
          </svg>
        </div>
        <h3 className={styles.emptyTitle}>Start Learning</h3>
        <p className={styles.emptyText}>
          Ask a question about this lesson or say &quot;teach me&quot; to get started.
        </p>
      </div>
    );
  }

  return (
    <div className={styles.messagesContainer}>
      {messages.map((message, index) => (
        <div
          key={`${message.timestamp}-${index}`}
          className={`${styles.message} ${
            message.role === 'user' ? styles.userMessage : styles.assistantMessage
          }`}
        >
          <div className={styles.messageAvatar}>
            {message.role === 'user' ? (
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                <circle cx="12" cy="7" r="4" />
              </svg>
            ) : (
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                <path d="M12 2a10 10 0 1 0 10 10H12V2z" />
                <path d="M12 2a10 10 0 0 1 10 10" />
                <circle cx="12" cy="12" r="3" />
              </svg>
            )}
          </div>
          <div className={styles.messageContent}>
            <span className={styles.messageRole}>
              {message.role === 'user' ? 'You' : 'AI Tutor'}
            </span>
            <div className={styles.messageText}>
              {message.content}
            </div>
          </div>
        </div>
      ))}

      {isLoading && (
        <div className={`${styles.message} ${styles.assistantMessage}`}>
          <div className={styles.messageAvatar}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M12 2a10 10 0 1 0 10 10H12V2z" />
              <path d="M12 2a10 10 0 0 1 10 10" />
              <circle cx="12" cy="12" r="3" />
            </svg>
          </div>
          <div className={styles.messageContent}>
            <span className={styles.messageRole}>AI Tutor</span>
            <div className={styles.typingIndicator}>
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        </div>
      )}

      <div ref={messagesEndRef} />
    </div>
  );
}
