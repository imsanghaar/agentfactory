import type { ReactNode } from "react";
import Link from "@docusaurus/Link";
import Layout from "@theme/Layout";
import { Avatar, AvatarImage, AvatarFallback } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
import { authors } from "@/data/authors";
import { ExternalLink } from "lucide-react";

export default function AuthorsPage(): ReactNode {
  const humanAuthors = authors.filter((a) => !a.isAI);
  const aiAuthors = authors.filter((a) => a.isAI);

  return (
    <Layout
      title="Co-Authors"
      description="Meet the human and AI co-authors of The AI Agent Factory book."
    >
      <main className="max-w-4xl mx-auto px-6 py-16">
        <div className="mb-12">
          <h1 className="text-4xl font-black tracking-tight text-foreground uppercase mb-4">
            Co-Authors
          </h1>
          <p className="text-lg text-muted-foreground max-w-2xl">
            The AI Agent Factory is a collaborative work between human experts
            and AI contributors, embodying the co-creation philosophy taught
            throughout the book.
          </p>
        </div>

        {/* Human Authors */}
        <section className="mb-16">
          <h2 className="text-sm font-bold text-muted-foreground uppercase tracking-widest mb-8">
            Author
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {humanAuthors.slice(0, 1).map((author) => (
              <div
                key={author.name}
                className="flex gap-4 p-6 border border-border bg-card"
              >
                <Avatar className="h-16 w-16 shrink-0">
                  <AvatarImage src={author.avatar} alt={author.name} />
                  <AvatarFallback className="text-sm font-bold">
                    {author.initials}
                  </AvatarFallback>
                </Avatar>
                <div className="flex flex-col">
                  <h3 className="text-base font-bold text-foreground">
                    {author.name}
                  </h3>
                  <p className="text-xs font-medium text-primary uppercase tracking-wide mb-2">
                    {author.role}
                  </p>
                  <p className="text-sm text-muted-foreground mb-3 flex-grow">
                    {author.bio}
                  </p>
                  <Button
                    variant="link"
                    className="h-auto p-0 justify-start text-xs text-muted-foreground hover:text-foreground"
                    asChild
                  >
                    <Link
                      to={author.link}
                      className="flex items-center gap-1"
                    >
                      LinkedIn <ExternalLink className="w-3 h-3" />
                    </Link>
                  </Button>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* AI Contributors */}
        <section>
          <h2 className="text-sm font-bold text-muted-foreground uppercase tracking-widest mb-8">
            AI Contributors
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {aiAuthors.map((author) => (
              <div
                key={author.name}
                className="flex gap-4 p-6 border border-border bg-card"
              >
                <Avatar className="h-16 w-16 shrink-0">
                  <AvatarImage src={author.avatar} alt={author.name} />
                  <AvatarFallback className="text-sm font-bold">
                    {author.initials}
                  </AvatarFallback>
                </Avatar>
                <div className="flex flex-col">
                  <h3 className="text-base font-bold text-foreground">
                    {author.name}
                  </h3>
                  <p className="text-xs font-medium text-primary uppercase tracking-wide mb-2">
                    {author.role}
                  </p>
                  <p className="text-sm text-muted-foreground mb-3 flex-grow">
                    {author.bio}
                  </p>
                  <Button
                    variant="link"
                    className="h-auto p-0 justify-start text-xs text-muted-foreground hover:text-foreground"
                    asChild
                  >
                    <Link
                      to={author.link}
                      className="flex items-center gap-1"
                    >
                      View <ExternalLink className="w-3 h-3" />
                    </Link>
                  </Button>
                </div>
              </div>
            ))}
          </div>
        </section>
      </main>
    </Layout>
  );
}
