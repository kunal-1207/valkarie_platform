# Phase 1: Foundation - Context

**Gathered:** 2026-05-16
**Status:** Ready for planning
**Source:** PRD Express Path (from User Request)

<domain>
## Phase Boundary

Phase 1 focuses on building a stable, production-style Kubernetes platform foundation for Valkyrie Platform. The primary goals are operational reliability, clean architecture, reproducible infrastructure, GitOps workflows, observability maturity, and production-grade engineering standards. It is NOT feature complete, but serves as the bedrock for future phases.
</domain>

<decisions>
## Implementation Decisions

### Infrastructure & Orchestration
- Use K3d locally for a lightweight multi-node cluster.
- Enforce namespace isolation, resource quotas, health probes, and RBAC policies.
- Provision infrastructure using Terraform with remote-state-ready structure and environment-based layouts.
- Prefer Helm charts for application deployments.
- NGINX ingress controller must be deployed.

### GitOps & CI/CD
- Use ArgoCD as the deployment controller.
- Git must be the single source of truth (declarative manifests).
- GitHub Actions pipeline should: lint, test, build Docker images, scan with Trivy, push to GHCR, and update manifests.

### Observability
- Monitoring stack MUST include Prometheus, Grafana, and Loki.
- Dashboards should surface CPU, memory, pod health, request latency, error rates, deployment health, and golden signals.

### Repository Architecture
- Use a monorepo structure initially (e.g., `infrastructure/`, `kubernetes/`, `apps/`, `monitoring/`, `docs/`, `scripts/`, `.github/`).

### Documentation
- Every major component requires a README, architecture notes, deployment instructions, and troubleshooting guidance.

### the agent's Discretion
- Specific configurations for K3d nodes, Prometheus scrape targets, Grafana dashboards layout, and the content of the demo microservice application.
- Terraform structure details (module organization).
</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Project Scope
- `.planning/PROJECT.md` — Core value and context
- `.planning/REQUIREMENTS.md` — Phase 1 Requirements mapping
- `.planning/ROADMAP.md` — Phase definitions
</canonical_refs>

<specifics>
## Specific Ideas

- Must deploy a demo microservice application to validate the pipeline and GitOps workflow.
- Platform must survive pod restarts cleanly to demonstrate resilience.
- Avoid premature complexity: Simplicity, Stability, Reproducibility, Maintainability, Observability, and GitOps-first.
</specifics>

<deferred>
## Deferred Ideas

- AI systems, LangGraph, Cortex
- Multi-cloud orchestration, Crossplane, Rancher
- Service mesh, Istio
- Backstage (Portal)
- Chaos engineering (LitmusChaos)
- FinOps (Kubecost)
- Security automation, Runtime threat detection (Falco, Kyverno)
- Kafka/NATS
- Disaster recovery, Multi-cluster federation
</deferred>

---

*Phase: 01-foundation*
*Context gathered: 2026-05-16 via PRD Express Path*
