import React from 'react';
import styles from './styles.module.css';
import clsx from 'clsx';

interface ThreeDBookProps {
    src: string;
    alt?: string;
    className?: string;
}

export const ThreeDBook: React.FC<ThreeDBookProps> = ({ src, alt = "Book Cover", className }) => {
    const bookRef = React.useRef<HTMLDivElement>(null);
    const wrapperRef = React.useRef<HTMLDivElement>(null);
    // Use ref instead of state to avoid re-renders on every mouse move
    const rafIdRef = React.useRef<number | null>(null);
    // Detect touch device once on mount - skip expensive mouse tracking on mobile
    const isTouchDeviceRef = React.useRef<boolean | null>(null);

    const handleMouseMove = React.useCallback((e: React.MouseEvent<HTMLDivElement>) => {
        // Lazy-init touch detection (SSR-safe)
        if (isTouchDeviceRef.current === null) {
            isTouchDeviceRef.current = 'ontouchstart' in window || navigator.maxTouchPoints > 0;
        }

        // Skip mouse tracking on touch devices - no benefit, only cost
        if (isTouchDeviceRef.current) return;

        if (!bookRef.current || !wrapperRef.current) return;

        // Cancel any pending animation frame to throttle updates
        if (rafIdRef.current !== null) {
            cancelAnimationFrame(rafIdRef.current);
        }

        // Use requestAnimationFrame to batch DOM updates at 60fps max
        rafIdRef.current = requestAnimationFrame(() => {
            if (!bookRef.current || !wrapperRef.current) return;

            const rect = wrapperRef.current.getBoundingClientRect();
            const width = rect.width;
            const height = rect.height;

            const mouseX = e.clientX - rect.left;
            const mouseY = e.clientY - rect.top;

            const rotateY = ((mouseX - width / 2) / width) * 30; // -15 to 15 deg
            const rotateX = ((height / 2 - mouseY) / height) * 20; // -10 to 10 deg

            // Directly update CSS custom properties - no React re-render
            bookRef.current.style.setProperty('--rotate-x', `${rotateX}deg`);
            bookRef.current.style.setProperty('--rotate-y', `${rotateY}deg`);
        });
    }, []);

    const handleMouseLeave = React.useCallback(() => {
        // Skip on touch devices
        if (isTouchDeviceRef.current) return;

        if (rafIdRef.current !== null) {
            cancelAnimationFrame(rafIdRef.current);
        }
        if (bookRef.current) {
            // Reset rotation smoothly - no React re-render
            bookRef.current.style.setProperty('--rotate-x', '0deg');
            bookRef.current.style.setProperty('--rotate-y', '0deg');
        }
    }, []);

    // Cleanup animation frame on unmount
    React.useEffect(() => {
        return () => {
            if (rafIdRef.current !== null) {
                cancelAnimationFrame(rafIdRef.current);
            }
        };
    }, []);

    return (
        <div
            ref={wrapperRef}
            className={clsx(styles.bookWrapper, className)}
            onMouseMove={handleMouseMove}
            onMouseLeave={handleMouseLeave}
        >
            <div
                ref={bookRef}
                className={styles.book}
                style={{
                    '--rotate-x': '0deg',
                    '--rotate-y': '0deg',
                } as React.CSSProperties}
            >
                {/* Front Cover */}
                <div className={styles.cover}>
                    <img src={src} alt={alt} className={styles.coverImg} />
                    {/* Dynamic Sheen */}
                    <div className={styles.sheen} />
                    <div className={styles.spineShadow} />
                </div>

                {/* Back Cover */}
                <div className={styles.back} />

                {/* Spine (Left) */}
                <div className={styles.left} />

                {/* Page Block (Top, Bottom, Right) */}
                <div className={styles.right} />
                <div className={styles.top} />
                <div className={styles.bottom} />
            </div>
        </div>
    );
};
