provider "aws" {
  region  = var.aws_region
  profile = var.aws_profile
}

resource "aws_ecr_repository" "ecr_repo" {
  name                 = "infinite-devops-repo"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
