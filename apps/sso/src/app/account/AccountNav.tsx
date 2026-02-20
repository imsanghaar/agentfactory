"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const navItems = [
  { href: "/account/profile", label: "Profile" },
  { href: "/account/organizations", label: "Organizations" },
];

export function AccountNav() {
  const pathname = usePathname();

  return (
    <nav className="max-w-5xl mx-auto px-4">
      <div className="flex items-center gap-1 border-t border-slate-200/50 pt-2 pb-1">
        {navItems.map((item) => {
          const isActive = pathname.startsWith(item.href);
          return (
            <Link
              key={item.href}
              href={item.href}
              className={`px-4 py-2 text-sm font-medium rounded-lg transition-colors ${
                isActive
                  ? "bg-primary/10 text-primary"
                  : "text-slate-600 hover:text-slate-900 hover:bg-slate-100"
              }`}
            >
              {item.label}
            </Link>
          );
        })}
      </div>
    </nav>
  );
}
