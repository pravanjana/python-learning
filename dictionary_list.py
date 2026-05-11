instances = [
    {"id": "i-0abc", "region": "us-east-1", "status": "running", "cost": 0.096},
    {"id": "i-0def", "region": "eu-west-1", "status": "stopped", "cost": 0.096},
    {"id": "i=0ghi", "region": "ap-south-1", "status": "running", "cost": 0.048},
    {"id": "i=0jkl", "region": "ca-central-1", "status": "running", "cost": 0.086},

]

print("--- Instance Report ---")
total_monthly = 0
for instance in instances:
    if instance ["status"] == "running":
        monthly = instance["cost"] * 730
        total_monthly = total_monthly + monthly
        print(f"{instance['id']} | {instance['region']} | {instance['status']} | ${monthly:.2f}/month")
    else:
        print(f"{instance['id']} | {instance['region']} | {instance['status']} | $0.00/month")
print (f"The total monthly cost of all running instances is : ${total_monthly}")
