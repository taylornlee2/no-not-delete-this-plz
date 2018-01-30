import PIL
import PIL.ImageDraw
import matplotlib.pyplot as plt
import os.path              

def function (side_thickness, color):
    color = color
    directory = os.path.dirname(os.path.abspath(__file__)) 
    student_file = os.path.join(directory, 'sean.png')
    student_img = PIL.Image.open(student_file)
    width, height = student_img.size
    frame = PIL.Image.new ("RGB" , (width + 2*side_thickness, height + 2* side_thickness) , color)
    frame.paste (student_img, (side_thickness, side_thickness), mask = None)
    new_directory = os.path.join(directory, 'built')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    new_image_filename = os.path.join(new_directory,  'sean1.png')
    frame.save(new_image_filename)   



def fun (side_thickness, color):
    color = color
    directory = os.path.dirname(os.path.abspath(__file__)) 
    var = os.listdir (directory)
    print (var)
    images = []
    for i in var:
        if '.jpg' in i:
            images += [i] 
    print images
            
    
    for image in images:
        PILimage = PIL.Image.open(image)
        width, height = PILimage.size
        var1 = PIL.Image.new ('RGBA', (width,height),(255,0,0,0))
        drawing_layer = PIL.ImageDraw.Draw(var1)
        drawing_layer.rectangle ([(height/1,0),(0,width/3)],
                            fill=(0,255,255,255),outline=None)
        result = PIL.Image.new('RGB', PILimage.size, color)
        result.paste(PILimage, (0,0), mask=var1)
        new_directory = os.path.join(directory, 'Newfile')
        try:
            os.mkdir(new_directory)
        except OSError:
            pass # if the directory already exists, proceed 
            new_image_filename = os.path.join(new_directory, image + '.jpg')
            result.save(new_image_filename)    