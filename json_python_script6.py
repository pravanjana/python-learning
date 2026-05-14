import json

instances = []

print(f"---Add instances (type 'done' to finish) ---")
while True:
    instance_id = input("Instance ID(or 'done'): ")
    if instance_id == "done":
        break
    region = input("Region: ")
    status = input("Status (Running/Stopped) : ")
    cost = float(input("cost_per_hour: $"))

    instances.append({
        "id" : instance_id,
        "region" : region,
        "status" : status,
        "cost" : cost
    })

with open("my_instances.json", "w") as file:
    json.dump(instances, file, indent=4)

print(f"\nSaved {len(instances)} instances to my_instances.json")
