# Plan: 06-01 LitmusChaos Deployment & Experiments

## Goal

Deploy the LitmusChaos operator via ArgoCD and create targeted chaos experiments against the Demo Workload.

## Implementation Steps

### 1. Litmus Operator Application
- Create `gitops/applications/litmus.yaml`.
- Define an ArgoCD Application targeting the `litmus` chart from the `litmuschaos` Helm repository.
- Deploy it into the `litmus` namespace.

### 2. Chaos Experiment Manifests
- Create `gitops/manifests/chaos/rbac.yaml`: A ServiceAccount, Role, and RoleBinding in the `demo` namespace granting Litmus permission to manipulate pods.
- Create `gitops/manifests/chaos/pod-delete.yaml`: A `ChaosEngine` defining a pod-delete experiment targeting the `vote` deployment.
- Create `gitops/manifests/chaos/cpu-hog.yaml`: A `ChaosEngine` defining a cpu-hog experiment targeting the `worker` deployment.
- Create `gitops/manifests/chaos/network-latency.yaml`: A `ChaosEngine` defining a network-latency experiment targeting the `db` deployment.

### 3. Chaos Experiments Application
- Create `gitops/applications/chaos-experiments.yaml`.
- Define an ArgoCD Application pointing to the `gitops/manifests/chaos/` directory, syncing these resources to the cluster.

## Verification

1. Commit all files and push to GitHub.
2. Verify ArgoCD deploys the `litmus` application successfully.
3. Verify ArgoCD deploys the `chaos-experiments` application successfully.
4. Check the `demo` namespace for chaos runner pods (`kubectl get pods -n demo -l component=chaos-runner`).
5. Verify the chaos results by checking the `ChaosResult` custom resources (`kubectl get chaosresult -n demo`).
