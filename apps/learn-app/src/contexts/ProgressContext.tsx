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
    if (!session?.user) {
      console.log("[ProgressContext] No session, skipping refresh");
      return;
    }
    console.log("[ProgressContext] Refreshing progress...");
    setIsLoading(true);
    try {
      const data = await getProgress(progressApiUrl);
      console.log("[ProgressContext] Progress loaded:", {
        totalXp: data.stats?.total_xp,
        rank: data.stats?.rank,
        badgeCount: data.stats?.badge_count,
      });
      setProgress((prev) => {
        // Force re-render even if data is same by always creating new reference
        return { ...data };
      });
    } catch (err) {
      console.error("[ProgressContext] Failed to load progress:", err);
    } finally {
      setIsLoading(false);
    }
  }, [session?.user?.id, progressApiUrl]);

  // Load on auth change
  useEffect(() => {
    if (session?.user) {
      console.log("[ProgressContext] User logged in, loading progress...");
      refreshProgress();
    } else {
      console.log("[ProgressContext] User logged out, clearing progress");
      setProgress(null);
    }
  }, [session?.user?.id]);

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
