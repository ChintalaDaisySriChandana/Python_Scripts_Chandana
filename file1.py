import os

for root, dirs, files in os.walk("/home/ubuntu"):
    for file in files:
        if file.startswith('LICENSE'):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as fh:
                content = fh.read()
                print(f"{content}")
            
            with open("license_append.txt", "a") as fh1:
                fh1.write(f"The path of the file: {file_path}\n")
                fh1.write(f"The corresponding content:\n{content}\n\n")
            
            with open("license_append.txt", "r") as fh1:
                content1 = fh1.read()
                print(content1)

