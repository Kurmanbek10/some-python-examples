# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

# Create a VPC resource
resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default" # Can also be "dedicated"

  tags = {
    Name = "main"
  }
}