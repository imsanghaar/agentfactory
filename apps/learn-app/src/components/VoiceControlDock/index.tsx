/**
 * VoiceControlDock
 * 
 * A floating control panel for voice reading controls.
 * Includes: Voice selector, playback speed, volume, pause/resume, and stop.
 */

import React, { useState } from "react";
import { useVoiceReading } from "@/contexts/VoiceReadingContext";

export function VoiceControlDock() {
    const {
        isPlaying,
        isPaused,
        availableVoices,
        selectedVoiceIndex,
        playbackRate,
        volume,
        pauseSpeech,
        resumeSpeech,
        setPlaybackRate,
        setVoice,
        setVolume,
        stopSpeech,
    } = useVoiceReading();

    const [isVoiceMenuOpen, setIsVoiceMenuOpen] = useState(false);
    const selectedVoice = availableVoices[selectedVoiceIndex] || null;

    // Don't render if not playing
    if (!isPlaying) return null;

    const handlePauseResume = () => {
        if (isPaused) {
            resumeSpeech();
        } else {
            pauseSpeech();
        }
    };

    return (
        <>
            {/* Voice Control Dock */}
            <div className="voice-control-dock">
                {/* Voice Selector */}
                <div className="voice-control-section">
                    <button
                        className="voice-selector-btn"
                        onClick={() => setIsVoiceMenuOpen(!isVoiceMenuOpen)}
                        title="Select Voice"
                    >
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                            <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z" />
                            <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
                            <line x1="12" y1="19" x2="12" y2="23" />
                            <line x1="8" y1="23" x2="16" y2="23" />
                        </svg>
                        <span className="voice-selector-label">
                            {selectedVoice?.name.split(" ").slice(0, 2).join(" ") || "Voice"}
                        </span>
                        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                            <polyline points="6 9 12 15 18 9" />
                        </svg>
                    </button>

                    {/* Voice Dropdown */}
                    {isVoiceMenuOpen && (
                        <div className="voice-dropdown">
                            {availableVoices.map((voice, index) => (
                                <button
                                    key={index}
                                    onClick={() => {
                                        setVoice(index);
                                        setIsVoiceMenuOpen(false);
                                    }}
                                    className={`voice-option ${index === selectedVoiceIndex ? "voice-option--active" : ""}`}
                                >
                                    <div className="voice-option-name">{voice.name}</div>
                                    <div className="voice-option-lang">{voice.lang}</div>
                                </button>
                            ))}
                        </div>
                    )}
                </div>

                <div className="voice-control-divider" />

                {/* Speed Control */}
                <div className="voice-control-section">
                    <div className="voice-control-group">
                        <label className="voice-control-label">Speed</label>
                        <div className="voice-slider-container">
                            <input
                                type="range"
                                min="0.5"
                                max="2.0"
                                step="0.1"
                                value={playbackRate}
                                onChange={(e) => setPlaybackRate(parseFloat(e.target.value))}
                                className="voice-slider"
                            />
                            <span className="voice-slider-value">{playbackRate.toFixed(1)}x</span>
                        </div>
                    </div>
                </div>

                <div className="voice-control-divider" />

                {/* Volume Control */}
                <div className="voice-control-section">
                    <div className="voice-control-group">
                        <label className="voice-control-label">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5" />
                                <path d="M15.54 8.46a5 5 0 0 1 0 7.07" />
                            </svg>
                        </label>
                        <div className="voice-slider-container">
                            <input
                                type="range"
                                min="0"
                                max="1"
                                step="0.1"
                                value={volume}
                                onChange={(e) => setVolume(parseFloat(e.target.value))}
                                className="voice-slider"
                            />
                            <span className="voice-slider-value">{Math.round(volume * 100)}%</span>
                        </div>
                    </div>
                </div>

                <div className="voice-control-divider" />

                {/* Pause/Resume Button */}
                <button
                    className="voice-pause-btn"
                    onClick={handlePauseResume}
                    title={isPaused ? "Resume Reading" : "Pause Reading"}
                >
                    {isPaused ? (
                        // Play icon
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg>
                    ) : (
                        // Pause icon
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                            <rect x="6" y="4" width="4" height="16" rx="1" />
                            <rect x="14" y="4" width="4" height="16" rx="1" />
                        </svg>
                    )}
                </button>

                {/* Stop Button */}
                <button
                    className="voice-stop-btn"
                    onClick={stopSpeech}
                    title="Stop Reading"
                >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                        <rect x="6" y="6" width="12" height="12" rx="2" />
                    </svg>
                </button>
            </div>

            {/* Backdrop to close voice menu */}
            {isVoiceMenuOpen && (
                <div
                    className="voice-menu-backdrop"
                    onClick={() => setIsVoiceMenuOpen(false)}
                />
            )}
        </>
    );
}

export default VoiceControlDock;
