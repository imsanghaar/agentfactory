### Core Concept
Quality gates are automated checkpoints in CI pipelines that enforce testing thresholds (coverage), code style (linting), and integration tests with service containers, blocking deployment when standards are not met.

### Key Mental Models
- **Quality Gate**: Automated checkpoint that must pass before pipeline continues; if any test fails, coverage drops, or linter finds issues, pipeline stops
- **Coverage Threshold**: Minimum percentage of code executed by tests (80%+); enforced with `--cov-fail-under` flag that fails pipeline if not met
- **Fail-Fast**: Stop immediately when any gate fails; don't waste resources building images if tests reject the code
- **Service Containers**: Temporary databases/services that spin up for tests and tear down automatically, ensuring isolated and repeatable integration tests

### Critical Patterns
- Use `pytest --cov=app --cov-fail-under=80` to enforce coverage thresholds
- Use `ruff check app/ tests/` for linting before tests run
- Use `needs: test` in GitHub Actions to create job dependencies (build only runs if test passes)
- Configure PostgreSQL service container with health checks for integration tests

### AI Collaboration Keys
- Ask Claude to generate a GitHub Actions workflow with quality gates that fail when thresholds aren't met
- Request service container configuration for integration tests requiring PostgreSQL
- Have AI explain the difference between unit tests and integration tests with service containers

### Common Mistakes
- Using `continue-on-error: true` for quality gates (failures should block, not warn)
- Not configuring health checks for service containers (tests may start before database is ready)
- Forgetting to set environment variables for database connection in test steps

### Connections
- **Builds on**: Lesson 3 - Building Docker Images in CI
- **Leads to**: Lesson 5 - GitOps Principles: Git as Truth
