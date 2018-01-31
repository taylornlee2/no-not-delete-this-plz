#####
# color_string_changer.py
# 
# Creates two Scales and a Text view. Updates Text based on the Scales
# 
# (c) 2013 PLTW
# version 11/1/2013
####

import Tkinter # Often people import Tkinter as *


def hexstring(slider_intvar):
    '''A function to prepare data from controller's widget for view's consumption
    
    slider_intvar is an IntVar between 0 and 255, inclusive
    hexstring() returns a 2-character string representing a value in hexadecimal
    '''
    # Get an integer from an IntVar
    slider_int = slider_intvar.get()
    # Convert to hex
    slider_hex = hex(slider_int)
    # Drop the 0x at the beginning of the hex string
    slider_hex_digits = slider_hex[2:] 
    # Ensure two digits of hexadecimal:
    if len(slider_hex_digits)==1:
        slider_hex_digits = '0' + slider_hex_digits 
    return slider_hex_digits
#####
# Create root window 
####

root = Tkinter.Tk()
root.wm_title('Hexadecimal Explorer')

#####
# Create Model
######
# Create two IntVar's and initialize them to 127
red_intvar = Tkinter.IntVar() 
red_intvar.set(127) 
green_intvar = Tkinter.IntVar()
green_intvar.set(127)
blue_intvar = Tkinter.IntVar()
blue_intvar.set(127)

color = '#'+ hexstring(blue_intvar) + hexstring(red_intvar) + hexstring(green_intvar)



######
# Create Controller
#######
# Event handler for slider


canvas = Tkinter.Canvas(width = 400, height = 400, background = 'white')
canvas.grid(row = 0, column = 1, rowspan = 3)
def color_changed(new_intval):
    # Controller updates the view by pulling data from model
    editor.insert(Tkinter.END, '#' + \
                               hexstring(red_intvar) + \
                               hexstring(green_intvar) + \
                               hexstring(blue_intvar) + '\n')
    editor.see(Tkinter.END) # scroll the Text window to see the new bottom line
    canvas.itemconfig(circle, fill = '#' + \
                               hexstring(red_intvar) + \
                               hexstring(green_intvar) + \
                               hexstring(blue_intvar))
        
circle=canvas.create_oval(20,20,120,120, outline = 'black', fill = color)

            
# Instantiate and place sliders


red_slider = Tkinter.Scale(root, from_=0, to=255, variable=red_intvar, 
                           orient=Tkinter.HORIZONTAL,   
                           label='Red', command=color_changed)
red_slider.grid(row=1, column=0, sticky=Tkinter.E)
green_slider = Tkinter.Scale(root, from_=0, to=255, variable=green_intvar,  
                             orient=Tkinter.HORIZONTAL,
                             label='Green', command=color_changed)
green_slider.grid(row=2, column=0, sticky=Tkinter.E)
blue_slider = Tkinter.Scale(root, from_=0, to=255, variable=blue_intvar,  
                             orient=Tkinter.HORIZONTAL,
                             label='Blue', command=color_changed)
blue_slider.grid(row=3, column=0, sticky=Tkinter.E)


# Create and place directions for the user
text = Tkinter.Label(root, text='Drag slider \nto adjust\ncolor code.')
text.grid(row=0, column=0)

######
# Create View
#######
# Create a text editor window for displaying information
editor = Tkinter.Text(root, width=10)
editor.grid(column=1, row=0, rowspan=3)

######
# Function to convert IntVar data from Scale widget to two hex digits as string
# for a Canvas widget color argument
#######



#######
# Event Loop
#######
root.mainloop()