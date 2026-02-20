import { useState } from "react";
import Layout from "@theme/Layout";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { ExternalLink, Quote, Star, ArrowRight } from "lucide-react";
import Link from "@docusaurus/Link";

const BOOK_URL = "https://agentfactory.panaversity.org";
const LLMS_TXT_URL = `${BOOK_URL}/llms.txt`;

const REVIEW_PROMPT = `Professionally review "The AI Agent Factory" (${BOOK_URL}) — 86 chapters teaching how to build and monetize AI agents using Claude Code, MCP, and agent SDKs.

For structured context, read: ${LLMS_TXT_URL}

Evaluate: educational quality, technical depth, uniqueness (does comparable content exist elsewhere?), and practical value. Be honest and detailed.`;

const AI_MODELS = [
  {
    name: "ChatGPT",
    provider: "OpenAI",
    url: "https://chatgpt.com/",
    color: "#10a37f",
    bgColor: "bg-[#10a37f]/5 hover:bg-[#10a37f]/10",
    borderColor: "border-[#10a37f]/20 hover:border-[#10a37f]/40",
    prefillParam: "q",
  },
  {
    name: "Claude",
    provider: "Anthropic",
    url: "https://claude.ai/new",
    color: "#d97757",
    bgColor: "bg-[#d97757]/5 hover:bg-[#d97757]/10",
    borderColor: "border-[#d97757]/20 hover:border-[#d97757]/40",
    prefillParam: "q",
  },
  {
    name: "Gemini",
    provider: "Google",
    url: "https://gemini.google.com/app",
    color: "#4285f4",
    bgColor: "bg-[#4285f4]/5 hover:bg-[#4285f4]/10",
    borderColor: "border-[#4285f4]/20 hover:border-[#4285f4]/40",
    prefillParam: null,
  },
  {
    name: "Grok",
    provider: "xAI",
    url: "https://grok.com/",
    color: "#a0a0a0",
    bgColor: "bg-[#a0a0a0]/5 hover:bg-[#a0a0a0]/10",
    borderColor: "border-[#a0a0a0]/20 hover:border-[#a0a0a0]/40",
    prefillParam: "q",
  },
] as const;

const HUMAN_REVIEWS = [
  {
    name: "Khurram",
    role: "Banking Sector Professional",
    context: "Banking Industry Seminar, February 2026",
    quote:
      "Before presenting at our banking seminar, I had multiple AI models independently review this book. Every model reached the same conclusion: a resource this comprehensive — covering the full journey from understanding AI agents to building and monetizing them — simply does not exist elsewhere on the internet. The individual topics are scattered across dozens of sources, but no one has assembled them into a single, structured learning path like this.",
    rating: 5,
  },
];

function LiveReviewSection() {
  const [copied, setCopied] = useState(false);

  const handleModelClick = async (model: (typeof AI_MODELS)[number]) => {
    // Copy prompt first
    try {
      await navigator.clipboard.writeText(REVIEW_PROMPT);
      setCopied(true);
      setTimeout(() => setCopied(false), 3000);
    } catch {
      // Continue to open even if copy fails
    }

    // Open model — use prefill param if supported
    const url = model.prefillParam
      ? `${model.url}?${model.prefillParam}=${encodeURIComponent(REVIEW_PROMPT)}`
      : model.url;

    window.open(url, "_blank", "noopener,noreferrer");
  };

  return (
    <section className="py-12 sm:py-16">
      <div className="max-w-5xl mx-auto px-6">
        {/* Section Header */}
        <div className="text-center mb-10">
          <h1 className="text-3xl sm:text-4xl md:text-5xl font-black tracking-tight mb-4">
            Live AI Reviews
          </h1>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Pick any frontier AI model. It will read our book and deliver an
            independent, unfiltered review — no cherry-picked quotes.
          </p>
        </div>

        {/* Model Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {AI_MODELS.map((model) => (
            <button
              key={model.name}
              onClick={() => handleModelClick(model)}
              className={`group flex flex-col items-center gap-3 p-6 border ${model.borderColor} ${model.bgColor} transition-all duration-200 cursor-pointer text-left`}
            >
              {/* Color indicator */}
              <div
                className="w-10 h-10 rounded-full flex items-center justify-center allow-rounded"
                style={{ backgroundColor: `${model.color}15` }}
              >
                <div
                  className="w-4 h-4 rounded-full allow-rounded"
                  style={{ backgroundColor: model.color }}
                />
              </div>

              {/* Model info */}
              <div className="text-center">
                <div className="font-bold text-foreground text-lg">
                  {model.name}
                </div>
                <div className="text-xs text-muted-foreground">
                  {model.provider}
                </div>
              </div>

              {/* Action */}
              <div className="flex items-center gap-1.5 text-xs font-medium text-muted-foreground group-hover:text-foreground transition-colors mt-1">
                {model.prefillParam ? "Open with prompt" : "Copy & Open"}
                <ExternalLink className="w-3 h-3" />
              </div>
            </button>
          ))}
        </div>

        {/* Instructions */}
        <p className="text-center text-sm text-muted-foreground mt-6">
          Each model opens with our review prompt pre-loaded. For Gemini, the
          prompt is copied to your clipboard —{" "}
          <span className="text-foreground font-medium">
            just paste and hit Enter.
          </span>
        </p>
      </div>
    </section>
  );
}

function HumanReviewsSection() {
  return (
    <section className="py-12 sm:py-16 border-t border-border/40">
      <div className="max-w-5xl mx-auto px-6">
        <div className="text-center mb-10">
          <h2 className="text-3xl sm:text-4xl font-black tracking-tight mb-4">
            Reader Reviews
          </h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Feedback from professionals using this book in their work.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {HUMAN_REVIEWS.map((review, i) => (
            <Card key={i} className="rounded-none border-border bg-background">
              <CardContent className="p-6 sm:p-8">
                {/* Quote icon */}
                <Quote className="w-8 h-8 text-primary/20 mb-4" />

                {/* Rating */}
                <div className="flex gap-0.5 mb-4">
                  {Array.from({ length: review.rating }).map((_, j) => (
                    <Star
                      key={j}
                      className="w-4 h-4 fill-primary text-primary"
                    />
                  ))}
                </div>

                {/* Quote text */}
                <blockquote className="text-foreground/90 leading-relaxed mb-6">
                  "{review.quote}"
                </blockquote>

                {/* Attribution */}
                <div className="border-t border-border/40 pt-4">
                  <div className="font-bold text-foreground">{review.name}</div>
                  <div className="text-sm text-muted-foreground">
                    {review.role}
                  </div>
                  <div className="text-xs text-muted-foreground/60 mt-1">
                    {review.context}
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}

          {/* Placeholder for more reviews */}
          <Card className="rounded-none border-border border-dashed bg-muted/10">
            <CardContent className="p-6 sm:p-8 flex flex-col items-center justify-center text-center h-full min-h-[250px]">
              <Quote className="w-8 h-8 text-muted-foreground/20 mb-3" />
              <p className="text-sm text-muted-foreground font-medium">
                Your review could be here
              </p>
              <p className="text-xs text-muted-foreground/60 mt-2 max-w-[200px]">
                Run any AI review above and share your results with us
              </p>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
}

function CTASection() {
  return (
    <section className="py-12 sm:py-16 border-t border-border/40 bg-muted/20">
      <div className="max-w-3xl mx-auto px-6 text-center">
        <h2 className="text-2xl sm:text-3xl font-black tracking-tight mb-4">
          Convinced? Start Building.
        </h2>
        <p className="text-lg text-muted-foreground mb-8">
          Learn to build and monetize AI agents — from concept to production.
        </p>
        <Button
          asChild
          size="lg"
          className="h-14 px-8 text-lg font-bold rounded-none bg-primary hover:bg-primary/90 text-primary-foreground"
        >
          <Link to="/docs/thesis" className="flex items-center gap-3">
            START READING <ArrowRight className="w-5 h-5" />
          </Link>
        </Button>
      </div>
    </section>
  );
}

export default function ReviewsPage() {
  return (
    <Layout
      title="Live AI Reviews"
      description="Get an independent AI review of The AI Agent Factory book from ChatGPT, Claude, Gemini, or Grok."
    >
      <LiveReviewSection />
      <HumanReviewsSection />
      <CTASection />
    </Layout>
  );
}
