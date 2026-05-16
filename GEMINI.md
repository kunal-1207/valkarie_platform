<!-- GSD:project-start source:PROJECT.md -->
## Project

**Valkyrie Platform**

Valkyrie Platform is a production-grade autonomous cloud reliability and platform engineering ecosystem designed to simulate real-world enterprise DevOps, SRE, DevSecOps, and AI-driven infrastructure operations. It automates infrastructure provisioning, enables self-service deployments, provides deep observability, and executes self-healing remediation.

**Core Value:** Demonstrate enterprise-scale platform engineering architecture and advanced DevOps/SRE capabilities in a modular, autonomous, and self-remediating cloud-native ecosystem.

### Constraints

- **Architecture**: Must be Kubernetes-native and modular (K3s local, EKS/GKE cloud).
- **Automation**: Must use GitOps workflows (ArgoCD) for CD and CI via GitHub Actions.
- **Security**: Must enforce supply chain security, runtime anomaly detection, and least privilege.
- **Cost**: Local environment using K3s, and optimized cloud scaling based on FinOps principles to manage expenses.
<!-- GSD:project-end -->

<!-- GSD:stack-start source:STACK.md -->
## Technology Stack

Technology stack not yet documented. Will populate after codebase mapping or first phase.
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

Conventions not yet established. Will populate as patterns emerge during development.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

Architecture not yet mapped. Follow existing patterns found in the codebase.
<!-- GSD:architecture-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->



<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
