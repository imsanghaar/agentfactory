import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { ChapterVideoButton } from "./ChapterVideoButton";

describe("ChapterVideoButton", () => {
  it("renders with Play text and icon", () => {
    render(<ChapterVideoButton />);

    expect(screen.getByText("Play")).toBeInTheDocument();
  });

  it("calls onClick when clicked", () => {
    const handleClick = vi.fn();
    render(<ChapterVideoButton onClick={handleClick} />);

    fireEvent.click(screen.getByText("Play"));

    expect(handleClick).toHaveBeenCalledTimes(1);
  });
});
