import React from "react";

// Stub for @docusaurus/Link
export const Link = ({
  children,
  to,
  ...props
}: {
  children: React.ReactNode;
  to?: string;
  [key: string]: unknown;
}) => React.createElement("a", { href: to, ...props }, children);

// Stub for @docusaurus/useBaseUrl
export function useBaseUrl(url: string): string {
  return url;
}

// Stub for @docusaurus/BrowserOnly
export function BrowserOnly({ children }: { children: () => React.ReactNode }) {
  return React.createElement(React.Fragment, null, children());
}

export default Link;
