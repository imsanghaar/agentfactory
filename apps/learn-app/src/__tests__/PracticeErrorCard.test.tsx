import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import React from 'react';
import { PracticeErrorCard } from '../components/PracticeErrorCard/index';

describe('PracticeErrorCard', () => {
  it('renders error message', () => {
    render(
      <PracticeErrorCard error={{ code: 'CLAUDE_NOT_FOUND', message: 'Claude Code not found' }} />,
    );
    expect(screen.getByText('Claude Code not found')).toBeInTheDocument();
  });

  it('renders action text when provided', () => {
    render(
      <PracticeErrorCard
        error={{ code: 'DOWNLOAD_FAILED', message: 'Download failed', action: 'Try again later' }}
      />,
    );
    expect(screen.getByText('Try again later')).toBeInTheDocument();
  });

  it('does not render action when not provided', () => {
    const { container } = render(
      <PracticeErrorCard error={{ code: 'EXERCISE_NOT_FOUND', message: 'Not available' }} />,
    );
    expect(container.querySelector('.practice-error-action')).toBeNull();
  });

  it('shows Try Again button for DOWNLOAD_FAILED', () => {
    const onRetry = vi.fn();
    render(
      <PracticeErrorCard
        error={{ code: 'DOWNLOAD_FAILED', message: 'Failed' }}
        onRetry={onRetry}
      />,
    );
    const btn = screen.getByText('Try Again');
    fireEvent.click(btn);
    expect(onRetry).toHaveBeenCalledOnce();
  });

  it('shows Try Again button for DOWNLOAD_TIMEOUT', () => {
    const onRetry = vi.fn();
    render(
      <PracticeErrorCard
        error={{ code: 'DOWNLOAD_TIMEOUT', message: 'Timed out' }}
        onRetry={onRetry}
      />,
    );
    expect(screen.getByText('Try Again')).toBeInTheDocument();
  });

  it('shows Restart button for PTY_EXITED', () => {
    const onRestart = vi.fn();
    render(
      <PracticeErrorCard
        error={{ code: 'PTY_EXITED', message: 'Claude Code exited' }}
        onRestart={onRestart}
      />,
    );
    const btn = screen.getByText('Restart');
    fireEvent.click(btn);
    expect(onRestart).toHaveBeenCalledOnce();
  });

  it('does not show Try Again for non-retryable errors', () => {
    render(
      <PracticeErrorCard
        error={{ code: 'CLAUDE_NOT_FOUND', message: 'Not found' }}
        onRetry={vi.fn()}
      />,
    );
    expect(screen.queryByText('Try Again')).toBeNull();
  });

  it('does not show Restart for non-PTY_EXITED errors', () => {
    render(
      <PracticeErrorCard
        error={{ code: 'DOWNLOAD_FAILED', message: 'Failed' }}
        onRestart={vi.fn()}
      />,
    );
    expect(screen.queryByText('Restart')).toBeNull();
  });

  it('renders error icon', () => {
    const { container } = render(
      <PracticeErrorCard error={{ code: 'INVALID_REQUEST', message: 'Bad request' }} />,
    );
    expect(container.querySelector('.practice-error-icon')).toBeInTheDocument();
  });
});
