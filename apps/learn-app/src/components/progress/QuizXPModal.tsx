import React, { useState, useEffect, useRef } from "react";
import { cn } from "@/lib/utils";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
  DialogFooter,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Zap, Trophy, ArrowRight } from "lucide-react";
import type { BadgeEarned } from "@/lib/progress-types";
import { BADGE_DEFINITIONS } from "@/lib/progress-types";
import Link from "@docusaurus/Link";
import "@/components/progress/gamification.css";

function useAnimatedNumber(
  targetValue: number,
  duration: number = 800,
  delay: number = 300,
): number {
  const [displayValue, setDisplayValue] = useState(0);
  const rafRef = useRef<number | undefined>(undefined);

  useEffect(() => {
    const delayTimer = setTimeout(() => {
      const startTime = performance.now();

      const animate = (currentTime: number) => {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const easeProgress = 1 - Math.pow(2, -10 * progress);
        const currentValue = Math.round(targetValue * easeProgress);
        setDisplayValue(currentValue);
        if (progress < 1) {
          rafRef.current = requestAnimationFrame(animate);
        }
      };

      rafRef.current = requestAnimationFrame(animate);
    }, delay);

    return () => {
      clearTimeout(delayTimer);
      if (rafRef.current !== undefined) {
        cancelAnimationFrame(rafRef.current);
      }
    };
  }, [targetValue, duration, delay]);

  return displayValue;
}

interface QuizXPModalProps {
  isOpen: boolean;
  onClose: () => void;
  scorePercentage: number;
  xpEarned: number;
  totalXp: number;
  newBadges: BadgeEarned[];
  attemptNumber: number;
  rank?: number | null;
  chapterTitle?: string;
}

export default function QuizXPModal({
  isOpen,
  onClose,
  scorePercentage,
  xpEarned,
  totalXp,
  newBadges,
  attemptNumber,
  rank,
  chapterTitle,
}: QuizXPModalProps) {
  const displayScore = useAnimatedNumber(scorePercentage, 1000, 200);
  const displayXp = useAnimatedNumber(xpEarned, 800, 600);

  const isPerfect = scorePercentage === 100;
  const isFirstAttempt = attemptNumber === 1;

  const getScoreColor = () => {
    if (scorePercentage >= 90) return "text-[oklch(0.68_0.16_142)]";
    if (scorePercentage >= 70) return "text-[oklch(0.77_0.16_77)]";
    return "text-foreground";
  };

  const getScoreMessage = () => {
    if (isPerfect && isFirstAttempt) return "Perfect on First Try!";
    if (isPerfect) return "Perfect Score!";
    if (scorePercentage >= 90) return "Excellent Work!";
    if (scorePercentage >= 80) return "Great Job!";
    if (scorePercentage >= 70) return "Good Effort!";
    if (scorePercentage >= 60) return "Keep Learning!";
    return "Room to Improve";
  };

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="sm:max-w-lg">
        <DialogHeader className="text-center pb-2">
          <DialogTitle className="text-xl">Quiz Complete!</DialogTitle>
          {chapterTitle && (
            <DialogDescription className="text-muted-foreground">
              {chapterTitle}
            </DialogDescription>
          )}
        </DialogHeader>

        {/* Score Circle */}
        <div className="flex flex-col items-center py-6">
          <div
            className={cn(
              "relative w-32 h-32 rounded-full flex flex-col items-center justify-center",
              "border-4 score-circle-reveal",
              isPerfect
                ? "border-[oklch(0.68_0.16_142)]"
                : scorePercentage >= 70
                  ? "border-[oklch(0.77_0.16_77)]"
                  : "border-border",
            )}
            style={{
              boxShadow: isPerfect
                ? "0 0 30px oklch(0.68 0.16 142 / 0.4), inset 0 0 20px oklch(0.68 0.16 142 / 0.1)"
                : undefined,
            }}
          >
            <span
              className={cn("text-4xl font-bold tabular-nums", getScoreColor())}
            >
              {displayScore}%
            </span>
            <span className="text-xs text-muted-foreground uppercase tracking-wider">
              Score
            </span>
          </div>

          <p className="text-lg font-semibold text-foreground mt-4">
            {getScoreMessage()}
          </p>

          {attemptNumber > 1 && (
            <p className="text-xs text-muted-foreground mt-1">
              Attempt #{attemptNumber}
            </p>
          )}
        </div>

        {/* XP Earned */}
        <div
          className={cn(
            "flex items-center justify-center gap-3 py-4 px-6 rounded-lg",
            "border border-[oklch(0.68_0.16_142)/30] bg-[oklch(0.68_0.16_142)/5]",
            "xp-earned-bounce",
          )}
        >
          <Zap
            className="h-6 w-6 text-[oklch(0.68_0.16_142)]"
            fill="currentColor"
          />
          <div className="flex items-baseline gap-2">
            <span className="text-3xl font-bold text-[oklch(0.68_0.16_142)] tabular-nums">
              +{displayXp}
            </span>
            <span className="text-sm text-muted-foreground">XP earned</span>
          </div>
        </div>

        {/* New Badges */}
        {newBadges.length > 0 && (
          <div className="mt-4 p-4 rounded-lg border border-primary/30 bg-primary/5">
            <div className="flex items-center gap-2 mb-3">
              <Trophy className="h-4 w-4 text-primary" />
              <span className="text-sm font-medium text-foreground">
                New Badge{newBadges.length > 1 ? "s" : ""} Earned!
              </span>
            </div>
            <div className="flex flex-wrap gap-3">
              {newBadges.map((badge) => {
                const def = BADGE_DEFINITIONS[badge.id];
                return (
                  <div
                    key={badge.id}
                    className="flex items-center gap-2 px-3 py-2 rounded-md bg-card border border-border"
                  >
                    <span className="text-xl">{def?.icon ?? "?"}</span>
                    <span className="text-sm font-medium">{badge.name}</span>
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* Total XP */}
        <div className="flex items-center justify-center gap-2 mt-4 text-sm text-muted-foreground">
          <span>Total XP:</span>
          <span className="font-semibold text-foreground tabular-nums">
            {totalXp.toLocaleString()}
          </span>
          {rank != null && (
            <>
              <span className="text-border">·</span>
              <Trophy className="h-3.5 w-3.5 text-primary" />
              <span>Rank:</span>
              <span className="font-semibold text-foreground tabular-nums">
                #{rank}
              </span>
            </>
          )}
        </div>

        {/* Actions */}
        <DialogFooter className="flex-col sm:flex-row gap-2 mt-6">
          <Button onClick={onClose} variant="outline" className="flex-1">
            Close
          </Button>
          <Button asChild className="flex-1">
            <Link to="/leaderboard">
              View Leaderboard
              <ArrowRight className="h-4 w-4 ml-2" />
            </Link>
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}
