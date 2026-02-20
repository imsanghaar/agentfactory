export interface Author {
  name: string;
  role: string;
  avatar: string;
  link: string;
  bio: string;
  isAI: boolean;
  initials: string;
}

export const authors: Author[] = [
  {
    name: "Imam Sanghaar Chandio",
    role: "Lead Author",
    avatar: "/img/authors/imam-sanghaar.jpeg",
    link: "https://www.linkedin.com/in/imam-sanghaar-chandio-96780b274/",
    bio: "Student at PIAIC - Learning Agentic AI, Prompt Engineer, Web Developer. Leading the imsanghaar initiative to democratize AI-native education through practical, hands-on learning. Passionate about building intelligent systems that empower individuals and organizations to thrive in the AI-first future.",
    isAI: false,
    initials: "ISC",
  },
  {
    name: "Qwen",
    role: "AI Co-Author",
    avatar: "/img/authors/qwen.webp",
    link: "https://github.com/imsanghaar/agentfactory",
    bio: "Alibaba's advanced AI assistant that helped refine and enhance this book's content. Contributed through intelligent analysis, technical explanations, and ensuring clarity across complex AI-native development concepts. Represents the next generation of open, collaborative AI partnerships.",
    isAI: true,
    initials: "Qw",
  },
  {
    name: "SpecKitPlus",
    role: "AI Co-Author",
    avatar: "/img/authors/speckitplus.webp",
    link: "https://github.com/panaversity/spec-kit-plus",
    bio: "An SDD-RI (Specification-Driven Development with Reusable Intelligence) framework built around one core idea: capture intelligence, not just deliver code. Powers the book's spec templates, curriculum architecture, and quality validation pipelines.",
    isAI: true,
    initials: "SK",
  },
];
