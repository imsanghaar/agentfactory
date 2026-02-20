import React, { useState, useCallback, useRef } from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useProgress } from "@/contexts/ProgressContext";
import { completeLesson } from "@/lib/progress-api";
import styles from "./LessonCompleteButton.module.css";

interface LessonCompleteButtonProps {
  chapterSlug: string;
  lessonSlug: string;
}

/**
 * Track active reading time silently via ref (no re-renders).
 * Pauses when tab is hidden, resumes when visible.
 */
function useActiveTime() {
  const secondsRef = useRef(0);
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const start = useCallback(() => {
    if (intervalRef.current) return;
    intervalRef.current = setInterval(() => {
      secondsRef.current += 1;
    }, 1000);
  }, []);

  const pause = useCallback(() => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
      intervalRef.current = null;
    }
  }, []);

  // Start/pause on visibility change
  React.useEffect(() => {
    const handler = () => {
      document.visibilityState === "hidden" ? pause() : start();
    };
    if (document.visibilityState === "visible") start();
    document.addEventListener("visibilitychange", handler);
    return () => {
      pause();
      document.removeEventListener("visibilitychange", handler);
    };
  }, [start, pause]);

  return secondsRef;
}

function formatReadingTime(secs: number): string {
  if (secs < 60) return "less than a minute";
  const m = Math.round(secs / 60);
  return `${m} minute${m !== 1 ? "s" : ""}`;
}

type ButtonState = "idle" | "submitting" | "done" | "error";

export default function LessonCompleteButton({
  chapterSlug,
  lessonSlug,
}: LessonCompleteButtonProps) {
  const { siteConfig } = useDocusaurusContext();
  const progressApiUrl =
    (siteConfig.customFields?.progressApiUrl as string) ||
    "http://localhost:8002";

  const { isLessonCompleted, refreshProgress } = useProgress();
  const alreadyCompleted = isLessonCompleted(chapterSlug, lessonSlug);

  const activeTimeRef = useActiveTime();
  const [state, setState] = useState<ButtonState>("idle");
  const [readingTime, setReadingTime] = useState("");
  const [xpEarned, setXpEarned] = useState(0);

  // Derive effective state: server says done overrides local state
  const effectiveState = alreadyCompleted ? "done" : state;

  const handleComplete = useCallback(async () => {
    if (effectiveState !== "idle") return;
    setState("submitting");
    try {
      const secs = activeTimeRef.current;
      const response = await completeLesson(progressApiUrl, {
        chapter_slug: chapterSlug,
        lesson_slug: lessonSlug,
        active_duration_secs: secs,
      });
      setReadingTime(formatReadingTime(secs));
      setXpEarned(response.xp_earned);
      setState("done");
      refreshProgress();
    } catch (err) {
      console.error("[LessonComplete] Failed:", err);
      setState("error");
    }
  }, [
    effectiveState,
    progressApiUrl,
    chapterSlug,
    lessonSlug,
    activeTimeRef,
    refreshProgress,
  ]);

  const handleRetry = useCallback(() => {
    setState("idle");
  }, []);

  return (
    <div className={styles.wrapper}>
      <div className={styles.divider} />

      {effectiveState === "done" ? (
        <div className={styles.doneRow}>
          <svg
            className={styles.checkIcon}
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2.5"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path d="M20 6 9 17l-5-5" />
          </svg>
          <span className={styles.doneText}>
            Lesson complete{readingTime ? ` — ${readingTime} of reading` : ""}
            {xpEarned > 0 && <span className={styles.xpBadge}>+{xpEarned} XP</span>}
          </span>
        </div>
      ) : effectiveState === "error" ? (
        <div className={styles.errorRow}>
          <span className={styles.errorText}>
            Could not save — check your connection
          </span>
          <button className={styles.retryButton} onClick={handleRetry}>
            Try again
          </button>
        </div>
      ) : (
        <button
          className={styles.button}
          onClick={handleComplete}
          disabled={effectiveState === "submitting"}
        >
          {effectiveState === "submitting" ? (
            <>
              <span className={styles.spinner} />
              Saving...
            </>
          ) : (
            <>
              <svg
                className={styles.icon}
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <path d="M20 6 9 17l-5-5" />
              </svg>
              Mark as complete
            </>
          )}
        </button>
      )}
    </div>
  );
}
