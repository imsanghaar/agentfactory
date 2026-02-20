"use client";

import * as React from "react";
import { Play } from "lucide-react";
import { cn } from "@/lib/utils";

export interface ChapterVideoButtonProps {
  onClick?: () => void;
  className?: string;
}

export function ChapterVideoButton({ onClick, className }: ChapterVideoButtonProps) {
  return (
    <button
      onClick={onClick}
      className={cn(
        "doc-page-actions-video",
        className
      )}
    >
      <Play className="h-4 w-4 fill-current" />
      <span>Play</span>
    </button>
  );
}
