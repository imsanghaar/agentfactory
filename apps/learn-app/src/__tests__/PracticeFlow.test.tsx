import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import React, { useState } from 'react';
import { PracticeContext } from '../contexts/PracticeContext';
import ExerciseCard from '../components/ExerciseCard/index';

function TestWrapper({ children }: { children: React.ReactNode }) {
  const [practiceOpen, setPracticeOpen] = useState(false);
  const [selectedExercise, setSelectedExercise] = useState<string | undefined>();

  const openPractice = (exerciseSubId?: string) => {
    setSelectedExercise(exerciseSubId);
    setPracticeOpen(true);
  };

  return (
    <PracticeContext.Provider value={{ practiceOpen, openPractice }}>
      {children}
      {practiceOpen && (
        <div data-testid="practice-overlay">Exercise: {selectedExercise}</div>
      )}
    </PracticeContext.Provider>
  );
}

describe('PracticeFlow', () => {
  it('ExerciseCard renders with title and badge', () => {
    render(
      <TestWrapper>
        <ExerciseCard id="1.1" title="First Task" />
      </TestWrapper>,
    );
    expect(screen.getByText('1.1')).toBeInTheDocument();
    expect(screen.getByText('First Task')).toBeInTheDocument();
  });

  it('ExerciseCard shows Start button when practice is not open', () => {
    render(
      <TestWrapper>
        <ExerciseCard id="1.1" title="First Task" />
      </TestWrapper>,
    );
    // The button contains an SVG + "Start" text, so use getByRole
    expect(screen.getByRole('button', { name: /Start/ })).toBeInTheDocument();
  });

  it('clicking Start opens practice overlay with exercise ID', () => {
    render(
      <TestWrapper>
        <ExerciseCard id="1.1" title="First Task" />
      </TestWrapper>,
    );

    fireEvent.click(screen.getByRole('button', { name: /Start/ }));

    expect(screen.getByTestId('practice-overlay')).toBeInTheDocument();
    expect(screen.getByTestId('practice-overlay').textContent).toContain('1.1');
  });

  it('Start button hidden after practice opens', () => {
    render(
      <TestWrapper>
        <ExerciseCard id="1.1" title="First Task" />
      </TestWrapper>,
    );

    fireEvent.click(screen.getByRole('button', { name: /Start/ }));

    // After practice opens, Start button should be hidden
    expect(screen.queryByRole('button', { name: /Start/ })).toBeNull();
  });

  it('ExerciseCard returns null without PracticeContext', () => {
    const { container } = render(
      <ExerciseCard id="1.1" title="First Task" />,
    );
    expect(container.innerHTML).toBe('');
  });

  it('multiple ExerciseCards work independently', () => {
    render(
      <TestWrapper>
        <ExerciseCard id="1.1" title="First Task" />
        <ExerciseCard id="1.2" title="Second Task" />
      </TestWrapper>,
    );

    expect(screen.getByText('First Task')).toBeInTheDocument();
    expect(screen.getByText('Second Task')).toBeInTheDocument();
    expect(screen.getAllByRole('button', { name: /Start/ })).toHaveLength(2);
  });
});
