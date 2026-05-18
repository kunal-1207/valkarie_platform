# Roadmap: Valkyrie Platform

## Overview

This roadmap defines the 14-day execution plan for building the Phase 1 MVP of the Valkyrie Platform, an autonomous DevOps platform foundation. The execution is broken down into 11 distinct phases, moving from foundational infrastructure to application delivery, observability, security, and ultimately an AI-driven incident engine with a developer portal.

## Phases

- [ ] **Phase 1: Infrastructure Bootstrap** - Terraform VPC, EKS cluster, node groups
- [ ] **Phase 2: GitOps Setup** - ArgoCD, Helm, ExternalDNS
- [ ] **Phase 3: Observability Stack** - Prometheus, Grafana, Loki, Tempo
- [ ] **Phase 4: Demo Workload** - Sample microservice with real telemetry
- [ ] **Phase 5: Security Layer** - Trivy, Falco, Kyverno
- [ ] **Phase 6: Chaos Engineering** - LitmusChaos
- [ ] **Phase 7: AI Incident Engine** - FastAPI, Ollama incident summarization
- [ ] **Phase 8: Automated Remediation** - Auto-restart and Slack notification
- [ ] **Phase 9: Developer Portal** - Backstage
- [ ] **Phase 10: Documentation Sprint** - Architecture diagrams, setup guide, workflows
- [ ] **Phase 11: Demo Video** - Polished walkthrough, chaos demo, Grafana dashboards

## Phase Details

### Phase 1: Infrastructure Bootstrap
**Goal**: Provision a functional EKS cluster with Terraform
**Depends on**: Nothing
**Requirements**: [INFRA-01, INFRA-02, INFRA-03, INFRA-04]
**Success Criteria** (what must be TRUE):
  1. `kubectl get nodes` works successfully.
  2. Terraform state is managed remotely.
**Plans**: 1 plan

Plans:
- [ ] 01-01: Setup Terraform and provision EKS

### Phase 2: GitOps Setup
**Goal**: Establish GitOps delivery pipeline
**Depends on**: Phase 1
**Requirements**: [GITOPS-01, GITOPS-02, GITOPS-03]
**Success Criteria** (what must be TRUE):
  1. Committing to GitHub triggers automatic deployment via ArgoCD.
**Plans**: TBD

### Phase 3: Observability Stack
**Goal**: Unified monitoring dashboard for metrics, logs, traces
**Depends on**: Phase 2
**Requirements**: [OBS-01, OBS-02, OBS-03, OBS-04, OBS-05]
**Success Criteria** (what must be TRUE):
  1. Grafana displays metrics, logs, and traces.
**Plans**: TBD

### Phase 4: Demo Workload
**Goal**: Deploy a microservice application to generate real telemetry
**Depends on**: Phase 3
**Requirements**: [DEMO-01, DEMO-02]
**Success Criteria** (what must be TRUE):
  1. The application generates visible telemetry in the observability stack.
**Plans**: TBD

### Phase 5: Security Layer
**Goal**: Runtime threat detection and policy enforcement
**Depends on**: Phase 4
**Requirements**: [SEC-01, SEC-02, SEC-03]
**Success Criteria** (what must be TRUE):
  1. Security policies are enforced.
  2. Image scanning happens automatically.
**Plans**: TBD

### Phase 6: Chaos Engineering
**Goal**: Introduce controlled failures to test resilience
**Depends on**: Phase 5
**Requirements**: [CHAOS-01, CHAOS-02, CHAOS-03, CHAOS-04]
**Success Criteria** (what must be TRUE):
  1. Chaos experiments execute and observability stack captures the impact.
**Plans**: TBD

### Phase 7: AI Incident Engine
**Goal**: Build FastAPI service for AI-driven incident summarization
**Depends on**: Phase 6
**Requirements**: [AI-01, AI-02, AI-03]
**Success Criteria** (what must be TRUE):
  1. Service ingests alerts and outputs JSON summaries with probable causes and recommendations.
**Plans**: TBD

### Phase 8: Automated Remediation
**Goal**: Automatically resolve specific incidents and notify teams
**Depends on**: Phase 7
**Requirements**: [AUTO-01, AUTO-02, AUTO-03]
**Success Criteria** (what must be TRUE):
  1. Failed pods are detected and auto-restarted.
  2. Slack notifications are sent.
**Plans**: TBD

### Phase 9: Developer Portal
**Goal**: Provide a unified developer portal
**Depends on**: Phase 8
**Requirements**: [PORTAL-01, PORTAL-02, PORTAL-03]
**Success Criteria** (what must be TRUE):
  1. Backstage service catalog lists the deployed services.
**Plans**: TBD

### Phase 10: Documentation Sprint
**Goal**: Complete project documentation
**Depends on**: Phase 9
**Requirements**: [DOC-01, DOC-02, DOC-03, DOC-04]
**Success Criteria** (what must be TRUE):
  1. Architecture, setup guide, and incident workflows are fully documented.
**Plans**: TBD

### Phase 11: Demo Video
**Goal**: Record a polished demo video of the platform
**Depends on**: Phase 10
**Requirements**: []
**Success Criteria** (what must be TRUE):
  1. A video demonstrating chaos testing, AI remediation, and observability is produced.
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Infrastructure Bootstrap | 0/1 | Not started | - |
| 2. GitOps Setup | 0/0 | Not started | - |
| 3. Observability Stack | 0/0 | Not started | - |
| 4. Demo Workload | 0/0 | Not started | - |
| 5. Security Layer | 0/0 | Not started | - |
| 6. Chaos Engineering | 0/0 | Not started | - |
| 7. AI Incident Engine | 0/0 | Not started | - |
| 8. Automated Remediation | 0/0 | Not started | - |
| 9. Developer Portal | 0/0 | Not started | - |
| 10. Documentation Sprint | 0/0 | Not started | - |
| 11. Demo Video | 0/0 | Not started | - |
