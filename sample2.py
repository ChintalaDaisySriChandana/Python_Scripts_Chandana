import pandas as pd

def check_str(x):
    if isinstance(x, str):
        return x.strip()
    else:
        return x

def read_excel_content(excel_file_path, json_file_path):
    # Read the Excel file (ensure correct path and sheet name)
    data = pd.read_excel(excel_file_path, sheet_name="Sheet1")
    data1 = data.applymap(check_str)
    data1.to_json(json_file_path, orient="records", indent=3)
    print("Excel file converted into the JSON file.")

# Correct file paths
excel_file_path = "/home/ubuntu/python/sample.xlsx"
json_file_path = "1.json"

read_excel_content(excel_file_path, json_file_path)

