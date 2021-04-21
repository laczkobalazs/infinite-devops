resource "aws_instance" "ec2_jenkins" {
  ami           = "ami-0767046d1677be5a0"
  instance_type = "t2.micro"
  key_name      = "infinite-key"
  tags = {
    "name" = "ec2-jenkins"
  }
}
