variable "cpu" { type = number }
variable "memory" { type = number }
variable "desired_count" { type = number }
variable "db_password_ssm_key" { type = string }
variable "execution_role" { type = string }
variable "image" { type = string }
variable "admin_password" { type = string }
variable "subnets" { type = list(string) }
