# File Organizer

A Python automation tool that automatically sorts messy folders 
into organized subdirectories based on file type.

## What it does
- Scans any folder on your computer
- Automatically categorizes files into Images, Videos, 
  Documents, Audio, Code, Archives, and Others
- Creates category folders automatically if they don't exist
- Moves every file into its correct category folder

## How to run
```bash
python file_organizer.py
```
Then enter the folder path you want to organize.

## Example
BEFORE:
Downloads/
photo.jpg
resume.pdf
song.mp3
script.py

AFTER:
Downloads/
Images/photo.jpg
Documents/resume.pdf
Audio/song.mp3
Code/script.py


## CS Concepts Demonstrated
- File system navigation (OS concept)
- Directory creation and management
- File I/O operations
- Python os and shutil modules

## Technologies Used
- Python 3
- os module
- shutil module
