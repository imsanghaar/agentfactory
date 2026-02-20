"""
Lesson chunker - splits lesson markdown into semantic teaching chunks.

Each chunk represents a single teachable concept that can be:
1. Explained by the model
2. Verified with a question
3. Re-explained if student gets it wrong

Chunking happens ONCE per lesson and is cached in Redis.
"""

import json
import logging
import re
from typing import TypedDict

from ..core.redis_cache import get_redis

logger = logging.getLogger(__name__)

# Cache TTL for chunks: 30 days (same as lesson content)
CHUNKS_CACHE_TTL = 60 * 60 * 24 * 30  # 30 days in seconds

# Chunk size limits
MIN_CHUNK_SIZE = 100  # Merge chunks smaller than this
MAX_CHUNK_SIZE = 800  # Split chunks larger than this


class LessonChunk(TypedDict):
    """A single teachable chunk from a lesson."""
    index: int
    title: str
    content: str
    chunk_type: str  # "intro", "concept", "summary"


def _clean_frontmatter(content: str) -> str:
    """Remove YAML frontmatter from markdown content."""
    if content.startswith("---"):
        # Find the closing ---
        end_match = re.search(r"\n---\n", content[3:])
        if end_match:
            return content[3 + end_match.end():].strip()
    return content


def _extract_title_from_heading(line: str) -> str:
    """Extract title from a markdown heading line."""
    # Remove heading markers and clean up
    title = re.sub(r"^#+\s*", "", line)
    # Remove any markdown formatting
    title = re.sub(r"\*\*([^*]+)\*\*", r"\1", title)  # Bold
    title = re.sub(r"\*([^*]+)\*", r"\1", title)  # Italic
    title = re.sub(r"`([^`]+)`", r"\1", title)  # Code
    return title.strip()


def _should_split_here(line: str, next_line: str | None = None) -> bool:
    """Determine if we should start a new chunk at this line."""
    # H2 headings are primary split points
    if line.startswith("## "):
        return True

    # Horizontal rules can indicate section breaks
    if line.strip() in ("---", "***", "___"):
        return True

    return False


def _get_chunk_type(title: str, index: int, total: int) -> str:
    """Determine chunk type based on title and position."""
    title_lower = title.lower()

    if index == 0:
        return "intro"

    if any(word in title_lower for word in ["summary", "conclusion", "recap", "review"]):
        return "summary"

    if index == total - 1 and "summary" not in title_lower:
        # Last chunk without explicit summary title
        return "summary"

    return "concept"


def chunk_lesson(markdown: str, lesson_title: str = "Lesson") -> list[LessonChunk]:
    """
    Split lesson markdown into semantic teaching chunks.

    Strategy:
    1. Remove frontmatter
    2. Split on ## headings (H2)
    3. Each section becomes a chunk
    4. Merge small chunks with previous
    5. Split large chunks at paragraph boundaries

    Args:
        markdown: Full lesson markdown content
        lesson_title: Fallback title for the lesson

    Returns:
        List of LessonChunk dictionaries
    """
    if not markdown or not markdown.strip():
        return [{
            "index": 0,
            "title": lesson_title,
            "content": "No content available.",
            "chunk_type": "intro",
        }]

    # Clean frontmatter
    content = _clean_frontmatter(markdown)

    # Split into lines
    lines = content.split("\n")

    # Build chunks by finding H2 boundaries
    raw_chunks: list[dict] = []
    current_chunk: dict = {
        "title": lesson_title,
        "content_lines": [],
    }

    for i, line in enumerate(lines):
        next_line = lines[i + 1] if i + 1 < len(lines) else None

        if _should_split_here(line, next_line):
            # Save current chunk if it has content
            if current_chunk["content_lines"]:
                raw_chunks.append(current_chunk)

            # Start new chunk with this heading
            title = _extract_title_from_heading(line) if line.startswith("#") else "Section"
            current_chunk = {
                "title": title,
                "content_lines": [],
            }
        else:
            # Add line to current chunk
            current_chunk["content_lines"].append(line)

    # Don't forget the last chunk
    if current_chunk["content_lines"]:
        raw_chunks.append(current_chunk)

    # If no chunks were created, make the whole thing one chunk
    if not raw_chunks:
        return [{
            "index": 0,
            "title": lesson_title,
            "content": content.strip(),
            "chunk_type": "intro",
        }]

    # Convert to final format with content as string
    chunks: list[LessonChunk] = []
    for i, raw in enumerate(raw_chunks):
        content_text = "\n".join(raw["content_lines"]).strip()

        # Skip empty chunks
        if not content_text:
            continue

        chunk_type = _get_chunk_type(raw["title"], i, len(raw_chunks))

        chunks.append({
            "index": len(chunks),  # Re-index after skipping empty
            "title": raw["title"],
            "content": content_text,
            "chunk_type": chunk_type,
        })

    # Merge small chunks with previous
    merged_chunks: list[LessonChunk] = []
    for chunk in chunks:
        if merged_chunks and len(chunk["content"]) < MIN_CHUNK_SIZE:
            # Merge with previous chunk
            prev = merged_chunks[-1]
            prev["content"] += f"\n\n### {chunk['title']}\n\n{chunk['content']}"
            # Keep the original title and type
        else:
            merged_chunks.append(chunk)

    # Re-index after merging
    for i, chunk in enumerate(merged_chunks):
        chunk["index"] = i

    # Note: We don't split large chunks here to preserve code blocks
    # The model can handle ~800 char chunks fine

    logger.info(f"[Chunker] Created {len(merged_chunks)} chunks from lesson")

    return merged_chunks


async def get_lesson_chunks(
    lesson_path: str, markdown: str, title: str = "Lesson"
) -> list[LessonChunk]:
    """
    Get lesson chunks, using Redis cache if available.

    Args:
        lesson_path: Path to lesson for cache key
        markdown: Full lesson markdown (used if not cached)
        title: Lesson title for fallback

    Returns:
        List of LessonChunk dictionaries
    """
    redis = get_redis()
    cache_key = f"lesson_chunks:{lesson_path}"

    # Try cache first
    if redis:
        try:
            cached = await redis.get(cache_key)
            if cached:
                chunks: list[LessonChunk] = json.loads(cached)
                logger.debug(f"[Chunker] Cache hit for {lesson_path}: {len(chunks)} chunks")
                return chunks
        except Exception as e:
            logger.warning(f"[Chunker] Cache read error: {e}")

    # Generate chunks
    chunks = chunk_lesson(markdown, title)

    # Cache the result
    if redis and chunks:
        try:
            await redis.setex(cache_key, CHUNKS_CACHE_TTL, json.dumps(chunks))
            logger.debug(f"[Chunker] Cached {len(chunks)} chunks for {lesson_path}")
        except Exception as e:
            logger.warning(f"[Chunker] Cache write error: {e}")

    return chunks


async def invalidate_chunks_cache(lesson_path: str) -> bool:
    """
    Invalidate cached chunks for a lesson.

    Called when lesson content is updated.
    """
    redis = get_redis()
    if not redis:
        return False

    cache_key = f"lesson_chunks:{lesson_path}"
    try:
        await redis.delete(cache_key)
        logger.info(f"[Chunker] Invalidated cache for {lesson_path}")
        return True
    except Exception as e:
        logger.warning(f"[Chunker] Cache invalidation error: {e}")
        return False
