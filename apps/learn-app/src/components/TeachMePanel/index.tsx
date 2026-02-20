/**
 * TeachMePanel Component - Official OpenAI ChatKit Integration
 *
 * Uses @openai/chatkit-react for the chat UI with Shadcn Sheet for the panel.
 * Connected to our self-hosted ChatKit server for book-grounded responses.
 *
 * Features:
 * - Socratic Teaching Mode (teach) - explains step-by-step, asks checking questions
 * - Quick Ask Mode (ask) - direct answers via text selection
 * - Text selection "Ask" button for quick questions
 *
 * Reference: https://github.com/openai/openai-chatkit-starter-app
 */

import React, { useState, useMemo, useCallback, useEffect } from "react";
import { ChatKit, useChatKit } from "@openai/chatkit-react";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import { useStudyMode } from "../../contexts/StudyModeContext";
import { useAuth } from "../../contexts/AuthContext";
import { useUserDisplayName } from "../../hooks/useUserDisplayName";
import { getOAuthAuthorizationUrl } from "@/lib/auth-client";
import { Sheet, SheetContent, SheetClose } from "@/components/ui/sheet";
import { X, Lock } from "lucide-react";
import styles from "./styles.module.css";

// Fallback user ID for anonymous users (not logged in)
function getAnonymousUserId(): string {
  if (typeof window === "undefined") return "anonymous";

  let userId = localStorage.getItem("study_mode_user_id");
  if (!userId) {
    userId = `anon_${Math.random().toString(36).substring(2, 15)}`;
    localStorage.setItem("study_mode_user_id", userId);
  }
  return userId;
}

// Chat mode type
type ChatMode = "teach" | "ask";

// Build URL with lesson path, user info, and optional selected context
// Mode is now handled per-message via ChatKit's composer.models picker
function getChatKitUrl(
  apiBase: string,
  lessonPath: string,
  userId: string,
  userName?: string,
  selectedContext?: string,
): string {
  const params = new URLSearchParams();
  params.set("user_id", userId);
  if (userName) {
    params.set("user_name", userName);
  }
  if (lessonPath) {
    params.set("lesson_path", lessonPath);
  }
  if (selectedContext) {
    // Send context to backend so it knows what user selected
    params.set("selected_text", selectedContext);
  }
  return `${apiBase}/chatkit?${params.toString()}`;
}

interface TeachMePanelProps {
  lessonPath: string;
}

/**
 * Inner ChatKit wrapper with user context
 */
function ChatKitWrapper({
  lessonPath,
  lessonTitle,
  apiBase,
  domainKey,
  mode = "teach",
  initialMessage,
  selectedContext,
  onSendMessage,
  onInitialMessageSent,
}: {
  lessonPath: string;
  lessonTitle: string;
  apiBase: string;
  domainKey: string;
  mode?: ChatMode;
  initialMessage?: string;
  selectedContext?: string;
  onSendMessage?: (sendFn: (text: string) => Promise<void>) => void;
  onInitialMessageSent?: () => void;
}) {
  const { session } = useAuth();

  // Use authenticated user ID if available, otherwise anonymous
  const userId = useMemo(() => {
    if (session?.user?.id) {
      return session.user.id;
    }
    return getAnonymousUserId();
  }, [session?.user?.id]);

  // Get user's display name from shared hook
  const userName = useUserDisplayName();

  const apiUrl = useMemo(
    () => getChatKitUrl(apiBase, lessonPath, userId, userName, selectedContext),
    [apiBase, lessonPath, userId, userName, selectedContext],
  );

  // Custom fetch that injects Authorization header with JWT token
  // Must use ID token (JWT format) not access token (may be opaque)
  const authenticatedFetch = useCallback(
    async (input: RequestInfo | URL, options?: RequestInit) => {
      const token = localStorage.getItem("ainative_id_token");

      const response = await fetch(input, {
        ...options,
        headers: {
          ...options?.headers,
          ...(token ? { Authorization: `Bearer ${token}` } : {}),
          "X-User-ID": userId,
          ...(userName ? { "X-User-Name": userName } : {}),
        },
      });

      return response;
    },
    [userId, userName],
  );

  const { control, sendUserMessage } = useChatKit({
    api: {
      url: apiUrl,
      domainKey,
      fetch: authenticatedFetch,
    },
    composer: {
      placeholder: selectedContext
        ? "Type your question about the selected text..."
        : mode === "teach"
          ? "Ask me anything about this lesson..."
          : "Ask a quick question...",
      attachments: { enabled: false },
      // Model picker for mode selection - appears as dropdown in composer
      // Backend reads selected mode from inference_options.model
      // Set default based on which button user clicked (mode prop)
      models: [
        {
          id: "teach",
          label: "Teach Me",
          description:
            "Socratic tutoring with questions to check understanding",
          default: mode === "teach",
        },
        {
          id: "ask",
          label: "Quick Ask",
          description: "Direct answers without follow-up questions",
          default: mode === "ask",
        },
      ],
    },
    startScreen: {
      greeting:
        mode === "teach"
          ? `Let's explore ${lessonTitle}`
          : selectedContext
            ? `Ask about your selection`
            : `Quick answers about ${lessonTitle}`,
      prompts:
        mode === "teach"
          ? [
              {
                icon: "circle-question",
                label: "What should I understand?",
                prompt: selectedContext
                  ? `Regarding this text: "${selectedContext.slice(0, 200)}"\n\nWhat are the key things I should understand from this? Ask me questions to check my understanding.`
                  : "What are the key things I should understand from this lesson? Ask me questions to check my understanding.",
              },
              {
                icon: "lightbulb",
                label: "Walk me through it",
                prompt: selectedContext
                  ? `Regarding this text: "${selectedContext.slice(0, 200)}"\n\nWalk me through this step by step. Pause to ask if I understand before moving on.`
                  : "Walk me through the main concept step by step. Pause to ask if I understand before moving on.",
              },
              {
                icon: "circle-question",
                label: "Help me think about this",
                prompt: selectedContext
                  ? `Regarding this text: "${selectedContext.slice(0, 200)}"\n\nHelp me think through this. What questions should I be asking myself?`
                  : "Help me think through this topic. What questions should I be asking myself?",
              },
              {
                icon: "lightbulb",
                label: "Quiz me",
                prompt: selectedContext
                  ? `Regarding this text: "${selectedContext.slice(0, 200)}"\n\nQuiz me on this to test my understanding. Ask one question at a time.`
                  : "Quiz me on this topic to test my understanding. Ask one question at a time.",
              },
            ]
          : [
              {
                icon: "circle-question",
                label: "Quick summary",
                prompt: selectedContext
                  ? "Summarize the highlighted text in 2-3 sentences."
                  : "Give me a quick summary in 2-3 sentences",
              },
              {
                icon: "lightbulb",
                label: "Define this concept",
                prompt: selectedContext
                  ? "Define the highlighted text briefly."
                  : "Define this concept briefly",
              },
            ],
    },
  });

  // Expose sendUserMessage to parent for Ask button
  useEffect(() => {
    if (onSendMessage && sendUserMessage) {
      onSendMessage(async (text: string) => {
        await sendUserMessage({ text, newThread: false });
      });
    }
  }, [onSendMessage, sendUserMessage]);

  // Send initial message if provided (for Ask feature or auto-start teach mode)
  // Calls onInitialMessageSent callback to clear the message after sending
  useEffect(() => {
    if (initialMessage && sendUserMessage) {
      sendUserMessage({ text: initialMessage, newThread: true }).then(() => {
        if (onInitialMessageSent) {
          onInitialMessageSent();
        }
      });
    }
  }, [initialMessage, sendUserMessage, onInitialMessageSent]);

  // Users type "A" or "B" to answer - this is handled by the chat input

  return (
    <div className={styles.chatWrapper}>
      <ChatKit control={control} className={styles.chatKit} />
    </div>
  );
}

export function TeachMePanel({ lessonPath }: TeachMePanelProps) {
  const { siteConfig } = useDocusaurusContext();
  const {
    isOpen,
    closePanel,
    openPanel,
    mode,
    setMode,
  } = useStudyMode();
  const { session } = useAuth();
  const [chatKey, setChatKey] = useState(0);
  // Mode is now managed by context (useStudyMode)
  const [initialMessage, setInitialMessage] = useState<string | undefined>();

  // Selected context - text user selected before clicking Ask
  const [selectedContext, setSelectedContext] = useState<string | undefined>();

  // Text selection state for Ask feature
  const [selectedText, setSelectedText] = useState("");
  const [selectionPosition, setSelectionPosition] = useState<{
    x: number;
    y: number;
  } | null>(null);

  // Auth check
  const isLoggedIn = !!session?.user;

  // Auth config for login redirect
  const authUrl = siteConfig.customFields?.authUrl as string | undefined;
  const oauthClientId = siteConfig.customFields?.oauthClientId as
    | string
    | undefined;

  // Login redirect handler for non-logged-in users
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

  // Get Study Mode API URL from Docusaurus config
  const studyModeApiUrl =
    (siteConfig.customFields?.studyModeApiUrl as string) ||
    "http://localhost:8000";

  // Get ChatKit domain key from config (register at OpenAI for production)
  const chatkitDomainKey =
    (siteConfig.customFields?.chatkitDomainKey as string)?.trim() ||
    "domain_pk_localhost_dev";

  // Extract lesson title for personalized greeting
  const lessonTitle = useMemo(() => {
    const parts = lessonPath.split("/");
    const lastPart = parts[parts.length - 1] || "this lesson";
    // Convert kebab-case to title case, remove numeric prefixes
    return lastPart
      .replace(/^\d+-/, "")
      .replace(/-/g, " ")
      .replace(/\b\w/g, (c) => c.toUpperCase());
  }, [lessonPath]);

  // Track if we've auto-started teach mode for this chat session
  const [hasAutoStarted, setHasAutoStarted] = useState(false);

  // Auto-start Socratic conversation when panel opens in teach mode
  // Backend auto-deletes the trigger so AI greeting appears first
  useEffect(() => {
    if (isOpen && mode === "teach" && !initialMessage && !hasAutoStarted) {
      setInitialMessage("\u200B"); // Zero-width space trigger
      setHasAutoStarted(true);
    }
  }, [isOpen, mode, initialMessage, hasAutoStarted]);

  // Reset auto-start flag when chat key changes (new chat) or mode changes
  useEffect(() => {
    setHasAutoStarted(false);
  }, [chatKey]);

  // Handle text selection for Ask feature
  const handleSelection = useCallback(() => {
    const selection = window.getSelection();
    if (!selection || selection.rangeCount === 0) {
      setSelectedText("");
      setSelectionPosition(null);
      return;
    }

    const text = selection.toString().trim();
    if (text.length > 0 && text.length < 5000) {
      // Allow longer selections (up to ~5000 chars / several paragraphs)
      setSelectedText(text);
      const range = selection.getRangeAt(0);
      const rect = range.getBoundingClientRect();
      // Position button above selection
      setSelectionPosition({
        x: rect.left + rect.width / 2,
        y: rect.top - 10 + window.scrollY,
      });
    } else {
      setSelectedText("");
      setSelectionPosition(null);
    }
  }, []);

  // Listen for text selection
  useEffect(() => {
    document.addEventListener("selectionchange", handleSelection);
    document.addEventListener("mouseup", handleSelection);
    return () => {
      document.removeEventListener("selectionchange", handleSelection);
      document.removeEventListener("mouseup", handleSelection);
    };
  }, [handleSelection]);

  // Handle Ask button click - auto-send selected text as message
  const handleAskSelectedText = useCallback(() => {
    if (!selectedText) return;

    // Pass context to backend URL and auto-send as user message
    setSelectedContext(selectedText);
    setMode("ask");
    setInitialMessage(selectedText);
    setChatKey((prev) => prev + 1);
    openPanel();

    // Clear text selection
    setSelectedText("");
    setSelectionPosition(null);
    window.getSelection()?.removeAllRanges();
  }, [selectedText, openPanel]);

  // Clear selected context
  const handleClearContext = useCallback(() => {
    setSelectedContext(undefined);
  }, []);

  return (
    <>
      {/* Floating Ask button appears when text is selected - shows for all users */}
      {selectedText && selectionPosition && !isOpen && (
        <div
          className={`${styles.askButton} ${!isLoggedIn ? styles.askButtonLocked : ""}`}
          style={{
            position: "absolute",
            left: `${selectionPosition.x}px`,
            top: `${selectionPosition.y}px`,
            transform: "translateX(-50%) translateY(-100%)",
            zIndex: 9999,
          }}
          onClick={isLoggedIn ? handleAskSelectedText : handleLoginRedirect}
          title={isLoggedIn ? "Ask about this text" : "Sign in to ask"}
        >
          {!isLoggedIn && <Lock className="h-3 w-3" />}
          <span>Ask</span>
        </div>
      )}

      <Sheet
        open={isLoggedIn && isOpen}
        onOpenChange={(open) => {
          if (!open) {
            closePanel();
            // Clear state when panel closes
            setInitialMessage(undefined);
            setSelectedContext(undefined);
            // Reset to teach mode as default
            setMode("teach");
          }
        }}
      >
        <SheetContent
          side="right"
          className="w-full sm:max-w-md md:max-w-lg p-0 flex flex-col"
          hideCloseButton
        >
          {/* Mobile close button - top left corner */}
          <SheetClose className={styles.mobileCloseButton}>
            <X className="h-5 w-5" />
            <span className="sr-only">Close</span>
          </SheetClose>

          <div className={styles.chatContainer}>
            <ChatKitWrapper
              key={`${lessonPath}-${chatKey}-${mode}`}
              lessonPath={lessonPath}
              lessonTitle={lessonTitle}
              apiBase={studyModeApiUrl}
              domainKey={chatkitDomainKey}
              mode={mode}
              initialMessage={initialMessage}
              onInitialMessageSent={() => setInitialMessage(undefined)}
              selectedContext={selectedContext}
            />
            {selectedContext && (
              <div className={styles.contextChip}>
                <div className={styles.contextLabel}>Asking about</div>
                <div className={styles.contextText}>
                  {selectedContext.length > 100
                    ? selectedContext.slice(0, 100) + "…"
                    : selectedContext}
                </div>
                <button
                  className={styles.contextDismiss}
                  onClick={handleClearContext}
                  aria-label="Clear context"
                >
                  <X className="h-3.5 w-3.5" />
                </button>
              </div>
            )}
          </div>
        </SheetContent>
      </Sheet>
    </>
  );
}

export default TeachMePanel;
