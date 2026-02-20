import { useState, useEffect, type ReactNode } from "react";
import Link from "@docusaurus/Link";
import Layout from "@theme/Layout";
import { ChevronDown, ChevronRight, ExternalLink, Play, CheckCircle2, Circle, Target, Zap, BookOpen } from "lucide-react";

// ============================================================================
// CHECKPOINT DATA
// ============================================================================

interface Checkpoint {
  id: string;
  title: string;
  goal: string;
  status: "locked" | "active" | "completed";
  actions: string[];
  constraints?: string[];
  deliverables: string[];
  helpingLessons: string;
  lessonsLink?: string;
  additionalContext?: string;
  successSignal: string;
}

const checkpoints: Checkpoint[] = [
  {
    id: "A1",
    title: "Extract Your Human Job Into Skills",
    goal: "Turn what you already do into 3–5 focused, reusable capabilities that replace parts of your own job and could help others with similar work.",
    status: "active",
    actions: [
      "Describe your daily/weekly work to Claude Code",
      "Identify repeatable cognitive tasks (decisions, writing, analysis, coordination)",
      "Implement 3–5 narrow, measurable skills that: (1) you actually use, (2) save time or reduce mental load, (3) could be reused by someone like you",
    ],
    constraints: [
      "Skills must be small (100–900 LOC is fine)",
      "Each skill must have one clear outcome",
      "Each skill must be measurable",
    ],
    deliverables: [
      "3–5 skills (Claude Code / General Agent)",
      "A short README.md describing what each skill replaces and time saved / quality improved",
      "One 60–90 second demo (screen recording) — Use Loom Chrome Extension to record easily",
    ],
    helpingLessons: "Part 2, Chapter 5: Claude Code Features",
    lessonsLink: "/docs/AI-Tool-Landscape/claude-code-features-and-workflows",
    successSignal: "At least one skill replaces a manual task for you this week.",
  },
  {
    id: "A2",
    title: "Set Up Your General Agent Vault",
    goal: "Transform Claude Code from a chatbot with amnesia into a trained operator with permanent memory, governance rules, and explicit skills.",
    status: "locked",
    actions: [
      "Install Obsidian and create your skills-lab vault",
      "Write AGENTS.md with governance rules and skill/agent formats",
      "Create CLAUDE.md that references your governance",
      "Test that Claude Code reads and follows your vault context",
      "Enable hidden files to see .claude/skills/ in Obsidian",
    ],
    constraints: [
      "Start with ONE vault (don't overcomplicate)",
      "Skills are teaching, not prompting",
      "No MCP needed for vault access — filesystem is simpler",
    ],
    deliverables: [
      "Obsidian vault with AGENTS.md and CLAUDE.md",
      ".claude/skills/ and .claude/agents/ directories visible in Obsidian",
      "Claude Code successfully responds with vault-specific knowledge",
    ],
    helpingLessons: "Chapter 6: Setting Up Your AI Vault",
    lessonsLink: "/docs/AI-Tool-Landscape/business-workflow-and-social-media/setting-up-your-ai-vault",
    successSignal: "Claude Code knows your rules without you re-explaining them.",
  },
  {
    id: "A3",
    title: "Automate Your Public Presence",
    goal: "Your social media and business communication runs without manual effort.",
    status: "locked",
    actions: [
      "Build an email management skill (drafts, categorization, follow-ups)",
      "Create a social media content skill (repurpose your work into posts)",
      "Publish at least 3 posts about what you built",
    ],
    constraints: [
      "Skills must live in your vault from A2",
      "Content must be original insight, not template spam",
      "Each skill must save measurable time",
    ],
    deliverables: [
      "Email assistant skill with measurable impact",
      "Content repurposing skill",
      "3+ public posts demonstrating your skills",
    ],
    helpingLessons: "Chapter 6: Email-1 through Email-7",
    lessonsLink: "/docs/AI-Tool-Landscape/business-workflow-and-social-media",
    successSignal: "You posted this week without manually writing the posts.",
  },
  {
    id: "A4",
    title: "Financial Intelligence Integration",
    goal: "Claude Code is embedded in your professional money workflows.",
    status: "locked",
    actions: [
      "Build a financial tracking/analysis skill for YOUR situation",
      "Create invoice, expense, or budget automation",
      "Integrate with your actual tools (Sheets, accounting software)",
    ],
    constraints: [
      "Must use your real financial data (anonymized if needed)",
      "Skills must produce actionable output, not just reports",
      "Integration must work without manual copy-paste",
    ],
    deliverables: [
      "Finance skill tailored to your workflow",
      "Integration with at least one real financial tool",
      "Documentation of time/accuracy improvements",
    ],
    helpingLessons: "Chapter 7: Claude Code for Finance",
    lessonsLink: "/docs/AI-Tool-Landscape/claude-code-for-finance",
    successSignal: "You can generate last month's financial summary in under 60 seconds.",
  },
  {
    id: "A5",
    title: "Share Your Skills With Your Domain",
    goal: "Your skills become valuable to professionals who share your domain expertise — packaged, documented, and used by someone other than you.",
    status: "locked",
    actions: [
      "Package 2–3 of your best skills for external use",
      "Write clear documentation: what it does, how to use it, what it replaces",
      "Share with colleagues, community, or domain professionals",
      "Collect feedback and iterate",
    ],
    constraints: [
      "Skills must solve real problems in your domain",
      "Documentation must be clear enough for someone else to use without your help",
      "At least one skill must be used by someone outside your immediate circle",
    ],
    deliverables: [
      "2–3 packaged skills with README documentation",
      "Distribution method (GitHub, community forum, direct share)",
      "Feedback from at least one external user",
      "Iteration based on real-world usage",
    ],
    helpingLessons: "Chapter 5: Claude Code Features — Skill Sharing",
    lessonsLink: "/docs/AI-Tool-Landscape/claude-code-features-and-workflows",
    successSignal: "Someone you don't work with daily is using your skill.",
  },
  {
    id: "B1",
    title: "Build Your First Custom Agent",
    goal: "Ship a production-ready agent using an SDK.",
    status: "locked",
    actions: [
      "Choose your SDK (OpenAI Agents, Claude SDK, or Google ADK)",
      "Build an agent that solves a real problem from your domain",
      "Add memory, tools, and proper error handling",
      "Write an eval suite that proves it works",
    ],
    deliverables: [
      "Working agent with SDK of choice",
      "MCP server for external integrations",
      "Eval suite with passing tests",
      "Pricing page (even if you don't sell yet)",
    ],
    helpingLessons: "Part 6: Chapters 33-47",
    lessonsLink: "/docs/AI-Native-Software-Development/introduction-to-ai-agents",
    successSignal: "You could invoice someone for this agent today.",
  },
  {
    id: "B2",
    title: "Build Reusable Agent Interface",
    goal: "Extract your B1 agent into a production-grade interface pattern — FastAPI backend, ChatKit frontend, tested and documented for reuse.",
    status: "locked",
    actions: [
      "Refactor B1 agent into FastAPI backend with proper async patterns",
      "Implement ChatKit server for rich UI interactions",
      "Write comprehensive test suite (TDD approach)",
      "Add persistent storage (SQLModel + PostgreSQL)",
      "Document the API for other developers",
    ],
    constraints: [
      "Must be reusable — not just for your use case",
      "Must have tests that prove it works",
      "Must handle errors gracefully",
      "Build on your B1 agent — don't start from scratch",
    ],
    deliverables: [
      "FastAPI agent backend with documented endpoints",
      "ChatKit server integration with interactive widgets",
      "Test suite with >80% coverage",
      "Database schema and migrations",
      "README with setup instructions",
    ],
    helpingLessons: "Chapters 40-41: FastAPI + ChatKit",
    lessonsLink: "/docs/AI-Native-Software-Development/fastapi-for-agents",
    successSignal: "Another developer can run your agent interface from the README.",
  },
  {
    id: "C1",
    title: "Local Deployment with Docker",
    goal: "Your agent runs in containers, ready for any environment.",
    status: "locked",
    actions: [
      "Write Dockerfile for your agent",
      "Create docker-compose for local development",
      "Test the containerized agent end-to-end",
      "Document the container setup",
    ],
    deliverables: [
      "Multi-stage Dockerfile optimized for production",
      "docker-compose.yml for local development",
      "Container runs successfully on fresh machine",
    ],
    helpingLessons: "Chapter 49: Docker for AI Services",
    lessonsLink: "/docs/AI-Cloud-Native-Development/docker-for-ai-services",
    successSignal: "docker-compose up starts your agent on any machine.",
  },
  {
    id: "C2",
    title: "Event-Driven Architecture",
    goal: "Your agents communicate through events, not direct calls.",
    status: "locked",
    actions: [
      "Set up Kafka/Strimzi for event streaming",
      "Implement event producers and consumers",
      "Design event schemas for agent communication",
      "Handle event failures gracefully",
    ],
    deliverables: [
      "Kafka cluster running (local or cloud)",
      "Agent publishes and consumes events",
      "Event schema documentation",
      "Dead letter queue for failed events",
    ],
    helpingLessons: "Chapter 52: Kafka and Strimzi",
    lessonsLink: "/docs/AI-Cloud-Native-Development/kafka-strimzi-event-streaming",
    successSignal: "Two agents communicate through Kafka without direct coupling.",
  },
  {
    id: "C3",
    title: "Dapr for Distributed Agents",
    goal: "Your agents use Dapr for state, pub/sub, and workflows.",
    status: "locked",
    actions: [
      "Install Dapr and understand the sidecar pattern",
      "Implement state management for agent memory",
      "Use Dapr pub/sub instead of direct Kafka",
      "Build a Dapr workflow for multi-step agent tasks",
    ],
    deliverables: [
      "Dapr sidecar running with your agent",
      "State store configured for agent persistence",
      "Pub/sub working through Dapr abstraction",
      "One Dapr workflow orchestrating agent steps",
    ],
    helpingLessons: "Chapters 55-57: Dapr Building Blocks",
    lessonsLink: "/docs/AI-Cloud-Native-Development/dapr-building-blocks",
    successSignal: "Your agent survives restarts because Dapr manages its state.",
  },
  {
    id: "C4",
    title: "Production Deployment",
    goal: "Your agent runs in production without your laptop.",
    status: "locked",
    actions: [
      "Deploy to Kubernetes (managed or self-hosted)",
      "Set up CI/CD with GitHub Actions + ArgoCD",
      "Implement monitoring and alerting",
      "Configure cost tracking and budget alerts",
    ],
    deliverables: [
      "Agent deployed to production Kubernetes",
      "GitOps pipeline auto-deploying on merge",
      "Monitoring dashboard showing uptime/usage",
      "Cost tracking with budget alerts",
      "Production runbook",
    ],
    helpingLessons: "Chapters 50, 54, 58-60: K8s + GitOps + Observability",
    lessonsLink: "/docs/AI-Cloud-Native-Development/kubernetes-for-ai-services",
    successSignal: "Your agent completed a task while you were asleep.",
  },
  {
    id: "D1",
    title: "Monetize Your First Digital FTE",
    goal: "Your deployed agent generates revenue — the thesis fulfilled. You now manufacture AI employees.",
    status: "locked",
    actions: [
      "Add billing/subscription to your agent (Stripe, LemonSqueezy, or usage-based)",
      "Create a landing page explaining what your Digital FTE does and for whom",
      "Launch publicly (ProductHunt, LinkedIn, domain community)",
      "Acquire your first paying customer",
      "Document the business model and unit economics",
    ],
    constraints: [
      "Must be a real product, not a demo",
      "Must solve a real problem for paying customers",
      "Pricing must be sustainable (covers infrastructure + your time)",
      "Must have terms of service and basic legal protection",
    ],
    deliverables: [
      "Payment integration with at least one provider",
      "Public landing page with clear value proposition",
      "First paying customer",
      "Documentation: pricing model, CAC, unit economics",
      "Testimonial or case study from first customer",
    ],
    helpingLessons: "The Agent Factory Thesis + All Prior Chapters",
    lessonsLink: "/docs/thesis",
    successSignal: "You earned your first dollar from an AI employee you manufactured.",
  },
];

// ============================================================================
// URL PARAM HELPER
// ============================================================================

function useCheckpointParam(): string | null {
  const [checkpointId, setCheckpointId] = useState<string | null>(null);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const params = new URLSearchParams(window.location.search);
      setCheckpointId(params.get('checkpoint'));
    }
  }, []);

  return checkpointId;
}

// ============================================================================
// COMPONENTS
// ============================================================================

function StatusIndicator({ status }: { status: "locked" | "active" | "completed" }) {
  if (status === "completed") {
    return (
      <div className="flex items-center gap-2">
        <div className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
        <span className="text-emerald-600 dark:text-emerald-500 font-mono text-xs uppercase tracking-wider">Complete</span>
      </div>
    );
  }
  if (status === "active") {
    return (
      <div className="flex items-center gap-2">
        <div className="w-2 h-2 rounded-full bg-amber-500 animate-pulse" />
        <span className="text-amber-600 dark:text-amber-500 font-mono text-xs uppercase tracking-wider">Active</span>
      </div>
    );
  }
  return (
    <div className="flex items-center gap-2">
      <div className="w-2 h-2 rounded-full bg-muted-foreground/30" />
      <span className="text-muted-foreground font-mono text-xs uppercase tracking-wider">Locked</span>
    </div>
  );
}

function CheckpointCard({ checkpoint, defaultExpanded = false }: { checkpoint: Checkpoint; defaultExpanded?: boolean }) {
  const [isExpanded, setIsExpanded] = useState(defaultExpanded);
  const isLocked = checkpoint.status === "locked";

  // Update expansion when defaultExpanded changes
  useEffect(() => {
    if (defaultExpanded) setIsExpanded(true);
  }, [defaultExpanded]);

  return (
    <div
      id={`checkpoint-${checkpoint.id}`}
      className={`
        border transition-all duration-300
        ${isLocked
          ? "border-border bg-muted/30 opacity-60"
          : "border-border bg-card hover:border-primary/50"
        }
      `}
    >
      {/* Header - Always Visible */}
      <button
        onClick={() => !isLocked && setIsExpanded(!isExpanded)}
        disabled={isLocked}
        className={`
          w-full p-6 text-left flex items-start justify-between gap-4
          ${isLocked ? "cursor-not-allowed" : "cursor-pointer"}
        `}
      >
        <div className="flex items-start gap-4 flex-1">
          {/* Checkpoint ID Badge */}
          <div className={`
            w-14 h-14 flex items-center justify-center font-mono font-black text-lg
            ${isLocked
              ? "bg-muted text-muted-foreground"
              : checkpoint.status === "completed"
                ? "bg-emerald-500/20 text-emerald-600 dark:text-emerald-400 border border-emerald-500/30"
                : "bg-amber-500/20 text-amber-600 dark:text-amber-400 border border-amber-500/30"
            }
          `}>
            {checkpoint.id}
          </div>

          <div className="flex-1 min-w-0">
            <div className="flex flex-wrap items-center gap-3 mb-2">
              <h3 className={`
                font-bold text-lg tracking-tight
                ${isLocked ? "text-muted-foreground" : "text-foreground"}
              `}>
                {checkpoint.title}
              </h3>
              <StatusIndicator status={checkpoint.status} />
            </div>
            <p className={`text-sm ${isLocked ? "text-muted-foreground/60" : "text-muted-foreground"}`}>
              {checkpoint.goal}
            </p>
          </div>
        </div>

        {!isLocked && (
          <div className="text-muted-foreground mt-1">
            {isExpanded ? <ChevronDown className="w-5 h-5" /> : <ChevronRight className="w-5 h-5" />}
          </div>
        )}
      </button>

      {/* Expanded Content */}
      {isExpanded && !isLocked && (
        <div className="border-t border-border p-6 space-y-6 bg-muted/20">
          {/* Actions */}
          <div>
            <div className="flex items-center gap-2 mb-3">
              <Play className="w-4 h-4 text-amber-500" />
              <h4 className="font-mono text-xs uppercase tracking-wider text-amber-600 dark:text-amber-500">Actions</h4>
            </div>
            <ul className="space-y-2">
              {checkpoint.actions.map((action, i) => (
                <li key={i} className="flex items-start gap-3 text-sm text-foreground/80">
                  <span className="text-amber-500/60 font-mono text-xs mt-0.5">{String(i + 1).padStart(2, '0')}</span>
                  {action}
                </li>
              ))}
            </ul>
          </div>

          {/* Constraints */}
          {checkpoint.constraints && (
            <div>
              <div className="flex items-center gap-2 mb-3">
                <Target className="w-4 h-4 text-red-500" />
                <h4 className="font-mono text-xs uppercase tracking-wider text-red-600 dark:text-red-400">Constraints</h4>
              </div>
              <ul className="space-y-1">
                {checkpoint.constraints.map((constraint, i) => (
                  <li key={i} className="flex items-start gap-2 text-sm text-muted-foreground">
                    <span className="text-red-500/60">!</span>
                    {constraint}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Deliverables */}
          <div>
            <div className="flex items-center gap-2 mb-3">
              <CheckCircle2 className="w-4 h-4 text-cyan-500" />
              <h4 className="font-mono text-xs uppercase tracking-wider text-cyan-600 dark:text-cyan-400">Deliverables</h4>
            </div>
            <ul className="space-y-2">
              {checkpoint.deliverables.map((deliverable, i) => (
                <li key={i} className="flex items-start gap-3 text-sm text-foreground/80">
                  <Circle className="w-3 h-3 text-cyan-500/40 mt-1 flex-shrink-0" />
                  {deliverable}
                </li>
              ))}
            </ul>
          </div>

          {/* Helping Lessons */}
          <div className="p-4 bg-background border border-border space-y-3">
            <div className="flex flex-wrap items-center justify-between gap-4">
              <div className="flex items-center gap-3">
                <BookOpen className="w-4 h-4 text-muted-foreground" />
                <span className="text-sm text-muted-foreground">
                  <span className="text-muted-foreground/60">Reference:</span> {checkpoint.helpingLessons}
                </span>
              </div>
              {checkpoint.lessonsLink && (
                <Link
                  to={checkpoint.lessonsLink}
                  className="flex items-center gap-1 text-xs text-primary hover:text-primary/80 transition-colors"
                >
                  Open Lessons <ExternalLink className="w-3 h-3" />
                </Link>
              )}
            </div>
            {checkpoint.additionalContext && (
              <div className="flex items-center gap-3 pt-2 border-t border-border">
                <span className="text-sm text-muted-foreground">
                  <span className="text-muted-foreground/60">Additional:</span>{" "}
                  <a
                    href={checkpoint.additionalContext}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-primary hover:text-primary/80 transition-colors"
                  >
                    {checkpoint.additionalContext.includes("youtube") ? "Watch Video" : "View Resource"}
                  </a>
                </span>
              </div>
            )}
          </div>

          {/* Success Signal */}
          <div className="p-4 border-l-2 border-emerald-500 bg-emerald-500/5">
            <div className="flex items-center gap-2 mb-2">
              <Zap className="w-4 h-4 text-emerald-500" />
              <h4 className="font-mono text-xs uppercase tracking-wider text-emerald-600 dark:text-emerald-400">Success Signal</h4>
            </div>
            <p className="text-sm text-emerald-700 dark:text-emerald-300/80">{checkpoint.successSignal}</p>
          </div>
        </div>
      )}
    </div>
  );
}


// ============================================================================
// MAIN PAGE
// ============================================================================

export default function FactoryPage(): ReactNode {
  const openCheckpoint = useCheckpointParam();

  // Scroll to checkpoint if specified in URL
  useEffect(() => {
    if (openCheckpoint && typeof window !== 'undefined') {
      setTimeout(() => {
        const element = document.getElementById(`checkpoint-${openCheckpoint}`);
        if (element) {
          element.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }, 300);
    }
  }, [openCheckpoint]);

  return (
    <Layout
      title="Factory Dashboard"
      description="Your Agent Factory Dashboard - Track your progress building Digital FTEs"
    >
      <div className="min-h-screen bg-background">

        {/* Hero Section - Public & Welcoming */}
        <header className="relative border-b border-border bg-gradient-to-b from-primary/5 to-background">
          <div className="max-w-6xl mx-auto px-6 py-16 md:py-20">
            {/* Badge */}
            <div className="flex items-center gap-3 mb-6">
              <span className="font-mono text-xs font-bold tracking-widest uppercase text-primary px-3 py-1.5 border border-primary/30 bg-primary/10">
                Your Journey
              </span>
            </div>

            {/* Main Headline */}
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-black tracking-tight text-foreground mb-6 leading-[1.1]">
              Build Your
              <span className="text-primary block">Agent Factory</span>
            </h1>

            {/* Thesis Statement */}
            <p className="text-lg md:text-xl text-muted-foreground leading-relaxed max-w-3xl mb-10">
              In the AI era, the most valuable companies won't sell software—they'll{" "}
              <span className="text-foreground font-semibold">manufacture AI employees</span>, powered by
              agents, specs, skills, MCP, autonomy and cloud-native technologies.
            </p>

          </div>
        </header>


        {/* Main Content */}
        <main className="max-w-6xl mx-auto px-6 py-12">

          {/* Section: The Checklist */}
          <section className="mb-16">
            <div className="flex items-center gap-3 mb-6">
              <div className="w-1 h-6 bg-primary" />
              <h2 className="font-mono text-sm uppercase tracking-wider text-muted-foreground">
                The Non-Negotiables
              </h2>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {[
                { label: "Build in public", desc: "Share what you build (LinkedIn, X, YouTube)" },
                { label: "Automate yourself first", desc: "Prove it works on YOU before selling" },
                { label: "Measure everything", desc: "Every skill has success metrics" },
                { label: "Ship weekly", desc: "No learning without shipping" },
              ].map((item, i) => (
                <div key={i} className="flex items-start gap-4 p-4 bg-card border border-border hover:border-primary/30 transition-colors">
                  <div className="w-8 h-8 border border-border flex items-center justify-center text-muted-foreground font-mono text-sm font-bold bg-muted">
                    {i + 1}
                  </div>
                  <div>
                    <h3 className="text-foreground font-semibold mb-1">{item.label}</h3>
                    <p className="text-muted-foreground text-sm">{item.desc}</p>
                  </div>
                </div>
              ))}
            </div>
          </section>

          {/* Section: Portfolio Checkpoints */}
          <section className="mb-16">
            <div className="flex flex-wrap items-center justify-between gap-4 mb-6">
              <div className="flex items-center gap-3">
                <div className="w-1 h-6 bg-cyan-500" />
                <h2 className="font-mono text-sm uppercase tracking-wider text-muted-foreground">
                  Portfolio Checkpoints
                </h2>
              </div>
              <div className="flex items-center gap-4 text-xs font-mono">
                <div className="flex items-center gap-2">
                  <div className="w-2 h-2 bg-amber-500" />
                  <span className="text-muted-foreground">Active</span>
                </div>
                <div className="flex items-center gap-2">
                  <div className="w-2 h-2 bg-emerald-500" />
                  <span className="text-muted-foreground">Complete</span>
                </div>
                <div className="flex items-center gap-2">
                  <div className="w-2 h-2 bg-muted-foreground/30" />
                  <span className="text-muted-foreground">Locked</span>
                </div>
              </div>
            </div>

            <div className="space-y-4">
              {checkpoints.map((checkpoint) => (
                <CheckpointCard
                  key={checkpoint.id}
                  checkpoint={checkpoint}
                  defaultExpanded={openCheckpoint === checkpoint.id}
                />
              ))}
            </div>
          </section>

          {/* Section: Hackathons */}
          <section className="mb-16">
            <div className="flex items-center gap-3 mb-6">
              <div className="w-1 h-6 bg-emerald-500" />
              <h2 className="font-mono text-sm uppercase tracking-wider text-muted-foreground">
                Hackathons & Competitions
              </h2>
            </div>

            <div className="p-8 border border-dashed border-border bg-muted/20 text-center">
              <p className="text-muted-foreground font-mono text-sm mb-4">
                Accelerate your portfolio with external challenges
              </p>
              <p className="text-muted-foreground/60 text-sm">
                Coming soon: Curated hackathons and competitions to test your skills
              </p>
            </div>
          </section>

          {/* CTA: Open the Book */}
          <section className="text-center py-12 border-t border-border">
            <p className="font-mono text-xs text-muted-foreground uppercase tracking-wider mb-4">
              Need reference material?
            </p>
            <Link
              to="/docs/thesis"
              className="inline-flex items-center gap-3 px-8 py-4 bg-card border border-border hover:border-primary/50 hover:bg-muted/50 transition-all text-foreground font-medium"
            >
              <BookOpen className="w-5 h-5 text-primary" />
              Open the Reference Manual
              <ExternalLink className="w-4 h-4 text-muted-foreground" />
            </Link>
          </section>

        </main>
      </div>
    </Layout>
  );
}
