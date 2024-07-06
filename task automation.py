import os
import shutil
from pathlib import Path

# Define the directory to be organized
directory_to_organize = "path/to/your/directory"

# Define file type categories and their corresponding extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".rb", ".sh", ".bat"],
    "Others": []
}

def organize_files(directory):
    # Create directories for each file type category if they don't exist
    for category in file_types.keys():
        category_path = Path(directory) / category
        category_path.mkdir(exist_ok=True)

    # Move files into their corresponding directories
    for file in Path(directory).iterdir():
        if file.is_file():
            moved = False
            for category, extensions in file_types.items():
                if file.suffix.lower() in extensions:
                    shutil.move(str(file), str(Path(directory) / category / file.name))
                    moved = True
                    break
            # If file type is not recognized, move it to the 'Others' directory
            if not moved:
                shutil.move(str(file), str(Path(directory) / "Others" / file.name))

if __name__ == "__main__":
    organize_files(directory_to_organize)
    print("Files organized successfully.")
