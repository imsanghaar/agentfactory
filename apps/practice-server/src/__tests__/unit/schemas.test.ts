import { describe, it, expect } from "vitest";
import { StartSessionSchema } from "../../routes/sessions.js";

describe("StartSessionSchema", () => {
  describe("exerciseId", () => {
    it("accepts valid exercise ID", () => {
      const result = StartSessionSchema.safeParse({ exerciseId: "ch3-basics" });
      expect(result.success).toBe(true);
    });

    it("accepts alphanumeric with hyphens", () => {
      const result = StartSessionSchema.safeParse({
        exerciseId: "my-exercise-1",
      });
      expect(result.success).toBe(true);
    });

    it("accepts underscores", () => {
      const result = StartSessionSchema.safeParse({
        exerciseId: "my_exercise",
      });
      expect(result.success).toBe(true);
    });

    it("rejects empty string", () => {
      const result = StartSessionSchema.safeParse({ exerciseId: "" });
      expect(result.success).toBe(false);
    });

    it("rejects missing exerciseId", () => {
      const result = StartSessionSchema.safeParse({});
      expect(result.success).toBe(false);
    });

    it("rejects path traversal characters", () => {
      const result = StartSessionSchema.safeParse({
        exerciseId: "../etc/passwd",
      });
      expect(result.success).toBe(false);
    });

    it("rejects spaces", () => {
      const result = StartSessionSchema.safeParse({
        exerciseId: "my exercise",
      });
      expect(result.success).toBe(false);
    });

    it("rejects shell metacharacters", () => {
      const result = StartSessionSchema.safeParse({
        exerciseId: "foo;rm -rf /",
      });
      expect(result.success).toBe(false);
    });

    it("rejects null bytes", () => {
      const result = StartSessionSchema.safeParse({ exerciseId: "foo\x00bar" });
      expect(result.success).toBe(false);
    });
  });

  describe("subExercise", () => {
    it("accepts valid sub-exercise ID", () => {
      const result = StartSessionSchema.safeParse({
        exerciseId: "ch3-basics",
        subExercise: "1.1",
      });
      expect(result.success).toBe(true);
    });

    it("accepts dotted notation", () => {
      const result = StartSessionSchema.safeParse({
        exerciseId: "ch3-basics",
        subExercise: "2.1.3",
      });
      expect(result.success).toBe(true);
    });

    it("is optional", () => {
      const result = StartSessionSchema.safeParse({ exerciseId: "ch3-basics" });
      expect(result.success).toBe(true);
      if (result.success) {
        expect(result.data.subExercise).toBeUndefined();
      }
    });

    it("rejects path traversal", () => {
      const result = StartSessionSchema.safeParse({
        exerciseId: "ch3-basics",
        subExercise: "../../../etc/passwd",
      });
      expect(result.success).toBe(false);
    });

    it("rejects shell metacharacters", () => {
      const result = StartSessionSchema.safeParse({
        exerciseId: "ch3-basics",
        subExercise: "1.1;ls",
      });
      expect(result.success).toBe(false);
    });

    it("rejects spaces", () => {
      const result = StartSessionSchema.safeParse({
        exerciseId: "ch3-basics",
        subExercise: "1 1",
      });
      expect(result.success).toBe(false);
    });

    it("accepts hyphens and underscores", () => {
      const result = StartSessionSchema.safeParse({
        exerciseId: "ch3-basics",
        subExercise: "sub-1_a",
      });
      expect(result.success).toBe(true);
    });
  });

  describe("extra fields", () => {
    it("strips unknown fields", () => {
      const result = StartSessionSchema.safeParse({
        exerciseId: "ch3-basics",
        malicious: "data",
      });
      expect(result.success).toBe(true);
      if (result.success) {
        expect("malicious" in result.data).toBe(false);
      }
    });
  });
});
