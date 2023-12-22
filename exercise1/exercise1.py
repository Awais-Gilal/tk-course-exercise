from tkinter import *
from PIL import ImageTk
import os

files_list = os.listdir()

root = Tk()
root.geometry("999x999")

images_list = []

for file in files_list:
    if "." in file and not file.endswith(".py"):
        img = ImageTk.PhotoImage(file=file)
        images_list.append(img)

root.mainloop()