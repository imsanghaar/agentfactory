### Core Concept
GitHub Actions provides workflow automation through YAML-defined workflows triggered by repository events, using jobs, steps, and actions to build, test, and deploy applications directly from your GitHub repository.

### Key Mental Models
- **Workflow**: YAML file in `.github/workflows/` defining automation triggered by events
- **Jobs and Steps**: Jobs run on runners (VMs), steps execute commands or actions sequentially
- **Events and Triggers**: Push, pull_request, schedule, or manual workflow_dispatch events start workflows
- **Actions Marketplace**: Reusable actions (checkout, setup-python, docker/build-push) encapsulate common tasks

### Critical Patterns
- Define workflow with `on:` triggers and `jobs:` containing steps
- Use `actions/checkout@v4` to clone repository code
- Use `actions/setup-python@v5` to configure Python environment
- Store secrets in GitHub repository settings, access via `${{ secrets.NAME }}`

### AI Collaboration Keys
- Ask Claude to generate a GitHub Actions workflow for your stack
- Request explanations of workflow syntax and available contexts
- Have AI optimize workflow for speed using caching and parallelization

### Common Mistakes
- Hardcoding secrets in workflow files instead of using GitHub Secrets
- Not understanding that jobs run on fresh VMs (no state between jobs without artifacts)
- Using outdated action versions without checking for updates

### Connections
- **Builds on**: Lesson 1 - CI/CD Concepts
- **Leads to**: Lesson 3 - Building Docker Images in CI
