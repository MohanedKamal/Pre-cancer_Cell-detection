from tkinter import filedialog
from turtle import position
from PIL import ImageTk, Image
from tkinter import *
import tkinter as tk
import PIL.Image
import pre_cancer_detect as pre

# Create object 
root = Tk()

new_pic = ImageTk.PhotoImage(PIL.Image.open("D:\gp\dna-background.png").resize((2000, 1000), PIL.Image.ANTIALIAS))



label = tk.Label(root, image=new_pic)
label.place(x = 0,y = 0)


file=tk.Label(root,text="Patient File:",width=11,font=30)
file.place(x=500,y=290)

mutatnt=tk.Label(root,text="Mutatnt:",font=50,width=11)
mutatnt.place(x=500,y=350)

text_box1=tk.Entry(root,width=30,font=100)
def browseFiles():
    global p
    global x
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    label_file_explorer.configure(text="File Opened: "+filename)
    p=filename
    x=pre.test(p)
    print(x)
    text_box1.insert(END,x)

button_explore =tk.Button(root,
                        text = "Browse Files",
                        width=11,
                        height=1,
                        font=1,
                         bg="white",
                        fg="black",
                        command=browseFiles
                        )
button_explore.place(x=500,y=240)
text_box1.place(x=650,y=350)


def cont():
    root.destroy()
    import thank

con=tk.Button(root,
    text="continue",
    font=50,
    width=43,
    height=1,
    bg="white",
    fg="black",
    
    command=cont
)
con.place(x=500,y=420)

def back():
    root.destroy()
    import pre_processing

bac=tk.Button(root,
    text="Back",
    font=50,
    width=43,
    height=1,
    bg="white",
    fg="black",
    command=back
)
bac.place(x=500,y=480)

label_file_explorer =tk.Label(root,
                            text = "File Explorer using Tkinter",
                           font=20,
                           width=30,
                           height=1,
                            fg = "blue")

label_file_explorer.place(x=650,y=290)

root.state('zoomed')
root.mainloop()