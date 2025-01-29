import zipfile
import sys

def unzip_file(zip_file, output_dir):
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
        print(f"Successfully extracted '{zip_file}' to '{output_dir}'.")
    except FileNotFoundError:
        print(f"Error: The file '{zip_file}' was not found.")
    except zipfile.BadZipFile:
        print(f"Error: '{zip_file}' is not a valid zip file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python unzip_file.py <zip_file_path> <output_directory>")
    else:
        zip_file = sys.argv[1]
        output_dir = sys.argv[2]
        unzip_file(zip_file, output_dir)

