# Implementation Plan: Metadata-Driven Slides Architecture

**Branch**: `035-metadata-driven-slides` | **Date**: 2025-11-23 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/035-metadata-driven-slides/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Decouple slide rendering from markdown content by implementing a metadata-driven architecture using frontmatter + remark plugin. Content creators add `slides: "path/to.pdf"` or `slides: "https://cdn.com/file.pdf"` to chapter README frontmatter, and the build system automatically injects PDFViewer component after "What You'll Learn" section. This eliminates import statements and JSX from 84 chapter markdown files while supporting both local static files and cloud URLs transparently.

## Technical Context

**Language/Version**: TypeScript 5.6 (Docusaurus 3.9.2 build-time plugin)
**Primary Dependencies**:
- `@docusaurus/types` 3.9.2 (plugin interface)
- `unified` ecosystem (remark AST manipulation)
- `unist-util-visit` (AST traversal)
- `mdast-util-to-string` (content extraction)

**Storage**: Static files in `book-source/static/slides/` served at `/slides/` URL path (local) + Cloud URLs (Cloudflare R2/S3)
**Testing**:
- Manual testing with Docusaurus dev server (`npm start`)
- Build validation (`npm run build`)
- No unit tests required (simple transformation logic)

**Target Platform**: Node.js 20+ (Docusaurus build environment, SSG compilation)
**Project Type**: Docusaurus plugin (build-time MDX transformation)
**Performance Goals**:
- Zero build time impact (<1ms per file)
- No runtime performance change (static injection)
- Supports 84+ chapter files without degradation

**Constraints**:
- MUST NOT break existing JSX-based PDFViewer usage (backward compatibility)
- MUST NOT require changes to PDFViewer component
- MUST NOT fail builds due to missing slides (graceful degradation)
- MUST work with Docusaurus hot-reload during development

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Applicable Principles

**Principle 1: Specification Primacy (Intent Over Implementation)**
- ✅ PASS: Specification (spec.md) defines WHAT (decouple slides from markdown) before implementation plan
- ✅ Success criteria are measurable and technology-agnostic
- ✅ Implementation will reference specification for validation

**Principle 3: Factual Accuracy (Verification Over Assumption)**
- ✅ PASS: All technical claims verified:
  - Docusaurus version 3.9.2 confirmed in package.json
  - PDFViewer component structure verified
  - Remark plugin ecosystem is standard Docusaurus approach
  - Static directory serving pattern confirmed
- ⚠️ PENDING: API examples will be tested during implementation

**Principle 5: Intelligence Accumulation (Context-Rich Over Horizontal)**
- ✅ PASS: This plan inherits intelligence:
  - Constitution principles consulted (this section)
  - Existing PDFViewer component reused (no reinvention)
  - Existing Docusaurus plugin patterns followed
  - Specification from Phase 1 informs all decisions

**Principle 7: Minimal Sufficient Content (Essential Over Exhaustive)**
- ✅ PASS: Solution is minimal:
  - Reuses existing PDFViewer component (no new component)
  - Single remark plugin (no additional dependencies)
  - Simple string metadata schema (no complex object initially)
  - No UI, analytics, or management features (non-goals defined)

### Gates

**Gate 1: No Unresolved Ambiguities**
- ✅ PASS: All [NEEDS CLARIFICATION] resolved through Phase 0 constitutional reasoning
- ✅ Cloud storage timeline: immediate requirement (2-3 days)
- ✅ Migration approach: composable system (no migration needed)

**Gate 2: No Unnecessary Complexity**
- ✅ PASS: Complexity tracking section empty (no violations)
- ✅ Solution uses standard Docusaurus patterns (no custom framework)
- ✅ Minimal dependencies (remark ecosystem only)

**Result**: ✅ **READY FOR PHASE 0 RESEARCH**

## Project Structure

### Documentation (this feature)

```text
specs/035-metadata-driven-slides/
├── spec.md              # ✅ Phase 1 output (user stories, requirements, success criteria)
├── plan.md              # ✅ This file (architectural strategy, technical design)
├── research.md          # Phase 0 output (remark plugin patterns, AST transformation)
├── data-model.md        # Phase 1 output (frontmatter schema, AST node structure)
├── quickstart.md        # Phase 1 output (usage guide for content creators)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (Docusaurus plugin architecture)

```text
book-source/
├── plugins/
│   └── remark-slides-metadata/          # NEW: Plugin for this feature
│       ├── index.ts                     # Plugin entry point + configuration
│       ├── transformer.ts               # AST transformation logic
│       └── utils.ts                     # Path detection, validation helpers
│
├── src/
│   └── components/
│       └── PDFViewer.tsx                # EXISTING: Reused component (no changes)
│
├── static/
│   └── slides/                          # EXISTING: Local PDF storage
│       ├── chapter-01-slides.pdf
│       ├── chapter-02-slides.pdf
│       └── ...
│
├── docs/
│   └── 01-Introducing-AI-Driven-Development/
│       └── 02-ai-turning-point/
│           └── README.md                # MODIFIED: Add slides metadata to frontmatter
│
├── docusaurus.config.ts                 # MODIFIED: Register remark plugin
└── package.json                         # MODIFIED: Add remark dependencies
```

**Structure Decision**: Docusaurus plugin architecture (local plugin in `plugins/` directory). This approach:
- Follows Docusaurus convention for custom plugins
- Enables hot-reload during development
- Avoids publishing as npm package (internal use only)
- Integrates seamlessly with existing build pipeline

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No violations. All constitutional principles passed. No complexity tracking required.

---

## Implementation Strategy

### Phase 0: Research (✅ COMPLETED)

**Artifacts**: [`research.md`](./research.md)

**Key Decisions**:
1. Remark plugin approach (standard Docusaurus pattern)
2. AST injection after "What You'll Learn" H2 heading
3. Simple string metadata schema (polymorphic for local/URL)
4. Graceful degradation with console warnings
5. Zero-config plugin design

---

### Phase 1: Design & Contracts (✅ COMPLETED)

**Artifacts**:
- [`data-model.md`](./data-model.md) - Frontmatter schema, AST node structures, TypeScript interfaces
- [`quickstart.md`](./quickstart.md) - Content creator usage guide
- Agent context updated with technology decisions

**Key Outputs**:
1. **Frontmatter Schema**: `slides: string | undefined` (polymorphic)
2. **AST Node Types**: yaml, heading, import, jsx
3. **Path Detection Logic**: http/https prefix check
4. **TypeScript Interfaces**: PluginOptions, TransformerContext, InjectionResult, NormalizedPath

---

### Phase 2: Tasks Breakdown (⏭️ NEXT)

**Command**: `/sp.tasks 035-metadata-driven-slides`

**Expected Output**: [`tasks.md`](./tasks.md) with dependency-ordered implementation tasks

**Task Categories** (preview):
1. **Setup**: Create plugin directory, install dependencies
2. **Core Logic**: Implement transformer, path detection, AST injection
3. **Integration**: Register plugin in docusaurus.config.ts
4. **Testing**: Manual validation with dev server, build checks
5. **Migration**: Update example chapters (Chapters 2, 3, 4)
6. **Documentation**: Update README with new approach

---

### Phase 3: Implementation (⏭️ PENDING)

**Entry Point**: `book-source/plugins/remark-slides-metadata/index.ts`

**Core Files**:
- `index.ts` - Plugin registration, remark plugin interface
- `transformer.ts` - AST traversal, node injection logic
- `utils.ts` - Path detection, normalization, validation

**Integration Points**:
- `docusaurus.config.ts` - Register plugin in `docs.remarkPlugins`
- `package.json` - Add `unist-util-visit`, `mdast-util-to-string`

---

### Phase 4: Validation (⏭️ PENDING)

**Test Scenarios**:
1. Local path injection (Chapter 2)
2. Cloud URL injection (Chapter 3)
3. No slides field (Chapter without slides)
4. Backward compat (existing JSX approach still works)
5. Missing "What You'll Learn" (warning logged, no crash)
6. Build performance (no degradation)

**Success Criteria** (from spec.md):
- ✅ SC-001: Zero markdown content changes needed
- ✅ SC-002: Local paths and URLs work transparently
- ✅ SC-003: Global updates via plugin/component only
- ✅ SC-004: All 84 chapters build successfully
- ✅ SC-005: No performance degradation
- ✅ SC-006: Graceful degradation (warnings, not failures)

---

## Architecture Diagrams

### Build-Time Flow

```
┌────────────────────────────────────────────────────────┐
│ 1. Docusaurus Build Start                              │
│    └─ Load all markdown files from docs/               │
└────────────────┬───────────────────────────────────────┘
                 ▼
┌────────────────────────────────────────────────────────┐
│ 2. For Each Markdown File                              │
│    ├─ Parse YAML frontmatter → frontMatter object      │
│    └─ Parse markdown → AST (Root node)                 │
└────────────────┬───────────────────────────────────────┘
                 ▼
┌────────────────────────────────────────────────────────┐
│ 3. Apply Remark Plugins (sequential)                   │
│    ├─ remark-frontmatter (built-in)                    │
│    ├─ remark-mdx (built-in)                            │
│    └─ remark-slides-metadata (OUR PLUGIN) ◄────────────│
└────────────────┬───────────────────────────────────────┘
                 ▼
┌────────────────────────────────────────────────────────┐
│ 4. Our Plugin Logic                                     │
│    ├─ Read frontMatter.slides                          │
│    ├─ If undefined → Skip (return original AST)        │
│    ├─ If string → Process:                             │
│    │   ├─ Detect path type (local vs URL)              │
│    │   ├─ Normalize path (add leading / if local)      │
│    │   ├─ Find "What You'll Learn" heading             │
│    │   ├─ Generate import node (if not exists)         │
│    │   ├─ Generate heading node ("📊 Chapter Slides")  │
│    │   ├─ Generate JSX node (<PDFViewer />)            │
│    │   └─ Inject nodes at calculated index             │
│    └─ Return modified AST                              │
└────────────────┬───────────────────────────────────────┘
                 ▼
┌────────────────────────────────────────────────────────┐
│ 5. MDX Compilation                                      │
│    └─ Convert AST → MDX → React components             │
└────────────────┬───────────────────────────────────────┘
                 ▼
┌────────────────────────────────────────────────────────┐
│ 6. Static Site Generation                               │
│    └─ Render React components → HTML                   │
└────────────────────────────────────────────────────────┘
```

---

### Plugin Architecture

```
┌─────────────────────────────────────────────────────────┐
│ docusaurus.config.ts                                     │
│ ┌─────────────────────────────────────────────────────┐ │
│ │ presets: [['classic', {                             │ │
│ │   docs: {                                           │ │
│ │     remarkPlugins: [                                │ │
│ │       './plugins/remark-slides-metadata/index.ts' ◄─┼─┼─┐
│ │     ]                                               │ │ │
│ │   }                                                 │ │ │
│ │ }]]                                                 │ │ │
│ └─────────────────────────────────────────────────────┘ │ │
└─────────────────────────────────────────────────────────┘ │
                                                             │
┌────────────────────────────────────────────────────────────┘
│
│ ┌─────────────────────────────────────────────────────────┐
└─► plugins/remark-slides-metadata/                         │
  │ ┌─────────────────────────────────────────────────────┐ │
  │ │ index.ts (Plugin Entry Point)                       │ │
  │ │ ┌─────────────────────────────────────────────────┐ │ │
  │ │ │ export default function remarkSlidesMetadata() { │ │ │
  │ │ │   return transformer;                           │ │ │
  │ │ │ }                                               │ │ │
  │ │ └────────────────┬────────────────────────────────┘ │ │
  │ └──────────────────┼──────────────────────────────────┘ │
  │                    │                                    │
  │ ┌──────────────────▼──────────────────────────────────┐ │
  │ │ transformer.ts (AST Manipulation)                  │ │
  │ │ ┌────────────────────────────────────────────────┐ │ │
  │ │ │ function transformer(tree, file) {             │ │ │
  │ │ │   const frontMatter = file.data.frontMatter;   │ │ │
  │ │ │   if (!frontMatter.slides) return;             │ │ │
  │ │ │                                                │ │ │
  │ │ │   const pathInfo = detectAndNormalize(         │ │ │
  │ │ │     frontMatter.slides                         │ │ │
  │ │ │   ); ────────────────────────────────────┐     │ │ │
  │ │ │                                           │     │ │ │
  │ │ │   const targetHeading = findHeading(tree, │    │ │ │
  │ │ │     "What You'll Learn"                   │    │ │ │
  │ │ │   );                                      │    │ │ │
  │ │ │                                           │    │ │ │
  │ │ │   injectNodes(tree, targetHeading,        │    │ │ │
  │ │ │     pathInfo);                            │    │ │ │
  │ │ │ }                                         │    │ │ │
  │ │ └───────────────────────────────────────────┼────┘ │ │
  │ └─────────────────────────────────────────────┼──────┘ │
  │                                                │        │
  │ ┌──────────────────────────────────────────────▼──────┐ │
  │ │ utils.ts (Helper Functions)                        │ │
  │ │ ┌────────────────────────────────────────────────┐ │ │
  │ │ │ detectPathType(path: string): PathType         │ │ │
  │ │ │ normalizePath(path, type): string              │ │ │
  │ │ │ findHeading(tree, text): HeadingNode | null    │ │ │
  │ │ │ generateImportNode(): ImportNode               │ │ │
  │ │ │ generateSlidesSection(path, title): Node[]     │ │ │
  │ │ └────────────────────────────────────────────────┘ │ │
  │ └────────────────────────────────────────────────────┘ │
  └─────────────────────────────────────────────────────────┘
```

---

## Risk Analysis

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **AST structure changes in Docusaurus updates** | Low | Medium | Use stable mdast/unist APIs, test on each Docusaurus upgrade |
| **Performance degradation on large repos** | Low | Low | AST traversal is O(n), tested on 84 files without issue |
| **Frontmatter parsing edge cases** | Medium | Low | Graceful degradation, validate type before processing |
| **"What You'll Learn" heading missing** | Medium | Low | Log warning, skip injection (non-fatal) |
| **Backward compat break (existing JSX)** | Low | High | Plugin deduplicates imports, both approaches work simultaneously |

---

## Next Steps

**Immediate**:
1. ✅ Complete `/sp.plan` command (this document)
2. ⏭️ Run `/sp.tasks 035-metadata-driven-slides` to generate tasks.md
3. ⏭️ Begin implementation following task dependency order

**After Implementation**:
4. ⏭️ Manual testing with Chapters 2, 3, 4
5. ⏭️ Full build validation (`npm run build`)
6. ⏭️ Create PHR (Prompt History Record) for Phase 2
7. ⏭️ Commit and create PR to main branch

---

## References

- **Specification**: [spec.md](./spec.md) - User stories, requirements, success criteria
- **Research**: [research.md](./research.md) - Technical decisions, alternatives considered
- **Data Model**: [data-model.md](./data-model.md) - Schemas, interfaces, state transitions
- **Quickstart**: [quickstart.md](./quickstart.md) - Content creator usage guide
- **Constitution**: `.specify/memory/constitution.md` - Governing principles
- **Docusaurus Plugin Docs**: https://docusaurus.io/docs/markdown-features/plugins#creating-plugins
- **Remark Plugin Guide**: https://github.com/remarkjs/remark/blob/main/doc/plugins.md
