# Phase 6: Chaos Engineering

## Context

To truly validate our platform's resilience and the effectiveness of our observability stack, we must intentionally inject failure. We are moving beyond hypothetical failures and introducing controlled chaos into the environment. 

We will use **LitmusChaos**, a cloud-native chaos engineering framework. Litmus operates using Custom Resource Definitions (CRDs). A `ChaosExperiment` defines the *type* of fault, and a `ChaosEngine` binds that experiment to a specific *target* (our Phase 4 Demo Workload).

This phase implements three specific chaos experiments:
1. **Pod Delete**: Randomly terminates pods to test self-healing and deployment redundancy.
2. **CPU Hog**: Artificially spikes CPU utilization to test resource limits and horizontal pod autoscaling (if configured), as well as monitor alerting thresholds.
3. **Network Latency**: Injects delay into network packets to test application timeout handling and degraded service scenarios.

## Requirements

- **CHAOS-01**: Install LitmusChaos
- **CHAOS-02**: Run pod delete chaos
- **CHAOS-03**: Run CPU stress
- **CHAOS-04**: Run network latency

## Success Criteria

1. LitmusChaos Operator is successfully deployed via ArgoCD.
2. Chaos experiment CRDs are deployed and executed successfully against the `demo` namespace.
3. The injected faults (pod terminations, CPU spikes, latency) are clearly visible in the Grafana observability dashboards.
4. The target application recovers from the injected faults automatically.

## Constraints

- Chaos experiments must be scoped specifically to the `demo` namespace to avoid accidentally impacting the core platform components (ArgoCD, Prometheus, etc.).
