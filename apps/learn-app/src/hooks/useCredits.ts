import { useState, useEffect, useCallback } from "react";
import { useAuth } from "@/contexts/AuthContext";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";

interface UseCreditsResult {
  balanceUsd: number | null;
  balanceFormatted: string | null;
  isLoading: boolean;
  isExpired: boolean;
  isLowBalance: boolean;
  error: string | null;
  refresh: () => void;
}

const LOW_BALANCE_THRESHOLD_USD = 0.01;
const CREDITS_TO_USD_DIVISOR = 10000;

function formatUsd(usd: number): string {
  if (usd === 0) return "$0.00";
  // Show 4 decimals for amounts < $0.10 to distinguish small balances
  if (usd < 0.1) return `$${usd.toFixed(4)}`;
  return `$${usd.toFixed(2)}`;
}

export function useCredits(): UseCreditsResult {
  const { session } = useAuth();
  const { siteConfig } = useDocusaurusContext();
  const meteringApiUrl =
    (siteConfig.customFields?.tokenMeteringApiUrl as string) ||
    "http://localhost:8001";

  const [balanceUsd, setBalanceUsd] = useState<number | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isExpired, setIsExpired] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchBalance = useCallback(async () => {
    if (typeof window === "undefined") return;

    const token = localStorage.getItem("ainative_id_token");
    if (!token) return;

    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch(`${meteringApiUrl}/api/v1/balance`, {
        headers: { Authorization: `Bearer ${token}` },
      });

      if (response.status === 404) {
        // Account not yet created — don't show balance
        setBalanceUsd(null);
        setIsExpired(false);
        return;
      }

      if (!response.ok) {
        throw new Error(`Balance fetch failed (${response.status})`);
      }

      const data = await response.json();
      const usd = (data.effective_balance ?? 0) / CREDITS_TO_USD_DIVISOR;
      setBalanceUsd(usd);
      setIsExpired(data.is_expired ?? false);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to fetch balance");
      setBalanceUsd(null);
    } finally {
      setIsLoading(false);
    }
  }, [meteringApiUrl]);

  // Fetch on mount when authenticated
  useEffect(() => {
    if (session?.user) {
      fetchBalance();
    }
  }, [session?.user, fetchBalance]);

  return {
    balanceUsd,
    balanceFormatted: balanceUsd !== null ? formatUsd(balanceUsd) : null,
    isLoading,
    isExpired,
    isLowBalance: balanceUsd !== null && balanceUsd < LOW_BALANCE_THRESHOLD_USD,
    error,
    refresh: fetchBalance,
  };
}
