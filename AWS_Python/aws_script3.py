import boto3

ec2 = boto3.client("ec2", region_name="us-east-1")
response = ec2.describe_instances()

reservations = response["Reservations"]

if not reservations:
    print("No EC2 instances found in us-east-1")
else:
    for reservation in reservations:
        for instance in reservation["Instances"]:
            if instance ['State']['Name'] == "running":
              print(f"ID : {instance['InstanceId']}")
              print(f"Type : {instance['InstanceType']}")
              print(f"State : {instance['State']['Name']}")

            print("---")

            