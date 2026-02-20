### Core Concept
Progressive delivery deploys new versions safely through canary (gradual traffic shift with real-traffic validation) or blue-green (instant switch after pre-flight testing), using Argo Rollouts to automate traffic shifting and metric-based promotion/rollback.

### Key Mental Models
- **Canary Deployment**: Gradually shift traffic (20% -> 50% -> 100%) while monitoring metrics; real traffic validates new version before full promotion
- **Blue-Green Deployment**: Run both versions fully, switch all traffic instantly after synthetic tests pass; instant rollback by switching back
- **AI Agent Risk**: Behavior changes are subtle and require real traffic to detect; all-or-nothing deployments miss subtle failures until all users affected
- **Argo Rollouts**: Kubernetes controller using Rollout CRD to automate canary/blue-green with analysis templates for metric-based decisions

### Critical Patterns
- Rollout CRD with `strategy.canary.steps`: setWeight for traffic percentage, pause for observation windows
- Analysis template with metrics query and successCriteria (e.g., error_rate &lt; 1%)
- Blue-green uses activeService and previewService for traffic routing with prePromotionAnalysis
- ArgoCD deploys Rollout CRD; Argo Rollouts controller manages progressive delivery

### AI Collaboration Keys
- Ask Claude to compare canary vs blue-green for stateless AI agent deployments
- Request Rollout manifest with canary steps and error rate analysis
- Have AI explain why progressive delivery is critical for detecting subtle agent behavior changes

### Common Mistakes
- Using standard Deployment instead of Rollout CRD (loses progressive delivery benefits)
- Not configuring analysis metrics (no automated rollback on failures)
- Choosing blue-green for services where real-traffic validation is needed (synthetic tests miss behavior issues)

### Connections
- **Builds on**: Lesson 12 - Health Status and Notifications
- **Leads to**: Lesson 14 - Secrets Management for GitOps
