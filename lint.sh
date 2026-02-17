#!/bin/sh

echo "Step 1"
echo "checking code for syntax/format errors ..."

terraform fmt
terraform validate

echo "checking terraform code with init and plan"
terraform init
terraform plan