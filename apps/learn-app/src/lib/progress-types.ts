export interface QuizSubmitRequest {
  chapter_slug: string;
  score_pct: number;
  questions_correct: number;
  questions_total: number;
  duration_secs?: number;
}

export interface BadgeEarned {
  id: string;
  name: string;
  earned_at: string;
}

export interface StreakInfo {
  current: number;
  longest: number;
}

export interface QuizSubmitResponse {
  xp_earned: number;
  total_xp: number;
  attempt_number: number;
  best_score: number;
  new_badges: BadgeEarned[];
  streak: StreakInfo;
}

export interface LessonCompleteRequest {
  chapter_slug: string;
  lesson_slug: string;
  active_duration_secs?: number;
}

export interface LessonCompleteResponse {
  completed: boolean;
  active_duration_secs: number;
  streak: StreakInfo;
  already_completed: boolean;
  xp_earned: number;
}

export interface ProgressResponse {
  user: { display_name: string; avatar_url: string | null };
  stats: {
    total_xp: number;
    rank: number | null;
    current_streak: number;
    longest_streak: number;
    quizzes_completed: number;
    perfect_scores: number;
    lessons_completed: number;
    badge_count: number;
  };
  badges: BadgeEarned[];
  chapters: Array<{
    slug: string;
    title: string;
    best_score: number | null;
    attempts: number;
    xp_earned: number;
    lessons_completed: Array<{
      lesson_slug: string;
      active_duration_secs: number;
      completed_at: string;
    }>;
  }>;
}

export interface LeaderboardEntry {
  rank: number;
  user_id: string;
  display_name: string;
  avatar_url: string | null;
  total_xp: number;
  badge_count: number;
  badge_ids: string[];
}

export interface LeaderboardResponse {
  entries: LeaderboardEntry[];
  current_user_rank: number | null;
  total_users: number;
}

export interface BadgeDefinition {
  id: string;
  name: string;
  description: string;
  icon: string;
}

/** All 14 Phase-1 badge definitions (mirrors backend BADGE_DEFINITIONS). */
export const BADGE_DEFINITIONS: Record<string, BadgeDefinition> = {
  "first-steps": {
    id: "first-steps",
    name: "First Steps",
    description: "Complete your first quiz",
    icon: "\uD83C\uDFAF",
  },
  "perfect-score": {
    id: "perfect-score",
    name: "Perfect Score",
    description: "Score 100% on any quiz",
    icon: "\u2B50",
  },
  ace: {
    id: "ace",
    name: "Ace",
    description: "Score 100% on your first attempt",
    icon: "\uD83C\uDFC6",
  },
  "on-fire": {
    id: "on-fire",
    name: "On Fire",
    description: "3-day learning streak",
    icon: "\uD83D\uDD25",
  },
  "week-warrior": {
    id: "week-warrior",
    name: "Week Warrior",
    description: "7-day learning streak",
    icon: "\uD83D\uDCAA",
  },
  dedicated: {
    id: "dedicated",
    name: "Dedicated",
    description: "30-day learning streak",
    icon: "\uD83C\uDF96\uFE0F",
  },
  "foundations-complete": {
    id: "foundations-complete",
    name: "Foundations",
    description: "Complete all Part 1 quizzes",
    icon: "\uD83D\uDCDA",
  },
  "workflows-complete": {
    id: "workflows-complete",
    name: "Applied",
    description: "Complete all Part 2 quizzes",
    icon: "\uD83D\uDEE0\uFE0F",
  },
  "sdd-complete": {
    id: "sdd-complete",
    name: "SDD Master",
    description: "Complete all Part 3 quizzes",
    icon: "\uD83D\uDCCB",
  },
  "coding-complete": {
    id: "coding-complete",
    name: "Coder",
    description: "Complete all Part 4 quizzes",
    icon: "\uD83D\uDCBB",
  },
  "deployment-complete": {
    id: "deployment-complete",
    name: "Agent Builder",
    description: "Complete all Part 5 quizzes",
    icon: "\uD83E\uDD16",
  },
  "cloud-native-complete": {
    id: "cloud-native-complete",
    name: "Cloud Native",
    description: "Complete all Part 6 quizzes",
    icon: "\u2601\uFE0F",
  },
  "agent-factory-graduate": {
    id: "agent-factory-graduate",
    name: "Agent Factory Graduate",
    description: "Complete all quizzes in the book",
    icon: "\uD83C\uDF93",
  },
  elite: {
    id: "elite",
    name: "Elite",
    description: "Reach top 100 on leaderboard",
    icon: "\uD83D\uDC51",
  },
};
