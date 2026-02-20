/**
 * Pyodide Context Provider
 * Provides Pyodide instance and loading state to all child components
 * Uses LAZY INITIALIZATION - Pyodide only loads when init() is called
 *
 * PERFORMANCE FIX (Jan 2026): Changed from eager to lazy loading.
 * Previously, Pyodide initialized on every page (including homepage),
 * causing 5+ second Total Blocking Time. Now initializes only when
 * a component actually needs Python execution.
 */

import React, {
  createContext,
  useContext,
  useState,
  useMemo,
  useCallback,
} from "react";
import { PyodideRunner } from "@/lib/pyodide-singleton";

/**
 * Context value type
 */
interface PyodideContextType {
  pyodide: PyodideRunner;
  isLoading: boolean;
  error: Error | null;
  /** Call this to initialize Pyodide when you need it */
  init: () => Promise<void>;
  /** Whether init() has been called */
  isInitialized: boolean;
}

/**
 * Create the context
 */
const PyodideContext = createContext<PyodideContextType | null>(null);

/**
 * Provider component - wrap your app with this to enable Pyodide
 * Usage: <PyodideProvider><App /></PyodideProvider>
 *
 * NOTE: This provider does NOT auto-initialize Pyodide.
 * Components must call init() when they need Python execution.
 */
export const PyodideProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const [isInitialized, setIsInitialized] = useState(false);
  const pyodide = PyodideRunner.getInstance();

  /**
   * Lazy initialize Pyodide - only called when needed
   */
  const init = useCallback(async () => {
    // Skip if already initialized or currently loading
    if (isInitialized || isLoading) return;

    setIsLoading(true);
    try {
      await pyodide.init();
      setIsInitialized(true);
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err : new Error(String(err)));
    } finally {
      setIsLoading(false);
    }
  }, [pyodide, isInitialized, isLoading]);

  // Memoize the context value to prevent unnecessary re-renders of consumers
  const contextValue = useMemo(
    () => ({ pyodide, isLoading, error, init, isInitialized }),
    [pyodide, isLoading, error, init, isInitialized],
  );

  return (
    <PyodideContext.Provider value={contextValue}>
      {children}
    </PyodideContext.Provider>
  );
};

/**
 * Custom hook to use Pyodide in any component
 * Must be used within a PyodideProvider
 *
 * IMPORTANT: Call init() before using pyodide.run()
 * Example:
 *   const { pyodide, init, isLoading, isInitialized } = usePyodide();
 *   useEffect(() => { init(); }, [init]);  // Initialize on mount
 */
export const usePyodide = (): PyodideContextType => {
  const context = useContext(PyodideContext);

  if (!context) {
    throw new Error(
      "usePyodide must be used within a PyodideProvider. " +
        "Wrap your app with <PyodideProvider> in Root.tsx",
    );
  }

  return context;
};
