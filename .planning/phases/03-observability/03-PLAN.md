# Plan: 03-01 Unified Observability

## Goal

Deploy Prometheus, Grafana, Loki, and Tempo via GitOps, pre-configuring Grafana to recognize Loki and Tempo as DataSources.

## Implementation Steps

### 1. Kube-Prometheus-Stack
- Create `gitops/applications/kube-prometheus-stack.yaml`.
- Define an ArgoCD Application targeting the `kube-prometheus-stack` chart from the `prometheus-community` Helm repository.
- Provide inline Helm values (`additionalDataSources`) to pre-configure `loki` and `tempo` datasources in Grafana.

### 2. Loki-Stack
- Create `gitops/applications/loki-stack.yaml`.
- Define an ArgoCD Application targeting the `loki-stack` chart from the `grafana` Helm repository.
- Ensure Promtail is enabled to automatically scrape logs from all nodes.

### 3. Tempo
- Create `gitops/applications/tempo.yaml`.
- Define an ArgoCD Application targeting the `tempo` chart from the `grafana` Helm repository.
- Configure Tempo to accept standard OpenTelemetry and Zipkin traces.

## Verification

1. Commit the new application manifests to the Git repository.
2. Observe the ArgoCD UI (`https://localhost:8080`) to ensure `kube-prometheus-stack`, `loki`, and `tempo` applications are created and sync successfully.
3. Access the Grafana UI using `kubectl port-forward svc/valkyrie-root-grafana -n monitoring 3000:80` (service name may vary based on helm release).
4. Navigate to `Connections -> Data sources` in Grafana to confirm Prometheus, Loki, and Tempo exist and test successfully.
