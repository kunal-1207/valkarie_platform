# Phase 4: Demo Workload

## Context

With our infrastructure, delivery mechanism, and observability tools in place, we need an actual workload running in the cluster to observe. A platform is only as good as the applications it supports. 

To generate realistic metrics and logs, we will deploy the standard Docker "Example Voting App." This architecture perfectly mirrors our requirement of a multi-tier microservice application:
- A Python front-end web app which lets you vote between two options
- A Redis queue which collects new votes
- A .NET worker which consumes votes and stores them
- A Postgres database backed by a Docker volume
- A Node.js web app which shows the results of the voting in real time

## Requirements

- **DEMO-01**: Deploy sample microservice app (frontend/backend, Redis/Postgres)
- **DEMO-02**: Generate real telemetry from the workload

## Success Criteria

1. The Voting App is successfully deployed into the `demo` namespace.
2. Users can cast votes on the `vote` service interface.
3. The `result` service accurately reflects the cast votes (proving the entire Redis -> Worker -> Postgres chain is healthy).
4. The observability stack (Loki, Prometheus) registers logs and resource metrics for these new pods.

## Constraints

- Deployed strictly via ArgoCD GitOps using plain Kubernetes manifests.
