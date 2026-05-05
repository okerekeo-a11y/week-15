"""
Ogechukwu Okereke
CMSC 111
Week 15 Assignment 1
"""
import os
import shutil
import zipfile

data_folder = "data"
csv_folder = os.path.join(data_folder, "CSV_Files")
zip_name = "data_backup.zip"

csv_files = []

for file_name in os.listdir(data_folder):
    if file_name.endswith(".csv"):
        csv_files.append(file_name)

print(f"Found {len(csv_files)} CSV files.")

os.makedirs(csv_folder, exist_ok=True)

moved_count = 0

for file_name in csv_files:
    source_path = os.path.join(data_folder, file_name)
    destination_path = os.path.join(csv_folder, file_name)

    shutil.move(source_path, destination_path)
    moved_count += 1

print(f"Moved {moved_count} CSV files to data/CSV_Files.")

with zipfile.ZipFile(zip_name, "w") as zip_file:
    for file_name in os.listdir(csv_folder):
        if file_name.endswith(".csv"):
            file_path = os.path.join(csv_folder, file_name)
            zip_file.write(file_path, arcname=file_name)

print(f"Created archive: {zip_name}")
