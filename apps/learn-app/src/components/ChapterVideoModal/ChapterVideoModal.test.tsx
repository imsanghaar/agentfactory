import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { ChapterVideoModal } from "./ChapterVideoModal";
import * as DialogPrimitive from "@radix-ui/react-dialog";

describe("ChapterVideoModal", () => {
  const mockOnOpenChange = vi.fn();

  beforeEach(() => {
    mockOnOpenChange.mockClear();
  });

  it("renders when isOpen=true", () => {
    render(
      <ChapterVideoModal isOpen={true} onOpenChange={mockOnOpenChange} />
    );

    expect(screen.getByRole("dialog")).toBeInTheDocument();
  });

  it("does not render when isOpen=false", () => {
    render(
      <ChapterVideoModal isOpen={false} onOpenChange={mockOnOpenChange} />
    );

    expect(screen.queryByRole("dialog")).not.toBeInTheDocument();
  });

  it("calls onOpenChange when close button is clicked", async () => {
    render(
      <ChapterVideoModal isOpen={true} onOpenChange={mockOnOpenChange} />
    );

    const closeButton = screen.getByLabelText("Close");
    fireEvent.click(closeButton);

    expect(mockOnOpenChange).toHaveBeenCalledWith(false);
  });

  it("calls onOpenChange when overlay is clicked", async () => {
    render(
      <ChapterVideoModal isOpen={true} onOpenChange={mockOnOpenChange} />
    );

    const overlay = document.querySelector('[data-state="open"]');
    if (overlay) {
      fireEvent.click(overlay);
      expect(mockOnOpenChange).toHaveBeenCalledWith(false);
    }
  });
});
