# Plan: 04-01 Voting App Deployment

## Goal

Deploy the complete multi-tier Voting App microservice architecture using ArgoCD.

## Implementation Steps

### 1. Create Application Manifests
- Create the `gitops/manifests/voting-app/` directory.
- Define `redis.yaml`: A Deployment and Service for the Redis message queue.
- Define `db.yaml`: A StatefulSet/Deployment and Service for the PostgreSQL database.
- Define `vote.yaml`: A Deployment and LoadBalancer/NodePort Service for the Python frontend.
- Define `result.yaml`: A Deployment and LoadBalancer/NodePort Service for the Node.js results UI.
- Define `worker.yaml`: A Deployment for the .NET background worker.

### 2. Configure GitOps Application
- Create `gitops/applications/voting-app.yaml`.
- Set the source to point to the new `gitops/manifests/voting-app` path in the Git repository.
- Instruct ArgoCD to automatically deploy this into a new namespace `demo`.

## Verification

1. Commit the manifests and push to the GitHub repository.
2. Wait for ArgoCD to sync the `voting-app`.
3. Check pod status: `kubectl get pods -n demo` - all should be `Running`.
4. Forward ports to access the UIs:
   - Vote: `kubectl port-forward svc/vote -n demo 5000:5000`
   - Result: `kubectl port-forward svc/result -n demo 5001:5001`
5. Cast a vote at `localhost:5000` and verify the result updates at `localhost:5001`.
6. Verify Logs are captured in Loki via the Grafana UI.
