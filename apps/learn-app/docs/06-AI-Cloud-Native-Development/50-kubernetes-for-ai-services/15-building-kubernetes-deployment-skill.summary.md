### Core Concept
Validate skill transferability by applying the Kubernetes skill (built in Lesson 0, refined through Lessons 1-14) to a different application type. A skill that only works for one project is a template—true skills guide decisions across different workloads.

### Key Mental Models
- **Skill vs Template**: Templates work for one project; skills transfer across application types
- **Cross-application testing**: Validates transferability by deploying unfamiliar workloads using only skill guidance
- **Gap identification**: Practical application reveals what the skill doesn't address
- **Iterative refinement**: Skills grow with each application deployed

### Critical Patterns
- Choose application type different from capstone (data job, web service, batch processor, API gateway)
- Work through 5 decision areas using only skill: resources, probes, config, labels, deployment strategy
- Document specific gaps discovered during cross-application testing
- Add missing patterns, edge cases, and application-specific guidance to SKILL.md

### Common Mistakes
- Copying capstone manifests instead of using skill guidance
- Not documenting gaps discovered during testing
- Treating skill as static instead of continuously refined
- Testing only on similar application types (doesn't validate transferability)

### Connections
- **Builds on**: Lesson 0 (skill creation) and Lesson 14 (capstone deployment)
- **Leads to**: Optional lessons 16-22 provide advanced patterns to extend skill further
