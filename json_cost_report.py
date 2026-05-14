import json
def calculate_monthly_cost(cost_per_hour):
    return cost_per_hour * 730

try:
    with open ("my_instances.json", "r") as file:
       instances=json.load(file)
    for instance in instances:
       cost = calculate_monthly_cost(instance["cost"])
       print(f"{instance['id']} | {instance['region']} | ${cost:.2f}/month")

except FileNotFoundError:
    print("My_instances.json file not found")









