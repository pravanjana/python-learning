import json

instances = [
    {"id" : "i-0abc", "region" : "us-east-1", "status" : "running", "cost" : 0.096},
    {"id" : "i-0def", "region" : "eu-west-1", "status" : "stopped", "cost" : 0.096},
    {"id" : "i-0ghi", "region" : "ap-south-1", "status" : "running", "cost" : 0.048},

]

with open ("instances.json", "w") as file:
    json.dump(instances, file, indent=4)

print("instances.json written successfully")