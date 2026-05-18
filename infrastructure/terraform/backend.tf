terraform {
  backend "s3" {
    bucket         = "vkyrie-tf-state-456840671315" # Change this to a globally unique bucket name
    key            = "foundation/terraform.tfstate"
    region         = "ap-south-1"
    encrypt        = true
    dynamodb_table = "valkyrie-platform-tf-locks"
  }
}
