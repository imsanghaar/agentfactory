# Business Case: From Book to AI Employee

**Feature**: `learn-agentfactory` — a skill that turns any general agent or prebuilt AI employee into a personalized tutor for the Agent Factory curriculum

**Status**: Business case for C-team review
**Date**: 2026-02-18
**Author**: Architecture team

---

## Executive Summary

The "book" is dead. What pre-2026 called a book — a static artifact you read — is being replaced by something fundamentally different: **an AI employee that teaches you**. The content doesn't change, but the delivery model does. Instead of a human reading pages, an agent consumes structured curriculum and delivers it conversationally, adapted to the learner's context, pace, and goals.

We propose extending our learning platform with a skill that any general agent or prebuilt AI employee can install — Claude Code, OpenClaw (Telegram, WhatsApp), or any future agent platform. The MVP is approximately 2 days of engineering (3 API endpoints + 1 skill file), building entirely on existing infrastructure.

The strategic value is fourfold:

1. **Cost flip**: Shifts our model from **platform-pays-for-AI** to **user-brings-their-own-AI**, turning every interaction from a cost center into a profit center.
2. **Foundation for our AI employee**: This skill is the first module of what becomes a prebuilt AI employee — a productized agent that learns, practices, and certifies on behalf of the user. Today it teaches; tomorrow it builds.
3. **Progressive tiers**: Install locally (credits per lesson, user brings LLM) → Run on our cloud (~$2/month Docker container, user brings LLM) → Personal AI tutor (fully managed reskilling product on Nanoclaw — the actual goal). Each tier removes friction. The content and observability are the same throughout.
4. **New consumption model**: We stop shipping a book and start shipping intelligence. The same curriculum that powers our website becomes fuel for agents across every channel.

---

## 1. Where We Are Today

### What We Have (Don't Undersell)

The Agent Factory learning platform is already an interactive experience:

| Capability             | Description                                      | Status               |
| ---------------------- | ------------------------------------------------ | -------------------- |
| **Study Mode**         | AI tutoring contextual to each lesson            | Live, credit-metered |
| **Ask Mode**           | AI Q&A about specific content                    | Live                 |
| **Sign-in / SSO**      | Better Auth with OAuth PKCE                      | Live                 |
| **Quizzes**            | Gated behind sign-in, XP/badges on completion    | Live                 |
| **Practice Exercises** | ExerciseCards + local practice server            | Beta (just shipped)  |
| **Progress Tracking**  | XP, 14 badge types, streaks, leaderboard         | Live                 |
| **Content**            | 120+ structured lessons with rich YAML metadata  | Live                 |
| **Exercise Packs**     | 12 GitHub repos with downloadable exercise files | Live                 |

**Institutional backing**: PIAIC, GIAIC, Panaversity — established student bodies with real enrollment.

### The Problem We Still Have

Despite all of the above, we face four structural challenges:

**1. We're still shipping a "book."**
No matter how interactive the website is, the mental model is: go to a website, read content, take a quiz. This is the pre-2026 model. The world is moving to agents that teach, not pages you read. Our content is excellent — our delivery model is a generation behind.

**2. Cost grows with engagement.**
Every Study Mode interaction costs us an OpenAI API call. More engaged students = higher costs. Our margins narrow as we succeed.

**3. Users must come to us.**
Students leave their work environment, open a browser, navigate to our site, learn, then go back to their terminal to practice. Context-switching kills engagement. Industry completion rates for online courses: 3-5%.

**4. Distribution is limited to SEO.**
Growth depends on someone searching for "how to build AI agents" and finding our site. No viral mechanism, no integration into existing workflows, no presence where developers already spend their time.

---

## 2. The Proposal

### What We Build

A skill called `learn-agentfactory` that any user can install on their **general agent** (Claude Code, Cursor, any coding agent) or **prebuilt AI employee** (OpenClaw, custom agents on Telegram/WhatsApp). The skill turns any agent into a personalized tutor:

- Contains the curriculum structure (chapters, lessons, metadata)
- Fetches lesson content from our API on demand
- Guides the user through lessons conversationally
- Orchestrates exercises (downloads exercise packs, coaches through them)
- Reports progress (XP, completion) back to our platform

This is the first skill of what becomes a **prebuilt AI employee for learning**. Today: the agent teaches you Agent Factory content. Tomorrow: the agent helps you build agents, reviews your code, coaches your career — all powered by the same curriculum API and credit system.

### How It Works

```
User installs skill on their agent
  → User says "/learn chapter 4 lesson 3"
  → Agent reads lesson from our Content API (credit charged)
  → Agent teaches the content conversationally, adapted to user's context
  → User says "/exercise 4.1"
  → Agent fetches exercise, sets up workspace, coaches user through it
  → On completion, agent reports to Progress API (XP awarded)
```

### Where It Works

| Surface                    | Agent Type              | How                                                         |
| -------------------------- | ----------------------- | ----------------------------------------------------------- |
| **Claude Code (terminal)** | General agent           | Skill installed in `.claude/skills/`, invoked with `/learn` |
| **Cursor / Windsurf**      | General coding agent    | Same skill format, same API                                 |
| **Telegram / WhatsApp**    | Prebuilt AI employee    | Via OpenClaw or similar AI employee platforms               |
| **Any future agent**       | General or prebuilt     | Portable skill format works in any compatible agent         |
| **Our own website**        | Platform-embedded agent | Future: web becomes another channel using the same model    |

---

## 3. The Design Journey (How We Got Here)

This section documents the push-backs that refined the concept. Each challenge led to a sharper understanding.

### Initial Idea

> "Ship a CLI with the full book. Users learn from anywhere."

**Push-back**: A CLI that displays book content is just a worse website. No one reads word-by-word. The "book" as a delivery format is dying — what's the actual value of putting it in a terminal?

### Refinement 1: Content Is For The Agent

> "The content isn't rendered — it's consumed by the agent and re-delivered conversationally. The MDX is training material for the tutoring agent, not display content for the student."

**Push-back**: We already have Study Mode and Ask Mode on the web. The site isn't passive. What does the agent skill offer that the web doesn't?

### Refinement 2: Location, Not Capability

> "The web app can already teach. The agent skill brings that teaching to where you work. The delta is location and context, not capability."

| Web Platform (today)             | Agent Skill (proposed)                            |
| -------------------------------- | ------------------------------------------------- |
| AI tutor in lesson context       | AI tutor in YOUR work context                     |
| Q&A about content                | Q&A while building a real project                 |
| Quiz-based assessment            | Exercise verification by agent watching your work |
| Practice server (separate setup) | Agent orchestrates practice + coaches             |
| Progress on one platform         | Progress across all channels                      |

**Push-back**: OK, but if we make the web more interactive to compete, we bear the LLM costs. Every improvement to Study Mode increases our OpenAI bill.

### Refinement 3: The Cost Flip

> "With the agent skill model, the LLM cost is on the user. We only serve content — which is a Redis cache hit, effectively free. This flips our unit economics."

**Push-back**: If this model works externally, why not bring it back to our own platform?

### Refinement 4: Platform Convergence

> "Exactly. If agent-fetches-content works in terminal and Telegram, the web site becomes just another channel. We stop paying for AI and start serving content. The platform becomes agent-native — which is literally what we teach."

This is the final architecture:

```
Content API (serves lessons, meters credits, tracks progress)
     │
     ├── Terminal (Claude Code)     ─── user's agent fetches + teaches
     ├── Telegram (OpenClaw)        ─── user's agent fetches + teaches
     ├── WhatsApp (OpenClaw)        ─── user's agent fetches + teaches
     └── Our Website (future)       ─── user's agent fetches + teaches
                                        (replaces our Study Mode costs)
```

All surfaces are equal channels. The agent — whether a general agent or a prebuilt AI employee — is the unifying intelligence layer. We provide curriculum + tracking + certification. The "book" becomes a curriculum API. The reader becomes an agent. The experience becomes personalized.

---

## 4. Economics

### Current Model: Platform Pays For AI

```
User → Website → Study Mode → OUR OpenAI API → WE PAY
```

- Every Study Mode interaction costs us ~$0.01-0.10 in API calls
- Credits charged to users may not fully cover compute
- More engaged users = higher costs
- Scaling: revenue grows linearly, costs grow linearly (or worse)

### Four Steps (Each Adds Control)

Each step increases what Panaversity owns. Each step is a separate product decision — we only advance when the previous step proves demand.

#### Step 0: Skill on their agent (MVP)

```
User installs skill on Claude Code / Cursor / any agent
  → Auth via CLI (device code flow)
  → Skill fetches content from Content API (credits deducted per lesson)
  → Observability: usage, progress tracked on our platform
  → User bears all costs (their LLM, their machine)
```

- **We own**: Content API, progress tracking, credit metering
- **We don't own**: The agent runtime, the LLM, the compute
- Zero cost for us — user runs everything, we serve cached content
- Credits per lesson fetch (existing metering system)
- Perfect for: developers already in Claude Code / Cursor who won't install another agent
- This is the **distribution hook** — lightest touch, widest reach

#### Step 1: Our own agent, their machine (forked Nanoclaw)

```
User installs Panaversity Learning Agent (forked Nanoclaw)
  → Runs locally on their machine (same UX as installing OpenClaw)
  → Teaching intelligence baked into the agent
  → Full observability: every LLM call, every interaction, every learning moment
  → User brings their own LLM (connects API key)
```

- **We own**: The agent runtime + content API + progress + observability
- **We don't own**: The LLM inference, the compute
- Users are on OUR agent from day one — not a plugin on someone else's platform
- Full control over teaching quality (agent enforces our pedagogical rules)
- Works from terminal, Telegram, WhatsApp — same agent everywhere
- Perfect for: PIAIC/GIAIC students, anyone who wants the dedicated learning experience
- Content credits still apply — same revenue model as Step 0

#### Step 2: Our compute + memory + personalization, their LLM (~$2/month)

```
User → Panaversity Cloud (our agent hosted) → User connects their LLM
  → Same agent as Step 1, but we host it
  → Persistent memory across all sessions
  → Personalization engine active (knows your history, weak areas, pace)
  → User brings their own LLM inference
```

- **We own**: Agent runtime + compute + memory + personalization + observability
- **We don't own**: The LLM inference (user connects their API key)
- ~$2/month for hosted container — user doesn't need a dev environment
- Persistent memory is the key upgrade: the agent REMEMBERS you across sessions
- Personalization engine uses accumulated progress data to adapt teaching
- Perfect for: mobile-first learners, students who want persistence without paying for LLM
- Margin: $2/month covers container; content credits + personalization value on top

#### Step 3: We own inference too — the premium product (pricing TBD)

```
User → Panaversity AI Tutor → WE HANDLE EVERYTHING
  → Our agent, our compute, our LLM
  → Full 6-mode orchestration (Tutor/Coach/Socratic/Mentor/Simulator/Manager)
  → Persistent memory + deep personalization + Feynman overlay
  → This is the personal AI employee for reskilling that actually works
```

- **We own**: Everything — runtime, compute, LLM, memory, personalization, orchestration
- A **personal AI employee for reskilling that actually works** — this is the real product
- The agent knows: learner's history, weak areas, pace, goals, work context
- Always available — Telegram, WhatsApp, terminal, web — same agent, same memory
- Pricing TBD (depends on LLM + compute cost model — needs validation before committing numbers)
- Perfect for: enterprise reskilling, institutional cohorts, anyone who wants it to "just work"

#### The Progression: What We Own At Each Step

```
                        Step 0    Step 1    Step 2    Step 3
                        (Skill)   (Agent)   (Cloud)   (Premium)
─────────────────────────────────────────────────────────────
Content API              ✓         ✓         ✓         ✓
Progress + Credits       ✓         ✓         ✓         ✓
Agent Runtime                      ✓         ✓         ✓
Full Observability                 ✓         ✓         ✓
Compute                                      ✓         ✓
Persistent Memory                            ✓         ✓
Personalization                              ✓         ✓
LLM Inference                                          ✓
6-Mode Orchestration                                   ✓
─────────────────────────────────────────────────────────────
What user pays:       credits   credits   ~$2/mo    TBD/mo
                                          +credits  (all-in)
```

Each step adds control AND value. Each step is gated by the previous step proving demand. The Content API is the constant — everything builds on top of it.

### Revenue Streams

**Stream 1: Content Access Credits (New)**

- Every lesson fetch = 10-50 credits (1-5 cents)
- Full chapter (~10 lessons) ≈ $0.50
- Complete book (~120 lessons) ≈ $6
- Implementation: one new pricing row in existing metering system

**Stream 2: AI Tutoring Credits (Existing, amplified)**

- Agent skill drives more "explain this" and "give me another example" interactions
- These can be metered through the same content API
- Volume increases because learning happens in workflow, not scheduled sessions

**Stream 3: Exercise + Certification (Existing + New)**

- Exercise completion verification: credit charge
- Certificate generation ("Agent Factory Certified Builder — Level 2"): premium gate
- Enterprise team certification tracking: institutional pricing
- Quizzes + badges already exist — certificate is the upsell

**Stream 4: Our Agent Install Base (Step 1, future)**

- Users install Panaversity Learning Agent (forked Nanoclaw) locally
- Same content credits as Step 0, but we own the runtime and get full observability
- Observability data feeds personalization engine
- Revenue: content credits (same as Step 0, but better data + upgrade path)

**Stream 5: Cloud Hosting + Personalization (~$2/month, Step 2)**

- Hosted agent per user — lightweight compute, persistent memory
- User connects their own LLM (we don't pay for AI inference)
- Memory + personalization active (the key differentiator over Step 0/1)
- Revenue: hosting fee + content credits

**Stream 6: Personal AI Employee (Premium, Step 3)**

- Fully managed reskilling product on forked Nanoclaw — we own inference too
- We pay for compute AND LLM — fully managed experience
- Pricing TBD pending cost validation (compute + LLM per user)
- Institutional tier: PIAIC/GIAIC cohorts at bulk pricing
- Revenue: subscription (MRR) — the actual business if it works

### Unit Economics Comparison

| Metric           | Free (Web)             | Step 0 (Skill) | Step 1 (Our Agent) | Step 2 (~$2/mo)  | Step 3 (Premium)   |
| ---------------- | ---------------------- | -------------- | ------------------ | ---------------- | ------------------ |
| What user pays   | Free                   | Credits        | Credits            | ~$2/mo + credits | Subscription (TBD) |
| Who owns runtime | Us (web)               | Their agent    | **Us** (Nanoclaw)  | **Us** (hosted)  | **Us** (managed)   |
| Who pays for LLM | Us                     | User           | User               | User             | **Us**             |
| Who pays compute | Us                     | User           | User               | **Us** (~$2/mo)  | **Us**             |
| Observability    | Web analytics          | Limited        | **Full**           | **Full**         | **Full**           |
| Memory/Personal. | None                   | None           | Local only         | **Server-side**  | **Server-side**    |
| Our cost/user    | $0.01-0.10/interaction | ~$0            | ~$0                | ~$2/mo           | Compute+LLM (TBD)  |
| Our revenue/user | $0                     | Credits        | Credits            | $2/mo + credits  | Subscription (TBD) |

---

## 5. Growth Mechanics

### Mechanic 1: Skills As Distribution

Skills spread through developer environments like npm packages through codebases. A colleague sees `learn-agentfactory` in a developer's `.claude/skills/` directory, asks about it, installs it. Zero-cost user acquisition.

### Mechanic 2: Learn At Point Of Need

Developer stuck building an agent types `/learn exercise 5.1` right in their terminal. No context switch. This is the "learn at point of need" model that enterprise training companies (Pluralsight, LinkedIn Learning) charge $50-200/user/month for.

### Mechanic 3: The Flywheel

```
Install skill → Agent teaches you to build agents → You build agents → You succeed → You recommend → New installs
```

Every successful student is a walking advertisement. Agent-delivered tutoring makes success more likely than reading a book, which accelerates the flywheel. And the irony sells itself: _you learned to build AI agents from an AI agent_.

### Mechanic 4: Multi-Channel Reach

The website is limited to browser users. The agent skill works on every platform that supports agent skills — terminal, messaging apps, IDEs. Each new platform that adopts skill standards = free distribution channel.

### Mechanic 5: Institutional Scale (PIAIC/GIAIC)

- Mobile-first students learn via Telegram/WhatsApp where laptop access is limited
- Instructors track progress across channels (some students use web, some use agent)
- Institutional bulk credit purchases for student cohorts
- Government-backed programs = potential for large-scale adoption

---

## 6. Teaching Intelligence: What's In The Skill vs. What's On The Server

### The IP Question

If the skill file contains our full teaching methodology (6 modes, Feynman loops, orchestration logic), anyone who installs it can read and copy it. Should we embed the teaching intelligence in the skill?

**No.** And here's why it doesn't matter:

### Teaching techniques are not the moat

Any user can already prompt an LLM: "Use the Socratic method to teach me about agents." The techniques — Socratic questioning, Feynman teach-back, coaching drills — are public knowledge. Embedding them in a skill file doesn't give us competitive advantage and doesn't take it away.

### What IS the moat: memory + personalization + orchestration

| Capability             | Skill (Tier 1/2)                                                                 | Personal AI Employee (Tier 3)                                                                   |
| ---------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Memory**             | None. General agents forget between sessions. AI employees have limited context. | Persistent across ALL sessions. Remembers every interaction, every mistake, every breakthrough. |
| **Personalization**    | None. The agent teaches the same way every time.                                 | Deep. Knows your weak areas, your pace, your learning style, your goals. Adapts in real-time.   |
| **Mode orchestration** | User's LLM does its best with content + metadata hints                           | Server-side 6-mode routing (Tutor/Coach/Socratic/Mentor/Simulator/Manager) with Feynman overlay |
| **Mastery tracking**   | Basic: lessons consumed, exercises completed                                     | Advanced: skill gaps identified, mastery scores, targeted remediation                           |
| **Teaching quality**   | Medium. Good enough to be useful.                                                | Premium. This is what "a personal AI employee that actually works" means.                       |

### The architecture

```
Skill (distributed, readable)           Server (proprietary, protected)
──────────────────────────────          ─────────────────────────────────
Content API access                      6-mode agent orchestration
Basic teaching prompts                  Feynman learning loop engine
Curriculum tree + metadata              Persistent learner memory
Progress reporting                      Personalization engine
Observability (usage tracking)          Mastery tracking + gap analysis
                                        Mode routing algorithms
  → The hook                              → The product
```

The skill is intentionally "good enough" — it delivers content through the user's AI, tracks progress, gives basic teaching guidance. This is the **hook**.

The premium product is everything the skill CAN'T do: remember you across sessions, adapt to your weaknesses, route between 6 teaching modes based on what you need right now, validate your understanding through Feynman teach-back loops. This intelligence runs on our servers, not in a readable skill file.

### Why this is clean freemium

The skill's limitations are the upgrade path:

- "My agent taught me chapter 4, but it forgot everything when I started chapter 5" → **Upgrade to persistent memory**
- "I keep getting stuck on the same concepts but the agent doesn't notice" → **Upgrade to personalization**
- "I want actual Socratic questioning, not just 'explain this back to me'" → **Upgrade to 6-mode orchestration**

The skill makes users WANT the premium product by showing them what agent-delivered learning feels like — then showing them it could be much better.

### Not competing with 6 modes — establishing their base

The skill and the 6-mode teaching intelligence are **different layers of the same system**, not competing products.

**What the skill MVP builds that the 6 modes need:**

```
Skill MVP (2 days)                     What it establishes for 6 modes
──────────────────                     ──────────────────────────────────
GET /content/tree                  →   The curriculum API that ALL agents consume
GET /content/lesson                →   Content delivery pipeline (cache, auth, metering)
POST /content/complete             →   Progress reporting that ALL tiers use
Auth (device code + JWT)           →   Cross-channel identity that Tier 3 needs
Credit metering for content        →   Revenue infrastructure for all tiers
Observability (usage tracking)     →   Data pipeline that feeds personalization engine
```

Without the Content API, the 6-mode agents have no content to teach from. Without the progress infrastructure, personalization has no history to personalize against. Without the observability layer, the Manager agent has no learning data to orchestrate from.

**The skill is the foundation, not a competitor:**

| Work Stream                 | What It Builds                                       | Dependency                           |
| --------------------------- | ---------------------------------------------------- | ------------------------------------ |
| **Skill MVP**               | Content API, auth, metering, progress, observability | None — this goes first               |
| **Personalization persona** | Learner model, adaptive teaching, memory             | Needs progress data from Content API |
| **Socratic persona**        | Teach-me mode, questioning patterns                  | Needs content from Content API       |
| **6-mode orchestration**    | Mode routing, Feynman loops, mastery tracking        | Needs all of the above               |

The skill proves demand (do people want agent-delivered learning?), generates the user base (who upgrades to premium?), and builds the infrastructure (Content API, progress pipeline, observability) that the 6-mode agents consume.

**Timeline:**

```
Month 1:  Step 0 (Skill MVP) ships → proves demand, builds Content API infrastructure
          Personas continue 6-mode work independently
Month 2:  Step 1 (Forked Nanoclaw) ships → our agent, full observability, user base on our runtime
          Observability data starts feeding personalization engine
Month 3:  Step 2 (Cloud + memory) ships → persistent memory, personalization active
          Personalization engine consuming progress + observability data
Month 4+: Step 3 (Premium tutor) ships → 6-mode agents + personalization + we own inference
          Powered by the same Content API that Step 0 established
```

### Active development

Two dedicated personas are currently building the teaching intelligence:

1. **Personalization persona**: Building the learner model, adaptive teaching, memory systems
2. **Socratic persona**: Implementing teach-me mode with proper Socratic questioning patterns

Their work powers both the web platform AND the Tier 3 personal tutor. The skill (Tier 1/2) builds the content and progress infrastructure they both depend on. The skill is the base layer — not an alternative to the 6 modes, but a prerequisite for them.

---

## 7. Competitive Moat

| Asset                                           | Why It's Defensible                                                                                                                       |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **120+ structured lessons with YAML metadata**  | Skills, objectives, cognitive load, differentiation paths. Months to build. The metadata is what makes agent-delivered teaching work.     |
| **6-mode teaching intelligence (server-side)**  | Tutor/Coach/Socratic/Mentor/Simulator/Manager orchestration + Feynman overlay. Runs on our backend. Not in the skill file. Not copyable.  |
| **Persistent learner memory + personalization** | Cross-session memory, adaptive teaching, mastery tracking. This is what makes the tutor "actually work." Cannot be replicated by a skill. |
| **Integrated infrastructure**                   | SSO + metering + progress + exercises. A competitor needs all four systems.                                                               |
| **12 exercise packs**                           | GitHub repos with structured exercises mapped to practice server. Hands-on learning, not just reading.                                    |
| **Network effects**                             | XP, badges, leaderboard, certification. Switching costs increase with student investment.                                                 |
| **Institutional relationships**                 | PIAIC/GIAIC partnerships. Not easily replicable.                                                                                          |
| **Own agent runtime (forked Nanoclaw)**         | Users on our runtime = full observability + control + upgrade path. Not dependent on Claude Code or OpenClaw's roadmap.                   |
| **First-mover on agent-delivered education**    | Curriculum API + own agent + credit system + progress tracking + server-side teaching intelligence. We define the category.               |

---

## 8. Risk Analysis

| Risk                                           | Severity | Probability | Mitigation                                                                                                                                                |
| ---------------------------------------------- | -------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Users won't pay for content that's free on web | Medium   | Medium      | Value isn't content — it's personalized agent tutoring. Netflix vs. public library.                                                                       |
| Low adoption of agent skill                    | Medium   | Medium      | Start with Claude Code (core user base). Expand channels only if traction.                                                                                |
| C-team concern about focus/distraction         | Medium   | High        | MVP is ~2 days. Kill if no traction in 30 days.                                                                                                           |
| Auth complexity across channels                | Medium   | Low         | Device code flow for CLI. OpenClaw handles its own auth.                                                                                                  |
| Cannibalization of web traffic                 | Low      | Low         | Web stays free. Skill is additive — different user behavior.                                                                                              |
| Content quality in agent delivery              | Low      | Low         | YAML metadata already structures agent teaching.                                                                                                          |
| OpenClaw/agent platform risk                   | Medium   | Medium      | Skill format is portable. Not locked to one platform.                                                                                                     |
| Skill file leaks teaching IP                   | Low      | Low         | Teaching techniques are public knowledge. Moat is server-side: memory, personalization, orchestration. Skill is intentionally "good enough," not premium. |

---

## 9. Implementation

### What We Build (MVP)

| Component                       | Description                                                       | Effort      |
| ------------------------------- | ----------------------------------------------------------------- | ----------- |
| Book tree manifest              | JSON file generated from filesystem (chapters, lessons, metadata) | 1 hour      |
| `GET /api/v1/content/tree`      | Serve book manifest                                               | 30 min      |
| `GET /api/v1/content/lesson`    | Serve content + deduct credits + mark progress                    | 4 hours     |
| `POST /api/v1/content/complete` | Mark exercise done + award XP                                     | 2 hours     |
| Pricing row                     | `model: "content-access"` in metering DB                          | 5 min       |
| `learn-agentfactory` skill      | SKILL.md with book tree, auth flow, teaching prompts              | 4 hours     |
| **Total**                       |                                                                   | **~2 days** |

### What We Reuse (Zero New Infrastructure)

| Existing System        | What We Reuse                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------ |
| **study-mode-api**     | Content loader (GitHub → Redis), JWT auth, metering client, rate limiter, Redis pool |
| **token-metering-api** | Credit check/deduct/release, reservation system, pricing table                       |
| **progress-api**       | Lesson completion, XP calculation, badge engine, leaderboard                         |
| **SSO (Better Auth)**  | JWT/JWKS validation, user identity                                                   |
| **Redis**              | Same instance, content already cached with 30-day TTL                                |

### What We Don't Build (MVP Scope)

- No new service or deployment
- No new database
- No new Redis instance
- No Telegram/WhatsApp integration (future, if MVP succeeds)
- No web platform changes (future convergence phase)

---

## 10. Success Criteria (30-Day MVP Evaluation)

| Metric                       | Target            | How Measured                                          |
| ---------------------------- | ----------------- | ----------------------------------------------------- |
| Skill installations          | 50+ unique users  | Content API auth'd requests                           |
| Lesson fetches               | 500+ total        | Metering API transactions with model="content-access" |
| Exercise completions         | 100+              | Progress API lesson/complete calls from API source    |
| Revenue from content credits | $25+              | Metering API revenue report                           |
| Repeat usage (>3 lessons)    | 30% of installers | Progress API user analysis                            |
| User feedback                | Net positive      | Direct feedback channel                               |

**Kill criteria**: If after 30 days, fewer than 20 unique users have fetched more than 3 lessons each, deprecate the skill and endpoints.

---

## 11. Future Vision (If Step 0 MVP Succeeds)

### Step 1: Our Own Agent — Forked Nanoclaw (Month 2)

- Fork Nanoclaw, ship as "Panaversity Learning Agent"
- Users install locally (same UX as installing OpenClaw)
- Teaching intelligence baked into our agent runtime
- Full observability from day one — every LLM call, every interaction
- Works from terminal, Telegram, WhatsApp — same agent everywhere
- Institutional pilot with PIAIC/GIAIC cohort on our agent
- Users on OUR runtime from this point forward

### Step 2: Cloud + Memory + Personalization (Month 3-4)

- Host our agent on our cloud (~$2/month per user)
- User connects their own LLM (we don't pay for inference yet)
- **Persistent memory** active — agent remembers across all sessions
- **Personalization engine** consuming observability + progress data
- Institutional deployment for PIAIC/GIAIC cohorts at scale
- Platform convergence: web platform also connects to same Content API

### Step 3: Premium AI Tutor — We Own Inference (Month 4-6, the actual goal)

- We add LLM inference — fully managed experience
- Full 6-mode orchestration (Tutor/Coach/Socratic/Mentor/Simulator/Manager)
- Feynman learning overlay active
- This is the **personal AI employee for reskilling that actually works**
- Each learner's agent knows their history, weak areas, pace, and goals
- The learning agent becomes one module of a broader **AI Employee** product
- Additional skills: code review, project scaffolding, deployment coaching
- Pricing validated against actual compute + LLM costs

### Beyond: Curriculum Marketplace (Month 9+)

- Other educators publish curricula through the same Content API
- Agent Factory becomes a curriculum marketplace, not just one course
- Revenue from platform fees on third-party content
- Any AI employee can install any curriculum skill — open ecosystem

### The Paradigm Shift

What we called a "book" in pre-2026 was a static artifact: chapters, pages, reading. What replaces it is a **living curriculum consumed by agents**. The student never reads — the agent reads, synthesizes, and teaches. The content is still structured (chapters, lessons, exercises), but the delivery is fundamentally different: personalized, conversational, available in every channel, and powered by the learner's own AI.

This skill is the first step in that transition. It proves the model works. If it does, the "book" concept is retired and replaced by agent-delivered education — which is, fittingly, exactly what Agent Factory teaches people to build.

---

## Appendix A: Architecture Diagram

```
                    ┌─────────────────────────┐
                    │   Content API            │
                    │   (study-mode-api ext.)  │
                    │                          │
                    │   /content/tree          │
                    │   /content/lesson        │
                    │   /content/complete      │
                    └──────────┬───────────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
     ┌────────────┐   ┌──────────────┐  ┌──────────────┐
     │ Token      │   │ Progress     │  │ Redis Cache  │
     │ Metering   │   │ API          │  │ (content +   │
     │ API        │   │ (XP/badges)  │  │  rate limit) │
     │ (credits)  │   │              │  │              │
     └────────────┘   └──────────────┘  └──────────────┘

              ▲                ▲                ▲
              │                │                │
              └────────────────┼────────────────┘
                               │
                    ┌──────────┴───────────┐
                    │   User's Agent       │
                    │   General agent OR   │
                    │   Prebuilt AI employee│
                    │   (skill installed)  │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
     ┌────────────┐   ┌──────────────┐  ┌──────────────┐
     │ Claude Code│   │ Telegram     │  │ Web Platform │
     │ Cursor etc.│   │ / WhatsApp   │  │ (future)     │
     │ (general)  │   │ (AI employee)│  │              │
     └────────────┘   └──────────────┘  └──────────────┘
```

## Appendix B: Existing Infrastructure Detail

### study-mode-api (port 8000)

- FastAPI + OpenAI ChatKit Server
- Redis: content cache (30d TTL), thread cache (1h), rate limiting (Lua scripts)
- Auth: JWT/JWKS from SSO, dev mode bypass
- Metering: 3-step reservation (check/deduct/release), fail-open
- Content: fetches from GitHub raw, caches in Redis
- Deployment: Docker multi-stage, horizontally scalable

### token-metering-api (port 8001)

- FastAPI + SQLModel + PostgreSQL + Redis
- Single unified credit balance (1 credit = $0.0001)
- Cost-weighted pricing per model, 20% platform markup
- Reservations via Redis sorted sets (atomic, idempotent)
- Starter balance: 20,000 credits (~$2 per new user)
- Inactivity expiry: 365 days

### progress-api (port 8002)

- FastAPI + SQLAlchemy + PostgreSQL + Redis
- XP calculation with diminishing returns on retries
- 14 badge types (milestone, achievement, streak, part completion, capstone)
- Lesson completion: idempotent (ON CONFLICT DO NOTHING)
- Leaderboard: materialized view, debounced refresh
- Streak tracking via activity_days table
