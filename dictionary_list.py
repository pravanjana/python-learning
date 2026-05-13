def get_monthly_cost(cost_per_hour, status):
    if status == "running":
        return cost_per_hour * 730
    return 0


def print_instance(instance):
    cost = get_monthly_cost(instance["cost"], instance["status"])
    print(f"{instance['id']} | {instance['region']} | {instance['status']} | ${cost:.2f}/month")

def count_running(instances):
    count = 0
    for instance in instances:
        if instance["status"] == "running":
            count = count + 1
    return count
    


def print_report(instances):
    print("---Instance Report---")
    total = 0
    for instance in instances:
        print_instance(instance)
        total += get_monthly_cost(instance["cost"], instance["status"])
    print(f"\nTotal running cost: ${total:.2f}/month")

instances = [
    {"id": "i-0abc", "region": "us-east-1", "status": "running", "cost": 0.096},
    {"id": "i-0def", "region": "eu-west-1", "status": "stopped", "cost": 0.096},
    {"id": "i-0ghi", "region": "ap-south-1", "status": "running", "cost": 0.048},
    {"id": "i-0jkl", "region": "ca-central-1", "status": "running", "cost": 0.086},

]


print_report(instances)
running = count_running(instances)
print(f"The total number of running instances is : {running:.2f}") 