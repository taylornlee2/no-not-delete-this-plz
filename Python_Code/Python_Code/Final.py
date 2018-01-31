import random
def guess():
    var1 = raw_input("Please type another number     ")
    var2 = raw_input("Please type another number     ")
    var3 = raw_input("Please type another number     ")
    var4 = raw_input("Please type another number     ")
    var5 = raw_input("Please type another number     ")
    var6 = raw_input("Please type another number     ")
    var7 = raw_input("Please type another number     ")
    var8 = raw_input("Please type another number     ")
    var9 = raw_input("Please type another number     ")
    var10 = raw_input("Please type another number    ")
    print (var1, var2, var3, var4, var5, var6, var7, var8, var9, var10)
    final = random.choice([var1,var2,var3,var4,var5,var6,var7,var8,var9,var10])
    print final
    


import PIL
import matplotlib.pyplot as plt
import os.path              

directory = os.path.dirname(os.path.abspath(__file__))  
black_file = os.path.join(directory, 'black.jpg')
fam_file = os.path.join(directory, 'fam.jpg')
food_file = os.path.join(directory, 'food.jpg')
tell_file = os.path.join(directory, 'tell.jpg')
shoes_file = os.path.join(directory, 'shoes.jpg')

img_black = PIL.Image.open(black_file)
img_fam = PIL.Image.open(fam_file)
img_food = PIL.Image.open(food_file)
img_tell = PIL.Image.open(tell_file)
img_shoes = PIL.Image.open(shoes_file)

img_tell= img_tell.resize ((1300,600))
img_shoes= img_shoes.resize((800,800))
img_food= img_food.resize ((600,800))
img_fam= img_fam.resize ((1000,1000))

img_black.paste(img_tell, (200,50))
img_black.paste(img_shoes, (650,700))
img_black.paste(img_food, (0,800))
img_black.paste(img_fam, (1500,400))
fig, ax = plt.subplots (1,1)

ax.imshow(img_black)
fig.show()