variable "region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR for public subnet"
  default     = "10.0.1.0/24"
}

variable "private_subnet_cidr" {
  description = "CIDR for private subnet"
  default     = "10.0.2.0/24"
}

variable "azs" {
  description = "Availability zones to use"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

variable "az" {
  description = "Availability zone"
  default     = "us-east-1a"
}

variable "ami" {
  description = "AMI for bastion host"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t3.micro"
}

variable "key_name" {
  description = "Key pair name for bastion"
}

variable "public_key_path" {
  description = "Path to public SSH key"
}

variable "backup_bucket" {
  description = "S3 bucket for Keycloak backups"
}

variable "trail_bucket" {
  description = "S3 bucket for CloudTrail logs"
}

variable "state_bucket" {
  description = "S3 bucket for Terraform state"
}

variable "state_lock_table" {
  description = "DynamoDB table for state locking"
}

variable "office_cidr" {
  description = "CIDR for office network access"
  default     = "0.0.0.0/0"
}
