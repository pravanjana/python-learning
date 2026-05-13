def get_instance_info(instance_id, region="us-east-1", status="running", cost_per_hour=0.096):
    print(f"ID : {instance_id}")
    print(f"Region : {region}")
    print(f"Status : {status}")
    print(f"Monthly cost : ${cost_per_hour*730}")
    print("---")

get_instance_info("i-0abc")
get_instance_info("i-0def", region="eu-west-1")
get_instance_info("i-0ghi", region="ap-south-1", status="stopped")
