"use client";

import * as React from "react";
import { Play, Lock } from "lucide-react";
import { cn } from "@/lib/utils";
import { useAuth } from "@/contexts/AuthContext";
import { getOAuthAuthorizationUrl } from "@/lib/auth-client";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";

export interface ChapterVideoButtonProps {
  onClick?: () => void;
  className?: string;
}

export function ChapterVideoButton({ onClick, className }: ChapterVideoButtonProps) {
  const { session, isLoading } = useAuth();
  const { siteConfig } = useDocusaurusContext();
  const [isHovering, setIsHovering] = React.useState(false);

  // Auth config from site config
  const authUrl = siteConfig.customFields?.authUrl as string | undefined;
  const oauthClientId = siteConfig.customFields?.oauthClientId as string | undefined;

  // Check if user is logged in
  const isLoggedIn = !isLoading && !!session?.user;

  const handleClick = () => {
    if (!isLoggedIn) {
      // Blocked - user must sign up first
      return;
    }
    onClick?.();
  };

  const handleLoginRedirect = async (e: React.MouseEvent) => {
    e.stopPropagation();
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
  };

  return (
    <div
      className="relative inline-block doc-page-actions-tooltip-wrapper"
      onMouseEnter={() => !isLoggedIn && setIsHovering(true)}
      onMouseLeave={() => setIsHovering(false)}
    >
      <button
        onClick={handleClick}
        className={cn(
          "doc-page-actions-video relative",
          !isLoggedIn && "doc-page-actions-video--locked",
          className
        )}
        aria-label={isLoggedIn ? "Play video" : "Sign up to access watch mode"}
      >
        {isLoggedIn ? (
          <>
            <Play className="h-4 w-4 fill-current" />
            <span>Play</span>
          </>
        ) : (
          <>
            <Lock className="h-4 w-4" />
            <span>Play</span>
          </>
        )}
      </button>

      {/* Tooltip - shown when locked and hovering */}
      {!isLoggedIn && (
        <div
          className={cn(
            "doc-page-actions-tooltip",
            isHovering && "doc-page-actions-tooltip--visible"
          )}
          role="tooltip"
        >
          <span>Sign up to access watch mode</span>
          <button
            onClick={handleLoginRedirect}
            className="doc-page-actions-tooltip-link"
          >
            Sign up
          </button>
        </div>
      )}
    </div>
  );
}
