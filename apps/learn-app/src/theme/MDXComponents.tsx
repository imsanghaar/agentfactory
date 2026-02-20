import React from "react";
import MDXComponents from "@theme-original/MDXComponents";
import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";
import Quiz from "@/components/quiz/Quiz";
import GatedQuiz from "@/components/GatedQuiz";
import GatedSummary from "@/components/GatedSummary";
import InteractivePython from "@/components/InteractivePython";
import PDFViewer from "@/components/PDFViewer";
import ContentGate from "@/components/ContentGate";
import {
  OSTabs,
  OSTabsProvider,
  WindowsContent,
  MacOSContent,
  LinuxContent,
} from "@/components/OSTabs";
import ExerciseCard from "@/components/ExerciseCard";
import { ChapterVideoModal, ChapterVideoButton, ChapterVideoPlayer } from "@/components/ChapterVideoModal";

export default {
  ...MDXComponents,
  // Docusaurus Tabs components (used by remark-os-tabs plugin)
  Tabs,
  TabItem,
  // Practice exercise marker
  ExerciseCard,
  // Original Quiz (ungated) - use when quiz should be freely accessible
  UnlockedQuiz: Quiz,
  // Default Quiz is now gated - requires sign-in
  Quiz: GatedQuiz,
  // Gated summary section for lesson takeaways
  GatedSummary,
  // Generic content gate for wrapping any content
  ContentGate,
  InteractivePython,
  PDFViewer,
  // OS-specific tabs with shadcn styling
  OSTabs,
  OSTabsProvider,
  WindowsContent,
  MacOSContent,
  LinuxContent,
  // Chapter 1 video playback
  ChapterVideoModal,
  ChapterVideoButton,
  ChapterVideoPlayer,
};
