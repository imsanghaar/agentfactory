/**
 * DocItem/Content Theme Swizzle (Wrap)
 *
 * Wraps the original DocItem/Content component with LessonContent
 * to provide tabbed interface for Full Lesson and AI Summary views.
 *
 * The summary is read from global data (populated by docusaurus-summaries-plugin)
 * which scans for .summary.md files at build time.
 */

import React, { useState, useEffect, useRef, useCallback } from "react";
import Content from "@theme-original/DocItem/Content";
import type ContentType from "@theme/DocItem/Content";
import type { WrapperProps } from "@docusaurus/types";
import { useDoc } from "@docusaurus/plugin-content-docs/client";
import { usePluginData } from "@docusaurus/useGlobalData";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import BrowserOnly from "@docusaurus/BrowserOnly";
import LessonContent from "../../../components/LessonContent";
import ReactMarkdown from "react-markdown";
import ReadingProgress from "@/components/ReadingProgress";
import DocPageActions from "@/components/DocPageActions";
import { useStudyMode } from "@/contexts/StudyModeContext";
import { useAuth } from "@/contexts/AuthContext";
import { TeachMePanel } from "@/components/TeachMePanel";
import { TeachingGuideSheet } from "@/components/TeachingGuideSheet";
import type { TeachingFrontmatter } from "@/components/TeachingGuideSheet";
import { getOAuthAuthorizationUrl } from "@/lib/auth-client";
import { useVoiceReading } from "@/contexts/VoiceReadingContext";
import { VoiceControlDock } from "@/components/VoiceControlDock";
import LessonCompleteButton from "@/components/progress/LessonCompleteButton";
import { usePracticeServer } from "@/components/TerminalPanel/usePracticeServer";
import { PracticeContext } from "@/contexts/PracticeContext";
import { PracticeSetupCard } from "@/components/PracticeSetupCard";
import { PracticeErrorCard } from "@/components/PracticeErrorCard";

// Lazy-load terminal (requires DOM)
const TerminalPanel = React.lazy(() =>
  import("@/components/TerminalPanel").then((mod) => ({
    default: mod.TerminalPanel,
  })),
);

type Props = WrapperProps<typeof ContentType>;

/**
 * Reading Time Component - calculates from content
 */
function ReadingTime() {
  const [readingTime, setReadingTime] = useState<number | null>(null);

  useEffect(() => {
    // Calculate reading time from article content
    const article = document.querySelector("article");
    if (article) {
      const text = article.textContent || "";
      const words = text.trim().split(/\s+/).length;
      const minutes = Math.ceil(words / 200); // 200 words per minute
      setReadingTime(minutes);
    }
  }, []);

  if (!readingTime) return null;

  return (
    <div className="reading-time">
      <svg
        width="14"
        height="14"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <circle cx="12" cy="12" r="10" />
        <polyline points="12 6 12 12 16 14" />
      </svg>
      <span>{readingTime} min read</span>
    </div>
  );
}

function formatLastUpdated(timestamp: number, locale: string) {
  try {
    return new Intl.DateTimeFormat(locale, {
      year: "numeric",
      month: "short",
      day: "2-digit",
    }).format(new Date(timestamp));
  } catch {
    return new Date(timestamp).toDateString();
  }
}

function getHistoryUrl(editUrl?: string): string | null {
  if (!editUrl) return null;
  try {
    const url = new URL(editUrl);
    if (!url.hostname.includes("github.com")) return null;
    url.pathname = url.pathname.replace("/edit/", "/commits/");
    return url.toString();
  } catch {
    return null;
  }
}

/**
 * Back to Top Button Component
 * Only shows when user scrolls UP (not always visible after scrolling down)
 */
function BackToTopButton() {
  const [visible, setVisible] = useState(false);
  const lastScrollY = useRef(0);

  useEffect(() => {
    const handleScroll = () => {
      const currentScrollY = window.scrollY;

      // Show only when:
      // 1. User has scrolled down at least 400px AND
      // 2. User is scrolling UP (current position < last position)
      const isScrollingUp = currentScrollY < lastScrollY.current;
      const hasScrolledEnough = currentScrollY > 400;

      setVisible(isScrollingUp && hasScrolledEnough);
      lastScrollY.current = currentScrollY;
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  if (!visible) return null;

  return (
    <button
      onClick={scrollToTop}
      className="back-to-top-button"
      title="Back to top"
      aria-label="Scroll back to top"
    >
      <svg
        width="20"
        height="20"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <path d="M18 15l-6-6-6 6" />
      </svg>
    </button>
  );
}

interface SummariesPluginData {
  summaries: Record<string, string>;
}

/**
 * Teach Me Floating Button - visible to all users
 * Redirects to login if not authenticated, opens panel if authenticated
 */
function TeachMeFloatingButton({
  isLoggedIn,
  openPanel,
  handleLoginRedirect,
}: {
  isLoggedIn: boolean;
  openPanel: () => void;
  handleLoginRedirect: () => void;
}) {
  return (
    <button
      onClick={isLoggedIn ? openPanel : handleLoginRedirect}
      className="study-mode-float"
      title={isLoggedIn ? "Teach Me" : "Sign in for Teach Me"}
      aria-label={isLoggedIn ? "Open Teach Me" : "Sign in for Teach Me Access"}
    >
      <svg
        width="20"
        height="20"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z" />
        <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z" />
      </svg>
    </button>
  );
}

/**
 * Ask Floating Button - opens panel directly in ask mode
 * Redirects to login if not authenticated
 */
function AskFloatingButton({
  isLoggedIn,
  openPanelInAskMode,
  handleLoginRedirect,
}: {
  isLoggedIn: boolean;
  openPanelInAskMode: () => void;
  handleLoginRedirect: () => void;
}) {
  return (
    <button
      onClick={isLoggedIn ? openPanelInAskMode : handleLoginRedirect}
      className="ask-mode-float"
      title={isLoggedIn ? "Ask a Question" : "Sign in to ask questions"}
      aria-label={isLoggedIn ? "Open Ask Mode" : "Sign in for Ask Mode Access"}
    >
      <svg
        width="20"
        height="20"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        <circle cx="12" cy="12" r="10" />
        <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" />
        <line x1="12" y1="17" x2="12.01" y2="17" />
      </svg>
    </button>
  );
}

/**
 * Speaker Floating Button - toggles voice/speaker controls using VoiceReadingContext
 * Provides word-by-word reading with blur/highlight animation
 */
function SpeakerFloatingButton() {
  const { isPlaying, toggleSpeech } = useVoiceReading();

  return (
    <button
      onClick={toggleSpeech}
      className={`speaker-float ${isPlaying ? "speaker-float--active" : ""}`}
      title={isPlaying ? "Stop Speaking" : "Read Aloud"}
      aria-label={isPlaying ? "Stop Speaking" : "Read Page Aloud"}
      aria-pressed={isPlaying}
    >
      <svg
        width="20"
        height="20"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      >
        {isPlaying ? (
          <>
            {/* Volume 2 icon (sound on with waves) */}
            <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5" />
            <path d="M15.54 8.46a5 5 0 0 1 0 7.07" />
            <path d="M19.07 4.93a10 10 0 0 1 0 14.14" />
          </>
        ) : (
          <>
            {/* Volume icon (speaker) */}
            <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5" />
            <path d="M15.54 8.46a5 5 0 0 1 0 7.07" />
          </>
        )}
      </svg>
    </button>
  );
}

/**
 * PracticeOverlay — Fixed overlay on right side of viewport.
 * Contains resize handle + terminal. The lesson content stays in the
 * normal document flow on the left (CSS constrains its width).
 */
function PracticeOverlay({
  exerciseId,
  subExercise,
  onClose,
}: {
  exerciseId: string;
  subExercise?: string;
  onClose: () => void;
}) {
  const {
    serverAvailable,
    startSession,
    resetSession,
    isStarting,
    sessionError,
    clearError,
    onWsConnected,
    onWsDisconnected,
    onWsError,
  } = usePracticeServer(true);
  const [wsUrl, setWsUrl] = useState<string | null>(null);
  const [leftWidth, setLeftWidth] = useState(50);
  const [isResetting, setIsResetting] = useState(false);
  const dragCleanupRef = useRef<(() => void) | null>(null);

  useEffect(() => {
    if (
      exerciseId &&
      serverAvailable &&
      !wsUrl &&
      !isStarting &&
      !sessionError
    ) {
      startSession(exerciseId, subExercise).then((session) => {
        if (session) setWsUrl(session.wsUrl);
      });
    }
  }, [
    exerciseId,
    subExercise,
    serverAvailable,
    wsUrl,
    isStarting,
    sessionError,
    startSession,
  ]);

  // Apply CSS custom properties for resizable split
  useEffect(() => {
    document.documentElement.style.setProperty(
      "--practice-left-width",
      `${leftWidth}%`,
    );
    document.documentElement.style.setProperty(
      "--practice-right-width",
      `${100 - leftWidth}%`,
    );
    return () => {
      document.documentElement.style.removeProperty("--practice-left-width");
      document.documentElement.style.removeProperty("--practice-right-width");
    };
  }, [leftWidth]);

  // Esc to close overlay
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
    };
    document.addEventListener("keydown", handleKeyDown);
    return () => document.removeEventListener("keydown", handleKeyDown);
  }, [onClose]);

  // Clean up drag listeners if component unmounts mid-drag
  useEffect(() => {
    return () => {
      dragCleanupRef.current?.();
    };
  }, []);

  const handleRetry = () => {
    clearError();
    setWsUrl(null);
  };

  const handleReset = async () => {
    setIsResetting(true);
    const ok = await resetSession(exerciseId);
    setIsResetting(false);
    if (ok) {
      setWsUrl(null);
      clearError();
    }
  };

  const handleResizeStart = (e: React.MouseEvent) => {
    e.preventDefault();
    document.body.style.cursor = "col-resize";
    document.body.style.userSelect = "none";

    const handleMouseMove = (ev: MouseEvent) => {
      const percent = (ev.clientX / window.innerWidth) * 100;
      setLeftWidth(Math.max(20, Math.min(80, percent)));
    };

    const handleMouseUp = () => {
      document.body.style.cursor = "";
      document.body.style.userSelect = "";
      document.removeEventListener("mousemove", handleMouseMove);
      document.removeEventListener("mouseup", handleMouseUp);
      dragCleanupRef.current = null;
    };

    dragCleanupRef.current = () => {
      document.body.style.cursor = "";
      document.body.style.userSelect = "";
      document.removeEventListener("mousemove", handleMouseMove);
      document.removeEventListener("mouseup", handleMouseUp);
    };

    document.addEventListener("mousemove", handleMouseMove);
    document.addEventListener("mouseup", handleMouseUp);
  };

  return (
    <div className="practice-overlay">
      <div
        className="practice-resize-handle"
        onMouseDown={handleResizeStart}
        title="Drag to resize"
      />
      <div className="practice-terminal-pane">
        <div className="practice-terminal-header">
          <svg
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <polyline points="4 17 10 11 4 5" />
            <line x1="12" y1="19" x2="20" y2="19" />
          </svg>
          <span className="practice-terminal-title">{exerciseId}</span>
          <span className="practice-terminal-beta">Beta</span>
          <span className="practice-terminal-hint">
            {subExercise ? `Exercise ${subExercise}` : exerciseId}
          </span>
          <button
            onClick={handleReset}
            className="practice-terminal-reset"
            title="Reset exercise (re-download fresh copy)"
            aria-label="Reset exercise"
            disabled={isResetting}
          >
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <polyline points="1 4 1 10 7 10" />
              <path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10" />
            </svg>
          </button>
          <button
            onClick={onClose}
            className="practice-terminal-close"
            title="Close terminal"
            aria-label="Close practice terminal"
          >
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <line x1="18" y1="6" x2="6" y2="18" />
              <line x1="6" y1="6" x2="18" y2="18" />
            </svg>
          </button>
        </div>
        <div className="practice-terminal-body">
          <BrowserOnly
            fallback={
              <div className="practice-terminal-loading">Loading...</div>
            }
          >
            {() =>
              !serverAvailable ? (
                <PracticeSetupCard />
              ) : sessionError ? (
                <PracticeErrorCard
                  error={sessionError}
                  onRetry={handleRetry}
                  onRestart={handleRetry}
                />
              ) : wsUrl ? (
                <React.Suspense
                  fallback={
                    <div className="practice-terminal-loading">
                      Loading terminal...
                    </div>
                  }
                >
                  <TerminalPanel
                    wsUrl={wsUrl}
                    onWsConnected={onWsConnected}
                    onWsDisconnected={onWsDisconnected}
                    onWsError={onWsError}
                    onRestart={handleRetry}
                  />
                </React.Suspense>
              ) : (
                <div className="practice-terminal-loading">
                  {isStarting ? "Starting exercise..." : "Connecting..."}
                </div>
              )
            }
          </BrowserOnly>
        </div>
      </div>
    </div>
  );
}

export default function ContentWrapper(props: Props): React.ReactElement {
  const doc = useDoc();

  // Persist zen mode in localStorage
  const [zenMode, setZenMode] = React.useState(() => {
    if (typeof window !== "undefined") {
      return localStorage.getItem("zenMode") === "true";
    }
    return false;
  });

  // Voice reading is now handled by VoiceReadingContext (word-by-word highlighting)

  React.useEffect(() => {
    if (zenMode) {
      document.body.classList.add("zen-mode");
      localStorage.setItem("zenMode", "true");
    } else {
      document.body.classList.remove("zen-mode");
      localStorage.setItem("zenMode", "false");
    }
  }, [zenMode]);

  // Apply zen mode on mount (for SSR hydration)
  React.useEffect(() => {
    if (localStorage.getItem("zenMode") === "true") {
      document.body.classList.add("zen-mode");
    }
  }, []);

  // Get summaries from global data (populated by docusaurus-summaries-plugin)
  let summaries: Record<string, string> = {};
  try {
    const pluginData = usePluginData("docusaurus-summaries-plugin") as
      | SummariesPluginData
      | undefined;
    summaries = pluginData?.summaries || {};
  } catch {
    // Plugin might not be loaded yet or doesn't exist
    summaries = {};
  }

  // Get the doc's source path to look up its summary
  // The sourceDirName is like "01-Introducing-AI-Driven-Development/01-ai-development-revolution"
  // The slug is the doc ID
  // The summary key is stored as relative path without .summary.md
  // e.g., "01-Introducing-AI-Driven-Development/01-ai-development-revolution/08-traditional-cs-education-gaps"

  // Build the lookup key from doc metadata
  const metadata = doc.metadata;
  const sourceDirName = metadata.sourceDirName || "";
  const slug = metadata.slug || "";

  // The source path in doc metadata points to the markdown file
  // We need to construct the summary lookup key
  // Doc ID format example: "01-Introducing-AI-Driven-Development/01-ai-development-revolution/08-traditional-cs-education-gaps"
  const docId = metadata.id;

  // Debug log in development
  if (typeof window !== "undefined" && process.env.NODE_ENV === "development") {
    console.log("[DocItem/Content] Doc ID:", docId);
    console.log("[DocItem/Content] Source dir:", sourceDirName);
    console.log("[DocItem/Content] Slug:", slug);
    console.log(
      "[DocItem/Content] Available summaries:",
      Object.keys(summaries),
    );
  }

  // Look up summary by doc ID (the key format matches how plugin stores them)
  const summary = summaries[docId];

  // Get lesson path for TeachMePanel
  // Use metadata.source for the actual file path with numeric prefixes
  // Format: @site/docs/01-Part/02-Chapter/03-lesson.md -> 01-Part/02-Chapter/03-lesson
  const rawSource = (metadata as { source?: string }).source || "";
  const lessonPath = rawSource
    .replace(/^@site\/docs\//, "")
    .replace(/\.(md|mdx)$/, "");

  // Study mode controls
  const { isOpen: isStudyModeOpen, openPanel, setMode } = useStudyMode();

  // Callback to open panel in ask mode
  const openPanelInAskMode = React.useCallback(() => {
    setMode("ask");
    openPanel();
  }, [setMode, openPanel]);
  const { session } = useAuth();
  const isLoggedIn = !!session?.user;

  // Auth config for login redirect
  const { siteConfig, i18n } = useDocusaurusContext();
  const authUrl = siteConfig.customFields?.authUrl as string | undefined;
  const oauthClientId = siteConfig.customFields?.oauthClientId as
    | string
    | undefined;
  const locale = i18n.currentLocale || "en";

  const lastUpdatedAt = metadata.lastUpdatedAt;
  const editUrl = metadata.editUrl;
  const historyUrl = getHistoryUrl(editUrl);
  // Only show real git dates, not simulated dev dates (year 2018 is Docusaurus's fake date)
  const isRealDate =
    lastUpdatedAt && new Date(lastUpdatedAt).getFullYear() > 2020;
  const showUpdateMeta = Boolean(isRealDate || historyUrl);

  /**
   * Redirect to login page with return URL (for non-logged-in users)
   */
  const handleLoginRedirect = useCallback(async () => {
    try {
      const returnUrl = window.location.href;
      localStorage.setItem("auth_return_url", returnUrl);
      const loginUrl = await getOAuthAuthorizationUrl(undefined, {
        authUrl,
        clientId: oauthClientId,
      });
      window.location.href = loginUrl;
    } catch (err) {
      console.error("Failed to redirect to login:", err);
    }
  }, [authUrl, oauthClientId]);

  // Determine if this is a content page vs category landing page
  // - Lessons have 3+ path segments: part/chapter/lesson
  // - Special root pages (thesis, preface) have 1 segment but ARE content pages
  // - Parts have 1 segment (category landing - no panel)
  // - Chapters have 2 segments (category landing - no panel)
  const pathSegments = docId.split("/").filter(Boolean);
  const specialRootPages = ["thesis", "preface", "preface-agent-native"];
  const isSpecialRootPage =
    pathSegments.length === 1 && specialRootPages.includes(pathSegments[0]);
  const isQuizPage = docId.toLowerCase().includes("quiz");
  const isLeafPage =
    (pathSegments.length >= 3 || isSpecialRootPage) && !isQuizPage;

  // Derive chapter + lesson slugs for the LessonCompleteButton
  // Use slug (from frontmatter) when available to preserve progress tracking
  // across directory restructuring. Falls back to docId for files without slug.
  const slugPath = (slug || docId).replace(/^\//, "");
  const slugSegments = slugPath.split("/");
  const lessonSlug = slugSegments[slugSegments.length - 1] || "";
  const chapterSlug = slugSegments.slice(0, -1).join("/");
  const hasValidSlug = chapterSlug.length > 0 && lessonSlug.length > 0;
  const isCategoryIndex =
    rawSource.endsWith("README.md") ||
    rawSource.endsWith("README.mdx") ||
    rawSource.endsWith("index.md") ||
    rawSource.endsWith("index.mdx");

  // Teaching Guide Sheet state
  const [teachingGuideOpen, setTeachingGuideOpen] = React.useState(false);
  const frontMatter = (doc as { frontMatter?: TeachingFrontmatter })
    .frontMatter;
  const hasTeachingData =
    isLeafPage &&
    frontMatter?.learning_objectives != null &&
    (frontMatter.learning_objectives as unknown[]).length > 0;

  // Practice terminal state (gated by feature flag)
  const practiceEnabled = siteConfig.customFields?.practiceEnabled as
    | boolean
    | undefined;
  const practiceExerciseId = practiceEnabled
    ? (doc as { frontMatter?: { practice_exercise?: string } }).frontMatter
        ?.practice_exercise
    : undefined;
  const [practiceOpen, setPracticeOpen] = useState(false);
  const [practiceSubExercise, setPracticeSubExercise] = useState<
    string | undefined
  >();

  // Add/remove body class for split layout (affects Docusaurus container widths)
  useEffect(() => {
    if (practiceOpen) {
      document.body.classList.add("practice-split-active");
    } else {
      document.body.classList.remove("practice-split-active");
    }
    return () => document.body.classList.remove("practice-split-active");
  }, [practiceOpen]);

  // Shared PracticeContext value for ExerciseCard components
  const practiceContextValue = React.useMemo(
    () => ({
      practiceOpen,
      openPractice: (subId?: string) => {
        setPracticeSubExercise(subId);
        setPracticeOpen(true);
      },
    }),
    [practiceOpen],
  );

  // If no summary, just render original content
  if (!summary) {
    return (
      <PracticeContext.Provider value={practiceContextValue}>
        <ReadingProgress />
        <div className="doc-content-header">
          <ReadingTime />
          <DocPageActions
            onOpenTeachingGuide={
              hasTeachingData ? () => setTeachingGuideOpen(true) : undefined
            }
          />
        </div>
        {showUpdateMeta && (
          <div className="doc-update-meta">
            {isRealDate && (
              <div className="doc-update-meta__item">
                Updated {formatLastUpdated(lastUpdatedAt, locale)}
              </div>
            )}
            {historyUrl && (
              <div className="doc-update-meta__links">
                <a href={historyUrl} target="_blank" rel="noopener noreferrer">
                  Version history
                </a>
              </div>
            )}
          </div>
        )}
        {/* Floating action buttons - hidden when study mode panel is open */}
        {!isStudyModeOpen && (
          <div className="floating-actions">
            <BackToTopButton />
            <SpeakerFloatingButton />
            {/* Play Video Button - Only on Preface page */}
            {docId === "preface-agent-native" && (
              <button
                onClick={() => {
                  const event = new CustomEvent("open-chapter-video");
                  window.dispatchEvent(event);
                }}
                className="play-video-float"
                title="Watch Video"
                aria-label="Watch Video of this Chapter"
              >
                <svg
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="currentColor"
                >
                  <path d="M8 5v14l11-7z" />
                </svg>
              </button>
            )}
            <button
              onClick={() => setZenMode(!zenMode)}
              className="zen-mode-toggle"
              title={zenMode ? "Exit Focus Mode" : "Focus Mode"}
              aria-label={zenMode ? "Exit Focus Mode" : "Enter Focus Mode"}
            >
              {zenMode ? (
                // Exit: Grid/sidebar icon
                <svg
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <rect x="3" y="3" width="7" height="7"></rect>
                  <rect x="14" y="3" width="7" height="7"></rect>
                  <rect x="14" y="14" width="7" height="7"></rect>
                  <rect x="3" y="14" width="7" height="7"></rect>
                </svg>
              ) : (
                // Enter: Focus/center icon
                <svg
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <circle cx="12" cy="12" r="3"></circle>
                  <path d="M3 12h4m10 0h4M12 3v4m0 10v4"></path>
                </svg>
              )}
            </button>
          </div>
        )}
        <Content {...props} />
        {isLeafPage &&
          isLoggedIn &&
          hasValidSlug &&
          !isQuizPage &&
          !isCategoryIndex && (
            <LessonCompleteButton
              chapterSlug={chapterSlug}
              lessonSlug={lessonSlug}
            />
          )}
        {practiceOpen && practiceExerciseId && (
          <PracticeOverlay
            exerciseId={practiceExerciseId}
            subExercise={practiceSubExercise}
            onClose={() => setPracticeOpen(false)}
          />
        )}
        <VoiceControlDock />
        {<TeachMePanel lessonPath={lessonPath} />}

        {hasTeachingData && frontMatter && (
          <TeachingGuideSheet
            open={teachingGuideOpen}
            onOpenChange={setTeachingGuideOpen}
            frontmatter={frontMatter}
          />
        )}
      </PracticeContext.Provider>
    );
  }

  const summaryElement = <ReactMarkdown>{summary}</ReactMarkdown>;

  return (
    <PracticeContext.Provider value={practiceContextValue}>
      <ReadingProgress />
      <div className="doc-content-header">
        <ReadingTime />
        <DocPageActions
          onOpenTeachingGuide={
            hasTeachingData ? () => setTeachingGuideOpen(true) : undefined
          }
        />
      </div>
      {showUpdateMeta && (
        <div className="doc-update-meta">
          {isRealDate && (
            <div className="doc-update-meta__item">
              Updated {formatLastUpdated(lastUpdatedAt, locale)}
            </div>
          )}
          {historyUrl && (
            <div className="doc-update-meta__links">
              <a href={historyUrl} target="_blank" rel="noopener noreferrer">
                Version history
              </a>
            </div>
          )}
        </div>
      )}
      {/* Floating action buttons - hidden when study mode panel is open */}
      {!isStudyModeOpen && (
        <div className="floating-actions">
          <BackToTopButton />
          <SpeakerFloatingButton />
          <TeachMeFloatingButton
            isLoggedIn={isLoggedIn}
            openPanel={openPanel}
            handleLoginRedirect={handleLoginRedirect}
          />
          <AskFloatingButton
            isLoggedIn={isLoggedIn}
            openPanelInAskMode={openPanelInAskMode}
            handleLoginRedirect={handleLoginRedirect}
          />
          <button
            onClick={() => setZenMode(!zenMode)}
            className="zen-mode-toggle"
            title={zenMode ? "Exit Focus Mode" : "Focus Mode"}
            aria-label={zenMode ? "Exit Focus Mode" : "Enter Focus Mode"}
          >
            {zenMode ? (
              // Exit: Grid/sidebar icon
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <rect x="3" y="3" width="7" height="7"></rect>
                <rect x="14" y="3" width="7" height="7"></rect>
                <rect x="14" y="14" width="7" height="7"></rect>
                <rect x="3" y="14" width="7" height="7"></rect>
              </svg>
            ) : (
              // Enter: Focus/center icon
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              >
                <circle cx="12" cy="12" r="3"></circle>
                <path d="M3 12h4m10 0h4M12 3v4m0 10v4"></path>
              </svg>
            )}
          </button>
        </div>
      )}
      <LessonContent summaryElement={summaryElement}>
        <Content {...props} />
      </LessonContent>
      {isLeafPage &&
        isLoggedIn &&
        hasValidSlug &&
        !isQuizPage &&
        !isCategoryIndex && (
          <LessonCompleteButton
            chapterSlug={chapterSlug}
            lessonSlug={lessonSlug}
          />
        )}
      {practiceOpen && practiceExerciseId && (
        <PracticeOverlay
          exerciseId={practiceExerciseId}
          subExercise={practiceSubExercise}
          onClose={() => setPracticeOpen(false)}
        />
      )}
      <VoiceControlDock />
      {<TeachMePanel lessonPath={lessonPath} />}
      {hasTeachingData && frontMatter && (
        <TeachingGuideSheet
          open={teachingGuideOpen}
          onOpenChange={setTeachingGuideOpen}
          frontmatter={frontMatter}
        />
      )}
    </PracticeContext.Provider>
  );
}
