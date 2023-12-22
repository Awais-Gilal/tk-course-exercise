from tkinter import *

root = Tk()
root.geometry("500x300")

def fun():
    print(uservar.get())
    print(passvar.get())
    print(gender.get())
    
    

uservar = StringVar()
passvar = StringVar()
gender = BooleanVar()

Label(root, text="User:").grid(row=0, column=0)
Label(root, text="Pass:").grid(row=1, column=0)
Label(root, text="Gender").grid(row=2, column=0)

userent = Entry(root, textvariable=uservar)
passent = Entry(root, textvariable=passvar)
genderent = Checkbutton(root, variable=gender)

userent.grid(row=0, column=1)
passent.grid(row=1, column=1)
genderent.grid(row=2, column=1)



Button(root, text="Click Me", command=fun).grid(row=3, column=1)


root.mainloop()