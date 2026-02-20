# ADR 0021: Framework-First Voice AI Curriculum

**Status**: Accepted
**Date**: 2026-01-02
**Deciders**: MJS, Claude Code
**Context**: Curriculum architecture for Part 11: Building Realtime Voice Agents

---

## Context

### Problem Statement

Voice AI development has two distinct approaches:

1. **Direct API Approach**: Teach raw WebRTC/WebSocket connections to OpenAI Realtime and Gemini Live APIs first, then introduce frameworks
2. **Framework-First Approach**: Teach LiveKit Agents and Pipecat frameworks first, then show direct APIs for edge cases

Traditional voice AI curricula follow the direct API approach, starting with low-level STT -> LLM -> TTS pipelines. This matches how the technology evolved but not how production systems are built today.

### Production Reality

| System | Framework Used | Notes |
|--------|---------------|-------|
| ChatGPT Advanced Voice Mode | LiveKit Agents | Powers OpenAI's flagship voice feature |
| Shopify Sidekick | Gemini via framework | Merchant voice assistant |
| Speechmatics production | Pipecat | 40+ AI service integrations |
| Gaia.ai | Custom framework | Production voice infrastructure |

No production voice system at scale uses raw APIs directly. Frameworks handle:
- Connection management and reconnection
- VAD (Voice Activity Detection) integration
- Turn detection and barge-in
- Provider failover
- Kubernetes deployment patterns

### Educational Consideration

Students who learn direct APIs first spend significant cognitive load on:
- WebRTC SDP negotiation
- ICE candidate handling
- Audio format conversion (sample rates, PCM encoding)
- Manual VAD implementation
- Custom turn detection logic

This complexity obscures the core voice AI concepts: conversation design, latency optimization, and multi-channel integration.

---

## Decision

**Adopt Framework-First curriculum for Part 11.**

### Chapter Structure

| Chapter | Approach | Rationale |
|---------|----------|-----------|
| 61: Voice AI Fundamentals | Conceptual | Mental models before implementation |
| 62: LiveKit Agents | Framework | Production standard, powers ChatGPT Voice |
| 63: Pipecat | Framework | Flexibility, multi-provider |
| 64: OpenAI Realtime API | Direct | For edge cases, after framework foundation |
| 65: Gemini Live API | Direct | Multimodal capabilities, after framework foundation |
| 66: Phone & Browser Integration | Applied | Skills for real channels |
| 67: Capstone | Integration | Compose all learned skills |

### Rationale

1. **Matches Production Reality**: No production system uses raw APIs. Teaching frameworks first prepares students for actual work.

2. **Cognitive Load Management**: Frameworks abstract connection management, letting students focus on voice AI concepts.

3. **Faster to Value**: Students build working voice agents in Chapter 80 (LiveKit) rather than spending chapters on WebRTC basics.

4. **When to Go Deeper**: Direct APIs (Chapters 82-83) are taught as "escape hatches" for edge cases, not fundamentals.

5. **Skill-First Alignment**: L00 lessons in Chapters 80, 81, and 84 build skills from official documentation. Direct API chapters don't create skills (they're for understanding, not daily use).

---

## Consequences

### Positive

1. **Production-Ready Graduates**: Students learn tools they'll actually use
2. **Lower Initial Barrier**: Framework abstractions ease entry
3. **Proper Abstraction Ordering**: Learn to use, then learn internals
4. **Skill Portfolio**: Students exit with `livekit-agents`, `pipecat`, `voice-telephony`, `web-audio-capture` skills

### Negative

1. **Reduced Low-Level Understanding**: Some students may not understand WebRTC internals
2. **Framework Lock-In Risk**: Deep framework knowledge without API understanding could limit flexibility
3. **Curriculum Dependency**: If LiveKit or Pipecat changes significantly, content needs updating

### Mitigations

- Chapters 82-83 teach direct APIs for those who need deeper understanding
- Chapter 85 capstone requires understanding of both layers
- Modular chapter structure allows updating framework chapters independently

---

## Related Decisions

### Economy Stack Pattern

Part 11 establishes a cost-optimized voice pipeline:

| Component | Provider | Cost/min | Latency |
|-----------|----------|----------|---------|
| STT | Deepgram Nova-3 | $0.0077 | ~90ms |
| LLM | GPT-4o-mini | $0.0015 | 200-400ms |
| TTS | Cartesia Sonic-3 | ~$0.024 | 40-90ms |
| VAD | Silero VAD | Free | <1ms |
| **Total** | | **~$0.033/min** | **~600ms** |

This "economy stack" is taught as the default for production deployments, with native speech-to-speech (OpenAI Realtime, Gemini Live) as premium alternatives.

### Capstone Skills Composition

Chapter 85 (Capstone) follows Layer 4: Spec-Driven Integration:
- No new skills created
- Students compose existing skills (`livekit-agents`, `pipecat`, `voice-telephony`, `web-audio-capture`)
- Specification written BEFORE implementation
- Production targets validated against spec

This distinguishes capstones from learning chapters.

---

## Alternatives Considered

### Alternative 1: Direct APIs First (Traditional)

**Rejected because**: Spends 3+ chapters on low-level details students won't use in production. High dropout risk before building anything useful.

### Alternative 2: Only Frameworks (No Direct APIs)

**Rejected because**: Students need to understand what frameworks abstract. Edge cases require direct API knowledge.

### Alternative 3: Parallel Tracks (Framework and Direct)

**Rejected because**: Doubles content without benefit. Students should learn one approach first, then the other.

---

## References

- [LiveKit Agents Documentation](https://docs.livekit.io/agents/)
- [Pipecat Documentation](https://pipecat.ai/docs)
- [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime)
- [Gemini Live API](https://ai.google.dev/gemini-api/docs/live)
- Part 11 Chapter Plans (61-67)
