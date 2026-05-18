# Plan: 08-01 Developer Portal Deployment

## Goal

Deploy Backstage to the cluster and populate its Software Catalog with the Demo Workload components.

## Implementation Steps

### 1. Define the Software Catalog
- Create `catalog-info.yaml` at the root of the repository.
- Define the following Backstage Component kinds:
  - `System`: Valkyrie Platform
  - `Component`: Vote Frontend (type: website)
  - `Component`: Result Frontend (type: website)
  - `Component`: Worker (type: service)
  - `Resource`: Postgres Database (type: database)
  - `Resource`: Redis Queue (type: cache)
- Establish the dependency relationships (e.g., `dependsOn`, `consumes`, `provides`) to generate a comprehensive architecture graph.

### 2. Backstage GitOps Application
- Create `gitops/applications/backstage.yaml`.
- Define an ArgoCD Application targeting the official `backstage` Helm chart from the `backstage` repository.
- Use Helm values to automatically provision the PostgreSQL dependency required by Backstage.

## Verification

1. Push all code to GitHub.
2. Verify ArgoCD deploys the `backstage` application successfully.
3. Wait for the `backstage` pod to become ready (this might take a few minutes as it runs database migrations).
4. Port-forward the Backstage frontend: `kubectl port-forward svc/backstage -n backstage 7007:80`.
5. Open the UI at `http://localhost:7007`.
6. Manually register the `catalog-info.yaml` URL in the Backstage UI (or configure Backstage to auto-discover it if a GitHub token is provided in the future).
7. Verify the Voting App components appear in the catalog and the architecture graph is accurately rendered.
