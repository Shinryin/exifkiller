# exifkiller
Easy multi-platform tool to remove all metadata (including EXIF) from images &amp; GIFs in bulk.
This program supports (JPG, JPEG, PNG, BMP, GIF, ICO, PCX, TGA, TIF, TIFF, and WebP) in a selected directory using the Python Imaging Library (Pillow).

# Installation
- Head over to releases and install exifkiller.zip, this is standalone version made with Nuitka. 
- All you need to do then is run exifkiller.exe - and the program will run!
- OR, you can build the program if you'd like:
- Install Python (version 3.6 or later).
- Install the Pillow library by running pip install pillow in your terminal or command prompt.
- Save the above code as a Python file with the name image_metadata_remover.py.
- Run the file in your terminal or command prompt by typing python image_metadata_remover.py.

# Usage
A file selection dialog will appear. Select the directory containing the images you want to remove metadata from.
The program will iterate over all image files in the selected directory and remove their metadata.
If metadata was cleared from an image file, the program will print a message indicating the filename and basic information about metadata that was removed.
You can then press any key to close the program. 
