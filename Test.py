name = input("Enter your name: ")
region = input("Enter AWS region: ")
instances = input("How many instances? ")

print(f"Hello {name}!")
print(f"Deploying {instances} instances to {region}")
print(f"Environment is now ready in {region.upper()}")