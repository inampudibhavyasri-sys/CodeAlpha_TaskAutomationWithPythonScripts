

import os
import shutil

# Source folder path
source_folder = "source_folder"

# Destination folder path
destination_folder = "destination_folder"

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Check all files in source folder
for file_name in os.listdir(source_folder):

    # Check if file is JPG
    if file_name.lower().endswith(".jpg"):

        # Full file paths
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        # Move file
        shutil.move(source_path, destination_path)

        print(file_name, "moved successfully!")

print("\nAll JPG files moved successfully!")