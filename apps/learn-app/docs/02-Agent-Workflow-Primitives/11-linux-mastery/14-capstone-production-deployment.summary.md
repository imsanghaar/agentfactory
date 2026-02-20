### Core Concept
**The difference between a hobbyist deployment and a production deployment is not the tools — it's the process: define success criteria before touching a terminal, implement against those criteria, and validate systematically.** This capstone synthesizes every chapter skill into a spec-first workflow: write a deployment specification, implement it step-by-step, validate with layered checks, and package as a repeatable script.

### Key Mental Models
- **Spec-First Methodology**: A deployment specification answers four questions before implementation begins — what am I deploying (service definition), how is it protected (security requirements), how do I know it's healthy (monitoring plan), and how do I prove it works (validation criteria). Every command you run traces back to a requirement.
- **Specification as Checklist**: Every section maps to concrete commands, every requirement is testable, nothing is ad-hoc. This separates specs from wish lists.
- **Layered Validation**: Five layers in sequence — service active, network responding, correct user, logs flowing, resource limits applied. Each catches a different failure class.
- **Idempotent Packaging**: `deploy.sh` runs on any clean server to produce a validated agent. Running twice doesn't break anything.

### Critical Patterns
- **Specification before implementation**: Write DEPLOYMENT-SPEC.md with service definition, security requirements, monitoring plan, and validation criteria. Review the spec before writing any commands.
- **Implementation traces to spec sections**: Each deployment step references which spec section it satisfies. Steps that don't trace to the spec don't belong.
- **Five-layer validation script**: Layer 1 (service active via `systemctl`), Layer 2 (network responding via `curl`), Layer 3 (security — correct user, not root), Layer 4 (monitoring — logs in journalctl), Layer 5 (resources — MemoryMax verified with `systemctl show`).
- **Deployment packaging**: A single bash script with `set -euo pipefail` that creates the user, sets up directories, writes the service file, enables and starts the service, then runs all five validation layers.

### Common Mistakes
- **Implementing before specifying**: Typing commands until the service starts means you can't reproduce the deployment and can't validate it against criteria. Write the spec first.
- **Skipping validation layers**: A service can be "active" in systemctl but return errors on its health endpoint. Running only Layer 1 misses functional failures caught by Layers 2-5.
- **Non-idempotent scripts**: A deploy script that fails on a second run because the user already exists or the directory is already present. Check for existing state before creating resources.
