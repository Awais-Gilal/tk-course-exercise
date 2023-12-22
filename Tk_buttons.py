from tkinter import *

def greet():
    print("Hellow! World")
root = Tk()
root.title("Tk Buttons")
root.geometry("400x100")

f1 = Frame(root, background="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=TOP, anchor="center", pady=10)

button = Button(f1, bg="red", text="Click Me", command=greet)
button.pack(side="left", padx=3, pady=2)

button1 = Button(f1, bg="red", text="Click Me")
button1.pack(side="left", padx=3, pady=2)

button2 = Button(f1, bg="red", text="Click Me")
button2.pack(side="left", padx=3, pady=2)

button3 = Button(f1, bg="red", text="Click Me")
button3.pack(side="left", padx=3, pady=2)

root.mainloop()
