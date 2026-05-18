# Phase 2: GitOps Setup

## Context

With the foundational AWS infrastructure and EKS cluster provisioned in Phase 1, we now establish the automated deployment engine. This phase focuses on setting up ArgoCD to realize the "GitOps" operational model. 

We are employing the "App of Apps" pattern. Instead of applying individual manifests manually, we bootstrap ArgoCD into the cluster with a single script. ArgoCD is then configured with a root application that watches a specific Git repository directory (`gitops/applications/`). This root app will automatically deploy all other platform components, including ExternalDNS and future observability or security tools.

## Requirements

- **GITOPS-01**: Install ArgoCD
- **GITOPS-02**: Install Helm and ExternalDNS
- **GITOPS-03**: Push to GitHub must result in automatic deployment

## Success Criteria

1. ArgoCD is running in the EKS cluster and accessible via port-forwarding.
2. The App of Apps is synchronized successfully.
3. ExternalDNS is deployed via ArgoCD and manages Route53/DNS records automatically.
4. Any new application manifest added to the repository is automatically deployed by ArgoCD.

## Constraints

- ArgoCD will be the single source of truth for all Kubernetes configurations moving forward. No manual `kubectl apply` for workloads after this phase.
