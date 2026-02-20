### Core Concept
Containers solve the "works on my machine" problem by packaging applications with their dependencies into portable, isolated units that share the host kernel, making them faster and lighter than VMs.

### Key Mental Models
- **Containers vs VMs**: Containers share the host kernel (lightweight, fast), VMs include full OS (heavy, slow)
- **Docker Architecture Stack**: Docker Desktop > Linux VM > Docker Engine > containerd > Containers
- **Images vs Containers**: Images are blueprints (class definition), containers are running instances (objects)
- **Kernel Sharing**: Containers are isolated processes, not full operating systems

### Critical Patterns
- Verify installation with `docker version` (must show both Client and Server)
- Run `docker run hello-world` to validate complete workflow
- Configure Docker Desktop resources for AI workloads (4+ CPUs, 8+ GB RAM)
- Use Hypervisor (macOS) or Hyper-V/WSL2 (Windows) for container runtime

### AI Collaboration Keys
- Ask AI to explain architectural layers and when you'd interact with each
- Use AI to refine mental models and challenge misconceptions
- Collaborate on resource planning for your specific AI workload

### Common Mistakes
- Not checking that Server section appears in `docker version`
- Forgetting to add user to docker group on Linux
- Using insufficient resources for AI workloads (models need 4GB+ RAM)

### Connections
- **Builds on**: Lesson 0 (your docker-deployment skill needs verification capabilities)
- **Leads to**: Lesson 2 (Container Fundamentals) for deeper image/container understanding
