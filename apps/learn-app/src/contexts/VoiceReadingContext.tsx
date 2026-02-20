/**
 * VoiceReadingContext
 * 
 * Provides word-by-word reading with speech synthesis and word highlighting.
 * Tracks the currently spoken word and provides methods to control playback.
 * Supports pause/resume and real-time volume/speed changes that continue from current word.
 */

import React, { createContext, useContext, useState, useCallback, useRef, useEffect } from "react";

interface VoiceReadingContextType {
    // Playback state
    isPlaying: boolean;
    isPaused: boolean;
    activeBlockIndex: number;
    currentWordIndex: number;

    // Voice settings
    availableVoices: SpeechSynthesisVoice[];
    selectedVoiceIndex: number;
    playbackRate: number;
    volume: number;

    // Methods
    toggleSpeech: () => void;
    pauseSpeech: () => void;
    resumeSpeech: () => void;
    setPlaybackRate: (rate: number) => void;
    setVoice: (index: number) => void;
    setVolume: (vol: number) => void;
    stopSpeech: () => void;
}

const VoiceReadingContext = createContext<VoiceReadingContextType | null>(null);

export function useVoiceReading() {
    const context = useContext(VoiceReadingContext);
    if (!context) {
        throw new Error("useVoiceReading must be used within VoiceReadingProvider");
    }
    return context;
}

export function useVoiceReadingOptional() {
    return useContext(VoiceReadingContext);
}

interface WordBoundary {
    index: number;
    start: number;
    end: number;
    word: string;
}

interface TextBlock {
    element: Element;
    text: string;
    originalHtml: string;
    wordBoundaries: WordBoundary[];
}

export function VoiceReadingProvider({ children }: { children: React.ReactNode }) {
    const [isPlaying, setIsPlaying] = useState(false);
    const [isPaused, setIsPaused] = useState(false);
    const [activeBlockIndex, setActiveBlockIndex] = useState(-1);
    const [currentWordIndex, setCurrentWordIndex] = useState(-1);

    const [availableVoices, setAvailableVoices] = useState<SpeechSynthesisVoice[]>([]);
    const [selectedVoiceIndex, setSelectedVoiceIndex] = useState(0);
    const [playbackRate, setPlaybackRateState] = useState(1.0);
    const [volume, setVolumeState] = useState(1.0);

    const blocksRef = useRef<TextBlock[]>([]);

    // Use refs for current settings
    const playbackRateRef = useRef(1.0);
    const volumeRef = useRef(1.0);
    const selectedVoiceRef = useRef<SpeechSynthesisVoice | null>(null);

    // Track current position with refs
    const activeBlockIndexRef = useRef(-1);
    const currentWordIndexRef = useRef(-1);

    // Synchronous pause guard — checked in onboundary and fallback to skip updates while paused
    const isPausedRef = useRef(false);

    // Chrome keepalive: re-calls pause() every 10s to prevent 15-second auto-resume
    const chromeKeepAliveRef = useRef<ReturnType<typeof setInterval> | null>(null);

    // Unique ID for each utterance to prevent stale callbacks
    const utteranceIdRef = useRef(0);
    const currentUtteranceIdRef = useRef(0);

    // Timer-based fallback for browsers that don't fire onboundary (Safari, iOS, etc.)
    const fallbackTimerRef = useRef<ReturnType<typeof setInterval> | null>(null);
    const fallbackDelayTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
    const boundaryFiredRef = useRef(false);

    /**
     * Clear all fallback timers to prevent memory leaks and orphaned intervals.
     * Centralized cleanup function used across all handlers.
     * Empty dependency array is safe: only accesses stable refs, not state or props.
     */
    const clearFallbackTimers = useCallback(() => {
        if (fallbackTimerRef.current) {
            clearInterval(fallbackTimerRef.current);
            fallbackTimerRef.current = null;
        }
        if (fallbackDelayTimerRef.current) {
            clearTimeout(fallbackDelayTimerRef.current);
            fallbackDelayTimerRef.current = null;
        }
    }, []);

    // Load voices on mount
    useEffect(() => {
        if (typeof window === "undefined" || !window.speechSynthesis) return;

        const loadVoices = () => {
            const voices = window.speechSynthesis.getVoices();
            if (voices.length > 0) {
                setAvailableVoices(voices);
                const defaultIndex = voices.findIndex(v =>
                    v.name.includes("Google US English") ||
                    v.name.includes("Microsoft David") ||
                    v.name.includes("Alex")
                );
                const idx = defaultIndex >= 0 ? defaultIndex : 0;
                setSelectedVoiceIndex(idx);
                selectedVoiceRef.current = voices[idx];
            }
        };

        loadVoices();
        window.speechSynthesis.onvoiceschanged = loadVoices;

        return () => {
            window.speechSynthesis.cancel();
            setIsPlaying(false);
            // Clear all timers on unmount
            clearFallbackTimers();
        };
    }, [clearFallbackTimers]);

    const selectedVoice = availableVoices[selectedVoiceIndex] || null;

    // Keep refs in sync
    useEffect(() => {
        playbackRateRef.current = playbackRate;
    }, [playbackRate]);

    useEffect(() => {
        volumeRef.current = volume;
    }, [volume]);

    useEffect(() => {
        selectedVoiceRef.current = selectedVoice;
    }, [selectedVoice]);

    useEffect(() => {
        activeBlockIndexRef.current = activeBlockIndex;
    }, [activeBlockIndex]);

    useEffect(() => {
        currentWordIndexRef.current = currentWordIndex;
    }, [currentWordIndex]);

    useEffect(() => {
        isPausedRef.current = isPaused;
    }, [isPaused]);

    const parseArticleContent = useCallback((): TextBlock[] => {
        const article = document.querySelector("article");
        if (!article) return [];

        const blockSelectors = "p, h1, h2, h3, h4, h5, h6, li, blockquote > p, blockquote";
        const elements = article.querySelectorAll(blockSelectors);

        const blocks: TextBlock[] = [];

        elements.forEach((element) => {
            const text = element.textContent?.trim() || "";
            if (!text) return;

            if (element.tagName === "P" && element.parentElement?.tagName === "BLOCKQUOTE") {
                return;
            }

            const wordBoundaries: WordBoundary[] = [];
            const regex = /\S+/g;
            let match;
            let wordIdx = 0;
            while ((match = regex.exec(text)) !== null) {
                wordBoundaries.push({
                    index: wordIdx++,
                    start: match.index,
                    end: match.index + match[0].length,
                    word: match[0]
                });
            }

            if (wordBoundaries.length > 0) {
                element.setAttribute("data-voice-block", String(blocks.length));
                blocks.push({ element, text, originalHtml: element.innerHTML, wordBoundaries });
            }
        });

        return blocks;
    }, []);

    const wrapWordsInBlock = useCallback((block: TextBlock, blockIndex: number) => {
        const { element, text } = block;
        const words = text.match(/\S+/g) || [];
        const fragment = document.createDocumentFragment();

        words.forEach((word, idx) => {
            const span = document.createElement("span");
            span.className = "voice-word";
            span.setAttribute("data-word-index", String(idx));
            span.setAttribute("data-block-index", String(blockIndex));
            span.textContent = word + " ";
            fragment.appendChild(span);
        });

        element.innerHTML = "";
        element.appendChild(fragment);
    }, []);

    const unwrapWords = useCallback(() => {
        const wrappedBlocks = document.querySelectorAll("[data-voice-block]");
        wrappedBlocks.forEach(block => {
            const stored = blocksRef.current.find((_, idx) =>
                block.getAttribute("data-voice-block") === String(idx)
            );

            if (stored) {
                block.innerHTML = stored.originalHtml;
            }
            block.removeAttribute("data-voice-block");
            block.classList.remove("voice-block--active", "voice-block--inactive");
        });
    }, []);

    const updateWordStyles = useCallback((blockIdx: number, wordIdx: number) => {
        document.querySelectorAll("[data-voice-block]").forEach((el, idx) => {
            if (idx === blockIdx) {
                el.classList.add("voice-block--active");
                el.classList.remove("voice-block--inactive");
            } else {
                el.classList.add("voice-block--inactive");
                el.classList.remove("voice-block--active");
            }
        });

        const activeBlock = document.querySelector(`[data-voice-block="${blockIdx}"]`);
        if (!activeBlock) return;

        activeBlock.querySelectorAll(".voice-word").forEach(wordEl => {
            const wIdx = parseInt(wordEl.getAttribute("data-word-index") || "-1", 10);
            wordEl.classList.remove("voice-word--read", "voice-word--current", "voice-word--pending");

            if (wIdx < wordIdx) {
                wordEl.classList.add("voice-word--read");
            } else if (wIdx === wordIdx) {
                wordEl.classList.add("voice-word--current");
            } else {
                wordEl.classList.add("voice-word--pending");
            }
        });
    }, []);

    /**
     * Play speech for a specific block starting from a specific word
     */
    const playBlockFromWord = useCallback((blockIndex: number, startWordIndex: number) => {
        const blocks = blocksRef.current;

        if (blockIndex >= blocks.length) {
            setIsPlaying(false);
            setIsPaused(false);
            setActiveBlockIndex(-1);
            activeBlockIndexRef.current = -1;
            setCurrentWordIndex(-1);
            currentWordIndexRef.current = -1;
            unwrapWords();
            return;
        }

        const block = blocks[blockIndex];

        const remainingBoundaries = block.wordBoundaries.filter(wb => wb.index >= startWordIndex);
        if (remainingBoundaries.length === 0) {
            playBlockFromWord(blockIndex + 1, 0);
            return;
        }

        const firstWordStart = remainingBoundaries[0].start;
        const remainingText = block.text.substring(firstWordStart);

        setActiveBlockIndex(blockIndex);
        activeBlockIndexRef.current = blockIndex;
        setCurrentWordIndex(startWordIndex);
        currentWordIndexRef.current = startWordIndex;
        updateWordStyles(blockIndex, startWordIndex);

        if (startWordIndex === 0) {
            block.element.scrollIntoView({ behavior: "smooth", block: "center" });
        }

        // Generate unique ID for this utterance
        const thisUtteranceId = ++utteranceIdRef.current;
        currentUtteranceIdRef.current = thisUtteranceId;

        const utterance = new SpeechSynthesisUtterance(remainingText);

        if (selectedVoiceRef.current) {
            utterance.voice = selectedVoiceRef.current;
        }

        utterance.rate = playbackRateRef.current;
        utterance.pitch = 1.0;
        utterance.volume = volumeRef.current;

        const adjustedBoundaries = remainingBoundaries.map(wb => ({
            ...wb,
            start: wb.start - firstWordStart,
            end: wb.end - firstWordStart
        }));

        // Reset boundary fired flag for this utterance
        boundaryFiredRef.current = false;

        // Clear any existing fallback timer
        if (fallbackTimerRef.current) {
            clearTimeout(fallbackTimerRef.current);
            fallbackTimerRef.current = null;
        }

        // ==========================================
        // TIMER-BASED FALLBACK FOR SAFARI/iOS/MOBILE
        // ==========================================
        // Estimate ~280ms per word at rate 1.0 (adjust based on actual rate)
        // This provides visual feedback when onboundary doesn't fire
        const safePlaybackRate = playbackRateRef.current > 0 ? playbackRateRef.current : 1;
        const avgWordDuration = 280 / safePlaybackRate; // ms per word
        let fallbackWordIndex = startWordIndex;

        // Start the fallback timer using setInterval
        const startFallbackTimer = () => {
            // Clear any existing timer first
            if (fallbackTimerRef.current) {
                clearInterval(fallbackTimerRef.current);
            }

            fallbackTimerRef.current = setInterval(() => {
                // Guard: stop if utterance changed, boundary events took over, or paused
                if (currentUtteranceIdRef.current !== thisUtteranceId) {
                    if (fallbackTimerRef.current) {
                        clearInterval(fallbackTimerRef.current);
                        fallbackTimerRef.current = null;
                    }
                    return;
                }
                if (boundaryFiredRef.current) {
                    if (fallbackTimerRef.current) {
                        clearInterval(fallbackTimerRef.current);
                        fallbackTimerRef.current = null;
                    }
                    return;
                }
                if (isPausedRef.current) return;

                // Advance to next word
                fallbackWordIndex++;
                if (fallbackWordIndex < block.wordBoundaries.length) {
                    setCurrentWordIndex(fallbackWordIndex);
                    currentWordIndexRef.current = fallbackWordIndex;
                    updateWordStyles(blockIndex, fallbackWordIndex);
                } else {
                    // Self-clear when last word is reached
                    if (fallbackTimerRef.current) {
                        clearInterval(fallbackTimerRef.current);
                        fallbackTimerRef.current = null;
                    }
                }
            }, avgWordDuration);
        };

        // Give onboundary 300ms to fire before starting fallback
        // Bug 2 fix: Store timeout handle in ref to allow cleanup
        if (fallbackDelayTimerRef.current) {
            clearTimeout(fallbackDelayTimerRef.current);
        }
        fallbackDelayTimerRef.current = setTimeout(() => {
            fallbackDelayTimerRef.current = null;
            if (!boundaryFiredRef.current && currentUtteranceIdRef.current === thisUtteranceId) {
                startFallbackTimer();
            }
        }, 150);

        utterance.onboundary = (event) => {
            // Only process if this is still the current utterance
            if (currentUtteranceIdRef.current !== thisUtteranceId) return;

            // Only perform word-level handling (including disabling the fallback)
            // when we get word boundaries. Some browsers/voices fire "sentence"
            // but not "word"; in those cases we keep the fallback timer running.
            if (event.name === "word") {
                // Word boundaries are working, so we can disable the fallback timer.
                boundaryFiredRef.current = true;
                if (fallbackTimerRef.current) {
                    clearTimeout(fallbackTimerRef.current);
                    fallbackTimerRef.current = null;
                }

                const charIndex = event.charIndex;
                const foundWord = adjustedBoundaries.find(wb =>
                    charIndex >= wb.start && charIndex < wb.end
                );

                if (!foundWord && adjustedBoundaries.length > 0) {
                    const closest = adjustedBoundaries.reduce((prev, curr) =>
                        Math.abs(curr.start - charIndex) < Math.abs(prev.start - charIndex) ? curr : prev
                        , adjustedBoundaries[0]);

                    if (closest && Math.abs(closest.start - charIndex) < 10) {
                        setCurrentWordIndex(closest.index);
                        currentWordIndexRef.current = closest.index;
                        updateWordStyles(blockIndex, closest.index);
                        return;
                    }
                }

                if (foundWord) {
                    setCurrentWordIndex(foundWord.index);
                    currentWordIndexRef.current = foundWord.index;
                    updateWordStyles(blockIndex, foundWord.index);
                }
            }
        };

        utterance.onend = () => {
            // Clear fallback timers
            clearFallbackTimers();
            // CRITICAL: Only advance if this is still the current utterance
            // This prevents stale callbacks from triggering double playback
            if (currentUtteranceIdRef.current !== thisUtteranceId) {
                return;
            }
            // Move to next block starting from word 0
            playBlockFromWord(blockIndex + 1, 0);
        };

        utterance.onerror = (e) => {
            // Clear fallback timers
            clearFallbackTimers();
            if (e.error === 'interrupted' || e.error === 'canceled') {
                return;
            }
            if (currentUtteranceIdRef.current !== thisUtteranceId) {
                return;
            }
            console.error("Speech error", e);
            setIsPlaying(false);
            setIsPaused(false);
            setActiveBlockIndex(-1);
            activeBlockIndexRef.current = -1;
            setCurrentWordIndex(-1);
            currentWordIndexRef.current = -1;
            unwrapWords();
        };

        window.speechSynthesis.speak(utterance);
    }, [updateWordStyles, unwrapWords, clearFallbackTimers]);

    const playBlock = useCallback((blockIndex: number) => {
        playBlockFromWord(blockIndex, 0);
    }, [playBlockFromWord]);

    const toggleSpeech = useCallback(() => {
        if (typeof window === "undefined" || !window.speechSynthesis) return;

        if (isPlaying) {
            // Clear fallback timers
            clearFallbackTimers();
            // Increment utterance ID to invalidate any pending callbacks
            currentUtteranceIdRef.current = ++utteranceIdRef.current;
            window.speechSynthesis.cancel();
            setIsPlaying(false);
            setIsPaused(false);
            setActiveBlockIndex(-1);
            activeBlockIndexRef.current = -1;
            setCurrentWordIndex(-1);
            currentWordIndexRef.current = -1;
            unwrapWords();
            return;
        }

        const blocks = parseArticleContent();
        if (blocks.length === 0) return;

        blocksRef.current = blocks;
        blocks.forEach((block, idx) => wrapWordsInBlock(block, idx));

        setIsPlaying(true);
        setIsPaused(false);
        playBlock(0);
    }, [isPlaying, parseArticleContent, wrapWordsInBlock, playBlock, unwrapWords, clearFallbackTimers]);

    const pauseSpeech = useCallback(() => {
        if (typeof window === "undefined" || !window.speechSynthesis) return;
        if (!isPlaying || isPaused) return;

        // Bug 1 fix: Clear fallback timer on pause to prevent desync
        clearFallbackTimers();

        window.speechSynthesis.pause();
        setIsPaused(true);
    }, [isPlaying, isPaused, clearFallbackTimers]);

    const resumeSpeech = useCallback(() => {
        if (typeof window === "undefined" || !window.speechSynthesis) return;
        if (!isPlaying || !isPaused) return;

        // Clear Chrome keepalive before resuming
        if (chromeKeepAliveRef.current) {
            clearInterval(chromeKeepAliveRef.current);
            chromeKeepAliveRef.current = null;
        }

        // Set synchronous ref BEFORE resume() so handlers see it immediately
        isPausedRef.current = false;

        window.speechSynthesis.resume();
        setIsPaused(false);

        // Bug 1 fix: Restart fallback timer on resume if onboundary never fired
        if (!boundaryFiredRef.current && activeBlockIndexRef.current >= 0) {
            const block = blocksRef.current[activeBlockIndexRef.current];
            if (block) {
                // Clear any existing timers first to prevent orphaned intervals on double-click
                clearFallbackTimers();
                const safePlaybackRate = playbackRateRef.current > 0 ? playbackRateRef.current : 1;
                const avgWordDuration = 280 / safePlaybackRate;
                let fallbackWordIndex = currentWordIndexRef.current;
                // Capture utterance ID to detect stale intervals after speed/voice/volume changes
                const resumeUtteranceId = currentUtteranceIdRef.current;
                fallbackTimerRef.current = setInterval(() => {
                    // Self-clear if utterance has changed (e.g., restart triggered)
                    if (currentUtteranceIdRef.current !== resumeUtteranceId) {
                        if (fallbackTimerRef.current) {
                            clearInterval(fallbackTimerRef.current);
                            fallbackTimerRef.current = null;
                        }
                        return;
                    }
                    if (boundaryFiredRef.current) {
                        if (fallbackTimerRef.current) {
                            clearInterval(fallbackTimerRef.current);
                            fallbackTimerRef.current = null;
                        }
                        return;
                    }
                    fallbackWordIndex++;
                    if (fallbackWordIndex < block.wordBoundaries.length) {
                        setCurrentWordIndex(fallbackWordIndex);
                        currentWordIndexRef.current = fallbackWordIndex;
                        updateWordStyles(activeBlockIndexRef.current, fallbackWordIndex);
                    } else {
                        if (fallbackTimerRef.current) {
                            clearInterval(fallbackTimerRef.current);
                            fallbackTimerRef.current = null;
                        }
                    }
                }, avgWordDuration);
            }
        }
    }, [isPlaying, isPaused, updateWordStyles, clearFallbackTimers]);

    const stopSpeech = useCallback(() => {
        if (typeof window === "undefined" || !window.speechSynthesis) return;

        // Clear fallback timers
        clearFallbackTimers();
        // Increment utterance ID to invalidate any pending callbacks
        currentUtteranceIdRef.current = ++utteranceIdRef.current;
        window.speechSynthesis.cancel();
        setIsPlaying(false);
        setIsPaused(false);
        setActiveBlockIndex(-1);
        activeBlockIndexRef.current = -1;
        setCurrentWordIndex(-1);
        currentWordIndexRef.current = -1;
        unwrapWords();
    }, [unwrapWords, clearFallbackTimers]);

    /**
     * Restart from current word with new settings
     */
    const restartFromCurrentWord = useCallback(() => {
        if (!isPlaying || isPaused) return;

        const currentBlock = activeBlockIndexRef.current;
        const currentWord = currentWordIndexRef.current;

        if (currentBlock < 0) return;

        // Increment utterance ID to invalidate the current utterance's callbacks
        currentUtteranceIdRef.current = ++utteranceIdRef.current;
        window.speechSynthesis.cancel();

        // Small delay then restart from current word
        setTimeout(() => {
            playBlockFromWord(currentBlock, Math.max(0, currentWord));
        }, 50);
    }, [isPlaying, isPaused, playBlockFromWord]);

    const setPlaybackRate = useCallback((rate: number) => {
        setPlaybackRateState(rate);
        playbackRateRef.current = rate;

        if (isPlaying && !isPaused && activeBlockIndexRef.current >= 0) {
            restartFromCurrentWord();
        }
    }, [isPlaying, isPaused, restartFromCurrentWord]);

    const setVoice = useCallback((index: number) => {
        setSelectedVoiceIndex(index);
        selectedVoiceRef.current = availableVoices[index] || null;

        if (isPlaying && !isPaused && activeBlockIndexRef.current >= 0) {
            restartFromCurrentWord();
        }
    }, [availableVoices, isPlaying, isPaused, restartFromCurrentWord]);

    const setVolume = useCallback((vol: number) => {
        const clampedVol = Math.max(0, Math.min(1, vol));
        setVolumeState(clampedVol);
        volumeRef.current = clampedVol;

        if (isPlaying && !isPaused && activeBlockIndexRef.current >= 0) {
            restartFromCurrentWord();
        }
    }, [isPlaying, isPaused, restartFromCurrentWord]);

    const value: VoiceReadingContextType = {
        isPlaying,
        isPaused,
        activeBlockIndex,
        currentWordIndex,
        availableVoices,
        selectedVoiceIndex,
        playbackRate,
        volume,
        toggleSpeech,
        pauseSpeech,
        resumeSpeech,
        setPlaybackRate,
        setVoice,
        setVolume,
        stopSpeech,
    };

    return (
        <VoiceReadingContext.Provider value={value}>
            {children}
        </VoiceReadingContext.Provider>
    );
}

export default VoiceReadingContext;
