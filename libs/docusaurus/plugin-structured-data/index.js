/**
 * Docusaurus Plugin: Structured Data (JSON-LD) Injection
 *
 * Injects structured data schemas into pages during build:
 * - Homepage: Organization + Course schemas (for brand and educational content recognition)
 * - Docs pages: Article schema (for content type recognition)
 *
 * This ensures search engines and AI systems see structured data in initial HTML.
 */

const fs = require("fs").promises;
const path = require("path");
const { load: loadHtml } = require("cheerio");

// Organization schema for Panaversity brand recognition
const ORGANIZATION_SCHEMA = {
  "@context": "https://schema.org",
  "@type": "Organization",
  name: "Panaversity",
  url: "https://panaversity.org",
  logo: "https://agentfactory.panaversity.org/img/logo.png",
  sameAs: [
    "https://github.com/panaversity",
    "https://www.linkedin.com/company/panaversity",
  ],
};

// Course schema for Agent Factory book (educational content recognition)
const COURSE_SCHEMA = {
  "@context": "https://schema.org",
  "@type": "Course",
  name: "The AI Agent Factory",
  description:
    "The Spec-Driven Blueprint for Building and Monetizing Digital FTEs. Learn to build AI agents using Claude Code, MCP, and agent SDKs.",
  provider: {
    "@type": "Organization",
    name: "Panaversity",
    url: "https://panaversity.org",
  },
  courseCode: "AIAF-2026",
  educationalLevel: "Intermediate to Advanced",
  teaches: [
    "AI Agent Development",
    "Claude Code",
    "Model Context Protocol (MCP)",
    "Spec-Driven Development",
    "Digital FTE Creation",
    "Agent Skills",
  ],
  inLanguage: "en",
  isAccessibleForFree: true,
  hasCourseInstance: {
    "@type": "CourseInstance",
    courseMode: "online",
    courseWorkload: "PT200H",
  },
};

module.exports = function structuredDataPlugin(context, options) {
  const { siteConfig } = context;

  return {
    name: "docusaurus-plugin-structured-data",

    async postBuild({ outDir }) {
      const docsDir = path.join(outDir, "docs");
      const rootIndex = path.join(outDir, "index.html");

      let homepageSuccess = false;
      let docsSuccess = false;

      // 1. Inject Organization + Course schemas on homepage
      try {
        if (await fileExists(rootIndex)) {
          await injectHomepageSchemas(rootIndex, siteConfig);
          homepageSuccess = true;
        }
      } catch (error) {
        console.warn("⚠ Failed to inject homepage schemas:", error.message);
      }

      // 2. Inject Article schema on docs pages
      try {
        await processDocsDirectory(docsDir, siteConfig);
        docsSuccess = true;
      } catch (error) {
        console.warn("⚠ Failed to inject docs schemas:", error.message);
      }

      // Report results
      if (homepageSuccess && docsSuccess) {
        console.log(
          "✓ Structured data injected (Organization, Course, Article)",
        );
      } else if (homepageSuccess) {
        console.log("✓ Homepage schemas injected; docs processing had issues");
      } else if (docsSuccess) {
        console.log("✓ Docs Article schemas injected; homepage had issues");
      }
    },
  };
};

async function fileExists(filePath) {
  try {
    await fs.access(filePath);
    return true;
  } catch {
    return false;
  }
}

async function injectHomepageSchemas(filePath, siteConfig) {
  const html = await fs.readFile(filePath, "utf-8");
  const $ = loadHtml(html);

  // Add Organization schema
  const orgScript = `<script type="application/ld+json" id="jsonld-organization">${JSON.stringify(ORGANIZATION_SCHEMA)}</script>`;
  $("head").append(orgScript);

  // Add Course schema
  const courseData = {
    ...COURSE_SCHEMA,
    url: siteConfig.url || "https://agentfactory.panaversity.org",
  };
  const courseScript = `<script type="application/ld+json" id="jsonld-course">${JSON.stringify(courseData)}</script>`;
  $("head").append(courseScript);

  await fs.writeFile(filePath, $.html(), "utf-8");
}

async function processDocsDirectory(dirPath, siteConfig) {
  let entries;
  try {
    entries = await fs.readdir(dirPath, { withFileTypes: true });
  } catch (error) {
    if (error.code === "ENOENT") return; // Directory doesn't exist, skip
    throw error;
  }

  for (const entry of entries) {
    const fullPath = path.join(dirPath, entry.name);

    if (entry.isDirectory()) {
      await processDocsDirectory(fullPath, siteConfig);
    } else if (entry.isFile() && entry.name.endsWith(".html")) {
      await injectArticleSchema(fullPath, siteConfig);
    }
  }
}

async function injectArticleSchema(filePath, siteConfig) {
  try {
    const html = await fs.readFile(filePath, "utf-8");
    const $ = loadHtml(html);

    // Extract page metadata
    const title = $("title").text() || siteConfig.title || "";
    const description =
      $('meta[name="description"]').attr("content") || siteConfig.tagline || "";
    const canonical = $('link[rel="canonical"]').attr("href") || "";

    // Build Article JSON-LD
    const articleData = {
      "@context": "https://schema.org",
      "@type": "Article",
      headline: title,
      description: description,
      mainEntityOfPage: canonical,
    };

    const scriptTag = `<script type="application/ld+json" id="jsonld-article">${JSON.stringify(articleData)}</script>`;
    $("head").append(scriptTag);

    await fs.writeFile(filePath, $.html(), "utf-8");
  } catch (error) {
    // Log but don't throw - one file failing shouldn't stop others
    console.warn(`Warning: ${path.basename(filePath)}: ${error.message}`);
  }
}
