# Plan: 05-01 Security Tooling Deployment

## Goal

Deploy Trivy Operator, Falco, and Kyverno via GitOps ArgoCD Applications to secure the cluster.

## Implementation Steps

### 1. Trivy Operator (Image Scanning)
- Create `gitops/applications/trivy-operator.yaml`.
- Define an ArgoCD Application targeting the `trivy-operator` chart from the `aqua` Helm repository.
- Configure namespace isolation (`trivy-system`).

### 2. Falco (Runtime Threat Detection)
- Create `gitops/applications/falco.yaml`.
- Define an ArgoCD Application targeting the `falco` chart from the `falcosecurity` Helm repository.
- Ensure the eBPF driver is used for kernel tracing (best practice for managed clusters like EKS).

### 3. Kyverno (Policy Enforcement)
- Create `gitops/applications/kyverno.yaml`.
- Define an ArgoCD Application targeting the `kyverno` chart from the `kyverno` Helm repository.
- Enable basic admission control features.

## Verification

1. Commit the new application manifests to the Git repository.
2. Wait for the ArgoCD UI (`https://localhost:8080`) to sync the new applications.
3. Validate Trivy: `kubectl get vulnerabilityreports -A` and verify reports exist.
4. Validate Falco: `kubectl logs -l app.kubernetes.io/name=falco -n falco` and ensure it initializes without errors.
5. Validate Kyverno: `kubectl get pods -n kyverno` and verify the admission controller is running.
