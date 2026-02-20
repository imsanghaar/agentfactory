import React, { useEffect, useState, useCallback } from "react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Link from "@docusaurus/Link";
import { useAuth } from "@/contexts/AuthContext";
import { getOAuthAuthorizationUrl } from "@/lib/auth-client";
import { getLeaderboard } from "@/lib/progress-api";
import type {
  LeaderboardEntry,
  LeaderboardResponse,
} from "@/lib/progress-types";
import { cn } from "@/lib/utils";
import { Card, CardContent } from "@/components/ui/card";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog";
import { BadgeCard } from "@/components/progress/BadgeCard";
import {
  Zap,
  Trophy,
  Medal,
  Crown,
  Award,
  Lock,
  LogIn,
  Loader2,
} from "lucide-react";
import "@/components/progress/gamification.css";
import styles from "./Leaderboard.module.css";

/* ───────────────────── Helpers ───────────────────── */

function getInitials(name: string): string {
  return name
    .split(" ")
    .map((w) => w[0])
    .join("")
    .slice(0, 2)
    .toUpperCase();
}

function ordinal(n: number): string {
  const s = ["th", "st", "nd", "rd"];
  const v = n % 100;
  return n + (s[(v - 20) % 10] || s[v] || s[0]);
}

/* ───────────────────── Badge Modal ───────────────────── */

interface BadgeModalProps {
  isOpen: boolean;
  onClose: () => void;
  displayName: string;
  badgeIds: string[];
}

function BadgeModal({
  isOpen,
  onClose,
  displayName,
  badgeIds,
}: BadgeModalProps) {
  return (
    <Dialog open={isOpen} onOpenChange={onClose} modal={false}>
      {/* Custom overlay since modal={false} disables the built-in one
          (modal={false} prevents the scrollbar-removal layout shift) */}
      {isOpen && (
        <div
          className="fixed inset-0 z-50 bg-background/60 backdrop-blur-md animate-in fade-in-0"
          onClick={onClose}
          aria-hidden="true"
        />
      )}
      <DialogContent className="allow-rounded max-w-md sm:max-w-lg max-h-[80vh] overflow-y-auto rounded-xl">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2">
            <Award className="w-5 h-5 text-primary" />
            {displayName}&apos;s Badges
          </DialogTitle>
          <DialogDescription>
            {badgeIds.length} badge{badgeIds.length !== 1 ? "s" : ""} earned
          </DialogDescription>
        </DialogHeader>

        <div className="grid grid-cols-2 sm:grid-cols-3 gap-3 mt-4">
          {badgeIds.map((id) => (
            <BadgeCard
              key={id}
              badgeId={id}
              isEarned={true}
              size="md"
              showDescription={true}
            />
          ))}
        </div>

        {badgeIds.length === 0 && (
          <div className="flex flex-col items-center py-8 text-muted-foreground">
            <Award className="w-12 h-12 mb-2 opacity-50" />
            <p>No badges earned yet</p>
          </div>
        )}
      </DialogContent>
    </Dialog>
  );
}

/* ───────────────────── Rank Badge ───────────────────── */

function RankBadge({ rank }: { rank: number }) {
  if (rank === 1) {
    return (
      <div className="allow-rounded w-7 h-7 sm:w-8 sm:h-8 flex items-center justify-center rank-badge-gold text-white font-bold text-sm rounded-full shrink-0">
        <Crown className="w-4 h-4 sm:w-5 sm:h-5" fill="currentColor" />
      </div>
    );
  }
  if (rank === 2) {
    return (
      <div className="allow-rounded w-7 h-7 sm:w-8 sm:h-8 flex items-center justify-center rank-badge-silver text-white font-bold text-sm rounded-full shrink-0">
        <Medal className="w-4 h-4 sm:w-5 sm:h-5" />
      </div>
    );
  }
  if (rank === 3) {
    return (
      <div className="allow-rounded w-7 h-7 sm:w-8 sm:h-8 flex items-center justify-center rank-badge-bronze text-white font-bold text-sm rounded-full shrink-0">
        <Medal className="w-4 h-4 sm:w-5 sm:h-5" />
      </div>
    );
  }
  return (
    <div className="w-7 h-7 sm:w-8 sm:h-8 flex items-center justify-center font-semibold text-muted-foreground text-xs sm:text-sm shrink-0">
      #{rank}
    </div>
  );
}

/* ───────────────────── Badge Button ───────────────────── */

function BadgeButton({
  entry,
  onBadgeClick,
}: {
  entry: LeaderboardEntry;
  onBadgeClick: (entry: LeaderboardEntry) => void;
}) {
  return (
    <button
      onClick={() => onBadgeClick(entry)}
      className={cn(
        "allow-rounded flex items-center gap-1 text-xs mt-1 px-2 py-0.5 rounded-full transition-colors",
        entry.badge_ids.length > 0
          ? "bg-amber-100 dark:bg-amber-900/30 text-amber-700 dark:text-amber-400 hover:bg-amber-200 dark:hover:bg-amber-900/50 cursor-pointer"
          : "bg-muted/50 text-muted-foreground cursor-default",
      )}
      disabled={entry.badge_ids.length === 0}
      title={entry.badge_ids.length > 0 ? "View badges" : "No badges yet"}
    >
      <Award
        className="w-3.5 h-3.5"
        fill={entry.badge_ids.length > 0 ? "currentColor" : "none"}
      />
      <span className="font-medium">{entry.badge_ids.length}</span>
    </button>
  );
}

/* ───────────────────── Top 3 Podium ───────────────────── */

function PodiumCard({
  entry,
  rank,
  isMe,
  onBadgeClick,
  size,
}: {
  entry: LeaderboardEntry;
  rank: number;
  isMe: boolean;
  onBadgeClick: (entry: LeaderboardEntry) => void;
  size: "lg" | "md" | "sm";
}) {
  const colorMap = {
    1: {
      border: "border-[oklch(0.77_0.16_70)]",
      bg: "bg-[oklch(0.77_0.16_70)]",
      text: "text-[oklch(0.77_0.16_70)]",
    },
    2: {
      border: "border-[oklch(0.75_0.02_260)]",
      bg: "bg-[oklch(0.75_0.02_260)]",
      text: "text-[oklch(0.75_0.02_260)]",
    },
    3: {
      border: "border-[oklch(0.6_0.1_50)]",
      bg: "bg-[oklch(0.6_0.1_50)]",
      text: "text-[oklch(0.6_0.1_50)]",
    },
  }[rank] ?? {
    border: "border-border",
    bg: "bg-muted",
    text: "text-muted-foreground",
  };

  const avatarSize =
    size === "lg"
      ? "w-14 h-14 sm:w-20 sm:h-20"
      : size === "md"
        ? "w-10 h-10 sm:w-14 sm:h-14"
        : "w-9 h-9 sm:w-12 sm:h-12";
  const avatarText =
    size === "lg" ? "text-sm sm:text-xl" : "text-xs sm:text-base";
  const cardWidth =
    size === "lg"
      ? "w-28 xs:36 sm:w-44 md:52"
      : size === "md"
        ? "w-24 xs:32 sm:w-40 md:48"
        : "w-24 xs:32 sm:w-40 md:48";
  const nameText =
    size === "lg"
      ? "text-sm sm:text-base font-semibold"
      : "text-xs sm:text-sm font-medium";

  return (
    <div className="flex flex-col items-center">
      {rank === 1 && (
        <Crown
          className="w-6 h-6 sm:w-8 sm:h-8 text-[oklch(0.77_0.16_70)] mb-1"
          fill="currentColor"
        />
      )}
      <div
        className={cn(
          cardWidth,
          "flex flex-col items-center gap-1.5 sm:gap-2 py-3 sm:py-4 px-2 border-2 bg-card",
          colorMap.border,
          "rounded-xl",
        )}
      >
        <Avatar
          className={cn(
            avatarSize,
            "allow-rounded rounded-full border-2",
            colorMap.border,
          )}
        >
          <AvatarImage src={entry.avatar_url ?? undefined} />
          <AvatarFallback
            className={cn(colorMap.bg, "text-white font-bold", avatarText)}
          >
            {getInitials(entry.display_name)}
          </AvatarFallback>
        </Avatar>
        <p className={cn(nameText, "text-center m-0 px-1 line-clamp-2")}>
          {entry.display_name}
          {isMe && <span className={styles.youTag}>you</span>}
        </p>
        <div className="flex items-center gap-1">
          <Zap
            className={cn("w-3 h-3 sm:w-3.5 sm:h-3.5", colorMap.text)}
            fill="currentColor"
          />
          <span className="text-xs sm:text-sm font-semibold tabular-nums">
            {entry.total_xp.toLocaleString()}
          </span>
        </div>
        <div className="hidden sm:block">
          <BadgeButton entry={entry} onBadgeClick={onBadgeClick} />
        </div>
      </div>
      <div
        className={cn(
          "mt-1.5 flex items-center justify-center rounded-full px-2.5 py-0.5",
          rank === 1 && "rank-badge-gold",
          rank === 2 && "rank-badge-silver",
          rank === 3 && "rank-badge-bronze",
        )}
      >
        <span className="text-white font-bold text-xs sm:text-sm">
          {ordinal(rank)}
        </span>
      </div>
    </div>
  );
}

function TopThreePodium({
  entries,
  currentUserId,
  onBadgeClick,
}: {
  entries: LeaderboardEntry[];
  currentUserId?: string;
  onBadgeClick: (entry: LeaderboardEntry) => void;
}) {
  const first = entries.find((e) => e.rank === 1);
  const second = entries.find((e) => e.rank === 2);
  const third = entries.find((e) => e.rank === 3);

  if (!first) return null;

  return (
    <div className="flex items-end justify-center gap-1 xs:gap-2 sm:gap-6 py-4 sm:py-8 px-1 xs:px-2 sm:px-4 bg-gradient-to-b from-card to-background border-b border-border">
      {second && (
        <PodiumCard
          entry={second}
          rank={2}
          isMe={second.user_id === currentUserId}
          onBadgeClick={onBadgeClick}
          size="md"
        />
      )}
      <PodiumCard
        entry={first}
        rank={1}
        isMe={first.user_id === currentUserId}
        onBadgeClick={onBadgeClick}
        size="lg"
      />
      {third && (
        <PodiumCard
          entry={third}
          rank={3}
          isMe={third.user_id === currentUserId}
          onBadgeClick={onBadgeClick}
          size="sm"
        />
      )}
    </div>
  );
}

/* ───────────────────── Leaderboard Row ───────────────────── */

function LeaderboardRow({
  entry,
  isMe,
  animationDelay = 0,
  onBadgeClick,
}: {
  entry: LeaderboardEntry;
  isMe: boolean;
  animationDelay?: number;
  onBadgeClick: (entry: LeaderboardEntry) => void;
}) {
  const isTopThree = entry.rank <= 3;

  return (
    <div
      className={cn(
        "flex items-center gap-2 sm:gap-4 px-2 sm:px-4 py-2 sm:py-3 transition-colors",
        "hover:bg-accent/50",
        isMe && "your-rank-highlight border-l-4 border-l-primary",
        isTopThree && "bg-card",
      )}
      style={{ animationDelay: `${animationDelay}ms` }}
    >
      {/* Rank */}
      <RankBadge rank={entry.rank} />

      {/* Avatar — smaller on mobile */}
      <Avatar
        className={cn(
          "w-8 h-8 sm:w-10 sm:h-10 allow-rounded rounded-full",
          isTopThree && "border-2",
          entry.rank === 1 && "border-[oklch(0.77_0.16_70)]",
          entry.rank === 2 && "border-[oklch(0.75_0.02_260)]",
          entry.rank === 3 && "border-[oklch(0.6_0.1_50)]",
        )}
      >
        <AvatarImage src={entry.avatar_url ?? undefined} />
        <AvatarFallback
          className={cn(
            "text-xs sm:text-sm font-semibold",
            isTopThree
              ? "bg-primary text-primary-foreground"
              : "bg-muted text-muted-foreground",
          )}
        >
          {getInitials(entry.display_name)}
        </AvatarFallback>
      </Avatar>

      {/* Name & Badge count */}
      <div className="flex-1 min-w-0">
        <p
          className={cn(
            "text-sm sm:text-base font-medium truncate",
            isMe ? "text-primary" : "text-foreground",
          )}
        >
          {entry.display_name}
          {isMe && (
            <span className="ml-1 sm:ml-2 text-[10px] sm:text-xs text-primary">
              (You)
            </span>
          )}
        </p>
        <button
          onClick={() => onBadgeClick(entry)}
          className={cn(
            "hidden sm:flex items-center gap-1.5 text-xs transition-colors",
            entry.badge_ids.length > 0
              ? "text-amber-600 dark:text-amber-400 hover:text-amber-700 dark:hover:text-amber-300 cursor-pointer"
              : "text-muted-foreground cursor-default",
          )}
          disabled={entry.badge_ids.length === 0}
          title={entry.badge_ids.length > 0 ? "View badges" : "No badges yet"}
        >
          <Award
            className="w-3.5 h-3.5"
            fill={entry.badge_ids.length > 0 ? "currentColor" : "none"}
          />
          <span className="font-medium">{entry.badge_ids.length}</span>
        </button>
      </div>

      {/* XP */}
      <div className="flex items-center gap-1">
        <Zap
          className={cn(
            "w-3.5 h-3.5 sm:w-4 sm:h-4",
            isTopThree
              ? "text-[oklch(0.72_0.18_142)]"
              : "text-[oklch(0.68_0.16_142)]",
          )}
          fill="currentColor"
        />
        <span
          className={cn(
            "font-semibold tabular-nums",
            isTopThree ? "text-sm sm:text-lg" : "text-xs sm:text-sm",
          )}
        >
          {entry.total_xp.toLocaleString()}
        </span>
      </div>
    </div>
  );
}

/* ───────────────────── Main ───────────────────── */

export default function Leaderboard() {
  const { siteConfig } = useDocusaurusContext();
  const progressApiUrl =
    (siteConfig.customFields?.progressApiUrl as string) ||
    "http://localhost:8002";
  const authUrl =
    (siteConfig.customFields?.authUrl as string) || "http://localhost:3001";
  const oauthClientId =
    (siteConfig.customFields?.oauthClientId as string) ||
    "agent-factory-public-client";
  const { session } = useAuth();
  const currentUserId = session?.user?.id;

  const handleSignIn = useCallback(async () => {
    const authorizationUrl = await getOAuthAuthorizationUrl("signin", {
      authUrl,
      clientId: oauthClientId,
    });
    window.location.href = authorizationUrl;
  }, [authUrl, oauthClientId]);

  const [data, setData] = useState<LeaderboardResponse | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Badge modal
  const [badgeModalOpen, setBadgeModalOpen] = useState(false);
  const [selectedEntry, setSelectedEntry] = useState<LeaderboardEntry | null>(
    null,
  );

  const fetchLeaderboard = () => {
    setIsLoading(true);
    setError(null);

    getLeaderboard(progressApiUrl)
      .then((res) => {
        setData(res);
      })
      .catch((err) => {
        console.error("[Leaderboard] Failed to load:", err);
        setError(err.message || "Failed to load leaderboard");
      })
      .finally(() => {
        setIsLoading(false);
      });
  };

  useEffect(() => {
    fetchLeaderboard();
  }, [progressApiUrl]);

  const handleBadgeClick = (entry: LeaderboardEntry) => {
    if (entry.badge_ids.length > 0) {
      setSelectedEntry(entry);
      setBadgeModalOpen(true);
    }
  };

  /* Loading */
  if (isLoading) {
    return (
      <div className="allow-rounded w-full max-w-3xl mx-auto px-4 py-8">
        <div className="flex flex-col items-center py-12">
          <Loader2 className="w-8 h-8 text-primary animate-spin mb-4" />
          <p className="text-muted-foreground">Loading leaderboard...</p>
        </div>
      </div>
    );
  }

  /* Error */
  if (error) {
    return (
      <div className="allow-rounded w-full max-w-3xl mx-auto px-4 py-8">
        <Card className="rounded-xl">
          <CardContent className="flex flex-col items-center py-12">
            <Trophy className="w-12 h-12 text-muted-foreground mb-4" />
            <p className="text-muted-foreground text-center mb-4">
              Could not load leaderboard.
              <br />
              <span className="text-xs">{error}</span>
            </p>
            <Button
              size="sm"
              variant="outline"
              className="rounded-md"
              onClick={fetchLeaderboard}
            >
              Try Again
            </Button>
          </CardContent>
        </Card>
      </div>
    );
  }

  const entries = data?.entries ?? [];

  /* Empty */
  if (entries.length === 0) {
    return (
      <div className="allow-rounded w-full max-w-3xl mx-auto px-4 py-8">
        <Card className="rounded-xl">
          <CardContent className="flex flex-col items-center py-12">
            <Trophy className="w-12 h-12 text-muted-foreground mb-4" />
            <p className="text-muted-foreground text-center">
              No learners on the leaderboard yet.
              <br />
              Complete quizzes to be the first!
            </p>
          </CardContent>
        </Card>
      </div>
    );
  }

  const top3 = entries.filter((e) => e.rank <= 3);
  const rest = entries.filter((e) => e.rank > 3);
  const myEntry = entries.find((e) => e.user_id === currentUserId);

  return (
    <div className="allow-rounded w-full max-w-3xl mx-auto px-4 py-8">
      {/* Header */}
      <div className="flex items-center justify-between gap-4 mb-4 sm:mb-6">
        <div className="flex items-center gap-2 sm:gap-3 min-w-0">
          <Trophy className="w-6 h-6 sm:w-8 sm:h-8 text-primary shrink-0" />
          <div>
            <h1 className="text-xl sm:text-2xl font-bold text-foreground m-0">
              Leaderboard
            </h1>
            <p className="text-xs sm:text-sm text-muted-foreground m-0">
              Top {Math.min(entries.length, 100)} learners
            </p>
          </div>
        </div>
        <Button
          size="sm"
          asChild
          className="hidden sm:inline-flex rounded-md shrink-0"
        >
          <Link to="/progress">Your Progress</Link>
        </Button>
      </div>

      {/* How XP Works */}
      <div className="rounded-lg border border-border bg-muted/30 px-4 py-3 mb-4 sm:mb-6">
        <div className="flex items-center gap-2 mb-2">
          <Zap className="w-4 h-4 text-[oklch(0.68_0.16_142)]" fill="currentColor" />
          <span className="text-sm font-semibold text-foreground">How to Earn XP</span>
        </div>
        <div className="text-xs sm:text-sm text-muted-foreground space-y-1">
          <p className="m-0"><strong>Quizzes</strong> — up to 100 XP per quiz, based on your score. First attempts earn the most.</p>
          <p className="m-0"><strong>Lessons</strong> — 1 XP for each lesson you read (after 60s).</p>
        </div>
        <p className="text-[11px] sm:text-xs text-muted-foreground/70 mt-2 mb-0">
          Tip: Aim for high scores on first attempts for maximum XP.
        </p>
      </div>

      <Card className="overflow-hidden rounded-xl">
        {/* Top 3 Podium */}
        {top3.length > 0 && (
          <TopThreePodium
            entries={top3}
            currentUserId={currentUserId}
            onBadgeClick={handleBadgeClick}
          />
        )}

        {/* Your Rank Section */}
        {!currentUserId ? (
          /* Sign-in prompt for non-logged-in users */
          <div className="border-b border-border bg-muted/20">
            <div className="flex items-center justify-between px-3 sm:px-4 py-2.5 sm:py-3">
              <span className="text-xs sm:text-sm text-muted-foreground">
                Sign in to track your rank
              </span>
              <Button size="sm" className="gap-1.5 shrink-0 rounded-md" onClick={handleSignIn}>
                <LogIn className="w-3.5 h-3.5" />
                Sign In
              </Button>
            </div>
          </div>
        ) : myEntry ? (
          /* Logged-in user's rank */
          <div className="border-b border-border">
            <div className="px-3 sm:px-4 py-2 text-xs font-medium text-primary uppercase tracking-wider flex items-center gap-2">
              <Trophy className="w-3 h-3" />
              Your Rank
            </div>
            <div className="flex items-center gap-2 sm:gap-4 px-2 sm:px-4 py-2 sm:py-3 your-rank-highlight border-l-4 border-l-primary">
              <div className="w-8 h-8 flex items-center justify-center font-bold text-primary text-base sm:text-lg shrink-0">
                {myEntry.rank}
              </div>
              <Avatar className="w-8 h-8 sm:w-10 sm:h-10 allow-rounded rounded-full shrink-0">
                <AvatarImage src={myEntry.avatar_url ?? undefined} />
                <AvatarFallback className="bg-primary text-primary-foreground text-xs sm:text-sm font-semibold">
                  {getInitials(myEntry.display_name)}
                </AvatarFallback>
              </Avatar>
              <div className="flex-1 min-w-0">
                <p className="text-sm sm:text-base font-medium text-primary m-0 truncate">
                  {myEntry.display_name}{" "}
                  <span className="text-[10px] sm:text-xs">(You)</span>
                </p>
                <button
                  onClick={() => handleBadgeClick(myEntry)}
                  className={cn(
                    "hidden sm:flex items-center gap-1.5 text-xs transition-colors",
                    myEntry.badge_ids.length > 0
                      ? "text-amber-600 dark:text-amber-400 hover:text-amber-700 cursor-pointer"
                      : "text-muted-foreground cursor-default",
                  )}
                  disabled={myEntry.badge_ids.length === 0}
                >
                  <Award
                    className="w-3.5 h-3.5"
                    fill={
                      myEntry.badge_ids.length > 0 ? "currentColor" : "none"
                    }
                  />
                  <span className="font-medium">
                    {myEntry.badge_ids.length} badge
                    {myEntry.badge_ids.length !== 1 ? "s" : ""}
                  </span>
                </button>
              </div>
              <div className="flex items-center gap-1">
                <Zap
                  className="w-3.5 h-3.5 sm:w-4 sm:h-4 text-[oklch(0.68_0.16_142)]"
                  fill="currentColor"
                />
                <span className="text-xs sm:text-sm font-semibold tabular-nums">
                  {myEntry.total_xp.toLocaleString()}
                </span>
              </div>
            </div>
          </div>
        ) : currentUserId ? (
          /* Logged-in but not ranked */
          <div className="border-b border-border">
            <div className="px-3 sm:px-4 py-2 text-xs font-medium text-primary uppercase tracking-wider flex items-center gap-2">
              <Trophy className="w-3 h-3" />
              Your Rank
            </div>
            <div className="flex items-center gap-2 sm:gap-4 px-3 sm:px-4 py-2 sm:py-3">
              <div className="w-8 h-8 flex items-center justify-center shrink-0">
                <Zap className="w-5 h-5 text-[oklch(0.68_0.16_142)]" />
              </div>
              <div className="flex-1 min-w-0">
                <p className="text-xs sm:text-sm text-foreground font-medium m-0">
                  Complete a quiz to join the leaderboard
                </p>
                <p className="text-[11px] sm:text-xs text-muted-foreground m-0 mt-0.5">
                  Quizzes earn up to 100 XP. Reading lessons earns 1 XP each.
                </p>
              </div>
            </div>
          </div>
        ) : null}

        {/* Leaderboard List (rank 4+) */}
        <div className="divide-y divide-border/50">
          {rest.map((entry, index) => (
            <LeaderboardRow
              key={entry.user_id}
              entry={entry}
              isMe={entry.user_id === currentUserId}
              animationDelay={index * 30}
              onBadgeClick={handleBadgeClick}
            />
          ))}
        </div>
      </Card>

      {/* Badge Modal */}
      {selectedEntry && (
        <BadgeModal
          isOpen={badgeModalOpen}
          onClose={() => setBadgeModalOpen(false)}
          displayName={selectedEntry.display_name}
          badgeIds={selectedEntry.badge_ids}
        />
      )}
    </div>
  );
}
