# Usage: py clahe.py

import cv2
import os
import sys
from os import path
from pathlib import Path, PureWindowsPath

target_dir = os.getcwd()
target_dir = os.path.join(target_dir, 'data_src')

#Count how many files in the directory
file_count = len(os.listdir(target_dir))

#Show some stats
print("Checking " + str(file_count) + " files")

#Setup the output directory
clahe_path = os.path.join(target_dir, 'clahe')

#Make sure the path exists and if not, create it.
if not path.isdir(clahe_path):
    try:
        os.mkdir(clahe_path)
    except OSError:
        print("Creation of the directory %s failed" % clahe_path)
    else:
        print("Successfully created the directory %s " % clahe_path)


for thisFile in os.listdir(target_dir):
    file_name = os.path.join(target_dir, thisFile)
    if os.path.isfile(file_name):

        img = cv2.imread(file_name)
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(2,2))
        img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])

        img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

        basename_without_ext = os.path.splitext(os.path.basename(file_name))[0]

        cv2.imwrite(clahe_path +  '/' + basename_without_ext + '.jpg', img)
