import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import { mkdir, rm, readdir, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';
import { tmpdir } from 'node:os';
import { randomUUID } from 'node:crypto';
import extract from 'extract-zip';
import { createWorkspace, resolveExerciseDir } from '../../exercises/workspace.js';

// Use a unique temp dir per test run to avoid collisions
let testDir: string;

beforeEach(async () => {
  testDir = join(tmpdir(), `practice-test-${randomUUID()}`);
  await mkdir(testDir, { recursive: true });
});

afterEach(async () => {
  await rm(testDir, { recursive: true, force: true });
});

describe('resolveExerciseDir', () => {
  it('resolves sub-exercise at depth 1', async () => {
    // Create structure: testDir/exercise-1.1-first-task/
    const exerciseDir = join(testDir, 'exercise-1.1-first-task');
    await mkdir(exerciseDir, { recursive: true });
    await writeFile(join(exerciseDir, 'INSTRUCTIONS.md'), 'test');

    const result = await resolveExerciseDir(testDir, '1.1');
    expect(result).toBe(exerciseDir);
  });

  it('resolves sub-exercise at depth 2 (inside module)', async () => {
    // Create structure: testDir/module-1/exercise-1.1-first-task/
    const moduleDir = join(testDir, 'module-1');
    const exerciseDir = join(moduleDir, 'exercise-1.1-first-task');
    await mkdir(exerciseDir, { recursive: true });

    const result = await resolveExerciseDir(testDir, '1.1');
    expect(result).toBe(exerciseDir);
  });

  it('falls back to workspace root when sub-exercise not found', async () => {
    const result = await resolveExerciseDir(testDir, 'nonexistent');
    expect(result).toBe(testDir);
  });

  it('works with dotted sub-exercise IDs', async () => {
    const exerciseDir = join(testDir, 'exercise-2.1.3-deep-task');
    await mkdir(exerciseDir, { recursive: true });

    const result = await resolveExerciseDir(testDir, '2.1.3');
    expect(result).toBe(exerciseDir);
  });

  it('handles empty directory gracefully', async () => {
    const result = await resolveExerciseDir(testDir, '1.1');
    expect(result).toBe(testDir);
  });

  it('ignores files (only matches directories)', async () => {
    // Create a file that matches the pattern but is not a directory
    await writeFile(join(testDir, 'exercise-1.1-fake'), 'not a dir');

    const result = await resolveExerciseDir(testDir, '1.1');
    expect(result).toBe(testDir);
  });
});

describe('test fixture ZIP extraction', () => {
  const fixturePath = join(
    import.meta.dirname,
    '..',
    'fixtures',
    'test-exercise.zip',
  );

  it('fixture ZIP extracts with expected structure', async () => {
    const extractDir = join(testDir, 'extracted');
    await mkdir(extractDir, { recursive: true });

    await extract(fixturePath, { dir: extractDir });

    // Should have a single top-level directory (GitHub zipball pattern)
    const topEntries = await readdir(extractDir);
    expect(topEntries).toContain('test-exercise');

    // Verify nested structure
    const exerciseRoot = join(extractDir, 'test-exercise');
    const rootEntries = await readdir(exerciseRoot);
    expect(rootEntries).toContain('CLAUDE.md');
    expect(rootEntries).toContain('INSTRUCTIONS.md');
    expect(rootEntries).toContain('module-1');
    expect(rootEntries).toContain('module-2');

    // Verify module-1 sub-exercises
    const mod1 = await readdir(join(exerciseRoot, 'module-1'));
    expect(mod1).toContain('exercise-1.1-first-task');
    expect(mod1).toContain('exercise-1.2-second-task');

    // Verify module-2 sub-exercises
    const mod2 = await readdir(join(exerciseRoot, 'module-2'));
    expect(mod2).toContain('exercise-2.1-third-task');

    // Verify INSTRUCTIONS.md exists in sub-exercise
    const instructions = await readFile(
      join(exerciseRoot, 'module-1', 'exercise-1.1-first-task', 'INSTRUCTIONS.md'),
      'utf-8',
    );
    expect(instructions).toContain('Exercise 1.1');
  });

  it('resolveExerciseDir finds sub-exercises after extraction', async () => {
    const extractDir = join(testDir, 'resolve-test');
    await mkdir(extractDir, { recursive: true });

    await extract(fixturePath, { dir: extractDir });

    // Simulate the GitHub zipball unwrap (move contents up from single subdir)
    const exerciseRoot = join(extractDir, 'test-exercise');

    const result = await resolveExerciseDir(exerciseRoot, '1.1');
    expect(result).toBe(join(exerciseRoot, 'module-1', 'exercise-1.1-first-task'));

    const result2 = await resolveExerciseDir(exerciseRoot, '2.1');
    expect(result2).toBe(join(exerciseRoot, 'module-2', 'exercise-2.1-third-task'));
  });

  it('resolveExerciseDir falls back for non-existent sub-exercise after extraction', async () => {
    const extractDir = join(testDir, 'fallback-test');
    await mkdir(extractDir, { recursive: true });

    await extract(fixturePath, { dir: extractDir });
    const exerciseRoot = join(extractDir, 'test-exercise');

    const result = await resolveExerciseDir(exerciseRoot, '99.99');
    expect(result).toBe(exerciseRoot);
  });
});
