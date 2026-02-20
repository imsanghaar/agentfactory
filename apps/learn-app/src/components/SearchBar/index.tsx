import React, { useState, useEffect, useMemo } from 'react';
import { useHistory } from '@docusaurus/router';
import { searchContent } from '@/lib/search-utils';
import {
  CommandDialog,
  CommandInput,
  CommandList,
  CommandEmpty,
  CommandGroup,
  CommandItem,
} from "@/components/ui/command";
import { Button } from "@/components/ui/button";
import { Search, Loader2, FileText, Hash } from "lucide-react";
import { cn } from "@/lib/utils";

// Detect OS for keyboard shortcut display
const isMac = typeof navigator !== 'undefined' && /Mac|iPod|iPhone|iPad/.test(navigator.platform);

export function SearchBar({ enableShortcut = true }: { enableShortcut?: boolean }) {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const history = useHistory();

  // Keyboard shortcut display
  const shortcutKey = isMac ? '⌘' : 'Ctrl';

  // Toggle Command Palette with Cmd+K / Ctrl+K
  useEffect(() => {
    if (!enableShortcut) return;
    const down = (e: KeyboardEvent) => {
      if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
        e.preventDefault();
        setOpen((open) => !open);
      }
    };
    document.addEventListener("keydown", down);
    return () => document.removeEventListener("keydown", down);
  }, [enableShortcut]);

  // Clear query when modal closes
  const handleOpenChange = (isOpen: boolean) => {
    setOpen(isOpen);
    if (!isOpen) {
      setQuery('');
      setResults([]);
    }
  };

  // Search Logic (Debounced)
  useEffect(() => {
    if (!query.trim()) {
      setResults([]);
      setLoading(false);
      return;
    }

    setLoading(true);
    const timeoutId = setTimeout(async () => {
      try {
        const searchResults = await searchContent(query);
        // Limit to 8 results for cleaner UI
        setResults(searchResults.slice(0, 8));
      } catch (error) {
        console.error("Search failed:", error);
        setResults([]);
      } finally {
        setLoading(false);
      }
    }, 300);

    return () => clearTimeout(timeoutId);
  }, [query]);

  const handleSelect = (url: string) => {
    handleOpenChange(false);
    history.push(url);
  };

  // Determine which state to show
  const showEmptyHint = !query.trim();
  const showLoading = loading && query.trim();
  const showNoResults = !loading && query.trim() && results.length === 0;
  const showResults = !loading && results.length > 0;

  return (
    <>
      <Button
        variant="outline"
        className={cn(
          "relative h-10 w-full justify-start text-sm text-muted-foreground sm:pr-12"
        )}
        onClick={() => setOpen(true)}
      >
        <Search className="mr-2 h-4 w-4" />
        <span className="hidden lg:inline-flex">Search Book...</span>
        <span className="inline-flex lg:hidden">Search...</span>
        <kbd className="pointer-events-none absolute right-1.5 top-1/2 -translate-y-1/2 hidden h-5 select-none items-center gap-1 rounded border bg-muted px-1.5 font-mono text-[10px] font-medium opacity-100 sm:flex">
          <span className="text-xs">{shortcutKey}</span>K
        </kbd>
      </Button>
      <CommandDialog open={open} onOpenChange={handleOpenChange}>
        <CommandInput
          placeholder="Search the book..."
          value={query}
          onValueChange={setQuery}
        />
        <CommandList className="min-h-[200px]">
          {/* Empty state - show hint when no query */}
          {showEmptyHint && (
            <div className="py-14 text-center">
              <Search className="mx-auto h-10 w-10 text-muted-foreground/40 mb-4" />
              <p className="text-sm text-muted-foreground">
                Type to search documentation
              </p>
              <p className="text-xs text-muted-foreground/60 mt-1">
                Press <kbd className="px-1.5 py-0.5 rounded bg-muted text-xs font-mono">{shortcutKey}+K</kbd> anytime to open
              </p>
            </div>
          )}

          {/* Loading state */}
          {showLoading && (
            <div className="py-14 text-center">
              <Loader2 className="mx-auto h-8 w-8 text-muted-foreground animate-spin mb-4" />
              <p className="text-sm text-muted-foreground">Searching...</p>
            </div>
          )}

          {/* No results state */}
          {showNoResults && (
            <CommandEmpty>No results found for "{query}"</CommandEmpty>
          )}

          {/* Results */}
          {showResults && (
            <CommandGroup heading="Results">
              {results.map((result, index) => (
                <CommandItem
                  key={`${result.url}-${index}`}
                  value={result.title || result.content}
                  onSelect={() => handleSelect(result.url)}
                  className="cursor-pointer"
                >
                  {result.type === 'heading' ? (
                    <Hash className="mr-2 h-4 w-4 text-muted-foreground" />
                  ) : (
                    <FileText className="mr-2 h-4 w-4 text-muted-foreground" />
                  )}
                  <div className="flex flex-col gap-0.5 overflow-hidden">
                    <span className="truncate font-medium">{result.title}</span>
                    {result.type && (
                      <span className="text-xs text-muted-foreground capitalize truncate">
                        {result.type}
                      </span>
                    )}
                  </div>
                </CommandItem>
              ))}
            </CommandGroup>
          )}
        </CommandList>
      </CommandDialog>
    </>
  );
}
