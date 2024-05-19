from ctypes.wintypes import SIZE
from tkinter import *
from tkinter import END,filedialog
  
from PIL import ImageTk, Image
import pre_cancer_detect as pre
import tkinter as tk


# Create object 
root = Tk()
  
# Adjust size 
root.geometry("590x350")


new_pic = ImageTk.PhotoImage(Image.open("dna-background.jpg").resize((2000, 1000), Image.ANTIALIAS))
img =Image.open('dna-background.jpg')
bg = ImageTk.PhotoImage(img)
# Create Canvas
canvas1 = Canvas( root, width = 400,
                 height = 600)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image=new_pic,
                     anchor = "nw")
  

root.state('zoomed')



label_file_explorer =tk.Label(canvas1,
                            text = "File Explorer using Tkinter",
                           font=20,
                           width=50,
                           height=1,
                            fg = "blue")

def browseFiles():
    global p
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)
    p=filename
    

button_explore =tk.Button(canvas1,
                        width=50,
                        height=1,
                        text = "Browse Files ",
                        font=50,
                        command=browseFiles
                        
                        )
            



def draw():
    
    train,test,error=pre.cancer(p)

    train_score=tk.Label(canvas1,text="Train Score: ",font=30)
    train_score.place(x=550,y=170)


    text_box=tk.Entry(canvas1,width=50)
    text_box.insert(END,train)
    text_box.place(x=710,y=175)
    
    
    test_score=tk.Label(canvas1,text="Test Score: ",font=30)
    test_score.place(x=550,y=220)

    text_box1=tk.Entry(canvas1,width=50)
    text_box1.insert(END,test)
    text_box1.place(x=710,y=225)
    
    


    error_score=tk.Label(canvas1,text="error Score: ",font=30)
    error_score.place(x=550,y=270)
    error_box2=tk.Entry(canvas1,width=50)
    error_box2.insert(END,error)
    error_box2.place(x=710,y=275)


button=tk.Button(canvas1,
    text="Cleaning",
    font=50,
    width=50,
    height=1,
    bg="white",
    fg="black",
    command=draw
)
def cont():
    root.destroy()
    import detection


con=tk.Button(canvas1,
    text="continue",
    font=50,
    width=50,
    height=1,
    bg="white",
    fg="black",
    command=cont
)
con.place(x=490,y=390)

button_explore.pack(side=TOP, padx=0, pady=60)
label_file_explorer.place(x=490,y=120)
button.place(x=490,y=320)

# Execute tkinter

root.mainloop()