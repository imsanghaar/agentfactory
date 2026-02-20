import React from "react";
import Link from "@docusaurus/Link";
import { useAuth } from "@/contexts/AuthContext";
import { useProgress } from "@/contexts/ProgressContext";
import { BadgeGrid } from "@/components/progress/BadgeCard";
import "@/components/progress/gamification.css";
import styles from "./ProgressDashboard.module.css";

export default function ProgressDashboard() {
  const { session } = useAuth();
  const { progress, isLoading } = useProgress();

  if (!session?.user) {
    return (
      <div className={styles.container}>
        <p className={styles.loginPrompt}>
          Sign in to view your learning progress.
        </p>
      </div>
    );
  }

  if (isLoading && !progress) {
    return (
      <div className={styles.container}>
        <p className={styles.loginPrompt}>Loading your progress...</p>
      </div>
    );
  }

  const stats = progress?.stats;

  return (
    <div className={styles.container}>
      <h1 className={styles.heading}>My Progress</h1>

      {/* Stat cards */}
      <div className={styles.stats}>
        <div className={`${styles.statCard} gf-stat-xp`}>
          <span className={`${styles.statValue} ${styles.xpValue}`}>
            {stats?.total_xp ?? 0}
          </span>
          <span className={styles.statLabel}>Total XP</span>
        </div>
        <Link
          to="/leaderboard"
          className={`${styles.statCard} ${styles.statCardClickable} gf-stat-rank no-underline`}
        >
          <span className={`${styles.statValue} ${styles.rankValue}`}>
            {stats?.rank ? `#${stats.rank}` : "--"}
          </span>
          <span className={styles.statLabel}>Rank</span>
        </Link>
        <div className={`${styles.statCard} gf-stat-streak`}>
          <span className={`${styles.statValue} ${styles.streakValue}`}>
            {stats?.current_streak ?? 0}
          </span>
          <span className={styles.statLabel}>Current Streak</span>
        </div>
        <div className={`${styles.statCard} gf-stat-perfect`}>
          <span className={`${styles.statValue} ${styles.perfectValue}`}>
            {stats?.perfect_scores ?? 0}
          </span>
          <span className={styles.statLabel}>Perfect Scores</span>
        </div>
      </div>

      {/* Badge gallery — uses BadgeGrid from BadgeCard.tsx */}
      <div className={styles.section}>
        <h2 className={styles.sectionTitle}>Badges</h2>
        <BadgeGrid
          earnedBadges={progress?.badges ?? []}
          showLocked
          size="md"
          columns={4}
        />
      </div>

      {/* Chapter progress */}
      <div className={styles.section}>
        <h2 className={styles.sectionTitle}>Chapter Progress</h2>
        {(progress?.chapters?.length ?? 0) === 0 ? (
          <p className={styles.empty}>
            No chapter activity yet. Take a quiz to get started!
          </p>
        ) : (
          <div className={styles.chapterList}>
            {progress!.chapters.map((ch) => (
              <div key={ch.slug} className={styles.chapterCard}>
                <div className={styles.chapterInfo}>
                  <div className={styles.chapterTitle}>
                    {ch.title || ch.slug}
                  </div>
                  <div className={styles.chapterMeta}>
                    <span>
                      Best: {ch.best_score != null ? `${ch.best_score}%` : "—"}
                    </span>
                    <span>{ch.xp_earned} XP</span>
                    <span>
                      {ch.attempts} attempt{ch.attempts !== 1 ? "s" : ""}
                    </span>
                    <span>
                      {ch.lessons_completed.length} lesson
                      {ch.lessons_completed.length !== 1 ? "s" : ""}
                    </span>
                  </div>
                </div>
                <div className={styles.progressBar}>
                  <div
                    className={styles.progressFill}
                    style={{ width: `${Math.min(ch.best_score ?? 0, 100)}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
