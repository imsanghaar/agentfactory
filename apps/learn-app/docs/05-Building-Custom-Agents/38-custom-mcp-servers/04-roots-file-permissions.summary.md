### Core Concept
Roots solve two problems: path discovery (Claude knows where to search) and security (prevents access outside boundaries). Implement list_roots() to expose directories, is_path_allowed() to validate every file operation.

### Key Mental Models
- **Path discovery**: Without roots, Claude guesses file locations and fails repeatedly
- **Whitelist security**: Only approved paths accessible; deny everything else
- **Path normalization**: Always use os.path.abspath() + os.path.realpath() before validation
- **Defense in depth**: Validate in EVERY tool that accesses filesystem

### Critical Patterns
- list_roots(): `@mcp.list_roots()` returns `[Root(uri=f"file://{path}", name="...")]`
- is_path_allowed(): Normalize path, resolve symlinks, check commonpath against roots
- Symlink handling: `os.path.realpath()` resolves symlinks to prevent escape attacks
- Traversal prevention: `os.path.abspath()` normalizes `../` sequences

### AI Collaboration Keys
- Roots tell Claude: "Search in Videos and Downloads, nowhere else"
- Security maintained even if user tries malicious paths
- Test with traversal attempts: `../../etc/passwd` should fail

### Common Mistakes
- Forgetting to validate in every tool (security hole in unvalidated tool)
- Not resolving symlinks (allows escape via symbolic links)
- Too-permissive roots (e.g., entire home directory defeats purpose)

### Connections
- **Builds on**: Progress & Logging Notifications (Lesson 3)
- **Leads to**: StreamableHTTP Transport (Lesson 5)
