# Phase 5: Security Layer

## Context

A production-grade platform requires a robust, defense-in-depth security posture. We have our infrastructure, GitOps engine, observability tools, and a running workload. Now we introduce the Security Layer to protect the cluster and workloads.

This phase implements three critical security controls:
1. **Continuous Vulnerability Scanning (Trivy Operator)**: Automatically scans deployed container images and Kubernetes resources for known vulnerabilities (CVEs) and misconfigurations.
2. **Runtime Threat Detection (Falco)**: Monitors Linux kernel system calls to detect anomalous or malicious activity at runtime, alerting on behaviors like unexpected shell execution inside containers.
3. **Policy Enforcement (Kyverno)**: Acts as a Kubernetes admission controller, defining and enforcing rules (e.g., preventing privileged containers or enforcing resource limits) natively.

## Requirements

- **SEC-01**: Install Trivy for image scanning
- **SEC-02**: Install Falco for runtime threat detection
- **SEC-03**: Install Kyverno for policy enforcement

## Success Criteria

1. **Trivy Operator** is running and successfully generates `vulnerabilityreport` custom resources for the demo workloads.
2. **Falco** is deployed as a DaemonSet across all nodes, actively monitoring syscalls without crashlooping.
3. **Kyverno** is running and capable of intercepting and validating API requests.
4. All deployments are fully managed via ArgoCD.

## Constraints

- No manual installations. All configuration must be committed to Git and applied by ArgoCD.
