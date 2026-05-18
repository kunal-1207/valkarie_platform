# Plan: 07-01 AI Engine Deployment

## Goal

Write and containerize a custom FastAPI incident engine, and deploy both it and Ollama to the cluster via GitOps.

## Implementation Steps

### 1. Incident Engine Application
- Create `src/incident-engine/main.py` using FastAPI. 
- Define a `POST /webhook` endpoint that accepts Alertmanager JSON payloads.
- Use `httpx` to send a prompt containing the alert data to the local Ollama API (`http://ollama:11434/api/generate`).
- Log the summarized response to stdout.
- Create `src/incident-engine/requirements.txt` and `src/incident-engine/Dockerfile`.

### 2. Ollama Manifest
- Create `gitops/manifests/ai/ollama.yaml`.
- Define a Deployment for the `ollama/ollama:latest` image.
- Include a `postStart` lifecycle hook or an init script to automatically pull the `phi3` model when the pod starts.
- Define a Service exposing port `11434`.

### 3. Incident Engine Manifest
- Create `gitops/manifests/ai/incident-engine.yaml`.
- Define a Deployment for the incident engine image (using a placeholder or standard image if unbuilt).
- Pass the `OLLAMA_URL` environment variable pointing to the Ollama service.
- Define a Service exposing port `8000`.

### 4. GitOps Application
- Create `gitops/applications/ai-engine.yaml`.
- Define an ArgoCD Application targeting the `gitops/manifests/ai/` directory.
- Deploy to the `ai` namespace.

## Verification

1. Push all code and manifests to GitHub.
2. Verify ArgoCD deploys the `ai-engine` successfully.
3. Wait for the `ollama` pod to download the model (`kubectl logs -n ai deployment/ollama`).
4. Port-forward the `incident-engine`: `kubectl port-forward svc/incident-engine -n ai 8000:8000`.
5. `curl -X POST http://localhost:8000/webhook -d '{"alerts": [{"labels": {"alertname": "HighCPU"}}]}'` and verify an AI summary is generated in the logs.
