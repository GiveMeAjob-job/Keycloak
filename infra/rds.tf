resource "aws_db_instance" "keycloak" {
  identifier              = var.rds_identifier
  engine                  = "postgres"
  engine_version          = "14"
  instance_class          = var.rds_instance_class
  allocated_storage       = 20
  username                = "keycloak"
  password                = var.rds_password
  db_name                 = "keycloak"
  multi_az                = true
  storage_encrypted       = true
  kms_key_id              = var.rds_kms_key_id
  vpc_security_group_ids  = [aws_security_group.db.id]
  backup_retention_period = 7
  skip_final_snapshot     = true
}
