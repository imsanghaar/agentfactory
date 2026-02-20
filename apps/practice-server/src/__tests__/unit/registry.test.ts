import { describe, it, expect } from "vitest";
import { getExercise, listExercises } from "../../exercises/registry.js";

describe("getExercise", () => {
  it("returns config for known exercise", () => {
    const result = getExercise("ch3-basics");
    expect(result).toBeDefined();
    expect(result!.repo).toBe("panaversity/claude-code-basic-exercises");
    expect(result!.releaseTag).toBe("latest");
  });

  it("returns config for all registered exercises", () => {
    const ids = [
      "ch3-basics",
      "ch3-skills",
      "ch3-plugins",
      "ch3-agent-teams",
      "ch4-context",
      "ch5-sdd",
      "ch6-principles",
      "ch8-file-processing",
      "ch9-computation",
      "ch10-structured-data",
      "ch11-linux",
      "ch12-version-control",
    ];
    for (const id of ids) {
      const result = getExercise(id);
      expect(result).toBeDefined();
      expect(result!.repo).toMatch(/^panaversity\//);
      expect(result!.releaseTag).toBe("latest");
    }
  });

  it("returns undefined for unknown exercise", () => {
    expect(getExercise("nonexistent")).toBeUndefined();
  });

  it("returns undefined for empty string", () => {
    expect(getExercise("")).toBeUndefined();
  });

  it("each exercise has a description", () => {
    const exercises = listExercises();
    for (const [id, config] of Object.entries(exercises)) {
      expect(
        config.description,
        `${id} should have a description`,
      ).toBeDefined();
      expect(config.description!.length).toBeGreaterThan(0);
    }
  });
});

describe("listExercises", () => {
  it("returns all registered exercises", () => {
    const exercises = listExercises();
    const ids = Object.keys(exercises);
    expect(ids).toContain("ch3-basics");
    expect(ids).toContain("ch3-skills");
    expect(ids).toContain("ch3-plugins");
    expect(ids).toContain("ch3-agent-teams");
    expect(ids).toContain("ch4-context");
    expect(ids).toContain("ch5-sdd");
    expect(ids).toContain("ch6-principles");
    expect(ids).toContain("ch8-file-processing");
    expect(ids).toContain("ch9-computation");
    expect(ids).toContain("ch10-structured-data");
    expect(ids).toContain("ch11-linux");
    expect(ids).toContain("ch12-version-control");
    expect(ids).toHaveLength(12);
  });

  it("returns a copy (not the original reference)", () => {
    const a = listExercises();
    const b = listExercises();
    expect(a).not.toBe(b);
    expect(a).toEqual(b);
  });

  it("mutations to returned object do not affect registry", () => {
    const exercises = listExercises();
    (exercises as Record<string, unknown>)["hacked"] = {
      repo: "evil",
      releaseTag: "v1",
    };
    expect(getExercise("hacked")).toBeUndefined();
  });
});
