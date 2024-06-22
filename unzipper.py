import shutil
import zipfile
import os

def unzip_and_move(zip_folder_path, universal_folder_path):
    # Ensure the universal folder exists
    if not os.path.exists(universal_folder_path):
        os.makedirs(universal_folder_path)
    
    # Iterate through each file in the zip folder
    for filename in os.listdir(zip_folder_path):
        if filename.endswith('.zip'):
            zip_path = os.path.join(zip_folder_path, filename)
            
            # Extract the zip file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                for member in zip_ref.namelist():
                    # Construct the path to the universal folder
                    extracted_path = os.path.join(universal_folder_path, os.path.basename(member))
                    
                    # If the extracted file is a directory, continue to the next item
                    if member.endswith('/'):
                        continue
                    
                    # Extract the member to the universal folder
                    with zip_ref.open(member) as source, open(extracted_path, 'wb') as target:
                        shutil.copyfileobj(source, target)


zip_folder_path = 'c:/unzip'  # Replace with your zip folder path
universal_folder_path = 'c:/zip'  # Replace with your universal folder path

# Unzip files and move contents
unzip_and_move(zip_folder_path, universal_folder_path)
