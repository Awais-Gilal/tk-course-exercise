from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Menues")

def fun(x):
    print(f"clicked on {X}")


filemenu = Menu(root)

file = Menu(filemenu)
file.add_command(label="New")
file.add_separator()
file.add_command(label="Save")

filemenu.add_cascade(label="file", menu=file)


root.config(menu=filemenu)
root.mainloop()
