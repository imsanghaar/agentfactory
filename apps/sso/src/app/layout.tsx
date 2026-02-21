import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Imam Sanghaar SSO",
  description: "Sign in or create an account for Imam Sanghaar",
  icons: {
    icon: "/new_favicon.png",
    apple: "/new_favicon.png",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="light">
      <body className="antialiased bg-gray-50 min-h-screen">
        {children}
      </body>
    </html>
  );
}
