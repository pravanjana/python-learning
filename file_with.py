with open ("servers.txt", "r") as file:
    for line in file:
        region = line.strip()
        if region.startswith("us") :
            print("US Region")
        else :
            print("International Region")
        
        print (f"Region: {region}")

