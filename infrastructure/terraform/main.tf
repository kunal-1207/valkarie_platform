module "networking" {
  source = "./networking"

  vpc_cidr     = var.vpc_cidr
  environment  = var.environment
  cluster_name = var.cluster_name
}

module "eks" {
  source = "./eks"

  cluster_name = var.cluster_name
  vpc_id       = module.networking.vpc_id
  subnet_ids   = module.networking.private_subnets
  environment  = var.environment
}
