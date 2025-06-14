output "alb_dns" { value = aws_lb.this.dns_name }
output "keycloak_admin_url" { value = "https://${aws_lb.this.dns_name}" }
