# Plan: 09-01 Architecture Documentation

## Goal

Generate comprehensive `ARCHITECTURE.md` documentation summarizing the built platform.

## Implementation Steps

### 1. Create Architecture Markdown
- Create `ARCHITECTURE.md` at the repository root.
- Draft the **System Overview**.

### 2. Design Mermaid Diagrams
- **GitOps Pipeline**: Diagram showing Developer -> GitHub -> ArgoCD -> EKS sync flow.
- **Observability & AI Engine**: Diagram showing Demo App -> Prometheus/Loki -> Alertmanager -> FastAPI -> Ollama.
- **Security & Chaos**: Diagram showing Trivy/Falco/Kyverno boundaries and Litmus ChaosEngine injections.

### 3. Component Catalog
- Document the purpose of each created namespace:
  - `default` / `kube-system`
  - `argocd`
  - `observability`
  - `demo`
  - `trivy-system`, `falco`, `kyverno`
  - `litmus`
  - `ai`
  - `backstage`

## Verification

1. Review the generated `ARCHITECTURE.md` file locally to ensure Markdown formatting is correct.
2. Commit the file and push to GitHub.
3. Visually confirm on GitHub that the Mermaid blocks render correctly into architecture diagrams.
