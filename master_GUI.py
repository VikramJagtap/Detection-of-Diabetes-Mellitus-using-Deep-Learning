import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time


##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Home Page")




# #####For background Image
image2 = Image.open('12.webp')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)





lbl = tk.Label(root, text="Dibetes Mellitus Detection System", font=('times', 30,' bold '), width=65,height=2,bg="black",fg="white")
lbl.place(x=0, y=0)



#################################################################################################################
def Main():
    from subprocess import call
    call(["python","GUI_Master_DFU.py"])
def Main1():
    from subprocess import call
    call(["python","GUI_Master_old.py"])
    
def reg():
    from subprocess import call
    call(["python","analysis.py"])
def log():
    from subprocess import call
    call(["python","remedy.py"])

def window():
    root.destroy()




button5 = tk.Button(root, text="ULCER", command=Main,width=18, height=2, font=('times', 15, ' bold '),bg="black",fg="white")
button5.place(x=1150, y=250)

button5 = tk.Button(root, text="DIBETES MELLITUS", command=Main1,width=18, height=2, font=('times', 15, ' bold '),bg="black",fg="white")
button5.place(x=1150, y=350)

button5 = tk.Button(root, text="ANALYSIS", command=reg,width=18, height=2, font=('times', 15, ' bold '),bg="black",fg="white")
button5.place(x=1150, y=450)

button5 = tk.Button(root, text="REMEDY", command=log,width=18, height=2, font=('times', 15, ' bold '),bg="black",fg="white")
button5.place(x=1150, y=550)




exit = tk.Button(root, text="Exit", command=window, width=15, height=2,bg="red", font=('times', 15, ' bold '),fg="white")
exit.place(x=1170, y=650)



root.mainloop()