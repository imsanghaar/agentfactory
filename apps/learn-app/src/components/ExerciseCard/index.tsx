import React from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { usePractice } from "@/contexts/PracticeContext";

interface ExerciseCardProps {
  id: string;
  title: string;
}

export default function ExerciseCard({ id, title }: ExerciseCardProps) {
  const { siteConfig } = useDocusaurusContext();
  const practiceEnabled = siteConfig.customFields?.practiceEnabled as
    | boolean
    | undefined;
  const practice = usePractice();

  if (!practiceEnabled || !practice) return null;

  return (
    <div className="exercise-card" id={`exercise-${id}`}>
      <div className="exercise-card-left">
        <span className="exercise-card-badge">{id}</span>
        <span className="exercise-card-title">{title}</span>
      </div>
      {!practice.practiceOpen && (
        <button
          className="exercise-card-start"
          onClick={() => {
            practice.openPractice(id);
            setTimeout(() => {
              document
                .getElementById(`exercise-${id}`)
                ?.scrollIntoView({ behavior: "smooth", block: "start" });
            }, 100);
          }}
          title="Open practice terminal"
        >
          <svg
            width="14"
            height="14"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.5"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <polygon points="5 3 19 12 5 21 5 3" />
          </svg>
          Start
        </button>
      )}
    </div>
  );
}
