# Phase 8: Developer Portal (Backstage)

## Context

As a platform scales, discovering services, documentation, and infrastructure health becomes a major bottleneck for developers. The Valkyrie Platform solves this by deploying a centralized Developer Portal using **Backstage** (open-sourced by Spotify).

Backstage acts as a single pane of glass. It uses a "Software Catalog" built from declarative `catalog-info.yaml` files stored alongside the code. In this phase, we will deploy Backstage and register our Phase 4 Demo Workload (The Voting App) so that developers have a centralized UI to understand the architecture, API, and ownership of the microservices.

## Requirements

- **PORTAL-01**: Install Backstage
- **PORTAL-02**: Register Demo workload in software catalog

## Success Criteria

1. Backstage is successfully deployed into the `backstage` namespace using GitOps.
2. A `catalog-info.yaml` file is created at the root of the repository documenting the Voting App architecture.
3. The Backstage UI is accessible and populates its Software Catalog from the repository's `catalog-info.yaml`.

## Constraints

- The Backstage instance should rely on an integrated PostgreSQL database (provisioned via Helm) rather than external cloud databases to keep the MVP self-contained.
