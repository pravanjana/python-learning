import json

with open("instances.json", "r") as file:
    instances = json.load(file)

print(f"Loaded {len(instances)} instances from file \n")

total_cost = 0
for instance in instances:
    if instance["status"] == "running":
        monthly = instance["cost"] * 730
        total_cost +=monthly
        print(f"{instance['id']} | {instance['region']} | ${monthly:.2f}/month")

print(f"\n Total running cost: ${total_cost:.2f}/month")
