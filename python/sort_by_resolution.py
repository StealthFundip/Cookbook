"""
This is a quick python script to loop through a folder and 
copy images with a specific resolution to another folder.  

Dependencies: Pillow
Install using "pip3 install pillow" 

Created by Nicolai Johnson 2018/12/21
"""

from PIL import Image  #image info/manipulation 
import os 
from shutil import copy 

#Constants
#WIDTH should be the longest side of your image, regardless of orientation
WIDTH = 2560
HEIGHT = 1440
sourceFolder = "C:\\path\\to\\source\\folder\\"
destinationFolder = "C:\\path\\to\\destination\\folder\\"

#loop through picture folder
for filename in os.listdir(sourceFolder):
    image = Image.open(sourceFolder + filename)
    print(image.size)
    if (image.size == (WIDTH, HEIGHT)):
        #copy picture to new folder
        print("Image found! Moving to destinationFolder")
        copy(sourceFolder + filename, destinationFolder)
print("Done! Closing script")