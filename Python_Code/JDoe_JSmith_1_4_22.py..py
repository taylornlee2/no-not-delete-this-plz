# -*- coding: utf-8 -*-
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)
img = plt.imread(filename)

height = len(img)
width = len(img[0])
for row in range(405, 460):
    for column in range(130, 160):
        img[row][column] = [0, 255, 0] # red + green = yellow
img = plt.imread(filename)
  
###
# Change a region if condition is True
###
height = len(img)
width = len(img[0])
for row in range(400, 470):
    for column in range(130, 180):
        img[row][column] = [0, 255, 0] # red + green = yellow
  
height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,0] # R + B = magenta
            
if RGB
###
# Show the image data
###
# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img)
ax[1].imshow(img, interpolation='none') # Override default
img = plt.imread(filename)
  
fig.show()
