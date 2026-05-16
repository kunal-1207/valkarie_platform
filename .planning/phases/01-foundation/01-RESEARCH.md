# Phase 1: Foundation - Research

## Technical Approach & Architecture

### Kubernetes Distribution (K3d)
K3d is a lightweight wrapper to run K3s inside Docker. It is ideal for local development and CI environments.
- **Node Topology:** 1 Server (control-plane), 2 Agents (worker nodes).
- **Ingress:** Traefik is default in K3s, but the PRD explicitly asks for NGINX ingress controller. We must disable Traefik when creating the K3d cluster.
- **Storage:** Local path provisioner is included by default.
- **Command:** `k3d cluster create valkyrie --servers 1 --agents 2 --api-port 6550 -p "80:80@loadbalancer" -p "443:443@loadbalancer" --k3s-arg "--disable=traefik@server:0"`

### GitOps (ArgoCD)
ArgoCD pulls manifests from Git and applies them to Kubernetes.
- **Deployment Strategy:** Install ArgoCD using its Helm chart or raw manifests.
- **App of Apps Pattern:** We should use the "App of Apps" pattern where one Root ArgoCD Application manages other Applications (e.g., Monitoring, Ingress, Demo App).
- **Namespaces:** `argocd`

### Observability Stack
The kube-prometheus-stack Helm chart is the industry standard for deploying Prometheus, Grafana, and Alertmanager.
- **Loki:** Promtail + Loki should be deployed for log aggregation. The `loki-stack` Helm chart provides both.
- **Grafana Configuration:** Configure Loki and Prometheus as default data sources.
- **Namespaces:** `monitoring`

### Infrastructure as Code (Terraform)
Terraform will manage the local environment bootstrap if possible, but typically Terraform shines in cloud (EKS/GKE). For K3d, we might use a shell script, but the PRD requires "Infrastructure provisioning using Terraform".
- We can use the Terraform `helm` and `kubernetes` providers to deploy ArgoCD and core charts.
- There is also a `k3d` Terraform provider we can use to spin up the cluster entirely declaratively.

### Demo Microservice
A simple Go or Node.js web server that exports Prometheus metrics, handles basic requests, and has health endpoints (`/healthz`).

## Validation Architecture

To pass validation, we need to ensure:
- Kubernetes nodes are ready (`kubectl get nodes`).
- NGINX ingress is routing traffic.
- ArgoCD is healthy and syncing.
- Prometheus targets are up.
- Logs are flowing into Loki.

## Risk & Gotchas
- **Port Conflicts:** Ensure ports 80/443 aren't used by the host OS during K3d cluster creation.
- **Resource Limits:** Docker must be allocated enough RAM/CPU for a multi-node cluster + observability stack.
- **Terraform State:** Local state is fine for now, but module structure must be "remote-state-ready" for later phases.

## Conclusion
The stack will be: K3d (cluster) -> Terraform (provisioning) -> ArgoCD (GitOps) -> Helm (Deployments).
