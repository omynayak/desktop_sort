# Desktop Sort

Automatically declutters your desktop using filename semantics and file extensions.

---

## What is it?

`desktop_sort` is a Python script that utilizes the `pathlib`, `shutil`, and `re` libraries to:

- Detect stray files on your desktop
- Identify their type using file extensions
- Organize them into categorized directories
- Further nest them into custom subfolders using semantic filename hints

---

## How it works

1. **File Type Detection**:  
   Based on the file extension, it assigns files to a primary category like `Media/Images`, `Documents/PDF`, etc.

2. **Semantic Subdirectory Sorting**:  
   If you name your file like this:
   ```
   report_finance_q1.pdf
   ```
   The script moves it to:
   ```
   ~/Desktop/Documents/PDF/finance/q1/report.pdf
   ```

   The filename format is interpreted as:  
   ```
   <filename>_<subdir1>_<subdir2>.<extension>
   ```

3. **Duplicate Handling**:  
   If a file with the same name exists, it appends a counter:
   ```
   report.pdf → report(1).pdf → report(2).pdf ...
   ```

---

## Getting Started

### Requirements

- Python 3.x  
- `pathlib`, `shutil`, `re` (all in standard library)

### Usage

1. Drop the script in any folder (or keep it on your desktop)
2. Run it:
   ```bash
   python desktop_sort.py
   ```
3. Your desktop gets neatly sorted.

---

## Supported File Types

- Media
  - Images: `.jpeg`, `.jpg`, `.png`
  - Video: `.mp4`, `.mpg`
  - Audio: `.mp3`, `.wav`
- Documents
  - PDFs: `.pdf`
  - Word: `.docx`
  - Excel: `.xlsx`
  - Stray Code: `.py`, `.c`, `.cpp`, `.html`, `.css`

Unrecognized files are left untouched to avoid misplacement of system or config files.

---

## Optional: Run at Startup (Windows)

You can automate this script to run every time you log in:

1. Create a `.bat` file with:
   ```bat
   @echo off
   "C:\Path\To\pythonw.exe" "C:\Path\To\desktop_sort.py"
   ```

2. Place it in the Startup folder (`Win + R` → `shell:startup`)

---

## Author

Manel Om Nayak – https://github.com/omynayak
