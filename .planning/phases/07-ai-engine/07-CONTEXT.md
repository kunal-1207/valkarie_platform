# Phase 7: AI Incident Engine

## Context

A core value proposition of the Valkyrie Platform is reducing Mean Time To Resolution (MTTR) by utilizing autonomous AI. When chaos engineering (or real-world failures) trigger Prometheus alerts, engineers are typically bombarded with raw JSON payloads and dense metric tags.

In this phase, we bridge the gap between telemetry and human comprehension. We deploy a localized, privacy-preserving Large Language Model (Ollama) directly into the cluster. We then deploy a custom Python FastAPI webhook service that intercepts alerts from Alertmanager, feeds the dense JSON context to the LLM, and logs a clear, human-readable summary of the incident and suggested remediation steps.

## Requirements

- **AI-01**: Install Ollama in cluster
- **AI-02**: Deploy small LLM (phi3 or llama3)
- **AI-03**: Create FastAPI webhook to receive Prometheus alerts and summarize

## Success Criteria

1. Ollama is running in the `ai` namespace and successfully serves the `phi3` model.
2. The custom `incident-engine` FastAPI service is deployed and reachable.
3. The FastAPI service successfully communicates with Ollama's local API.
4. Sending a mock Prometheus alert to the FastAPI webhook results in an AI-generated summary logged to stdout.

## Constraints

- The LLM must run locally within the cluster (no external OpenAI/Anthropic API calls) to guarantee data privacy and zero egress costs.
