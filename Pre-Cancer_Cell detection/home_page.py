from turtle import color, position
from PIL import ImageTk, Image
from tkinter import *
import tkinter as tk
import PIL.Image

# Create object 
root = Tk()
  
# Adjust size 
root.geometry("590x350")


new_pic = ImageTk.PhotoImage(PIL.Image.open("D:\gp\dna-background.png").resize((2000, 1000), PIL.Image.ANTIALIAS))

# Create Canvas
canvas1 = Canvas( root, width = 400,
                 height = 600)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image=new_pic,
                     anchor = "nw")
  
# Add Text
canvas1.create_text( 750, 300, text = "Prediction Of Pre-cancer cells",font='Helvetica 50 bold',fill="white")
canvas1.create_text( 750, 400, text = "Find Out What Your DNA Says",font='Helvetica 38 bold',fill="white")
root.state('zoomed')
def cont():
    root.destroy()
    import pre_processing
   

con=tk.Button(canvas1,
    text="continue",
    font=20,
    width=15,
    height=3,
    bg="white",
    fg="black",
    
    command=cont
)

con.pack(side=BOTTOM, padx=700, pady=20)
root.mainloop()