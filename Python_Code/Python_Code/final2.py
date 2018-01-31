import PIL
import matplotlib.pyplot as plt
import os.path              

directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'black.jpg')


student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400)
axes[1].set_ylim(1100, 850)
fig.show()

earth_file = os.path.join(directory, 'shoes.jpg')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((100, 90)) 
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.show()

earth_file = os.path.join(directory, 'food.jpg')
earth_img = PIL.Image.open(earth_file)
earth_small2 = earth_img.resize((100, 90)) 
fig4, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig4.show()

earth_file = os.path.join(directory, 'fam.jpg')
earth_img = PIL.Image.open(earth_file)
earth_small3 = earth_img.resize((100, 90)) 
fig5, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig5.show()

earth_file = os.path.join(directory, 'tell.jpg')
earth_img = PIL.Image.open(earth_file)
earth_small4 = earth_img.resize((100, 90)) 
fig6, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig6.show()


student_img.paste(earth_small, (200, 200))
student_img.paste(earth_small2, (1400, 200)) 
student_img.paste(earth_small3, (2000, 200)) 
student_img.paste(earth_small4, (2000, 1400))  

fig3, axes3 = plt.subplots(1, 2)
fig4, axes3 = plt.subplots(1, 2)
fig5, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(0,100 )
axes3[1].set_ylim(480, 320)
fig3.show()