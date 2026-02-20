# Research: Metadata-Driven Slides Architecture

**Feature**: `035-metadata-driven-slides`
**Date**: 2025-11-23
**Phase**: Phase 0 (Research & Technology Investigation)

## Research Summary

This document captures technical research for implementing a remark plugin that injects PDFViewer components based on frontmatter metadata.

---

## 1. Remark Plugin Architecture

### Decision: Use Remark Plugin (Not Docusaurus Plugin)

**Rationale**:
- Remark plugins operate on markdown AST during MDX compilation
- Docusaurus automatically applies remark plugins during build
- Enables content transformation before React rendering
- Standard pattern for Docusaurus content extensions

**Alternatives Considered**:
1. **Docusaurus Plugin**: Would require implementing lifecycle hooks (contentLoaded, postBuild). More complex, operates after MDX processing. REJECTED: Too late in pipeline for AST manipulation.

2. **Webpack Loader**: Would require custom loader configuration. REJECTED: Docusaurus abstracts webpack, breaks on version upgrades.

3. **MDX Plugin**: Similar to remark but operates on different AST format. REJECTED: Remark is the standard Docusaurus pattern.

---

## 2. AST Transformation Strategy

### Decision: Inject JSX After "What You'll Learn" H2 Heading

**AST Node Types** (mdast specification):
- Frontmatter: `yaml` node (parsed by remark-frontmatter)
- Headings: `heading` nodes with `depth` property (1-6)
- Content: `paragraph`, `list`, `code`, etc.

**Injection Algorithm**:
```typescript
1. Parse frontmatter → Extract `slides` field
2. Traverse AST → Find heading with text "What You'll Learn"
3. Locate insertion point → Node immediately after heading
4. Detect path type → Local (no http/https) vs URL (http/https prefix)
5. Generate MDX node →
   - Import statement at top of document
   - JSX component with appropriate src prop
6. Inject nodes → Insert at calculated index
7. Return modified AST
```

**Alternatives Considered**:
1. **Inject at document end**: REJECTED - Users expect slides near top, after intro.
2. **Inject before first lesson**: REJECTED - "What You'll Learn" is consistent landmark across chapters.
3. **Require explicit marker (e.g., `{/* SLIDES */}`)**: REJECTED - Violates zero-markdown-changes requirement.

---

## 3. Path Normalization

### Decision: Simple Prefix Detection (http/https)

**Local Path Handling**:
```typescript
// Input: "slides/chapter-02.pdf"
// Detection: !src.startsWith('http://') && !src.startsWith('https://')
// Normalization: Ensure leading slash → "/slides/chapter-02.pdf"
// Rationale: Static directory maps to root URL path
```

**URL Handling**:
```typescript
// Input: "https://cdn.example.com/chapter-02.pdf"
// Detection: src.startsWith('http://') || src.startsWith('https://')
// Normalization: Use as-is (no transformation)
// Rationale: Full URLs are already absolute
```

**Alternatives Considered**:
1. **URL.parse validation**: REJECTED - Build should not fail on malformed URLs (graceful degradation).
2. **File existence check (local)**: REJECTED - Build-time filesystem checks slow down hot-reload.
3. **Complex schema (object with type field)**: REJECTED - YAGNI (future consideration if needed).

---

## 4. Frontmatter Schema

### Decision: Simple String Field

**Schema**:
```yaml
---
slides: "slides/chapter-02.pdf"  # Local path
# OR
slides: "https://cdn.example.com/chapter-02.pdf"  # Cloud URL
---
```

**Rationale**:
- Minimal cognitive load for content creators
- Polymorphic (handles both formats transparently)
- TypeScript type: `string | undefined`
- No breaking changes if schema evolves

**Alternatives Considered**:
1. **Object schema** (`{local: "...", url: "..."}`): REJECTED - Over-engineering, forces content creators to understand implementation.
2. **Array of URLs** (multiple slides): REJECTED - Current requirement is 1 slide per chapter.
3. **Separate fields** (`slidesLocal`, `slidesUrl`): REJECTED - Forces migration when switching storage.

---

## 5. MDX Import Injection

### Decision: Generate Import Statement at Document Start

**Implementation**:
```typescript
// Step 1: Check if import already exists (avoid duplicate)
const hasImport = tree.children.some(
  node => node.type === 'import' &&
          node.value.includes('@site/src/components/PDFViewer')
);

// Step 2: If no import, inject at document start
if (!hasImport) {
  tree.children.unshift({
    type: 'import',
    value: "import PDFViewer from '@site/src/components/PDFViewer';"
  });
}
```

**Rationale**:
- MDX requires imports before JSX usage
- Deduplication prevents duplicate imports (backward compat)
- Unshift (prepend) is standard pattern for remark import injection

**Alternatives Considered**:
1. **Inline import syntax** (`import()`): REJECTED - Not supported in MDX static analysis.
2. **Global component registration**: REJECTED - Docusaurus doesn't support this for custom components.

---

## 6. Error Handling Strategy

### Decision: Graceful Degradation with Console Warnings

**Philosophy**: Invalid slide references should NOT block build. Warn developers but continue compilation.

**Implementation**:
```typescript
try {
  // Attempt transformation
  injectSlidesComponent(tree, frontmatter);
} catch (error) {
  console.warn(`[remark-slides-metadata] Failed to inject slides for ${filePath}:`, error.message);
  // Return original tree (no modification)
  return tree;
}
```

**Validation Warnings**:
- Missing "What You'll Learn" section → Skip injection, log warning
- Malformed frontmatter → Skip injection, log warning
- Empty slides field → No action (chapters without slides are valid)

**Alternatives Considered**:
1. **Throw errors on invalid references**: REJECTED - Violates FR-010 (must not fail build).
2. **Silent failures**: REJECTED - Developers need visibility for debugging.

---

## 7. Testing Strategy

### Decision: Manual Testing with Dev Server

**Test Cases**:
1. **Local path**: `slides: "slides/chapter-02.pdf"` → Verify `/slides/chapter-02.pdf` rendered
2. **Cloud URL**: `slides: "https://cdn.example.com/file.pdf"` → Verify URL rendered as-is
3. **No slides field**: Frontmatter without slides → Verify no injection, no errors
4. **Existing JSX**: Chapter with manual PDFViewer → Verify both work (dual-support)
5. **Missing section**: Chapter without "What You'll Learn" → Verify warning logged, build succeeds
6. **Hot-reload**: Modify frontmatter during dev → Verify plugin re-processes instantly

**Rationale**:
- Unit tests for simple AST transformation add overhead without value
- Manual testing covers all acceptance scenarios
- Build validation ensures no regressions

**Alternatives Considered**:
1. **Jest unit tests**: REJECTED - Over-engineering for deterministic transformation.
2. **E2E visual tests**: REJECTED - Manual verification sufficient for internal tool.

---

## 8. Dependencies

### Decision: Minimal Remark Ecosystem Packages

**Required**:
```json
{
  "dependencies": {
    "unist-util-visit": "^5.0.0",     // AST traversal
    "mdast-util-to-string": "^4.0.0"  // Extract text from heading nodes
  }
}
```

**Rationale**:
- `unist-util-visit`: Standard library for AST traversal (battle-tested)
- `mdast-util-to-string`: Extracts text content from nodes (e.g., heading text)
- Both are lightweight, zero transitive dependencies

**Alternatives Considered**:
1. **gray-matter** (frontmatter parsing): REJECTED - Docusaurus already parses frontmatter, accessible via `vfile.data.frontMatter`.
2. **remark-mdx**: REJECTED - Docusaurus includes this, no explicit dependency needed.

---

## 9. Plugin Configuration

### Decision: Zero-Config Plugin

**Registration** (docusaurus.config.ts):
```typescript
presets: [
  ['classic', {
    docs: {
      remarkPlugins: [
        './plugins/remark-slides-metadata/index.ts'
      ]
    }
  }]
]
```

**Rationale**:
- No configuration options needed (behavior is fixed)
- Plugin auto-detects slides metadata
- Follows "convention over configuration" principle

**Alternatives Considered**:
1. **Configurable injection point** (allow custom heading text): REJECTED - YAGNI, "What You'll Learn" is standard.
2. **Enable/disable per-document**: REJECTED - Presence of `slides` field already acts as opt-in.

---

## 10. Performance Considerations

### Decision: No Optimization Needed

**Analysis**:
- AST traversal is O(n) where n = nodes per document (~500-1000 nodes/chapter)
- Frontmatter parsing is already done by Docusaurus (no additional cost)
- String operations (path detection) are O(1)
- **Total overhead per file: <1ms** (negligible)

**Measurement Plan**:
- Baseline build time: `npm run build` (before implementation)
- Post-implementation build time: `npm run build` (after implementation)
- **Acceptance**: <5% build time increase for 84 chapters

**Alternatives Considered**:
1. **Caching transformed ASTs**: REJECTED - Docusaurus already caches, redundant.
2. **Parallel processing**: REJECTED - Docusaurus parallelizes at file level, not AST level.

---

## Research Outcomes

### Resolved Unknowns

All technical unknowns from spec.md resolved:

1. ✅ **Remark plugin architecture**: Standard Docusaurus pattern, proven approach
2. ✅ **AST injection strategy**: Inject after "What You'll Learn" H2 heading
3. ✅ **Path detection**: Simple http/https prefix check
4. ✅ **Frontmatter schema**: String field (polymorphic)
5. ✅ **Error handling**: Graceful degradation with warnings
6. ✅ **Testing approach**: Manual testing, build validation
7. ✅ **Performance impact**: <1ms per file, negligible

### Next Phase

**Phase 1: Design & Contracts** ready to begin. Proceed to:
- `data-model.md`: Frontmatter schema + AST node structure
- `quickstart.md`: Content creator usage guide
- Update agent context with technology decisions
