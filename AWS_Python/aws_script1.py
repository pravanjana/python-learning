import boto3

s3 = boto3.client("s3")
response = s3.list_buckets()

buckets = response["Buckets"]
if len(buckets) == 0:
    print("No buckets found")

else:
  print(f"You have {len(buckets)} S3 bucket(s):\n")
  for bucket in buckets:
    print(f"Bucket: {bucket['Name']} | Created: {bucket['CreationDate']}")



