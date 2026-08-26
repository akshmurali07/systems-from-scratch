import os
import shutil

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

def get_category(extension):
    for category, extensions in categories.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    files_moved = 0

    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)

        if os.path.isdir(filepath):
            continue

        _, extension = os.path.splitext(filename)
        if not extension:
            continue

        category = get_category(extension)
        category_path = os.path.join(folder_path, category)
        os.makedirs(category_path, exist_ok=True)

        new_path = os.path.join(category_path, filename)
        shutil.move(filepath, new_path)
        print(f"✅ Moved: {filename} → {category}/")
        files_moved += 1

    print(f"\nDone! {files_moved} files organized.")

folder = input("Enter folder path (e.g. C:\\Users\\dell\\Downloads): ")
organize_folder(folder)