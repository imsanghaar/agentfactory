### Core Concept
ApplicationSets generate multiple ArgoCD Applications from a single template using generators (List, Cluster, Matrix, Git), enabling multi-environment and multi-cluster deployments without duplicating YAML.

### Key Mental Models
- **List Generator**: Creates one Application per element in a list; explicit environments like dev/staging/prod with different parameters
- **Cluster Generator**: Creates one Application per registered ArgoCD cluster; automatic multi-cluster deployment
- **Matrix Generator**: Combines two generators for Cartesian product; environments x regions = all combinations
- **Git Generator**: Auto-discovers Applications from directory structure in Git repo; add directory, get Application automatically

### Critical Patterns
- Use template placeholders `{{.paramName}}` that generators fill with per-environment values
- List generator elements define parameters: `name`, `environment`, `replicas`, `logLevel`
- Matrix combines lists: 2 environments x 2 regions = 4 Applications automatically generated
- Git generator uses `path.basename` to extract directory name as Application parameter

### AI Collaboration Keys
- Ask Claude to create ApplicationSet with List generator for dev/staging/prod environments
- Request Matrix generator combining environments and regions with different configurations
- Have AI explain when to use Git generator vs List generator for environment management

### Common Mistakes
- Missing parameters in list elements that are referenced in template (sync failures)
- Using Matrix when List would suffice (unnecessary complexity)
- Forgetting CreateNamespace=true when generating namespaces dynamically

### Connections
- **Builds on**: Lesson 9 - Sync Waves and Resource Hooks
- **Leads to**: Lesson 11 - ArgoCD Projects and RBAC
