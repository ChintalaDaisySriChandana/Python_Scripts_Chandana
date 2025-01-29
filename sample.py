def display_content(file_name):
    with open(file_name, "r") as fh:
        print (fh.read())
file_name="file.txt"
display_content(file_name)    
