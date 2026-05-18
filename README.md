<div align="center">
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" />
  <img src="https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white" />
  <img src="https://img.shields.io/badge/ArgoCD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white" />
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" />
  <img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" />
  <img src="https://img.shields.io/badge/Ollama-000000?style=for-the-badge&logo=ollama&logoColor=white" />
</div>

<h1 align="center">Valkyrie Platform 🛡️</h1>

<p align="center">
  <strong>A Production-Grade, Autonomous DevOps Platform on AWS EKS</strong>
</p>

## 📖 Overview

The **Valkyrie Platform** is a comprehensive, end-to-end DevOps environment designed to demonstrate modern cloud-native engineering principles. It goes beyond simple deployment, offering a fully autonomous platform featuring Infrastructure as Code (IaC), GitOps delivery, deep observability, active security enforcement, chaos engineering, and a localized AI Incident Engine.

## 🚀 Key Features

*   **Infrastructure as Code (IaC)**: Modular Terraform provisioning an AWS EKS cluster, VPC, and networking architecture.
*   **GitOps Delivery Engine**: Complete declarative deployment via ArgoCD using the "App of Apps" pattern.
*   **Full-Stack Observability**: Metrics (Prometheus), Logs (Loki), and Traces (Tempo) unified within a dynamic Grafana dashboard.
*   **Active Security & Policy**: Continuous vulnerability scanning (Trivy), runtime threat detection (Falco), and native admission control (Kyverno).
*   **Chaos Engineering**: Intentional fault injection (LitmusChaos) to validate system resilience and alert configurations.
*   **AI Incident Summarization**: A localized, privacy-preserving LLM (`phi3` via Ollama) integrated with a custom FastAPI webhook to automatically intercept alerts and generate human-readable root-cause summaries.
*   **Developer Portal**: A unified catalog and documentation hub powered by Spotify's Backstage.

## 🏗️ Architecture

For a deep dive into the system's architecture, including interactive Mermaid.js diagrams mapping the delivery flows and the AI incident pipeline, please see the [Architecture Documentation](ARCHITECTURE.md).

## 🛠️ Technology Stack

| Category | Tools Used |
| :--- | :--- |
| **Cloud & Infrastructure** | AWS, EKS, Terraform |
| **Container Orchestration** | Kubernetes, Helm |
| **CI/CD & GitOps** | GitHub Actions, ArgoCD |
| **Observability** | Prometheus, Grafana, Loki, Promtail, Tempo |
| **Security & Policies** | Trivy Operator, Falco (eBPF), Kyverno |
| **Chaos Engineering** | LitmusChaos |
| **AI & Automation** | Ollama (phi3), Python, FastAPI |
| **Developer Experience** | Backstage |

## ⚙️ Quick Start

This repository is designed to be fully declarative. To replicate this platform:

1.  **Provision Infrastructure**:
    ```bash
    cd infrastructure/terraform
    terraform init && terraform apply
    aws eks update-kubeconfig --region us-east-1 --name valkyrie-cluster
    ```
2.  **Bootstrap GitOps**:
    ```bash
    ./scripts/bootstrap-gitops.sh
    ```
    *This script installs ArgoCD and applies the root `app-of-apps.yaml`, which automatically synchronizes all other platform layers (Observability, Security, Chaos, AI Engine) directly from this repository.*

## 🏷️ Repository Tags

If you are discovering this repository, it touches upon the following domains:
`kubernetes` `aws` `terraform` `gitops` `argocd` `observability` `prometheus` `grafana` `security` `devsecops` `chaos-engineering` `llm` `aiops` `backstage`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
