import { createContext, useContext } from "react";

interface PracticeContextType {
  practiceOpen: boolean;
  openPractice: (exerciseSubId?: string) => void;
}

export const PracticeContext = createContext<PracticeContextType | null>(null);

export function usePractice(): PracticeContextType | null {
  return useContext(PracticeContext);
}
