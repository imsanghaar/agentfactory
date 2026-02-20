const fs = require("fs");
const path = require("path");
const sharp = require("sharp");

// Satori is ESM-only, we'll use dynamic import
let satori;
const initSatori = async () => {
  if (!satori) {
    satori = (await import("satori")).default;
  }
  return satori;
};

// Cache fonts globally to avoid repeated file reads (major memory savings)
let cachedFonts = null;
const loadFontsOnce = () => {
  if (cachedFonts) return cachedFonts;

  // Bundled fonts (Inter) - these are included in the plugin and work on all platforms
  const bundledFontsDir = path.join(__dirname, "fonts");
  const bundledFonts = [
    { name: "Inter", weight: 400, file: "Inter-Regular.ttf" },
    { name: "Inter", weight: 700, file: "Inter-Bold.ttf" },
  ];

  // System font fallbacks (only used if bundled fonts are missing)
  const systemFonts = [
    {
      name: "Sans",
      weight: 400,
      paths: [
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arial.ttf",
      ],
    },
    {
      name: "Sans",
      weight: 700,
      paths: [
        "/Library/Fonts/Arial Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
      ],
    },
  ];

  // Try bundled fonts first (preferred - works on Vercel/CI)
  cachedFonts = bundledFonts
    .map((font) => {
      const fontPath = path.join(bundledFontsDir, font.file);
      try {
        if (fs.existsSync(fontPath)) {
          return {
            name: font.name,
            data: fs.readFileSync(fontPath),
            weight: font.weight,
            style: "normal",
          };
        }
      } catch {
        // Ignore errors, fall through to system fonts
      }
      return null;
    })
    .filter(Boolean);

  // If bundled fonts loaded, use them
  if (cachedFonts.length >= 2) {
    console.log("  Using bundled Inter fonts");
    return cachedFonts;
  }

  // Fallback to system fonts
  console.log("  Bundled fonts not found, trying system fonts...");
  cachedFonts = systemFonts
    .map((c) => {
      const found = c.paths.find((p) => {
        try {
          return fs.existsSync(p);
        } catch {
          return false;
        }
      });
      if (!found) return null;
      return {
        name: c.name,
        data: fs.readFileSync(found),
        weight: c.weight,
        style: "normal",
      };
    })
    .filter(Boolean);

  if (!cachedFonts.length) {
    throw new Error(
      "No fonts found. Bundled Inter fonts missing and no system fonts available."
    );
  }

  return cachedFonts;
};

/**
 * Docusaurus plugin to automatically generate Open Graph images for each page
 */
module.exports = function (context, options) {

  return {
    name: "docusaurus-plugin-og-image-generator",

    async postBuild({ siteConfig, routesPaths, outDir, head }) {
      console.log("\n🎨 Generating Open Graph images...\n");

      // Load fonts ONCE at the start (prevents repeated file reads)
      try {
        loadFontsOnce();
        console.log("  ✓ Fonts loaded and cached\n");
      } catch (err) {
        console.log(`  ⚠ Font loading failed: ${err.message}`);
        console.log("  ⚠ OG image generation will be skipped\n");
        return;
      }

      // Ensure OG images are generated into the FINAL BUILD output, not static/
      const ogOutDir = path.join(outDir, "img", "og");
      if (!fs.existsSync(ogOutDir)) {
        fs.mkdirSync(ogOutDir, { recursive: true });
      }

      // Generate homepage OG image
      await generateOGImage({
        title: siteConfig.title,
        description: siteConfig.tagline,
        slug: 'home',
        ogDir: ogOutDir,
        siteConfig,
      });

      // Read all docs from the docs directory
      const docsDir = path.join(context.siteDir, "docs");
      await generateImagesFromDirectory(docsDir, ogOutDir, siteConfig, docsDir);

      // Inject OG image meta tags into built HTML files
      await injectOGImagesIntoHTML(outDir, siteConfig, context.siteDir);

      console.log("\n✅ Open Graph images generated and injected successfully!\n");
    },
  };
};

/**
 * Recursively scan docs directory and collect all markdown files
 */
function collectMarkdownFiles(dir, docsRoot, files = []) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      collectMarkdownFiles(fullPath, docsRoot, files);
    } else if (
      entry.isFile() &&
      (entry.name.endsWith(".md") || entry.name.endsWith(".mdx")) &&
      !entry.name.endsWith(".summary.md") // Skip summary files
    ) {
      files.push(fullPath);
    }
  }

  return files;
}

/**
 * Process markdown files in batches to prevent memory exhaustion
 */
async function generateImagesFromDirectory(dir, ogDir, siteConfig, docsRoot) {
  const files = collectMarkdownFiles(dir, docsRoot);
  const BATCH_SIZE = 20; // Process 20 files at a time
  let processed = 0;

  console.log(`  Found ${files.length} markdown files to process\n`);

  for (let i = 0; i < files.length; i += BATCH_SIZE) {
    const batch = files.slice(i, i + BATCH_SIZE);

    for (const fullPath of batch) {
      const content = fs.readFileSync(fullPath, "utf-8");
      const metadata = extractFrontMatter(content);

      if (metadata.title) {
        const relativePath = path.relative(docsRoot, fullPath);
        const slug = relativePath.replace(/\\/g, "/").replace(/\.mdx?$/, "");

        await generateOGImage({
          title: metadata.title,
          description: metadata.description || "",
          slug,
          ogDir,
          siteConfig,
        });
      }
      processed++;
    }

    // Hint garbage collection between batches (if available)
    if (global.gc) {
      global.gc();
    }

    // Progress update every batch
    if (processed % BATCH_SIZE === 0 || processed === files.length) {
      console.log(`  Progress: ${processed}/${files.length} docs processed`);
    }
  }
}

/**
 * Extract front matter from markdown content
 */
function extractFrontMatter(content) {
  const frontMatterRegex = /^---\s*\n([\s\S]*?)\n---/;
  const match = content.match(frontMatterRegex);

  if (!match) {
    return {};
  }

  const frontMatter = {};
  const lines = match[1].split("\n");

  for (const line of lines) {
    const [key, ...valueParts] = line.split(":");
    if (key && valueParts.length > 0) {
      const value = valueParts
        .join(":")
        .trim()
        .replace(/^["']|["']$/g, "");
      frontMatter[key.trim()] = value;
    }
  }

  return frontMatter;
}

/**
 * Inject OG image meta tags into built HTML files
 */
async function injectOGImagesIntoHTML(outDir, siteConfig, siteDir) {
  console.log("\n🔧 Injecting OG images into HTML files...\n");

  const htmlFiles = [];

  // Recursively find all HTML files
  function findHTMLFiles(dir) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        findHTMLFiles(fullPath);
      } else if (entry.isFile() && entry.name.endsWith('.html')) {
        htmlFiles.push(fullPath);
      }
    }
  }

  findHTMLFiles(outDir);

  console.log(`  Found ${htmlFiles.length} HTML files to process\n`);

  // Look for generated images inside the built output directory
  const ogImagesDir = path.join(outDir, 'img', 'og');

  // Stable version token per build, overridable from env/CI
  const buildVersion = process.env.BUILD_VERSION || String(Math.floor(Date.now() / 1000));

  let processed = 0;
  const BATCH_SIZE = 50;

  for (const htmlFile of htmlFiles) {
    processed++;
    try {
      let html = fs.readFileSync(htmlFile, 'utf-8');
      
      // Extract the path from the HTML file location
      const relativePath = path.relative(outDir, htmlFile);
      
      // Convert HTML path to slug (similar to how we generate images)
      let slug = relativePath
        .replace(/\\/g, '/')
        .replace(/\.html$/, '')
        .replace(/\/index$/, ''); // Remove trailing /index
      
      // Handle special cases
      if (slug === 'index' || slug === '') {
        slug = 'home';
      }
      
      // For docs pages, remove the "docs/" prefix to match generated image names
      if (slug.startsWith('docs/')) {
        slug = slug.replace(/^docs\//, '');
      }
      
      // Convert to OG image filename
      const imageFilename = slug.replace(/\//g, '-') + '.png';
      const ogImagePath = path.join(ogImagesDir, imageFilename);

      // Homepage: use a static book cover image for previews
      if (slug === 'home') {
        const srcPng = path.join(siteDir, 'static', 'img', 'book-cover-page.png');
        const destJpg = path.join(outDir, 'img', 'book-cover-social.jpg');
        let homepageImageUrl;

        // Try to create optimized JPEG from source PNG
        try {
          if (fs.existsSync(srcPng)) {
            await sharp(srcPng)
              .resize(1200, 630, { fit: 'cover' })
              .jpeg({ quality: 80, progressive: true, chromaSubsampling: '4:2:0' })
              .toFile(destJpg);
            homepageImageUrl = `${siteConfig.url}/img/book-cover-social.jpg?v=${buildVersion}`;
            console.log(`  ✓ Generated homepage social image: book-cover-social.jpg`);
          } else {
            console.log(`  ⚠ Homepage source image not found: ${srcPng}`);
          }
        } catch (err) {
          console.log(`  ⚠ Failed to generate homepage social image: ${err.message}`);
        }

        // Fallback to the original PNG if JPEG conversion failed
        if (!homepageImageUrl) {
          if (fs.existsSync(srcPng)) {
            homepageImageUrl = `${siteConfig.url}/img/book-cover-page.png?v=${buildVersion}`;
            console.log(`  ⚠ Using fallback: book-cover-page.png`);
          } else {
            // Generate OG image as last resort
            try {
              await generateOGImage({
                title: siteConfig.title,
                description: siteConfig.tagline,
                slug: 'home',
                ogDir: path.join(outDir, 'img', 'og'),
                siteConfig,
              });
              homepageImageUrl = `${siteConfig.url}/img/og/home.png?v=${buildVersion}`;
              console.log(`  ✓ Generated fallback OG image: home.png`);
            } catch (genErr) {
              console.log(`  ✗ Failed to generate homepage OG image: ${genErr.message}`);
            }
          }
        }

        if (homepageImageUrl) {
          // Don't add trailing slash - respect trailingSlash: false config
          const pageUrl = siteConfig.url;

          // Remove existing image/url tags
          html = html.replace(/<meta[^>]*property=\"og:image\"[^>]*>/gi, '');
          html = html.replace(/<meta[^>]*name=\"twitter:image\"[^>]*>/gi, '');
          html = html.replace(/<meta[^>]*property=\"og:url\"[^>]*>/gi, '');

          const ogTags = `
  <meta property=\"og:image\" content=\"${homepageImageUrl}\">\n  <meta property=\"og:image:width\" content=\"1200\">\n  <meta property=\"og:image:height\" content=\"630\">\n  <meta property=\"og:image:secure_url\" content=\"${homepageImageUrl}\">\n  <meta property=\"og:site_name\" content=\"${siteConfig.title}\">\n  <meta property=\"og:url\" content=\"${pageUrl}\">\n  <meta name=\"twitter:image\" content=\"${homepageImageUrl}\">\n</head>`;

          html = html.replace(/<\/head>/i, ogTags);
          fs.writeFileSync(htmlFile, html, 'utf-8');
        }
        continue;
      }
      
      

      // Ensure OG image exists for this page (generate on demand if missing)
      if (!fs.existsSync(ogImagePath)) {
        // Try to derive title/description from existing meta tags
        const titleMatch = html.match(/<meta[^>]*property="og:title"[^>]*content="([^"]+)"[^>]*>/i) ||
                           html.match(/<title[^>]*>([^<]+)<\/title>/i);
        const descMatch = html.match(/<meta[^>]*name="description"[^>]*content="([^"]+)"[^>]*>/i) ||
                          html.match(/<meta[^>]*property="og:description"[^>]*content="([^"]+)"[^>]*>/i);

        const title = titleMatch ? (titleMatch[1] || '').trim() : '';
        const description = descMatch ? (descMatch[1] || '').trim() : '';

        try {
          await generateOGImage({
            title: title || siteConfig.title,
            description: description || siteConfig.tagline || '',
            slug,
            ogDir: ogImagesDir,
            siteConfig,
          });
        } catch (err) {
          console.log(`  ⚠ Failed to generate OG image for ${slug}: ${err.message}`);
        }
      }

      if (fs.existsSync(ogImagePath)) {
        const imageUrl = `${siteConfig.url}/img/og/${imageFilename}?v=${buildVersion}`;
        // Build canonical page URL for better social parsing
        let pagePath = '';
        if (slug === 'home') {
          pagePath = '/';
        } else if (relativePath.startsWith('docs/')) {
          pagePath = `/docs/${slug}`;
        } else {
          pagePath = `/${slug}`;
        }
        const pageUrl = `${siteConfig.url}${pagePath}`;
        
        // Replace or add OG image meta tags
        // Remove existing og:image, twitter:image, and og:url tags
        html = html.replace(/<meta[^>]*property="og:image"[^>]*>/gi, '');
        html = html.replace(/<meta[^>]*name="twitter:image"[^>]*>/gi, '');
        html = html.replace(/<meta[^>]*property="og:url"[^>]*>/gi, '');
        
        // Add new OG image tags before </head>
        const ogTags = `
  <meta property="og:image" content="${imageUrl}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:secure_url" content="${imageUrl}">
  <meta property="og:site_name" content="${siteConfig.title}">
  <meta property="og:url" content="${pageUrl}">
  <meta name="twitter:image" content="${imageUrl}">
</head>`;
        
        html = html.replace(/<\/head>/i, ogTags);
        
        // Write back
        fs.writeFileSync(htmlFile, html, 'utf-8');
        console.log(`  ✓ Injected OG image: ${imageFilename}`);
      }
    } catch (error) {
      console.log(`  ⊘ Error processing ${path.basename(htmlFile)}: ${error.message}`);
    }

    // Progress update and GC hint every batch
    if (processed % BATCH_SIZE === 0) {
      console.log(`  Progress: ${processed}/${htmlFiles.length} HTML files injected`);
      if (global.gc) global.gc();
    }
  }

  // Final progress update
  console.log(`  Progress: ${processed}/${htmlFiles.length} HTML files injected`);
}

/**
 * Generate an OG image for a specific page
 */
async function generateOGImage({
  title,
  description,
  slug,
  ogDir,
  siteConfig,
}) {
  try {
    const satoriRenderer = await initSatori();
    const width = 1200;
    const height = 630;

    // Truncate title if too long
    const maxTitleLength = 60;
    const displayTitle =
      title.length > maxTitleLength
        ? title.substring(0, maxTitleLength) + "..."
        : title;

    // Truncate description
    const maxDescLength = 120;
    const displayDesc =
      description && description.length > maxDescLength
        ? description.substring(0, maxDescLength) + "..."
        : description || "";

    // Create SVG using React-like JSX syntax
    // Use cached fonts (loaded once at plugin startup)
    const resolvedFonts = loadFontsOnce();

    const svg = await satoriRenderer(
      {
        type: "div",
        props: {
          style: {
            height: "100%",
            width: "100%",
            display: "flex",
            flexDirection: "column",
            alignItems: "flex-start",
            justifyContent: "space-between",
            backgroundColor: "#1a1a2e",
            backgroundImage:
              "linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)",
            padding: 60,
            fontFamily: "Inter",
            position: "relative",
          },
          children: [
            // Decorative circles
            {
              type: "div",
              props: {
                style: {
                  position: "absolute",
                  top: -150,
                  right: -150,
                  width: 400,
                  height: 400,
                  borderRadius: "50%",
                  backgroundColor: "rgba(255, 255, 255, 0.03)",
                },
              },
            },
            {
              type: "div",
              props: {
                style: {
                  position: "absolute",
                  bottom: -100,
                  left: -100,
                  width: 300,
                  height: 300,
                  borderRadius: "50%",
                  backgroundColor: "rgba(255, 255, 255, 0.03)",
                },
              },
            },
            // Content
            {
              type: "div",
              props: {
                style: {
                  display: "flex",
                  flexDirection: "column",
                  gap: 40,
                },
                children: [
                  // Brand
                  {
                    type: "div",
                    props: {
                      style: {
                        fontSize: 24,
                        fontWeight: "bold",
                        color: "#5ee0e4",
                      },
                      children: "Panaversity • AI Native Development",
                    },
                  },
                  // Title
                  {
                    type: "div",
                    props: {
                      style: {
                        fontSize: 56,
                        fontWeight: "bold",
                        color: "#ffffff",
                        lineHeight: 1.2,
                        maxWidth: 1000,
                      },
                      children: displayTitle,
                    },
                  },
                  // Description
                  displayDesc && {
                    type: "div",
                    props: {
                      style: {
                        fontSize: 28,
                        color: "rgba(255, 255, 255, 0.7)",
                        lineHeight: 1.4,
                        maxWidth: 1000,
                      },
                      children: displayDesc,
                    },
                  },
                ].filter(Boolean),
              },
            },
            // Footer
            {
              type: "div",
              props: {
                style: {
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "space-between",
                  width: "100%",
                  paddingTop: 30,
                  borderTop: "4px solid #5ee0e4",
                },
                children: [
                  {
                    type: "div",
                    props: {
                      style: {
                        fontSize: 28,
                        fontWeight: "bold",
                        color: "#5ee0e4",
                      },
                      children: "agentfactory.panaversity.org",
                    },
                  },
                ],
              },
            },
          ],
        },
      },
      {
        width,
        height,
        fonts: resolvedFonts,
      }
    );

    // Convert SVG to PNG using Sharp
    const pngBuffer = await sharp(Buffer.from(svg)).png().toBuffer();

    // Save the image
    const filename = slug.replace(/\//g, "-") + ".png";
    const filepath = path.join(ogDir, filename);
    fs.writeFileSync(filepath, pngBuffer);

    console.log(`  ✓ Generated: ${filename}`);
    return filename;
  } catch (error) {
    console.error(
      `  ✗ Failed to generate image for "${title}":`,
      error.message
    );
    return null;
  }
}
