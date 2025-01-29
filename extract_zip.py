import shutil

def folder_to_zip(folder_path, output_zip_path):
    """
    Compress a folder into a ZIP file.

    :param folder_path: Path to the folder to compress.
    :param output_zip_path: Path for the output ZIP file (without .zip extension).
    """
    try:
        # Create a ZIP file from the folder
        shutil.make_archive(output_zip_path, 'zip', folder_path)
        print(f"Folder successfully compressed into: {output_zip_path}.zip")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
folder_path = "/home/ubuntu/hello-world-war"  # Replace with the path to your folder
output_zip_path = "/home/ubuntu/hello-world-war"  # Replace with the desired output file path (no .zip needed)
folder_to_zip(folder_path, output_zip_path)
