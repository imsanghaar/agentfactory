import React, { useState, useEffect } from "react";
import { useAuth } from "@/contexts/AuthContext";
import { getOAuthAuthorizationUrl } from "@/lib/auth-client";
import { getHomeUrl } from "@/lib/url-utils";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import {
  User,
  LogOut,
  Settings,
  RefreshCw,
  Trophy,
  Zap,
  Flame,
} from "lucide-react";
import { useCredits } from "@/hooks/useCredits";
import { useProgress } from "@/contexts/ProgressContext";
import Link from "@docusaurus/Link";
import XPCounter from "@/components/progress/XPCounter";

export function NavbarAuth() {
  const { session, isLoading, signOut, refreshUserData } = useAuth();
  const { siteConfig } = useDocusaurusContext();
  const credits = useCredits();
  const { progress } = useProgress();
  const authUrl =
    (siteConfig.customFields?.authUrl as string) || "http://localhost:3001";
  const oauthClientId =
    (siteConfig.customFields?.oauthClientId as string) ||
    "agent-factory-public-client";

  // OAuth config
  const oauthConfig = {
    authUrl,
    clientId: oauthClientId,
  };

  const handleSignIn = async () => {
    const authorizationUrl = await getOAuthAuthorizationUrl(
      "signin",
      oauthConfig,
    );
    await new Promise((resolve) => setTimeout(resolve, 50));
    window.location.href = authorizationUrl;
  };

  const handleSignUp = async () => {
    if (session?.user) {
      const homeUrl = getHomeUrl();
      window.location.href = `${homeUrl}docs/preface-agent-native`;
      return;
    }
    const oauthUrl = await getOAuthAuthorizationUrl("signup", oauthConfig);
    const signupUrl = `${authUrl}/auth/sign-up?redirect=${encodeURIComponent(oauthUrl)}`;
    window.location.href = signupUrl;
  };

  const getInitials = (name?: string, email?: string) => {
    if (name) {
      return name
        .split(" ")
        .map((n) => n[0])
        .join("")
        .toUpperCase()
        .slice(0, 2);
    }
    return email ? email[0].toUpperCase() : "?";
  };

  const handleEditProfile = () => {
    const currentUrl =
      typeof window !== "undefined" ? window.location.href : "";
    const profileUrl = `${authUrl}/account/profile?redirect=${encodeURIComponent(currentUrl)}`;
    localStorage.setItem("ainative_refresh_on_return", "true");
    window.location.href = profileUrl;
  };

  useEffect(() => {
    const shouldRefresh = localStorage.getItem("ainative_refresh_on_return");
    if (shouldRefresh === "true" && session?.user) {
      localStorage.removeItem("ainative_refresh_on_return");
      refreshUserData();
    }
  }, [session]);

  if (isLoading) {
    return <div className="h-9 w-9 animate-pulse rounded-full bg-muted" />;
  }

  if (session?.user) {
    const displayName = session.user.name || session.user.email.split("@")[0];
    const initials = getInitials(session.user.name, session.user.email);
    const software = session.user.softwareBackground
      ? session.user.softwareBackground.charAt(0).toUpperCase() +
        session.user.softwareBackground.slice(1)
      : null;
    const hardware = session.user.hardwareTier;
    const hardwareLabel =
      hardware === "tier1"
        ? "Windows PC"
        : hardware === "tier2"
          ? "Mac"
          : hardware === "tier3"
            ? "Linux"
            : hardware === "tier4"
              ? "Chromebook/Web"
              : hardware;

    return (
      <div className="flex items-center gap-2">
        <Link
          to="/leaderboard"
          className="flex items-center justify-center h-9 w-9 sm:w-auto sm:gap-1.5 sm:px-2.5 rounded-md border border-border bg-card hover:bg-accent transition-colors allow-rounded no-underline"
          title="Leaderboard"
          aria-label="Leaderboard"
        >
          <Trophy className="h-4 w-4 text-[oklch(0.77_0.16_70)]" />
          <span className="hidden sm:inline text-xs font-medium text-foreground">
            Leaderboard
          </span>
        </Link>
        <div className="hidden sm:block">
          <XPCounter />
        </div>
        <DropdownMenu modal={false}>
          <DropdownMenuTrigger asChild>
            <Button variant="ghost" className="relative h-9 w-9 rounded-full">
              <Avatar className="h-9 w-9">
                <AvatarFallback>{initials}</AvatarFallback>
              </Avatar>
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent className="w-56" align="end" forceMount>
            <DropdownMenuLabel className="font-normal">
              <div className="flex flex-col space-y-1">
                <p className="text-sm font-medium leading-none">
                  {displayName}
                </p>
                <p className="text-xs leading-none text-muted-foreground">
                  {session.user.email}
                </p>
              </div>
            </DropdownMenuLabel>
            <DropdownMenuSeparator />
            {(software || hardware) && (
              <>
                <div className="px-2 py-1.5 text-xs text-muted-foreground">
                  {software && <p>Software: {software}</p>}
                  {hardware && <p>Hardware: {hardwareLabel}</p>}
                </div>
                <DropdownMenuSeparator />
              </>
            )}
            {credits.isLoading && (
              <>
                <div className="px-2 py-1.5">
                  <div className="h-4 w-24 animate-pulse rounded bg-muted" />
                </div>
                <DropdownMenuSeparator />
              </>
            )}
            {!credits.isLoading && credits.balanceFormatted !== null && (
              <>
                <div className="flex items-center justify-between px-2 py-1.5 text-xs">
                  <span
                    className={
                      credits.balanceUsd === 0 || credits.isExpired
                        ? "text-destructive"
                        : credits.isLowBalance
                          ? "text-[color:var(--warning)]"
                          : "text-foreground"
                    }
                  >
                    Balance: {credits.balanceFormatted}
                  </span>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      credits.refresh();
                    }}
                    className="text-muted-foreground hover:text-foreground"
                    aria-label="Refresh balance"
                  >
                    <RefreshCw className="h-3 w-3" />
                  </button>
                </div>
                <DropdownMenuSeparator />
              </>
            )}
            {/* XP stats — always visible in dropdown (primary on mobile) */}
            {progress?.stats && (
              <>
                <div className="px-2 py-1.5">
                  <Link
                    to="/progress"
                    className="flex items-center justify-between text-xs hover:text-primary transition-colors"
                  >
                    <div className="flex items-center gap-3">
                      <span className="flex items-center gap-1">
                        <Zap
                          className="h-3.5 w-3.5 text-[oklch(0.68_0.16_142)]"
                          fill="currentColor"
                        />
                        <span className="font-semibold">
                          {progress.stats.total_xp.toLocaleString()}
                        </span>
                        <span className="text-muted-foreground">XP</span>
                      </span>
                      {progress.stats.current_streak > 0 && (
                        <span className="flex items-center gap-1">
                          <Flame
                            className="h-3.5 w-3.5 text-[oklch(0.77_0.16_77)]"
                            fill="currentColor"
                          />
                          <span className="font-semibold">
                            {progress.stats.current_streak}
                          </span>
                        </span>
                      )}
                    </div>
                    <span className="text-muted-foreground">
                      {progress.stats.rank ? `#${progress.stats.rank}` : "—"}
                    </span>
                  </Link>
                </div>
                <DropdownMenuSeparator />
              </>
            )}
            <DropdownMenuItem
              onClick={handleEditProfile}
              className="cursor-pointer"
            >
              <Settings className="mr-2 h-4 w-4" />
              <span>Edit Profile</span>
            </DropdownMenuItem>
            <DropdownMenuItem
              onClick={() => signOut()}
              className="cursor-pointer text-red-500 focus:text-red-500"
            >
              <LogOut className="mr-2 h-4 w-4" />
              <span>Sign out</span>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
    );
  }

  return (
    <div className="flex items-center gap-2">
      <Link
        to="/leaderboard"
        className="flex items-center justify-center h-9 w-9 sm:w-auto sm:gap-1.5 sm:px-2.5 rounded-md border border-border bg-card hover:bg-accent transition-colors allow-rounded no-underline"
        title="Leaderboard"
        aria-label="Leaderboard"
      >
        <Trophy className="h-4 w-4 text-[oklch(0.77_0.16_70)]" />
        <span className="hidden sm:inline text-xs font-medium text-foreground">
          Leaderboard
        </span>
      </Link>
      <Button
        variant="ghost"
        onClick={handleSignIn}
        className="hidden sm:inline-flex"
      >
        Sign In
      </Button>
      <Button onClick={handleSignUp}>Sign Up</Button>
    </div>
  );
}

export default NavbarAuth;
