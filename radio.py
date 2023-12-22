from tkinter import *

def data():
    print(var.get())

root = Tk()
root.geometry("400x400")
root.title("Radio Buttons")

Label(text="Select courses", justify=CENTER, font="lucida 23 bold").pack(padx=23)

var = IntVar()
var.set(00)
r1 = Radiobutton(root, text="python", value=1).pack(anchor=W)
r2 = Radiobutton(root, text="Java", value=2).pack(anchor=W)
r3 = Radiobutton(root, text="Ruby", value=3).pack(anchor=W)
r4 = Radiobutton(root, text="Swift", value=4).pack(anchor=W)
r5 = Radiobutton(root, text="C++", value=5).pack(anchor=W)a
r6 = Radiobutton(root, text="java script", value=6).pack(anchor=W)
r7 = Radiobutton(root, text="html", value=7).pack(anchor=W)
r8 = Radiobutton(root, text="css", value=8).pack(anchor=W)

Button(root, text="check", command=data).pack(anchor=W)

root.mainloop()