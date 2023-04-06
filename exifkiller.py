from PIL import Image
import os
import platform
import tkinter as tk
from tkinter import filedialog

system = platform.system()

root = tk.Tk()
root.withdraw()

print("exifkiller 1.0.0 - https://github.com/Shinryin/exifkiller")
input("Press any key to open a selection window...")
print("Select the folder that has the images you want to sanitize in them.")

if system == "Windows":
    image_dir = filedialog.askdirectory(title="Select Directory Containing Images")
elif system == "Darwin":
    image_dir = filedialog.askdirectory(title="Select Directory Containing Images", parent=root, initialdir="/")
else:
    image_dir = filedialog.askdirectory(title="Select Directory Containing Images", parent=root)

file_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".ico", ".pcx", ".tga", ".tif", ".tiff", ".webp"]

for filename in os.listdir(image_dir):
    if any(filename.lower().endswith(ext) for ext in file_extensions):
        image_path = os.path.abspath(os.path.join(image_dir, filename))
        image = Image.open(image_path)
        metadata = image.info
        image_without_metadata = Image.new(image.mode, image.size)
        image_without_metadata.putdata(list(image.getdata()))
        image_without_metadata.save(image_path)

        if metadata:
            print(f"Cleared metadata for {filename}: {metadata}")
        else:
            print(f"No metadata found for {filename}")

input("Press any key to close the program...")
