# The ENDPOINT for python app
output "rds_hostname" {
  value = aws_db_instance.rds_postgres.address
}
