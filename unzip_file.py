import zipfile
import os

# Specify the path to the zip file
zip_file_path = "/home/ubuntu/practice_2024/sample.xlsx"

# Specify the directory where the files will be extracted
extract_to_path = "/home/ubuntu/"

# Ensure the extraction directory exists
os.makedirs(extract_to_path, exist_ok=True)

# Open and extract the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)

print(f"Files extracted to: {extract_to_path}")
