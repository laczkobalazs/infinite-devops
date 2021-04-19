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

resource "aws_s3_bucket" "s3_bucket" {
  bucket = "infinite-bucket-for-hosting"
  acl    = "public-read"
  versioning {
    enabled = true
  }

  website {
    index_document = "index.html"
  }

  policy = file("s3-public-read-policy.json")
}
