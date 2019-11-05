#!/usr/bin/env python3

import os, json, time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Rename this to whatever parent folder you want sort.
source = '/home/christine/Downloads/'

pdf_folder = os.path.join(source, "pdfs/")
images_folder = os.path.join(source, "images/")
word_folder = os.path.join(source, "word_docs/")
compressed_folder = os.path.join(source, "compressed/")
misc_folder = os.path.join(source, "misc/")


class EHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(source):
            if file.endswith(".docx") or file.endswith(".doc"):
                shutil.move(os.path.join(source, file), word_folder)
            elif file.endswith(".pdf"):
                shutil.move(os.path.join(source, file), pdf_folder)
            elif file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".gif") or file.endswith(".tiff"):
                shutil.move(os.path.join(source, file), images_folder)
            elif file.endswith(".zip") or file.endswith(".rar") or file.endswith(".tar.gz"):
                shutil.move(os.path.join(source, file), compressed_folder)
            elif not (file.startswith("pdfs") or file.startswith("images") or file.startswith("word_docs") or file.startswith("compressed") or file.startswith("misc")):
                shutil.move(os.path.join(source, file), misc_folder)


def create_folders():
    if not os.path.exists(pdf_folder):
        os.mkdir(pdf_folder)
    if not os.path.exists(images_folder):
        os.mkdir(images_folder)
    if not os.path.exists(word_folder):
        os.mkdir(word_folder)
    if not os.path.exists(compressed_folder):
        os.mkdir(compressed_folder)
    if not os.path.exists(misc_folder):
        os.mkdir(misc_folder)


# Uncomment this line if you want it to create the folders for you
#create_folders()
event_handler = EHandler()
observer = Observer()
observer.schedule(event_handler, source, recursive=True)
observer.start()

try: 
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
