import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import React from "react";
import { PracticeSetupCard } from "../components/PracticeSetupCard/index";

describe("PracticeSetupCard", () => {
  it("renders the setup heading", () => {
    render(<PracticeSetupCard />);
    expect(screen.getByText("Start Practice Server")).toBeInTheDocument();
  });

  it("displays the npx command inside the code element", () => {
    render(<PracticeSetupCard />);
    // The <code> element contains both the command text and a "Click to copy" span,
    // so we use a partial matcher to find the command text within the code element.
    const codeEl = document.querySelector(".practice-setup-cmd");
    expect(codeEl).toBeInTheDocument();
    expect(codeEl!.textContent).toContain("npx af-practice");
  });

  it("shows waiting indicator", () => {
    render(<PracticeSetupCard />);
    expect(screen.getByText("Waiting for server...")).toBeInTheDocument();
  });

  it("copies command on click", async () => {
    render(<PracticeSetupCard />);
    const codeEl = document.querySelector(".practice-setup-cmd")!;
    fireEvent.click(codeEl);

    expect(navigator.clipboard.writeText).toHaveBeenCalledWith(
      "npx af-practice",
    );
  });

  it('shows "Copied!" feedback after click', async () => {
    render(<PracticeSetupCard />);
    const codeEl = document.querySelector(".practice-setup-cmd")!;
    fireEvent.click(codeEl);

    await waitFor(() => {
      expect(screen.getByText("Copied!")).toBeInTheDocument();
    });
  });

  it("toggles Claude Code info section", () => {
    render(<PracticeSetupCard />);

    expect(screen.queryByText(/docs.anthropic.com/)).toBeNull();

    fireEvent.click(screen.getByText("Don't have Claude Code?"));
    expect(screen.getByText(/docs.anthropic.com/)).toBeInTheDocument();

    fireEvent.click(screen.getByText("Hide"));
    expect(screen.queryByText(/docs.anthropic.com/)).toBeNull();
  });

  it("renders retry button when onRetry provided", () => {
    const onRetry = vi.fn();
    render(<PracticeSetupCard onRetry={onRetry} />);
    const btn = screen.getByText("Retry");
    fireEvent.click(btn);
    expect(onRetry).toHaveBeenCalledOnce();
  });

  it("does not render retry button when onRetry not provided", () => {
    render(<PracticeSetupCard />);
    expect(screen.queryByText("Retry")).toBeNull();
  });
});
