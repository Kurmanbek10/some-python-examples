import subprocess
import sys

def run(cmd):
    print(f"\nRunning: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"Command failed: {' '.join(cmd)}")
        sys.exit(result.returncode)

print("Step 1")
print("checking code for syntax/format errors ...")

run(["terraform", "fmt"])
run(["terraform", "init"])
run(["terraform", "validate"])

print("checking terraform code with init and plan")

run(["terraform", "plan"])