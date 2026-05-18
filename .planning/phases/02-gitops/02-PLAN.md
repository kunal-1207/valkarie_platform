# Plan: 02-01 GitOps App of Apps

## Goal

Install ArgoCD to the EKS cluster and configure the "App of Apps" GitOps delivery model.

## Implementation Steps

### 1. Define ArgoCD Configuration
- Create `gitops/argocd/values.yaml` to specify Helm configurations for ArgoCD (e.g., enabling insecure mode for the MVP server).

### 2. Establish App of Apps Root
- Create `gitops/applications/app-of-apps.yaml` defining the root ArgoCD Application.
- This Application will target the same GitHub repository and watch the `gitops/applications/` directory for child Applications.

### 3. Add ExternalDNS Application
- Create `gitops/applications/external-dns.yaml`.
- This will declare ExternalDNS via its official Helm chart, delegating its deployment to ArgoCD.

### 4. Create Bootstrap Script
- Create `scripts/bootstrap-gitops.sh`.
- The script will:
  1. Add the ArgoCD Helm repository.
  2. Install ArgoCD via Helm using the custom values file.
  3. Wait for the ArgoCD server pod to become ready.
  4. Apply the `app-of-apps.yaml` manifest via `kubectl`.
  5. Fetch and print the initial admin password.

## Verification

1. Run the `scripts/bootstrap-gitops.sh` script.
2. Confirm the script outputs the initial admin password successfully.
3. Access the ArgoCD UI using `kubectl port-forward svc/argocd-server -n argocd 8080:443`.
4. Log in using `admin` and the provided password.
5. Verify the `app-of-apps` and `external-dns` applications appear and synchronize successfully in the UI.
