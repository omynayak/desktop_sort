# Author: omynayak, 2025
# Desktop Sorter Program 2.0
# Purpose: Automatically organizes desktop files into categorized folders
# Motivation: To avoid manually cleaning the desktop every week

from pathlib import Path  # OS-independent path handling
import shutil  # Used to move files between directories
import re  # For splitting filenames intelligently based on patterns

# Define categories and their corresponding file extensions
formats = {
    "Media/Images": ['.jpeg', '.png', '.jpg'],
    "Media/Video": ['.mpg', '.mp4'],
    "Media/Audio": ['.mp3', '.wav'],
    "Documents/Excel": ['.xlsx'],
    "Documents/PDF": ['.pdf'],
    "Documents/Word": ['.docx'],
    "Documents/Stray_Code": ['.py', '.cpp', '.c', '.html', '.css']
}

# Get the path to the user's Desktop
desktop = Path.home() / "OneDrive" / "Desktop"

# Go through each item on the Desktop
for file in desktop.iterdir():
    if file.is_file():  # Skip folders
        ext = file.suffix.lower()  # Normalize extension case

        # Split the filename (without extension) on underscores and dots
        extraPath = re.split(r'[_.]', file.name)

        # Check which category this file belongs to
        for folder, extension in formats.items():
            for ex in extension:
                if ex == ext:  # Match found
                    dest_path = desktop / folder  # Start building the target folder path

                    # Add subfolders based on filename parts (excluding name and extension)
                    for element in extraPath[1:-1]:
                        if element:
                            dest_path = dest_path / element

                    # Handle duplicate filenames by appending a counter
                    suffix = file.suffix
                    counter = 1
                    new_name = f"{extraPath[0]}{suffix}"
                    while (dest_path / new_name).exists():
                        new_name = f"{extraPath[0]}({counter}){suffix}"
                        counter += 1

                    # Ensure destination exists, then move the file
                    dest_path.mkdir(parents=True, exist_ok=True)
                    shutil.move(file, dest_path / new_name)
                    break  # Stop once a match is found

        # Note: Unmatched files are left untouched.
        # This avoids unnecessary relocation of system or config files.

# AUTO-START SETUP (Optional):
# To run this script at startup, use a .bat file with the following content:
#
#   @echo off
#   "C:\Users\ASUS\AppData\Local\Programs\Python\Python313\pythonw.exe" "C:\Users\ASUS\OneDrive\Desktop\Dev Stuff\Python\desktop_sort2.py"
#
# Place this .bat file in the Windows startup folder (accessible via `shell:startup`)
# This ensures your desktop stays organized automatically after every login.
