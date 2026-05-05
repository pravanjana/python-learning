
print ("---Cloud Setup Wizard---")
name = input ("What is your name? ")
company = input("What is your current company? ")
region = input ("In which region would you like to deploy your instances? ")
instances = input ("Enter the number of instances: ")
instance_type = input ("Enter the type of instance e.g. t2.micro:  ")
cost_per_hr = 0.96

monthly_cost = int(instances) * cost_per_hr * 730

print("")
print(f"Summary for {company}: ")
print(f"Engineer: {name}")
print(f"Region: {region.upper()}")
print(f"Instances: {instances}  Type: {instance_type} ")
print(f"Estimated monthly cost : ${monthly_cost:.2f}")


