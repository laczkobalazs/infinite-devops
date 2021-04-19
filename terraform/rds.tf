resource "aws_db_instance" "rds_postgres" {
  allocated_storage     = 20
  max_allocated_storage = 50
  engine                = "postgres"
  engine_version        = "12.5"
  instance_class        = "db.t2.micro"
  identifier            = "postgresql-db-1"
  name                  = "value"
  username              = "value"
  password              = "value"
  skip_final_snapshot   = true
}
