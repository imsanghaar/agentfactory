---
sidebar_position: 11
title: "Chapter 14: Ten Axioms Quiz"
proficiency_level: B1
layer: 2
estimated_time: "30 mins"
chapter_type: Concept
running_example_id: ten-axioms-quiz
---

# Chapter 14: Ten Axioms of Agentic Development Quiz

Test your understanding of the ten axioms that govern effective agentic software development — from shell orchestration through production observability. These questions follow James's journey building an order management system, the same running example from the chapter lessons.

<Quiz
  title="Chapter 14: Ten Axioms of Agentic Development Assessment"
  questions={[
    {
      question: "James has an 80-line bash script that fetches order data from an API, transforms it with jq, filters results with grep, and writes output to a file. The script has nested if-else blocks for error handling and retry logic. Emma reviews it and says it needs restructuring. What should James do?",
      options: [
        "Keep the full script in bash and add set -euo pipefail at the top — the shell is designed to handle error propagation through exit codes and trap handlers, so the retry logic just needs proper signal handling",
        "Rewrite the entire workflow as a Python CLI application using click and requests, since Python's try/except and type hints make complex control flow more maintainable than bash conditionals",
        "Refactor the script into modular shell functions (fetch_data, transform_data, filter_results) within the same file, using local variables and return codes to isolate each concern",
        "Keep the shell as the orchestrator that pipes and coordinates tools, but extract the retry logic and complex transformations into a typed, tested Python program that the shell calls"
      ],
      correctOption: 3,
      explanation: "Axiom I (Shell as Orchestrator) distinguishes between the shell's role as coordinator and programs' role as computational engines. The shell excels at piping data between programs, but when logic grows complex (nested conditionals, retry mechanisms, state management), that logic has crossed the complexity threshold and belongs in a proper program. The shell should still orchestrate (call the program, pipe its output), but the computation itself should be a typed, tested program. Option A sounds disciplined (set -euo pipefail is good practice) but doesn't solve the fundamental issue — complex retry logic with state management exceeds what bash handles well. Option B eliminates the shell entirely when it should still orchestrate the pipeline. Option C improves readability but the complexity remains in bash where it can't be typed or tested.",
      source: "Lesson 01: Shell as Orchestrator"
    },
    {
      question: "James needs to coordinate four steps for his order system deployment: run ruff formatting, run pyright type checking, run pytest, and build a Docker image. He writes a Python script that calls subprocess.run() for each step. What architectural problem does this introduce?",
      options: [
        "The subprocess.run() calls create a process-spawning chain where each command runs in a child process of Python, which is itself a child process, adding latency and making signal propagation unreliable across the process tree",
        "He replaced the shell (the natural orchestrator) with a program, hiding sequential coordination logic inside Python code that is harder to inspect and modify than a Makefile or shell script",
        "The script will fail silently if any subprocess returns a non-zero exit code unless James explicitly passes check=True to each subprocess.run() call — a subtle bug that Makefile targets and shell set -e handle automatically",
        "The Python script couples the deployment workflow to a specific Python version and its installed packages, creating a bootstrap problem where you need a working Python environment to set up the Python environment"
      ],
      correctOption: 1,
      explanation: "Axiom I states that the shell is the natural orchestration layer — it coordinates programs. By wrapping shell orchestration inside Python (using subprocess.run), James hides the coordination logic inside a program, making it harder to read, modify, and debug. A Makefile or shell script would express this coordination more transparently: each step is visible, the flow is obvious, and any developer can understand or modify it without Python knowledge. The shell coordinates; programs compute. When your 'program' is just calling other programs in sequence, it should be shell orchestration. Option A identifies a real but minor concern — the overhead exists but isn't the architectural issue. Option C identifies a genuinely dangerous pitfall of subprocess.run() — silent failures are a real bug source — but it describes an implementation-level fix (add check=True) rather than the architectural mistake of using the wrong layer for coordination. Option D raises a valid practical concern about the bootstrap problem, but the core issue is layer confusion, not dependency management.",
      source: "Lesson 01: Shell as Orchestrator"
    },
    {
      question: "James's team stores project decisions in a Notion database, API documentation in Confluence, and coding standards in a Google Doc. When James asks Claude Code to follow the team's coding standards, the AI cannot access any of these sources. What axiom are they violating?",
      options: [
        "Knowledge is Markdown — persistent knowledge should live in version-controlled markdown files that AI agents can read directly from the repository without authentication",
        "Shell as Orchestrator — they should write a shell pipeline using each platform's API to fetch and pipe content into the AI's context before each session",
        "Version Control is Memory — they should export their Notion database, Confluence pages, and Google Docs as HTML snapshots and commit them to the repository alongside the source code",
        "Observability Extends Verification — they need a monitoring dashboard that tracks documentation freshness across all three platforms and alerts when content becomes stale"
      ],
      correctOption: 0,
      explanation: "Axiom II (Knowledge is Markdown) states that all persistent knowledge should live in markdown files because markdown is human-readable, version-controllable, AI-parseable, and tool-agnostic. Notion, Confluence, and Google Docs are proprietary silos that require API authentication, special tooling, and network access for AI to read. Markdown files (CLAUDE.md, ADRs, README.md) sit in the repository where any AI agent can read them directly with standard file access. Option B is creative but creates a fragile dependency — if any API changes or credentials expire, the pipeline breaks, and the knowledge is still locked in proprietary platforms. Option C commits files to git (good) but HTML is noisy and the source of truth remains in external platforms that can diverge from the committed snapshots. Option D monitors staleness but doesn't solve the access problem.",
      source: "Lesson 02: Knowledge is Markdown"
    },
    {
      question: "James creates a DECISIONS.md file to track architectural choices for his order system but writes entries like: 'We picked PostgreSQL because it seemed good.' Three months later, when Emma asks why they didn't choose SQLite, nobody can reconstruct the reasoning. What aspect of Axiom II did James miss?",
      options: [
        "He should have used a structured YAML or JSON schema for decisions, with required fields enforced by a linter, so that incomplete entries are caught before they're committed to the repository",
        "He should have stored each decision in its own numbered ADR file (001-database-choice.md, 002-api-framework.md) under a dedicated decisions/ directory, with cross-references between related decisions",
        "He captured the decision but not the reasoning — effective markdown knowledge must include the problem context, alternatives considered, and rationale",
        "He should have used GitHub Discussions or a wiki platform where team members can comment, ask questions, and add context collaboratively rather than relying on a static markdown file"
      ],
      correctOption: 2,
      explanation: "Axiom II requires that markdown knowledge be self-contained and complete. 'Seemed good' provides no reconstructible context — future developers (or AI agents) cannot understand the trade-offs, alternatives considered, or constraints that drove the choice. Proper markdown knowledge includes: the problem, options considered, decision made, and reasoning. An ADR (Architecture Decision Record) format captures all of this. The axiom isn't just 'use markdown files' — it's 'encode knowledge completely in markdown so it persists beyond the original author's memory.' Option A enforces structure but a linter can't judge whether reasoning is sufficient — you can fill required fields with shallow content. Option B improves organization (and ADR numbering is good practice) but individual files with 'seemed good' are just as useless as one big file with 'seemed good.' Option D enables discussion but the captured knowledge still needs to be self-contained — comments scatter context rather than consolidating it.",
      source: "Lesson 02: Knowledge is Markdown"
    },
    {
      question: "James has a 200-line bash script for his order system that parses CSV order exports, validates customer email formats with regex, handles database connections, and sends HTTP requests with retry logic. It works most of the time but has no tests and fails silently on edge cases. Which axiom guides the fix?",
      options: [
        "Shell as Orchestrator — restructure the script so bash coordinates four focused tools (csvkit for parsing, a regex validator, psql for database access, and curl with retry flags) piped together through stdin/stdout",
        "Programs Over Scripts — this script has crossed the complexity threshold and should graduate to a typed Python program with the full discipline stack (pyright, pytest, ruff, uv) and CI integration",
        "Composition Over Monoliths — split it into four smaller bash scripts (parse_csv.sh, validate_email.sh, db_connect.sh, http_request.sh) that the main script sources and calls as modular functions",
        "Tests Are the Specification — write a BATS (Bash Automated Testing System) test suite with fixtures for each CSV format, valid/invalid emails, and mock HTTP responses to validate the script's behavior"
      ],
      correctOption: 1,
      explanation: "Axiom III (Programs Over Scripts) states that production work requires proper programs with the full discipline stack: types (pyright), linting (ruff), testing (pytest), dependency management (uv), and CI integration. A 200-line bash script doing CSV parsing, email validation, database connections, and HTTP requests is well past the complexity threshold — it needs type safety for data structures, proper error handling, testable functions, and CI to catch regressions. Option A improves the orchestration layer but the fundamental problem is that complex computation (CSV parsing, email regex, retry logic) shouldn't live in bash regardless of how cleanly it's piped. Option C splits the bash into smaller files but smaller bash scripts still lack types, still can't be statically analyzed, and still resist testability. Option D shows initiative (BATS is a real framework) but testing bash at this complexity is fragile — mocking HTTP and database connections in shell is orders of magnitude harder than in Python with pytest fixtures.",
      source: "Lesson 03: Programs Over Scripts"
    },
    {
      question: "James asks Emma: 'Why do I need uv, pyright, ruff, AND pytest for my order system? Can't I just write Python and run it?' What is the best response based on Axiom III?",
      options: [
        "Each tool catches a different error category: uv prevents environment drift, pyright catches type errors statically, ruff enforces style, and pytest verifies behavior — removing any layer leaves a gap",
        "Start with pytest since it catches the highest-impact bugs (wrong behavior), then add pyright and ruff incrementally once the test suite is stable — uv can wait until the team grows beyond one developer",
        "Focus on pyright and Pydantic together since static type analysis combined with runtime validation at API boundaries covers both development-time and production-time errors comprehensively",
        "For a small order system with one developer, the full stack adds overhead that slows iteration — start with just Python and ruff for formatting, then add the other tools when complexity justifies them"
      ],
      correctOption: 0,
      explanation: "Axiom III defines the Python discipline stack as a layered defense system where each tool serves a distinct purpose: uv ensures reproducible environments (no 'works on my machine'), pyright catches type errors at analysis time (wrong argument types, missing attributes), ruff enforces consistent style (readability, common mistakes), and pytest verifies behavior (correct outputs for given inputs). Removing any layer leaves a gap — without types, you get runtime AttributeError; without tests, you get undetected logic bugs; without dependency management, you get environment drift. Option B sounds pragmatic but 'incrementally adding later' rarely happens in practice — by the time complexity demands pyright, the codebase has accumulated type errors that are painful to retrofit. Option C covers two layers well but misses dependency management (environment drift) and testing (behavioral correctness). Option D's 'add tools when complexity justifies them' is the Prototype Trap from Axiom III — complexity arrives before the tools are in place.",
      source: "Lesson 03: Programs Over Scripts"
    },
    {
      question: "James builds an OrderManager class that handles: database connections, input validation, discount logic, shipping calculation, email notifications, and error reporting. When he needs to change the shipping API provider, he must modify and retest the entire class. What axiom addresses this?",
      options: [
        "Types Are Guardrails — define a ShippingProvider protocol with type annotations so that any new provider implements the same interface, allowing James to swap implementations without touching OrderManager's internals",
        "Tests Are the Specification — write focused TDG tests for each responsibility (test_validate_order, test_calculate_shipping, test_send_notification) so changes to shipping logic are covered by their own isolated test suite",
        "Composition Over Monoliths — decompose the class into focused units (Validator, OrderRepository, ShippingCalculator, Notifier) injected through the constructor",
        "Shell as Orchestrator — split each responsibility into its own Python script (validate.py, ship.py, notify.py) coordinated by a shell pipeline that passes order data between them via JSON on stdin/stdout"
      ],
      correctOption: 2,
      explanation: "Axiom IV (Composition Over Monoliths) prescribes building from composable, focused units rather than monolithic blocks. James's OrderManager class violates this by combining six unrelated responsibilities into one unit. Following the Unix philosophy and dependency injection, each concern should be a separate component injected through the constructor, so each can be modified, tested, and replaced independently. Option A is a useful technique (protocols enable swappable implementations) but types alone don't decompose the monolith — the class still has six responsibilities even with better type annotations. Option B improves test granularity but the coupling remains in the implementation — tests organized by concern still exercise a single tightly-coupled class. Option D applies shell orchestration to what is a program-level architecture problem — splitting into scripts loses type safety and makes the system harder to test as an integrated unit.",
      source: "Lesson 04: Composition Over Monoliths"
    },
    {
      question: "James's team debates whether to build their order system as one FastAPI application with all endpoints or as multiple microservices. Following Axiom IV, which approach is correct?",
      options: [
        "Use microservices from the start — separate order-service, shipping-service, and notification-service communicate via message queues, ensuring each domain can be deployed and scaled independently",
        "It depends primarily on the test architecture — if each module has its own comprehensive test suite with mocked dependencies, either monolith or microservices will be equally maintainable long-term",
        "Use a modular monolith with separate Python packages per domain (orders/, shipping/, notifications/) but deploy as a single FastAPI application, since network boundaries between services add latency and operational complexity",
        "Start with a well-structured monolith using composable internal modules (separate routers, services, repositories) connected through dependency injection, then extract services only when specific boundaries prove necessary"
      ],
      correctOption: 3,
      explanation: "Axiom IV (Composition Over Monoliths) doesn't mean 'always use microservices' — it means build from composable units with clear interfaces. A well-structured monolith with internal modules (separate routers, services, repositories) IS composition. The key is focused interfaces and dependency injection, not deployment boundaries. Extract to separate services only when you have clear evidence: different scaling needs, different team ownership, or different deployment cadences. Option A sounds disciplined but introduces distributed system complexity (network failures, message serialization, deployment coordination) before the team has proven they need independent scaling — premature decomposition is as harmful as no decomposition. Option B correctly notes that tests matter but test architecture alone doesn't determine whether monolith or microservices is appropriate — the architectural concern is about coupling and change boundaries. Option C is close and reasonable but is too absolute in the other direction — it rules out ever extracting services, while the axiom says 'extract when boundaries prove necessary.'",
      source: "Lesson 04: Composition Over Monoliths"
    },
    {
      question: "James writes `def process_order(data)` that accepts any input — dictionaries, lists, strings, None — and uses isinstance() checks throughout to handle each case. The function frequently crashes in production when the shipping API returns an unexpected format. Which axiom provides the solution?",
      options: [
        "Types Are Guardrails — define `def process_order(order: OrderRequest) -> OrderResult` so pyright catches invalid inputs at analysis time, replacing runtime isinstance() checks with compile-time guarantees",
        "Tests Are the Specification — write TDG tests like `test_process_order_rejects_invalid_dict()` and `test_process_order_handles_api_timeout()` covering each input type the shipping API might return",
        "Observability Extends Verification — add structlog fields like `log.info('processing', input_type=type(data).__name__, source='shipping_api')` so crashes show exactly what unexpected format arrived",
        "Verification is a Pipeline — add a pyright strict-mode check and a custom ruff rule to the CI pipeline that flags any function accepting untyped `data` parameters as a code smell"
      ],
      correctOption: 0,
      explanation: "Axiom V (Types Are Guardrails) states that type systems prevent errors at compile/analysis time rather than runtime. Instead of accepting 'any' and checking types dynamically, James should declare explicit types: `def process_order(order: OrderRequest) -> OrderResult`. With the three-layer type stack (hints for documentation, Pyright for static analysis, Pydantic for runtime validation at API boundaries), invalid inputs are caught before they cause production crashes. The isinstance() pattern is a symptom of missing type discipline. Option B catches specific known cases but can't cover every possible unexpected format — the shipping API might return something no test anticipated. Option C provides excellent post-crash diagnostics (you'll know exactly what broke) but doesn't prevent the crash — it's treating symptoms rather than the disease. Option D is partially correct (pyright in CI is good practice) but flags the symptom (untyped parameters) rather than solving the root cause — the function needs to be redesigned with proper types, not just flagged by a linter.",
      source: "Lesson 05: Types Are Guardrails"
    },
    {
      question: "James's team uses Pydantic models for their order API request/response types but does not run Pyright in their CI pipeline. They catch some type errors from Pydantic validation at runtime but keep finding type mismatches in error handlers and rarely-executed code paths. What layer of the type stack are they missing?",
      options: [
        "They need stricter Pydantic validators with custom field validators, constrained types (conint, constr), and model validators that enforce business rules like 'discount percentage must be between 0 and 100'",
        "They should replace Pydantic with Python dataclasses combined with beartype for runtime type checking, which provides lighter-weight validation with less overhead than Pydantic's model initialization",
        "They're missing the static analysis layer (Pyright in CI) which catches type mismatches across all code paths — including error handlers and untested branches — without executing the code",
        "They need to add targeted unit tests for each error handler and rare code path using pytest parametrize to systematically cover the type combinations that Pydantic doesn't validate at the boundary"
      ],
      correctOption: 2,
      explanation: "Axiom V defines a three-layer type stack: type hints (documentation), Pyright (static analysis), and Pydantic (runtime validation). Pydantic validates data at boundaries (API requests, external input) but only when that code path executes. Pyright analyzes ALL code paths statically — it finds type mismatches in error handlers, rare branches, and untested paths without running the code. The team has layer 1 (hints via Pydantic models) and layer 3 (runtime validation) but is missing layer 2 (static analysis). Adding Pyright to CI would catch the type errors in rare paths that Pydantic never sees because those paths haven't been triggered yet. Option A only covers runtime boundaries. Option B changes the tool but doesn't add static analysis. Option D helps but can't cover every path the way static analysis can.",
      source: "Lesson 05: Types Are Guardrails"
    },
    {
      question: "James stores his order records as JSON files in a directory — one file per order, with fields like status, customer_id, shipping_address, and total. When Emma asks him to find 'all orders over $500 shipped to the UK that are still pending,' he realizes he must read every file and filter in Python. What axiom suggests a better approach?",
      options: [
        "Knowledge is Markdown — convert the JSON files into structured markdown tables with YAML frontmatter for each order, enabling grep-based queries and version-controlled history through git log",
        "Shell as Orchestrator — build a query pipeline using `find . -name '*.json' | xargs jq 'select(.total > 500 and .country == \"UK\" and .status == \"pending\")'` to filter orders without writing Python code",
        "Programs Over Scripts — write a proper Python CLI tool with click and type hints that loads all JSON files into Pydantic models, indexes them in memory, and provides a typed query interface",
        "Data is Relational — structured data with defined fields and query patterns belongs in a relational database (even SQLite) where SQL handles filtering, joining, and indexing natively"
      ],
      correctOption: 3,
      explanation: "Axiom VI (Data is Relational) states that SQL is the default for structured data. James's order records have defined fields, relationships (customer_id references a customers table), and query patterns (filter by total, country, status). A relational database handles this naturally: `SELECT * FROM orders WHERE total > 500 AND country = 'UK' AND status = 'pending'`. With JSON files, every query requires reading all files, parsing JSON, and filtering in application code — no indexes, no joins, no query optimization. Even SQLite provides this capability with zero server setup. Option A converts to markdown but markdown tables are not queryable — grep-based filtering is fragile and can't handle numeric comparisons like 'total > 500.' Option B is a clever shell pipeline that works for this specific query, but each new question requires a new jq expression, there are no indexes for performance, and complex joins (orders + customers) become impractical. Option C builds a proper Python tool but reinvents database functionality — in-memory indexing, query interfaces, and data loading are exactly what SQLite already provides.",
      source: "Lesson 06: Data is Relational"
    },
    {
      question: "James's order management system runs on a single server with fewer than 10,000 orders and no concurrent write requirements. His team debates between SQLite and PostgreSQL. Which does Axiom VI recommend?",
      options: [
        "PostgreSQL — it supports JSONB columns for nested shipping addresses, full-text search for order descriptions, and connection pooling that will be needed when the system scales beyond a single server",
        "SQLite — a file-based relational database requiring zero infrastructure (no server process, no connection pooling, no separate deployment), perfect for single-server applications with modest data volumes and no concurrent write pressure",
        "MongoDB — document databases map naturally to order records since each order contains nested objects (shipping address, line items, payment details) that would require multiple joined tables in SQL",
        "DuckDB — an embedded analytical database optimized for the kind of aggregate queries (total revenue, average order size, top customers) that an order management system needs for reporting"
      ],
      correctOption: 1,
      explanation: "Axiom VI provides clear guidance on SQLite vs PostgreSQL: SQLite is ideal for single-server applications with modest data volumes and no concurrent write pressure. It requires zero infrastructure (no database server, no connection management, no separate deployment) — it's just a file. PostgreSQL becomes necessary when you need concurrent writes from multiple processes, advanced features (JSONB, full-text search), or when data exceeds what a single file handles efficiently. For James's fewer than 10,000 orders on a single server, SQLite is the right choice — simpler deployment, simpler backup (copy the file), and zero operational overhead. Option A lists real PostgreSQL advantages but they're solving problems James doesn't have yet — JSONB and full-text search are premature for 10K orders on one server. Option C is tempting for nested data but violates the relational axiom — and SQLite/PostgreSQL both handle nested structures through proper table design or JSON columns. Option D is designed for analytical workloads (OLAP) not transactional order processing (OLTP) — it excels at aggregates but isn't optimized for the individual inserts and updates an order system performs.",
      source: "Lesson 06: Data is Relational"
    },
    {
      question: "James asks Claude Code to 'implement a discount calculator for the order system.' The AI generates code, but in production a customer receives a $12,000 discount on a $200 order because the percentage was applied as a multiplier instead of a fraction. How should James have approached this using Axiom VII?",
      options: [
        "Ask the AI to generate both the implementation and a comprehensive test suite simultaneously, so `test_discount_percentage()` and `calculate_discount()` are created together with consistent assumptions about how percentages work",
        "Write a detailed natural language specification: 'A 15% discount on a $200 order means $30 off, not $200 * 15 = $3000. Discounts must never exceed the order total. Round to two decimal places.' — then give this spec to the AI",
        "Write failing tests first — like `test_bulk_discount_never_exceeds_order_total()` and `test_fifteen_percent_of_200_equals_30()` — then give the AI those tests as the specification to implement against",
        "Review the AI's generated code with a checklist: verify percentage operations use division by 100, add assert statements for discount < order_total, and manually test with boundary values like 0%, 50%, and 100% discounts"
      ],
      correctOption: 2,
      explanation: "Axiom VII (Tests Are the Specification) prescribes Test-Driven Generation (TDG): write tests FIRST that define correct behavior, then prompt AI to generate implementation that passes those tests. A test like `test_fifteen_percent_of_200_equals_30()` would have caught the $12,000 bug before any customer saw it — the test defines the boundary, and any implementation that violates it fails immediately. Option A creates circular validation — when the AI generates both code and tests simultaneously, it may encode the same misunderstanding in both, so the tests pass but the behavior is wrong (the Circular Testing Trap). Option B is more specific than 'implement a discount calculator' but natural language is still interpretable — the AI might follow the examples literally while handling unlisted edge cases incorrectly. Option D catches problems but relies on manual diligence — the reviewer must understand the bug pattern to spot it, and manual checks don't persist as automated regression protection.",
      source: "Lesson 07: Tests Are the Specification"
    },
    {
      question: "James's test suite shows 53 passing tests — all green. He feels confident and deploys his order system. But in production, the shipping calculator fails for orders over $10,000 because no test ever checked that boundary. What named trap from Axiom VII did he fall into?",
      options: [
        "The Green Bar Illusion — 53 passing tests create false confidence when the test suite itself has coverage gaps, like the missing $10,000 boundary that no test ever checked despite the green bar suggesting everything works",
        "The Shallow Pipeline — his verification pyramid was incomplete because it included unit tests but lacked integration tests that would exercise the shipping calculator with realistic order values",
        "The Circular Testing Trap — the AI generated both the implementation and the tests, so the tests verified the code's assumptions rather than independently defining what correct behavior should be",
        "The Prototype Trap — the shipping calculator was built as a quick prototype with hardcoded assumptions about order sizes, then deployed to production without being rewritten as a proper program"
      ],
      correctOption: 0,
      explanation: "The Green Bar Illusion is the belief that 'all tests pass' means 'the system is correct.' It confuses test count with behavioral coverage. James's 53 tests verified 53 specific scenarios — but none tested orders above $10,000, so the boundary failure was invisible. The fix is to think about what the tests DON'T cover: edge cases, boundary values, error paths, and load conditions. A green bar means 'all specified behaviors work' — not 'all possible behaviors work.' Option B identifies a real concern (integration tests might have caught this) but the root cause isn't the pipeline's depth — it's that the specification itself (the tests) was incomplete, which is a testing problem, not a CI structure problem. Option C describes a real trap from Axiom VII but doesn't match this scenario — James's tests weren't AI-generated alongside the code, they simply didn't cover the boundary. Option D describes a different trap (Axiom III) about prototypes graduating to production — the issue here is test coverage, not code maturity.",
      source: "Lesson 07: Tests Are the Specification"
    },
    {
      question: "James fixes the $12,000 discount bug, updates the FREE_SHIPPING_THRESHOLD constant, and refactors three TDG test files — all in a single commit with the message 'fix: various updates.' During a post-mortem the next week, his team needs to find exactly when the shipping threshold changed. They cannot. Which axiom did he violate?",
      options: [
        "Knowledge is Markdown — he should have written a CHANGELOG.md entry for each change with the date, reason, and impact assessment, so the team can search the changelog independently of git history",
        "Version Control is Memory — each change should be its own atomic commit with a conventional message explaining the 'why', forming searchable project memory",
        "Observability Extends Verification — he should have added a structured log entry that records configuration changes at startup, like `log.info('config_loaded', free_shipping_threshold=75, previous=50)`, so runtime changes are traceable",
        "Tests Are the Specification — each change should have had its own test commit first (failing test for the bug, test for the new threshold, tests for the refactored modules) before the implementation commits"
      ],
      correctOption: 1,
      explanation: "Axiom VIII (Version Control is Memory) requires atomic commits — one logical change per commit — with conventional messages that explain reasoning. James mixed three unrelated changes into one commit, so `git log --grep='shipping'` finds nothing, and reverting the discount fix also reverts the threshold change. Proper practice: three separate commits — `fix(orders): cap discount to never exceed order total`, `feat(shipping): raise FREE_SHIPPING_THRESHOLD to $75`, `refactor(tests): reorganize TDG fixtures for discount module`. Option A is useful supplementary documentation but a changelog is a manual duplicate of what git history should provide natively — if commits are atomic and well-messaged, the changelog writes itself via `git log`. Option C provides valuable runtime observability but tracks when the application loads config, not when the developer changed the code — different questions answered by different systems. Option D describes a TDG-aligned workflow (test-first commits) but the fundamental problem is mixing unrelated changes in one commit, not the absence of test-first ordering.",
      source: "Lesson 08: Version Control is Memory"
    },
    {
      question: "James accidentally commits his database password in a configuration file. He immediately makes another commit removing the password and thinks the problem is solved. What does Axiom VIII's 'Permanent Record' trap warn about this situation?",
      options: [
        "He should have used `git stash` to hold the configuration file temporarily while working on it, then added it to .gitignore before unstashing — preventing the password from ever entering the commit history",
        "He needs to add the configuration file to .gitignore and run `git rm --cached config.py` to stop tracking it, then use environment variables loaded from a .env file for all credentials going forward",
        "He should have worked on a feature branch so the password commit would be isolated from main — then force-pushed the branch with the sensitive commit removed before merging the clean version",
        "Git never forgets — the password still exists in the commit history and anyone with repo access can find it via `git show <previous-commit>`, even though it was removed"
      ],
      correctOption: 3,
      explanation: "The Permanent Record is a named trap from Axiom VIII: git's greatest strength (it remembers everything) becomes a liability when secrets are committed. Deleting the password in a new commit only removes it from the current state — `git show <previous-commit>` reveals it instantly. The damage requires rotating the credential immediately and using tools like git-filter-branch or BFG Repo Cleaner to rewrite history (a destructive, complex operation). Prevention is the cure: use .env files (gitignored), environment variables, or secret managers. Option A describes good preventive practice (stash + gitignore workflow) but the question asks about what's wrong NOW — the password is already committed and stashing is for temporary work context, not a security mechanism. Option B fixes the future (stop tracking the file, use env vars) but doesn't address the existing exposure — the password is already in history even after git rm --cached. Option C isolates the commit to a branch but force-pushing a branch doesn't remove the commit from any developer who already fetched it — and if the branch was pushed to a remote before cleanup, the secret was already exposed.",
      source: "Lesson 08: Version Control is Memory"
    },
    {
      question: "James pushes his first pull request for the order management system. The CI pipeline rejects it with four failures: ruff finds a formatting error, pyright flags a type mismatch in `calculate_shipping()`, two TDG tests fail, and a dependency vulnerability is detected. Frustrated, he considers adding `--no-verify` to skip the checks. Why is this pipeline actually helping him, according to Axiom IX?",
      options: [
        "The pipeline caught four different error categories (formatting, types, logic, security) — each level of the verification pyramid catches errors the others miss",
        "The pipeline is providing signal overload — four simultaneous failures on a first PR indicates the checks should be introduced gradually, starting with tests and adding stricter checks as the codebase matures",
        "He should prioritize the two test failures and the type mismatch since they indicate behavioral and structural bugs, while formatting and dependency checks can be addressed in a follow-up PR to keep the review focused",
        "The dependency vulnerability is the most critical failure and should block the merge, while the formatting, type, and test issues should be warnings that James can address after the initial deployment"
      ],
      correctOption: 0,
      explanation: "Axiom IX (Verification is a Pipeline) states: 'If it's not in CI, it's not enforced.' The pipeline caught errors across four levels of the verification pyramid: formatting (fast, cheap), types (structural correctness), tests (behavioral correctness), and security (dependency safety). Each level catches errors the others miss — ruff won't catch logic bugs, pyright won't catch vulnerable dependencies, tests won't catch formatting drift. Skipping with --no-verify defeats the entire system. The frustration James feels is the pipeline *working* — it costs minutes now to save hours of production debugging later. Option B sounds reasonable but 'introducing checks gradually' means the codebase accumulates the exact problems those checks prevent — by the time you add pyright later, you have hundreds of type errors to fix at once. Option C prioritizes some checks over others, but the axiom's point is that each level catches different errors — formatting consistency matters because inconsistent code is harder to review, and deferred fixes often never happen. Option D inverts the priority — all four failures indicate real issues, and letting any category through creates a precedent for selective bypassing.",
      source: "Lesson 09: Verification is a Pipeline"
    },
    {
      question: "A team's CI pipeline runs only unit tests and linting. Their code always passes CI, but in production they repeatedly discover issues: a database migration was never applied, an environment variable was missing, and the API fails under concurrent requests. What named anti-pattern from Axiom IX describes their pipeline?",
      options: [
        "The Green Bar Illusion — their unit tests pass with mocked dependencies, creating false confidence that the real database, environment, and concurrent access will behave the same way as the test doubles",
        "The Shallow Pipeline — their verification pyramid covers the lower levels (format, lint, unit tests) but skips integration tests, E2E tests, and environment validation that catch deployment-level failures",
        "The Prototype Trap — their CI pipeline was set up quickly during the project's early days and never evolved to match the system's growing complexity, deployment requirements, and production environment",
        "The God Object — their single CI configuration file tries to handle all verification in one monolithic workflow instead of composing specialized pipeline stages that each verify a different architectural layer"
      ],
      correctOption: 1,
      explanation: "The Shallow Pipeline is a named trap from Axiom IX: a CI pipeline that only runs fast, cheap checks (linting, unit tests) while skipping the higher levels of the verification pyramid (integration tests, E2E tests, deployment validation). Unit tests verify isolated function behavior but cannot catch missing database migrations, environment configuration errors, or concurrency failures — these require higher-level verification. The six-level pyramid runs from format (seconds) through lint, types, unit tests, integration tests, to E2E tests (minutes) — each level catches errors invisible to the levels below. Option A is tempting because it sounds like the Green Bar Illusion (Axiom VII). The key distinction: the Green Bar Illusion is about *depth* within the testing layer (tests pass but miss edge cases), while the Shallow Pipeline is about *breadth* across verification layers (entire categories of checks are absent). Here the problem is that entire verification layers (integration, E2E, environment) are missing from the pipeline structure. Option C describes a real phenomenon (CI pipelines that don't evolve) but the Prototype Trap is an Axiom III concept about scripts graduating to programs, not about pipeline maturity. Option D applies composition thinking to CI, which is reasonable architecturally, but the problem isn't pipeline organization — it's missing verification levels.",
      source: "Lesson 09: Verification is a Pipeline"
    },
    {
      question: "James's CI pipeline is green — all 53 TDG tests pass, types check clean, linting is spotless. He deploys his order management system. At 2:47 AM, international shipping rates fail under production load. He checks the logs and finds only `print('Processing order...')` repeated thousands of times — no timestamps, no order IDs, no error context. Which observability pillar would have detected this problem earliest?",
      options: [
        "Logs — if James had used structlog with structured fields like `log.error('shipping_failed', order_id=order.id, carrier='dhl', error=str(e))`, he would see exactly which orders failed, which carrier timed out, and the specific error for each failure",
        "He needs better CI coverage — adding load tests with locust or k6 that simulate 500 concurrent international orders would have caught the shipping rate failure during the verification pipeline before deployment",
        "Metrics — a Prometheus counter like `shipping_errors_total{carrier='dhl'}` with an alert threshold would have fired the moment failure rates spiked above baseline",
        "Traces — OpenTelemetry spans across `process_order → calculate_shipping → call_carrier_api` would show exactly where each request stalled and reveal that the DHL API was timing out under concurrent load"
      ],
      correctOption: 2,
      explanation: "Axiom X (Observability Extends Verification) defines three pillars, each answering different questions. Metrics answer 'how much?' and 'how fast?' — a Prometheus counter tracking shipping errors with an alert threshold would have fired at 2:30 AM, seventeen minutes before the customer service ticket. Logs would tell James *what* failed (which orders, which errors), and traces would show *where* time was spent (the shipping API timing out under concurrent load). But metrics provide the earliest automated detection — they aggregate across all requests and trigger alerts on deviation from baselines without anyone watching. Option A provides excellent diagnostic detail (you'd know exactly what broke) but structured logs still require someone to read them — they don't trigger automated alerts the way metrics do. Option B is valid defensive engineering (load testing catches some production-like failures) but CI cannot simulate every production condition — observability catches what testing misses at runtime. Option D pinpoints the root cause beautifully (you'd see the DHL timeout) but tracing is diagnostic, not alerting — it helps after you know something is wrong, not before.",
      source: "Lesson 10: Observability Extends Verification"
    },
    {
      question: "After the 2:47 AM incident, James adds DEBUG-level logging to every function in his order system. Within a day, logs generate 2GB per hour — storage costs spike and when a new error occurs, it is buried under millions of irrelevant entries. What named trap from Axiom X did he fall into?",
      options: [
        "The Shallow Pipeline — his observability stack has logging but lacks metrics and tracing, so he's compensating with excessive log volume instead of using the right pillar for each question (how much, what happened, where)",
        "The Permanent Record — his logs capture sensitive customer data (email addresses, shipping addresses, order amounts) at DEBUG level, creating compliance and privacy risks alongside the storage cost problem",
        "The Green Bar Illusion — his 2GB of hourly logs create the appearance of comprehensive observability, but the sheer volume means critical errors pass unnoticed, giving false confidence in system health",
        "The Log Avalanche — logging everything at DEBUG level drowns signal in noise, making observability worse because important errors are buried under millions of irrelevant entries"
      ],
      correctOption: 3,
      explanation: "The Log Avalanche is a named trap from Axiom X: the overcorrection of adding maximum logging everywhere after experiencing an observability gap. James went from zero visibility (`print('Processing order...')`) to maximum noise (DEBUG on everything) — neither extreme works. Effective observability requires the right data at the right level: DEBUG for development only (off in production), INFO for normal operations, WARNING for handled anomalies, ERROR for failures requiring attention, CRITICAL for system-level emergencies. As Emma told James: 'If everything is important, nothing is.' Option A makes a valid architectural point (he should add metrics and traces too) but the immediate problem isn't missing pillars — it's that the one pillar he's using (logging) is misconfigured with excessive volume. Option B identifies a real secondary risk of DEBUG logging (sensitive data exposure) but the question focuses on the primary problem — signal drowning in noise, not privacy compliance. Option C sounds plausible but the Green Bar Illusion is specifically about test coverage creating false confidence (Axiom VII) — here the problem isn't false confidence, it's that he literally can't find errors in the noise.",
      source: "Lesson 10: Observability Extends Verification"
    }
  ]}
/>

## Answer Key

| Question | Correct Answer | Axiom Tested |
|----------|---------------|--------------|
| 1 | D | Axiom I: Shell as Orchestrator |
| 2 | B | Axiom I: Shell as Orchestrator |
| 3 | A | Axiom II: Knowledge is Markdown |
| 4 | C | Axiom II: Knowledge is Markdown |
| 5 | B | Axiom III: Programs Over Scripts |
| 6 | A | Axiom III: Programs Over Scripts |
| 7 | C | Axiom IV: Composition Over Monoliths |
| 8 | D | Axiom IV: Composition Over Monoliths |
| 9 | A | Axiom V: Types Are Guardrails |
| 10 | C | Axiom V: Types Are Guardrails |
| 11 | D | Axiom VI: Data is Relational |
| 12 | B | Axiom VI: Data is Relational |
| 13 | C | Axiom VII: Tests Are the Specification |
| 14 | A | Axiom VII: Tests Are the Specification |
| 15 | B | Axiom VIII: Version Control is Memory |
| 16 | D | Axiom VIII: Version Control is Memory |
| 17 | A | Axiom IX: Verification is a Pipeline |
| 18 | B | Axiom IX: Verification is a Pipeline |
| 19 | C | Axiom X: Observability Extends Verification |
| 20 | D | Axiom X: Observability Extends Verification |

## Scoring Guide

| Score | Proficiency Level | Interpretation |
|-------|------------------|----------------|
| 18-20 | B2 (Advanced) | Strong understanding of all ten axioms and their practical application |
| 14-17 | B1 (Intermediate) | Good understanding with some gaps in applying axioms to real scenarios |
| 10-13 | A2 (Elementary) | Basic understanding of axioms but needs more practice with application |
| 0-9 | A1 (Beginner) | Review the lessons and work through the "Try With AI" exercises |

## Next Steps

Based on your performance, focus on the group where you missed the most questions. The ten axioms fall into three groups (the same groups introduced in the chapter overview):

- **Axioms I-IV (Structure)**: If you missed questions 1-8, review shell orchestration (the complexity threshold between shell and program), markdown knowledge (complete reasoning, not just decisions), the Python discipline stack (uv, pyright, ruff, pytest), and composition patterns (composable monolith vs. microservices). These axioms govern how your code is organized.
- **Axioms V-VI (Data)**: If you missed questions 9-12, study the three-layer type stack (hints, Pyright, Pydantic) and relational data modeling (SQLite vs. PostgreSQL). These axioms make sure information stays correct as it moves through your system.
- **Axioms VII-X (Verification)**: If you missed questions 13-20, revisit Test-Driven Generation (the $12,000 discount bug and the Green Bar Illusion), git as memory (atomic commits, the Permanent Record trap), CI/CD pipelines (the verification pyramid and the Shallow Pipeline trap), and observability practices (the three pillars and the Log Avalanche). These axioms create a chain of verification — from writing the first test to monitoring the live system.

Remember: The ten axioms build upon each other — shell orchestrates programs (I, III), programs are composed (IV) with types (V) and relational data (VI), tested via TDG (VII), tracked in git (VIII), verified in CI (IX), and monitored in production (X). Master each group before advancing to the next.
