"""TeachContext dataclass for agent-native teaching mode.

This context is passed to the agent via RunContextWrapper and contains
all state needed for the teaching session.

Per reviewer's architecture: simple dataclass, no nested objects.
"""

from dataclasses import dataclass


@dataclass
class TeachContext:
    """Context passed to agent via RunContextWrapper.

    This replaces the complex server-side session state management
    with a simple dataclass that the agent can read and tools can modify.
    """

    lesson_title: str
    chunks: list[dict]  # [{index, title, content}, ...]
    current_chunk_index: int = 0
    attempt_count: int = 0
    max_attempts: int = 3
    total_chunks: int = 0
    is_first_message: bool = True
    thread_id: str = ""  # For Redis operations
    user_name: str = ""  # For personalized greeting

    @property
    def current_chunk(self) -> dict | None:
        """Get the current chunk being taught."""
        if self.current_chunk_index < len(self.chunks):
            return self.chunks[self.current_chunk_index]
        return None

    @property
    def is_complete(self) -> bool:
        """Check if lesson is complete."""
        return self.current_chunk_index >= self.total_chunks
