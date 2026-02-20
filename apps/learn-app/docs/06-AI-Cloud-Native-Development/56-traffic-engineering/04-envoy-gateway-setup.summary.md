### Core Concept
Envoy Gateway is a CNCF controller built specifically for Gateway API, using a control plane that translates Gateway resources to xDS configuration and an Infra Manager that deploys Envoy proxy pods as the data plane.

### Key Mental Models
- **Control Plane vs Data Plane**: Controller watches resources and computes config; Envoy proxies handle actual traffic
- **xDS Protocol**: gRPC streaming for dynamic configuration (LDS, RDS, CDS, EDS, SDS) without proxy restarts
- **GatewayClass "eg"**: Automatic class created by Helm chart; referenced by Gateways
- **Gateway Triggers Deployment**: Creating a Gateway causes Infra Manager to deploy Envoy proxy pods

### Critical Patterns
- Install Gateway API CRDs first: `kubectl apply -f standard-install.yaml`
- Install Envoy Gateway via Helm: `helm install eg oci://docker.io/envoyproxy/gateway-helm`
- Verify GatewayClass: `kubectl get gatewayclass eg` should show ACCEPTED: True
- Check Gateway status: PROGRAMMED means data plane deployed successfully

### AI Collaboration Keys
- Explain xDS protocol and how configuration flows from YAML to traffic handling
- Generate EnvoyProxy CRD for production customization (replicas, resources, anti-affinity)
- Troubleshoot Gateway stuck at ACCEPTED but not PROGRAMMED

### Common Mistakes
- Installing Envoy Gateway without Gateway API CRDs first
- Not waiting for controller to be Available before creating Gateway
- Using wrong GatewayClass name (must match controller's advertised name)

### Connections
- **Builds on**: Lesson 3 (Gateway API) specification understanding
- **Leads to**: Lesson 5 (Traffic Routing with HTTPRoute) for defining routing rules
