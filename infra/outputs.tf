output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_ids" {
  value = [for s in aws_subnet.public : s.id]
}

output "private_subnet_ids" {
  value = [for s in aws_subnet.private : s.id]

}

output "bastion_ip" {
  value = aws_instance.bastion.public_ip
}

output "nat_gateway_id" {
  value = aws_nat_gateway.ngw.id
}

