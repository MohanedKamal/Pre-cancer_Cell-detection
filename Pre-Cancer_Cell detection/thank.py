from turtle import color, position
from PIL import ImageTk, Image
from tkinter import *
import tkinter as tk
import PIL.Image

# Create object 
root = Tk()
  
# Adjust size 
root.geometry("590x350")

root.state('zoomed')
new_pic = ImageTk.PhotoImage(PIL.Image.open("D:\gp\dna-background.png").resize((2000, 1000), PIL.Image.ANTIALIAS))
# Create Canvas
canvas1 = Canvas( root, width = 400,
                 height = 600)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image=new_pic,
                     anchor = "nw")
  
# Add Text
canvas1.create_text( 750, 300, text = "Thank you for using Pre-Cancer Cell detector application",font='Helvetica 35 bold',fill="white")
root.mainloop()