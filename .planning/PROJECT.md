# Valkyrie Platform

## What This Is

A production-grade autonomous DevOps platform foundation. It features Kubernetes infrastructure, GitOps delivery, comprehensive observability, and AI-driven incident summarization and automated remediation.

## Core Value

An operationally realistic, tightly integrated operational platform. Integration quality beats a disconnected collection of advanced features.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] GitOps deployment pipeline
- [ ] Kubernetes production stack
- [ ] Comprehensive monitoring + tracing
- [ ] Security scanning layer
- [ ] Chaos testing capabilities
- [ ] AI incident summaries
- [ ] Automated remediation
- [ ] Developer portal

### Out of Scope

- Over-engineering microservices early — focus on MVP operational realism.
- Adding 40 tools — focus on tightly integrated foundational stack.
- Building custom Kubernetes operators immediately — use existing stable helm charts and operators.
- Prematurely optimizing AI — start with basic FastAPI + Ollama incident summarization.
- Chasing perfection — the goal is an MVP centerpiece within 14 days.

## Context

- Building a top-tier DevOps portfolio centerpiece.
- Timeframe is a strict 14-day execution plan.
- Every feature built must be:
  - Running in Kubernetes
  - Observable
  - Logged
  - Automated
  - Documented
  - Demoable

## Constraints

- **Tech Stack**: AWS EKS, Terraform, ArgoCD, Prometheus, Grafana, Loki, Tempo, Falco, Trivy, LitmusChaos, FastAPI, Ollama, Backstage. — Locked stack requirements.
- **Integration**: A tightly integrated operational platform beats disconnected features — That's how senior infrastructure teams evaluate engineers.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| No custom K8s operators | Avoid early over-engineering and focus on core integrations | — Pending |
| AI for incident summarization | Demonstrates advanced operational AI use cases, easily demoable | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-05-16 after initialization*
