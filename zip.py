import zipfile
import os
import shutil

# Define paths
zip_file_path = "saved_stable_diffusion_pipeline.zip"
temp_extracted_dir = "temp_extracted_model"
final_dir_name = "model"
# Extract the zip file to a temporary directory
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(temp_extracted_dir)

# Rename the extracted directory to "model"
extracted_dir_contents = os.listdir(temp_extracted_dir)
if len(extracted_dir_contents) == 1:
    # If there is only one directory in the temp folder, rename it
    original_dir_path = os.path.join(temp_extracted_dir, extracted_dir_contents[0])
    if os.path.exists(final_dir_name):
        print(f"Directory '{final_dir_name}' already exists.")
    else:
        os.rename(original_dir_path, final_dir_name)
        print(f"Directory renamed to '{final_dir_name}'")
else:
    print("The temporary directory contains more than one item or no items. Manual intervention may be needed.")

# Clean up temporary directory if it's empty
if not os.listdir(temp_extracted_dir):
    os.rmdir(temp_extracted_dir)

