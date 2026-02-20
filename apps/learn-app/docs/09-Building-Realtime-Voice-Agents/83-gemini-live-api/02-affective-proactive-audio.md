---
sidebar_position: 3
title: "Affective Dialog and Proactive Audio"
description: "Implement Gemini Live API's advanced conversational features: emotion detection that adapts response tone, proactive audio that decides when to speak, and background noise handling for device-directed queries."
keywords: [Gemini Live API, affective dialog, emotion detection, proactive audio, device-directed speech, voice AI, adaptive responses]
chapter: 83
lesson: 2
duration_minutes: 40

# HIDDEN SKILLS METADATA
skills:
  - name: "Implementing Affective Dialog"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can configure affective dialog to enable emotion-aware responses in voice agents"

  - name: "Configuring Proactive Audio Behavior"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can implement proactive audio that responds only to device-directed speech"

  - name: "Designing Adaptive Response Strategies"
    proficiency_level: "B1"
    category: "Applied"
    bloom_level: "Analyze"
    digcomp_area: "Problem-Solving"
    measurable_at_this_level: "Student can design response strategies that adapt to user emotional state"

  - name: "Handling Complex Audio Environments"
    proficiency_level: "B1"
    category: "Technical"
    bloom_level: "Apply"
    digcomp_area: "Digital Content Creation"
    measurable_at_this_level: "Student can configure agents to distinguish device-directed queries from background conversation"

learning_objectives:
  - objective: "Configure affective dialog to detect and respond to user emotional state"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Code successfully enables affective dialog and demonstrates adapted response tone"

  - objective: "Implement proactive audio that determines when to respond versus remain silent"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Agent correctly ignores background conversation and responds only to direct queries"

  - objective: "Design response strategies that match user emotional state"
    proficiency_level: "B1"
    bloom_level: "Analyze"
    assessment_method: "Student articulates when to use calming versus energetic response styles"

  - objective: "Handle device-directed speech detection in noisy environments"
    proficiency_level: "B1"
    bloom_level: "Apply"
    assessment_method: "Agent distinguishes between user addressing device versus background speakers"

cognitive_load:
  new_concepts: 5
  assessment: "5 concepts (affective dialog, emotion detection, proactive audio, device-directed speech, adaptive tone) within B1 limit of 7-10 concepts"

differentiation:
  extension_for_advanced: "Implement custom emotion-to-response mapping with multiple tone presets; analyze latency impact of proactive audio on response timing"
  remedial_for_struggling: "Use provided configuration templates; focus on binary proactive audio (on/off) before exploring device-directed nuances"
---

# Affective Dialog and Proactive Audio

Your voice agent from Lesson 1 responds to what users say. But in the real world, how users say something matters as much as what they say. A customer saying "I need help with my order" in a frustrated tone requires a different response than the same words spoken calmly.

Gemini Live API offers two capabilities that traditional voice pipelines cannot match: **affective dialog** that detects emotional state and adapts response tone, and **proactive audio** that intelligently decides when to respond. These features transform voice agents from rigid question-answering systems into emotionally intelligent conversational partners.

This lesson teaches you to implement both capabilities, giving your Task Manager voice agent the ability to recognize user frustration and respond with appropriate empathy---and to stay silent when users are not addressing the device.

---

## The Emotional Intelligence Gap

Traditional voice pipelines process words, not emotions:

```
Traditional Pipeline:
User speaks (frustrated) → STT → Text only → LLM → Generic response
                          ↓
              Emotion lost in transcription

Gemini Native Audio:
User speaks (frustrated) → gemini-2.5-flash-native-audio → Empathetic response
                          ↓
              Tone, pace, emotion preserved
```

When raw audio reaches the model directly, acoustic nuances survive. The model interprets tone, pace, and emotion---then generates speech that matches the appropriate register.

### Why This Matters for Production

Consider these identical sentences spoken differently:

| Words | Tone | Appropriate Response |
|-------|------|---------------------|
| "I need to cancel my subscription" | Neutral | Standard cancellation flow |
| "I need to cancel my subscription" | Frustrated | Empathetic acknowledgment, then flow |
| "I need to cancel my subscription" | Sad | Gentle inquiry about concerns |

Without affective dialog, your agent treats all three identically. With it, your agent de-escalates the frustrated user and shows appropriate care for the sad one.

---

## Configuring Affective Dialog

Affective dialog is not enabled by default. You must configure it explicitly:

### Basic Configuration

```python
from google import genai
from google.genai import types

# Note: Affective dialog requires v1alpha API version
client = genai.Client(
    api_key=os.environ.get("GOOGLE_API_KEY"),
    http_options={"api_version": "v1alpha"}
)

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    enable_affective_dialog=True,  # Enable emotion-aware responses
    speech_config=types.SpeechConfig(
        voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                voice_name="Kore"  # Warm voice for empathetic responses
            )
        )
    ),
    system_instruction=types.Content(
        parts=[types.Part(text="""
        You are a supportive Task Manager assistant.
        When users sound frustrated, acknowledge their feelings first.
        When users sound excited, match their energy.
        Keep responses warm and helpful.
        """)]
    )
)
```

**Output:**
```python
>>> # Connection with affective dialog enabled
>>> print(config.enable_affective_dialog)
True
>>> # API version required for affective features
>>> print(client._http_options.get("api_version"))
v1alpha
```

### Key Configuration Requirements

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `api_version` | `v1alpha` | Required for affective features |
| `enable_affective_dialog` | `True` | Activates emotion detection |
| `response_modalities` | `["AUDIO"]` | Must include audio for tone adaptation |
| `voice_name` | Warm voices preferred | Kore, Vesta, Orus suit empathetic responses |

---

## How Affective Dialog Works

Gemini's native audio model processes acoustic features to interpret emotional state:

### Acoustic Analysis

The model analyzes:
- **Pitch patterns**: Rising pitch may indicate frustration or questions
- **Speech rate**: Faster speech often signals urgency or excitement
- **Volume dynamics**: Louder speech may indicate frustration
- **Pause patterns**: Hesitation may signal uncertainty or sadness

### Response Adaptation

When affective dialog is enabled, the model automatically:
1. Detects emotional indicators in user speech
2. Selects appropriate response tone
3. Adjusts generated speech to match

You do not explicitly program "if frustrated, do X." The model handles this internally based on its training.

### Practical Example: De-escalation

```python
async def handle_customer_support():
    """Demonstrate affective dialog in customer support scenario."""

    config = types.LiveConnectConfig(
        response_modalities=["AUDIO"],
        enable_affective_dialog=True,
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name="Orus"  # Calm, measured voice
                )
            )
        ),
        system_instruction=types.Content(
            parts=[types.Part(text="""
            You are a customer support agent for Task Manager.

            When users express frustration:
            - Acknowledge their feelings first
            - Apologize for any inconvenience
            - Then address their issue

            When users express confusion:
            - Reassure them
            - Explain step by step
            - Offer to clarify further

            Always maintain a calm, supportive tone regardless of user emotion.
            """)]
        )
    )

    async with client.aio.live.connect(
        model="gemini-2.5-flash-native-audio-preview",
        config=config
    ) as session:
        print("[affective] Session with emotion detection active")
        # Session now adapts responses to user emotional state
```

**Output:**
```
[affective] Session with emotion detection active

Frustrated user: "This is the THIRD time I've tried to complete this task!"
Agent response: "I completely understand how frustrating that must be.
Let me help you get this resolved right now. Can you tell me
which task you're working on?"

Calm user: "I'd like to complete my weekly review task."
Agent response: "Sure! I'll mark your weekly review as complete.
Is there anything else you'd like to update?"
```

Notice the difference: the frustrated user receives acknowledgment first, then assistance. The calm user gets direct help.

---

## Proactive Audio: Speaking Only When Addressed

Traditional voice agents respond to all detected speech. In smart device scenarios, this creates problems:

```
Living Room Scene:
Person A: "What should we have for dinner?"
Person B: "I don't know, maybe pizza?"

Traditional Agent: "I can help you order pizza! Would you like..."
Everyone: [groans]
```

Proactive audio solves this. The model analyzes context to determine if speech is directed at the device.

### Enabling Proactive Audio

```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key=os.environ.get("GOOGLE_API_KEY"),
    http_options={"api_version": "v1alpha"}
)

config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={"proactive_audio": True},  # Enable smart response selection
    speech_config=types.SpeechConfig(
        voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                voice_name="Puck"
            )
        )
    ),
    system_instruction=types.Content(
        parts=[types.Part(text="""
        You are a Task Manager assistant on a smart device.
        Only respond when the user is clearly addressing you.
        Ignore background conversations.
        When addressed, be helpful and concise.
        """)]
    )
)
```

**Output:**
```python
>>> print(config.proactivity)
{'proactive_audio': True}
```

### How Proactive Audio Works

With proactive audio enabled, Gemini:

1. **Analyzes speech direction**: Is the user facing the device? Using direct address?
2. **Evaluates query relevance**: Is this a command or general conversation?
3. **Decides response strategy**: Respond, remain silent, or provide minimal acknowledgment

| Speech Type | Traditional Behavior | Proactive Audio Behavior |
|-------------|---------------------|-------------------------|
| "Hey device, add a task" | Responds | Responds |
| Background conversation | Responds (incorrectly) | Silent |
| User talking to someone else | Responds (incorrectly) | Silent |
| Ambient TV audio | May respond | Silent |

### Implementation Example: Smart Device

```python
class SmartDeviceAgent:
    """Voice agent for smart device with proactive audio."""

    def __init__(self):
        self.client = genai.Client(
            api_key=os.environ.get("GOOGLE_API_KEY"),
            http_options={"api_version": "v1alpha"}
        )
        self.session = None

    async def connect(self, device_name: str = "Task Manager"):
        """Connect with proactive audio enabled."""

        config = types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            proactivity={"proactive_audio": True},
            enable_affective_dialog=True,  # Can combine both features
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name="Aoede"
                    )
                )
            ),
            system_instruction=types.Content(
                parts=[types.Part(text=f"""
                You are {device_name}, a voice-activated task assistant.

                IMPORTANT: Only respond when users address you directly.
                Triggers include:
                - "Hey {device_name}"
                - "{device_name}, ..."
                - Questions clearly directed at you

                Do NOT respond to:
                - Background conversations
                - TV or radio audio
                - People talking to each other

                When addressed, be concise and helpful.
                """)]
            )
        )

        async with self.client.aio.live.connect(
            model="gemini-2.5-flash-native-audio-preview",
            config=config
        ) as session:
            self.session = session
            print(f"[{device_name}] Ready. Listening for direct address only.")
            await self._handle_audio()

    async def _handle_audio(self):
        """Process audio stream with proactive filtering."""
        async for response in self.session.receive():
            if hasattr(response, 'data') and response.data:
                # Model decided this query was device-directed
                print("[response] Speaking...")
                await self._play_audio(response.data)
            # Note: No response generated for background audio
```

**Output:**
```
[Task Manager] Ready. Listening for direct address only.

Background: "Did you finish the report?"
[no response - correctly ignored]

User: "Task Manager, what's on my list today?"
[response] Speaking...
"You have three tasks: prepare presentation, review contracts, and schedule team meeting."
```

---

## Combining Affective and Proactive Features

For production agents, you typically want both capabilities:

```python
class ProductionVoiceAgent:
    """Full-featured voice agent with affective and proactive audio."""

    def __init__(self):
        self.client = genai.Client(
            api_key=os.environ.get("GOOGLE_API_KEY"),
            http_options={"api_version": "v1alpha"}
        )

    async def create_session(
        self,
        voice: str = "Kore",
        affective: bool = True,
        proactive: bool = True
    ) -> types.LiveConnectConfig:
        """Create session with specified features."""

        config = types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            enable_affective_dialog=affective,
            proactivity={"proactive_audio": proactive} if proactive else None,
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=voice
                    )
                )
            ),
            system_instruction=types.Content(
                parts=[types.Part(text="""
                You are a Task Manager voice assistant.

                Behavior rules:
                1. Only respond when directly addressed
                2. Match your tone to user's emotional state
                3. Acknowledge frustration before solving problems
                4. Be concise but warm

                You help users manage tasks through natural conversation.
                """)]
            )
        )

        return config

    async def run(self):
        """Start the voice agent."""
        config = await self.create_session(
            voice="Kore",
            affective=True,
            proactive=True
        )

        async with self.client.aio.live.connect(
            model="gemini-2.5-flash-native-audio-preview",
            config=config
        ) as session:
            print("[agent] Production mode: affective + proactive")
            print("[agent] Features enabled:")
            print(f"  - Affective dialog: {config.enable_affective_dialog}")
            print(f"  - Proactive audio: {config.proactivity}")

            # Handle conversation...
            async for response in session.receive():
                await self._process_response(response)

    async def _process_response(self, response):
        """Process model responses."""
        if hasattr(response, 'text') and response.text:
            print(f"[transcript] {response.text}")

        if hasattr(response, 'data') and response.data:
            # Play audio response
            pass
```

**Output:**
```
[agent] Production mode: affective + proactive
[agent] Features enabled:
  - Affective dialog: True
  - Proactive audio: {'proactive_audio': True}

Background: "I'm so stressed about this deadline"
[no response - background conversation]

User: "Task Manager, I need help. This deadline is killing me!"
[transcript] I hear you - deadlines can be really stressful. Let me help
you prioritize. What's the most urgent thing on your plate right now?

User: "The quarterly report is due tomorrow"
[transcript] Got it. Let's focus on that. I'll move the quarterly report
to the top of your list. Would you like me to reschedule anything else
to give you more time?
```

Notice how the agent:
1. Ignored the background conversation about stress
2. Responded to the direct address with empathetic acknowledgment
3. Offered practical help after emotional acknowledgment

---

## Handling Noisy Environments

Proactive audio helps in noisy environments, but you can optimize further:

### System Instruction Strategies

```python
# For office environments
office_instructions = """
You operate in an open office environment.

Expect:
- Multiple conversations nearby
- Phone calls in background
- Video meetings from colleagues

Only respond to direct address using my name or "Task Manager".
If uncertain whether you're being addressed, ask for confirmation
rather than assuming.
"""

# For home environments
home_instructions = """
You operate in a home environment.

Expect:
- TV or music in background
- Family conversations
- Children playing

Only respond when specifically addressed. Never interrupt
family conversations or respond to media content.
"""

# For vehicle environments
vehicle_instructions = """
You operate in a vehicle environment.

Expect:
- Radio or podcasts playing
- Passenger conversations
- Road noise

Respond only to driver commands. Keep responses very brief
to minimize distraction. For complex requests, suggest
pulling over first.
"""
```

### Barge-In Behavior

With proactive audio, barge-in (interrupting the agent) works more naturally:

```python
config = types.LiveConnectConfig(
    response_modalities=["AUDIO"],
    proactivity={"proactive_audio": True},
    realtime_input_config={
        "activity_handling": "ALLOW_INTERRUPTION"  # Enable natural barge-in
    },
    # ... other config
)
```

When a user interrupts:
1. Agent stops speaking immediately
2. Proactive audio analyzes the interruption
3. If device-directed, agent responds to new query
4. If background noise, agent resumes or stays silent

---

## Voice Selection for Emotional Contexts

Different voices suit different emotional strategies:

| Voice | Character | Best For |
|-------|-----------|----------|
| **Kore** | Warm, nurturing | De-escalation, support |
| **Orus** | Calm, measured | Stressful situations |
| **Vesta** | Friendly, approachable | General assistance |
| **Charon** | Deep, authoritative | Serious matters |
| **Puck** | Energetic, youthful | Positive interactions |

### Dynamic Voice Selection Pattern

```python
def select_voice_for_context(context: str) -> str:
    """Select appropriate voice based on expected context."""

    voice_mapping = {
        "customer_support": "Kore",      # Warm for complaints
        "finance": "Charon",             # Authoritative for money matters
        "healthcare": "Orus",            # Calm for sensitive topics
        "productivity": "Aoede",         # Clear for task management
        "entertainment": "Puck",         # Energetic for fun
    }

    return voice_mapping.get(context, "Vesta")  # Default: friendly
```

**Output:**
```python
>>> select_voice_for_context("customer_support")
'Kore'
>>> select_voice_for_context("finance")
'Charon'
>>> select_voice_for_context("unknown")
'Vesta'
```

---

## Complete Implementation

Here is a complete Task Manager agent with all features:

```python
import asyncio
import os
import base64
from google import genai
from google.genai import types


class TaskManagerVoiceAgent:
    """
    Task Manager voice agent with:
    - Affective dialog (emotion detection)
    - Proactive audio (smart response selection)
    - Appropriate voice selection
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=os.environ.get("GOOGLE_API_KEY"),
            http_options={"api_version": "v1alpha"}
        )
        self.session = None

    async def start(self):
        """Start the voice agent session."""

        config = types.LiveConnectConfig(
            response_modalities=["AUDIO"],
            enable_affective_dialog=True,
            proactivity={"proactive_audio": True},
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name="Kore"
                    )
                )
            ),
            system_instruction=types.Content(
                parts=[types.Part(text="""
                You are Task Manager, a voice-activated productivity assistant.

                RESPONSE RULES:
                1. Only respond when directly addressed
                2. Acknowledge user emotions before solving problems
                3. If user sounds frustrated, empathize first
                4. If user sounds excited, match their energy
                5. Keep responses concise (under 30 words when possible)

                CAPABILITIES:
                - Add, complete, and list tasks
                - Set reminders and due dates
                - Prioritize and reschedule tasks
                - Provide encouragement when tasks are completed

                When users complete tasks, celebrate with them briefly.
                When users are overwhelmed, help them prioritize.
                """)]
            )
        )

        async with self.client.aio.live.connect(
            model="gemini-2.5-flash-native-audio-preview",
            config=config
        ) as session:
            self.session = session
            print("[task-manager] Voice agent ready")
            print("[task-manager] Features: affective dialog + proactive audio")

            # Start audio handling
            await self._audio_loop()

    async def _audio_loop(self):
        """Main audio processing loop."""
        import sounddevice as sd
        import numpy as np

        sample_rate = 16000

        # Start microphone capture
        mic_task = asyncio.create_task(self._capture_microphone(sample_rate))

        try:
            async for response in self.session.receive():
                await self._handle_response(response)
        except asyncio.CancelledError:
            pass
        finally:
            mic_task.cancel()

    async def _capture_microphone(self, sample_rate: int):
        """Capture and stream microphone audio."""
        import sounddevice as sd
        import numpy as np

        chunk_size = int(sample_rate * 0.1)  # 100ms chunks

        def callback(indata, frames, time_info, status):
            audio_bytes = (indata * 32767).astype(np.int16).tobytes()
            asyncio.create_task(self._send_audio(audio_bytes))

        with sd.InputStream(
            samplerate=sample_rate,
            channels=1,
            dtype='float32',
            callback=callback,
            blocksize=chunk_size
        ):
            while True:
                await asyncio.sleep(0.1)

    async def _send_audio(self, audio_bytes: bytes):
        """Send audio chunk to Gemini."""
        if self.session:
            await self.session.send(
                input=types.LiveClientRealtimeInput(
                    media_chunks=[
                        types.Blob(
                            mime_type="audio/pcm",
                            data=base64.b64encode(audio_bytes).decode()
                        )
                    ]
                )
            )

    async def _handle_response(self, response):
        """Handle response from Gemini."""
        import sounddevice as sd
        import numpy as np

        if hasattr(response, 'text') and response.text:
            print(f"[agent] {response.text}")

        if hasattr(response, 'data') and response.data:
            audio_bytes = base64.b64decode(response.data)
            audio = np.frombuffer(audio_bytes, dtype=np.int16)
            audio = audio.astype(np.float32) / 32767
            sd.play(audio, samplerate=16000)


async def main():
    agent = TaskManagerVoiceAgent()

    try:
        await agent.start()
    except KeyboardInterrupt:
        print("\n[exit] Shutting down...")


if __name__ == "__main__":
    asyncio.run(main())
```

**Output:**
```
[task-manager] Voice agent ready
[task-manager] Features: affective dialog + proactive audio

Background: "Should we order lunch?"
[no response - proactive audio ignores background]

User: "Task Manager, I have so much to do today. I'm overwhelmed."
[agent] I hear you - feeling overwhelmed is tough. Let's tackle this
together. What's the most important thing you need to finish today?

User: "The client presentation is due at 3pm"
[agent] Got it. I'm adding 'client presentation' as priority one.
You have about 4 hours. Would you like me to block off distractions?

User (excited): "I finished the presentation early!"
[agent] That's fantastic! Great job getting ahead of the deadline.
I've marked it complete. What would you like to tackle next?
```

---

## Try With AI

### Prompt 1: Emotion Response Design

```
I'm building a customer support voice agent using Gemini Live API.
My users often call when frustrated about product issues.

Help me design:
1. System instructions that guide empathetic responses
2. Voice selection rationale for de-escalation
3. Specific phrases the agent should use when detecting frustration
4. How to transition from empathy to problem-solving

Consider: How do I acknowledge emotions without sounding scripted?
```

**What you are learning:** Designing for emotional intelligence requires more than enabling a flag. You must craft system instructions that guide natural, contextually appropriate responses---not robotic acknowledgments.

### Prompt 2: Proactive Audio Scenarios

```
I want to deploy my Task Manager voice agent in three environments:
1. Smart speaker in a family kitchen
2. Desktop app in an open office
3. Mobile app for commuters

For each environment:
1. What proactive audio behaviors make sense?
2. What system instructions should differ?
3. What trigger phrases work best?
4. How do I handle false positives (responding when I shouldn't)?
```

**What you are learning:** Proactive audio is not one-size-fits-all. Different environments require different sensitivity levels and response strategies. Understanding context shapes how you configure intelligence.

### Prompt 3: Production Implementation

```
I have affective dialog and proactive audio working in development.
Now I need to deploy to production. Help me plan:

1. How do I test emotion detection systematically?
2. What metrics should I track for proactive audio accuracy?
3. How do I handle edge cases (sarcasm, monotone users)?
4. What fallback behavior makes sense when detection is uncertain?

My agent handles task management for busy professionals.
```

**What you are learning:** Production deployment requires systematic testing and monitoring. Emotion detection and proactive audio can fail in unexpected ways---planning for edge cases prevents user frustration.

**Safety considerations**: Affective dialog and proactive audio require careful deployment. These features analyze voice characteristics beyond words---ensure users understand and consent to emotional analysis. Emotional expression varies across cultures; test with diverse user groups. The model may occasionally respond when it should not (or vice versa); build user override mechanisms.
