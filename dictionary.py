instance = {
    "id" : "i-0abc12345",
    "owner" : "Pravanjana",
    "type" : "t2.micro",
    "region" : "us-east-1",
    "status" : "running",
    "cost_per_hour" : 0.096
}

print ("Instance ID:", instance["id"])
print ("Region:", instance["region"])
print ("Status:", instance["status"])
print ("Monthly cost: $" + str(instance["cost_per_hour"]*730))
print ("Owner:", instance["owner"])

