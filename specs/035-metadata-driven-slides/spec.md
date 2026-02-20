# Feature Specification: Metadata-Driven Slides Architecture

**Feature Branch**: `035-metadata-driven-slides`
**Created**: 2025-11-23
**Status**: Draft
**Input**: User description: "Implement metadata-driven slides architecture with frontmatter and remark plugin for decoupled, composable slide rendering"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Content Creator Adds Slides via Frontmatter (Priority: P1)

A content creator adds slide PDFs to chapter documentation without modifying markdown content or importing components. They simply add metadata to the frontmatter and the system handles rendering.

**Why this priority**: This is the core value proposition - decoupling content from presentation. Enables all 84 chapters to adopt slides without polluting markdown with imports and JSX.

**Independent Test**: Can be fully tested by adding `slides: "path/to.pdf"` to any chapter README frontmatter and verifying PDF renders after build without any imports or JSX in the markdown content.

**Acceptance Scenarios**:

1. **Given** a chapter README with frontmatter, **When** content creator adds `slides: "slides/chapter-01.pdf"`, **Then** slides render below "What You'll Learn" section without requiring any imports
2. **Given** a chapter README without slides metadata, **When** content remains unchanged, **Then** no slides section appears (backward compatible)
3. **Given** a chapter with existing PDFViewer JSX, **When** migrated to metadata approach, **Then** old approach continues working (no breaking changes)

---

### User Story 2 - Content Creator Uses Cloud URL Instead of Local Path (Priority: P1)

A content creator references slides hosted on CDN/cloud storage (Cloudflare R2, S3) by providing a full URL instead of a local path. The system renders the slides identically regardless of source.

**Why this priority**: Cloud migration is happening in 2-3 days, so URL support is immediate requirement (not future-proofing). System must be composable from day one.

**Independent Test**: Can be fully tested by setting `slides: "https://cdn.example.com/chapter-01.pdf"` and verifying the PDF renders identically to local path approach.

**Acceptance Scenarios**:

1. **Given** frontmatter with `slides: "https://r2.cloudflare.com/slides/chapter-01.pdf"`, **When** page builds, **Then** slides render from cloud URL
2. **Given** frontmatter with `slides: "slides/chapter-01.pdf"` (local), **When** page builds, **Then** slides render from local static directory
3. **Given** mixed chapters (some local, some URL), **When** site builds, **Then** all slides render correctly regardless of source
4. **Given** invalid URL or missing local file, **When** page builds, **Then** build succeeds with warning logged (graceful degradation)

---

### User Story 3 - Developer Maintains Slides Across 84 Chapters (Priority: P2)

A developer needs to update slide rendering behavior (e.g., change height, add download button, modify styling) across all 84 chapters from a single location without touching individual markdown files.

**Why this priority**: Centralized maintenance is the key benefit of decoupling. Changes propagate automatically without manual updates to 84 files.

**Independent Test**: Can be fully tested by modifying the remark plugin or PDFViewer component and verifying changes apply to all chapters with slides metadata.

**Acceptance Scenarios**:

1. **Given** remark plugin renders slides with height=700, **When** developer changes default to height=800 in plugin, **Then** all chapters reflect new height without markdown changes
2. **Given** PDFViewer component lacks download button, **When** developer adds download functionality, **Then** all chapters gain download button without per-file updates
3. **Given** slides use light mode styling, **When** developer updates dark mode colors, **Then** all slides respect new dark mode without touching markdown

---

### User Story 4 - Build System Validates Slide References (Priority: P3)

During build, the system validates that slide references (local paths or URLs) are accessible and warns developers about broken references without failing the build.

**Why this priority**: Helps catch issues early but shouldn't block deployment if a single slide is temporarily unavailable.

**Independent Test**: Can be fully tested by intentionally adding invalid slide references and verifying build warnings appear in logs while build still succeeds.

**Acceptance Scenarios**:

1. **Given** frontmatter with `slides: "slides/nonexistent.pdf"`, **When** build runs, **Then** warning logged but build succeeds
2. **Given** frontmatter with `slides: "https://unreachable-cdn.com/slide.pdf"`, **When** build runs, **Then** warning logged but build succeeds
3. **Given** all slide references are valid, **When** build runs, **Then** no warnings and slides render correctly

---

### Edge Cases

- What happens when frontmatter has both local path and old-style JSX import? (Plugin should take precedence, JSX becomes redundant but doesn't break)
- How does system handle malformed URLs in slides metadata? (Graceful degradation: log warning, skip rendering, don't crash build)
- What if "What You'll Learn" section doesn't exist in README? (Plugin should inject after title or skip injection if no suitable anchor point found)
- How are relative vs absolute local paths handled? (Normalize to absolute from static directory: `slides/X.pdf` → `/slides/X.pdf`)
- What if slides metadata is an object with multiple formats? (Future: support `slides: {pdf: "local.pdf", url: "cdn-url"}`, initially treat as string)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST parse `slides` metadata from chapter README frontmatter (YAML format)
- **FR-002**: System MUST detect whether `slides` value is local path (no http/https prefix) or URL (starts with http:// or https://)
- **FR-003**: System MUST inject PDFViewer component automatically at build time after "What You'll Learn" section when slides metadata present
- **FR-004**: System MUST render local path slides by resolving path relative to static directory (`slides/X.pdf` → `/slides/X.pdf`)
- **FR-005**: System MUST render URL slides by using URL as-is in PDFViewer src prop
- **FR-006**: System MUST NOT require any imports or JSX in markdown content when using metadata approach
- **FR-007**: System MUST maintain backward compatibility with existing JSX-based PDFViewer usage (both approaches work simultaneously)
- **FR-008**: System MUST inject PDFViewer using existing component (`@site/src/components/PDFViewer`)
- **FR-009**: System MUST support chapters without slides metadata (no rendering, no errors)
- **FR-010**: System MUST log warnings for invalid slide references without failing build
- **FR-011**: System MUST work with Docusaurus build pipeline (remark plugin compatible with MDX processing)

### Key Entities *(include if feature involves data)*

- **Chapter README**: Markdown file with YAML frontmatter containing metadata including optional `slides` field
- **Slides Metadata**: String value in frontmatter representing either local path or full URL to PDF slide deck
- **PDFViewer Component**: React component that renders embedded PDF with dark mode and fullscreen support
- **Remark Plugin**: Build-time transformer that parses frontmatter and injects JSX into markdown AST

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Content creators can add slides to any chapter by editing only frontmatter (zero markdown content changes)
- **SC-002**: System supports both local paths and cloud URLs transparently (no code changes needed when migrating to cloud)
- **SC-003**: Developers can modify slide rendering globally by updating plugin/component (zero per-chapter updates needed)
- **SC-004**: All 84 chapters build successfully with slides metadata (backward compatibility maintained)
- **SC-005**: Build completes in same timeframe as current implementation (no performance degradation from plugin processing)
- **SC-006**: Invalid slide references produce warnings but don't block deployment (graceful degradation)

## Assumptions *(if any)*

- All chapter READMEs use YAML frontmatter (not TOML or JSON)
- "What You'll Learn" section exists in standard location (H2 heading after intro)
- Static slides directory (`book-source/static/slides/`) is served at `/slides/` URL path
- PDFViewer component accepts `src`, `title`, and `height` props
- Docusaurus version supports remark plugins in configuration
- Cloud migration to Cloudflare R2 or similar will occur in 2-3 days (URL support is immediate requirement, not future)
- Existing PDFViewer JSX approach will eventually be removed after all chapters migrate to metadata (no permanent dual-support needed)

## Constraints

- MUST NOT break existing chapters during migration (both approaches work simultaneously)
- MUST NOT require changes to PDFViewer component (reuse as-is)
- MUST NOT add build-time dependencies beyond remark plugin ecosystem
- MUST NOT require manual updates to 84 chapter files (composability requirement)
- MUST NOT fail builds due to missing slides (warn only, degrade gracefully)

## Non-Goals

- Creating new PDF rendering component (reuse existing PDFViewer)
- Supporting slide formats other than PDF (out of scope)
- Implementing slide generation pipeline (handled by NotebookLM workflow)
- Adding slide management UI (metadata editing done via text editor)
- Versioning or caching strategy for cloud-hosted slides (handled by CDN layer)
- Analytics or tracking for slide views (separate concern)
- Automated migration script to update all 84 chapters (manual update acceptable given simplicity of frontmatter change)

## Open Questions *(for clarification)*

None - all critical decisions resolved through Phase 0 clarification:
1. Cloud storage timeline: 2-3 days (immediate URL support required)
2. Migration approach: Composable system handles both formats (no migration needed)
