import React, { useState, useEffect, useRef } from "react";
import { cn } from "@/lib/utils";
import { useProgress } from "@/contexts/ProgressContext";
import { useAuth } from "@/contexts/AuthContext";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Zap, Flame, Trophy, ChevronDown } from "lucide-react";
import Link from "@docusaurus/Link";
import "@/components/progress/gamification.css";

function useAnimatedNumber(
  targetValue: number,
  duration: number = 600,
): number {
  const [displayValue, setDisplayValue] = useState(targetValue);
  const previousValue = useRef(targetValue);

  useEffect(() => {
    if (targetValue === previousValue.current) return;

    const startValue = previousValue.current;
    const difference = targetValue - startValue;
    const startTime = performance.now();

    const animate = (currentTime: number) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const easeProgress = 1 - Math.pow(1 - progress, 3);
      const currentValue = Math.round(startValue + difference * easeProgress);
      setDisplayValue(currentValue);
      if (progress < 1) {
        requestAnimationFrame(animate);
      }
    };

    requestAnimationFrame(animate);
    previousValue.current = targetValue;
  }, [targetValue, duration]);

  return displayValue;
}

interface XPCounterProps {
  className?: string;
}

export default function XPCounter({ className }: XPCounterProps) {
  const { session } = useAuth();
  const { progress } = useProgress();

  const totalXp = progress?.stats?.total_xp ?? 0;
  const displayXp = useAnimatedNumber(totalXp);
  const currentStreak = progress?.stats?.current_streak ?? 0;
  const rank = progress?.stats?.rank;
  const badgeCount = progress?.stats?.badge_count ?? 0;

  if (!session?.user) {
    return null;
  }

  return (
    <DropdownMenu modal={false}>
      <DropdownMenuTrigger asChild>
        <button
          className={cn(
            "relative flex items-center gap-1.5 px-2.5 py-1.5 text-sm font-medium",
            "rounded-md border border-border bg-card hover:bg-accent",
            "transition-all duration-200",
            "focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
            className,
          )}
        >
          <Zap
            className="h-4 w-4 text-[oklch(0.68_0.16_142)]"
            fill="currentColor"
          />
          <span className="tabular-nums font-semibold tracking-tight text-foreground">
            {displayXp.toLocaleString()}
          </span>
          <span className="text-muted-foreground text-xs">XP</span>
          <ChevronDown className="h-3 w-3 text-muted-foreground ml-0.5" />
        </button>
      </DropdownMenuTrigger>

      <DropdownMenuContent
        align="end"
        className="w-64 p-0 border bg-card"
        sideOffset={8}
      >
        {/* Header */}
        <div className="px-4 py-3 border-b border-border bg-muted/30">
          <div className="flex items-center justify-between">
            <span className="text-sm font-medium text-foreground">
              Your Progress
            </span>
            <Link
              to="/progress"
              className="text-xs text-primary hover:underline"
            >
              View All
            </Link>
          </div>
        </div>

        {/* Stats Grid */}
        <div className="p-3 grid grid-cols-3 gap-3">
          <div className="flex flex-col items-center p-2 rounded-md border border-border bg-background">
            <Zap
              className="h-5 w-5 text-[oklch(0.68_0.16_142)] mb-1"
              fill="currentColor"
            />
            <span className="text-lg font-bold tabular-nums text-foreground">
              {totalXp.toLocaleString()}
            </span>
            <span className="text-[10px] text-muted-foreground uppercase tracking-wider">
              Total XP
            </span>
          </div>

          <Link
            to="/leaderboard"
            className="flex flex-col items-center p-2 rounded-md border border-border bg-background hover:bg-accent transition-colors no-underline"
          >
            <Trophy className="h-5 w-5 text-primary mb-1" />
            <span className="text-lg font-bold tabular-nums text-foreground">
              {rank ? `#${rank}` : "--"}
            </span>
            <span className="text-[10px] text-muted-foreground uppercase tracking-wider">
              Rank
            </span>
          </Link>

          <div className="flex flex-col items-center p-2 rounded-md border border-border bg-background">
            <Flame
              className={cn(
                "h-5 w-5 mb-1",
                currentStreak > 0
                  ? "text-[oklch(0.77_0.16_77)] gf-streak-flame"
                  : "text-muted-foreground",
              )}
              fill={currentStreak > 0 ? "currentColor" : "none"}
            />
            <span className="text-lg font-bold tabular-nums text-foreground">
              {currentStreak}
            </span>
            <span className="text-[10px] text-muted-foreground uppercase tracking-wider">
              Streak
            </span>
          </div>
        </div>

        {/* Footer */}
        <div className="px-4 py-3 border-t border-border bg-muted/20">
          <div className="flex items-center justify-between text-xs">
            <span className="text-muted-foreground">
              {progress?.chapters?.length ?? 0} chapters started
            </span>
            <span className="text-muted-foreground">
              {badgeCount} badge{badgeCount !== 1 ? "s" : ""}
            </span>
          </div>
        </div>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
