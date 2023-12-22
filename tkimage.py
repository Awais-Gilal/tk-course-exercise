from tkinter import *
from PIL import ImageTk

root = Tk()
root.geometry("900x900")

photo = PhotoImage(file="h.png")
#for jpeg images
image = ImageTk.PhotoImage(file="halima.bmp")

label = Label(image=image)
label.pack()









root.mainloop()