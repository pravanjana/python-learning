import boto3
import json
from datetime import datetime

s3 = boto3.client("s3")
response = s3.list_buckets()
buckets = response["Buckets"]

report = []

print ("--- S3 Security Report ---\n")
total_public_bucket = 0
total_private_bucket = 0
for bucket in buckets:
    name = bucket["Name"]

    try:
        acl = s3.get_bucket_acl(Bucket=name)
        public = False

        for grant in acl["Grants"]:
            grantee = grant.get("Grantee", {})
            if grantee.get("URI") == "https://acs.amazonaws.com/groups/global/AllUsers":
             public = True
        
        if public:
            total_public_bucket += 1
        else:
            total_private_bucket += 1


        status = "PUBLIC ⚠️" if public else "Private ✅"
    except Exception as e:
        status = f"Error: {str(e)}"

    print(f"{name}-> {status}")
    report.append({"bucket": name, "status" : status})

with open("s3_security_report.json", "w") as file:
    json.dump(report, file, indent=4)

print(f"\nReport saved to s3_security_report.json")
print(f"\nTotal public bucket(s) is {total_public_bucket} and Total private bucket(s) is {total_private_bucket}")
print(f"Scanned {len(buckets)} bucket(s) at {datetime.now().strftime('%Y-%m-%d %H:%M')}")


