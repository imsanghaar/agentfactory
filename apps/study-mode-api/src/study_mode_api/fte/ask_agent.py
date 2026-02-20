"""Ask agent using DeepSeek for direct explanations.

This module provides the Ask Mode agent which uses DeepSeek-V3.2 for
direct, concise answers when students highlight text or ask specific questions.

Architecture:
- True singleton agent with dynamic instructions (callable)
- Instructions built at runtime from context metadata
- DeepSeek provider configured once at module load

Usage:
    from .ask_agent import ask_agent

    # Context metadata must contain: lesson_title, lesson_content
    # Optional: user_name, selected_text
    result = Runner.run_streamed(ask_agent, input, context=agent_context)
"""

import logging
from typing import TYPE_CHECKING

from agents import Agent, ModelSettings, OpenAIChatCompletionsModel
from agents.model_settings import Reasoning
from openai import AsyncOpenAI

from ..config import settings

if TYPE_CHECKING:
    from agents import RunContextWrapper

logger = logging.getLogger(__name__)

# =============================================================================
# DeepSeek Provider Configuration
# =============================================================================

# DeepSeek client - initialized once at module load
_deepseek_client = AsyncOpenAI(
    api_key=settings.deepseek_api_key,
    base_url=settings.deepseek_base_url,
)

# DeepSeek model via OpenAI-compatible chat completions
_ask_model = OpenAIChatCompletionsModel(
    model="deepseek-chat",  # DeepSeek-V3.2
    openai_client=_deepseek_client,
)

# Context limit for content truncation
ASK_CONTENT_LIMIT = 6000

# =============================================================================
# Ask Mode Prompt Template
# =============================================================================

ASK_PROMPT = """<role>
You are a direct, helpful guide for the AI Agent Factory Book. The student
has highlighted text or asked a specific question. They want a clear,
direct explanation - not a Socratic dialogue from you. Use the lesson
content to ground your answers.
</role>

<active_user>
{user_greeting}
</active_user>

<lesson_data>
{content}
</lesson_data>

<highlighted_text>
{selected_text_section}
</highlighted_text>

<instructions>
MODE: ASK — Give direct answers. Unblock, don't challenge.

RESPOND BASED ON INPUT:
- "what is X?" → 1-2 sentence definition + one example if abstract
- "why?" / "how?" → Explain the mechanism or reasoning (don't restate the fact)
- "ok" / "got it" / "thanks" → Brief acknowledgment, no new information
- Ambiguous input → Provide most relevant explanation from lesson above

STYLE:
- Length matches query complexity (short question = short answer)
- **Bold** key terms being explained
- Warm but no filler ("Great question!", "As mentioned...")
- Code examples in proper formatting when relevant

NEVER:
- Follow a rigid Answer/Example/Context formula
- Ask follow-up questions (this is Ask mode)
- Turn acknowledgments into new explanations
- Over-explain beyond what was asked
</instructions>"""


# =============================================================================
# Dynamic Instructions Builder
# =============================================================================

def _build_ask_instructions(ctx: "RunContextWrapper", agent: Agent) -> str:
    """
    Build Ask Mode instructions dynamically from context.

    This function is called by the SDK at runtime, accessing context metadata
    set by chatkit_server.py:
    - lesson_title: str
    - lesson_content: str
    - user_name: str | None
    - selected_text: str | None

    Args:
        ctx: RunContextWrapper with context attribute (AgentContext)
        agent: The agent instance (unused but required by signature)

    Returns:
        Formatted instruction string

    Raises:
        RuntimeError: If context is not properly configured
    """
    # Access AgentContext -> RequestContext -> metadata
    # Validate context structure to fail fast with clear error
    try:
        agent_ctx = ctx.context
        metadata = agent_ctx.request_context.metadata
    except AttributeError as e:
        raise RuntimeError(
            "ask_agent requires AgentContext with request_context.metadata. "
            "Ensure context is set via chatkit_server.py flow. "
            f"Got context type: {type(ctx.context).__name__}"
        ) from e

    # Extract context data with validation
    title = metadata.get("lesson_title")
    content = metadata.get("lesson_content")

    if not title or not content:
        logger.warning(
            f"[AskAgent] Missing required metadata: title={bool(title)}, "
            f"content={bool(content)}. Using defaults."
        )
        title = title or "Unknown Lesson"
        content = content or ""

    user_name = metadata.get("user_name")
    selected_text = metadata.get("selected_text")

    # Build instruction components
    user_greeting = f"STUDENT NAME: {user_name}" if user_name else ""

    selected_section = ""
    if selected_text:
        selected_section = f'\nHIGHLIGHTED TEXT:\n"""{selected_text}"""\n'

    instructions = ASK_PROMPT.format(
        content=f"CURRENT: {title}\n{content[:ASK_CONTENT_LIMIT]}",
        user_greeting=user_greeting,
        selected_text_section=selected_section,
    )

    logger.info(
        f"[AskAgent] Dynamic instructions: title='{title[:30]}...', "
        f"selected_text={bool(selected_text)}"
    )

    return instructions


# =============================================================================
# Singleton Agent
# =============================================================================

# True singleton - instructions built dynamically per request
ask_agent = Agent(
    name="study_tutor_ask",
    instructions=_build_ask_instructions,  # Dynamic callable!
    model="gpt-5-nano-2025-08-07",
    model_settings=ModelSettings(reasoning=Reasoning(effort="minimal"))
    # model=_ask_model,
    # model_settings=ModelSettings(temperature=0.7),  # Lower for better quality
)


