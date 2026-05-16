---
wave: 1
depends_on: []
files_modified:
  - "infrastructure/main.tf"
  - "infrastructure/variables.tf"
  - "infrastructure/outputs.tf"
  - "kubernetes/argocd/install.yaml"
  - "kubernetes/ingress/nginx-ingress.yaml"
  - "kubernetes/monitoring/kube-prometheus-stack.yaml"
  - "kubernetes/monitoring/loki-stack.yaml"
  - "apps/demo-app/deployment.yaml"
  - "apps/demo-app/service.yaml"
  - ".github/workflows/ci.yml"
autonomous: true
---

# Phase 1: Foundation Plan

## Objective
Establish the Valkyrie Core Foundation: local K3d cluster, Terraform provisioning, ArgoCD GitOps, observability stack, and CI/CD pipelines.

## Requirements Addressed
- FND-01: Provision local K3s cluster
- FND-02: Establish GitOps Engine with ArgoCD
- FND-03: Configure basic Terraform infrastructure management

## Tasks

```xml
<task>
  <description>Create repository structure</description>
  <read_first>
    - .planning/phases/01-foundation/01-CONTEXT.md
  </read_first>
  <action>
    Create directories: `infrastructure/`, `kubernetes/`, `kubernetes/argocd/`, `kubernetes/ingress/`, `kubernetes/monitoring/`, `apps/demo-app/`, `docs/`, `scripts/`, `.github/workflows/`.
    Create an empty `docs/README.md`.
  </action>
  <acceptance_criteria>
    - Directory `infrastructure` exists
    - Directory `kubernetes/argocd` exists
  </acceptance_criteria>
</task>

<task>
  <description>Provision Kubernetes cluster using Terraform</description>
  <read_first>
    - .planning/phases/01-foundation/01-RESEARCH.md
  </read_first>
  <action>
    Create `infrastructure/main.tf` using the `pvotal-tech/k3d` Terraform provider (or null_resource with k3d CLI).
    Configure a K3d cluster named "valkyrie" with 1 server and 2 agents.
    Disable default Traefik by passing `--disable=traefik@server:0` to k3s.
    Expose ports 80 and 443 on the load balancer.
  </action>
  <acceptance_criteria>
    - `infrastructure/main.tf` contains `resource "k3d_cluster"` or equivalent local-exec
    - `terraform init` and `terraform validate` succeed in `infrastructure/`
  </acceptance_criteria>
</task>

<task>
  <description>Deploy ArgoCD via GitOps</description>
  <read_first>
    - infrastructure/main.tf
  </read_first>
  <action>
    Create `kubernetes/argocd/install.yaml` pulling the official ArgoCD manifests.
    Add a basic `Application` manifest for the "App of Apps" pattern inside `kubernetes/argocd/root-app.yaml` that points to the local `kubernetes/` folder.
  </action>
  <acceptance_criteria>
    - `kubernetes/argocd/install.yaml` exists
    - `kubernetes/argocd/root-app.yaml` points to `kubernetes` folder path
  </acceptance_criteria>
</task>

<task>
  <description>Deploy Ingress Controller</description>
  <read_first>
    - .planning/phases/01-foundation/01-CONTEXT.md
  </read_first>
  <action>
    Create `kubernetes/ingress/nginx-ingress.yaml` referencing the NGINX Ingress Controller Helm chart (using ArgoCD Application or HelmRelease).
  </action>
  <acceptance_criteria>
    - `kubernetes/ingress/nginx-ingress.yaml` contains `chart: ingress-nginx`
  </acceptance_criteria>
</task>

<task>
  <description>Deploy Observability Stack</description>
  <read_first>
    - .planning/phases/01-foundation/01-CONTEXT.md
  </read_first>
  <action>
    Create `kubernetes/monitoring/kube-prometheus-stack.yaml` as an ArgoCD Application to deploy `kube-prometheus-stack`.
    Create `kubernetes/monitoring/loki-stack.yaml` as an ArgoCD Application to deploy `loki-stack` (promtail + loki).
  </action>
  <acceptance_criteria>
    - `kubernetes/monitoring/kube-prometheus-stack.yaml` contains reference to `prometheus-community` repo
    - `kubernetes/monitoring/loki-stack.yaml` contains reference to `grafana` helm repo
  </acceptance_criteria>
</task>

<task>
  <description>Configure CI/CD Pipeline</description>
  <read_first>
    - .planning/phases/01-foundation/01-CONTEXT.md
  </read_first>
  <action>
    Create `.github/workflows/ci.yml`.
    Add steps to: lint, test, build Docker image, scan with `aquasecurity/trivy-action`, and output image digest.
  </action>
  <acceptance_criteria>
    - `.github/workflows/ci.yml` contains `uses: aquasecurity/trivy-action`
  </acceptance_criteria>
</task>

<task>
  <description>Deploy Demo Application</description>
  <read_first>
    - .planning/phases/01-foundation/01-CONTEXT.md
  </read_first>
  <action>
    Create `apps/demo-app/deployment.yaml` and `apps/demo-app/service.yaml` for a simple `nginx` or `httpbin` image.
    Include resources, limits, and a liveness probe.
    Create `kubernetes/apps/demo-app.yaml` as an ArgoCD Application connecting to `apps/demo-app`.
  </action>
  <acceptance_criteria>
    - `apps/demo-app/deployment.yaml` contains `livenessProbe`
  </acceptance_criteria>
</task>
```

## Verification

### Must Haves
- The K3d cluster config must disable Traefik and expose 80/443.
- ArgoCD, Prometheus, Grafana, Loki, and NGINX Ingress must all be defined as Kubernetes manifests.
- Trivy scan must be included in the GitHub Actions workflow.

### Verification Steps
1. Run `terraform validate` in the `infrastructure/` directory to ensure IaC is syntactically valid.
2. Verify that `kubernetes/argocd/install.yaml` exists.
3. Verify that `kubernetes/monitoring/` contains both prometheus and loki definitions.
4. Verify that `.github/workflows/ci.yml` includes Trivy.
