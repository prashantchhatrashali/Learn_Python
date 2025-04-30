import os
import shutil
import time
from datetime import datetime


def organize_downloads(download_dir):
    """
    Automatically organizes files in the downloads directory by file type
    """
    print(f"Organizing downloads in: {download_dir}")

    # Define categories and their corresponding file extensions
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"],
        "Audio": [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
        "Executables": [".exe", ".msi", ".app", ".dmg"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".json", ".xml", ".ipynb"]
    }

    # Create category folders if they don't exist
    for category in categories:
        category_path = os.path.join(download_dir, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
            print(f"Created folder: {category}")

    # Create an 'Others' folder for uncategorized files
    others_path = os.path.join(download_dir, "Others")
    if not os.path.exists(others_path):
        os.makedirs(others_path)

    # Get all files in the downloads directory
    files = [f for f in os.listdir(download_dir) if os.path.isfile(os.path.join(download_dir, f))]

    # Counter for moved files
    moved_count = 0

    # Move each file to its corresponding category folder
    for file in files:
        file_path = os.path.join(download_dir, file)

        # Skip folders and hidden files
        if os.path.isdir(file_path) or file.startswith('.'):
            continue

        # Get the file extension
        _, extension = os.path.splitext(file)
        extension = extension.lower()

        # Find the category for this file extension
        destination_folder = others_path
        for category, extensions in categories.items():
            if extension in extensions:
                destination_folder = os.path.join(download_dir, category)
                break

        # Move the file if it's not already in a category folder
        if os.path.dirname(file_path) != destination_folder:
            # Check if file with same name already exists in destination
            destination_path = os.path.join(destination_folder, file)
            if os.path.exists(destination_path):
                # Add timestamp to filename to make it unique
                base_name, ext = os.path.splitext(file)
                timestamp = datetime.now().strftime("_%Y%m%d_%H%M%S")
                new_file_name = f"{base_name}{timestamp}{ext}"
                destination_path = os.path.join(destination_folder, new_file_name)

            try:
                shutil.move(file_path, destination_path)
                print(f"Moved: {file} -> {os.path.basename(destination_folder)}")
                moved_count += 1
            except Exception as e:
                print(f"Error moving {file}: {e}")

    print(f"\nOrganization complete! Moved {moved_count} files.")


if __name__ == "__main__":
    # Replace with your downloads directory path
    # For Windows: "C:\\Users\\YourUsername\\Downloads"
    # For Mac/Linux: "/Users/YourUsername/Downloads" or "/home/YourUsername/Downloads"
    downloads_directory = os.path.expanduser("~/Downloads")

    organize_downloads(downloads_directory)

    # Optional: Run this script automatically at regular intervals
    # Uncomment the code below to run every hour
    """
    while True:
        organize_downloads(downloads_directory)
        print("Sleeping for 1 hour before next organization...")
        time.sleep(3600)  # Sleep for 1 hour (3600 seconds)
    """