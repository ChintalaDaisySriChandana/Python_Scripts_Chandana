with open("aws.py","r") as fh:
     content= fh.read()
     print(f"{content}")

with open("file.txt","w") as fh:
    fh.write("Hello World!")
    
with open("file.txt","a") as fh:
    fh.write("\nWelcome to the DevOps Class")

with open("file.txt","r") as fh:
    content= fh.read()
    print(f"{content}")


