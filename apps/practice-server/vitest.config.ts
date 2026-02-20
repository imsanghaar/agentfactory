import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    root: '.',
    include: ['src/__tests__/**/*.test.ts'],
    testTimeout: 10_000,
    hookTimeout: 10_000,
  },
});
