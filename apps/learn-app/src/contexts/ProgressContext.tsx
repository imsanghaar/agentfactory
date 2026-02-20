import React, {
  createContext,
  useContext,
  useState,
  useEffect,
  useCallback,
  ReactNode,
} from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useAuth } from "./AuthContext";
import { getProgress } from "@/lib/progress-api";
import type { ProgressResponse } from "@/lib/progress-types";

interface ProgressContextType {
  progress: ProgressResponse | null;
  isLoading: boolean;
  refreshProgress: () => Promise<void>;
  /** Check if a specific lesson is already completed */
  isLessonCompleted: (chapterSlug: string, lessonSlug: string) => boolean;
}

const ProgressContext = createContext<ProgressContextType | undefined>(
  undefined,
);

export function ProgressProvider({ children }: { children: ReactNode }) {
  const { session } = useAuth();
  const { siteConfig } = useDocusaurusContext();
  const progressApiUrl =
    (siteConfig.customFields?.progressApiUrl as string) ||
    "http://localhost:8002";

  const [progress, setProgress] = useState<ProgressResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const refreshProgress = useCallback(async () => {
    if (!session?.user) return;
    setIsLoading(true);
    try {
      const data = await getProgress(progressApiUrl);
      setProgress(data);
    } catch (err) {
      console.error("[ProgressContext] Failed to load progress:", err);
    } finally {
      setIsLoading(false);
    }
  }, [session, progressApiUrl]);

  // Load on auth
  useEffect(() => {
    if (session?.user) {
      refreshProgress();
    } else {
      setProgress(null);
    }
  }, [session?.user?.id, refreshProgress]);

  const isLessonCompleted = useCallback(
    (chapterSlug: string, lessonSlug: string): boolean => {
      if (!progress) return false;
      const chapter = progress.chapters.find((c) => c.slug === chapterSlug);
      if (!chapter) return false;
      return chapter.lessons_completed.some(
        (l) => l.lesson_slug === lessonSlug,
      );
    },
    [progress],
  );

  return (
    <ProgressContext.Provider
      value={{ progress, isLoading, refreshProgress, isLessonCompleted }}
    >
      {children}
    </ProgressContext.Provider>
  );
}

export function useProgress() {
  const context = useContext(ProgressContext);
  if (context === undefined) {
    throw new Error("useProgress must be used within a ProgressProvider");
  }
  return context;
}
