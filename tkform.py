from tkinter import *

root = Tk()
root.geometry("500x300")
def revewdata():
    print(firstnamevar.get())
    print(lastnamevar.get())
    print(fathernamevar.get())
    print(castvar.get())
    print(agevar.get())
    print(contactvar.get())

firstnamevar = StringVar()
lastnamevar = StringVar()
fathernamevar = StringVar()
castvar = StringVar()
agevar = IntVar()
contactvar = StringVar()

Label(text="Form").grid(row=0 , column=3)
Label(text="First Name").grid(row=1, column=0)
Label(text="Last Name").grid(row=2, column=0)
Label(text="Father Name").grid(row=3, column=0)
Label(text="Cast").grid(row=4, column=0)
Label(text="Age").grid(row=5, column=0)
Label(text="contact").grid(row=6, column=0)

firstnameent = Entry(root, textvariable=firstnamevar).grid(row=1, column=1)
lastnameent = Entry(root, textvariable=lastnamevar).grid(row=2, column=1)
fathernameent = Entry(root, textvariable=fathernamevar).grid(row=3, column=1)
castent = Entry(root, textvariable=castvar).grid(row=4, column=1)
ageent = Entry(root, textvariable=agevar).grid(row=5, column=1)
contactent = Entry(root, textvariable=contactvar).grid(row=6, column=1)

Button(text="Submit", command=revewdata).grid(row=7, column=1)

root.mainloop()