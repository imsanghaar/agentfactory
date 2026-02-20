import React, { useState, useCallback } from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Quiz, { QuizProps } from "@/components/quiz/Quiz";
import ContentGate from "@/components/ContentGate";
import QuizXPModal from "@/components/progress/QuizXPModal";
import { submitQuizScore } from "@/lib/progress-api";
import { useProgress } from "@/contexts/ProgressContext";
import type { QuizSubmitResponse } from "@/lib/progress-types";

interface GatedQuizProps extends QuizProps {
  /** Override the default gate title */
  gateTitle?: string;
  /** Override the default gate description */
  gateDescription?: string;
}

/**
 * GatedQuiz - A Quiz component wrapped with authentication gate
 *
 * Users must be signed in to access the quiz.
 * When not authenticated, shows a preview with sign-in prompt.
 * On completion, submits score to the progress API and shows XP modal.
 */
export function GatedQuiz({
  gateTitle,
  gateDescription,
  ...quizProps
}: GatedQuizProps) {
  const { siteConfig } = useDocusaurusContext();
  const progressApiUrl =
    (siteConfig.customFields?.progressApiUrl as string) ||
    "http://localhost:8002";

  const { progress, refreshProgress } = useProgress();
  const [quizResult, setQuizResult] = useState<{
    xpData: QuizSubmitResponse;
    scorePct: number;
  } | null>(null);

  const handleComplete = useCallback(
    async (result: {
      score_pct: number;
      questions_correct: number;
      questions_total: number;
    }) => {
      try {
        const pathSegments = window.location.pathname.split("/");
        const docsIndex = pathSegments.indexOf("docs");
        const chapterSlug =
          docsIndex >= 0
            ? pathSegments.slice(docsIndex + 1, -1).join("/")
            : window.location.pathname;

        const response = await submitQuizScore(progressApiUrl, {
          chapter_slug: chapterSlug,
          score_pct: result.score_pct,
          questions_correct: result.questions_correct,
          questions_total: result.questions_total,
        });
        setQuizResult({ xpData: response, scorePct: result.score_pct });
        refreshProgress();
      } catch (err) {
        console.error("[GatedQuiz] Failed to submit quiz score:", err);
      }
    },
    [progressApiUrl, refreshProgress],
  );

  return (
    <>
      <ContentGate type="quiz" title={gateTitle} description={gateDescription}>
        <Quiz {...quizProps} onComplete={handleComplete} />
      </ContentGate>
      {quizResult && (
        <QuizXPModal
          isOpen={true}
          onClose={() => setQuizResult(null)}
          scorePercentage={quizResult.scorePct}
          xpEarned={quizResult.xpData.xp_earned}
          totalXp={quizResult.xpData.total_xp}
          newBadges={quizResult.xpData.new_badges}
          attemptNumber={quizResult.xpData.attempt_number}
          rank={progress?.stats?.rank}
        />
      )}
    </>
  );
}

export default GatedQuiz;
