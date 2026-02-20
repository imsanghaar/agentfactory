import React from "react";
import { cn } from "@/lib/utils";
import { Lock } from "lucide-react";
import type { BadgeEarned } from "@/lib/progress-types";
import { BADGE_DEFINITIONS } from "@/lib/progress-types";
import "@/components/progress/gamification.css";

interface BadgeCardProps {
  badgeId: string;
  isEarned: boolean;
  earnedAt?: string;
  size?: "sm" | "md" | "lg";
  showDescription?: boolean;
  className?: string;
}

export function BadgeCard({
  badgeId,
  isEarned,
  earnedAt,
  size = "md",
  showDescription = true,
  className,
}: BadgeCardProps) {
  const def = BADGE_DEFINITIONS[badgeId];
  if (!def) return null;

  const sizeClasses = {
    sm: "p-2",
    md: "p-3",
    lg: "p-4",
  };

  const iconSizes = {
    sm: "text-xl",
    md: "text-2xl",
    lg: "text-4xl",
  };

  const nameSizes = {
    sm: "text-xs",
    md: "text-sm",
    lg: "text-base",
  };

  return (
    <div
      className={cn(
        "relative flex flex-col items-center rounded-xl border transition-all duration-200",
        sizeClasses[size],
        isEarned
          ? "bg-card border-primary/30 hover:border-primary/50"
          : "bg-muted/30 border-border opacity-60",
        className,
      )}
    >
      {/* Badge Icon */}
      <div
        className={cn(
          "relative flex items-center justify-center",
          iconSizes[size],
          isEarned ? "badge-earned-glow" : "grayscale",
        )}
      >
        <span role="img" aria-label={def.name}>
          {def.icon}
        </span>

        {!isEarned && (
          <div className="absolute inset-0 flex items-center justify-center">
            <Lock className="h-3 w-3 text-muted-foreground opacity-70" />
          </div>
        )}
      </div>

      {/* Badge Name */}
      <span
        className={cn(
          "font-medium text-center mt-2 leading-tight",
          nameSizes[size],
          isEarned ? "text-foreground" : "text-muted-foreground",
        )}
      >
        {def.name}
      </span>

      {/* Description */}
      {showDescription && size !== "sm" && (
        <span
          className={cn(
            "text-[10px] text-muted-foreground text-center mt-1 leading-tight",
            size === "lg" && "text-xs",
          )}
        >
          {def.description}
        </span>
      )}

      {/* Earned date */}
      {isEarned && earnedAt && size === "lg" && (
        <span className="text-[10px] text-primary mt-2">
          Earned {new Date(earnedAt).toLocaleDateString()}
        </span>
      )}
    </div>
  );
}

interface BadgeGridProps {
  earnedBadges: BadgeEarned[];
  showLocked?: boolean;
  size?: "sm" | "md" | "lg";
  columns?: 2 | 3 | 4 | 5 | 6;
  className?: string;
}

export function BadgeGrid({
  earnedBadges,
  showLocked = true,
  size = "md",
  columns = 4,
  className,
}: BadgeGridProps) {
  const earnedIds = new Set(earnedBadges.map((b) => b.id));
  const allBadgeIds = Object.keys(BADGE_DEFINITIONS);

  const gridCols = {
    2: "grid-cols-2",
    3: "grid-cols-2 sm:grid-cols-3",
    4: "grid-cols-2 sm:grid-cols-4",
    5: "grid-cols-2 sm:grid-cols-3 md:grid-cols-5",
    6: "grid-cols-3 sm:grid-cols-4 md:grid-cols-6",
  };

  return (
    <div className={cn("grid gap-3", gridCols[columns], className)}>
      {/* Earned badges first */}
      {earnedBadges.map((badge) => (
        <BadgeCard
          key={badge.id}
          badgeId={badge.id}
          isEarned={true}
          earnedAt={badge.earned_at}
          size={size}
          showDescription={size !== "sm"}
        />
      ))}

      {/* Locked badges */}
      {showLocked &&
        allBadgeIds
          .filter((id) => !earnedIds.has(id))
          .map((badgeId) => (
            <BadgeCard
              key={badgeId}
              badgeId={badgeId}
              isEarned={false}
              size={size}
              showDescription={size !== "sm"}
            />
          ))}
    </div>
  );
}

export default BadgeCard;
