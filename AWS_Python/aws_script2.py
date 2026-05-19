import boto3
from botocore.exceptions import ClientError

s3 = boto3.client("s3")
bucket_name = input ("Enter a unique bucket name: ")

try :
 
 s3.create_bucket(Bucket=bucket_name)
 print(f"Bucket '{bucket_name}' created successfully!")

except ClientError as e:
 error_code = e.response["Error"]["Code"]
 if error_code == "BucketAlreadyOwnedByYou":
  print("You already own this bucket")
 elif error_code == "BucketAlreadyExists":
  print("This bucket is taken by someone else - try a different name")
 else:
  print(f"Error :{error_code}")


response = s3.list_buckets()
print(f"\n You have now {len(response['Buckets'])} bucket(s)")
