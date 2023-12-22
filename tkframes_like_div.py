from tkinter import *

root = Tk()
root.geometry("600x333")
root.title("FRAMES PRACTICE GUI")

f1 = Frame(root, relief="sunken", background="red", borderwidth=6)
f1.pack(side=LEFT, padx=10, pady=20, fill=X)

label = Label(f1, text="This text is written in Frame, frames are like div tag")
label.pack(padx=10, pady=20)


root.mainloop()