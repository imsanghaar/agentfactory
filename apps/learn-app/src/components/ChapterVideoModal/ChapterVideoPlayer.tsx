"use client";

import * as React from "react";
import { ChapterVideoModal } from "./ChapterVideoModal";
import { ChapterVideoButton } from "./ChapterVideoButton";

export function ChapterVideoPlayer() {
  const [showModal, setShowModal] = React.useState(false);

  React.useEffect(() => {
    const handleOpenVideo = () => setShowModal(true);
    window.addEventListener("open-chapter-video", handleOpenVideo);
    return () => window.removeEventListener("open-chapter-video", handleOpenVideo);
  }, []);

  return (
    <>
      <ChapterVideoModal isOpen={showModal} onOpenChange={setShowModal} />
    </>
  );
}

export default ChapterVideoPlayer;
