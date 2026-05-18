#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "=========================================="
echo " Valkyrie Platform - GitOps Bootstrap"
echo "=========================================="

echo "[1/4] Adding ArgoCD Helm repository..."
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update

echo "[2/4] Installing ArgoCD via Helm..."
# Create the namespace if it doesn't exist
kubectl create namespace argocd --dry-run=client -o yaml | kubectl apply -f -

# Install ArgoCD with our custom values
helm upgrade --install argocd argo/argo-cd \
  --namespace argocd \
  --version 6.7.11 \
  -f gitops/argocd/values.yaml

echo "[3/4] Waiting for ArgoCD server to be ready..."
kubectl wait --for=condition=available deployment/argocd-server -n argocd --timeout=300s

echo "[4/4] Applying App of Apps root application..."
kubectl apply -f gitops/applications/app-of-apps.yaml

echo ""
echo "=========================================="
echo " GitOps Bootstrap Complete! "
echo "=========================================="
echo ""
echo "ArgoCD is now managing the cluster state."
echo ""
echo "To access the ArgoCD UI, run:"
echo "  kubectl port-forward svc/argocd-server -n argocd 8080:443"
echo ""
echo "Your initial admin password is:"
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
echo ""
echo "Open https://localhost:8080 in your browser and login with username 'admin'."
