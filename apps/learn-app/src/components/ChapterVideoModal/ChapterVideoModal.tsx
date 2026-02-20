"use client";

import * as React from "react";
import * as DialogPrimitive from "@radix-ui/react-dialog";
import { X } from "lucide-react";
import { cn } from "@/lib/utils";

export interface ChapterVideoModalProps {
  isOpen?: boolean;
  onOpenChange?: (open: boolean) => void;
  videoUrl?: string;
}

const ChapterVideoModal = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Content>,
  ChapterVideoModalProps
>(({ isOpen = false, onOpenChange, videoUrl = "https://www.youtube.com/embed/Yl_yOFXZKrY", ...props }, ref) => {
  const [isPlayerReady, setIsPlayerReady] = React.useState(false);
  const [showProjector, setShowProjector] = React.useState(false);
  const [showScreen, setShowScreen] = React.useState(false);

  React.useEffect(() => {
    if (isOpen) {
      // Trigger animations in sequence
      const projectorTimer = setTimeout(() => setShowProjector(true), 100);
      const screenTimer = setTimeout(() => setShowScreen(true), 800);
      const playerTimer = setTimeout(() => setIsPlayerReady(true), 1200);
      
      return () => {
        clearTimeout(projectorTimer);
        clearTimeout(screenTimer);
        clearTimeout(playerTimer);
      };
    } else {
      setIsPlayerReady(false);
      setShowProjector(false);
      setShowScreen(false);
    }
  }, [isOpen]);

  return (
    <DialogPrimitive.Root open={isOpen} onOpenChange={onOpenChange}>
      <DialogPrimitive.Portal>
        <DialogPrimitive.Overlay
          className={cn(
            "fixed inset-0 z-50 bg-black data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0"
          )}
        />
        <DialogPrimitive.Content
          ref={ref}
          className={cn(
            "fixed inset-0 z-50 flex items-center justify-center bg-transparent p-0 overflow-hidden"
          )}
          {...props}
        >
          {/* Projector Assembly - Descends from top */}
          <div className={cn(
            "projector-assembly",
            showProjector ? "projector-descended" : ""
          )}>
            {/* Projector Body */}
            <div className="projector-body">
              <div className="projector-branding">imsanghaar</div>
              <div className="projector-lens">
                <div className="lens-glass"></div>
              </div>
              <div className="projector-vents"></div>
            </div>
            
            {/* Light Rays */}
            <div className={cn(
              "projector-rays",
              showProjector ? "rays-visible" : ""
            )}>
              <div className="ray ray-left"></div>
              <div className="ray ray-center"></div>
              <div className="ray ray-right"></div>
              <div className="ray ray-far-left"></div>
              <div className="ray ray-far-right"></div>
            </div>
          </div>

          {/* Projection Screen */}
          <div className={cn(
            "projection-screen-container",
            showScreen ? "screen-visible" : ""
          )}>
            <div className="projection-screen">
              <div className="screen-border">
                <div className="video-container">
                  <iframe
                    src={`${videoUrl}${videoUrl.includes('?') ? '&' : '?'}autoplay=${isPlayerReady ? '1' : '0'}`}
                    title="Chapter Video"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    allowFullScreen
                  />
                </div>
              </div>
            </div>
            {/* Screen glow effect */}
            <div className="screen-glow"></div>
          </div>

          {/* Close Button */}
          <DialogPrimitive.Close className="projector-close-button">
            <X className="h-5 w-5" />
            <span className="sr-only">Close</span>
          </DialogPrimitive.Close>
        </DialogPrimitive.Content>
      </DialogPrimitive.Portal>
    </DialogPrimitive.Root>
  );
});

ChapterVideoModal.displayName = "ChapterVideoModal";

export { ChapterVideoModal };
