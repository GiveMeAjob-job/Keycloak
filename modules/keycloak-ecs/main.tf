resource "aws_ecs_task_definition" "kc" {
  family                   = "keycloak"
  cpu                      = var.cpu
  memory                   = var.memory
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = var.execution_role
  container_definitions    = jsonencode([
    {
      name  = "keycloak"
      image = var.image
      portMappings = [{ containerPort = 8080 }]
      environment = [
        { name = "KEYCLOAK_ADMIN", value = "admin" },
        { name = "KEYCLOAK_ADMIN_PASSWORD", value = var.admin_password }
      ]
    }
  ])
}

resource "aws_lb" "this" {
  name               = "kc-lb"
  load_balancer_type = "application"
  subnets            = var.subnets
}

output "alb_dns" {
  value = aws_lb.this.dns_name
}
