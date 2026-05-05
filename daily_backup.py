"""
Ogechukwu Okereke
CMSC 111
Week 15 Assignment 2
"""
import os
import zipfile
from datetime import datetime

important_folder = "important_files"
backup_folder = "backups"
log_file = "backup_log.txt"

os.makedirs(backup_folder, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
zip_filename = f"backup_{timestamp}.zip"
zip_path = os.path.join(backup_folder, zip_filename)

file_count = 0

with zipfile.ZipFile(zip_path, "w") as zip_file:
    for file_name in os.listdir(important_folder):
        file_path = os.path.join(important_folder, file_name)

        if os.path.isfile(file_path):
            zip_file.write(file_path, arcname=file_name)
            file_count += 1

log_time = datetime.now().strftime("%Y-%m-%d %H:%M")

with open(log_file, "a") as log:
    log.write(f"{log_time} - Created {zip_path} ({file_count} files)\n")

print(f"Backup created: {zip_path}")
print(f"Files backed up: {file_count}")
