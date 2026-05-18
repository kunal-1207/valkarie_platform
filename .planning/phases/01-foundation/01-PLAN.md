# Plan: 01-01 Infrastructure Bootstrap

## Goal

Provision the foundational AWS infrastructure using Terraform, including a VPC, Subnets, IAM roles, and an EKS cluster with managed node groups.

## Implementation Steps

### 1. Setup Terraform Scaffolding
- Create the `infrastructure/terraform` directory structure.
- Define `providers.tf` for the AWS provider.
- Define `backend.tf` for remote state management (S3 bucket and DynamoDB table for locking).
- Define `variables.tf` for configurable parameters (e.g., region, cluster name).

### 2. Network Provisioning (VPC)
- Create `infrastructure/terraform/networking` module or definitions.
- Provision a new VPC.
- Create public and private subnets across multiple Availability Zones.
- Setup Internet Gateway for public subnets and NAT Gateways for private subnets.
- Configure route tables.

### 3. EKS Cluster Provisioning
- Create `infrastructure/terraform/eks` module or definitions.
- Define the EKS Cluster control plane.
- Define EKS Managed Node Groups in the private subnets.
- Setup necessary IAM roles and policies for the EKS cluster and worker nodes.

### 4. Outputs and Validation
- Define `outputs.tf` to output the EKS cluster endpoint, certificate authority data, and cluster name.
- Create a script or documentation on how to update the local `kubeconfig` using the AWS CLI.

## Verification

1. Run `terraform init`, `terraform plan`, and `terraform apply`.
2. Verify remote state is updated in the S3 bucket.
3. Run `aws eks update-kubeconfig --region <region> --name <cluster_name>`.
4. Run `kubectl get nodes` and ensure nodes are `Ready`.
