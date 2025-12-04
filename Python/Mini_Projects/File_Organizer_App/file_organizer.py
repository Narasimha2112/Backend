"""
MINI PROJECT – File Organizer App (Automation + Pathlib)
🎯 Goal

Organize files into folders based on extension:

.txt → TEXT/

.jpg → IMAGES/

.py → PYTHON/

Others → OTHERS/"
"""

from pathlib import Path
import shutil

# Current working directory
folder = Path(".")

# Folder mapping based on extension
mapping = {
    ".txt": "TEXT",
    ".jpg": "IMAGES",
    ".png": "IMAGES",
    ".py": "PYTHON",
}

# Loop through all files
for file in folder.iterdir():

    if file.is_file():
        ext = file.suffix  # get file extension
        
        # Choose folder
        if ext in mapping:
            dest_folder = Path(mapping[ext])
        else:
            dest_folder = Path("OTHERS")
        
        # Create folder if not exist
        dest_folder.mkdir(exist_ok=True)
        
        # Move file
        shutil.move(str(file), dest_folder)
        print(f"Moved {file} → {dest_folder}")
