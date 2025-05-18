#Author: omynayak, 2025
#Desktop sorter program
#Purpose: To look through the files on the desktop and sort them into the respective folders on the desktop
#Why: Because lazy to clean up my desktop


from pathlib import Path #imports the pathlib module that helps navigate around the desktop
import shutil #shell utilities helps move things around like the files I want to move around in this program

#A dictionary containing all the formats as lists and mapping them to their respective file paths relative to the desktop
formats = {
    "Media/Images":['.jpeg','.png','.jpg'],
    "Media/Video": ['.mpg', '.mp4'],
    "Media/Audio": ['.mp3', '.wav'],
    "Documents/Excel": ['.xlsx'],
    "Documents/PDF": ['.pdf'],
    "Documents/Word": ['.docx'],
}


desktop = Path.home()/"OneDrive"/"Desktop" #set the path to the desktop 

for file in desktop.iterdir(): #.iterdir iterates through all the entities in the desktop whether files, folders or whatever else
    if file.is_file(): #if the selected entity is a file
        moved=False #set the moved flag to false. This helps us find any miscellaneous files and put them into Misc
        ext = file.suffix.lower() #sets ext to the lower case version of the file extension
        for folder, extension in formats.items(): #iterating through the formats dictionary
            for ex in extension: #for each element in the lists
                if ex == ext: #if the current file extension matches the element in the list
                    dest_path = desktop / folder #add the key of the list to the desktop file path
                    dest_path.mkdir(parents=True, exist_ok=True) #creates the required file if it doesn't exist
                    shutil.move(file, dest_path / file.name) #moves the selected file to the final path
                    moved = True #set the moved flag to true so it doesnt try to move this file to Misc folder
                    break #break out of the loop
        if not moved: #if the file selected has not been moved, ie; the file extension is not in the dictionary
            dest_path = desktop / "Misc" #adds the Misc folder to the final path 
            print(f"Moving {file.name} to {dest_path}") #Just a print statement I'd put in to debug
            dest_path.mkdir(parents=True, exist_ok=True) #makes directory if it doesnt exist
            shutil.move(file, dest_path / file.name) #moves the file into the Misc folder

#I do realise that something like: 
#extension_map = {ext: folder for folder, extensions in formats.items() for ext in extensions}
#Could've made things look a lot cleaner, but I am used to the C/C++ style of deconstructed programming
#It also helps me train my python muscles before I bite into shorthand

