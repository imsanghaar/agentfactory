/**
 * StudyModeContext
 *
 * Global state for Interactive Study Mode
 * Manages panel visibility, current mode, and conversation state
 *
 * State is client-side only (sessionStorage for persistence)
 */

import React, {
  createContext,
  useContext,
  useState,
  useCallback,
  useEffect,
} from "react";

// =============================================================================
// Types
// =============================================================================

export type ChatMode = "teach" | "ask";

export interface Message {
  role: "user" | "assistant";
  content: string;
  timestamp: string;
}

export interface ConversationState {
  messages: Message[];
  lessonPath: string;
}

export interface StudyModeState {
  isOpen: boolean;
  mode: ChatMode;
  conversations: Record<string, ConversationState>; // Keyed by lessonPath
  isLoading: boolean;
  error: string | null;
}

export interface StudyModeContextValue extends StudyModeState {
  // Panel controls
  openPanel: () => void;
  closePanel: () => void;
  togglePanel: () => void;

  // Mode controls
  setMode: (mode: ChatMode) => void;

  // Conversation controls
  getCurrentConversation: (lessonPath: string) => ConversationState;
  addMessage: (lessonPath: string, message: Message) => void;
  clearConversation: (lessonPath: string) => void;

  // Loading/error state
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
}

// =============================================================================
// Context
// =============================================================================

const StudyModeContext = createContext<StudyModeContextValue | null>(null);

// =============================================================================
// Storage helpers
// =============================================================================

const STORAGE_KEY = "study-mode-state";

function loadFromStorage(): Partial<StudyModeState> {
  if (typeof window === "undefined") return {};

  try {
    const stored = sessionStorage.getItem(STORAGE_KEY);
    if (stored) {
      const parsed = JSON.parse(stored);
      return {
        mode: parsed.mode || "teach",
        conversations: parsed.conversations || {},
      };
    }
  } catch {
    // Ignore storage errors
  }
  return {};
}

function saveToStorage(state: Partial<StudyModeState>): void {
  if (typeof window === "undefined") return;

  try {
    sessionStorage.setItem(
      STORAGE_KEY,
      JSON.stringify({
        mode: state.mode,
        conversations: state.conversations,
      }),
    );
  } catch {
    // Ignore storage errors
  }
}

// =============================================================================
// Provider
// =============================================================================

export function StudyModeProvider({ children }: { children: React.ReactNode }) {
  const [state, setState] = useState<StudyModeState>(() => {
    const stored = loadFromStorage();
    return {
      isOpen: false,
      mode: stored.mode || "teach",
      conversations: stored.conversations || {},
      isLoading: false,
      error: null,
    };
  });

  // Persist to sessionStorage on state change
  useEffect(() => {
    saveToStorage({
      mode: state.mode,
      conversations: state.conversations,
    });
  }, [state.mode, state.conversations]);

  // Panel controls
  const openPanel = useCallback(() => {
    setState((s) => ({ ...s, isOpen: true, error: null }));
  }, []);

  const closePanel = useCallback(() => {
    setState((s) => ({ ...s, isOpen: false }));
  }, []);

  const togglePanel = useCallback(() => {
    setState((s) => ({ ...s, isOpen: !s.isOpen, error: null }));
  }, []);

  // Mode controls
  const setMode = useCallback((mode: ChatMode) => {
    setState((s) => ({ ...s, mode }));
  }, []);

  // Conversation controls
  const getCurrentConversation = useCallback(
    (lessonPath: string): ConversationState => {
      return state.conversations[lessonPath] || { messages: [], lessonPath };
    },
    [state.conversations],
  );

  const addMessage = useCallback((lessonPath: string, message: Message) => {
    setState((s) => {
      const existing = s.conversations[lessonPath] || {
        messages: [],
        lessonPath,
      };
      return {
        ...s,
        conversations: {
          ...s.conversations,
          [lessonPath]: {
            ...existing,
            messages: [...existing.messages, message],
          },
        },
      };
    });
  }, []);

  const clearConversation = useCallback((lessonPath: string) => {
    setState((s) => {
      const { [lessonPath]: _, ...rest } = s.conversations;
      return {
        ...s,
        conversations: rest,
        error: null,
      };
    });
  }, []);

  // Loading/error state
  const setLoading = useCallback((isLoading: boolean) => {
    setState((s) => ({ ...s, isLoading }));
  }, []);

  const setError = useCallback((error: string | null) => {
    setState((s) => ({ ...s, error, isLoading: false }));
  }, []);

  const value: StudyModeContextValue = {
    ...state,
    openPanel,
    closePanel,
    togglePanel,
    setMode,
    getCurrentConversation,
    addMessage,
    clearConversation,
    setLoading,
    setError,
  };

  return (
    <StudyModeContext.Provider value={value}>
      {children}
    </StudyModeContext.Provider>
  );
}

// =============================================================================
// Hook
// =============================================================================

export function useStudyMode(): StudyModeContextValue {
  const context = useContext(StudyModeContext);
  if (!context) {
    throw new Error("useStudyMode must be used within a StudyModeProvider");
  }
  return context;
}

// Export context for advanced use cases
export { StudyModeContext };
