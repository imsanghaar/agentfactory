import { defineConfig } from "vitest/config";
import { resolve } from "node:path";

export default defineConfig({
  resolve: {
    alias: {
      "@": resolve(__dirname, "src"),
      // Stub Docusaurus imports that aren't available in test environment
      "@docusaurus/Link": resolve(
        __dirname,
        "src/__tests__/__mocks__/docusaurus.ts",
      ),
      "@docusaurus/useBaseUrl": resolve(
        __dirname,
        "src/__tests__/__mocks__/docusaurus.ts",
      ),
      "@docusaurus/BrowserOnly": resolve(
        __dirname,
        "src/__tests__/__mocks__/docusaurus.ts",
      ),
      "@theme/Layout": resolve(
        __dirname,
        "src/__tests__/__mocks__/docusaurus.ts",
      ),
      "@docusaurus/useDocusaurusContext": resolve(
        __dirname,
        "src/__tests__/__mocks__/useDocusaurusContext.ts",
      ),
    },
  },
  test: {
    root: ".",
    environment: "jsdom",
    include: ["src/__tests__/**/*.test.{ts,tsx}"],
    setupFiles: ["src/__tests__/setup.ts"],
    testTimeout: 10_000,
    css: {
      modules: {
        classNameStrategy: "non-scoped",
      },
    },
  },
});
