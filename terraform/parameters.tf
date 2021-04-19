data "aws_ssm_parameter" "rds_database_name" {
  name = "rds_database_name"
}

data "aws_ssm_parameter" "rds_database_username" {
  name = "rds_database_username"
}

data "aws_ssm_parameter" "rds_database_password" {
  name = "rds_database_password"
}
