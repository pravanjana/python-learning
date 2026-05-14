file = open("servers.txt", "r")
print("File contents: ")
#content = file.read()
lines = file.readlines()
for line in lines:
    print(line)
    
file.close()



