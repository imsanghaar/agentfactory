### Core Concept
CI/CD automates the journey from code commit to production deployment through Continuous Integration (building, testing, packaging) and Continuous Delivery/Deployment (releasing to environments), reducing manual errors and accelerating feedback loops.

### Key Mental Models
- **Continuous Integration**: Automatically build and test code on every commit to catch issues early
- **Continuous Delivery vs Deployment**: Delivery stops at a deployable artifact; Deployment goes all the way to production automatically
- **Pipeline Stages**: Code commit triggers build, test, package, deploy in sequence with quality gates
- **Feedback Loops**: Fast failures (tests, builds) provide immediate developer feedback

### Critical Patterns
- Trigger pipeline on push to main branch or pull request events
- Run unit tests before integration tests before deployment
- Build and tag Docker images with commit SHA for traceability
- Use environment-specific deployment stages (staging, production)

### AI Collaboration Keys
- Ask Claude to explain the difference between CI and CD for your project
- Request pipeline stage recommendations for a FastAPI agent
- Have AI design quality gates appropriate for your deployment risk

### Common Mistakes
- Conflating Continuous Delivery with Continuous Deployment
- Skipping test stages to speed up pipelines (shortcuts cause production issues)
- Not including rollback mechanisms in the deployment stage

### Connections
- **Builds on**: Lesson 0 - Building your GitOps skill
- **Leads to**: Lesson 2 - GitHub Actions Fundamentals
