import boto3

s3 = boto3.client("s3")
s3.delete_bucket(Bucket="pravanjana-python-2026")
print("Bucket deleted successfully")
