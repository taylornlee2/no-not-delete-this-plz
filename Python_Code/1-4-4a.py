import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'brobro.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.show()


# Open, resize, and display earth
earth_file = os.path.join(directory, 'logo.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((60, 60)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.show()




# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (195, 430), mask=earth_small) 
# Display
fig3, axes3 = plt.subplots(1, 3)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(100, 300)
axes3[1].set_ylim(500, 400)
fig3.show()