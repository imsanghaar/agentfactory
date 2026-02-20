import { mkdir, readdir, rm, cp } from "node:fs/promises";
import { createWriteStream } from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";
import { pipeline } from "node:stream/promises";
import { Readable } from "node:stream";
import extract from "extract-zip";
import { getExercise } from "./registry.js";
import { appError } from "../errors.js";

const PRACTICE_ROOT = join(homedir(), "af-practice");

const inFlightDownloads = new Map<string, Promise<string>>();

export async function createWorkspace(exerciseId: string): Promise<string> {
  const workspacePath = join(PRACTICE_ROOT, exerciseId);
  await mkdir(workspacePath, { recursive: true });
  return workspacePath;
}

export async function downloadAndExtract(exerciseId: string): Promise<string> {
  const existing = inFlightDownloads.get(exerciseId);
  if (existing) return existing;

  const promise = doDownloadAndExtract(exerciseId);
  inFlightDownloads.set(exerciseId, promise);
  try {
    return await promise;
  } finally {
    inFlightDownloads.delete(exerciseId);
  }
}

async function doDownloadAndExtract(exerciseId: string): Promise<string> {
  const exercise = getExercise(exerciseId);
  if (!exercise) {
    throw appError("EXERCISE_NOT_FOUND", `Unknown exercise: ${exerciseId}`);
  }

  const workspacePath = await createWorkspace(exerciseId);

  // Check if workspace already has content (resume scenario)
  try {
    const entries = await readdir(workspacePath);
    const hasContent = entries.some(
      (e) => !e.startsWith(".") && e !== "__download.zip",
    );
    if (hasContent) {
      console.log(
        `[workspace] ${exerciseId}: workspace already exists (${entries.length} entries), skipping download`,
      );
      return workspacePath;
    }
  } catch {
    // Directory doesn't exist yet, proceed with download
  }

  const apiUrl = `https://api.github.com/repos/${exercise.repo}/releases/latest`;
  console.log(
    `[workspace] ${exerciseId}: fetching release info from ${apiUrl}`,
  );

  let releaseRes: Response;
  try {
    releaseRes = await fetch(apiUrl, {
      headers: {
        "User-Agent": "agentfactory-practice",
        Accept: "application/vnd.github+json",
      },
      signal: AbortSignal.timeout(30_000),
    });
  } catch (err) {
    if (err instanceof DOMException && err.name === "TimeoutError") {
      throw appError(
        "DOWNLOAD_TIMEOUT",
        "Timed out fetching release info",
        "Check your internet connection and try again",
      );
    }
    throw appError(
      "DOWNLOAD_FAILED",
      `Failed to fetch release info: ${err instanceof Error ? err.message : err}`,
    );
  }

  if (!releaseRes.ok) {
    throw appError(
      "DOWNLOAD_FAILED",
      `HTTP ${releaseRes.status} fetching release info from ${apiUrl}`,
    );
  }

  const release = (await releaseRes.json()) as {
    assets: Array<{ browser_download_url: string; name: string }>;
    zipball_url: string;
  };

  // Prefer a .zip asset, fall back to zipball_url
  const zipAsset = release.assets?.find((a) => a.name.endsWith(".zip"));
  const downloadUrl = zipAsset?.browser_download_url ?? release.zipball_url;

  console.log(`[workspace] ${exerciseId}: downloading from ${downloadUrl}`);

  // Stream ZIP to disk
  const zipPath = join(workspacePath, "__download.zip");
  let downloadRes: Response;
  try {
    downloadRes = await fetch(downloadUrl, {
      headers: { "User-Agent": "agentfactory-practice" },
      signal: AbortSignal.timeout(30_000),
    });
  } catch (err) {
    if (err instanceof DOMException && err.name === "TimeoutError") {
      throw appError(
        "DOWNLOAD_TIMEOUT",
        "Download timed out",
        "Check your internet connection and try again",
      );
    }
    throw appError(
      "DOWNLOAD_FAILED",
      `Download failed: ${err instanceof Error ? err.message : err}`,
    );
  }

  if (!downloadRes.ok) {
    throw appError(
      "DOWNLOAD_FAILED",
      `HTTP ${downloadRes.status} downloading ${downloadUrl}`,
      "Try again later or check your internet connection",
    );
  }

  if (!downloadRes.body) {
    throw appError("DOWNLOAD_FAILED", "No response body received");
  }

  await pipeline(
    Readable.fromWeb(
      downloadRes.body as import("node:stream/web").ReadableStream,
    ),
    createWriteStream(zipPath),
  );

  console.log(`[workspace] ${exerciseId}: extracting to ${workspacePath}`);
  try {
    await extract(zipPath, { dir: workspacePath });
  } catch (err) {
    throw appError(
      "EXTRACTION_FAILED",
      `Failed to extract ZIP: ${err instanceof Error ? err.message : err}`,
      "Try running with --refresh to re-download",
    );
  }

  // Clean up zip
  await rm(zipPath, { force: true });

  // If extracted into a single subdirectory (GitHub zipball pattern), move contents up.
  // Use fs.cp to capture dotfiles (.claude/, .clauderc, etc.) that glob patterns miss.
  const entries = await readdir(workspacePath, { withFileTypes: true });
  const subdirs = entries.filter((e) => e.isDirectory());
  if (subdirs.length === 1 && entries.length === 1) {
    const subdir = join(workspacePath, subdirs[0].name);
    await cp(subdir, workspacePath, { recursive: true });
    await rm(subdir, { recursive: true, force: true });
  }

  console.log(`[workspace] ${exerciseId}: ready at ${workspacePath}`);
  return workspacePath;
}

/**
 * Delete the workspace for an exercise so it can be re-downloaded fresh.
 */
export async function resetWorkspace(exerciseId: string): Promise<void> {
  const workspacePath = join(PRACTICE_ROOT, exerciseId);
  console.log(`[workspace] Resetting workspace at ${workspacePath}`);
  await rm(workspacePath, { recursive: true, force: true });
  console.log(`[workspace] Workspace reset: ${exerciseId}`);
}

/**
 * Resolve a sub-exercise ID (e.g., "1.1") to its directory within the workspace.
 * Searches up to 3 levels deep for directories matching `exercise-{id}-*`.
 * Falls back to the workspace root if not found.
 */
export async function resolveExerciseDir(
  workspacePath: string,
  subExercise: string,
): Promise<string> {
  console.log(
    `[workspace] Resolving sub-exercise "${subExercise}" in ${workspacePath}`,
  );

  const match = await findExerciseDir(workspacePath, subExercise, 3);
  if (match) {
    console.log(`[workspace] Resolved sub-exercise ${subExercise} → ${match}`);
    return match;
  }

  console.log(
    `[workspace] Could not resolve sub-exercise "${subExercise}", using workspace root`,
  );
  return workspacePath;
}

/**
 * Recursively search for a directory matching `exercise-{id}-*` up to maxDepth levels.
 */
async function findExerciseDir(
  dir: string,
  subExercise: string,
  maxDepth: number,
): Promise<string | null> {
  if (maxDepth <= 0) return null;

  let entries;
  try {
    entries = await readdir(dir, { withFileTypes: true });
  } catch {
    return null;
  }

  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    if (entry.name.startsWith(`exercise-${subExercise}-`)) {
      return join(dir, entry.name);
    }
  }

  // Recurse into subdirectories
  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    const found = await findExerciseDir(
      join(dir, entry.name),
      subExercise,
      maxDepth - 1,
    );
    if (found) return found;
  }

  return null;
}
