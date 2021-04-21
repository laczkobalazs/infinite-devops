variable "aws_profile" {
  type    = string
  default = "twosteps-admin"
}

variable "aws_region" {
  type    = string
  default = "eu-central-1"
}

variable "DB_PORT" {
  type        = string
  description = "The port on which the DB accepts connections"
  default     = "5432"
}
