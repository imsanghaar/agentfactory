### Core Concept
Docker Desktop includes a built-in Kubernetes cluster that uses the identical API and architecture as production Kubernetes. It's not a simulator—it runs real Kubernetes on your machine. The only difference is scale: Docker Desktop runs one node locally, production runs many nodes in data centers. Everything you learn here transfers directly to cloud deployment.

### Key Mental Models
- **kubeconfig is your connection string**—Stored at ~/.kube/config, it tells kubectl which cluster to talk to, with what credentials, and which context (namespace/user combo) to use by default
- **kubectl is your CLI to the API**—Every kubectl command goes through the API server. When you run `kubectl get pods`, you're querying the API server for Pod objects
- **Docker Desktop as Kubernetes host**—Docker Desktop runs the Kubernetes control plane and a single worker node inside its VM/container runtime. Everything inside runs as normal Kubernetes—same API, same architecture

### Critical Patterns
- **Enable Kubernetes** in Docker Desktop Settings → Kubernetes → Enable Kubernetes (takes 1-2 minutes on first enable)
- **kubectl config use-context docker-desktop** switches to the Docker Desktop cluster (useful when managing multiple clusters)
- **kubectl get nodes** verifies your cluster is running and shows the single docker-desktop node
- **Docker Desktop provides metrics-server** by default—no addon installation needed

### Common Mistakes
- Forgetting to enable Kubernetes in Docker Desktop Settings before running kubectl commands
- Not understanding that kubeconfig changes are persistent (switching contexts via `kubectl config use-context` changes the default for future commands)
- Expecting multiple nodes—Docker Desktop Kubernetes is single-node by design

### Connections
- **Builds on**: Docker knowledge from Chapter 49 (Docker Desktop is the host environment)
- **Leads to**: All subsequent lessons—Pods, Deployments, Services, Networking all run on your Docker Desktop Kubernetes cluster
