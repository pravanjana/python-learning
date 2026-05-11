regions = [ "us-east-1", "eu-west-1", "ap-south-1", "us-gov-west-1", "ca-central-1" ]

for region in regions:
    if region.startswith("us-gov"):
        print(f"{region} -> GovCloud (restricted)" )
    elif region.startswith("us"):
        print(f"{region} -> US region" )
    elif region.startswith("eu"):
        print(f"{region} -> Europe region" )
    elif region.startswith("ap"):
        print(f"{region} -> Asia Pacific region" )
    else:
        print(f"{region} -> Canadian region" )
