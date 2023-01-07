import sys
import os
from PIL import Image, ImageFilter


# Set the directory you want to start from
rootDir = 'Pokedex'
# Create the output directory
outputDir = '../Pokedex_PNG'
if not os.path.exists(outputDir):
    os.makedirs(outputDir)

for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        # Open image
        print("Processing file:", fname)
        im = Image.open(rootDir + '/' + fname)
        print("Image opened, size =", im.size)
        # Save as png
        im.save(outputDir + '/' + fname[:-4] + "png")
        print("Image saved")
        # Close image file
        im.close()