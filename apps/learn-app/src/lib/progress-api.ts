import type {
  QuizSubmitRequest,
  QuizSubmitResponse,
  LessonCompleteRequest,
  LessonCompleteResponse,
  ProgressResponse,
  LeaderboardResponse,
} from "./progress-types";

const getAuthHeaders = (): Record<string, string> => {
  const token = localStorage.getItem("ainative_id_token");
  if (!token) return {};
  return { Authorization: `Bearer ${token}` };
};

export async function submitQuizScore(
  baseUrl: string,
  data: QuizSubmitRequest,
): Promise<QuizSubmitResponse> {
  const response = await fetch(`${baseUrl}/api/v1/quiz/submit`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...getAuthHeaders(),
    },
    body: JSON.stringify(data),
  });
  if (!response.ok) {
    throw new Error(`Quiz submit failed: ${response.status}`);
  }
  return response.json();
}

export async function completeLesson(
  baseUrl: string,
  data: LessonCompleteRequest,
): Promise<LessonCompleteResponse> {
  const response = await fetch(`${baseUrl}/api/v1/lesson/complete`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...getAuthHeaders(),
    },
    body: JSON.stringify(data),
  });
  if (!response.ok) {
    throw new Error(`Lesson complete failed: ${response.status}`);
  }
  return response.json();
}

export async function getProgress(baseUrl: string): Promise<ProgressResponse> {
  const response = await fetch(`${baseUrl}/api/v1/progress/me`, {
    headers: getAuthHeaders(),
  });
  if (!response.ok) {
    throw new Error(`Get progress failed: ${response.status}`);
  }
  return response.json();
}

export async function getLeaderboard(
  baseUrl: string,
): Promise<LeaderboardResponse> {
  const headers: Record<string, string> = {};
  // Send auth if available (for personalized current_user_rank), but don't require it
  const token = localStorage.getItem("ainative_id_token");
  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }
  const response = await fetch(`${baseUrl}/api/v1/leaderboard`, { headers });
  if (!response.ok) {
    throw new Error(`Get leaderboard failed: ${response.status}`);
  }
  return response.json();
}

export async function updatePreferences(
  baseUrl: string,
  data: { show_on_leaderboard: boolean },
): Promise<void> {
  const response = await fetch(`${baseUrl}/api/v1/progress/me/preferences`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      ...getAuthHeaders(),
    },
    body: JSON.stringify(data),
  });
  if (!response.ok) {
    throw new Error(`Update preferences failed: ${response.status}`);
  }
}
