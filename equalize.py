from PIL import Image, ImageOps
import os
import sys
from os import path
from pathlib import Path, PureWindowsPath

# Usage: py equalize.py

target_dir = os.getcwd()
target_dir = os.path.join(target_dir, 'data_src')
target_dir = os.path.join(target_dir, 'aligned')

file_count = len(os.listdir(target_dir))

print("Checking " + str(file_count) + " files")

equalize_path = os.path.join(target_dir, 'equalize')

if not path.isdir(equalize_path):
    try:
        os.mkdir(equalize_path)
    except OSError:
        print("Creation of the directory %s failed" % equalize_path)
    else:
        print("Successfully created the directory %s " % equalize_path)


for thisFile in os.listdir(target_dir):
    file_name = os.path.join(target_dir, thisFile)
    if os.path.isfile(file_name):
        file_name = os.path.join(target_dir, thisFile)

        im = Image.open(file_name)

        if im.format == "JPEG":
            im = im.convert("YCbCr")
            yy, cb, cr = im.split()

            yy = ImageOps.equalize(yy);
            im = Image.merge("YCbCr", (yy, cb, cr))

            im = im.convert("RGB")

            basename_without_ext = os.path.splitext(os.path.basename(file_name))[0]
            im.save(equalize_path + '/' + basename_without_ext + '.jpg', quality=100)
