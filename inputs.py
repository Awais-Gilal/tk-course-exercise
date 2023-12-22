from tkinter import *

root = Tk()
root.geometry("500x300")

def fun():
    print(f"User name is: {ent1.get()}")
    print(f"Password is: {ent2.get()}")
    
uservar = StringVar()
passwordvar = StringVar()

user = Label(text="User: ")
password = Label(text="Pass: ")
ent1 = Entry(root, textvariable=uservar)
ent2 = Entry(root, textvariable=passwordvar)

 
user.grid(column=0, row=0)
password.grid(column=0, row=1)
ent1.grid(column=1, row=0)
ent2.grid(column=1, row=1)

Button(root, text="Click Me", command=fun).grid(column=0, row=2)





root.mainloop()