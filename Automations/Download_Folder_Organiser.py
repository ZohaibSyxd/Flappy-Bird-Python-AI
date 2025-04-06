import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# Define the folder to monitor and where to move files based on their extension
downloads_folder = 'C:/Users/Zohaib/Downloads'
folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.doc', '.xlsx', '.pptx', '.txt'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar'],
    'Others': []
}

# Create folders if they don't exist
for folder in folders:
    folder_path = os.path.join(downloads_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

class DownloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            self.move_or_delete_file(event.src_path)
    
    def move_or_delete_file(self, src_path):
        # Skip processing for certain temporary files
        if src_path.endswith(('.tmp', '.crdownload')):
            logging.info(f'Skipping temporary file: {src_path}')
            return

        file_name, file_extension = os.path.splitext(src_path)
        destination_folder = None

        # Find the appropriate folder for the file extension
        for folder, extensions in folders.items():
            if file_extension.lower() in extensions:
                destination_folder = folder
                break
        if destination_folder is None:
            destination_folder = 'Others'
        
        destination_path = os.path.join(downloads_folder, destination_folder, os.path.basename(src_path))
        
        # Check if source path exists before attempting to move or delete
        if not os.path.exists(src_path):
            logging.info(f'File not found: {src_path}. Skipping.')
            return

        try:
            if os.path.exists(destination_path):
                logging.info(f'Duplicate found. Deleting: {src_path}')
                os.remove(src_path)
            else:
                logging.info(f'Moving {src_path} to {destination_path}')
                shutil.move(src_path, destination_path)
        except PermissionError as e:
            logging.error(f'PermissionError: {e}. File in use or other issue. Skipping file: {src_path}')
        except FileNotFoundError as e:
            logging.error(f'FileNotFoundError: {e}. File not found, possibly already deleted: {src_path}')
        except Exception as e:
            logging.error(f'Unexpected error: {e}. Skipping file: {src_path}')

def process_existing_files():
    for file_name in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, file_name)
        if os.path.isfile(file_path):
            logging.info(f'Processing existing file: {file_path}')
            event_handler.move_or_delete_file(file_path)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    event_handler = DownloadHandler()
    
    # Process existing files at the start
    process_existing_files()
    
    observer = Observer()
    observer.schedule(event_handler, downloads_folder, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
