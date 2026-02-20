"""FTE (Full-Time Equivalent) Agent System.

This module provides the agent orchestration layer:
- teach_agent.py: Agent-native teaching mode with function tools
- teach_context.py: Teaching context management
- teach_instructions.py: Dynamic instructions for teaching
- ask_agent.py: Ask mode agent using DeepSeek
- answer_verification.py: Answer verification utilities
"""

from .ask_agent import ASK_PROMPT, ask_agent
from .teach_agent import create_teach_agent
from .teach_context import TeachContext

__all__ = [
    # Teach agent (agent-native mode)
    "create_teach_agent",
    "TeachContext",
    # Ask agent (DeepSeek) - singleton with dynamic instructions
    "ask_agent",
    "ASK_PROMPT",
]
