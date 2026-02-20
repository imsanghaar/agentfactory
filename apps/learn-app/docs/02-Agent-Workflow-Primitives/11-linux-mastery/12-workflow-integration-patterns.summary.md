### Core Concept
**The jump from "deploy one agent" to "deploy reliably every time" requires patterns — structured approaches that combine scripting, systemd, security, and monitoring into integrated workflows with zero downtime, automatic rollback, and continuous health verification.** Production deployment is never one skill at a time; it's orchestrating all your skills together.

### Key Mental Models
- **Deployment Pattern as Trade-off Matrix**: Simple restart (seconds of downtime, easy), blue-green (zero downtime, instant rollback, double resources), rolling (zero downtime, gradual rollout, requires multiple instances). Choose based on your constraints, not habit.
- **Blue-Green as the Production Sweet Spot**: Two identical services on different ports — one live, one idle. Deploy to the idle instance, verify health, then switch traffic. If the new version fails, switch back instantly. For single-server agents, this eliminates downtime without multi-instance infrastructure.
- **Monitoring as a Layer, Not an Afterthought**: Log rotation prevents disk exhaustion, disk alerts catch problems before they crash services, and scheduled health checks verify that agents are functional — not just running.
- **Docker Awareness**: systemd-based deployment is sufficient for single-server agents. Containers add value when you need environment reproducibility, dependency isolation across multiple agents, or orchestration across multiple servers.

### Critical Patterns
- **Blue-green deployment flow**: Two service files on different ports. Deploy to the idle instance, verify health, then switch traffic. If the new version fails, switch back instantly.
- **Log rotation with logrotate**: Automatic rotation compresses and archives old logs. Without it, long-running agents fill the disk.
- **Disk alert cron jobs**: Scheduled checks that compare disk usage against a threshold and write alerts when space runs low.
- **Multi-step deployment scripts**: A single script that creates users, installs services, sets permissions, starts agents, and verifies health in one pass.

### Common Mistakes
- **Using simple restart in production**: Stopping and starting introduces downtime. Users and dependent services see failures during the gap. Blue-green eliminates this.
- **Skipping log rotation**: Agents that run for weeks generate gigabytes of logs. Without rotation, the disk fills and the agent crashes with no space to write.
- **Deploying without a rollback plan**: If the new version fails and you've already overwritten the old code, recovery is manual and slow. Blue-green gives instant rollback by switching back to the previous instance.
