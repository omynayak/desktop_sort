# Author: omynayak, 2025
# Desktop Sorter Program 2.0
# Purpose: To automatically sort files on the desktop into structured folders based on type
# Why: Because I don’t want to manually clean my desktop every week

from pathlib import Path  # Helps navigate and manage file paths in an OS-independent way
import shutil  # Gives me shell operations like moving files
import re  # Helps in pattern splitting to break filenames intelligently

# A dictionary mapping categories to lists of extensions, determining where each file goes
formats = {
    "Media/Images": ['.jpeg', '.png', '.jpg'],
    "Media/Video": ['.mpg', '.mp4'],
    "Media/Audio": ['.mp3', '.wav'],
    "Documents/Excel": ['.xlsx'],
    "Documents/PDF": ['.pdf'],
    "Documents/Word": ['.docx'],
}

# Get the path to the my Desktop 
desktop = Path.home() / "OneDrive" / "Desktop"

# Iterate over every item in the desktop folder
for file in desktop.iterdir():
    if file.is_file():  # Only care about actual files (not folders)
        ext = file.suffix.lower()  # Get the file extension, lowercase to handle cases like .JPG

        # Break the filename (excluding the extension) into components using _ and . as delimiters
        extraPath = re.split(r'[_.]', file.name)

        # Loop through our predefined format categories
        for folder, extension in formats.items():
            for ex in extension:
                if ex == ext:  # If we find a match
                    dest_path = desktop / folder  # Start the destination path with the base folder

                    # Build nested folders using the components of the filename (ingoring the first which is name and last which is format)
                    for element in extraPath[1:-1]:
                        if element:  # Avoid empty strings
                            dest_path = dest_path / element

                    #I noticed that if a file with the same name already exists in the destination it just gets overwritten 
                    #This bit of code helps protect from that
                    counter = 1
                    new_name = file.name
                    while(dest_path / new_name).exists(): #as long as there is a file in the destination with the same filename
                        #split the name into file name and suffix
                        stem = file.stem    
                        suffix = file.suffix

                        #attach the counter value to the filename and put it back together
                        new_name = f"{stem}({counter}){suffix}"
                        counter += 1 #increment counter 


                    dest_path.mkdir(parents=True, exist_ok=True)  # Create the destination directory if needed
                    shutil.move(file, dest_path / new_name)  # Move the file (new name) to the appropriate location
                    break  # Stop checking once matched

        # Unlike previous versions, we don't move unmatched files into a "Misc" folder.
        # Why? Because it's better to leave unknown or system files where they are rather than lumping them together
        # This avoids clutter and potential errors from moving system or config files

# AUTO-START INTEGRATION:
# This script is meant to run automatically on system startup via a .bat file.
# The .bat file should look like this:
#
#   @echo off
#   "C:\Users\ASUS\AppData\Local\Programs\Python\Python313\pythonw.exe" "C:\Users\ASUS\OneDrive\Desktop\Dev Stuff\Python\desktop_sort2.py"
#
# By using `pythonw.exe`, we ensure the script runs silently in the background (no terminal pop-up).
# Placing this .bat file in the system startup folder (`shell:startup`) makes sure it runs every time you log in.
# This gives you a constantly tidy desktop with no manual effort.
